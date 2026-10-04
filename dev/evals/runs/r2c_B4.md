# B4 IronCore Fitness plan

Assumptions: ₹50,000/day joint pool (₹15L/30). Margin unknown: labelled 50% (cost evidence ≤50). "Trial-to-member 24%" = attended trial to paid member. No live checks (would verify GTM/Pixel, GBPs, Ad Library, keyword volume, policy).

## Outcome, economics, transaction
Consumer: paid member. ₹27k midpoint × 50% = ₹13.5k, so break-even ₹13.5k per member, ₹3.2k per attended trial. Franchise: qualified investor (capacity ≥ ₹25L fee, timeline ≤6 months), then signing (₹25L fee; labelled 50% = ₹12.5L). Transaction: gym desk/POS (invisible; weekly tally) and the BD manager's CRM.

## Goal translation, declined asks
- "Trial sign-ups for every gym": kept, judged on cost per attended trial/member. "Equal per gym" declined: spend follows capacity and closers; the 9% gym gets an ops fix first. Sign-off: marketing head.
- "20 franchise leads": defined as qualified; funded for ~15 (8-36). Sign-off: franchise head. 85/15 split: CEO/MD.
- Declined "₹8L profit/month assured": use "investment ₹1.5-2 Cr, payback not guaranteed". Sign-off: franchise head + legal.
- Declined franchisee brand bidding: agreement clause, Auction Insights, head office owns brand terms. Sign-off: franchise head.
- Declined 22 franchisee pages with own offers: creative kit + Partnership Ads. Sign-off: marketing head.

## Platform split
Consumer ₹42,500 (85%), franchise ₹7,500 (15%). Meta is cheaper per attended trial (₹1,150 vs ₹1,770, derived), but 14 city ad sets × ₹1,925 = ₹26,950 is unaffordable. So Search covers all 38 gyms; Meta is a 5-city, 10-gym pilot (best/average/worst) with a ₹7,000 reserve (14%), released day 30 if cost per attended trial ≤₹1,500 and gym_id is verified. Franchise is Search only.

## Campaigns
| # | Platform, stage | Conversion location; event; bid | Location | ₹/day | Budget check | Forecast |
|---|---|---|---|---|---|---|
| C1 | Google Search, bottom, non-brand, 14 city campaigns | Form with gym picker; GA4 generate_lead; Max conversions | Presence, 5 km pins | 18,800 | CPA ₹425, CPC ₹30 (derived): min max(₹425, 15×₹30=₹450); city floor ₹900 ≥ 2×CPA. Pass | 29-89 leads/day; 2.5 members/day (50-154/mo); ₹7.4k/member (₹3.7-11.3k) |
| C2 | Search brand | Same | Presence | 1,700 | 8% of Search; min ₹450. Pass | 7-25 leads/day (derived); separate report |
| C3 | Meta Leads, bottom, 5-city pilot | Higher-intent instant form with gym picker + WhatsApp confirm; Leads; Highest volume | Living in or recently in, 5 km pins merged, expansion off | 15,000 | CPR ₹275 (high ₹410): 7× = ₹1,925 (₹2,870 high). ₹3,000/city passes | 37-107 leads/day; ~96 members/mo; ₹4.7k/member (₹2.4-7.0k) |
| C4 | Search, franchise | Form with investor qualifiers; Max conversions | India, presence or interest | 7,500 | CPA ₹3,750: 2× = ₹7,500. Pass | 40-120 leads/mo; 8-36 qualified; ₹15k each; ~1 signing/mo (assumed 5-10%) |
| Reserve | Meta roll-out | n/a | n/a | 7,000 | 3 cities at minimum | Held |

Sum: 18,800+1,700+15,000+7,500+7,000 = ₹50,000. Blended consumer ≈5.7 members/day at ~₹6.2k vs ₹13.5k break-even. All forecasts: benchmark table, ±50%.

## Deferred (₹) and Other channels
- Meta, 6 more cities: ₹11,550/day more (marketing head).
- Meta franchise: ≥₹12k/day (franchise head).
- UAE NRI test: ~₹6,000/day, after legal clearance, ≤10%.
- PMax store visits: ~₹2,000/day, after GBPs are fixed.
- Other channels: GBP fixes and location group (free); LinkedIn/franchise portals (~30% of franchise budget); Cult.fit/Fitpass-type listings; WhatsApp/email to lapsed trials, member referrals.

## Policy
Consumer: no special category, not required, do not opt in. Franchise: not required outside US/CA/EU; answer India investment declaration accurately; verify live (Meta financial products, Google financial services). Qualifier questions, no earnings claims. 18+, no body-shaming, limited before/after, no health claims. Checked from baseline, not live.

## Operating constraints
Search schedule matches desk hours; Meta uses away message plus morning follow-up. Router replies ≤15 minutes; offers steer to empty slots. Pass gym_id into GA4 and router. BD manager gets scheduled callbacks (~60 leads/month). Weekly POS tally by campaign code. 30/60/90 pilot.

## Risks and blockers
1. No gym_id in router (launch blocker).
2. Six duplicate GBPs.
3. Franchisee brand bids.
4. Pixel/Ads import unconfirmed.
5. POS not integrated.
6. Margin unknown.
7. 20 qualified franchise leads is a stretch.
8. Worst gym wastes leads.

## Test and scale
| Day | Kill/fix if | Scale if |
|---|---|---|
| 3 | Rejections, no gym_id, replies >30 min | n/a |
| 7 | Meta CPL >₹615 with CTR <0.8%; Search CPL >₹960 | Hold |
| 14 | Cost per attended trial >₹1,500 Meta / ₹2,300 Search; franchise qualified >₹19.5k | Below target: +20% every 3-4 days |
| 30 | Cost per member >₹13.5k; gym <12% close: halve spend | ≤₹7k: release reserve. Day 60-90 franchise signings check |

## Confidence
C1 60, C2 64, C3 62, C4 55 (factors T/B/Cost/Offer/Comp/Pol/Season: C1 5/9/3/6/4/7/7; C2 5/10/3/6/6/7/7; C3 5/10/3/6/4/7/7; C4 5/9/3/5/4/6/5). Overall 60 (spend-weighted, reserve excluded). Caps: no client CPL or live benchmark, so forecasts ≤60 and bands ±50%. Launch with fixes. ~76 if gym_id and POS import verified (+8), live benchmarks and Ad Library scan (+5), margin supplied (+3).

## Creative angles (C3)
1. Pain: resolutions fade by February; free pass nearby.
2. Proof: consented members plus that gym's rating.
3. Offer: free trial pass until a real date.
4. Authority: head trainer's 5-step first session.
5. Objection: no joining pressure, from ₹1,500/month (client to confirm).

## Plugin gaps and improvisation
- Hard catchments need city ad sets but 14 cities fail 7× CPR; pilot and reserve are mine.
- Franchise Meta CPR ₹4,000 fails 3× within the cap; no nearer-funnel event, so deferred.
- Franchise share 15-25% vs 15-20%; used 15%.
- No sign-off owner for the split; named CEO.
- No gym CPC benchmark (derived ₹30); funnel anchors assumed.
- Margin treatment for a one-time fee unspecified.
- Reserve cap basis unclear.
- Manual-tally tracking score range 5-7; used 5.
- "Qualified lead" undefined.
- Gate F (five creatives each) vs word cap; gate K resolved it.
