# Directive: cartoon-channel buildout — Debug Loop

## Goal
Resolve pipeline and upload bugs quickly so no episode is lost, delayed, or published in a broken state.

## Inputs
- Bug description: which episode, which stage, what went wrong
- YouTube upload logs or API error codes
- Dashboard server logs

## Outputs
- Root cause documented in one sentence
- Fix applied without affecting other episodes in the pipeline
- New checklist item for the failure scenario

## Process
1. Identify which layer the bug is in: the Kanban UI, the stage-transition logic, the file upload, or the YouTube API call.
2. For upload failures: check the YouTube API error code first (quota exceeded, auth expired, file format rejected) before looking at app code.
3. For stage-transition bugs: inspect the episode record in the database to see what state it is actually in vs. what the UI shows.
4. Reproduce the bug in staging using an episode with the same metadata and file.
5. Apply the minimal fix and re-run the full testing checklist.
6. If a scheduled episode failed to publish, manually trigger the upload immediately to protect the content calendar.
7. Add one new checklist item covering the exact failure scenario.

## Edge Cases
- Episode stuck between two stages with neither the old nor new state clearly set: Set the stage manually in the database to the last confirmed good state, then reproduce and fix.
- YouTube auth token expired mid-upload: Implement automatic token refresh; treat any bug in this path as high priority since it blocks all future uploads.

## Definition of Done
- [ ] Bug layer is identified before any code is written.
- [ ] Root cause is documented in one sentence.
- [ ] Bug is reproduced in staging.
- [ ] Fix passes the full testing checklist.
- [ ] Any episode that missed its publish window is manually uploaded before the debug session closes.

## Self-Anneal Log
