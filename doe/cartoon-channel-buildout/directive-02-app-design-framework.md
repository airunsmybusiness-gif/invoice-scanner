# Directive: cartoon-channel buildout — App Design Framework

## Goal
Define the content management and publishing interface for the cartoon channel so Lily can plan, track, and release episodes without a production team.

## Inputs
- Core user actions: add an episode to the pipeline, track production stage, schedule for upload, review performance
- Brand identity: playful, colourful, child-friendly palette
- Target platform: web admin dashboard (content creation happens on desktop)

## Outputs
- Screen map for the episode pipeline dashboard
- Component list (EpisodeCard, StageTracker, ThumbnailPreview, ScheduleSlot)
- Colour and type token file using channel brand colours

## Process
1. Map the episode lifecycle as stages: Concept → Script → Animation → Review → Scheduled → Published.
2. Design the dashboard as a Kanban-style board where each EpisodeCard moves across stage columns.
3. The EpisodeCard shows: episode title, thumbnail preview, target publish date, and current stage.
4. Design a StageTracker component (a horizontal step indicator) that appears on the episode detail view.
5. Use the channel's brand colours as stage-column headers; keep the rest of the UI neutral so thumbnails pop.
6. Write a one-paragraph description of each screen and what Lily does there.

## Edge Cases
- More than 20 episodes in the pipeline: Add a filter by stage so the board stays manageable.
- Thumbnail not yet created: Show a placeholder with the episode title on the EpisodeCard.

## Definition of Done
- [ ] Episode lifecycle stages are defined and documented.
- [ ] Kanban board layout is designed with column headers per stage.
- [ ] EpisodeCard and StageTracker components are fully specified.
- [ ] Token file uses the channel's brand colours.
- [ ] Lily has reviewed and approved the dashboard layout.

## Self-Anneal Log
