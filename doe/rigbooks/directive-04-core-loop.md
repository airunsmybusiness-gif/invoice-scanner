# Directive: RigBooks — Core Loop

## Goal
Define the repeating cycle that keeps RigBooks useful every job: open job → log costs → close job → view summary.

## Inputs
- Job name, client, and start date
- Expense entries (category, amount, note, date)
- Job close event triggered by Lily

## Outputs
- Running cost total visible at any point during the job
- Closed-job summary with itemised expense list and total
- Monthly report aggregating all closed jobs

## Process
1. Lily opens the app and taps "New Job"; enters job name, client name, and start date.
2. Throughout the job, Lily taps "Add Expense" and enters category, amount, and an optional note; each entry is saved immediately.
3. Running total is displayed on the job detail screen and updates in real time.
4. When the job is complete, Lily taps "Close Job"; the system locks the job from further edits and generates a summary.
5. The summary shows each expense line, a category breakdown, and the total.
6. At month end, the Reports screen aggregates all closed jobs into a single monthly total by category.

## Edge Cases
- Expense entered with wrong amount: Allow editing any expense on an open job; closed jobs are locked but Lily can reopen a job if needed.
- Two jobs open simultaneously: Support multiple open jobs; the job list is the default Home view so both are visible.

## Definition of Done
- [ ] New job can be created in under 30 seconds.
- [ ] Expense added to a job updates the running total immediately.
- [ ] Closing a job locks it and generates a summary.
- [ ] Monthly report aggregates all closed jobs in the current calendar month.

## Self-Anneal Log
