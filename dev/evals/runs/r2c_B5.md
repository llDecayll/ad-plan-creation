# B5 Akshara Foundation: ad plan (quality gate run; no live checks)

Not verified live (no web): Ad Library, PageSpeed, policy-watch, nonprofit status, GTM. Numbers are plugin-table or derived.

## 1. Real outcome and economics
- Outcome: a completed Razorpay donation, net of ~2% fee, plus repeat donors (22% in a year). It happens on the client's site (Razorpay, then /thank-you; GA4 `purchase` fires). 80G receipt auto-emailed.
- Break-even per donation ₹2,400 less 2% = ₹2,352; target ≤₹1,400; first-year value with repeats ~₹2,928.
- ₹1.2 Cr needs ~5,000 gifts (~417/month). Paid ₹1.5L/month yields ~₹19-49L/year. Paid cannot hit the goal alone; the rest needs email/WhatsApp to the own audience, CSR and major donors.

## 2. Goal translation / declined asks
- Honoured: online donations; Ad Grants.
- Declined: NRI donors (US/UK/UAE/SG). No FCRA registration. India-only; get counsel's view on Indian-citizen NRIs, then test. Sign-off: trustees + FCRA counsel.
- Declined: named children and "starving" copy (dignity, consent, policy). Alternative: consented or anonymised imagery and composite stories with verified figures, tested against the angles below. Sign-off: CEO.

## 3. Platform split
Intent order, no history. Grants are the Search channel (§7); paid Search needs ≥1× CPA (₹1,750/day) beyond what Meta's floor leaves. Meta 90% (₹1.35L), reserve 10% (₹15k, release day 14 to the winner), Google paid 0%, Grants ₹0.

## 4. Campaigns
| | C1 Meta India donors | C2 Google Ad Grants Search |
|---|---|---|
| Stage | Demand creation to decision | Demand capture |
| Objective / location | Sales; website donation page | Website donations |
| Optimise / bid | Purchase with value (Pixel+CAPI), Highest volume | Max conversions, GA4 purchase imported |
| Location | India "living in", expansion off, 18+, Advantage+ audience | India, Presence |
| Daily | ₹4,500 (+₹15k reserve) | ₹0 (~$10k in-kind) |

**Budget check.** C1: ₹4,500 ÷ ₹1,400 midpoint CPR = 3.2× (7× would be ₹9,800; at ₹2,000 it is 2.25×). Labelled learning-limited test, 14-day read, ~22 donations/week. C2: ≥15 clicks/day at ₹15-40 CPC is fine within the Grants cap.

**Forecast C1** (±50%+, plugin benchmark ₹800-2,000): 68-169 donations/month (mid 96); gift revenue ₹1.6-4.1L; first-gift ROAS 1.2-3.0×, ~2.1× with repeats; 15-37 repeat donors/year.
**Forecast C2** (derived, rough): 600-2,000 clicks × 1-3% = ~6-60 donations/month, ₹0 spend.
C2 setup: 2+ ad groups, multi-word phrase/exact keywords ("donate for child education", "80G donation education NGO", brand), sitelinks; negatives (jobs, volunteer, internship, free, scholarship, govt, courses). Fixes the single-word keywords behind the CTR failure.

## 5. Deferred and Other channels
- Paid Search: ₹1,750-3,500/day. Trigger: GA4 import verified and C1 CPR known.
- Meta retargeting/monthly-giving nurture: ~₹1,500/day (derived CPR ~₹500). Trigger: pool ≥3,000 after pixel; email/WhatsApp nurture to past donors meanwhile.
- Diaspora: ~₹25-30k/day per country (derived 6-20×); only after FCRA/counsel clearance, one country at a time.
- Peak shift (80G Jan-Mar, Giving Tuesday 1 Dec): client to approve moving 20-30% of off-peak spend.
- Other (outside plugin): own-list email/WhatsApp, CSR and major donors, Ketto/Milaap/GiveIndia, Meta Donate/fundraisers, GBP.

## 6. Special category / policy
Charity is not a Meta special category; India only: "not required, do not opt in; verify live". Check Meta social-issue authorisation if copy turns to advocacy. Verify nonprofit status (Google for Nonprofits, Meta charity tools). Grants: appeal and rebuild, never a second account. DPDP purpose line and privacy link. No identifiable children.

## 7. Operating constraints
One fundraising officer: flow is self-serve (UPI, auto 80G email). Officer handles payment failures and gifts ≥₹10k within 24h.

## 8. Risks / blockers
1. No Meta pixel: no C1 launch until Pixel+CAPI fire on /thank-you (day-0 test donation).
2. GA4 purchase not in Google Ads: C2 capped until imported.
3. Goal unrealistic from paid alone.
4. FCRA; CEO creative ask; Grants ≥5% CTR rule.

## 9. Test and scale (₹)
| Day | Look at | Kill/fix if | Scale if |
|---|---|---|---|
| 3 | Approvals; Pixel vs Razorpay within 20% | Not firing; rejections | n/a |
| 7 | CPR vs ₹800-2,000; CTR; Grants CTR | CPR >₹3,000 and CTR <0.8%: creative fix; Grants CTR <5%: pause weak keywords | In range: hold |
| 14 | Cost per donation (≥20 donations) | >₹1,820: new-angle duplicate | <₹1,400: release reserve, +20% every 3-4 days |
| 30 | Net vs ₹2,352 break-even | Above: cut/restructure | At target: fund Search/retargeting |
Repeat-donor check at day 90.

## 10. Confidence
| | Now | After fix | Factors (track/budget/cost/offer/comp/policy/season) | Caps |
|---|---|---|---|---|
| C1 | 40 | ~49 | 0→6 / 5 / 3 / 5 / 4 / 6 / 5 | Untracked event cap 40 (per campaign) |
| C2 | 42 | ~52 | 4 / 5 / 3 / 5 / 4 / 3 / 5 | "Events exist, not linked" cap 45 (per campaign) |
Overall 40 now, ~49 after fixes (C1 only; C2 excluded). Band: fix blockers first. Raises: Pixel/CAPI verified (+9), 90-day cost per donation (+8), live Ad Library scan (+3).

## 11. Five creative angles (C1)
1. Pain: "Many Class 5 children can't read a Class 2 text" (verified figure; composite child).
2. Proof: "Where your ₹2,400 goes", anonymised classroom plus 80G receipt.
3. Offer/urgency: "Give by 31 Mar, claim 80G" or a real match day.
4. Authority: a teacher on camera, three steps from gift to reading.
5. Objection-killer: "Is it safe?" 12A/80G, instant receipt, UPI, ₹200/month option.

## 12. Plugin gaps / improvisation
- Gate J's 50% margin assumption does not fit donations; I used net gift after the 2% fee.
- Budget rules clash (7× vs 3× vs playbook 3×); I applied §7 and showed the high-end downside.
- No Donate-button/fundraiser guidance; chose Sales+Purchase.
- No nonprofit CPC, Grants conversion or diaspora CPR benchmarks (all derived).
- "No pixel" is not a defined status; I used "untracked", cap 40. Whether literacy advocacy needs Meta authorisation is unclear.
- Unclear whether in-kind Grants count in the budget (I used §7, excluded).
- Retargeting pool needs a pixel that does not exist yet.
