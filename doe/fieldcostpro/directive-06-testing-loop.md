# Directive: FieldCostPro — Testing Loop

## Goal
Ensure that every code change leaves cost tracking, budget calculations, and exports working correctly before reaching project managers and field workers.

## Inputs
- Code change ready to merge
- Seeded test project with budget and sample cost entries
- Physical mobile device and a desktop browser

## Outputs
- Pass/fail result for each critical-path item
- Clear go/no-go decision for the merge
- Any regressions filed as bug reports

## Process
1. Deploy the change to the staging environment.
2. Run the critical-path checklist on mobile: (a) create a test project with a budget, (b) log three cost entries in different categories, (c) verify the BudgetGauge updates correctly, (d) log a cost that exceeds the remaining budget and confirm the over-budget state.
3. Open the web dashboard and verify the same project reflects all four cost entries.
4. Trigger an export and confirm the CSV contains all entries grouped by category with correct totals.
5. Test offline: disable network on mobile, log a cost, re-enable, confirm it syncs without duplication.
6. Record all results with date, tester, and device/browser model.

## Edge Cases
- Export produces incorrect totals: This is a blocking bug; do not merge until resolved.
- Offline sync creates a duplicate entry in staging: Treat as blocking; investigate the sync deduplication logic before merging.

## Definition of Done
- [ ] All five critical-path steps pass on mobile and web.
- [ ] Export CSV has correct entries and totals.
- [ ] Offline sync test passes with no duplicates.
- [ ] Test results are logged with date and environment.

## Self-Anneal Log
