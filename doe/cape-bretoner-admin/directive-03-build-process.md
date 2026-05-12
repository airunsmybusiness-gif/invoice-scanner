# Directive: Cape Bretoner's admin workflows — Build Process

## Goal
Establish a solo-maintainable build and deployment process for the admin dashboard that Lily can update and ship without outside help.

## Inputs
- Web app project (React via Expo Web or a dedicated web framework)
- Cloud database for member records, requests, and announcements
- Email service credentials (for notification sending)

## Outputs
- Local dev server running the full admin dashboard
- Database seeded with representative member records and requests
- Deployment checklist covering code, database migrations, and post-deploy smoke test

## Process
1. Clone the repo and start the dev server; confirm the dashboard loads with the four workflow sections visible.
2. Copy `.env.example` to `.env.local`; fill in the database URL and email service credentials.
3. Run the seed script to create 10 member records and five requests in varied statuses (New, In Progress, Resolved).
4. Send a test notification email from the local environment and confirm it arrives.
5. To deploy: run any pending database migrations first, then build and push the web app, then verify the dashboard loads at the production URL and send a test notification.

## Edge Cases
- Database migration fails mid-deploy: Roll back to the previous migration version; never deploy app code that requires a migration that has not yet run.
- Email service rate limit in development: Use a sandbox email address that catches all outbound mail instead of sending real emails during development.

## Definition of Done
- [ ] Dashboard loads with all four sections from a clean clone.
- [ ] Seeded records and requests appear correctly.
- [ ] Test notification email is delivered in the local environment.
- [ ] Deployment checklist includes migration step before app deploy.

## Self-Anneal Log
