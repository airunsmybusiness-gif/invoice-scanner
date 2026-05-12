# Directive: RigBooks — App Design Framework

## Goal
Define the screen structure, navigation model, and component system for RigBooks so the bookkeeping UI is consistent and usable in the field on a phone.

## Inputs
- Core user jobs (log an expense, review a job summary, generate a monthly report)
- Field context: users are often on mobile with dirty hands; large tap targets required
- Brand preference (clean, industrial, high-contrast)

## Outputs
- Screen map covering every bookkeeping action
- Mobile-first component library (BigButton, ExpenseRow, JobCard, ReportSummary)
- Colour and type token file

## Process
1. List every bookkeeping action a rig operator needs (log fuel, log parts, log labour, view totals, export report).
2. Assign one screen per action cluster; keep navigation to at most two taps from Home.
3. Design for thumb reach: all primary actions sit in the bottom 40% of the screen.
4. Define component tokens: minimum tap target 48 px, high-contrast text (4.5:1 ratio), large numeric display for dollar amounts.
5. Write a one-paragraph description of each screen including what data it shows and what the user does.

## Edge Cases
- Offline in the field: Every data-entry screen must function fully offline; sync happens when connectivity returns.
- Small screen (older Android phones): Test all layouts at 360 × 640 dp minimum.

## Definition of Done
- [ ] Screen map covers all core bookkeeping actions.
- [ ] Component list exists with tap-target and contrast specifications.
- [ ] Token file is created with colour, font, and spacing values.
- [ ] All screens are described and reviewed by Lily.
- [ ] Layout tested at 360 × 640 dp.

## Self-Anneal Log
