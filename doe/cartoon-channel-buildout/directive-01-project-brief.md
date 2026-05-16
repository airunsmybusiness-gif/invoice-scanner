# Directive: cartoon-channel buildout — Project Brief

## Goal
Give Lily a production tracker that moves each cartoon episode from idea to published YouTube video through a defined stage pipeline — so nothing gets lost between concept, animation, and upload.

## Inputs
- Lily's current episode production workflow (however informal)
- YouTube channel credentials for automated upload
- Number of episodes planned per month (sets the pace the tool must support)

## Outputs
- A web app with an episode board showing every episode and its current stage
- Automated YouTube upload triggered when an episode is approved for publishing
- 48-hour performance snapshot stored per episode

## Process
1. Confirm the production stages Lily actually uses (Concept, Script, Animation, Review, Scheduled, Published) and adjust to match her real workflow.
2. Agree on which stages require a file attachment and which are status-only.
3. Connect the YouTube Data API with Lily's channel credentials; confirm upload and scheduling permissions.
4. Build the episode board first so Lily can track in-flight episodes immediately, before automation is wired up.
5. Add automated upload only after Lily has used the board manually through at least one full episode cycle.

## Edge Cases
- Multiple episodes in production simultaneously: The board must show all of them without confusion; use stage columns or a filtered list.
- Lily works alone: No team assignment features needed; all actions are attributed to a single admin account.

## Definition of Done
- [ ] Every in-flight episode is visible on the board with its current stage and latest file.
- [ ] An episode can be scheduled and published to YouTube without Lily opening the YouTube Studio UI.
- [ ] 48-hour performance data is collected automatically and visible on the episode card.
- [ ] Lily can onboard a new episode in under two minutes.

## Self-Anneal Log
