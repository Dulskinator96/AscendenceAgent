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
