# Grade v04 (S1-S5) vs answer key
Scoring: Pass 1, Partial 0.5, Fail 0. outputs.md holds no per-scenario v0.3 scores, only the 87.5% total you gave, so I compare totals only.

| Scenario | Score |
|---|---|
| S1 SmileCraft | 8.5/9 |
| S2 VeloSkin | 6.5/9 |
| S3 PeopleOS | 9/9 |
| S4 Skyline | 7.5/9 |
| S5 Crumb & Co | 8/8 |
| **Total** | **39.5/44 = 89.8%** (baseline 87.5%, +2.3 pts) |

## Item-level
**S1:** Items 1-4 and 6-9 hit. Item 5 is partial: Google is Presence with a ~4 km radius, but Meta uses "living in or recently in" where the key wants a hard living-in boundary. The small-audience risk is noted.

**S2:**
- Hits: items 1-4 (value bidding, Advantage+ sales, PMax with brand exclusions and brand Search, acne claim treated as a launch blocker).
- Item 5 partial: it computes a break-even CPA of ₹480 and ROAS ~1.9 by inventing ₹150 shipping/COD/RTO costs. The key's ~1.4 (₹900 x 70% = ₹630 CPA) is never stated, and the invented inputs go beyond the scenario.
- Item 6 partial: creative angles and a creator test are given, but there is no volume target or refresh cadence.
- Item 7 partial: retargeting is folded into the Advantage+ campaign with a 15% existing-customer cap. The 85k IG pool is not used for a separate retargeting campaign.
- Item 8 partial: the 30k email list appears only as an "other channel" for repeat orders. It is not used for exclusions or lookalike seeds.
- Item 9 partial: confidence is 55 now and 72 after the claim is removed. The key expects 75-85 for verified value tracking and volume.

**S3:** All 9 hit. LinkedIn is flagged, Google is the core, the ₹23.3k per qualified demo figure is used, SQL import is planned, Meta is deferred, UAE gets its own campaign with a budget need stated, and negatives and the 60-90 day window are in. Confidence is 74 for C1 and 68 for C2.

**S4:** Items 1, 3, 4, 5, 6, 7 and 9 hit.
- Item 2 partial: the housing category is correctly "required US only, not India/UAE", but the US restrictions (no age/gender/postcode targeting, 15-mile radius, no lookalikes) are never listed. The US is deferred.
- Item 8 partial: Google Search covers project/location/configuration and competitor projects. The conflict between the hard boundary and NRIs is resolved with per-market campaigns (Presence UAE plus geo-intent keywords). It never offers interest-based targeting of Pune for NRIs abroad.

**S5:** All 8 hit. It rejects followers as a goal, runs one campaign, picks click-to-WhatsApp, lists Swiggy/Zomato in-app ads (D2), notes the small 3 km pool, defers Google in favour of free GBP, uses organic reels, and gives 57 confidence.

**Cross-cutting:** Guardrails and ranges with confidence are followed. S1, S2, S4 and S5 invent economics, and S2 invents COD/RTO costs. All are labelled "assumed", but they still go beyond the scenario.

## Plugin-rule gaps, prioritized
1. **D2C break-even.** Add one rule: break-even CPA = AOV x gross margin, with extra costs only if the client gives them. Report break-even ROAS ~1.4 first, then a target adjusted for repeat rate. Intake should ask for shipping/COD/RTO instead of letting the model invent them. (Fixes S2 item 5; S2 flagged "intake gaps".)
2. **Policy-blocker cap.** Say whether the cap applies per campaign or account-wide, and present the post-fix score as the headline for launch-with-fixes. (S2 item 9; S2 flagged the ambiguity.)
3. **Existing-audience tactics for D2C.** Require a separate retargeting campaign when the pools are large (social followers, email list, 30-day visitors), plus customer-list exclusions or seeds. Add a creative refresh cadence and a minimum number of concepts. (S2 items 6-8; S2 lists no existing-customer cap % and no brand-search benchmark.)
4. **US housing restrictions.** The plan must list the restrictions whenever a US audience is deferred or planned. Add a diaspora default: use interest-based location (people interested in Pune) for NRIs abroad, in a separate campaign per market. (S4 items 2 and 8; S4 improvisations 4 and 7.)
5. **Hard-boundary wording.** Resolve the contradiction between meta-ads-planner step 7 ("living in") and the intake table ("living or recently in"). Make hard boundary mean living-in on Meta. (S1, S5 and the baseline all flagged it; it cost S1 item 5.)
6. **Quality-gate vs word-cap conflict.** The "five prompts per campaign" rule cannot be met within the word cap (S1, S2, S4, S5). Either lower it to the main campaign only or raise the cap.
7. **Budget and split rules.**
   - State whether the budget is joint or per-platform (S3, S4).
   - Extend the learning-limited tier to Google and test budgets (S4).
   - Say which CPR point to test against (S5).
   - Add budget rules for brand and impression-share campaigns (S3).
8. **Funnel and measurement gaps.**
   - Add lead-to-attended and conversation-to-order benchmarks (S1, S5).
   - Add guidance for low-volume offline events: value rules or secondary imports (S4).
   - Fix the day-14 "real outcome" check for long sales cycles (S3).
   - Add a Tracking-factor definition for WhatsApp-native conversions (S1, S5).
9. **Vertical playbooks.** Add dental advertising law, health-data/DPDP limits on CAPI/CRM uploads, a bakery/food playbook, and a B2B ACV break-even formula with no-LinkedIn handling (S1, S3, S5).
10. **Minor.** Add a rule for vanity goals like followers, and Search-first intent order when there is no website (S5). Clarify the ambiguous day-7 cost rule (S2) and the ±35%/±50% band edge at the forecast cap of 60 (S1).
