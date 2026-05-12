# Directive: TicketDrop — Core Loop

## Goal
Define the end-to-end cycle that turns a spare ticket into cash: list → discover → buy → attend.

## Inputs
- Seller: event details, section, row, seat, asking price, ticket file or barcode
- Buyer: search query or event browse action, payment method

## Outputs
- Active listing visible to buyers
- Completed purchase with confirmation to both parties
- Ticket delivered to buyer (PDF or barcode)

## Process
1. Seller taps "List a Ticket", enters event details and price, and uploads the ticket file or barcode image.
2. System validates the listing (required fields, file format) and publishes it as "available".
3. Buyer browses or searches; taps a TicketCard to see full details and taps "Buy Now".
4. Buyer completes payment through the payment provider; on success, the listing status changes to "sold".
5. System delivers the ticket file to the buyer and sends confirmation to both seller and buyer.
6. Seller's payout is queued for the next settlement cycle.

## Edge Cases
- Two buyers attempt to purchase the last ticket simultaneously: Use a reservation lock; the first payment to complete wins, the second receives an "already sold" message and is not charged.
- Seller uploads an unreadable barcode image: Reject at upload time with a clear error and instructions for an acceptable format.

## Definition of Done
- [ ] A listing can be created in under 60 seconds.
- [ ] Buyer completes a purchase and receives the ticket file.
- [ ] Seller receives confirmation and a payout record.
- [ ] Simultaneous-purchase race condition is handled without double-charging.

## Self-Anneal Log
