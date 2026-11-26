# FSO field report — coordinator inbox

**Role:** Local agent appends observed evidence here; coordinator reads it and issues the next task in FSO-COORDINATION.md. This is the single report inbox on FSO-assignment. Public-safe summaries only; no private records, personal identifiers, credentials, raw student data, or proprietary course materials. Never write to another branch for this task.

## Report R-000 — baseline, 2026-11-25
- **Who:** Coordinator (repository review only); local student/operator and field AI (runtime evidence not yet returned).
- **What:** IDB Lab 1; draft deliverables and ZIP integrity were previously reported, but no actual SQL execution or restore is established.
- **When:** Historical checkpoint 2026-11-25; latest local runtime timestamp UNKNOWN.
- **Where:** Quasar; existing MySQL Workbench workspace; exact local details stay in the authorized conversation.
- **Why:** Complete the instructor's actual requirements with genuine results; avoid repeating setup or treating a draft as proof.
- **Done:** Workspace creation, source extraction, MySQL installation and successful connection reported; source inspection reported.
- **Not done / unknown:** Current schema/table state, successful import, live Q2–Q6, final export/restore, written reconciliation and LMS receipt.
- **Next:** Execute dispatch D-001 from FSO-COORDINATION.md. No fresh local observations have been made by the coordinator.

## Field agent append template (one report per meaningful task result)
Aim for 100–180 words; do not omit critical evidence. Replace placeholders; do not copy prior reports. Report a blocked attempt immediately rather than inventing completion.

```md
### R-<next> | D-<dispatch> | <date/time + zone>
- Who: local agent / student operator; who actually ran the action
- What: assigned task; command/action; actual result (redacted)
- When: actual observation timestamp, or UNKNOWN
- Where: confirmed machine role, application/shell, schema/workspace (public-safe)
- Why: rubric item or prerequisite being verified
- Done: exact verified or reported milestones; affected count/exit status where applicable
- Evidence: OBSERVED / USER_REPORTED / UNKNOWN / BLOCKED; public-safe command/result summary; keep sensitive proof in authorized chat
- Blocked / not done: first actual error, missing evidence, remaining task
- Next: single concrete action or question for coordinator; acceptance check
```

Append with current blob SHA and verify original bytes preserved, new report appears once, commit touches only this file. Do not edit previous reports or instructions. If safe write cannot be performed, return the completed report in the current chat marked NOT COMMITTED. No automatic notification or cross-chat execution is implied.
