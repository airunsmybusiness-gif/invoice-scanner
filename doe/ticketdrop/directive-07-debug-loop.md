# Directive: TicketDrop — Debug Loop

## Goal
Resolve payment, listing, and delivery bugs quickly while protecting user funds and preventing duplicate charges.

## Inputs
- Bug report with transaction ID (if payment-related), listing ID, and a description of what went wrong
- Payment provider dashboard logs
- App server logs

## Outputs
- Root cause documented in one sentence
- Fix applied and verified without affecting legitimate transactions
- New checklist item covering the bug scenario

## Process
1. Identify whether the bug is in the payment flow, the listing state machine, or the ticket delivery step.
2. Pull the transaction ID from the payment provider dashboard and check its status (succeeded, pending, failed, refunded).
3. Compare the payment provider status with the record in the app database; the discrepancy is usually the root cause.
4. Never modify a payment record directly; use the payment provider's API or dashboard for any refunds or voids.
5. Reproduce the bug in the staging environment using a sandbox transaction with the same parameters.
6. Apply the fix, re-run the critical-path checklist, and confirm the reproduction no longer occurs.
7. Add a checklist item for the exact failure mode.

## Edge Cases
- Buyer was charged but never received the ticket: Treat as highest priority; manually deliver the ticket and issue an apology before debugging the root cause.
- Bug only reproducible in production: Enable request-level logging for the affected endpoint for one hour, reproduce once, pull logs, then disable.

## Definition of Done
- [ ] Root cause is identified and documented before any code change.
- [ ] No payment record is modified directly in the database.
- [ ] Bug is reproduced in staging before the fix is written.
- [ ] Fix passes the full critical-path checklist.
- [ ] New checklist item covers the failure mode.

## Self-Anneal Log
