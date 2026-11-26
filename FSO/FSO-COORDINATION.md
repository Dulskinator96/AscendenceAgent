# FSO coordination — active task and AI handoff

**As of:** 2026-11-25 | **Task:** IDB Activity 1.2 / Lab 1 | **Status:** IN PROGRESS; Q2 observed PASS; Q3–Q6, final export and submission pending.
**Use:** [coordination ADR](../docs/adr/0002-fso-coordination.md) · [existing branch handoff](FSO-ASSIGNMENT-HANDOFF.md).
This is a branch-local coordination record, not a merged academic archive.

## RELOOK — field-agent communication protocol (2026-11-25)
When the operator says "relook", refresh this file at the current FSO-assignment branch revision. Read this short protocol and the first current dispatch immediately below; stop at its next level-two heading. Do not read historical orders, GPT ADRs, other repositories or unrelated files. The coordination file is the coordinator's outgoing message; FSO/FSO-REPORT.md is the field agent's incoming report. The operator is not responsible for relaying technical instructions.

For a SQL dispatch, return the exact supplied runnable SQL in one code block and one short execution instruction. Do not recap the assignment or ask for previously completed setup, unavailable drafts or additional research. If the operator has already executed the dispatch, collect its actual outcome rather than replaying it. After receiving results, append the requested compact evidence report to FSO/FSO-REPORT.md; preserve prior reports and verify the commit. If a report is already present for that execution, do not duplicate it. If blocked, report the exact redacted error. Do not change coordination instructions or other files.

Current state: Q2 observed PASS. D-006 immediately below is the only active order, covering all remaining work. D-005 and earlier orders are historical; do not replay them. No new mutation is authorized by this protocol itself. Future coordinator orders will be inserted immediately below this protocol; historical dispatches are inactive. If a completed dispatch has no successor, report its status without rerunning it. Keep responses concise to conserve context. No automatic inter-chat messaging is implied; "relook" is the manual refresh trigger.

## ACTIVE DISPATCH D-006 — complete ALL remaining IDB Lab 1 requirements (2026-11-25)

**Read only this order.** This supersedes the old D-005 status in the RELOOK protocol. Coordinator observed Workbench screenshot: D-005/Q2 INSERT affected 1 row, duplicates 0, warnings 0, SELECT returned LAB1_DEMO_1125 / Alex Example / lab1_demo_1125 with created 2026-11-25 23:04:40. Q2 PASS; do not repeat. No further schema discovery or context loading unless a real error requires it. Use this same fictional lab user throughout. No new identity.

**Field agent:** output the entire remaining SQL block verbatim and the short finalization steps below in one response. User runs the SQL in the existing Workbench connection and reviews the result. Do not wait for a fresh coordinator dispatch between questions. Only stop for errors or unmet checks. Follow the current course AI-use policy. The SQL below is engineered from the recovered draft, not yet executed; contact lookup table names/IDs are source-based candidates and must resolve successfully. Do not silently change the commands.

### Remaining SQL — Q3, Q4, Q5, Q6
Run once, in order, in the same Workbench connection. Do not run again after a successful commit. Stop on the first SQL error; if the transaction is open, ROLLBACK rather than committing partial work. Require all three mutated tables to be InnoDB for transactional protection. Initial gate requires the intended Q2 row and no existing contact rows for it, so an unexpected existing state blocks mutations rather than duplicating contacts.

