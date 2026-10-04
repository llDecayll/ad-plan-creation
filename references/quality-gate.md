# Quality gate (run before delivering any plan)

Go through every line. Fix what fails; if something cannot be fixed, say so in the plan's Summary. A plan that fails a line marked ★ is not finished.

## A. Business truth
- ★ The plan names the client's **real outcome** (vertical-playbooks.md) and every funded campaign has a forecast for it (e.g. cost per qualified lead, per site visit, per show-up, per paying user, per sale net of RTO), not only platform results.
- ★ Where the transaction happens was checked (scope-and-channels.md §1); untrackable steps have a reconciliation method.
- Platform data vs CRM/backend reconciled when history exists; broken tracking blocks scaling.

## B. Scope
- ★ Every market, audience, product line and stakeholder goal in the brief appears as a campaign or under "Deferred" with ₹ needed and a client decision.
- ★ "Other channels to consider" block present (LinkedIn, aggregators, portals, marketplaces, GBP, Ad Grants, Apple Search Ads… as relevant), even if empty with reason.

## C. Money
- ★ Every funded learning unit passes budget-allocation.md §1 (arithmetic shown) or is explicitly labelled a learning-limited test.
- ★ The split follows the stated reasoning (budget-allocation.md §2.3). No "X is better" followed by an equal or opposite split without a stated constraint.
- Forecasts are ranges, centred on the stated benchmark/history, with source.

## D. Compliance and ethics
- ★ Special ad categories decided per audience country (Meta and Google personalised-ads restrictions).
- ★ Client requests that break policy, law or basic ethics are declined in the plan with a compliant alternative (see policy-watch.md "Client asks to rework"). Never silently comply, never silently drop.
- Claims in ads are substantiated (numbers, rankings, "free", "guaranteed", "#1", health/financial outcomes).
- Creatives contain no personal-attribute phrasing ("your acne", "your debt", "are you depressed").
- Age-restricted products/audiences handled (minors).

## E. Operations
- ★ Operating constraints applied: who answers and when → ad schedule / away messages / callback scheduling; capacity (empty days/slots) → day-parting and offers; time zones for overseas audiences.
- Lead handling: first-reply script, response-time target, qualification questions.

## F. Completeness of deliverables
- ★ Every funded campaign has ≥5 creative concepts (Search: 5 RSA angle sets + image assets), budget check, forecast, settings, and confidence score.
- Planned/deferred campaigns have a trigger.
- URL parameters / campaign codes for attribution.

## G. Test and scale plan (always include)
Per funded campaign:
| Checkpoint | Look at | Kill / fix if | Scale if |
|---|---|---|---|
| Day 3 | Delivery, approvals, tracking firing, reply times | Rejected ads, events not firing, replies > 30 min | — |
| Day 7 | Cost per platform result vs forecast; CTR; frequency | > 1.5× forecast high end with CTR below benchmark → creative/offer fix | within range → hold |
| Day 14 | Cost per real outcome (qualified / visit / sale) | > 1.3× target → change goal/audience/creative in a duplicate | < target and stable → +20% budget every 3-4 days |
| Day 30 | Real outcomes vs plan, MER/blended | Below break-even → cut or restructure | At target → scale, add next deferred campaign |
Adapt thresholds to the client's economics and state them in ₹.

## H. Confidence
- Scores follow confidence-rubric.md including caps; overall is spend-weighted.

## I. v0.5 additions
- **Sanity-check client numbers** (CPL, close rate, AOV, margin) against `benchmarks.md`; if they differ by more than 2x, say so and plan with the benchmark as the downside case.
- **Creative sets:** five prompts for every funded campaign; planned/deferred campaigns get two. Under a word cap, give one line each for the main campaign and list the rest as "to be written at launch".
- **Stakeholder conflict:** cap the secondary goal at 15-25% of budget and name who signs off.
- **Day-14 for long cycles:** use the leading proxy, and state the real-outcome check date.

## J. v0.5.2 additions
- Five creative angles are required for the lead funded campaign in a written answer; other funded campaigns get a launch-time brief. In the HTML board, every funded campaign still carries ≥5 creatives.
- Ask for gross margin (or contribution) at intake; if missing, show a labelled 50% assumption and cap cost evidence at 50.
- Long cycles (45-90 days): day-14 uses the qualified proxy (qualified demo, visit booked); put a day 60-90 won-deal check in the table.

## K. v0.5.3 additions
- ★ In a written (word-capped) answer, F and J are satisfied by five creative angles for the lead campaign and a launch-time brief for others. Do not flag F as failed for this.
- ★ Margin unknown: gate J applies (labelled 50%, cost evidence ≤50); also ask for margin at intake and say what real margin would change.
- ★ Each declined client ask names the person who signs off (e.g. CEO, marketing manager) and the compliant alternative.
- Units checked: "trial-to-member", "deposit", "lead", "booking" are defined (per person or per group; attended vs signed up; margin before or after ad spend).
- Currency: no ₹ in non-INR plans.
- Launch/hard-date plans show phasing (burst/sustain or ramp) and any reserve.

## L. v0.5.5 clarification
- Money amounts in plans use the client's currency; the "₹ needed" phrases in rulebooks mean "amount needed in the client's currency".
