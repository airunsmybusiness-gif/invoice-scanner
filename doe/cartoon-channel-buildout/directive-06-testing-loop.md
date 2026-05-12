# Directive: cartoon-channel buildout — Testing Loop

## Goal
Ensure every dashboard change leaves the episode pipeline and YouTube scheduling intact so no episode misses its publish window.

## Inputs
- Code change ready to merge
- Seeded test episodes in all pipeline stages
- Staging YouTube channel for upload tests

## Outputs
- Documented pass/fail per checklist item
- Go/no-go decision for the merge
- Any regressions filed as issues

## Process
1. Before merging, run the critical-path checklist in the staging environment: (a) create a new episode card, (b) move it through all six stages, (c) attach a test video file in the Scheduled stage, (d) trigger a manual upload to the staging channel, (e) confirm the card moves to "Published" and the YouTube URL is stored, (f) confirm the 48-hour performance fetch is queued.
2. Verify the Kanban board still shows the correct episode count in each stage after the full flow.
3. Record pass or fail for each step, plus the tester and date.
4. If all steps pass, merge and re-run steps (d)–(f) in production with a private test video.

## Edge Cases
- Staging channel not available: Use an unlisted video on the production channel with a clearly named "TEST" title; delete it after the test.
- 48-hour performance fetch cannot be tested in real time: Manually trigger the fetch function with a mock timestamp and confirm it attaches the result to the correct episode card.

## Definition of Done
- [ ] All six critical-path steps pass in staging before any merge.
- [ ] Kanban board stage counts are correct after the full flow.
- [ ] Production smoke test is run after every merge.
- [ ] Test results are logged with date, tester, and environment.

## Self-Anneal Log
