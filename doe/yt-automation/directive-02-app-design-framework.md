# Directive: yt-automation — App Design Framework

## Goal
Define the screen layout, navigation structure, and visual design system for the yt-automation dashboard so every future screen follows the same pattern.

## Inputs
- List of core user actions (schedule video, review analytics, approve thumbnail)
- Brand colours and preferred font
- Target device (web-first, then mobile via Expo)

## Outputs
- Screen map document listing every view and its purpose
- Reusable component list (Button, Card, StatusBadge, VideoRow)
- Colour/typography token file

## Process
1. List every job the tool performs for Lily and assign one screen to each job.
2. Draw a simple box-and-arrow flow showing how screens connect (Home → Queue → Upload → Analytics).
3. Pick three colours (primary, surface, accent) and one font; record them as named tokens.
4. Define five reusable UI components needed on at least two screens; name and describe each.
5. Write one-paragraph usage notes per screen explaining what the user sees and what action they take.

## Edge Cases
- Channel not yet authorised: Show an empty-state screen with a single "Connect YouTube" call-to-action before any other screen is accessible.
- No scheduled videos: Queue screen shows an illustrated empty state with a prompt to schedule the first video.

## Definition of Done
- [ ] Screen map covers every identified user action with no orphan screens.
- [ ] Component list has at least five entries with names and descriptions.
- [ ] Token file exists with colour and font values.
- [ ] Every screen has a one-paragraph usage note.
- [ ] Lily has reviewed and signed off on the design direction.

## Self-Anneal Log
