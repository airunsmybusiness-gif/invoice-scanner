# Directive: RigBooks — Testing Loop

## Goal
Verify that every code change leaves the core bookkeeping workflow intact before it ships to field users.

## Inputs
- New feature or fix ready to merge
- Critical-path checklist for the core bookkeeping workflow
- A physical test device (iOS or Android)

## Outputs
- Documented pass/fail result for each checklist item
- Confirmation that the change is safe to ship
- Any regressions logged as new bug reports

## Process
1. Before merging, test these critical paths on a physical device: (a) create a job, (b) add three expenses, (c) verify running total, (d) close the job and check the summary, (e) open the Reports screen and confirm the monthly total updates.
2. Test offline mode: disable network, add an expense, re-enable network, confirm the expense syncs.
3. Record pass or fail for each step in the Self-Anneal Log of this directive.
4. If all steps pass, merge and rebuild via Expo Go for a final smoke test.
5. Log the build version, test date, and device model with the result.

## Edge Cases
- Physical device unavailable: Use the Expo iOS or Android simulator as a fallback; note this in the log.
- Sync test produces duplicate expense: Treat as a blocking bug; do not ship until resolved.

## Definition of Done
- [ ] All five critical-path steps pass on a physical device.
- [ ] Offline sync test passes with no duplicate entries.
- [ ] Test result is logged with build version, device, and date.
- [ ] No untested merge reaches production.

## Self-Anneal Log
