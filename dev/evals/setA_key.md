# Ad-Planning Exam — Set A Grading Key (A1–A6)

Score each checkpoint as Pass (1), Partial (0.5) or Fail (0). Checkpoints marked **[TRAP]** test whether the tool spots something wrong in the brief; failing a trap is a red flag regardless of the total score.

---

## A1 — Shaant meditation app

1. Does not optimise for installs. Recommends Google App campaigns (ACi) optimised for `trial_start` and later `purchase` (tCPA, then tROAS once volume allows), and Meta app-promotion campaigns optimised for an in-app event rather than installs.
2. Uses the history as evidence: a ₹14 CPI with 0.4% trial start works out to roughly ₹3,500 per trial and about ₹19,400 per payer. That is far above the ₹1,150 India LTV, so cheap installs destroy value.
3. **[TRAP]** Refuses the "Are you depressed? Shaant can cure it" headline. It breaks Meta's personal-attributes policy (it asserts a health condition) and is an unsubstantiated medical "cure" claim. The tool proposes compliant alternatives, such as "Wind down with a 10-minute sleep story".
4. **[TRAP]** States that Meta has no detailed targeting for health conditions (those options were removed) and that Google does not allow personalised targeting on health conditions. The plan therefore uses broad or Advantage+ audiences and interest proxies like sleep, yoga and wellness, not condition targeting. It also flags that Meta's health and wellness data restrictions may limit lower-funnel event optimisation, and treats that as a confidence reducer.
5. Requires a tracking fix before launch: link Firebase to Google Ads and import `trial_start`/`purchase`, connect AppsFlyer to Meta and Google (SDK or Meta AEM), set up a SKAN/AdAttributionKit conversion-value schema for iOS, and reconcile against store revenue net of the 15% fee.
6. Treats the UK as a separate test with its own campaigns, currency and budget. It notes the better UK unit economics (31% trial-to-paid, LTV around £33) and that this makes a small UK test worth running, but limits the test to a bounded share of budget, about 15–25%.
7. Checks whether the budget is enough to exit learning. ₹2.5L/month is about ₹8.3k/day. The plan must not split this across more than 2–3 campaigns, and it estimates whether optimising on `trial_start` gives enough weekly events (about 50 per week per ad set on Meta, and roughly 10+ per day recommended for ACi tCPA). If it doesn't, the tool proposes a proxy event.
8. Recommends creative that fits app ads: 9:16 Reels or Shorts showing the actual app UI and an audio preview, a free-trial CTA, and store-listing (ASO) consistency. Repurposing the existing breathing Reels counts as a plus.
9. Uses device and geography controls to address the Tier-3 problem through optimisation event and value, not by blanket-excluding regions without data. Excluding regions is acceptable as a test and should be stated with low confidence.

---

## A2 — Hearth & Loom UK homewares

1. **[TRAP]** Flags Consent Mode v2 as mandatory for UK/EEA traffic: Google's EU user consent policy requires it for remarketing and personalised measurement. Recommends a certified CMP (or wiring Shopify's Customer Privacy API to Consent Mode) and Advanced Consent Mode for modelling, and puts this before scaling.
2. **[TRAP]** Questions the 7.8x PMax ROAS. Brand search rose while total revenue stayed flat, which points to PMax harvesting branded and returning-customer demand. Recommends brand exclusions in PMax (or a separate Brand Search campaign), customer-acquisition goal settings, and judging by blended MER or new-customer revenue in Shopify.
3. Calls the Merchant Center fixes blockers: add GTINs (or set `identifier_exists` correctly for own-brand products) and fix or remove the promotion causing the misrepresentation flag. Treats Shopping/PMax confidence as conditional on feed health.
4. Proposes Google Shopping/PMax with feed segmentation by margin or bestseller status (custom labels), plus brand search. Optionally adds a Standard Shopping campaign for control on hero categories.
5. Recommends a Meta Advantage+ Sales (shopping) campaign optimised for Purchase with the catalogue connected. Requires Conversions API through the Shopify Meta channel app, with the event match quality and deduplication checks it implies.
6. Uses Q4 seasonality: front-loads the budget into October–December and has creative and promotions ready before Black Friday. Also sets the 4x target against margin (58% margin gives a breakeven ROAS of about 1.7, so 4x is a choice, not a floor). Recommends a lower new-customer target given 30% reorder value.
7. Sets location to UK only, with Ireland excluded (or "presence" targeting so Irish users browsing UK content are not reached), and uses GBP currency feeds.
8. Recommends creative for Instagram/Pinterest-style UGC Reels and lifestyle carousels. Raises Pinterest as an optional channel or later test without derailing the Meta/Google plan.
9. Gives a realistic split for £9k/month (for example about 55–60% Google, 40–45% Meta, or justifies a different split) with stated confidence, and does not fragment budget across many PMax campaigns.

