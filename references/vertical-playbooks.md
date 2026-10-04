# Vertical playbooks: business truth, traps and channel norms

Read the section(s) matching the client. Each lists the **real outcome** to optimise toward (not the platform's proxy), the common traps, and must-do items. Policy details change: confirm live before quoting rules as current.

## Universal truths (apply to every plan)
- **Platform-reported results are not business results.** Reconcile platform conversions with the CRM/store/backend. If they differ by >20%, treat tracking as broken until explained (double-firing, page-view-as-lead, duplicates, view-through inflation).
- **Attribution conflicts:** GA4 last-click under-credits Meta and over-credits brand search; platforms over-credit themselves. Decide with CRM cost per real outcome, blended efficiency (MER = total revenue ÷ total ad spend), and incrementality tests (geo holdouts, Meta conversion lift, Google brand-search pause tests) — not with whichever dashboard a stakeholder prefers.
- **Brand search:** PMax and broad match harvest existing brand demand and inflate ROAS. Use brand exclusions in PMax, a separate small brand campaign, and judge non-brand performance separately.
- **Never scale on broken data.** If tracking is broken, fix and verify first; meanwhile keep spend flat or reduce, and optimise to the most reliable event.
- **Test plan with kill/scale rules** for every launch (see quality-gate.md).

## Local services (clinics, salons, home services, gyms, repairs)
- Real outcome: booked AND attended appointment / completed job. Track show-up rate (CRM or manual tally) and feed it back (offline conversions, conversion leads).
- Must-do: Google Business Profile hygiene (verified, de-duplicated, reviews), call assets + call tracking, location assets, radius targeting, ad schedule matched to who answers (Google ad schedule; Meta scheduling needs lifetime budget, otherwise use away messages + morning follow-up).
- Capacity: if specific days/slots are empty, use day-parting, slot-specific offers and bid adjustments; don't buy demand for days already full.
- Separate high-value services (implants, aligners, AC installation) from low-value ones (cleaning, servicing) in ad groups/creatives; low-price hooks fill the funnel with low-value leads.
- Google lead form assets bring cheap low-quality leads for high-ticket local services; default off unless qualifying questions are added.
- Health: no targeting or copy that implies the viewer's condition; no guaranteed outcomes; before/after limits.
- Directories (Practo, Justdial, UrbanCompany) and LSAs where available: mention as channels.

## D2C / e-commerce
- Real outcome: contribution margin after returns. India: COD orders with 15-35% RTO (return-to-origin) inflate platform ROAS — optimise on prepaid or delivered purchases where possible (send a "Purchase-Prepaid" or "Delivered" event via CAPI/offline), push prepaid with incentives, and use RTO-adjusted CPA.
- Unit economics: break-even CPA = AOV × gross margin − shipping/payment/RTO cost; break-even ROAS = 1 ÷ contribution margin %. Use 90-day LTV to set the acquisition target; separate new-customer CAC from blended.
- Structure: Meta Advantage+ sales (with existing-customer budget cap) as the core; catalog ads; partnership/creator ads (whitelisting) and UGC; Google PMax with feed + brand exclusions, Standard Shopping for control, brand Search; Demand Gen for video.
- Creative is the main lever: plan volume (at ₹10k+/day, 5-10 new concepts per week), refresh when frequency > 3/week or CTR falls 30%.
- Claims: cosmetics can't claim to treat/cure conditions; no personal-attribute angles ("your acne"). Merchant Center misrepresentation and product disapprovals block Shopping.
- Q4/peak: plan budget ramps, promotions, and shipping cut-offs; adjust smart bidding with seasonality adjustments for short promos.
- UK/EU: consent mode v2 and a consent banner are required for personalised ads/remarketing; without them, conversion data and audiences collapse. Server-side tagging/CAPI recommended.

## B2B / SaaS
- Real outcome: SQL/opportunity/pipeline value. Import CRM stages offline (HubSpot/Salesforce) and use value rules (demo < SQL < won).
- LinkedIn usually first for job-title/company-size targeting (flag as outside plugin). Google Search for high intent; competitor brand terms and comparison landing pages ("X vs Y", "alternative to X"); Meta mostly retargeting.
- Demo forms: qualifying fields (company size, role); avoid free-email-only leads; long conversion windows (60-90 days).
- Sales cycle: show pipeline expectations at 30/60/90 days, not just leads. Seasonality: India FY-end (Jan-Mar budgets), annual planning cycles.

## Real estate
- Real outcome: site visit → booking. Compare channels on cost per site visit.
- Meta: higher-intent forms with budget/config/timeline/loan questions; conversion leads via CAPI with CRM stages. Google: project, micro-market and configuration keywords; competitor projects.
- Portals (99acres, MagicBricks, Housing.com; Bayut/Property Finder in UAE) and channel partners are major lead sources.
- Compliance: RERA number on ads in India; housing special ad category for US/Canada/Europe audiences (see policy-watch.md). No guaranteed appreciation/returns.
- NRI: see scope-and-channels.md §4.

## Education / admissions
- Real outcome: completed application → admission/enrolment (fee paid).
- Seasonality: plan by admission cycle (awareness before exams/results, peak during application windows, retargeting near deadlines). Budget pacing toward deadlines.
- Audience: students may be minors — target parents (and students 18+); avoid targeting under-18s with interest/behaviour data.
- Claims: placement %, rankings and accreditations must be verifiable and current; never "100% placement" or "#1" unless provably true.
- Untrackable application portals: track the last controllable step (form start/redirect click), UTMs, and reconcile with admissions data weekly.

## Apps
- Real outcome: paying user / subscriber / retained user — not installs. Cheap installs with no trials = wrong optimisation.
- Must-do: connect an MMP or Firebase to Meta and Google (SDK events: trial_start, purchase, subscription); Google App campaigns optimising for in-app actions (tCPA/tROAS); Meta app promotion optimising for app events/value; iOS SKAdNetwork/AEM limits. Apple Search Ads as an off-plugin channel.
- Health/wellness apps: no targeting by health condition; no "cure" claims; mental-health claims need care.

## Finance / lending / insurance / fintech
- Real outcome: approved, disbursed (or funded) customers with acceptable risk — not applications.
- Google: financial services verification required in many countries including India; personal loan ads must meet country rules (India: lender or RBI-regulated partner disclosed; APR, fees and repayment terms disclosed; app-store declarations for loan apps). Account suspension history: never open a new account to get around a suspension (circumvention policy) — appeal or fix.
- Meta: Financial products and services special ad category is required for US/Canada/EU audiences; elsewhere follow policy (no targeting by financial vulnerability). No "guaranteed approval", "no credit check", or misleading "0% interest" claims.
- India RBI digital-lending norms: key fact statement, disclosure of regulated entity, no misleading claims — verify live.

## Recruitment / hiring
- Real outcome: qualified applicant → hire. Platform leads without licence/eligibility checks are junk; add knock-out questions.
- Meta employment special ad category: required for US/Canada/Europe audiences (no age/gender targeting, minimum ~15-mile/25 km radius, no lookalikes). Google: no targeting by age, gender, parental or marital status for employment ads in the US/Canada. Never discriminate by age/gender/etc. anywhere, even where not technically required.
- External ATS domains: use UTMs and track apply-click + ATS confirmation if possible; reconcile hires.

## Events / ticketing
- Real outcome: tickets sold (net of refunds) by the date. Plan a countdown flight: announce → early bird → sustain → last-chance ramp; use lifetime budgets or scheduled budget changes. Stop or switch to day-of/next-event messaging after the date.
- Ticketing platforms often block ad tags: use their pixel integrations if offered, UTMs, promo codes per channel.
- Alcohol: 18+/21+ by country, no targeting minors or minor-centric segments; no "unlimited drinking" or irresponsible consumption messaging.

## Launches / awareness (when awareness IS the right goal)
- Right when: new brand/category, distribution-led (retail/offline sales), no measurable online conversion, or demand creation before a sales push. Optimise to reach, ThruPlay/video views, ad recall lift; YouTube reach/video, Meta reach & frequency; frequency caps (2-3/week per platform), CPM-based planning.
- Measure with brand lift studies, search-volume lift (Google Trends/brand queries), and sales/distribution data — not clicks.
- Store-locator clicks are a weak proxy; don't make them the main objective for a mass launch.
- Age-restricted products (energy drinks, alcohol, gambling): 18+ targeting and creative not appealing to minors.

## Franchise / multi-location
- Separate objectives: consumer campaigns per location (location-level budgets, radius per outlet) vs franchise-investor leads (different audience, longer cycle, disclosure rules; no earnings guarantees).
- Governance: brand-bidding rules for franchisees (avoid bidding against head office), GBP verification and de-duplication for every location, shared negative lists, consistent naming.

## Nonprofits
- Google Ad Grants: $10k/month in-kind, Search only; requires conversion tracking, ≥5% account CTR, keyword quality rules (no single-word keywords except allowed, quality score ≥3), max conversions bidding to exceed $2 bids — rebuild compliant structure if suspended. Paid Google/Meta for scale.
- India FCRA: foreign contributions need FCRA registration — donations from Indian-citizen NRIs are generally treated differently from foreign nationals/OCI holders; get legal confirmation before targeting donors abroad.
- Imagery of children: dignity, guardian consent, no identifiable details without consent.

## Gulf (UAE / KSA)
- Arabic + English creatives (separate ads, not mixed), culturally appropriate imagery (modest dress, no alcohol for most categories), Ramadan timing (behaviour shifts to evenings/late night, plan seasonal creative), weekends (UAE Sat-Sun; KSA Fri-Sat).
- Only advertise in markets where the business is licensed and can deliver (e.g. KSA requires local registration for many services).
- Check current UAE advertising/influencer permit rules live.

## Solar / energy (incl. Australia)
- Real outcome: qualified homeowner site assessment → install. Exclude renters with qualifying questions; "free solar" or misleading rebate claims breach consumer law (e.g. ACCC); accreditation (e.g. CEC in Australia) as trust signal.

## v0.5 additions

### D2C break-even (replaces ad-hoc economics)
- Break-even CPA = AOV x gross margin. Break-even ROAS = 1 / gross margin (so 70% margin ≈ 1.4). State this first.
- Add shipping, COD fees and RTO losses only if the client supplied them; otherwise list them as "ask" items and show the base figure plainly. Never invent costs; a labelled assumption goes in a separate line and the confidence factor "cost evidence" is capped at 50.
- Existing audiences: when the IG/FB/site/email pool is large enough (Meta custom audience ≥1,000 matched), plan a separate retargeting/existing-customer campaign at 10-20% of budget, and use customer lists as exclusions (new-customer acquisition) and lookalike seeds. Creative refresh: 2-3 new concepts every 2-3 weeks; target ≥8 active concepts for D2C at ₹1,500+/day.
- Shopping/Merchant Center: use custom labels by margin tier (hero, standard, clearance), supply GTIN or declare identifier_exists correctly, start with Standard Shopping when margin segmentation matters; PMax once ≥30 conversions/month.
- Consent-gated tracking (UK/EEA): Consent Mode v2 with a working CMP is a launch blocker; until verified, tracking is capped at "Configured, firing unverified".

### Health, wellness and apps
- Meta has removed detailed targeting on health conditions; Google bans personalised-ad targeting on health. State this in the plan. Use broad / Advantage+ audiences with proxy interests (sleep, yoga, meditation, wellness) and creative that speaks to the product, not the viewer's condition.
- Health-related lower-funnel events (sign-ups to a condition programme, appointments) may be restricted from being sent to Meta. Cap the tracking factor at 60 when only restricted events exist, and optimise on a non-sensitive event (install, trial start).
- Apps: SKAN / AdAttributionKit for iOS, Android install referrers, per-OS campaigns; optimise on the deepest event that occurs within about 3 days and yields ≥50/week.

### Lending / credit
- Treat the financial-products declaration (India) and the Meta credit special ad category (US/CA/EU audiences) as always to state. "Not required" is valid only for audiences outside those regions, and the plan still says "verify live".
- Disbursal lag of days: primary event = KYC-complete or application-complete (≥50/week); disbursal comes back as a value/secondary signal.

### Recruitment, education, B2B
- Search-led plans list 5-10 keyword themes per funded Search campaign plus a mandatory negatives list (recruitment: CNA/LPN/student/free/jobs-for-others; education: free/scholarship/govt exam).
- Capacity sizing: check recruiter/counsellor/sales headcount against forecast leads per day; if leads exceed capacity, cap spend rather than burn leads.
- Admissions: add capitation-fee and admission-law checks to policy; no seat or placement guarantee claims.
- B2B: break-even from ACV x win rate x margin; day-14 checks include "meetings booked", not just form fills.

### Food and bakery, vanity goals
- Food/bakery: transaction usually via WhatsApp or aggregator; real outcome = paid orders; optimise for conversations then orders; local radius with "living in or recently in"; aggregators (Swiggy/Zomato) are a deferred/other channel, not a Meta destination.
- Vanity goals (followers, likes): decline as the goal, translate to the business outcome, and offer a capped (≤10-15%) engagement campaign as a support, with the ₹ stated.
- No website: Google Search first only if people search the intent; otherwise Meta + WhatsApp, with a Google Business Profile as the free "other channel".
