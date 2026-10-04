# Grade r1 Set A
Total: 50.0 / 54 = 92.6% (v0.4: 48.5 = 89.8%; delta +1.5 pts, +2.8 pp). Traps: all passed except A1 #4 partial (unchanged from v0.4).

| Scenario | r1 | v0.4 |
|---|---|---|
| A1 | 8.0 | 8.0 |
| A2 | 8.5 | 8.0 |
| A3 | 8.5 | 8.0 |
| A4 | 8.5 | 7.5 |
| A5 | 8.0 | 8.0 |
| A6 | 8.5 | 9.0 |

## A1 8.0/9
Hits: 1, 2, 3, 5, 7, 8, 9.
Misses: #4 0.5 (no condition targeting and proxies stated, but the health-data limit on lower-funnel events is not a confidence reducer; only "mental-health policy rejections" is a risk). #6 0.5 (UK deferred because derived CPI makes it lose money, not run as a 15-25% bounded test).

## A2 8.5/9
Hits: 1 (CMP + Consent Mode v2 blocker), 2 (brand harvesting, MER, PMax paused), 3, 4 (Standard Shopping, margin labels, brand search; fixed from v0.4), 5, 7, 8, 9.
Misses: #6 0.5 (break-even ROAS 1.72 and a lower target are right, but the Q4 uplift is deferred and funded from Jan-Mar instead of front-loading Oct-Dec).

## A3 8.5/9
Hits: 1, 2, 3, 5, 6 (UTM/fbclid carry-over, CAPI, Google offline import gated), 7, 8, 9.
Misses: #4 0.5 (Meta 100%, Google deferred; the key wants Search weighted. No keyword list or CNA/LPN/student negatives).

## A4 8.5/9
Hits: 1, 2, 3, 4 (15%, Chairman signs off; fixed), 5, 6, 7, 9.
Misses: #8 0.5 (CPC rise Mar-Jul noted; no keyword themes or negatives in the output).

## A5 8.0/9
Hits: 1, 2, 3, 4, 6 (KYC primary, disbursal as value; fixed), 8, 9.
Misses: #5 0.5 (Meta credit category "not required, do not opt in", the same wrong direction as v0.4). #7 0.5 (lag handled, but web CAPI is not mentioned).

## A6 8.5/9
Hits: 1, 2, 3, 4, 6, 7, 8, 9.
Misses: #5 0.5 (negatives for jobs, DIY and rebate application are listed only under Risks; no phrase/exact intent set). Regression from 9.0.

## Plugin-rule gaps (priority order), including runs' own sections
1. **Policy-watch "SAC not required" outside US/CA (A5 #5; A4, A6, A2 repeat it as "do not opt in").** Run notes: "no-opt-in vs always-state (Lending)". Rule change: for credit, lending, employment and housing advertisers, always state the Meta declaration and its targeting limits, then "verify live". "Not required, do not opt in" is allowed only for other verticals.
2. **Health vertical (A1 #4).** Add a rule that condition-based detailed targeting is removed on Meta and banned on Google. Use broad/Advantage+ with sleep/yoga/wellness proxies, and apply a -5 confidence for restricted lower-funnel events.
3. **Search keyword and negatives mandate (A3, A4, A6).** Every funded or deferred Search campaign lists 5-10 themes plus a vertical negatives list (recruitment: CNA, LPN, student, salary; education: cutoff, government college; solar: jobs, DIY, rebate). Add a rule on when Search outranks Meta for employment when CPCs are given (A3 gap: "no rule for Google minimum vs test cap").
4. **Test cap vs 3x CPR minimum (A1 UK, A2, A3, A6, A5).** Every run flagged this. Rule: if the minimum exceeds the 10-20% cap, the minimum wins or the test is deferred, and the plan must say which. Allow a 15-25% bounded test when the secondary market has better unit economics (A1 UK).
5. **Seasonality vs fixed monthly budget (A2).** Add: when peak months exceed 40% of revenue, front-load the fixed budget by shifting 20-30% from Jan-Sep into Oct-Dec. Do not just defer the uplift.
6. **Benchmarks (A1, A2, A3, A4, A5, A6 all).** Add UK, US, AU and Gulf rows, a US healthcare-recruitment row, a lending row, an app-trial row and a management-quota row. State that client history overrides the multiplier. Anchor lead-to-qualified rates (A3, A4).
7. **Tracking vocabulary (A1, A2, A3, A6).** Add statuses: "events exist, not linked" (A1), "consent-gated" (A2), "thank-you-only pixel on external ATS" (A3), and "wrong trigger/duplicate primary" (A6). Score tracking both pre-fix and post-fix. Add an app section (SKAN/AAK, AEM, per-OS campaigns, Meta app minimum).
8. **Blocked platform vs "give best channel all it absorbs" (A5, A6).** Rule: parked money is held, not rerouted, and a scale decision needs a client sign-off. Add a suspended-account process (appeal, evidence, no new account).
9. **Declined client ask and the policy-blocker cap (A3, A4).** State that a declined ask is not an open blocker; the cap applies only when an unresolved item is in the plan.
10. **Minors and stakeholders (A4).** Add a minor-audience rule (parents-first, 18+ minimum, YouTube 25+) and a stakeholder cap of 15-25% with a named sign-off.
11. **Word cap vs five creatives per funded campaign (A1, A2, A5).** Require five angles for the lead funded campaign only; others get a launch-time brief.
12. **Smaller items.** Rule on how a capped score affects forecast band width; exchange-rate default; whether LTV is net or gross of store fee (A1); how to treat a CAPI requirement in web flows for lending (A5); an ATS/CRM capacity-sizing line (A3); unknown depot or radius handling (A6); retargeting pools when the pixel is consent-gated (A2).