```sql
USE example1512O;
START TRANSACTION;

SET @lab_user = 'LAB1_DEMO_1125';
SET @q3_ready = 0, @q3_ok = 0, @deleted_rows = 0,
    @occupation_matches = 0, @occupation_id = NULL;

SELECT COUNT(*) = 1
INTO @user_ok
FROM users
WHERE userid = @lab_user AND username = 'lab1_demo_1125'
  AND created IS NOT NULL;

SELECT (
    @user_ok = 1
    AND @@SESSION.foreign_key_checks = 1
    AND (SELECT COUNT(*) FROM information_schema.TABLES
         WHERE TABLE_SCHEMA = DATABASE()
           AND TABLE_NAME IN ('users','userEmail','userPhone')
           AND ENGINE = 'InnoDB') = 3
    AND (SELECT COUNT(*) FROM userEmail WHERE userId = @lab_user) = 0
    AND (SELECT COUNT(*) FROM userPhone WHERE userId = @lab_user) = 0
    AND (SELECT COUNT(*) FROM userEmailType
         WHERE userEmailTypeId IN (1,3)) = 2
    AND (SELECT COUNT(*) FROM userPhoneType
         WHERE userPhoneTypeId IN (1,2)) = 2
) INTO @q3_ready;
SELECT @q3_ready AS q3_preconditions_pass;

-- Q3: four separate INSERT statements, omitting auto-increment IDs.
INSERT INTO userEmail (userId, userEmail, userEmailTypeId)
SELECT @lab_user, 'lab1.demo.personal@example.com', 1
WHERE @q3_ready = 1;

INSERT INTO userEmail (userId, userEmail, userEmailTypeId)
SELECT @lab_user, 'lab1.demo.school@example.com', 3
WHERE @q3_ready = 1;

INSERT INTO userPhone (userId, userPhone, userPhoneTypeId)
SELECT @lab_user, '555-0101', 1
WHERE @q3_ready = 1;

INSERT INTO userPhone (userId, userPhone, userPhoneTypeId)
SELECT @lab_user, '555-0102', 2
WHERE @q3_ready = 1;

SELECT COUNT(*) AS emails_before_delete
FROM userEmail WHERE userId = @lab_user;
SELECT COUNT(*) AS phones_before_delete
FROM userPhone WHERE userId = @lab_user;

SELECT (
    @q3_ready = 1
    AND (SELECT COUNT(*) FROM userEmail WHERE userId = @lab_user) = 2
    AND (SELECT COUNT(*) FROM userPhone WHERE userId = @lab_user) = 2
    AND (SELECT COUNT(*) FROM userPhone
         WHERE userId = @lab_user AND userPhone = '555-0102'
           AND userPhoneTypeId = 2) = 1
) INTO @q3_ok;

-- Q4: exact four requested columns and filter.
SELECT u.lastname AS lastName, u.firstname AS firstName,
       u.username AS userName, e.userEmail
FROM users AS u
INNER JOIN userEmail AS e ON u.userid = e.userId
WHERE u.firstname = 'mary';

SELECT COUNT(*) AS mary_join_rows
FROM users AS u
INNER JOIN userEmail AS e ON u.userid = e.userId
WHERE u.firstname = 'mary';

-- Q5: delete exactly one of the newly inserted phones.
DELETE FROM userPhone
WHERE userId = @lab_user AND userPhone = '555-0102'
  AND userPhoneTypeId = 2 AND @q3_ok = 1
LIMIT 1;
SET @deleted_rows = ROW_COUNT();
SELECT @deleted_rows AS deleted_rows;

SELECT COUNT(*) AS phones_after_delete
FROM userPhone WHERE userId = @lab_user;

-- Q6: select all occupation columns and resolve the live ID.
SELECT * FROM occupation
WHERE occupation = 'Computer Software Engineers';

SELECT COUNT(*), MIN(occupationId)
INTO @occupation_matches, @occupation_id
FROM occupation
WHERE occupation = 'Computer Software Engineers';

UPDATE users
SET occupationId = @occupation_id
WHERE userid = @lab_user AND @q3_ok = 1
  AND @deleted_rows = 1 AND @occupation_matches = 1
LIMIT 1;

SELECT u.userid, u.occupationId, o.occupation
FROM users AS u
INNER JOIN occupation AS o ON u.occupationId = o.occupationId
WHERE u.userid = @lab_user;

-- Final transaction acceptance check.
SELECT @q3_ready AS preconditions_pass,
       @q3_ok AS q3_pass_before_delete,
       @deleted_rows AS deleted_rows,
       @occupation_matches AS occupation_matches,
       @occupation_id AS live_occupation_id,
       (SELECT COUNT(*) FROM userEmail WHERE userId = @lab_user) AS emails_final,
       (SELECT COUNT(*) FROM userPhone WHERE userId = @lab_user) AS phones_final,
       (
        @q3_ready = 1 AND @q3_ok = 1
        AND @deleted_rows = 1 AND @occupation_matches = 1
        AND (SELECT COUNT(*) FROM userEmail WHERE userId = @lab_user) = 2
        AND (SELECT COUNT(*) FROM userPhone WHERE userId = @lab_user) = 1
        AND (SELECT COUNT(*) FROM userPhone WHERE userId = @lab_user
             AND userPhone = '555-0101') = 1
        AND (SELECT COUNT(*) FROM users WHERE userid = @lab_user
             AND occupationId = @occupation_id) = 1
       ) AS ready_to_commit;
```

