# Directive: TicketDrop — App Design Framework

## Goal
Define the screen structure and design system for TicketDrop so buyers and sellers share a fast, trust-building ticket marketplace UI.

## Inputs
- Core user journeys: seller lists a ticket, buyer discovers and purchases a ticket
- Mobile-first requirement (most ticket activity happens on phones at events)
- Design mood: urgent, bold, high-energy to match live-event context

## Outputs
- Dual-role screen map (seller views vs. buyer views)
- Component list (TicketCard, CountdownBadge, PriceTag, ConfirmationBanner)
- Colour and type token file

## Process
1. Separate the app into two role paths: Seller (list, manage, cash out) and Buyer (browse, buy, present).
2. Map screens for each role; identify which screens are shared (event detail, profile).
3. Design the TicketCard as the central reusable unit: event name, date/time, section/row, price, and a countdown if the event is within 24 hours.
4. Choose an accent colour that signals urgency (e.g., amber or red) for countdown states; use it sparingly.
5. Document each screen with a one-paragraph note: who sees it, what they do, and what they see next.

## Edge Cases
- Sold-out event: Replace the buy button with a "Notify Me" option; never show a disabled button with no explanation.
- Last ticket remaining: Surface a "1 left" badge on the TicketCard to create honest urgency.

## Definition of Done
- [ ] Seller and buyer screen maps are complete with no dead ends.
- [ ] TicketCard component is fully specified.
- [ ] Countdown and sold-out states are designed.
- [ ] Token file covers colour, type, and spacing.
- [ ] Lily has reviewed and approved both role paths.

## Self-Anneal Log
