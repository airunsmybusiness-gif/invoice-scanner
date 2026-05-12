# Directive: Cape Bretoner's admin workflows — Debug Loop

## Goal
Give Lily a structured path to identify and fix admin workflow bugs without losing member data or missing a community commitment.

## Inputs
- Bug description: which member, which request, what went wrong, when it was noticed
- Email delivery logs from the email service
- App server logs

## Outputs
- Root cause documented in one sentence
- Fix applied without altering any member or request record incorrectly
- New testing checklist item for the failure scenario

## Process
1. Categorise the bug: data display issue, status-transition logic, notification failure, or report calculation.
2. For notification failures: check the email service delivery log first; look for bounce codes, spam blocks, or auth errors before touching app code.
3. For status-transition bugs: read the request record directly from the database to confirm what state it is actually in.
4. For report calculation bugs: manually calculate the expected value from the raw records and compare with the report output.
5. Reproduce the bug in staging using a test member and request with the same data pattern.
6. Apply the minimal fix and re-run the full testing checklist.
7. If the bug caused a community member to miss a notification or receive incorrect information, send a manual correction before the fix ships.
8. Add one new checklist item for the failure scenario.

## Edge Cases
- Bug only reproducible with a specific member's data: Create a anonymised copy of the record in staging for reproduction; never use real member data in a development environment.
- Fix requires changing a member's status record: Get Lily's explicit approval before modifying any member record, even in a fix context.

## Definition of Done
- [ ] Bug is categorised before any code is written.
- [ ] Root cause is documented in one sentence.
- [ ] Reproduction uses anonymised staging data, not real member records.
- [ ] Fix passes the full testing checklist.
- [ ] Any community member affected by the bug has received a manual correction before the session closes.

## Self-Anneal Log