**Commit gate:** If every statement succeeded (including Q4), and ready_to_commit = 1, run `COMMIT;` in the same connection. If there is an error or ready_to_commit is 0/NULL, run `ROLLBACK;` in that connection, report the first error and summary output, and do not rerun blindly. Verify committed final rows with the existing final SELECTs only, not by repeating the mutations. The Workbench Action Output and result grids are evidence; merely displaying SQL is not a pass.

### Finish Word document and Q1 — do not wait for another dispatch
1. Q2 already passed. In a copy of the original IDBLab1.doc, enter the student's own name locally. Paste the actual successful D-005 Q2 INSERT below (not the older personal draft); the observed created timestamp is 2026-11-25 23:04:40. Include the relevant session setup/variables with the executed statements wherever needed so the answers are reproducible. Do not copy the precondition/reporting SQL as an alleged additional assignment requirement.
```sql
INSERT INTO users
(userid, firstname, lastname, middleName,
 username, gender, userStatusId, userTypeId)
SELECT 'LAB1_DEMO_1125', 'Alex', 'Example', 'T',
       'lab1_demo_1125', 'M', 1, 1
WHERE @@SESSION.foreign_key_checks = 1
  AND EXISTS (SELECT 1 FROM userStatus WHERE userStatusId = 1)
  AND EXISTS (SELECT 1 FROM userType WHERE userTypeId = 1)
  AND NOT EXISTS (
      SELECT 1 FROM users
      WHERE userid = 'LAB1_DEMO_1125' OR username = 'lab1_demo_1125'
  );
```
2. Q3: paste the four executed INSERTs and necessary variable/precondition definitions. Q4: paste the exact four-column JOIN. Q5: paste the targeted DELETE with its necessary variable definitions. Q6: paste the occupation SELECT and the executed UPDATE with the observed occupation ID/lookup variable setup. Keep SQL and evidence consistent; use the real output, never fabricate an ID or row count. Original worksheet asks for SQL statements, not mandatory screenshots; retain evidence locally. Preserve original instructor file and review against the actual rubric.
3. Q1: after successful COMMIT, Workbench Server > Data Export; choose example1512O, all tables, Dump Structure and Data, Export to Self-Contained File, include triggers and relevant stored routines/events where present. Save a new SQL export in the existing output folder. Start Export, check success and nonzero file size. Do not overwrite the instructor dump. Package the actual SQL export as ZIP if current LMS requires it; original worksheet accepts plain SQL. Independent restore is useful QA, not explicit worksheet requirement; do not risk the working database or delay submission solely for this optional check. Report restore NOT RUN if not performed.
4. Confirm the Word file contains all six answers/required statements, name and correct fictional lab identity; verify final SQL dump is the live export, not the previously drafted derivative. Student reviews, follows course policy, uploads the two required deliverables and verifies LMS receipt. Do not claim submission unless observed.

