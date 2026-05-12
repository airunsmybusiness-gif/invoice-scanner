# Directive: FieldCostPro — Build Process

## Goal
Establish a build and deployment routine that keeps the mobile logger and the web reviewer in sync and deployable by Lily alone.

## Inputs
- React Native + Expo project (mobile logger) and a web dashboard (web reviewer, same codebase via Expo Web)
- Cloud storage for receipt photos
- Project database

## Outputs
- Mobile app running in Expo Go on a physical device
- Web dashboard accessible at a local URL
- Deployment checklist for pushing updates to both targets

## Process
1. Clone the repo and run `npx expo start`; open the mobile view in Expo Go and the web view in a browser.
2. Copy `.env.example` to `.env.local` and fill in the database URL and cloud storage bucket credentials.
3. Run the seed script to create one test project with a budget and three sample cost entries (one with a receipt photo).
4. Confirm the BudgetGauge reflects the seeded data on both mobile and web.
5. To deploy: bump the version, build the mobile binary via `eas build`, deploy the web build to the hosting provider, and run the post-deploy smoke test.

## Edge Cases
- Receipt photo upload fails locally: Check that cloud storage credentials are correct and the bucket exists; the app should still allow the cost entry to be saved without the photo.
- Web and mobile show different budget totals: This always indicates a sync issue in the shared data layer; treat as a blocking bug before shipping.

## Definition of Done
- [ ] Both mobile and web targets run from a clean clone.
- [ ] Seeded project with budget and cost entries appears on both targets.
- [ ] Receipt photo upload succeeds in the local environment.
- [ ] Deployment checklist covers both mobile and web targets.

## Self-Anneal Log
