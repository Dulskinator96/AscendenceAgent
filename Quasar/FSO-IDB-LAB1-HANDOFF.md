# FSO — IDB Lab 1 Assignment Handoff

> **Purpose:** Transfer the current Full Sail Online (FSO) database-lab work to another AI agent without losing the verified machine context, local file locations, setup state, or remaining work.
>
> **Status:** In progress — MySQL is installed and Workbench connection succeeded; the assignment SQL dump has been extracted but has **not** yet been imported.
>
> **Last updated:** 2026-11-25

## 1. Task identity and objective

- **Course/workstream:** FSO — Introduction to Databases (IDB)
- **Assignment:** IDB Lab 1 / Activity 1.2 (confirm exact title and requirements against the course instructions before finalizing)
- **Goal:** Complete the required database exercises, verify each result against the assignment instructions, export the final database, prepare the written deliverable, and post/submit the finished work.
- **Do not treat this handoff as proof that the assignment is complete.** No assignment SQL has been imported and no exercise queries have yet been verified.

A prior conversation summary described a six-part task involving a supplied database, adding a user record and contact information, an INNER JOIN involving Mary and user/email tables, deleting a designated phone record, and updating an occupation to `Computer Software Engineers`. These are **reported task details, not yet revalidated against the authoritative assignment prompt**. Inspect the course instructions and supplied PDF before executing data-changing SQL.

## 2. Machine and account attribution

This work is being performed in the Quasar machine context:

| Field | Current evidence |
|---|---|
| Machine codename | Quasar |
| Reported Windows hostname | `AURORA` |
| Windows profile / home directory | `C:\\Users\\mxz` |
| Workspace root | `C:\\FSO\\IDB-Lab1` |
| OS | Windows 11 Pro Education, x64 (from the Quasar system profile) |

Quasar is a separate machine context identified in the parent Quasar system profile. Do not merge its files, hardware, credentials, or runtime assumptions with another computer or account. Confirm the current machine before running any machine-specific command.

See [Quasar system profile](./QUASAR-SYSTEM-PROFILE.md) for the hardware evidence, unknowns, and machine-specific AI handoff rules.

## 3. Local workspace and source files

Workspace structure:

```text
C:\FSO\IDB-Lab1\
├── source\
├── working\
└── output\
```

The folders were initially empty. The assignment ZIP was found in Downloads and extracted into `source`.

### Original archive

- **Archive:** `C:\Users\mxz\Downloads\DBS_example_Database_2015.zip`
- **Reported archive size:** 40,132,488 bytes
- The original ZIP remains in Downloads; preserve it unchanged.

### Extracted files