---

## A3 — CareBridge nurse recruitment (US)

1. **[TRAP]** Declares Meta's Employment Special Ad Category. States that it removes age and gender targeting, removes ZIP-level targeting, and enforces a minimum radius of about 15 miles. Refuses the "women 24–40" and "exclude over 50" request as discriminatory: it would breach Meta and Google policy and likely US employment law (ADEA, Title VII).
2. **[TRAP]** States that Google's US employment ads policy also prohibits age, gender, parental status, marital status and ZIP-code targeting in personalised ads.
3. Uses qualification inside the ad and lead flow rather than demographics. Examples: "RN licence (TX or compact)" and "1+ years acute care" as required instant-form questions or ad copy filters, plus a higher-intent form type to fix the 80% CNA/student problem.
4. Recommends Google Search on high-intent terms ("RN jobs Houston", "ICU nurse jobs Dallas", "travel nurse Texas") with negatives for CNA, LPN, student, school, salary-only and "how to become". Budget is weighted toward Search given the $4–9 CPCs and intent.
5. Does the maths on the economics: 200 qualified applications × 1/6 ≈ 33 placements × $9,500 ≈ $317k revenue against $18k spend. Allowable CPA is high (up to about $90 per qualified applicant). It also judges whether 200 applications in 60 days is realistic at $18k (about $300/day) and states its confidence.
6. Addresses tracking: thank-you-page pixel on the ATS for Meta, Conversions API, or recruiter-qualified offline conversions uploaded back to Meta and Google (CRM/ATS export with click IDs, or enhanced conversions for leads). It notes that the missing Google tag on the ATS needs a fix (GTM on the ATS thank-you page or cross-domain tracking) or a lead-form asset fallback.
7. Respects recruiter capacity: two recruiters with a 48-hour screening SLA. Paces lead volume, or recommends instant SMS or call follow-up and lead-routing alerts.
8. Handles locations: hard Houston and Dallas metros with radius at or above the SAC minimum, and a separate small, lower-priority "travel nurse — Texas" campaign or ad set.
9. Creative recommendations show real nurses and shift and pay specifics where legally accurate (for example sign-on bonus, pay range, which Texas pay-transparency practice allows), and avoid any demographic-exclusionary imagery or wording.

---

## A4 — Vidyanidhi engineering admissions

1. **[TRAP]** Refuses "100% placement" and "#1 in Karnataka" as false or unsubstantiated (actual figures: 64% placement, NIRF 151–200). Notes Google's misrepresentation policy, Meta's deceptive-claims policy and Indian advertising standards (ASCI, UGC/AICTE guidance on misleading claims). Offers verifiable alternatives, such as "64% of 2025 eligible graduates placed, top recruiters X/Y".
2. **[TRAP]** Addresses minors: applicants are 16–18. Meta limits ad targeting for under-18s to age and location, and Google does not serve personalised ads to under-18s. The plan therefore targets parents (40–55) as primary decision-makers and reaches students only through broad, compliant settings.
3. Builds a seasonal phasing plan. October–February is a low-spend nurture and awareness phase (YouTube, Meta video, remarketing pool build). The bulk of the budget (for example 60–70%) goes into March–July around KCET/COMEDK/JEE results. Includes result-day bursts.
4. Resolves the Chairman vs Admissions Director conflict explicitly. Gives a bounded awareness budget (for example 15–25%) measured on reach, frequency and branded search lift, and the rest goes to enquiries and applications. Names who signs off on the split.
5. Fixes measurement: GA4 enquiry is only a soft signal, so the plan proposes offline conversion import of "application fee paid" and "admission confirmed" from the ERP or call-centre CRM (GCLID/FBCLID capture on the form, or enhanced conversions for leads), and moves bidding to those once volume allows.
6. Uses Meta instant forms with qualifying questions (stream, entrance exam taken, expected score range, preferred city) and higher-intent settings. Uses WhatsApp or call routing, and accounts for call-centre hours with lead scheduling and dayparting, or after-hours auto-reply on WhatsApp.
7. Location strategy: state-level targeting in the four states, and Gulf NRI parents as a separate small test (UAE, Saudi, Qatar, Oman) with English and Malayalam/Telugu creative. Notes the NRI quota or fee difference if relevant.
8. Recommends Google Search keyword themes (management quota, direct admission, branch + city) with negatives (government college, cutoff-only queries, jobs, recruitment), and notes that CPCs rise from March to July.
9. Gives a sense of capacity and economics: 720 seats, ₹60L budget ≈ ₹8,300 per seat filled as a ceiling. The tool estimates the enquiry → application → admission funnel and states its confidence.

