# Directive: yt-automation — Debug Loop

## Goal
Give Lily a fast, structured way to find, reproduce, fix, and confirm any bug without losing a scheduled upload.

## Inputs
- Bug report (what happened, what was expected, which video or feature was affected)
- Logs from the cloud function and the Expo dev console
- The schedule entry or API call that triggered the failure

## Outputs
- Confirmed root cause written in one sentence
- Fix applied to the codebase
- Regression test added to the critical-path checklist

## Process
1. When a bug is reported, write down: what the user did, what the system did, and what should have happened.
2. Check the cloud function logs first; most upload failures leave a clear error code.
3. Reproduce the bug locally using the same input that caused it in production.
4. Identify the smallest code change that makes the reproduction pass.
5. Apply the fix, re-run the full critical-path checklist, and confirm the original bug no longer appears.
6. Add one new checklist item covering the exact scenario that broke.

## Edge Cases
- Cannot reproduce locally: Add extra logging to the production function, trigger the bug again, then read the enriched logs before touching any code.
- Fix introduces a new failure: Revert the fix, update the reproduction case to cover both scenarios, and start over.

## Definition of Done
- [ ] Root cause is documented in one sentence.
- [ ] Bug is reproducible locally before any fix is attempted.
- [ ] Fix passes the full critical-path checklist.
- [ ] At least one new test item is added to the checklist covering the bug scenario.

## Self-Anneal Log
