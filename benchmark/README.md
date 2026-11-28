# Deterministic transition verification — research compartment

## Purpose
A small, self-contained workspace for joint investigation of explicit state tracking under updates, reversals, exceptions and changing dependencies. The initial question is whether incremental constraint verification preserves the detection behavior of full-state verification while reducing work. Neither correctness beyond the tested domain nor a speed advantage is assumed.

This is a benchmark-first collaboration. No codename, AI-to-AI transfer, gate exercise, agent installation, paid service or prior integration with the main application is required. Contributors can work directly on deterministic cases. This document describes the research scope, not any contributor's personal background or affiliation.

## Existing executable starting point
- `transition_benchmark.py`: full-state and affected-constraint reference implementations, five proposed cases, and manually specified expected violation sets.
- Frozen initial code: [3e253bc](https://github.com/Dulskinator96/AscendenceAgent/commit/3e253bc3e3a51a055ded9ed27509c34a86b7e0d2).
- Run from the repository root: `python benchmark/transition_benchmark.py`.
- Initial pilot: 18/18 exact steps for each verifier; 69 versus 40 predicate evaluations including setup. This is a bounded authored-fixture result, not independently validated general correctness or a speedup. See the branch README for timing and limitations.

## First joint task: agree on the transition cases
The current starter cases are proposals. Review or replace the initial suite by mutual agreement before making performance claims. Each proposed case should state:
1. Initial state and active constraint definitions, with explicit dependency fields.
2. Ordered transitions, including state updates and rule/dependency edits; define whether each transition is atomic.
3. Expected post-transition state, active constraints, and complete violation set after every step, derived independently of either verifier.
4. The invariant or failure mode the case is intended to discriminate and any assumption about exceptional transitions.
5. Whether the case fits the existing runner or needs a separately agreed extension.

Start with reversals, persistent violations across unrelated changes, dependency changes and conflicting updates. Exceptions and rejected transitions are a useful next research question: agree on rejection/rollback semantics and expected unchanged or changed state before implementing them. Do not silently assume transaction or concurrency semantics.

### Example of a directly runnable contribution
The current runner uses a shared initial state `x=1, y=3, z=5, w=5` and rules `xy: x<=y`, `yz: y<=z`, `zw: z==w`. A contributor can add a new named entry to `CASES` in the existing Python file. Each row is `(state_patch, constraint_edits, expected_violation_ids)`; edits map a rule name to a replacement tuple or `None` for removal. For example, a proposed no-op-after-violation case:

```python
"no_op_after_violation": [
    ({"x": 4}, {}, ["xy"]),
    ({"x": 4}, {}, ["xy"]),
    ({"x": 1}, {}, []),
],
```

Expected states in order: `{x:4,y:3,z:5,w:5}`, the same state again, then the original state; rules unchanged. This is an illustrative proposed case, not an added or executed fixture. The present runner checks violation sets, not independent complete post-state equality. If a case needs a different initial state, a richer constraint type or rejection semantics, propose it first rather than forcing it into the existing fixed-state interface.

## Evidence and comparison protocol
- Freeze the accepted cases, expected results and verifier revisions before comparison. Keep independently authored holdouts separate from development cases; do not tune against their expected answers.
- Compare each verifier with the independently derived expected result, not merely with each other. A shared predicate can cause a shared error. For the current pilot, exact violation sets are the acceptance criterion; full post-state and rule-set checks are a proposed extension.
- Record false positives and false negatives separately, per-step exactness, constraint evaluations, initialization, dependency-index updates, total transition time and memory where measured. Count the cost of maintaining the incremental index. Preserve failures and timeouts.
- Correctness first; then repeat timing runs across state size, change locality, mutation rate and dependency fan-out. Include dense/worst-case updates where incremental checking may not help. Keep workloads, environment, and measurement boundaries identical and record revisions and raw results. Do not use one tiny timing run as a speedup claim.
- Keep the current restricted domain explicit: serial atomic patches, fixed integer fields, pure two-field equality/inequality constraints. No general solver, transitive dependency engine, probabilistic model or distributed transaction guarantee is established.

## Collaboration
Open a case proposal in an issue or submit a pull request directly to `incremental-verification-benchmark` with the transition sequence, expected results and rationale. A suitable first PR is one independently specified deterministic case. No code change is necessary to propose a case. Review expected outcomes together before changing the algorithms or broadening the scope. Retain authorship and attribution through the ordinary Git history; no additional identity exercise.

Keep this compartment independent of the agent runtime and other research branches. Future integrations are separate decisions after evidence, not part of this initial benchmark.
