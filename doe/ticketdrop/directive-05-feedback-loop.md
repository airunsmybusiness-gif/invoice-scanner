# Directive: TicketDrop — Feedback Loop

## Goal
Track listing and purchase patterns so Lily can improve the marketplace experience and identify the event categories that drive the most sales.

## Inputs
- Completed transaction records (event type, price, time-to-sale, seller region)
- Listings that expired unsold
- Buyer search terms with no results

## Outputs
- Weekly marketplace health summary (listings created, sold, expired, average time-to-sale)
- Top-selling event categories for the current month
- "No results" search terms that reveal unmet demand

## Process
1. Every Sunday, generate a marketplace health summary covering the past 7 days.
2. Calculate average time-to-sale for sold tickets; flag categories with time-to-sale over 48 hours as "slow movers".
3. List the top five event categories by completed sales volume.
4. Collect the 10 most common search terms that returned zero listings; surface them in the admin dashboard as demand signals.
5. Lily reviews the summary, tags any insight worth acting on, and notes what to try next week.

## Edge Cases
- Fewer than 10 transactions in a week: Show data as-is with a note that insights improve with more volume; do not suppress the summary.
- Search term logging fails: Fail silently and resume logging on the next request; never block a buyer's search due to a logging error.

## Definition of Done
- [ ] Weekly summary generates automatically every Sunday.
- [ ] Slow-mover categories are flagged.
- [ ] Zero-result search terms are captured and displayed in the admin dashboard.
- [ ] Lily can tag insights from the summary view.

## Self-Anneal Log
