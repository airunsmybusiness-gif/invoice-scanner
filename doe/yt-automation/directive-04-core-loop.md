# Directive: yt-automation — Core Loop

## Goal
Define the single repeating cycle that delivers value every week: draft → schedule → publish → report.

## Inputs
- Video title, description, thumbnail, and file path
- Publish date and time chosen by Lily
- YouTube channel credentials

## Outputs
- Scheduled upload queued in the system
- Published video live on the channel at the chosen time
- Basic performance snapshot (views, likes) available 24 hours post-publish

## Process
1. Lily adds a new video entry (title, description, thumbnail, file, publish time) via the Queue screen.
2. The system validates all required fields are present and the file is an accepted format.
3. Entry is written to the schedule store with status "pending".
4. At the scheduled time, the cloud function picks up pending entries and calls the YouTube upload API.
5. On successful upload, status updates to "live" and the video URL is stored.
6. 24 hours after publish, the system fetches view/like counts and stores a snapshot; status moves to "reported".

## Edge Cases
- Upload fails mid-transfer: Retry once immediately; if still failing, set status to "upload_error" and notify Lily via dashboard alert.
- Publish time passes while app is offline: Cloud function detects the missed window on next run and uploads immediately, logging the delay.

## Definition of Done
- [ ] A video can be added, scheduled, and published end-to-end without manual intervention.
- [ ] Status transitions (pending → live → reported) are visible on the Queue screen.
- [ ] 24-hour performance snapshot appears automatically.
- [ ] Upload errors surface as actionable dashboard alerts.

## Self-Anneal Log
