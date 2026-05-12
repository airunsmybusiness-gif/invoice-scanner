# Directive: TicketDrop — Build Process

## Goal
Set up and maintain a solo-developer build pipeline that lets Lily iterate on the marketplace quickly and ship safely.

## Inputs
- React Native + Expo project
- Payment provider credentials (for ticket purchases)
- Cloud database for listings and transactions

## Outputs
- Working local dev build with test listings seeded
- Payment sandbox connected and processing test transactions
- Deployment checklist for releasing an update

## Process
1. Clone the repo and run `npx expo start`; open in a browser or Expo Go.
2. Copy `.env.example` to `.env.local`; fill in the database URL and payment sandbox keys.
3. Run the seed script to create five test event listings in varied states (available, low stock, sold out).
4. Use the payment sandbox to complete a test purchase and confirm the transaction record is created.
5. To deploy: bump the version in `app.json`, run the production build, deploy the cloud functions, and smoke-test a purchase in the staging environment before promoting to production.

## Edge Cases
- Payment sandbox returns unexpected errors: Check that sandbox API keys are not mixed with production keys; keep them in clearly named env vars.
- Seed script fails on a fresh database: Ensure the schema migrations run before seeding; document the order in the README.

## Definition of Done
- [ ] App opens with seeded listings visible from a clean clone.
- [ ] Test purchase completes in the sandbox environment.
- [ ] All environment variable names are documented in `.env.example`.
- [ ] Deployment checklist is written and has been executed at least once end-to-end.

## Self-Anneal Log
