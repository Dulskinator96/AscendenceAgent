# FSO Assignment — AI Handoff Record

> **Status:** IN PROGRESS — workspace initialized; source import and database execution not yet evidenced  
> **Prepared:** 2026-11-25  
> **Target machine:** Quasar (Windows hostname AURORA, local Windows profile mxz)  
> **Git branch:** FSO-assignment, created from Quasar  
> **Purpose:** Transfer the FSO IDB Lab 1 task to another AI/operator without losing context or confusing prepared work with executed work.

---

## 1. Executive summary

This handoff tracks **Activity 1.2 — Lab 1** for the Full Sail University course record titled **Introduction to Databases (IDB)**. The task uses an instructor-provided MySQL database dump and requires a database dump deliverable, SQL data manipulation, a join query, a deletion, and an occupation update.

The immediate working environment is the Windows machine identified in the Quasar system profile as hostname AURORA, with the local profile C:\Users\mxz. The user has created the local workspace directories under C:\FSO\IDB-Lab1.

**Current verified progress:** the four workspace directories were created successfully and the user ran the tree command, which showed the expected source, working, and output folders. No source ZIP, extracted SQL file, imported database, executed lab query, verified export, restore test, or LMS submission is evidenced by that output.

The next action is to place the original instructor ZIP in source, preserve it, extract a working copy, and inspect the SQL before attempting an import.

## 2. The 5 Ws

### Who

- **Student/operator:** the person completing the FSO assignment through the Windows profile mxz; do not infer a legal name or student ID from the profile name.
- **GitHub/repository context:** project owner account Dulskinator96. This identifies repository ownership, not necessarily the student's official course identity.
- **Target computer:** Quasar, documented separately in Quasar/QUASAR-SYSTEM-PROFILE.md; reported Windows hostname AURORA.
- **Machine ownership boundary:** Quasar is identified in the system profile as the user's brother's PC, not the user's primary computer. Do not merge its files, credentials, specifications, or runtime state with another machine.
- **Future AI/operator:** must continue from observed local state, verify before changing anything, and maintain the status distinctions in this document.

### What

Complete **Activity 1.2 — Lab 1** for Introduction to Databases (IDB), including the six rubric items:

1. **Q1 — Database dump (20 points):** produce the required database dump deliverable.
2. **Q2 — Insert user (16 points):** insert one row into users, including userId and at least five additional columns; use a unique username; omit the created field so the database's default/trigger behavior can populate it.
3. **Q3 — Insert contact details (16 points):** insert two rows into userEmail and two rows into userPhone; omit auto-increment ID columns.
4. **Q4 — Inner join (16 points):** join users and userEmail; return exactly lastName, firstName, userName, and userEmail; filter for first name Mary.
5. **Q5 — Delete phone row (16 points):** delete exactly one phone record inserted for the lab user and verify the affected-row count.
6. **Q6 — Occupation update (16 points):** identify the occupation named Computer Software Engineers, update the newly created user's occupation foreign key, and verify the resulting row.

The source SQL identifies a legacy Sequel Pro export using MySQL 5.5.42, database example1512O, generated 2015-11-24. Compatibility with a current MySQL release is not guaranteed and must be tested against a preserved copy.

### When

- **Recorded LMS due date:** November 25, 2026, 11:59 PM EST.
- **Handoff prepared:** November 25, 2026.
- Treat the LMS as the authoritative source if its displayed deadline, timezone, or assignment status differs from this record.
- Do not claim on-time submission, late submission, grading, or instructor acceptance without an LMS receipt or other direct evidence.

### Where

**Local workspace on Quasar:**

~~~text
C:\FSO\IDB-Lab1\
├── source\    # Original instructor ZIP and preserved source files
├── working\   # Extracted SQL and controlled working copies
└── output\    # Verified final export and submission package
~~~

The user created the parent and three child directories using Windows Command Prompt (CMD). The user then ran:

~~~cmd
tree C:\FSO\IDB-Lab1
~~~

Observed output:

~~~text
C:\FSO\IDB-LAB1
├───output
├───source
└───working
~~~

This verifies directory creation only. It does not show files inside those folders.

**Repository context:**

- This handoff is stored in Dulskinator96/AscendenceAgent, branch FSO-assignment.
- The branch was created from the existing Quasar branch, preserving the Quasar system-profile baseline.
- Related FSO course/project notes were previously located in Dulskinator96/AscendenceAgent007, branch FSO_FullSailUniversity. These are separate repositories. Do not assume that a file or local checkout in one repository exists in the other.
- This handoff branch is documentation-only unless a later, explicitly reviewed commit adds scripts or other artifacts. Do not commit the instructor's large SQL dump, personal course credentials, or secrets.

### Why

The assignment demonstrates practical database operations against the instructor's supplied schema: data insertion, relational joins, targeted deletion, foreign-key updates, and producing a database dump. The handoff exists so a new AI/operator can resume without repeating setup, corrupting the original source, or falsely reporting completion.

The evidence standard is strict: **a command being prepared is not a command being run; a command being run is not proof it succeeded; a generated file is not proof it restores; and an uploaded file is not proof it was accepted or graded.**

## 3. Environment baseline and resource constraints

Quasar's recorded system profile reports:

- Windows 11 Pro Education, x64, build 26300.
- AMD Ryzen 5 5600, 6 cores / 12 logical processors.
- NVIDIA GeForce RTX 4060; dedicated VRAM amount remains unverified.
- Approximately 16 GB system RAM.
- Gigabyte A520M K V2 motherboard.
- Firmware virtualization was reported disabled in the captured system report.

For this database task, the CPU/GPU are not expected to be the limiting factors. The approximately 16 GB RAM baseline and the large SQL import are the relevant resource considerations. Avoid launching unnecessary virtual machines, local AI models, Unreal Engine, or other memory-heavy applications during import. Do not recommend hardware changes without workload evidence.

Do not write Windows Product IDs, serial numbers, passwords, API keys, tokens, private network addresses, or course login credentials into this repository.

## 4. Source package and schema facts

Previously identified source package:

- ZIP filename: DBS_example_Database_2015.zip
- Approximate compressed size: 39 MB.
- SQL file inside: dbs_database.sql, approximately 171 MB.
- Other package contents include dbs_database.mwb and dbs_database.pdf, plus macOS metadata.
- SQL header identifies Sequel Pro 4499, MySQL 5.5.42, database example1512O, generated 2015-11-24.

These are facts from the previously inspected course materials/package description. **The package has not yet been observed inside the current Quasar workspace.** Confirm its actual filename and contents after the user places it in source.

Legacy SQL may contain syntax, collation, engine, or routine/trigger behavior that differs from a modern MySQL installation. Do not assume that a successful connection means the entire import succeeded. Preserve the first meaningful import error and investigate it before retrying.

## 5. Work completed — evidence ledger

| Item | Status | Evidence / interpretation |
|---|---|---|
| Quasar system profile exists | RECORDED | Existing Quasar branch profile; use it for machine identity and constraints. |
| FSO workspace parent created | VERIFIED | User ran mkdir C:\FSO\IDB-Lab1 without an error. |
| source directory created | VERIFIED | User ran mkdir C:\FSO\IDB-Lab1\source without an error. |
| working directory created | VERIFIED | User ran mkdir C:\FSO\IDB-Lab1\working without an error. |
| output directory created | VERIFIED | User ran mkdir C:\FSO\IDB-Lab1\output without an error. |
| Directory tree checked | VERIFIED | User's tree output showed all three expected directories. |
| Original ZIP copied into source | NOT YET EVIDENCED | No file listing or copy result supplied. |
| ZIP integrity / extraction | NOT YET EVIDENCED | No extraction or archive test result supplied. |
| MySQL installed and service running | UNKNOWN | No Quasar installation/service output supplied. |
| Database imported | NOT RUN / NOT EVIDENCED | No successful import log or live schema query supplied. |
| Q2–Q6 SQL executed | NOT RUN / NOT EVIDENCED | No live query results supplied. |
| Final database export generated | NOT RUN / NOT EVIDENCED | A previously prepared SQL package is not proof of a live export. |
| Independent restore test | NOT RUN / NOT EVIDENCED | No restore result supplied. |
| DOCX and ZIP submitted to LMS | NOT EVIDENCED | No submission receipt supplied. |
| Grade / instructor acceptance | UNKNOWN | No grading evidence supplied. |

