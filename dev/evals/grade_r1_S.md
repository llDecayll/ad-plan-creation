# Grade r1 (S1-S5) vs answer key (Pass 1 / Partial 0.5 / Fail 0)

| Scenario | r1 | v0.4 |
|---|---|---|
| S1 SmileCraft | 8.5/9 | 8.5 |
| S2 VeloSkin | 7/9 | 6.5 |
| S3 PeopleOS | 9/9 | 9 |
| S4 Skyline | 8.5/9 | 7.5 |
| S5 Crumb & Co | 6/8 | 8 |
| **Total** | **39/44 = 88.6%** | 39.5 = 89.8% |

Delta vs v0.4: -1.2 pts (-0.5 item). Vs v0.3 (87.5%): +1.1 pts. Gains in S2/S4 offset by S5 regression.

## Item-level
**S1:** Items 1-8 hit (awareness reframed to bookings with empty-chair reason; Search on implants/aligners/RCT with call asset; Meta CTWA; Google 45%; Presence + living-in with expansion off; no condition targeting; cleaning/Rs999 excluded; Mon-Fri slots and attended tally). Item 9 partial: confidence 59/60 (about 68 after fixes) vs key 65-80, held down by the "attended tally untracked" cap.

**S2:** Hits: 1 (value bidding), 2 (Advantage+ sales plus catalog retargeting), 4 (acne claim declined), 5 (break-even Rs630 / ROAS 1.43, no invented costs; fixed from v0.4), 7 (Rs3k retargeting), 8 (existing-customer cap; 30k list as seed/exclusion).
- Item 3 partial: PMax with brand exclusions plus Shopping, but Brand Search deferred.
- Item 6 partial: five angles, but no volume target or refresh cadence ("testing folded into M1").
- Item 9 fail: 55 capped (66 fixed) vs 75-85.

**S3:** All 9 hit (LinkedIn flagged with 30-50% note, Rs23.3k per qualified demo, qualified-stage import, Meta Rs0, UAE separate with Rs19k minimum, long-cycle windows, negatives, thin-budget statement, C1 75).

**S4:** Items 1-3, 5-7, 9 hit (US required / India-UAE not; US restrictions listed; cost per visit; time zones; RERA; per-country campaigns resolve the hard-boundary vs NRI conflict).
- Item 4 partial: qualifying form fields added, but CAPI site-visit feedback explicitly not recommended ("unreachable").
- Item 8 hit (conflict resolved with per-market campaigns, Presence in UAE/USA).

**S5:** Hits: 1 (followers declined), 3 (CTWA), 4 (Swiggy/Zomato ads), 6 (no Google, GBP free), 8 (confidence 50).
- Item 2 partial: two campaigns (Rs270 + Rs30), not one.
- Item 5 fail: 3 km audience size and frequency not addressed.
- Item 7 partial: QR/organic suggested, but 10% still goes to paid follower engagement.

## Prioritized rule gaps and fixes
1. **Tiny-budget single-campaign rule (S5, cost 1.5).** Test cap, vanity cap and 3x minimum collide. Fix: below about Rs500/day, one campaign only; vanity-goal "support spend" is 0, organic only. Add hyperlocal rule: state audience size, set frequency cap/watch (above about 3 in 7 days = refresh).
2. **Confidence ceiling too punitive (S1, S2; cost 1.5).** "Real outcome untracked" and "policy blocker" caps push verified-tracking plans to 55-60. Fix: tally cap applies only when no tracking exists at all; a blocker cap applies to the pre-fix score and the headline is the post-fix score ("launch with fixes"), with a floor of 65 when value/lead events are verified and history or volume exists.
3. **Creative-volume rule for D2C (S2).** Fix: minimum concepts (e.g. 6+ at Rs10k/day+) and a refresh cadence (every 2-3 weeks or frequency above 3), exempt from the five-prompts word cap.
4. **Brand Search (S2).** Fix: for brands with Merchant/PMax, include brand Search at 3-5% as default; defer only if the brand has no search demand.
5. **Offline feedback at low volume (S4; run's own gap).** Fix: when visits are under 50/month, still send the site-visit event as a secondary or custom conversion/CAPI and optimise on the qualified-lead proxy; say so.
6. **Platform split vs cost-per-outcome (S1 gap 1).** Fix: tie-break: if derived cost-per-outcome favours one platform, shift up to 15 pts from the intent-order default, and state the reason.
7. **Contradictions the runs flagged:**
   - Hard boundary vs "living in or recently in" and pins vs one radius (S1, S5): hard boundary = living-in, expansion off; two pins allowed.
   - Diaspora "living in" vs "interest" (S4): living-in for the country campaign; interest for NRIs searching Pune on Google.
   - Joint vs per-platform pool (S3, S4): default joint.
   - Meta 7x CPR vs low-volume B2B (S3): learning-limited tier extends to B2B and test budgets.
   - Capped-score band step (S2): define as widening from +/-35% to +/-50%.
8. **Missing benchmarks and tracking definitions (S1, S3, S4, S5):** lead-to-attended and conversation-to-order anchors; tracking-factor definition for click-to-WhatsApp, no-website/manual tally, and "event verified, CRM unlinked"; UAE B2B and bakery CPR rows; brand/impression-share minimum budget (5-10% rule applies down to Rs500).
9. **Break-even without margin (S1, S5):** ask at intake; if absent, show a labelled 50% contribution assumption and cap cost evidence, as S5 did.
10. **Day-14 real-outcome gate for 45-90 day cycles (S3):** use proxy (qualified demo) plus a day 60-90 check, written into the rule.