### Final field report
Append one compact 5W report for D-006 to FSO/FSO-REPORT.md, including D-005/Q2 observed result, actual Q3 email/phone counts before deletion, Q4 four columns and count, Q5 affected count and surviving phone count, Q6 actual occupation ID and association, transaction committed/rolled back, Word completed status, SQL export size/format, restore status and LMS receipt status. If blocked, record exact redacted error and next single action. No raw personal result rows, student identifiers or course documents in Git. Verify report commit; if no write access, return report in chat. Do not duplicate historical handoffs. Coordinator may review after user requests it; no new dispatch needed between successful steps.

## ACTIVE DISPATCH D-005 — Q2 command delivery (2026-11-25)
> Historical status before D-006 (retained): **Status:** IN PROGRESS; import and runtime not verified.
> Current state: database access and required tables/trigger observed; Q2 execution is still unverified. D-005 below remains the active order.

Read ONLY this section. D-004 is superseded because it required unavailable private values. The coordinator supplies fictional lab data below; the worksheet requires a new user, not the student's personal identity in the database. The student enters their own name in the Word worksheet separately. Use this same lab identity throughout Q2–Q6. Do not create another identity if an earlier Q2 was actually executed; report that case instead.

**Field agent response:** reproduce the following SQL exactly in one code block, tell the operator to run it in the existing MySQL Workbench SQL editor, and request the result. Do not research, summarize, reconstruct, ask for a draft, or reload prior instructions. Schema access and the users INSERT trigger were already observed. No literal placeholders. Candidate lookup IDs are tested by the INSERT predicates below; the two lookup table names follow the conventional schema and are not yet runtime-confirmed. If either is missing or any SQL error occurs, report the exact redacted error; do not guess a replacement. The existing database must have foreign key checks enabled. No schema changes.

```sql
USE example1512O;

INSERT INTO users
(userid, firstname, lastname, middleName,
 username, gender, userStatusId, userTypeId)
SELECT
 'LAB1_DEMO_1125', 'Alex', 'Example',
 'T', 'lab1_demo_1125', 'M', 1, 1
WHERE @@SESSION.foreign_key_checks = 1
  AND EXISTS (SELECT 1 FROM userStatus WHERE userStatusId = 1)
  AND EXISTS (SELECT 1 FROM userType WHERE userTypeId = 1)
  AND NOT EXISTS (
    SELECT 1 FROM users
    WHERE userid = 'LAB1_DEMO_1125'
       OR username = 'lab1_demo_1125'
  );

SELECT ROW_COUNT() AS inserted_rows;

SELECT userid, firstname, lastname, username, created
FROM users
WHERE userid = 'LAB1_DEMO_1125';
```

**Report:** D-005, 5Ws in brief; actual inserted_rows, whether the exact intended row exists and created is populated, and any error. A zero-row insert is not new execution success; if the same intended row already exists, report existing row separately, otherwise BLOCKED. The student's Word answer must reflect the actual executed SQL, not the prior draft identity. Append to FSO/FSO-REPORT.md using fresh SHA and verify; if unable, return report in chat. No other file edits. Coordinator will issue the next command from actual results. Historical orders below are inactive.

## ACTIVE SQL DISPATCH — D-004 / Q2 (2026-11-25)

**Field agent: output the preserved SQL block below, not an explanation or another research task.** Read only this section (stop at the next heading). Use the student's existing local draft to substitute the five private values marked LOCAL and the locally approved gender value; do not invent them or publish them in Git. Confirm status/type IDs 1 and 1 against the existing local schema/lookup evidence before execution; these are draft candidates, not verified runtime facts. If evidence is missing, request only the necessary lookup/column detail. Do not repeat import or the already-successful SHOW CREATE TABLE/SHOW TRIGGERS checks. Never execute literal placeholders. Paste the resulting command as one SQL block for the operator in MySQL Workbench.

