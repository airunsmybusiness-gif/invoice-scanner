# Directive: cartoon-channel buildout — Core Loop

## Goal
Define the weekly cycle that moves an episode idea from concept to a published video with a performance record.

## Inputs
- Episode concept (title, premise, target length)
- Production files as they become available (script, animation file, thumbnail)
- Publish date and time

## Outputs
- Episode published on the YouTube channel at the scheduled time
- Performance snapshot (views, watch time) collected 48 hours post-publish

## Process
1. Lily creates a new episode card with a title, premise, and target publish date; it enters the "Concept" stage.
2. As production progresses, Lily moves the card through stages (Script, Animation, Review) and attaches the relevant file at each stage.
3. When the episode reaches "Review", Lily watches the finished animation and either approves it (moves to "Scheduled") or sends it back to "Animation" with a note.
4. In the "Scheduled" stage, Lily sets the exact publish date and time; the system queues the upload via the YouTube API.
5. At the scheduled time, the cloud function uploads the episode; the card moves to "Published" and the YouTube URL is stored.
6. 48 hours after publish, the system fetches view and watch-time data and attaches it to the episode card.

## Edge Cases
- Animation file too large to upload in one request: Split the upload into resumable chunks using the YouTube resumable upload API.
- Review rejection with no note: Prompt Lily to add at least one sentence of feedback before moving the card back.

## Definition of Done
- [ ] An episode can progress through all six stages to "Published" without manual API calls.
- [ ] Review rejection requires a written note.
- [ ] Performance snapshot attaches to the episode card automatically 48 hours after publish.
- [ ] Large file uploads use resumable upload with progress feedback.

## Self-Anneal Log
