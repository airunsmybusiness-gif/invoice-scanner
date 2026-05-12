# Directive: Cape Bretoner's admin workflows — Feedback Loop

## Goal
Surface patterns in community requests and response times so Lily can improve workflows and plan for recurring needs.

## Inputs
- Resolved request records (type, time from New to Resolved, month)
- Member activity data (requests per member, membership tenure)
- Announcement engagement if measurable (open rate from email service)

## Outputs
- Monthly admin summary: total requests by type, average resolution time, unresolved backlog count
- Top three request types for the current quarter
- Slowest-to-resolve request types flagged for process improvement

## Process
1. On the first of each month, generate the admin summary for the prior month.
2. Calculate average resolution time per request type (time from "New" to "Resolved" in hours).
3. Rank request types by volume and flag the top three.
4. Flag any request type with an average resolution time over 72 hours as a process improvement candidate.
5. Lily reviews the summary, notes what caused delays, and decides whether to adjust a workflow or add a resource.
6. Summary and Lily's notes are stored in the admin log.

## Edge Cases
- No resolved requests in the prior month: Generate the summary with a zero-count note; do not suppress the report.
- Request type names vary (e.g., "info request" vs. "Information Request"): Normalise to title case on save; review for consolidation quarterly.

## Definition of Done
- [ ] Monthly admin summary generates automatically on the first of each month.
- [ ] Average resolution time per request type is calculated correctly.
- [ ] Request types over 72 hours average are flagged.
- [ ] Lily can add a note to the monthly summary and have it saved.

## Self-Anneal Log
