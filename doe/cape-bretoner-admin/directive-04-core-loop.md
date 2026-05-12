# Directive: Cape Bretoner's admin workflows — Core Loop

## Goal
Define the repeating cycle that keeps the community running: receive request → process and respond → record outcome → communicate result.

## Inputs
- Incoming request (type, requester name, contact, description)
- Lily's action (status change, note, resolution)
- Announcement or response to be published or sent

## Outputs
- Request resolved and status updated to "Resolved"
- Requester notified of the outcome
- Outcome recorded in the member or request record

## Process
1. A new request arrives (submitted via a public form or entered manually by Lily); it appears on the Requests screen with status "New".
2. Lily opens the RequestCard, reads the details, and changes the status to "In Progress"; an optional internal note can be added.
3. Lily works the request (looks up a member record, prepares a response, coordinates a resource).
4. When complete, Lily writes a resolution note, changes the status to "Resolved", and triggers a notification email to the requester.
5. The resolved request is archived and linked to the member record if the requester is a member.
6. Lily publishes any relevant announcement to the community via the Announcements screen.

## Edge Cases
- Requester is not a member: Allow requests to be created without a linked member record; link retrospectively if the person later joins.
- Duplicate request from the same person: Surface a warning when a new request matches a recent open request from the same contact; let Lily merge or keep separate.

## Definition of Done
- [ ] A request can move from "New" to "Resolved" with a notification sent in under 5 minutes of Lily's time.
- [ ] Resolution notes are stored on the request record.
- [ ] Resolved requests link to member records when applicable.
- [ ] Announcements can be composed and published independently of the request workflow.

## Self-Anneal Log
