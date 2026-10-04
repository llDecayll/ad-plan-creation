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

## v0.5.1 additions

### FMCG / beverages / offline products
- Real outcome = incremental units sold through (rate of sale, repeat), not clicks. Platforms can't see it: set up matched-city sell-out lift, brand lift, and brand-search trend as the read, and state it plainly.
- Awareness (reach and frequency) is the right objective for distribution-led launches; locator clicks are a diagnostic, capped at ~5% of spend.
- Run ads only where stock is live; pause by city on stock-out. Quick-commerce in-app ads are an "other channel" to price.
- Age-restricted (energy drinks, alcohol): 18+ only, Audience Network off, adult cast, verify creator audience age; caffeine and health-claim rules live-checked.
- Tracking for awareness is scored on whether the lift read is set up, not on pixel events (see confidence-rubric v0.5.1).

### Events with third-party ticketing
- If tickets sell on Eventfinda/BookMyShow/etc.: send ads straight to the ticket URL, use per-channel promo codes and UTMs, import GA4 purchase to Google only if the platform allows tags; otherwise reconcile weekly from the sales export.
- Hard-dated: back-load spend to match the sales curve (last 3 weeks often 50-65% of sales), keep a reserve of 5-10% for the final push, and phase budget changes ≤20% every 3-4 days.
- Reconcile pace-implied and bottom-up forecasts; if they differ, say which one the plan is built on and price the gap under Deferred.
- Hard + soft locations (city core vs regional) need separate ad sets.

### Services in the Gulf with local-language demand
- If a meaningful share of enquiries is Arabic but the team can't reply in Arabic, park Arabic ads until cover exists (budget parked, not rerouted) and list the trigger.

## v0.5.2 additions
- **Search plans (every funded or deferred Search campaign):** list 5-10 keyword themes in phrase/exact intent sets plus a vertical negatives list (solar: DIY, rebate application, jobs, renters; recruitment: CNA/LPN/student; education: free/scholarship/govt exam). Negatives belong in the setup, not only under Risks. When CPCs are known and employment/education Search is cheaper per qualified outcome, weight Search up.
- **D2C creative volume:** at ₹1,500+/day plan ≥8 active concepts and refresh 2-3 every 2-3 weeks or when frequency > 3; this is exempt from the five-prompts-per-answer word cap (launch-time brief).
- **Brand Search:** when Shopping/PMax is live and brand search demand exists, include brand Search at 3-5% of Search spend by default; defer only if no brand demand.
- **Hyperlocal (single-neighbourhood) businesses:** state audience size and frequency risk; widen radius if too small.
- **Minors as the end-user (education, kids):** target parents; 18+ minimum on Meta; YouTube 25+; no minor-centric creative.
- **Suspended or restricted ad account:** appeal with evidence; never open a new account to bypass; parked budget stays parked (not rerouted) until the client approves a plan.
- **Local awareness asks (billboard-style reach):** cap at 10-15% as a supported campaign, or decline as the goal; never the lead objective.
- **Health vertical confidence:** apply about -5 on the tracking factor when only restricted lower-funnel events can be sent to the platform.
- **Credit / lending / employment / housing:** always state the special-ad-category or financial-products declaration and its targeting limits, then "verify live"; "not required, do not opt in" is only for other verticals.

## v0.5.3 additions (Round 2 fixes)

### Regulated consumables (energy drinks, alcohol, supplements)
- Minimum audience age 18+ everywhere; 21+ where law sets it (US; check India state rules and NZ/AU codes live). Never target minors or minor-centric creative (13+ gamers, school students). Adult gamers and 18+ students are fine.
- Alcohol: no "unlimited", "bottomless", "drink all you can", intoxication or performance claims; responsible-drinking line on every creative; Audience Network off; expect slower ad review, so submit early.
- Energy drinks: carry the pack disclaimer ("not recommended for children, pregnant or lactating women") on every creative; no health or performance claims; check FSSAI/ASCI (India) live.
- Launches with sell-in only: phase **launch burst (first 2 weeks, ~50-60% of reach budget)** then **sustain**, and hold back a 10-15% **winners reserve** released at day 14 to the best-performing channel and creative.
- Reach saturation: a single brand with a tiny follower base cannot absorb unlimited reach at stable CPM; check that daily reach ÷ addressable adult population in the cities stays under ~1.5% and say what happens if CPM climbs.
- Awareness creative spec: 6s bumper, 15s and 30s cuts, 9:16 and 1:1, brand in the first 2 seconds, sound-off readable, partnership (creator) ads on Meta.
- Objective changes (e.g. "make it a conversion campaign"): name who signs off (CEO/CMO) and the measurement that replaces clicks.

