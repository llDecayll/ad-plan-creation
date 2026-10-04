# Grade v04 Set A

Total: 48.5 / 54 = 89.8%

| Scenario | Score |
|---|---|
| A1 | 8.0/9 |
| A2 | 8.0/9 |
| A3 | 8.0/9 |
| A4 | 7.5/9 |
| A5 | 8.0/9 |
| A6 | 9.0/9 |

## A1 (8.0/9)
Hits: 1 (trial_start on both platforms), 2 (₹3,500 per trial, ₹19,400 per payer vs ₹1,150), 3 (headline declined, alternative offered), 5 (links, SKAN, store-revenue reconcile), 7 (budget and event-volume checks), 8, 9.
Misses:
- #4 partial: no explicit statement that Meta removed health detailed-targeting. The health-data limit on lower-funnel events is not used as a confidence reducer. No interest proxies.
- #6 partial: UK deferred as unaffordable, not run as a bounded 15-25% test. The better UK economics are not exploited.

## A2 (8.0/9)
Hits: 1 (Consent Mode v2 plus CMP as a launch blocker), 2 (brand harvesting, exclusions, new-customer goal, MER), 3, 5, 7, 8, 9.
Misses:
- #4 partial: no custom-label feed segmentation by margin or bestseller, no Standard Shopping.
- #6 partial: the Q4 ramp is a "client decision" with a fixed budget, not front-loaded to Oct-Dec. Break-even ROAS (about 2x) and the lower new-customer target are correct.

## A3 (8.0/9)
Hits: 1, 2, 3, 5, 7, 8, 9.
Misses:
- #4 partial: Google gets only 33%. No keyword list and no negatives (CNA, LPN, student). The key wants Search weighted heavily.
- #6 partial: no offline conversion upload to Google and no GTM or cross-domain fix on the ATS. Only a lead-form asset fallback and CAPI.

## A4 (7.5/9)
Hits: 1, 2, 3, 5, 7, 9.
Misses:
- #4 partial: awareness is capped at about 12% and measured on branded-search lift, but no one is named to sign off the split.
- #6 partial: no qualifying questions (stream, exam, score) on the instant form. Call-centre hours are handled.
- #8 partial: no keyword themes or negatives. CPC seasonality is only implied by the phasing.

## A5 (8.0/9)
Hits: 1, 2, 3, 4 (no new Google account, appeal first), 6, 8, 9.
Misses:
- #5 partial: says the Meta financial-services SAC is "not required, don't opt in" and defers to a live check. The key expects the credit declaration to be stated.
- #7 partial: the core campaign optimises on `loan_disbursed` despite the 1-3 day lag. KYC is only a 15% test. Web CAPI is deferred.

## A6 (9.0/9)
All checkpoints passed. A$65 real CPL, scaling refused, fix list, re-learning, negatives, "free solar" refused, renter filter, 80 km presence, staged budget with break-even.

Traps: all passed except A1 #4 (partial). That one is a mild red flag.

## Plugin-rule gaps (prioritised) and fixes

1. **Meta credit/financial SAC in India (A5 #5, A6 policy).** Policy-watch says the SAC "isn't required" outside the US and Canada. Fix: add a rule that loans, credit and lending advertisers always state the financial-products declaration and its targeting limits, and verify live. Treat "SAC not required" as true only for non-credit, non-employment, non-housing categories.
2. **Health targeting restrictions (A1 #4).** There is no rule that detailed targeting on health conditions is removed on Meta and banned on Google. Fix: add a health-vertical rule requiring the plan to say so, use broad or Advantage+ audiences with sleep, yoga and wellness proxies, and cap confidence for restricted lower-funnel events.
3. **Delayed or deep events (A5, A1, A4 #5).** No guidance for lagged events. Fix: "primary optimisation event = the deepest event that occurs within about 3 days and gives at least 50/week. Deeper events go in as a secondary or value signal, and the deeper-event campaign is capped at a test."
4. **Search-led employment and education plans (A3, A4).** Fix: a vertical rule that every funded Search campaign lists 5-10 keyword themes plus a mandatory negatives list. For recruitment, weight Search toward high-intent terms when the client supplies CPCs.
5. **Currency and region (A2, A3, A6, all).** Benchmarks and gates are INR and India D2C only; the 6-15x multiplier gives a range too wide to use. Fix: add per-region benchmark rows (UK, US, AU, Gulf) or rule that client history overrides the multiplier. Express the gates as multiples of CPA, not ₹ values.
6. **E-commerce feed and Q4 (A2).** Fix: add a Shopping playbook covering custom labels by margin, GTIN and identifier_exists, and a Standard Shopping option. Add a rule to front-load the fixed monthly budget toward the peak months when seasonality is above 40% of revenue.
7. **Multi-month cycles (A4).** Fix: a phased-budget template with a seasonal phase split (nurture, then peak with result-day bursts). Day-30 checks should use leading proxies when the outcome lags.
8. **Stakeholder conflicts (A4).** Fix: when two goals conflict, cap the secondary goal at 15-25% and name who signs off.
9. **Tracking vocabulary (A1, A2).** Add "events exist but are not linked" and "consent-gated". Add an app-tracking section (SKAN or AdAttributionKit, AEM, per-OS campaigns). Let tracking be scored both before and after a fix, which A6 had to invent.
10. **Test cap vs minimum spend (A1 UK, A6).** Fix: when the 3x CPR minimum exceeds the 10-20% test cap, the minimum wins, or the test is deferred. Say which.
11. **Google App campaign budget rule (A1, A5).** Add "about 10x tCPA, and at least 10 conversions per day for tCPA".
12. **Smaller items:**
    - Say whether a capped confidence score widens the forecast band.
    - Say whether planned or deferred spend counts in the overall score.
    - Creative sets are required for funded campaigns only.
    - Add a step that sanity-checks client numbers (A6's $22 CPL).
    - Add a capacity-sizing rule (sales headcount, recruiters).
    - Add a policy-watch entry for solar under Housing and for capitation and admission law.
    - Add a rule that the SAC location minimum applies to the hard boundary.
