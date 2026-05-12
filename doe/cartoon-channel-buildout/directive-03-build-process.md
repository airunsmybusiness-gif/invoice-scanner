# Directive: cartoon-channel buildout — Build Process

## Goal
Establish a web-first build and deployment process for the cartoon channel's content management dashboard that Lily can run and maintain solo.

## Inputs
- Web app framework (React via Expo Web or a dedicated web framework)
- Cloud database for episode records
- YouTube Data API for scheduling uploads

## Outputs
- Local dev server running the dashboard
- Database seeded with sample episodes in multiple stages
- Deployment checklist for publishing a new dashboard version

## Process
1. Clone the repo and start the dev server; confirm the Kanban board loads in the browser.
2. Copy `.env.example` to `.env.local`; fill in the database URL and YouTube API credentials.
3. Run the seed script to create six test episodes spread across all six pipeline stages.
4. Confirm each stage column on the Kanban board shows at least one episode card.
5. To deploy: build the web app, push to the hosting provider, and verify the dashboard loads at the production URL before announcing the deploy.

## Edge Cases
- YouTube API credentials expire: The dashboard should still load and allow pipeline management; only the scheduling feature should be unavailable, with a clear "reconnect YouTube" prompt.
- Seed script creates duplicate episodes on re-run: Add a check to skip seeding if episodes already exist.

## Definition of Done
- [ ] Dev server starts and Kanban board loads from a clean clone.
- [ ] All six pipeline stages have at least one seeded episode card.
- [ ] Environment variables are documented in `.env.example`.
- [ ] Deployment checklist is written and tested end-to-end.

## Self-Anneal Log
