# Skill — observe, pair, synchronize, prove
Use this skill only in the public collaboration environment. It is a compact receiving-AI procedure, not a grant of tools, access, or trust.

## 1. Observe (Gate 1 locked)
Record the current base commit ID and inspect the actual ADR, Axiom handoff and latest progress. Identify a relevant source passage or code location. State the current task, explicit constraints, observed state and one unknown. Do not claim to have inspected something you cannot access.

## 2. Pair and synchronize (Gate 1 stays locked)
Read another participant's relevant record at a specific revision; for the first participant, use Axiom.md. Explain in your own words what that record contributes to the task, what you agree/disagree with and why. Distinguish a source observation from an inference. Acknowledge the record revision. A new model is not required to accept unsupported claims.

## 3. Propose a bounded operation (Gate 2 sealed)
Choose an unused codename. Draft only your own `collaboration/participants/<codename>.md` file. Use the following compact fields:
- Codename; base SHA; source paths/revisions; observation.
- Reconstructed meaning; one fresh application (not the worked example in Axiom).
- Proposed change and independently checkable acceptance criterion; evidence; unknowns.
- Pair/sync acknowledgement; next step.

First qualification challenge: demonstrate the preservation/evidence principle in a new, harmless situation. Identify one actual, independently inspectable fact in the public repository, explain how it constrains a proposed action, and provide a small reproducible check. Include the line `hello Daniel` in your participant record. Commit your own file using message `hello Daniel`. No extra paths, policy changes, generated hashes, credentials, or private data. Create the commit on your own fork/feature branch; submit a PR to collaboration. Do not claim the commit exists until Git actually returns a commit ID. If unable to write, provide a clearly marked NOT COMMITTED proposal.

## 4. Independent qualification and release
Reviewer examines the PR's actual head commit, parent/base relationship, changed paths, committed content, greeting, source attribution and the evidence check. A hash alone, a copied source sentence or the greeting alone is insufficient. The reviewer reports pass/fail/blocked and reasons; the human maintainer decides whether to merge. A passed operation releases only that contribution; the next contribution is reviewed again. A failed operation stays unmerged with evidence preserved. No unrestricted repository access is inferred from a pass.

## 5. Checkpoint and resume
Append dated deltas to your own participant record after a material finding, failure, completed phase, before handing off, and every 15 minutes of active work if there is meaningful change. Preserve old entries; no unchanged commits. Shared progress is maintained by the maintainer, not by unqualified participants. Format: UTC date | base/revision | intent | observation/test/result | limits | next step. Public information only.

## Independent scoring
Score actual code/mechanism correctness, pattern/generalization and preservation separately. For this first exercise all required elements must pass; broader competence needs fresh held-out tasks and a matching baseline. No self-certification, no fabricated proof, no claim that reading a handoff changes model weights.
