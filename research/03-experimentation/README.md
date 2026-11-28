# Phase 3 — Reproducible experiments

**Status: NOT STARTED.** Do not treat a template or a successful software test as a study outcome. Await an agreed [protocol](../02-methodology/README.md).

## Reproduction plan
Once the methodology is agreed, add the actual permitted datasets or acquisition instructions, runnable scripts, dependency versions, exact commands, and documented environment in this phase. Prefer free/local tooling unless jointly agreed otherwise. Pilot using development cases to check harness behavior and logging; keep evaluation cases unseen. No test data, executable framework or recorded run exists yet.

## Run record (one per real run)
- Run ID, timestamp, protocol and code commit:
- Dataset/source versions or hashes; partition and case IDs:
- Model/version/configuration, prompts, input artifacts, seed if applicable:
- Runtime environment, commands, intervention/arm and pass order:
- Raw outputs and external verification references:
- Reviewer decisions with criterion IDs, exclusions and failures:
- Latency, token/compute use and applicable costs:
- Reproduction instructions and differences from protocol:

Retain initial and revised artifacts, negative results, errors and incomplete runs. Record observed versus asserted state. A hash proves byte identity, not correctness. Publish only authorized public-safe material; keep held-out labels and confidential materials outside the public branch.

## Ready to proceed when
The agreed study has actual execution records, data provenance, independently assessed outputs, and a reproducible path. Report missing runs rather than inventing them. Freeze the analysis input snapshot.
