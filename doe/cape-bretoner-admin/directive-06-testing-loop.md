# Directive: Cape Bretoner's admin workflows — Testing Loop

## Goal
Ensure every dashboard change leaves member records, request workflows, and notifications working correctly before it reaches real community members.

## Inputs
- Code change ready to merge
- Seeded member records and requests in the staging environment
- Sandbox email address for notification testing

## Outputs
- Pass/fail result for each critical-path item
- Go/no-go decision for the merge
- Any regressions filed as issues

## Process
1. Deploy the change to the staging environment.
2. Run the critical-path checklist: (a) create a new request manually, (b) move it from "New" to "In Progress" to "Resolved", (c) confirm a notification email arrives at the sandbox address, (d) confirm the resolved request links to the correct member record, (e) publish a test announcement and confirm it is saved.
3. Verify the monthly summary generates correctly with the test data (trigger it manually if needed).
4. Record pass or fail for each step with date and tester.
5. If all steps pass, merge and run steps (a)–(c) in production with a clearly labelled test request; delete the test request after confirming.

## Edge Cases
- Notification email goes to spam in the sandbox: Check email headers for missing SPF/DKIM; treat recurring spam delivery as a blocking issue.
- Monthly summary manual trigger not available: Test summary generation by setting a test date parameter in the function call.

## Definition of Done
- [ ] All five critical-path steps pass in staging.
- [ ] Notification email is delivered (not spam-filtered) in the sandbox.
- [ ] Monthly summary generates correctly with test data.
- [ ] Production smoke test is run and the test request is deleted after confirmation.

## Self-Anneal Log
