# Directive: Cape Bretoner's admin workflows — Project Brief

## Goal
Give Lily a single, simple web dashboard to manage all incoming community requests, member records, and announcements for the Cape Bretoner organisation — eliminating manual email tracking and spreadsheet juggling.

## Inputs
- Lily's list of recurring admin tasks (handling requests, updating member info, sending announcements)
- Existing member data to be migrated or entered
- Lily's available time budget: solo operator, part-time availability

## Outputs
- A working web app Lily can open in any browser with no installation
- Member directory with contact and status records
- Request inbox with status tracking and email notifications
- Announcements screen for publishing to the community

## Process
1. Confirm the three core problems Lily wants solved first (request tracking, member records, or announcements) and rank them by urgency.
2. Agree on the hosting approach: a managed platform (Railway, Render, or Vercel) that Lily can deploy to without a dedicated server.
3. Define the data model for members and requests; confirm what fields are required vs. optional.
4. Build and ship the highest-priority screen first; let Lily use it before building the next.
5. After each screen ships, run one real admin task through it with Lily to confirm it reduces her workload.

## Edge Cases
- Lily is the only user: No multi-user auth is needed initially; a single admin password is sufficient.
- Existing data lives in a spreadsheet: Plan a one-time import step; do not block the build on it.

## Definition of Done
- [ ] Lily can complete her most common weekly admin task (handle a member request end-to-end) faster than before.
- [ ] No critical data lives only in email or spreadsheet after migration.
- [ ] App is accessible from any device Lily uses without installing software.
- [ ] Lily can add, edit, and look up any member record without help.

## Self-Anneal Log
