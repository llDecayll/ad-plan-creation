# B5 Akshara Foundation: paid plan (no live checks run; Ad Library, SERP, policy, FCRA and Ad Grants rules are playbook/benchmark values to verify live)

## Real outcome + economics
- Outcome: a completed online donation (net of the ~2% Razorpay fee), plus a repeat gift. Average gift is ₹2,400; 22% repeat within a year, so year-one value is about ₹2,400 x 1.22 = ₹2,930 (~₹2,870 net).
- Allowable cost per donation: ₹2,350 break-even on the first gift. Target is ₹1,400 or less (ROAS 1.7+). Unit is "one online gift". Margin is not applicable; the fee is the only cost given.
- Transaction: own site, Razorpay, then /thank-you with GA4 `purchase`. Google can see it only after GA4 is linked and imported. Meta sees nothing (no pixel). Reconcile weekly against the Razorpay settlement report. A gap above 20% means tracking is broken.
- ₹1.2 Cr = 5,000 gifts a year (~417 a month). Paid ₹1.5L/month buys about 107 gifts (₹2.6L), so paid is roughly ₹31L a year at best, about 25% of the goal. Stated plainly: paid cannot deliver ₹1.2 Cr.

## Goal translation and declined asks
- Reframe: paid media is one pillar, and the ₹1.2 Cr needs email/WhatsApp to the existing donor list, CSR and the 80G push. The target is cost per donation and ROAS, not ₹1.2 Cr from ads.
- Declined 1, NRI donors in US/UK/UAE/Singapore: no FCRA registration (pending, no date). Defer the whole diaspora campaign. Indian-citizen NRIs need counsel's confirmation. Sign-off: trustees and legal counsel. Alternative: India-only now, with Razorpay international cards off.
- Declined 2, named, identifiable children and "Rani, 8, can't read — her family is starving": breaks guardrail 7. Sign-off: CEO. Alternative: consented, anonymised or composite stories with verified figures ("X children reading at grade level"), and test the emotional angle against proof.
- Accepted: Ad Grants, rebuilt compliantly.

## Platform split and why
Budget is one joint pool: ₹1,50,000 a month = ₹5,000 a day. Paid is 100% Meta. Search intent is served free by Ad Grants, and paid Google cannot meet its minimum (₹1,750 a day) without starving Meta.

## Campaigns
**C1 Meta, India donors (funded)**
- Journey stage: lower funnel, cold prospecting. Objective: Sales. Conversion location: website. Optimisation event: Purchase/Donate via pixel + CAPI.
- Bid: Highest volume. Advantage+ audience, one ad set, 3-5 creatives, "People living in India", location expansion off. Always-on (self-serve). Daily budget ₹5,000.
- Budget check: CPR midpoint ₹1,400, so ₹5,000 = 3.6x. That passes the 3x learning-limited test level, not the 7x minimum (₹9,800). At the ₹2,000 high end it is 2.5x, which fails. Label it a learning-limited test with a 14-day read. About 25 gifts a week is under 50, so InitiateCheckout is the labelled fallback.
- Forecast, range ±50% (derived, plugin benchmark ₹800-2,000): 107 gifts a month (75-188), ₹2.6L raised (₹1.8-4.5L), ROAS 1.7 (1.2-3.0). Real outcome: net donations ₹2.5L, with repeat adding about 22% over 12 months.

**C2 Google Ad Grants, India (funded in-kind, separate ₹0 account)**
- Journey stage: lower funnel. Type: Search, text only. Conversion: website, GA4 `purchase` imported. Bid: Maximise conversions. Presence in India. Budget ₹0 (about USD 10,000 a month in-kind credit).
- Budget check: ≥15 clicks a day is feasible from the in-kind credit. The $2 CPC cap is lifted by Max conversions.
- Rebuild after the suspension: 2+ ad groups, multi-word keywords only ("donate for child education India", "80G donation NGO"), sitelinks, quality score 3+, account CTR ≥5%. Appeal or reactivate the existing account; never open a second one.
- Forecast, derived: 1,500-3,000 clicks x 1-2% = 15-60 gifts a month (₹36k-1.4L), rough.

## Deferred (client decision)
- Diaspora (US/UK/UAE/SG): after FCRA/counsel clearance. Derived ₹ needed per country: ₹35k-85k a day for the US/UK, ₹12k-25k a day for UAE (3x CPR with the 3-20x market multipliers).
- Paid Google Search: ₹1,750-2,000 a day (₹55-60k a month). Trigger: Grants saturated and GA4 import verified.
- Meta retargeting/donor reactivation: ₹1,100-2,700 a day. Trigger: pool of several thousand in 30 days.

