# Directive: yt-automation — Testing Loop

## Goal
Ensure every new feature and bug fix is validated before it reaches the live channel, protecting Lily's content schedule.

## Inputs
- New feature branch or bug fix ready for review
- Checklist of critical paths (schedule, upload, analytics fetch)
- Staging YouTube channel for safe upload tests

## Outputs
- Pass/fail result for each critical path
- A list of any regressions found
- Green light to merge and deploy

## Process
1. Before merging any change, run the critical-path checklist manually against the staging environment.
2. Critical paths to verify: (a) add and save a new video entry, (b) trigger a manual upload to the staging channel, (c) confirm status moves to "live", (d) confirm the analytics fetch returns data.
3. If all four paths pass, the change is cleared to merge.
4. After merging, re-run the checklist against the production environment within 30 minutes.
5. Log the test date, tester (Lily), and pass/fail result in the Self-Anneal Log of the affected directive.

## Edge Cases
- Staging channel quota exhausted: Use a short unlisted test video (under 1 minute) to stay within free quota.
- Production test fails post-merge: Roll back the deploy immediately, then open a debug session before attempting the fix.

## Definition of Done
- [ ] Critical-path checklist exists with at least four steps.
- [ ] Every merge has a logged test result.
- [ ] A rollback procedure is documented and has been tested at least once.
- [ ] No change ships to production without a passing staging test.

## Self-Anneal Log