### Important distinction about prior draft artifacts

Earlier project work described a draft IDBLab1_Completed.docx and a ZIP containing a SQL file assembled from the instructor dump plus proposed lab operations. The ZIP integrity was checked, but that artifact was **not independently verified as an export from a live database after successful execution**. Do not reuse or label it as a verified final database dump without inspecting it, reconciling it against the current source, executing the required operations, exporting the actual database, and completing a restore test.

## 6. Remaining work — ordered execution plan

### Phase A — stage and preserve source

1. Locate the actual DBS_example_Database_2015.zip on the target computer or obtain it from the official course source.
2. Copy it to C:\FSO\IDB-Lab1\source\.
3. Record its exact filename, file size, and SHA-256 hash.
4. Keep the original ZIP unchanged. Extract a copy into working.
5. Confirm that dbs_database.sql exists and record its size/hash.
6. Inspect the SQL header and any database-selection statements before importing.

**Exit criteria:** source ZIP and extracted SQL are present, readable, and checksummed; original source remains preserved.

### Phase B — establish MySQL runtime

1. Determine whether MySQL Server and Workbench are already installed.
2. Record exact server/client versions and service state.
3. Select a MySQL version based on compatibility testing, not assumption. The dump is from MySQL 5.5.42.
4. Confirm sufficient free disk space for the SQL file, imported database, temporary files, and final export.
5. Import into a controlled local instance using a documented command or Workbench import workflow.
6. Save stdout/stderr or the Workbench import log. Stop on the first meaningful error and investigate rather than repeatedly importing into a partially modified schema.
7. Verify database example1512O, expected tables, and relevant triggers/defaults.

**Exit criteria:** import completes without unresolved errors; schema and required tables are visible; import evidence is retained.

### Phase C — execute and verify Q2–Q6

1. Inspect actual table definitions, primary keys, foreign keys, defaults, triggers, and required columns.
2. Confirm a unique username and non-conflicting lab user ID before inserting.
3. Execute Q2 and verify the inserted user row and generated created value.
4. Execute Q3 and verify exactly two email rows and two phone rows linked to the lab user.
5. Execute Q4 and verify the query returns exactly the four requested columns and filters first name Mary.
6. Execute Q5 using a predicate that identifies exactly one phone row inserted for this lab user; verify one affected row and confirm the other intended contact data remains.
7. For Q6, query the occupation table for the exact occupation name Computer Software Engineers. Do not assume an occupation ID from an earlier draft. Use the ID returned by the live database, update the new user, and verify the joined occupation name.
8. Save the exact SQL statements and result evidence for the completed document.

**Exit criteria:** every rubric operation has a live result and independent verification; no guessed IDs or unverified affected-row counts.

### Phase D — export and restore verification

1. Export the actual resulting database from the live MySQL instance.
2. Save the export under C:\FSO\IDB-Lab1\output\.
3. Record file size and SHA-256.
4. Package the final SQL dump in the ZIP format requested by the LMS. The LMS overview was previously reported to require a zipped SQL dump, while the original worksheet reportedly allowed a plain .sql; follow the stricter LMS requirement unless the current LMS instructions say otherwise.
5. Restore the exported dump into a separate test schema or clean disposable instance. Inspect CREATE DATABASE / USE statements first so the restore test does not overwrite the working schema.
6. Verify the restored schema and the lab user's relevant records.

**Exit criteria:** final export exists, ZIP opens, and an independent restore test succeeds.

### Phase E — final review and LMS submission

Expected deliverables:

- IDBLab1_Completed.docx
- IDBLab1_Database_Dump.zip

