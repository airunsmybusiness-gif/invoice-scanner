# Directive: yt-automation — Project Brief

## Goal
Automate the mechanical parts of running a YouTube channel — scheduling uploads, setting titles and thumbnails, and collecting performance data — so Lily spends her time on content, not on clicking through YouTube Studio.

## Inputs
- YouTube channel credentials (OAuth2 access to Lily's channel)
- Lily's preferred publishing cadence (days of week, times)
- Video files and metadata (title, description, thumbnail) produced outside this system

## Outputs
- Scheduled upload queue where Lily adds a video once and the system handles the rest
- Published videos live at the chosen time without Lily being at her computer
- Weekly performance snapshot (views, watch time, subscriber change) stored per video

## Process
1. Connect the YouTube Data API with Lily's channel; confirm upload, scheduling, and analytics read permissions before writing any queue logic.
2. Define the minimum metadata Lily must provide per video (title, description, tags, thumbnail, publish time) and make every other field optional.
3. Build the queue screen so Lily can add and reorder videos before the upload automation exists — let her see value immediately.
4. Wire up the cloud upload function; test with one real video on a private publish setting before enabling public scheduling.
5. Add performance snapshots only after uploads are reliable; do not block the queue on analytics.

## Edge Cases
- YouTube API quota exhausted: The daily upload quota is limited; never queue more uploads in one day than the quota allows, and surface a warning when Lily is close to the limit.
- Lily's OAuth token expires: Refresh tokens automatically; if refresh fails, alert Lily before an upload is due rather than failing silently.

## Definition of Done
- [ ] A video added to the queue publishes to YouTube at the scheduled time without manual intervention.
- [ ] Lily is alerted before any scheduled upload fails, not after.
- [ ] Performance snapshots for each video are collected and visible in the dashboard 24 hours post-publish.
- [ ] The system respects YouTube API quotas and never silently drops an upload.

## Self-Anneal Log
