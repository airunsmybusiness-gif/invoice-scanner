# Directive: TicketDrop — Testing Loop

## Goal
Protect buyers and sellers from broken purchases or lost tickets by validating every change against the critical transaction flow before it ships.

## Inputs
- Code change ready for review
- Sandbox payment credentials
- Seeded test listings in the staging environment

## Outputs
- Pass/fail result for each critical-path item
- Confirmation that the change can ship
- Any newly discovered issues filed as bug reports

## Process
1. Deploy the change to the staging environment before merging.
2. Run the critical-path checklist: (a) create a test listing, (b) complete a sandbox purchase, (c) confirm ticket delivery to the buyer, (d) confirm seller payout record created, (e) confirm sold listing is no longer available to other buyers.
3. Test the race-condition path: open the same listing in two browser tabs and attempt purchase from both simultaneously; confirm only one succeeds.
4. Record pass or fail for each step and the tester (Lily) and date.
5. If all steps pass, merge and re-run steps (b)–(e) in production with a low-value test listing.

## Edge Cases
- Race-condition test is difficult to time manually: Use two incognito windows and click buy within two seconds of each other; if the window is too small, test at least one-at-a-time and document the manual limitation.
- Staging payment fails for sandbox reasons (card expired): Refresh the sandbox test card and retry once before escalating.

## Definition of Done
- [ ] All five critical-path steps pass in staging before any merge.
- [ ] Race-condition test is attempted and result is logged.
- [ ] Production smoke test is run after every merge.
- [ ] All test results are logged with date, tester, and environment.

## Self-Anneal Log
