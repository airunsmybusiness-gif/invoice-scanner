# Directive: FieldCostPro — App Design Framework

## Goal
Define the screen structure and component system for FieldCostPro so project managers can capture and review field costs clearly on any device.

## Inputs
- Core user actions (log a cost item, attach a photo of a receipt, view project budget status, export a cost report)
- Mixed audience: field workers log on mobile, project managers review on desktop
- Design requirement: legible outdoors in bright sunlight (high contrast)

## Outputs
- Screen map for both mobile (logger) and web (reviewer) views
- Component list (CostRow, BudgetGauge, ReceiptThumb, ProjectHeader)
- Token file with high-contrast colour values and minimum font sizes

## Process
1. Define the two usage contexts: field logging (mobile, one-handed, quick entry) and desktop review (wider layout, sortable tables, export).
2. Map screens for each context; share the project detail and cost list screens between both.
3. Design the BudgetGauge as the central status indicator: shows budget used vs. total as a bar with colour state (green below 80%, amber 80–99%, red at or over 100%).
4. Set minimum font size at 16 sp for all field-entry labels; ensure all touch targets are at least 48 px.
5. Document each screen with its context (mobile or desktop), the data it displays, and the action the user takes.

## Edge Cases
- Field worker has no connectivity: All logging screens must work fully offline; gauge updates when sync completes.
- Desktop reviewer on a small laptop: Ensure the desktop layout is usable at 1280 × 720 px minimum.

## Definition of Done
- [ ] Mobile logging and desktop review screen maps are complete.
- [ ] BudgetGauge colour states are specified.
- [ ] All mobile touch targets meet 48 px minimum.
- [ ] Token file covers colour, font, and spacing for both contexts.
- [ ] Lily has reviewed both screen maps.

## Self-Anneal Log
