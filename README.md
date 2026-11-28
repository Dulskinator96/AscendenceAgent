# Incremental versus full-state verification benchmark

**Start here. This branch is dedicated to deterministic transition verification.** Contributors can propose or implement cases directly. No codename exercise, AI-to-AI transfer, gate demonstration, model, API key, or knowledge-transfer prerequisite is required. The separate collaboration branch remains unchanged.

## Research question
On identical deterministic state-transition sequences, can an affected-constraint verifier detect the same inconsistencies as full-state verification, at lower computational cost? This is a question to test, not an established result.

- **Full-state:** evaluate every active constraint after each transition.
- **Incremental:** reevaluate constraints affected by changed fields and constraint/dependency edits; maintain the complete violation set, including unchanged violations.
- Both receive the same initial state, rules and transitions. Manually specified expected violation sets after every transition are a third reference, not derived from either algorithm. A shared predicate implementation is a limitation: agreement alone cannot prove correctness.

## Initial cases — open for joint review
| Case | Required behavior |
|---|---|
| Reversal | Detect a violation, clear it when reversed, detect it again. |
| Persistent violation | Retain earlier violations across unrelated edits. |
| Dependency change | Remove stale dependency edges, evaluate changed constraints even without a state write, track new edges. |
| Conflicting transitions | Report all simultaneous inconsistencies and subsequent repairs. |
| Constraint addition/removal | Evaluate new rules, remove stale violations and track reintroduced rules. |

These five starter cases are proposed, not collaborator-approved or blind holdouts. Add cases before optimizing and agree on the expected sets independently. Preserve previous cases and failed runs. The pilot uses atomic, serial patches to a fixed set of integer fields and pure two-field constraints (`<=`, `==`); malformed input, concurrency, derived/transitive dependencies, and general constraint languages are outside this initial scope. If those become relevant, define new cases jointly.

## Run
Python 3, standard library only, from the repository root:

```sh
python benchmark/transition_benchmark.py
```

The report shows per-transition expected/actual violation sets, false-positive and false-negative counts, exact-step counts, constraint evaluations (including initialization), initialization and transition timing. Nonzero exit on a missed expected set. No existing agent services need to run.

## Initial reproducible pilot
Code commit `3e253bc3e3a51a055ded9ed27509c34a86b7e0d2`, file blob `91443f7f828eba49433da0dc6979979cd72cf98e`. A byte-matched local copy was executed with Python 3.13.5.

| Metric | Full-state | Incremental |
|---|---:|---:|
| Exact transitions | 18/18 | 18/18 |
| False positives (constraint-step) | 0 | 0 |
| False negatives (constraint-step) | 0 | 0 |
| Predicate evaluations including setup | 69 | 40 |

29 fewer evaluations on these authored fixtures (~42%). This is not a speedup claim. Single-run elapsed transition times were 83,143 ns full and 92,490 ns incremental; initialization 14,523 ns and 19,620 ns respectively. Timings include input copying and are noisy, with fixed execution order, tiny states, no repetitions and no memory measurements. Incremental indexing incurs overhead. Neither general correctness nor a performance advantage is established.

## Contributing
Fork or branch from this benchmark branch, submit a PR targeting `incremental-verification-benchmark`. Start with deterministic cases, explicit transitions and independently reasoned expected violations. Proposed next phase: mutually freeze the initial cases, include independent holdouts, compare repeated runs at different state sizes, dependency fan-out and mutation rates, and measure setup, checking, update overhead, total time and memory separately. Report negative as well as positive results. No changes to the agent or the other collaboration workflow are required.

---

## Original repository README (preserved)
# AscendenceAI: Learning Agent Core

Run locally or deploy via Render. Edit `.env` with your API keys.
"# AscendenceAgent" 