```sql
USE example1512O;

INSERT INTO users
(userid, firstname, lastname, middleName,
 username, gender, userStatusId, userTypeId)
SELECT
 'LOCAL_USER_ID', 'LOCAL_FIRST_NAME', 'LOCAL_LAST_NAME',
 'LOCAL_MIDDLE_NAME', 'LOCAL_USERNAME', 'LOCAL_GENDER', 1, 1
WHERE NOT EXISTS (
    SELECT 1 FROM users
    WHERE userid = 'LOCAL_USER_ID'
       OR username = 'LOCAL_USERNAME'
);

SELECT userid, username, created
FROM users
WHERE userid = 'LOCAL_USER_ID';
```

Preservation: coordinator's previous Q2 SQL structure retained; only private literal values are withheld from this public file. If an existing username belongs to a different user ID, or no intended row is returned, report BLOCKED rather than calling it a pass. On execution, record the insert affected-row count (Workbench Action Output), intended row returned, created populated or not, and any error. Append a short 5W D-004 result to FSO/FSO-REPORT.md; no raw personal values. If unable to commit, return the report in chat. Do not mark Q2 done merely because the SQL was displayed. No other file/branch writes. Earlier orders are retained as history; no reload required.

## Coordinator override — context exhaustion observed (2026-11-25)
The operator supplied a screenshot of the field chat displaying Context window full while requesting the existing users definition. No new mutation result is visible. For this assignment, the coordinator now prepares the next SQL directly and the operator runs it in Workbench. Do not restart the field chat or reload continuity files just to obtain perspective. Preserve the existing D-003 answer map as reference. If a local assistant is used, give it only the current SQL/result task; its report should contain the observed outcome and blocker, not another full handoff. No claim of successful execution or measured token savings.

## CURRENT ORDER — D-003: recovered worksheet and draft validation (2026-11-25)
**Read only this order.** Coordinator recovered and inspected both original Word worksheet copies and the earlier completed draft. Import is USER_REPORTED successful (R-001). Do not search other chats, repositories, or redo setup. Use the following condensed technical answer map to verify and fill the actual local Word worksheet. Preserve its original layout, paste the verified SQL under each question, enter the student's name locally, and follow course AI-use rules. If the prior draft is available, correct it; otherwise use a working copy of the original. This is a redacted operational summary, not a copy of the instructor document or private archive.

**Important:** Prior draft SQL was written using the source schema; it was not executed on live MySQL. Prior ZIP passed archive integrity only. Earlier draft language implying submission is not supported by a receipt. Do not reuse that claim. Worksheet requires SQL statements, not mandatory screenshots; capture verification locally but do not add extra deliverables unless the LMS requires them. Reported deadline: Nov 25 at 11:59 PM EST; confirm current LMS instructions. Work efficiently.

