# B4 IronCore Fitness plan (benchmarks only; no live checks run)

Assumptions: no live Ad Library, SERP, tracking or policy check (the plugin would do all four). Margin unknown: labelled 50%. Fee midpoint ₹27k. "24% trial-to-member" read as attended trial to paid member (to confirm).

## Real outcome, economics, transaction
- Consumer: paid annual member. Break-even ≈ ₹27k x 50% = ₹13.5k per member.
- Franchise: qualified investor meeting, then signed franchise (₹25L fee).
- Sale happens at gym POS or BD desk, invisible to platforms. Reconcile with gym_id plus campaign code and a weekly manual POS tally.

## Goal translation, declined asks
- "Trial sign-ups for every gym" becomes cost per paid member by gym; all 38 run in city clusters.
- "20 franchise leads" kept, judged on qualified leads; capped at 15% (₹7,500/day). Sign-off: CEO.
- Declined: "₹8L profit/month assured" (banned earnings claim). Alternative: "Investment ₹1.5-2 Cr; returns not guaranteed" plus disclosure. Sign-off: CEO and legal.
- Franchisee brand bidding: stop via franchise agreement; franchisees run non-brand only.

## Platform split
₹50,000/day (₹15L/month): consumer ₹42,500 (Meta ₹23,000, Search ₹19,500; derived CPL ₹275 vs ₹425, so shifted toward Meta); franchise ₹7,500 Search only (Meta minimum exceeds the cap). Total Meta 46%, Google 54%.

## Campaigns (all lower funnel)
1. **M1 Meta Trial Pass:** Leads, instant form (higher intent, gym picker, WhatsApp confirm), Highest volume then CAPI conversion leads. 5 km pins, living in or recently in, expansion off, 18+. ₹21,000 = 7 cluster ad sets x ₹3,000. Check: 3,000 ÷ 275 = 10.9/day ≥ 7 x 275 = ₹1,925 ✓ (₹400: 7.5/day ✓). Forecast ₹6.3L ÷ ₹150-400 = 1,575-4,200 leads; 6% to member (25% attend x 24%) ≈ 137 members, ≈ ₹4,600 each (₹1,800-11,000).
2. **M2 Retargeting:** IG engagers and site visitors, exclude members; Advantage+ off; instant form; ₹2,000. Check: 7 x ₹200 = ₹1,400 ✓ (pool to verify). ≈ 240-400 leads, 26 members.
3. **G1 Search non-brand:** 14 city campaigns, Presence only, per-gym 5 km. Max conversions (Max clicks with CPC cap until gym_id verified). ₹18,000 (₹1,286 each). Check: ≥ 1 x ₹425 ✓; 37 clicks/day ≥ 15 ✓. 900-2,160 leads, ≈ 76 members (≈ ₹7,100).
4. **G2 Brand Search:** head office owns brand+city terms. ₹1,500 (5.6% of Search). Check: 15 x ₹10 ✓. 225-560 leads, ≈ 33 members.
5. **F1 Franchise Search:** India-wide, Presence or interest, own landing page. Max clicks capped, then Max conversions. ₹7,500. Check: ≥ 1 x ₹4,000 ✓ (1.9x). ₹2.25L ÷ ₹2-6k = 37-112 leads; 20-30% qualified = 7-34 (mid 14, ≈ ₹16k each). 20 leads reachable; signed franchises 1-2 in 6-9 months (rough).

Consumer: ≈ 270 members/month (135-400) on ₹12.75L, vs ≈ ₹36L first-year contribution (rough).

## Deferred, Other channels
- Meta India franchise: ₹12,000/day (pushes franchise to ~39%). NRI UAE: ₹36-72k/day after legal clearance. PMax store-visit: ₹5,000/day after GBP fix. Local awareness: ₹4-6k/day, 10-15% cap.
- Other: fix 6 GBPs (free), LinkedIn and franchise portals, member WhatsApp referrals, Justdial-type directories.

## Policy
Meta special category: none, not required in India, do not opt in (verify live). Franchise: no earnings claims; India securities declaration only if Meta franchise is added; verify Google financial-services policy. Fitness: 18+, no body-ideal before/after, no personal-attribute copy.

## Operating constraints
First reply ≤30 min, away message, next-morning follow-up; call assets on gym hours; off-peak trial offers if slots empty. One BD manager: ~2 leads/day, call within 1 hour, cap spend if backlog >10. GBP before location assets/PMax; gym_id into GA4 and router; franchisee creative kit.

## Risks
No gym_id (week-1 fix; gym URL parameter stopgap); Pixel, CAPI and Ads tag unknown; POS not integrated; franchisee brand bidding; margin unknown; 6 GBPs; clusters mask weak gyms.

## Test and scale (M1)
| Day | Kill/fix | Scale |
|---|---|---|
| 3 | Rejections, no gym_id, replies >30 min | n/a |
| 7 | CPL >₹600 and CTR <0.8%: fix creative | ₹150-400 hold |
| 14 | Cost per attended trial >₹1,430 (target ₹1,100): duplicate | Below ₹1,100: +20% per 3-4 days |
| 30 | Cost per member >₹9,000 (break-even ₹13.5k): cut | ≤₹6,000: scale, add deferred item |

F1: day 14 qualified >₹21k fix, ≤₹16k scale; day 90 signed-deal check.

## Confidence
M1 56, M2 52, G1 60, G2 55, F1 55; overall 57 (bands ±50%).
- M1 factors: Tracking 5, Budget 8, Cost evidence 3, Offer 5, Competitor 4, Policy 8, Season 6.
- Caps: forecasts ≤60 (no history); G2 55 until franchisee bidding stops.
- → ~72 if gym_id verified (+8), POS tally and margin supplied (+6), Ad Library scan (+3), CPL history (+5).

## Five creative angles (M1)
1. Pain: "Resolutions dying by February? Free 3-day pass nearby."
2. Proof: consented 12-week member stories, coach credentials.
3. Offer: free trial, real per-gym pass limits.
4. Authority: head coach walks through your first session.
5. Objection-killer: clear fee, no joining pressure (confirm terms).

## Plugin gaps (improvised)
- Pilot of 8-10 gyms vs "every gym": unclear if the pilot limits spend; I ran all 38 in clusters, 10 as measurement pilot.
- No rule for gyms per ad set (invented 7 clusters).
- "Trial-to-member" unit undefined.
- 55-70% Search default: per goal or overall unclear.
- Franchise cap vs Meta 3x CPR minimum contradictory (deferred).
- No franchise CPC benchmark; brand 5-10% rule covers competitors, not franchisees.
- "Open policy blocker" cap vs franchisee bidding ambiguous.
- No router-to-instant-form guidance; seasonality unscored live.
- The word cap conflicts with full deliverables; other campaigns' creatives left to launch.