Before submission:

1. Compare the DOCX answers against the live SQL evidence and rubric.
2. Ensure identifiers and sample contact details are consistent across answers and database.
3. Confirm the ZIP contains the final verified export, not the earlier proposed/draft SQL.
4. Check filenames and LMS upload requirements.
5. Submit through the official LMS and retain the observed receipt/status.
6. Record submission timestamp and receipt reference without copying sensitive account data into Git.
7. Treat grading and instructor acceptance as separate, later outcomes.

**Exit criteria:** both required deliverables uploaded and an LMS receipt/status observed.

## 7. AI-agent operating instructions

Any AI agent taking over must follow these rules:

1. **Start with a read-only state check.** Confirm machine identity, current directory, files present, MySQL service/version, and Git working tree before making changes.
2. **Do not confuse shells.** The user has been working in Windows Command Prompt (C:\Users\mxz>). Commands such as mkdir, dir, tree, and where are appropriate in CMD. New-Item, Get-ChildItem, and Get-Service are PowerShell commands. Clearly label any shell switch.
3. **Preserve originals.** Never edit or overwrite the instructor ZIP or original SQL dump. Work from extracted copies.
4. **Do not assume local files exist.** Ask for or inspect an actual directory listing; do not infer file presence from a prior conversation or a Git document.
5. **Inspect before executing.** Review schema and constraints before proposing inserts, deletes, or updates.
6. **Use exact predicates.** Avoid broad updates/deletes. Verify row counts and resulting rows.
7. **Never guess foreign keys.** Query the live database for the occupation ID by exact occupation name.
8. **Separate artifact states.** Label every output as draft, proposed SQL, executed result, exported backup, restore-tested backup, or submitted deliverable.
9. **Protect the machine.** Keep the workflow resource-aware for a 16 GB RAM machine. Avoid unnecessary model inference, benchmarks, stress tests, VMs, or background services during import.
10. **Protect credentials.** The user enters MySQL and LMS credentials locally. Never request them in chat or write them to Git.
11. **Maintain reproducibility.** Record commands, versions, timestamps, hashes, and concise result summaries. Do not store unnecessary personal identifiers.
12. **Never claim success without evidence.** If an operation was not observed, mark it UNKNOWN or NOT YET VERIFIED.
13. **Respect course policy.** The user must review and understand the work and comply with the current course AI-use rules before submitting.
14. **Do not submit autonomously.** Prepare and verify the package; submission must follow the user's explicit authorization and the LMS must return an observable receipt.

## 8. Immediate next action

The next useful commands are read-only listings in the current CMD window:

~~~cmd
dir C:\FSO\IDB-Lab1\source
dir C:\FSO\IDB-Lab1\working
dir C:\FSO\IDB-Lab1\output
~~~

If the source directory is empty, copy the original instructor ZIP into it. Do not start the MySQL import until the archive and extracted SQL file have been confirmed.

## 9. Handoff completion checklist

- [ ] Original instructor ZIP staged and checksummed.
- [ ] Extracted SQL staged and checksummed.
- [ ] MySQL version/service and disk headroom recorded.
- [ ] Database import completed and logged.
- [ ] Schema/tables/triggers inspected.
- [ ] Q2 insert executed and verified.
- [ ] Q3 email/phone inserts executed and verified.
- [ ] Q4 exact-column Mary join executed and verified.
- [ ] Q5 one-row phone deletion executed and verified.
- [ ] Q6 occupation FK resolved by name, updated, and verified.
- [ ] Final live database export created.
- [ ] ZIP package created and integrity checked.
- [ ] Independent restore test passed.
- [ ] DOCX reconciled with actual results.
- [ ] LMS submission receipt captured.
- [ ] Final status and evidence references recorded.

## 10. Change log

- **2026-11-25:** Initial FSO handoff prepared on the FSO-assignment branch from Quasar. Recorded the user's successful creation and tree verification of C:\FSO\IDB-Lab1\{source,working,output}. No database import or SQL execution is claimed at this checkpoint.
