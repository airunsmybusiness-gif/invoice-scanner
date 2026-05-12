# Directive: yt-automation — Build Process

## Goal
Establish a repeatable, solo-dev-friendly process for setting up the environment, running the app locally, and deploying a new version.

## Inputs
- Chosen stack (React Native + Expo, cloud functions for scheduling logic)
- YouTube Data API credentials
- Target platforms (web first, iOS/Android later via Expo Go)

## Outputs
- Local dev server running at a known address
- Working cloud function endpoint for job scheduling
- Deployment checklist for pushing a new build

## Process
1. Clone the repo and run `npx expo start` to confirm the dev server boots.
2. Copy `.env.example` to `.env.local` and fill in YouTube API key and OAuth client ID.
3. Verify the scheduling cloud function is reachable by calling its health-check endpoint.
4. Run the app in a browser using Expo's web target; confirm the Home screen loads.
5. To deploy: increment the version in `app.json`, run the build script, push to the hosting target, and update the changelog with what changed.

## Edge Cases
- `npx expo start` fails on first run: Check Node version (requires 18+) and delete `node_modules`, then reinstall.
- Cloud function cold-start timeout: Retry the health-check once after 5 seconds before declaring the environment broken.

## Definition of Done
- [ ] `npx expo start` boots without errors on a clean clone.
- [ ] Environment variables are documented in `.env.example`.
- [ ] Cloud function health-check returns 200 in the local environment.
- [ ] A new version can be deployed end-to-end by following the checklist with no undocumented steps.

## Self-Anneal Log