## Other channels
- Email/WhatsApp to the donor base (22% repeat; cheapest)
- Meta fundraisers / donate button
- CSR/corporate giving
- Giving platforms (Give/Milaap/Ketto)
- GBP (free)

## Policy decisions
- Special ad category: none (charity). Not required for India. Verify live. Verify nonprofit status via Meta charity tools / Google for Nonprofits. If copy becomes advocacy, check social-issue authorisation.
- India securities declaration: not applicable.
- 80G claim only if the certificate is current. No FCRA language. No "starving" distress claims.

## Operating constraints
- One fundraising officer, but donation is self-serve. Large-gift/CSR enquiries get a next-working-day reply. 80G receipts are auto-emailed.
- Seasonal calendar (verify dates): Daan Utsav (early Oct), Diwali, Giving Tuesday (Dec 1), Jan-Mar 80G push. Shift 20-30% of Apr-Sep budget into Jan-Mar, at the cost of off-peak.

## Key risks and blockers
1. No Meta pixel/CAPI: install before launch, with a day-0 test donation.
2. GA4 purchase not linked or imported to Google Ads.
3. Ad Grants account status and suspension cause unconfirmed.
4. FCRA exposure: international cards must be off.
5. Razorpay thank-you must carry fbclid/gclid and UTMs (UTMs improvised; url-parameters.md not read).

## Test-and-scale (₹)
| Day | Check | Kill/fix | Scale |
|---|---|---|---|
| 3 | Approvals, pixel/GA4 firing, test donation | Events not firing, or named-child creative | none |
| 7 | CPR vs ₹800-2,000, CTR | CPR over ₹3,000 and CTR under 0.8%: change creative/offer | ₹800-2,000: hold |
| 14 | Razorpay-reconciled cost per gift | Over ₹1,800: duplicate with new creative/goal | Under ₹1,400 and stable: +20% every 3-4 days |
| 30 | Net ROAS | Cost per gift over ₹2,350: restructure | ROAS 1.7+: fund Google Search or retargeting |
| 90 | Repeat-donor rate vs 22% | Below 10%: rethink reactivation | At or above 22%: add to the value assumption |

## Confidence
| Campaign | Now | After fix | Cap applied |
|---|---|---|---|
| C1 Meta | 40 | ~55 | Untracked event (per campaign); learning-limited cap 60 after fix |
| C2 Ad Grants | 45 | ~58 | "Events exist, not linked" (per campaign) |
| Overall | 40 | ~55 | Only C1 is funded |

- C1 factors (0-10): tracking 2, budget 5, cost evidence 3, offer 6, competitor 4, policy 6, season 7.
- C2 factors (0-10): tracking 4, budget 7, cost 3, offer 6, competitor 4, policy 3, season 7.
- Forecast bands ±50%. Band: fix blockers first, or run as a small test.
- Raises: pixel/CAPI verified (+10), live Ad Library scan (+3), own cost-per-gift data (+8).

## Five creative angles (C1)
1. Proof: "₹2,400 keeps 4 children in a reading programme for a term" (verified figure).
2. Pain/problem: "1 in 3 Class 5 children can't read a Class 2 paragraph" (verified stat, anonymised).
3. Offer/urgency: 80G tax-saving, with the FY-end deadline and a matching gift.
4. Authority/process: "Where your ₹ goes, in 5 steps", with an annual report and 12A/80G badge.
5. Objection-killer: "Receipt in 60 seconds, 100% transparent, cancel monthly gift anytime."

## Improvised or unclear in the plugin
- The plugin's own gates conflict. §1 minimum is 7x CPR (₹9,800 a day) but the budget is ₹5,000. I used the v0.5.3 donation rule (3x). The "test cap 10-20%" is unclear when the only funded campaign is itself a test.
- Overall spend-weighting when the second campaign has a ₹0 budget is unspecified. I used C1 only.
- No benchmark for Ad Grants volume. I derived 1-2% conversion and clicks (labelled).
- The paid-Google minimum (₹1,750 a day) contradicts the 55-70% Search default. I chose "Grants as Search" without a rule that says so.
- Diaspora deferral ₹ figures are derived from multipliers meant for CPC, not donations.
- url-parameters.md was not in my read list.
- Not live-checked: Ad Library, SERP, Ad Grants rules, FCRA, festival dates, policy, status of GA4 events.
