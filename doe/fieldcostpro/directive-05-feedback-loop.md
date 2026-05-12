# Directive: FieldCostPro — Feedback Loop

## Goal
Surface cross-project spending patterns so Lily and her clients can build better budgets on future projects.

## Inputs
- Completed project cost logs (all categories, totals, duration)
- Budget vs. actual figures for each completed project
- Category names used across projects

## Outputs
- Per-project budget accuracy score (actual / budget as a percentage)
- Category overspend report showing which categories consistently run over
- Rolling average cost per day for projects of similar type

## Process
1. When a project is marked complete, calculate its budget accuracy score and store it.
2. The Analytics screen shows all completed projects ranked by budget accuracy (best to worst).
3. Group categories across all completed projects and highlight any category that ran over budget in more than half of projects.
4. For projects tagged with a type (e.g., "road work", "utilities"), calculate the average cost per day and display it as a benchmark for future projects of the same type.
5. Lily reviews the analytics monthly and adds a note to any insight worth sharing with clients.

## Edge Cases
- Only one completed project: Show data as-is; note that benchmarks improve with more completed projects.
- Category names vary across projects (e.g., "labour" vs. "Labor"): Normalise to lowercase on save to prevent fragmentation.

## Definition of Done
- [ ] Budget accuracy score is calculated and stored when a project is marked complete.
- [ ] Category overspend report shows after two or more completed projects.
- [ ] Per-day cost benchmark appears for projects with a matching type tag.
- [ ] Category names are normalised at save time.

## Self-Anneal Log