| File | Location | Size | Role / status |
|---|---|---:|---|
| `dbs_database.sql` | `C:\FSO\IDB-Lab1\source\dbs_database.sql` | 171,121,411 bytes | SQL dump; **not imported yet** |
| `dbs_database.mwb` | `C:\FSO\IDB-Lab1\source\dbs_database.mwb` | 24,886 bytes | MySQL Workbench model |
| `dbs_database.pdf` | `C:\FSO\IDB-Lab1\source\dbs_database.pdf` | 176,042 bytes | Supplied PDF; inspect for schema/task context |
| `__MACOSX\` | `C:\FSO\IDB-Lab1\source\__MACOSX\` | small metadata files | ZIP/macOS metadata; not database input |

The `working` and `output` directories were empty at the last inspection. Use them for intermediate and final artifacts respectively; do not overwrite the source files.

## 4. MySQL installation and connection status

- MySQL Installer was used to install MySQL Server 8.0.46 and MySQL Workbench.
- MySQL Workbench is open and a local connection succeeded.
- MySQL Shell 8.0.46 is also open. Its prompt was `MySQL JS >`, meaning it was in JavaScript mode at that point, not SQL mode.
- A successful Workbench connection was reported by the user.
- The user ran `SHOW DATABASES;`. The returned schemas were:

```text
information_schema
mysql
performance_schema
sakila
sys
world
```

- The assignment database was **not present** in that result, so the supplied dump still needs to be imported.
- Do not infer that the target schema name is known. Inspect the SQL dump's opening statements (for `CREATE DATABASE`, `USE`, and table definitions) and/or the assignment instructions before choosing the import target.
- Do not assume a database named `mine` or `dummy`; neither appeared in the reported schema list.

## 5. Verified progress

| Step | Status | Evidence |
|---|---|---|
| Install MySQL Server / Workbench | Reported complete | User reports both applications open |
| Connect through Workbench | Complete | User explicitly reported success |
| List current schemas | Complete | Output listed only the six standard schemas above |
| Locate assignment archive | Complete | CMD listing showed the ZIP in Downloads |
| Extract archive | Complete | Extracted-file listing showed SQL, MWB, and PDF |
| Import SQL dump | **Not started** | Assignment schema absent from reported `SHOW DATABASES` |
| Inspect schema and rows | Not started | No assignment tables inspected |
| Complete assignment queries | Not started | No query results supplied |
| Verify final database state | Not started | No post-exercise verification |
| Export final SQL dump | Not started | No export created |
| Prepare written deliverable | Not started | No completed document created |
| Package and post submission | Not started | No submission package created |

## 6. Next actions — execute in order

### Phase A — Inspect the supplied material

1. Read `source\\dbs_database.pdf` and compare it with the actual course assignment prompt.
2. Inspect the beginning of `source\\dbs_database.sql` for schema/database creation statements and encoding/collation directives. The file is approximately 171 MB; do not load the entire file into an editor unnecessarily.
3. Inspect the Workbench model `source\\dbs_database.mwb` if it helps confirm table names and relationships.
4. Record the exact intended database name and required table/column names from evidence, not guesswork.

### Phase B — Import

1. Use MySQL Workbench's **Server → Data Import** workflow or a verified command-line import.
2. Prefer importing into the schema specified by the assignment/dump. If the dump does not define a schema, create a clearly named assignment schema only after confirming the expected name.
3. Keep the source dump unchanged.
4. Capture import completion/error output.
5. Run `SHOW DATABASES;` and `SHOW TABLES;` in the imported schema. Confirm expected tables before making changes.

### Phase C — Complete and verify exercises

1. Translate each assignment requirement into a specific SQL statement.
2. Before any UPDATE or DELETE, run a SELECT that identifies the exact target row(s).
3. Use transactions where practical; verify affected-row counts.
4. Execute the required INSERT, JOIN, DELETE, and UPDATE operations only after checking exact names, IDs, and predicates against the assignment prompt and imported data.
5. Verify every result with SELECT queries and preserve the query text plus output as evidence.
6. Never assume a user ID (including any previously suggested example ID) without querying the database.

### Phase D — Deliverables

The prior workflow anticipated these deliverables; confirm their required names and formats against the course submission instructions:

- `IDBLab1_Completed.docx` — completed written assignment with accurate SQL, results, and any required screenshots.
- `IDBLab1_Database_Dump.zip` — containing the final exported SQL dump (previously proposed filename: `IDBLab1_Final.sql`).

Use `C:\\FSO\\IDB-Lab1\\output` for final artifacts. Export only after validating the final database. Re-import the exported dump into a clean test schema if feasible to verify that the dump is restorable. Do not claim successful submission until the user confirms it has been posted.

## 7. User interaction and command conventions

- Give **step-by-step** instructions and wait for the user's output before proceeding to the next consequential step.
- Distinguish clearly between **Windows CMD**, **PowerShell**, **MySQL Workbench SQL Editor**, and **MySQL Shell**. Do not provide a SQL statement for CMD or a CMD command for the MySQL prompt.
- The user explicitly requested: **from now on, every Windows CMD command block must include a command that copies the relevant output to the clipboard.**
- For CMD output, a safe repeatable pattern is:

```cmd
some-command > "%TEMP%\\fso-step.txt" 2>&1
type "%TEMP%\\fso-step.txt"
clip < "%TEMP%\\fso-step.txt"
```

- If using PowerShell from CMD, label it as such and ensure the output is captured/copied.
- Do not ask the user to paste passwords, connection secrets, or tokens. Use interactive password prompts.
- Keep instructions resource-aware and avoid unnecessary heavy inspection or stress tests.

## 8. Evidence and uncertainty rules for the next AI

1. Treat user-provided terminal output as evidence of what was displayed, not independent access to the machine.
2. Preserve the distinction between **verified**, **user-reported**, **inferred**, and **unknown**.
3. Do not fabricate query results, screenshots, database contents, file paths, import success, or submission status.
4. Do not guess schema names, IDs, table/column names, assignment requirements, or target rows.
5. Preserve the original ZIP, SQL, MWB, and PDF files.
6. Avoid destructive SQL until the target rows and predicates have been previewed and confirmed.
7. Keep credentials and personal secrets out of Git and all Markdown artifacts.
8. Record each meaningful milestone with date, exact command/query, result, and any remaining uncertainty.

## 9. Handoff starting point

**Start here:** The user has MySQL Workbench open and connected. The original archive has been extracted. The next safe operation is to inspect the supplied PDF and the SQL dump's initial schema statements, then import the dump into the correct schema.

Do not restart the installation process. Do not re-extract or overwrite the source files unless an error requires it. Do not begin assignment mutations until the import and schema inspection are complete.

---

## Update log

- **2026-11-25:** Created from the active conversation and prior Quasar machine-profile context. Recorded the installed MySQL/Workbench state, successful Workbench connection, current schemas, extracted assignment files, exact local paths, and remaining import/assignment/submission work. Explicitly marked all unperformed steps as pending.


## 10. Cross-chat reconciliation — 2026-11-25

This section supersedes earlier uncertainty in this handoff about the assignment's database identity and records the authoritative cross-chat references. It does **not** claim that the local database has been imported or that assignment operations have run.

### Canonical cross-chat sources

The user directed the receiving AI to consult the GPT cross-chat continuity records in the separate private repository:

- **Repository:** `Dulskinator96/AscendenceAgent007`
- **Branch:** `FSO_FullSailUniversity`
- **Canonical GPT continuity ADR:** [`docs/gpt/ADR-0001-GPT-CROSS-CHAT-CONTINUITY.md`](https://github.com/Dulskinator96/AscendenceAgent007/blob/FSO_FullSailUniversity/docs/gpt/ADR-0001-GPT-CROSS-CHAT-CONTINUITY.md)
- **IDB assignment handoff:** [`FSO_FullSailUniversity/courses/IDB-INTRODUCTION-TO-DATABASES-IDENTITY-PENDING.md`](https://github.com/Dulskinator96/AscendenceAgent007/blob/FSO_FullSailUniversity/FSO_FullSailUniversity/courses/IDB-INTRODUCTION-TO-DATABASES-IDENTITY-PENDING.md)
- **Special database evidence ADR:** [`FSO_FullSailUniversity/adrs/ADR-0005-IDB-LAB1-DUMP-AND-RUNTIME-EVIDENCE.md`](https://github.com/Dulskinator96/AscendenceAgent007/blob/FSO_FullSailUniversity/FSO_FullSailUniversity/adrs/ADR-0005-IDB-LAB1-DUMP-AND-RUNTIME-EVIDENCE.md)

The continuity ADR requires an incoming AI to observe first, fetch the current repository sources, preserve evidence classifications, and distinguish prepared artifacts from executed work. Cross-chat synchronization is manual; this handoff is a pointer and reconciliation record, not an assertion of automatic synchronization.

### Assignment facts established by the cross-chat records

- **Target schema:** `example1512O` (last character is capital letter O).
- **Assignment:** IDB Activity 1.2 — Lab 1.
- **Original instructor archive:** `DBS_example_Database_2015.zip`.
- **Original SQL source:** `dbs_database.sql`, approximately 171 MB; archive provenance identifies Sequel Pro 4499 / MySQL 5.5.42 and generation date 2015-11-24.
- **Six rubric tasks:** (Q1) database dump; (Q2) insert a user with userId plus at least five other columns, include unique username, omit `created`; (Q3) insert two email and two phone rows without supplying auto-increment IDs; (Q4) INNER JOIN returning lastName, firstName, userName, userEmail for firstname Mary; (Q5) delete exactly one phone row; (Q6) query occupation `Computer Software Engineers` and update the user's occupation foreign key.
- **Prepared identity values in a prior artifact:** userId `FSO20261124DULSKY` and username `dulsky_idb_lab1`. Treat these as previously prepared draft values, not proof of rows in the current Quasar database.
- **Occupation ID 187:** appears in a prior prepared answer, but the cross-chat handoff explicitly says it requires database verification. Do not use it without checking the live lookup table.

### Previously prepared deliverables — separate from Quasar runtime proof

The cross-chat assignment handoff reports that on 2026-11-24 these artifacts were created and inspected in a prior workflow:

- `IDBLab1_Completed.docx` (approximately 38 KB), containing draft answers for all six questions.
- `IDBLab1_Database_Dump.zip` (approximately 39 MB), containing `IDBLab1_database.sql` (approximately 171 MB).

The ZIP CRC passed, but its SQL is an altered copy of the instructor export with proposed lab SQL appended. It is **not** a post-CRUD export from a running database and has **not** been independently restored. Do not recreate these artifacts automatically; first locate and inspect the existing files if they are needed. Their presence in another workflow does not establish that they exist under this Quasar machine's `output` directory.

### Current Quasar session evidence — 2026-11-25

- MySQL Server 8.0.46 and Workbench are installed; Workbench connection succeeded.
- The reported `SHOW DATABASES` output did not include `example1512O`.
- The user inspected the SQL dump's table-definition area; the visible excerpt showed a `dvd` table definition.
- The inspection command searched for lines beginning `CREATE DATABASE` or `USE ` and returned no matches. Therefore the import must explicitly target the confirmed schema `example1512O`; the dump does not appear to select it itself.
- **Import into Quasar: NOT YET VERIFIED.** No successful import output, `SHOW TABLES` from `example1512O`, or row checks have been supplied.

### Correct next operation

Continue from the existing Quasar MySQL Workbench connection. If `example1512O` has not yet been created, create it once; then import the unchanged source file `C:\\FSO\\IDB-Lab1\\source\\dbs_database.sql` into that schema. Do not re-run installation, re-extraction, or connection setup. After import, verify tables and relevant triggers/lookup rows before running Q2–Q6.

### Evidence lifecycle and submission boundary

Maintain this sequence as separate evidence gates:

`original instructor dump → imported sandbox database → executed Q2–Q6 statements → observed row/trigger results → genuine post-operation SQL export → independent restore check → FSO upload receipt`.

The prior handoff reports the LMS overview requests a zipped SQL dump while the original worksheet says a .sql file need not be zipped; preserve both source instructions and do not claim the conflict was resolved. FSO submission and grade remain **UNKNOWN** until the user supplies a receipt or grade evidence.
