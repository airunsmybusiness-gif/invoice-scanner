# Directive: FieldCostPro — Debug Loop

## Goal
Give Lily a structured process for diagnosing and fixing cost-tracking or sync bugs without corrupting any project's financial records.

## Inputs
- Bug description including project name, cost entry involved, and the symptom
- Server and sync logs
- App version and device or browser where the bug was seen

## Outputs
- Root cause documented in one sentence
- Fix verified against the affected project's data
- New testing checklist item for the failure scenario

## Process
1. Categorise the bug: UI display issue, calculation error, sync failure, or export error.
2. For calculation errors: fetch the raw cost entries from the database and manually verify the expected total; compare with what the app shows.
3. For sync failures: check the sync log for the entry ID, identify whether the failure was on upload or on the device, and determine if a duplicate was created.
4. Reproduce the bug in staging using a test project with the same data shape.
5. Apply the minimal fix and re-run the full testing checklist.
6. If the bug caused a wrong total to be shown to a client, notify Lily immediately so she can correct it manually before the fix ships.
7. Add a checklist item for the exact failure mode.

## Edge Cases
- Bug caused incorrect export delivered to a client: Regenerate the correct export immediately as the first action; debugging comes second.
- Root cause is in the shared sync library, not the app code: Isolate the library version, update it in staging, re-test, and pin the working version in `package.json`.

## Definition of Done
- [ ] Bug is categorised before any code is written.
- [ ] Root cause is documented in one sentence.
- [ ] Reproduction confirmed in staging.
- [ ] Fix passes the full testing checklist.
- [ ] Incorrect data delivered to any client is corrected before the debug session closes.

## Self-Anneal Log
