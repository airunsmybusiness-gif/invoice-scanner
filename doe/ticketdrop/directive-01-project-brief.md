# Directive: TicketDrop — Project Brief

## Goal
Build a peer-to-peer ticket marketplace where people with extra tickets can sell them fast and people arriving at an event can buy them on the spot — cutting out scalpers and reducing wasted seats.

## Inputs
- Target event types (concerts, sports, local shows) and the cities to launch in first
- Payment processing approach (Stripe or equivalent) agreed before building the listing flow
- Trust and safety rules: what listings are allowed, how disputes are handled

## Outputs
- Mobile app with two clear role paths: seller lists a ticket, buyer finds and buys it
- Secure payment flow that holds funds until the ticket is confirmed received
- Simple seller payout process (bank transfer or digital wallet)

## Process
1. Confirm the launch scope: one city, one event type, or open from day one — scope determines how complex the listing form needs to be.
2. Agree on the payment hold and release rule before writing any payment code; this is the hardest thing to change later.
3. Build the seller listing flow first (the supply side must exist before buyers can browse).
4. Build the buyer browse and purchase flow; test end-to-end with a real payment in the sandbox before launch.
5. Define the minimum trust features needed for launch (seller rating, ID verification, or neither) and implement only those.

## Edge Cases
- Seller lists a fraudulent ticket: Define the dispute resolution path before launch; at minimum, hold payment until the buyer confirms entry.
- Event is cancelled: Decide the refund policy in advance and automate it; a manual refund process at scale is unworkable.

## Definition of Done
- [ ] A seller can list a ticket and a buyer can purchase it end-to-end with a real (sandbox) payment in under five minutes total.
- [ ] Funds are held securely and released to the seller only after the buyer confirms receipt.
- [ ] The cancellation and refund policy is implemented, not just documented.
- [ ] Both role paths work on iOS and Android without platform-specific bugs.

## Self-Anneal Log
