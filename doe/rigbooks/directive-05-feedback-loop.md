# Directive: RigBooks — Feedback Loop

## Goal
Surface spending patterns across jobs so Lily can spot where costs are running high and adjust estimates for future jobs.

## Inputs
- Closed job summaries (category totals, job duration, client)
- Historical expense data (rolling 90 days)
- Lily's manual tags on jobs (e.g., "over budget", "profitable")

## Outputs
- Monthly category breakdown chart (fuel, parts, labour, other)
- Top-three cost drivers for the current month
- Per-job profitability note if a revenue field is provided

## Process
1. After each job is closed, its expense totals feed the aggregate store.
2. The Reports screen recalculates category breakdowns on open.
3. Each month, the system flags the three categories with the highest spend.
4. If Lily has entered a revenue figure for a job, the system shows a simple margin (revenue minus costs).
5. Lily can tag a job with a one-word label; tags appear in the monthly report to group similar jobs.

## Edge Cases
- No closed jobs yet: Reports screen shows an empty state with instructions to close the first job.
- Revenue field left blank: Hide the margin calculation rather than showing zero or an error.

## Definition of Done
- [ ] Monthly category breakdown appears after at least one job is closed.
- [ ] Top-three cost drivers are highlighted on the Reports screen.
- [ ] Margin shows correctly when a revenue value is present and is hidden when it is not.
- [ ] Job tags appear in the monthly report.

## Self-Anneal Log
