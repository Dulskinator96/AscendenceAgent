# FSO coordination — active task and AI handoff

**As of:** 2026-11-25 | **Task:** IDB Activity 1.2 / Lab 1 | **Status:** IN PROGRESS; import and runtime not verified.
**Use:** [coordination ADR](../docs/adr/0002-fso-coordination.md) · [existing branch handoff](FSO-ASSIGNMENT-HANDOFF.md).
This is a branch-local coordination record, not a merged academic archive.

## FIELD AGENT — READ THIS SECTION ONLY FIRST (2026-11-25)
You are the coordinator's eyes and local execution assistant. Do not load GPT ADR, other projects, the entire academic archive, or older handoffs to reconstruct perspective. This section supplies your current order. Read further only for a specific missing fact. Use the actual instructor prompt and current course policy as authority. No private-to-public transfer, no instruction edits, no merge. Your only coordination write is an append to [FSO-REPORT.md](FSO-REPORT.md); the coordinator controls this dispatch file. The report is the response channel, not a new task ledger. Keep chat minimal.

### D-001 — establish actual database state and finish import if needed
- **Objective:** Verify the existing MySQL connection and whether the assignment schema is imported. Last report: setup and extraction done, import not verified. Do not restart installation or re-extract.
- **Action:** In the existing Workbench SQL editor, ask the local operator to run the following read-only queries (or use an authorized tool if actually available):
```sql
SELECT VERSION() AS mysql_version;
SELECT SCHEMA_NAME FROM information_schema.SCHEMATA
WHERE SCHEMA_NAME = 'example1512O';
SELECT TABLE_NAME, TABLE_TYPE FROM information_schema.TABLES
WHERE TABLE_SCHEMA = 'example1512O' ORDER BY TABLE_NAME;
```
- **Branch on observation:** If schema has tables, check evidence of a complete import and expected table definitions; do not blindly re-import. If schema is absent/empty, confirm original dump and target selection; use Workbench Server > Data Import > Import from Self-Contained File, explicitly select/create the confirmed schema and import. Stop on the first meaningful error; retain its exact redacted message and do not retry over partially imported data.
- **Evidence:** actual version, schema present/absent, tables present/count, import result/error if attempted, and whether required tables/triggers exist. Do not expose student records or credentials. Source files remain unchanged. Report real observations, not commands merely proposed.
- **Exit:** Append a 5W report (100–180 words guideline) to FSO-REPORT.md with D-001, what was done, what is pending, and next action. Commit and verify; if no write capability, give the report in chat as NOT COMMITTED. If import is already complete, skip it and report the evidence. If blocked, send the blocker without filling gaps. Do not make unrelated changes.
- **After reporting:** If a live result reveals a decision that needs schema-specific reasoning, return the report to the coordinator (user can say "FSO report"). Do not spin on broad research or request an entire new context.

### Assignment execution map — only load the current item
Use the actual assignment and local schema, not a reconstructed rubric or guessed IDs. After D-001, the coordinator can issue the next order based on the report. In the absence of a new order, only proceed with clearly authorized, fully specified, independently verifiable steps; stop when evidence or authorization is missing.
| Gate | Task | Evidence to return |
|---|---|---|
| D-002 / Q2 | Inspect users definition, keys, defaults/triggers. Insert the required user, unique username, omit created. | Actual insert outcome; generated created; required fields and uniqueness checked. |
| D-003 / Q3 | Inspect related table definitions and lookup constraints; add two email and two phone entries, omit generated IDs. | Actual counts for the intended user, valid keys. |
| D-004 / Q4 | Run instructor-required join with exact requested columns/filter. | Column names and row count; no raw personal data in Git. |
| D-005 / Q5 | Preview exact new-user phone target, delete only that row, verify. | One affected row and postcondition. |
| D-006 / Q6 | Resolve specified occupation by exact name from live lookup, update intended user. | Actual affected count and verified association; no guessed IDs. |
| D-007 / Q1 | Produce required SQL dump from verified state in the format required by actual rubric; test safe separate restore where feasible. | Export size/hash, ZIP/restore outcome, unresolved issues. |
| D-008 | Reconcile written answers with actual results; student reviews and submits. | Rubric coverage, deliverables verified, LMS receipt status separately. |

