# Directive: Cape Bretoner's admin workflows — App Design Framework

## Goal
Define the screen structure and component system for the Cape Bretoner's admin dashboard so community and business workflows are manageable by one person.

## Inputs
- Core admin actions: manage member records, process incoming requests, publish announcements, generate reports
- Users are primarily desktop-based office workers; secondary mobile access for on-the-go approvals
- Design mood: professional, approachable, reflective of Cape Breton's community identity

## Outputs
- Screen map covering all admin workflow types
- Component list (MemberRow, RequestCard, AnnouncementComposer, ReportWidget)
- Token file with community-appropriate colour palette and accessible type scale

## Process
1. Inventory every recurring admin task and group into workflow categories (Members, Requests, Communications, Reports).
2. Assign a primary screen to each category; navigation is a left-side menu on desktop, a bottom tab on mobile.
3. The RequestCard is the central unit: shows requester name, request type, date received, and current status (New, In Progress, Resolved).
4. Design a status-change action directly on the RequestCard so Lily can update status without navigating to a detail page.
5. Use accessible colour tokens: minimum 4.5:1 contrast for all text; avoid relying on colour alone to convey status.
6. Write a one-paragraph description for each screen.

## Edge Cases
- Large member list (over 500 records): Add search and filter by status or region; the table must not paginate in a way that breaks screen-reader flow.
- Mobile approval flow: Ensure the RequestCard status-change action is reachable with one thumb on a 375 px wide screen.

## Definition of Done
- [ ] All four workflow categories have a mapped screen.
- [ ] RequestCard component is fully specified including status-change action.
- [ ] All colour tokens meet 4.5:1 contrast ratio.
- [ ] Desktop and mobile navigation patterns are defined.
- [ ] Lily has reviewed and approved the screen map.

## Self-Anneal Log
