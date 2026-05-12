# Directive: FieldCostPro — Core Loop

## Goal
Define the repeating cycle that keeps project costs tracked in real time: create project → log costs in the field → review budget status → export report.

## Inputs
- Project name, budget amount, and start date (entered by project manager)
- Cost entries: description, amount, category, optional receipt photo (entered by field worker)
- Export trigger from the project manager

## Outputs
- Running budget consumed figure visible to all parties
- Cost log with full entry history
- Exportable cost report (CSV or PDF)

## Process
1. Project manager creates a project with name, total budget, and start date; the project appears on all team members' project lists.
2. Field worker opens the project, taps "Add Cost", enters description, amount, and category, optionally attaches a receipt photo, and saves.
3. The entry syncs to the cloud; the BudgetGauge updates immediately on the project detail screen.
4. Project manager reviews the running total and individual entries from the web dashboard at any time.
5. When the project concludes, the project manager taps "Export Report"; the system generates a CSV or PDF with all cost entries grouped by category.

## Edge Cases
- Field worker logs a cost offline: Entry is stored locally and syncs when connectivity returns; a "pending sync" indicator shows until confirmed.
- Cost entry exceeds remaining budget: Allow the entry but change the BudgetGauge to the red over-budget state and show a notification to the project manager.

## Definition of Done
- [ ] Project creation to cost entry takes under 60 seconds for a field worker.
- [ ] BudgetGauge updates within 5 seconds of a cost entry being saved.
- [ ] Offline cost entries sync without data loss when connectivity returns.
- [ ] Export produces a correctly grouped CSV or PDF.

## Self-Anneal Log
