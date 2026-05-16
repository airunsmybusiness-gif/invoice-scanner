# Directive: RigBooks — Project Brief

## Goal
Give rig operators and small oilfield contractors a no-fuss mobile app to track jobs and expenses in the field — so the numbers are ready at month end without digging through receipts or relying on memory.

## Inputs
- Operator's list of job types and recurring expense categories
- Target platform: iOS and Android via Expo; operator is unlikely to use a desktop for daily entry
- Existing records (paper or spreadsheet) to migrate if needed

## Outputs
- Mobile app where an operator can create a job and log expenses against it in the field
- Running total per job visible at a glance
- Monthly summary exportable for the accountant or owner-operator's own records

## Process
1. Confirm the minimum data an operator needs per job (job name, client, date, status) and per expense (description, amount, category, receipt photo optional).
2. Agree on the export format the accountant or owner actually uses; build to that format from day one.
3. Build job creation and expense entry first; get the app on one operator's phone before adding any reporting.
4. Add the monthly summary and export once the entry flow has been used for at least two real jobs.
5. Keep the UI to the fewest possible taps per entry; field conditions make detailed data entry painful.

## Edge Cases
- Operator works offline at the rig site: All entry must work without a network connection; sync when back in range.
- Operator loses their phone: Data must be backed up to the cloud automatically; no data should live only on the device.

## Definition of Done
- [ ] An operator can create a job and add three expenses in under three minutes on a physical device.
- [ ] All data syncs to the cloud automatically; deleting and reinstalling the app restores all records.
- [ ] Monthly summary export is in a format the accountant can open without additional tools.
- [ ] The app works fully offline and syncs without errors when reconnected.

## Self-Anneal Log
