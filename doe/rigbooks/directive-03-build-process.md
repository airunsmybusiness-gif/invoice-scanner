# Directive: RigBooks — Build Process

## Goal
Establish a reliable, solo-maintainable process to set up, run, and ship the RigBooks mobile app.

## Inputs
- React Native + Expo project scaffolded from a known template
- Cloud database credentials (for job and expense storage)
- Target platforms: iOS and Android via Expo Go during development; standalone builds for distribution

## Outputs
- Local dev environment running in Expo Go on a physical device
- Database connected and seeded with sample job data
- Step-by-step deployment checklist for pushing a new standalone build

## Process
1. Clone the repo and run `npx expo start`; scan the QR code to open in Expo Go.
2. Copy `.env.example` to `.env.local` and fill in the database connection string.
3. Run the seed script to create one sample job with three linked expenses.
4. Confirm the Home screen loads and the sample job appears.
5. To ship: bump the version in `app.json`, run `eas build` for the target platform, submit via `eas submit`, and update the changelog.

## Edge Cases
- Expo Go version mismatch: Pin the Expo SDK version in `package.json` and document the required Expo Go version in the README.
- EAS build quota exhausted (free tier): Use a local build as a fallback via `expo run:android` or `expo run:ios`.

## Definition of Done
- [ ] App opens in Expo Go on a physical device from a clean clone.
- [ ] Sample job and expenses appear on first load.
- [ ] All environment variables documented in `.env.example`.
- [ ] `eas build` completes without error for at least one platform.

## Self-Anneal Log
