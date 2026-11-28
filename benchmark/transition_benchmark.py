"""Deterministic transition benchmark: reference pilot, Python standard library only."""
from copy import deepcopy
from time import perf_counter_ns
import json

# Each constraint reads two named integer fields. Constraints are immutable tuples.
BASE = {"x": 1, "y": 3, "z": 5, "w": 5}
RULES = {"xy": ("x", "<=", "y"), "yz": ("y", "<=", "z"),
         "zw": ("z", "==", "w")}
# Expected sets are manually specified, not obtained from either verifier.
# Steps: state patch, constraint edits (None = removal), expected violations.
CASES = {
    "reversal": [
        ({"x": 4}, {}, ["xy"]),
        ({"x": 1}, {}, []),
        ({"x": 4}, {}, ["xy"]),
    ],
    "persistent_violation": [
        ({"x": 4}, {}, ["xy"]),
        ({"w": 6}, {}, ["xy", "zw"]),
        ({"w": 5}, {}, ["xy"]),
    ],
    "dependency_change": [
        ({"x": 4}, {}, ["xy"]),
        ({}, {"xy": ("x", "<=", "z")}, []),
        ({"y": 0}, {}, []),
        ({"z": 3}, {}, ["xy", "zw"]),
        ({"z": 5}, {}, []),
    ],
    "conflicting_transitions": [
        ({"x": 7, "y": 6}, {}, ["xy", "yz"]),
        ({"x": 2, "z": 7, "w": 7}, {}, []),
        ({"y": 1}, {}, ["xy"]),
    ],
    "add_remove_constraint": [
        ({"x": 4}, {"extra": ("x", "==", "y")}, ["extra", "xy"]),
        ({}, {"extra": None}, ["xy"]),
        ({}, {"xy": None}, []),
        ({}, {"xy": ("x", "<=", "y")}, ["xy"]),
    ],
}

def violated(state, rule):
    a, op, b = rule
    if op == "<=":
        return state[a] > state[b]
    if op == "==":
        return state[a] != state[b]
    raise ValueError("Unsupported constraint")

def apply(state, rules, patch, edits):
    state.update(patch)
    for name, rule in edits.items():
        if rule is None:
            del rules[name]
        else:
            rules[name] = rule

class Full:
    def __init__(self):
        self.state = dict(BASE)
        self.rules = dict(RULES)
        self.bad = self.scan()
        self.initial_checks = len(self.rules)

    def scan(self):
        return {name for name, rule in self.rules.items()
                if violated(self.state, rule)}

    def step(self, patch, edits):
        apply(self.state, self.rules, patch, edits)
        self.bad = self.scan()
        return set(self.bad), len(self.rules)

class Incremental:
    def __init__(self):
        self.state = dict(BASE)
        self.rules = dict(RULES)
        self.index = {}
        self.bad = set()
        self.initial_checks = len(self.rules)
        for name, rule in self.rules.items():
            self.add_index(name, rule)
            if violated(self.state, rule):
                self.bad.add(name)

    def add_index(self, name, rule):
        for field in {rule[0], rule[2]}:
            self.index.setdefault(field, set()).add(name)

    def remove_index(self, name, rule):
        for field in {rule[0], rule[2]}:
            self.index[field].remove(name)
            if not self.index[field]:
                del self.index[field]

    def step(self, patch, edits):
        # Collect affected rules using OLD dependency edges before edits.
        changed = {k for k, v in patch.items() if self.state[k] != v}
        affected = set(edits)
        for field in changed:
            affected.update(self.index.get(field, ()))
        for name in edits:
            if name in self.rules:
                self.remove_index(name, self.rules[name])
            self.bad.discard(name)
        apply(self.state, self.rules, patch, edits)
        for name, rule in edits.items():
            if rule is not None:
                self.add_index(name, rule)
        # NEW edges matter too, including a changed constraint with no state write.
        for field in changed:
            affected.update(self.index.get(field, ()))
        checks = 0
        for name in sorted(affected):
            if name in self.rules:
                checks += 1
                if violated(self.state, self.rules[name]):
                    self.bad.add(name)
                else:
                    self.bad.discard(name)
        # Return the whole violation set, including untouched violations.
        return set(self.bad), checks

def run():
    totals = {name: {"checks": 0, "false_positive": 0, "false_negative": 0,
                     "exact_steps": 0, "elapsed_ns": 0, "init_ns": 0}
              for name in ("full", "incremental")}
    rows = []
    for case, steps in CASES.items():
        engines = {}
        for name, cls in (("full", Full), ("incremental", Incremental)):
            start = perf_counter_ns()
            engine = cls()
            totals[name]["init_ns"] += perf_counter_ns() - start
            totals[name]["checks"] += engine.initial_checks
            assert engine.bad == set(), "Unexpected initial violation"
            engines[name] = engine
        for i, (patch, edits, expected) in enumerate(steps, 1):
            row = {"case": case, "step": i, "expected": expected}
            for name, engine in engines.items():
                start = perf_counter_ns()
                actual, checks = engine.step(deepcopy(patch), deepcopy(edits))
                elapsed = perf_counter_ns() - start
                record = totals[name]
                record["elapsed_ns"] += elapsed
                record["checks"] += checks
                record["false_positive"] += len(actual - set(expected))
                record["false_negative"] += len(set(expected) - actual)
                record["exact_steps"] += int(actual == set(expected))
                row[name] = {"violations": sorted(actual), "checks": checks}
            rows.append(row)
    return {"cases": len(CASES), "steps": len(rows), "totals": totals,
            "rows": rows, "note": "Single-run timings are descriptive only; checks include initialization."}

if __name__ == "__main__":
    report = run()
    print(json.dumps(report, indent=2))
    raise SystemExit(0 if all(v["exact_steps"] == report["steps"]
                              for v in report["totals"].values()) else 1)