### Franchise / multi-location networks
- Two goals (consumer sign-ups and franchisee leads): consumer is primary, franchise capped at 15-25%; named sign-off.
- Franchisee ad accounts: franchise agreement should bar brand-term bidding against head office; monitor with Auction Insights; shared negative keyword list; head-office sets brand terms, franchisees run only non-brand local.
- Fix Google Business Profiles first (verify, de-duplicate, link all locations in a location group); gate PMax store-visit goals and location assets on that fix. GBP-first sequencing.
- Provide a franchisee creative kit (approved templates, claims list, Partnership Ads from head-office page) rather than 22 separate pages.
- Pass a unit/gym ID from the router into GA4 and the CRM; reconcile paid members from each POS weekly (manual tally until integrated).
- Pilot cluster: 30/60/90 plan starting with 8-10 gyms (mix of best, average and worst), then scale per catchment once cost per member is known.
- Earnings guarantees ("₹8L/month assured") are banned; use "investment ₹X, typical payback is not guaranteed" disclosures. Franchise investment ads: state the disclosure and "verify live".

### Nonprofits, donations and Ad Grants (extra)
- Foreign donors need FCRA registration or a registered partner entity; without it, plan India-only and defer diaspora; Indian-citizen NRIs still need counsel's confirmation.
- Timing: 80G/tax-saving push Jan-Mar; giving festivals (Daan Utsav early Oct, Giving Tuesday, festival seasons); year-end.
- Google Ad Grants: about USD 10,000/month in-kind credit, text Search only, needs ≥5% account CTR, multi-word keywords, 2+ ad groups, sitelinks, no single-word generic terms; keep it a separate ₹0 budget. After suspension, rebuild structure and appeal; never open a second account.
- Meta optimisation for donations: if donations are < 50/week, optimise Purchase/Donate with CAPI where affordable at 3× CPR learning-limited; use InitiateCheckout only as the labelled fallback.
- Creative: never named or identifiable children, never claims such as "starving"; consented, anonymised or composite stories with verified figures.

### Travel / treks / tours
- Seasonality: bookings lead the season by 2-3 months; bank budget for peaks only with client approval and say what off-peak loses.
- Check the deposit unit (per booking vs per person) and whether margin is before or after ad spend.
- Strong channel history (CRM cost per deposit) outranks intent order: follow it. Brand Search 5-10% of Search and holdout test if GA4 over-credits brand.
- WhatsApp: automation (auto-reply, qualification, away message) and lead scoring when volume exceeds counsellor capacity.
- Optimise the deposit event (Purchase via CAPI) when ≥50/week; else Lead plus a qualified-lead offline event.
- New-manager hypotheses ("Search is intent, Meta is likes"): frame it as a testable hypothesis with a holdout, not as a loss.

### UAE home services (Ramadan, Arabic)
- Ramadan/Eid and end-of-tenancy peaks: ramp 3-4 weeks before; AC demand ramps April-May.
- Arabic demand: if the team cannot answer in Arabic, plan Arabic ads only with Arabic WhatsApp templates and a named handler; otherwise defer with ₹/AED needed.
- Modest imagery; no swimwear/body-focused creative; tie Google location assets to the GBP.
- Scope: say whether "Abu Dhabi" means the city or the whole emirate (Al Ain); hard-exclude emirates without teams.

### Events with a hard date (extra)
- Derive paid share: tickets still needed − expected email/organic/partner tickets (use last year's share). Allowable CPA = price × margin; if margin unknown, use a labelled 50% and say so.
- Countdown and genuine-scarcity copy only (real early-bird dates, capacity); ramp spend in the last 3 weeks in steps ≤20% per 3 days or state the exception.
