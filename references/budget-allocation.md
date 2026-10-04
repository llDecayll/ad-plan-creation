# Budget allocation and learning thresholds

One rulebook for how much each campaign needs, how to split money across platforms, and how to roll scores up. When rules elsewhere seem to conflict, this file wins.

## 1. Minimum daily budget per learning unit
A "learning unit" is a Meta ad set (or Advantage+ campaign) or a Google campaign using smart bidding. CPR = expected cost per optimisation result (the event the platform bids on).

| Platform / bidding | Minimum daily budget | Comfortable | Why |
|---|---|---|---|
| Meta, any conversion goal | **≥ 7 × CPR** (50 events ÷ 7 days ≈ 7.1 per day) | 10 × CPR | ~50 events in 7 days exits learning |
| Meta, "learning-limited test" | ≥ 3 × CPR | — | Allowed only as an explicitly labelled test with a 14-day read, never for the core campaign when budget allows more |
| Google Search, Max conversions / tCPA | ≥ 1 × CPA (≈30 conv/month) AND ≥ 15 clicks/day at expected CPC | 2 × CPA | Smart bidding needs ~30 conv/30 days; Search needs click volume |
| Google PMax / Demand Gen | ≥ 1.5 × CPA and ≥ 30 conv/month in account | 3 × CPA | Multi-channel exploration needs more data |
| Google Max clicks (no tracking, temporary) | ≥ 15 clicks/day × CPC | — | Only until tracking is fixed |
| Awareness / reach (Meta, YouTube) | Enough for target reach × frequency: daily = (reach ÷ days) × frequency × CPM ÷ 1,000 | — | Optimises impressions, not events |

The old "3-5 × CPR" shorthand is retired; use this table. Show the arithmetic for every campaign.

## 2. Platform and campaign split (in this order)
1. **Fund the must-haves first.** Brand-defence search if competitors bid on the brand (usually small), and any campaign the business literally depends on (e.g. the only trackable channel).
2. **Allocate by cost per real outcome** (qualified lead, site visit, show-up, sale net of returns, deposit, install-to-paying), not cost per platform result.
   - With history: rank channels by cost per real outcome; give the best channel as much as it can absorb (until its marginal cost rises — impression share lost to budget near 0 on Search, frequency > 3/week or CPM climbing on Meta), then move to the next.
   - Without history, use intent order: (a) Search where there is real search demand for the service, (b) Meta/WhatsApp/forms for demand creation, (c) upper funnel only when the lower funnel is funded. Typical starting points: local high-intent services with search demand 55-70% Search; impulse/visual D2C 60-75% Meta; B2B with job-title targeting needs → LinkedIn first (flag), then Search.
3. **Never contradict your own reasoning.** If the plan says channel X is more efficient, X gets the larger share unless a stated constraint (absorption limit, minimum for the other channel's learning unit, test budget) explains otherwise — state it.
4. **Cap tests** at 10-20% of total budget.
5. **Retargeting** only when the pool can support it (Meta: ~1,000+ people in the window reachable per day of budget; practical floor a few thousand in 30 days) and it isn't already covered by Advantage+ sales (existing-customer budget cap is the modern alternative).
6. **If the budget cannot fund everything the brief asks for,** fund in the order above and list the rest under "Deferred / needs budget" with the ₹ needed and what the client must decide (see scope-and-channels.md).

## 3. Overall confidence roll-up
- Overall = spend-weighted average of funded campaigns' scores, then apply plan-level caps from confidence-rubric.md.
- Deferred campaigns are scored but excluded from the average.

## 4. v0.5 additions
- **Express every gate as a multiple of CPA/CPR, then convert to local currency.** Never reuse ₹ values for other markets. Client history overrides benchmark multipliers.
- **Joint vs per-platform budget:** if the client gave one pool, split it by §2; if they gave per-platform budgets, do not move money between platforms without saying so.
- **Cost point for the check:** use the midpoint cost for the plan, and show the high-end cost as the downside case. A campaign that passes only at the low end is a labelled test.
- **Test cap vs minimum spend:** if the 3x CPR learning-limited minimum exceeds the test cap (10-20% of budget), the minimum wins, or the test is deferred with the ₹/$ needed. Say which.
- **Google App campaigns:** about 10x target CPA per day and ≥10 conversions per day to exit learning; otherwise defer or run a web/WhatsApp path first.
- **Seasonality above 40% of annual revenue:** front-load a fixed monthly budget toward the peak months and say what is taken from off-peak.
- **Multi-month cycles (admissions, B2B, property):** use phases (nurture, peak, result-day or deadline bursts). Day-30 checks use leading proxies (qualified enquiries, visit bookings), not the final outcome.
- **Unspent budget** when a platform is blocked (policy, tracking, account suspension): park it, do not re-route silently; list it under Deferred.
- **Brand and impression-share campaigns:** a small brand-Search campaign is allowed when competitors bid on the brand name; budget ≈ 5-10% of Search and it is reported separately.

## 5. v0.5.2 additions
- **Tiny budgets (< ~₹500/day or equivalent):** run ONE campaign only. No vanity or engagement spend (organic only). Say it is a learning-limited test with a 14-day read. For hyperlocal radii, state the audience size (Meta estimate) and watch frequency; if reach < ~20,000 or frequency > 3/week, widen the radius.
- **Joint pool by default:** if the client gives one budget, treat it as joint across Meta + Google; ask only if the brief is genuinely ambiguous.
- **Split shift:** the 55-70% Search starting default may move up to 15 points toward Meta (or the reverse) when derived cost per outcome clearly favours the other platform; state the reason and the numbers.
- **Learning-limited tier** (3× CPR) also applies to B2B and test budgets on Google (≥1× CPA minimum, flagged as a test).
- **Low-volume offline outcomes (< 50/month):** still send the offline event (site visit, qualified lead) as a secondary conversion or via CAPI; optimise on the qualified-lead proxy and say so.
- **Fixed monthly budget with a peak season:** shift 20-30% of the Jan-Sep budget into the peak months instead of only deferring the uplift; show the cost to off-peak.
- **Test bounded in a secondary market:** a 15-25% test is allowed when the secondary market has better unit economics; otherwise defer.
