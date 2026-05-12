# Directive: yt-automation — Feedback Loop

## Goal
Collect signals from published videos and surface insights that help Lily improve the next video's performance.

## Inputs
- YouTube Analytics API data (views, watch time, click-through rate, subscribers gained)
- Video metadata (title, thumbnail, publish time, topic tag)
- Lily's manual notes added after reviewing a video's performance

## Outputs
- Weekly digest showing top and bottom performers
- Per-video insight card with one actionable recommendation
- A running log of what worked and what did not, keyed by topic tag

## Process
1. Every Monday, pull the prior week's analytics for all published videos.
2. Rank videos by watch-time retention rate and flag the top and bottom performer.
3. For each video, generate an insight card showing: retention, CTR, title length, and publish day/time.
4. Surface one plain-English recommendation per card (e.g., "Thumbnails posted on Tuesday had 18% higher CTR this month").
5. Lily reviews the digest, adds a note to any video, and marks the digest as "reviewed".
6. Notes feed into the topic log so patterns are visible across weeks.

## Edge Cases
- YouTube API quota exceeded: Cache the last known analytics values and surface a "data may be stale" banner instead of failing silently.
- No videos published in the prior week: Show a prompt reminding Lily to schedule her next video.

## Definition of Done
- [ ] Weekly digest auto-generates every Monday.
- [ ] Every published video has an insight card with one recommendation.
- [ ] Lily can add a manual note to any video from the insight card.
- [ ] Topic log shows at least 30 days of pattern data after 30 days of use.

## Self-Anneal Log