### D-003 progress update — 2026-11-25 22:57
**OBSERVED (operator's Workbench photo):** USE example1512O and SHOW CREATE TABLE for users, userEmail, userPhone and occupation all succeeded; each definition query returned one row. SHOW TRIGGERS returned two rows, including usersCreatedDateInsert (BEFORE INSERT on users). This establishes access to the required tables and trigger, not completeness of all imported data or executed lab mutations. The displayed trigger statement is truncated; do not assert its full body. No Q2–Q6 mutations or export are evidenced yet.

**Next:** Do not repeat the six schema queries. The four existing Workbench result tabs contain their definitions: inspect Result 1 (users), Result 2 (userEmail), Result 3 (userPhone), Result 4 (occupation) for exact columns, defaults, PKs and FK references; copy the relevant DDL into the authorized chat if needed. Resolve actual lookup IDs and check the intended unique user before Q2. If absent, execute the verified Q2 INSERT, omitting created, and confirm the row and generated timestamp. Proceed through the remaining D-003 map as authorized. Record actual evidence in the existing Word worksheet and append the short field report; no raw student data in public Git. This update supersedes the earlier import-only status; do not restart the import.

### Answer map — prior draft, not runtime evidence
| Item | Verified worksheet requirement and prior draft approach | Local acceptance |
|---|---|---|
| Q1 (20) | Actual example database SQL backup. Original worksheet allows unzipped SQL; LMS reportedly asks for ZIP. No explicit pre/post-operation timing in worksheet. | Export real database; if a pre-change backup is still possible, preserve it locally; do not undo completed work. Verify requested final format. |
| Q2 (16) | Insert into users, supplying userId and at least five other fields including unique username (max 20 chars); omit created. Draft used userid, firstname, lastname, middleName, username, gender, userStatusId, userTypeId. | Check exact live schema, FK values and existing intended user; insert only if absent; verify generated created. Prior draft used status/type 1/1, trigger usersCreatedDateInsert; confirm rather than assume. |
| Q3 (16) | Four separate INSERTs: two emails using userEmail(userId,userEmail,userEmailTypeId); two phones using userPhone(userId,userPhone,userPhoneTypeId). Omit auto-increment IDs. | Use same user; validate lookup IDs first. Draft email types 1/3 and phone types 1/2 are candidates only. Verify two of each before Q5; don't duplicate existing records. |
| Q4 (16) | JOIN users and userEmail on user ID. Return lastName, firstName, userName, userEmail only, for firstname mary. | Execute correct query, report output columns and row count, no personal result rows in Git. |
| Q5 (16) | Delete a single one of the lab user's inserted phone records. Prior draft matched userId plus phone value and LIMIT 1. | Preview unique target (prefer confirmed phone primary key plus userId); check ROW_COUNT() immediately after DELETE and one intended phone remains. |
| Q6 (16) | Two SQL statements: select every column for the specified occupation, then update the new user's occupationId. Prior draft candidate ID 187. | Find Computer Software Engineers by name in actual occupation table, verify one matching row and actual ID, update only intended user, confirm association. If already correct, report verified no-op. |

### Minimal SQL guide (read-only first; no placeholder may be run literally)
```sql
USE example1512O;
SHOW CREATE TABLE users;
SHOW CREATE TABLE userEmail;
SHOW CREATE TABLE userPhone;
SHOW CREATE TABLE occupation;
SHOW TRIGGERS;
```
Use existing confirmed lab user if present, otherwise choose student-approved values and check uniqueness. Prior draft's personal values are intentionally withheld from public Git. Q2 uses one INSERT with the eight columns above, then SELECT userid, username, created for the intended user. Q3 uses the three columns listed for each of the four INSERT statements. Verify actual constraints and lookup rows before mutations. Q4 draft query shape:
```sql
SELECT u.lastname AS lastName, u.firstname AS firstName,
       u.username AS userName, e.userEmail
FROM users AS u
INNER JOIN userEmail AS e ON u.userid = e.userId
WHERE u.firstname = 'mary';
```
Q5 use the actual confirmed phone ID and intended user, not an unbound placeholder or broad predicate. Q6 lookup shape: SELECT * FROM occupation WHERE occupation = 'Computer Software Engineers'; then use the observed unique occupationId and confirmed user ID in UPDATE. Recheck resulting association. Stop for actual SQL error/unsafe ambiguity; no schema changes or disabling constraints to force success. If progress already exists, validate it instead of repeating.

### Finish and report
Student fills name and verified SQL into the original worksheet copy (the draft is a reference, not evidence); ensure the six questions and exact statement counts are satisfied. Export genuine SQL from Workbench, package per LMS, review final documents. Restore check is additional quality assurance, not stated worksheet requirement; report if not performed and do not risk overwriting current schema. The student submits, and only actual receipt establishes submission.

Append one compact 5W report tagged D-003 in FSO/FSO-REPORT.md, using next unused report ID. Include Q1–Q6 each OBSERVED PASS / REPORTED / BLOCKED / NOT RUN; statement counts, actual generated created status, contact counts before/after delete, join columns/count, occupation lookup count/ID and update postcondition, actual error if blocked. Include Word answers filled, export/ZIP status, receipt status and next concrete action. Keep names, IDs identifying the student, raw result rows, worksheet text, credentials and private links out of Git. No duplicate handoff or other repository writes. Preserve old bytes and verify report commit. If write fails, return report in chat marked NOT COMMITTED.

Older orders below are history. This order supersedes D-002 and D-001. Coordinator has inspected the worksheet and prior draft directly; field agent should not spend context reconstructing them.

## CURRENT ORDER — D-002 (supersedes D-001, 2026-11-25)
**Read this order only.** R-001 and the operator report successful import into example1512O. Accept as USER_REPORTED; do not repeat installation, extraction, import or general database verification. The next task is answering the actual Word worksheet using the imported database, not preparing another handoff. Work in the existing Workbench SQL editor. Follow actual instructor requirements and course AI-use policy.

**Field mission:** locate the instructor Word worksheet and existing draft answer document if available; inspect Q2–Q6 requirements locally, not unrelated history. If the draft is absent, proceed from the original worksheet; do not reconstruct missing requirements or copy private material into Git. Keep the Word document and SQL/result evidence locally. Use minimal schema checks directly needed for the current operation.

1. Run `USE example1512O;` and `SHOW CREATE TABLE users;` (if naming differs, locate the actual table). Inspect relevant triggers/defaults and referenced lookup tables only as needed. Return exact non-sensitive column names/types, required columns, key constraints, and how created is populated. No full database dump, raw personal records, or unnecessary table scans.
2. Q2: inspect the existing intended lab user by its exact unique identifier first. If absent, construct/execute the worksheet's required INSERT using confirmed schema, valid keys and student-approved values; omit created. If already present, validate rather than insert again. SELECT the intended row to verify created and required fields. Report whether newly inserted or already present, outcome and actual count.
3. If Q2 passes and the worksheet and schema unambiguously support the next steps, continue Q3–Q6 sequentially without waiting for a new chat: inspect only relevant table definitions; verify two email and two phone rows before deletion; run the required join with its exact four columns and filter; preview and delete exactly the intended newly inserted phone row, verify affected count and remaining contact; resolve the requested occupation by its exact live name and verify the user's updated association. Do not replay completed mutations. Stop at the first unresolved constraint, unsafe ambiguity, or SQL error; return the exact redacted error and necessary schema facts. No guesses, no broad UPDATE/DELETE, no disabling integrity checks.
4. As each question is completed, place the actual SQL and observed results in the local Word worksheet/draft according to instructor directions. Do not invent answers or claim a result merely because SQL was drafted. Capture actual result evidence locally. Q1: check whether the worksheet requires a pre-operation dump, final dump, or other specific timing/format; report the requirement and status. Do not overwrite the original source or working schema. Final export/restore and submission are separate gates.

**Return to coordinator — append ONE short R-002 report in FSO/FSO-REPORT.md after this batch or first blocker (or earlier if context is running low):**
- Who / When / Where / Why: actual operator, observation time (or UNKNOWN), Workbench + schema, worksheet task.
- What: worksheet present? draft present? Q1 dump requirement/timing confirmed? Use a brief public-safe paraphrase only.
- Q2–Q6: for each, mark OBSERVED PASS / REPORTED / BLOCKED / NOT RUN; actual result counts or column names as relevant; report Q2 created populated?, Q3 two+two confirmed before Q5?, Q4 four columns/filter/row count?, Q5 exactly one affected and remaining count?, Q6 lookup unique and association verified?
- Necessary schema facts and first exact redacted error, if blocked; next single action and acceptance check. No raw student data, private links, personal identifiers, credentials or proprietary assignment text in public Git.
- Word status: which questions actually filled/verified locally, which pending; final export/restore and submission status separately.

Aim for 150–250 words plus indispensable schema/error facts; do not omit evidence to hit a limit. Append using fresh blob SHA, preserve original bytes and verify commit. If no safe write, return the report in chat marked NOT COMMITTED. No other repository writes. Coordinator reads report on explicit request. Old D-001 and later sections below are retained history; do not execute them as new orders.

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
