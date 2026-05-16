# Directive: FieldCostPro — Project Brief

## Goal
Give field crews and project managers a fast mobile-first way to log costs in real time and see live budget status — replacing paper tickets, delayed spreadsheets, and end-of-project cost surprises.

## Inputs
- Project list with budgets (from the project manager)
- Cost categories agreed on by the team (labour, materials, equipment, subcontractor, other)
- Target platforms: iOS and Android (field workers use both)

## Outputs
- Mobile app where a field worker can log a cost in under 60 seconds
- Web dashboard where a project manager sees live budget consumption per project
- Exportable cost report (CSV or PDF) for invoicing and record-keeping

## Process
1. Confirm the cost fields that matter most to the field team; keep the entry form to five fields or fewer.
2. Decide on the sync strategy: real-time where possible, offline-first with queue where not.
3. Build the cost-entry flow on mobile first; get it in the hands of one field worker before adding the dashboard.
4. Add the BudgetGauge and project-level summary once cost entries are flowing reliably.
5. Add export only after the project manager has validated that the data inside the app matches their expected format.

## Edge Cases
- Field workers have limited phone storage: Keep the app under 20 MB installed; avoid bundling large assets.
- Project manager needs historical reports after a project closes: Closed projects must remain readable; never purge cost data.

## Definition of Done
- [ ] A field worker can log a cost, including an optional receipt photo, in under 60 seconds on a real device.
- [ ] The BudgetGauge reflects the latest entries within 5 seconds when online.
- [ ] Offline entries sync without data loss when connectivity is restored.
- [ ] A project manager can export a full cost report for a closed project at any time.

## Self-Anneal Log
