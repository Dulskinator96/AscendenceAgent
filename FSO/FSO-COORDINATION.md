# FSO coordination — active task and AI handoff

**As of:** 2026-11-25 | **Task:** IDB Activity 1.2 / Lab 1 | **Status:** IN PROGRESS; import and runtime not verified.
**Use:** [coordination ADR](../docs/adr/0002-fso-coordination.md) · [existing branch handoff](FSO-ASSIGNMENT-HANDOFF.md).
This is a branch-local coordination record, not a merged academic archive.

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