Read [report template](FSO-REPORT.md) only for writing the next short report. Keep the exact local commands/results in the authorized chat if needed; report only public-safe observations to Git. No asynchronous communication is implied. Coordinator must explicitly read the report in a later turn.

## Latest checkpoint — 2026-11-25

**Intent:** Complete the actual database exercise, verify the six rubric items and prepare the required deliverables. Preserve the instructor's original source and avoid repeating setup.

| Workstream | Earlier AI work | Local operator progress / next gate |
|---|---|---|
| Preparation | Draft written answers and derived SQL ZIP were reported; archive integrity checked, not SQL execution | Workspace created; original archive located and extracted (reported in Quasar session handoff) |
| MySQL setup | Planned compatibility and runtime test, not demonstrated | Server/Workbench installed and connection reported successful |
| Import | Source dump provenance identified; draft SQL was not a proven live backup | Schema absent from last reported list; source inspection reported. Successful import still not evidenced |
| Lab operations | Proposed SQL and verification plan; not executed or verified by the earlier AI | No live Q2–Q6 result supplied to this review |
| Export / restore | ZIP byte integrity reported; no independent database restore | Genuine live export, restore test and final package pending evidence |
| Submission | Deliverable planning only | LMS receipt and grade unknown |

**Evidence basis:** Existing branch handoff (blob 95ee7bd16ef8f1a659ff89ba63fa4e9735987656); additional reported progress in the separate Quasar session's FSO-IDB-LAB1-HANDOFF.md (blob 3d23cf47a36ff5306015af92ca72bc12fd9cbce5). These are historical documentation, not independently observed local execution by the coordinating AI. No branch history was imported or synchronized. Verify current machine state before action. Private details are not reproduced here.

## Next action (load this first)
In the already-connected MySQL Workbench SQL editor, check whether the assignment schema now exists and contains tables. Inspect the original dump header and database selection statements if not already confirmed. Import the unchanged instructor SQL file into the explicitly selected assignment schema using Server > Data Import > Import from Self-Contained File; if the schema already contains tables, inspect before re-importing. Stop on import errors. Refresh schemas, verify tables and triggers. Do not reinstall MySQL or re-extract unless evidence shows it is needed.

## Completion gates (use actual rubric; do not guess schema/IDs)
1. Import: successful log plus expected schema/tables; confirm required definitions, unique constraints, foreign keys and triggers.
2. Q2–Q3: create one intended user and required related records; confirm actual generated values and exact counts.
3. Q4–Q6: run required join, preview and delete exactly the intended single record, resolve occupation by name and verify updated association. Record actual affected rows and SELECT evidence; no hard-coded lookup IDs without live confirmation.
4. Q1 / backup: verify current rubric's dump requirement; export actual verified database as self-contained SQL; preserve any separately required original-state dump. Check archive and, where feasible, restore to a safe separate instance/schema after inspecting database-selection directives. Do not overwrite working database.
5. Written deliverable: reconcile every answer with actual queries and results. Confirm LMS format, current deadline and course AI-use policy. Student reviews and submits through LMS; only receipt establishes submission, grade remains separate.

Official technical references: [Workbench SQL Data Export and Import Wizard](https://dev.mysql.com/doc/workbench/en/wb-admin-export-import-management.html), [MySQL SHOW statements](https://dev.mysql.com/doc/refman/8.0/en/show.html), [ROW_COUNT information function](https://dev.mysql.com/doc/refman/8.0/en/information-functions.html), [mysqldump](https://dev.mysql.com/doc/refman/8.0/en/mysqldump.html). Vendor documentation is not runtime evidence.

## Coordination protocol
Append a brief public-safe checkpoint only when something material changes:
- Date / task / last verified step and evidence classification
- Actual outcome or error (redacted)
- Next action and observable acceptance condition
- Relevant public-safe source reference

Read only relevant checkpoints and source sections. Preserve previous bytes; verify current SHA, append and re-fetch. Do not duplicate the same event in the assignment handoff. Do not merge, synchronize or modify other branches or private academic records. No live database access or new assignment execution was performed in this coordination review.
