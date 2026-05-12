# Directive: cartoon-channel buildout — Feedback Loop

## Goal
Turn episode performance data into a learning record that helps Lily make better creative decisions for future episodes.

## Inputs
- 48-hour and 7-day performance snapshots per episode (views, watch time, average view duration, subscribers gained)
- Episode metadata (title, topic tag, episode length, publish day and time)
- Lily's post-publish notes

## Outputs
- Episode performance dashboard ranking published episodes by watch-time retention
- Monthly insight summary highlighting what creative choices correlated with stronger performance
- A growing topic-tag library showing which themes resonate most with the audience

## Process
1. After each 7-day snapshot is collected, update the episode's performance rank on the dashboard.
2. Each month, identify the top three and bottom three episodes by average view duration percentage.
3. Compare metadata across top and bottom performers: look for patterns in episode length, publish day, and topic tag.
4. Surface one plain-English observation (e.g., "Episodes under 5 minutes had 22% higher retention this month").
5. Lily adds a creative note to any episode and tags it with what she would do differently.
6. Creative notes feed a running "What Works" log organised by topic tag.

## Edge Cases
- Fewer than six published episodes: Show available data without making trend claims; note that insights sharpen with more episodes.
- YouTube API data delayed (common for new channels): Mark the snapshot as "pending" and retry after 6 hours.

## Definition of Done
- [ ] 7-day performance snapshots trigger automatic rank updates.
- [ ] Monthly insight summary generates with at least one plain-English observation.
- [ ] Topic-tag "What Works" log exists after three months of publishing.
- [ ] Lily can add a creative note to any episode from the dashboard.

## Self-Anneal Log
