# Directive: RigBooks — Debug Loop

## Goal
Give Lily a structured path from a reported data problem to a confirmed fix, without risking loss of job or expense records.

## Inputs
- Bug description (which job, which expense, what went wrong)
- Device and OS version where the bug appeared
- App version number

## Outputs
- Root cause confirmed and written in one sentence
- Fix applied without corrupting existing records
- Regression test added to the critical-path checklist

## Process
1. Write down exactly what happened and what was expected; note the job name and expense details involved.
2. Check whether the issue is a display bug (data is correct in the database but shown wrong) or a data bug (wrong value stored).
3. For display bugs: trace the data from the store to the component and find where the value changes.
4. For data bugs: inspect the raw database record before touching any code.
5. Reproduce the bug with a test job containing the same data pattern; confirm the reproduction before writing a fix.
6. Apply the minimal fix, re-run the critical-path checklist, and confirm the test job no longer shows the bug.
7. Add one new checklist item for the exact bug scenario.

## Edge Cases
- Bug only appears in production, not locally: Enable verbose logging in the production build, reproduce once in the field, then pull logs before reverting to normal logging.
- Fix requires a database migration: Test the migration on a copy of the production data before applying; never run a migration on live data without a tested rollback script.

## Definition of Done
- [ ] Bug classified as display or data before any code is written.
- [ ] Reproduction confirmed with a test job.
- [ ] Fix passes the full critical-path checklist.
- [ ] New checklist item covers the bug scenario.
- [ ] No existing job or expense record was altered by the fix process.

## Self-Anneal Log