---

## A5 — RupeeRaft personal loans

1. **[TRAP]** Refuses "0% interest", "no CIBIL check" and "guaranteed approval". These are false (APR 18–36%, 22% approval rate) and banned by Google's Financial Services and personal-loan policies and Meta's financial services and deceptive-claims rules. They also conflict with RBI Digital Lending Guidelines (KFS/APR disclosure). The tool provides compliant copy with a representative APR or "APR 18%–36%" disclosure.
2. **[TRAP]** Refuses targeting "people with low credit scores". Meta's personal-attributes policy forbids asserting financial status, and credit-status targeting is not available or is restricted. Recommends broad targeting with compliant creative.
3. Requires Google India financial services verification and personal-loan policy compliance before any spend: lender licence declaration, NBFC partner named on the site and app, minimum and maximum repayment period, max APR, and a representative total-cost example. Notes the Play Store personal-loan app declaration.
4. **[TRAP]** Treats the previous Google suspension ("unacceptable business practices") as a blocker. The plan must investigate and appeal or resolve it, not create a new account. Opening a new account is circumvention and risks a permanent ban. Google work is held at low confidence or deferred until this is resolved.
5. States the Meta Special Ad Category or financial services declaration for credit, per current Meta policy for India, and its targeting limits. Says to verify the current status if unsure.
6. Optimises deep in the funnel: Meta app campaigns on `kyc_complete`, then `loan_disbursed` once volume allows. Value: ₹1,800 per disbursal → at a 22% approval rate the tool computes an allowable cost per KYC/application. The ₹38 CPI is judged against downstream disbursal, not alone.
7. Addresses the 1–3 day lag between install and disbursal: picks a shorter-latency optimisation event (KYC complete) as primary and imports disbursal as a secondary or value signal. Adds Conversions API for the web flow.
8. Location: India with J&K and the North-Eastern states excluded, set as hard exclusions on both platforms.
9. Recommends trust-led creative: NBFC partner name, RBI-registered, transparent fees and a grievance officer contact. Notes that lending ads with trust signals perform better given the reputation problems of loan apps.

---

## A6 — SunGrid Solar (broken tracking)

1. **[TRAP]** Diagnoses the inflated conversions. GA4 `generate_lead` fires on the form page-view, not on submission, and the Google Ads tag and the imported GA4 conversion are both primary, so leads are double-counted. 412 reported vs 92 CRM enquiries means the real cost per lead is about A$65, not A$22.
2. **[TRAP]** Rejects tripling the budget until tracking is fixed. Maximize Conversions has been training on fake conversions for 14 months, so scaling now would scale waste.
3. Gives a specific fix list: move the event to a confirmed submission or thank-you page, keep one primary conversion (Ads tag or GA4 import, not both), add call tracking (call assets with Google forwarding numbers plus website call conversions), add enhanced conversions for leads, and import HubSpot offline conversions (qualified lead, site visit booked, sale).
4. Plans a recovery period: temporarily switch to Manual CPC/Max Clicks with a CPC cap or to tCPA on corrected data, or accept a relearning period, and states when to re-enable smart bidding (for example after 30+ clean conversions in 30 days).
5. Cleans search terms: negatives for jobs, careers, DIY, rebate application, "how to", and possibly "free". Uses phrase and exact match on high-intent queries such as "solar panels installer Melbourne" and "solar quote".
6. **[TRAP]** Refuses "Free solar panels — government pays" style claims as misleading under ACCC/Australian Consumer Law and platform misrepresentation rules. Any rebate or STC claim must be accurate and conditional. "$0 upfront" may only be used if finance is actually offered with the required disclosures.
7. Adds qualification to remove renters and apartment dwellers (25% waste). Uses a homeowner question and roof type on the Meta instant form, landing page copy saying "for homeowners", and keyword and audience choices that reflect this.
8. Location: Melbourne metro + Geelong set to "presence" (people in the area), with a radius of 80 km or less from the depot. Excludes areas the installers can't service.
9. Gives a staged budget plan: start Meta at a modest test (for example A$2–4k/month) with lead forms or website leads, and scale overall spend in steps tied to CRM-verified cost per qualified lead. Unit economics: A$9,500 × 28% margin ≈ A$2,660 gross profit; at a 15% close rate the allowable cost per qualified lead is about A$400 at breakeven.
