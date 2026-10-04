# Meta playbook: front end → back end

Source: Iugale's "Meta Ads Explained: Front End vs Back End" guide (Oct 2026), restructured as decision rules, plus 2025-26 platform changes. Menu labels change often; the logic changes slowly. Verify labels live when precision matters.

## 1. Three layers
| Layer | Question | Holds |
|---|---|---|
| Campaign | Why? | Objective, buying type, special ad category, campaign budget, bid strategy |
| Ad set | Who, where, when? | Conversion location, performance goal, audience, placements, schedule, spend limits |
| Ad | What do they see? | Identity (Page + Instagram), media, primary text, headline, CTA, WhatsApp greeting |
Rules:
- The objective decides every option below it. Awareness ad sets only offer reach/impression goals — a classic mistake when enquiries are wanted. Always confirm the objective in the breadcrumb.
- Meta learns per ad set. Splitting a small budget across many ad sets starves each.
- Once targeting is sensible, creative is the biggest lever.

## 2. What happens behind the scenes
1. Publish → review (usually hours, sometimes 24h+).
2. Active → learning phase: volatile, often pricier.
3. A person opens the app → Meta collects all eligible ad sets for that slot (location, age, placements, schedule, exclusions).
4. Auction: **Total value = Bid × Estimated action rate + Ad quality.** Highest total value wins, not highest bid.
5. Prediction model estimates this person's likelihood of the performance-goal action.
6. Impression charged (usually per 1,000 impressions). Daily budget can flex ~25% above average on good days (up to 1.75× on a single day), balanced across the week (7× daily).
7. Action recorded and fed back to the model.
8. Reporting attributed and refreshed; numbers can lag and shift.
Implication: a sharper creative and clearer offer raise estimated action rate and quality, so a lower bid can win. Creative quality directly lowers cost per result.

## 3. Learning phase
- ~50 optimisation events per ad set within ~7 days to exit.
- Resets: budget change > ~20%, new audience, new creative, long pause, goal change.
- "Learning limited": widen audience, raise budget, merge ad sets, or choose a higher-volume event.
- Make fewer, larger decisions. Don't edit winners; duplicate to test.

## 4. Objectives
| Objective | Optimises for | Goals available | Use when |
|---|---|---|---|
| Awareness | Reach / recall | Reach, impressions, ad recall lift, ThruPlay, 2-sec views | New brand, launch, local recall; not for enquiries |
| Traffic | Clicks / landing page views | Link clicks, LPV, daily unique reach | Content, blog, app store visits |
| Engagement | Interactions | Post engagement, conversations, video views, Page likes, event responses | Social proof, followers, low-commitment messages |
| Leads | Contact details / conversations | Leads, conversations, conversion leads, calls, higher-intent leads | Quotes, bookings, enquiries, sign-ups |
| App promotion | Installs / in-app events | Installs, app events, value | Apps |
| Sales | Purchases / value | Conversions, value, catalogue sales, messaging purchases | E-commerce, paid bookings online |
10-second rule: know us → Awareness; visit → Traffic; react/message lightly → Engagement; raise a hand → Leads; install → App; pay online → Sales.

## 5. Leads: conversion locations
| Location | Experience | Back end | Best when | Watch out |
|---|---|---|---|---|
| Website | Landing page form/call | Needs Pixel or CAPI; optimises for Lead/Contact/Submit | Strong page + verified tracking | Blind without tracking; slow pages kill results |
| Instant form | In-app form, pre-filled | Leads Center / CRM sync; leads or higher-intent leads | Fast volume, low friction, no website needed | Low quality unless higher-intent + qualifying questions |
| Messenger | Chat with greeting | Counts conversation on first message | Facebook-active audiences | Lower usage than WhatsApp in India; needs fast replies |
| Instagram DM | DM thread | Same as Messenger | Visual, younger audiences | Replies must be quick |
| WhatsApp | Opens WhatsApp with pre-filled message | Counts conversation started; goals: conversations, conversations with replies | India and markets where WhatsApp dominates | Someone must answer within minutes; number linked to Page/BM |
| Calls | Call button | Optimise for calls; business-hours option | Urgent / home services | Mobile only; missed calls waste spend |
| Combos | Multiple paths | Advantage+ leads can test which works | Maximise lead count across channels | Harder to attribute |

Performance goal for messaging ad sets:
- Start: **Maximise number of conversations** (highest volume, lowest cost).
- After ~50+ conversations, if quality is poor: test **conversations with replies** in a duplicate ad set.
- With CRM + Conversions API: **conversion leads / qualified events** — best quality, needs setup.
- Never use link clicks or impressions for lead generation.

## 6. Formats
| Format | Use for | Example (home services) |
|---|---|---|
| Single image (1:1/4:5 + 9:16) | Simple offer, proof, price | Before/after wall + "Free site visit" |
| Single video (9:16, ≤15s strong default) | Story, demo, transformation; captions essential | 12-second room time-lapse |
| Carousel (2-10 cards) | Multiple services or steps | Interior / Exterior / Waterproofing / Texture / Wood polish |
| Collection / Instant Experience | Browsing a range | Gallery of finished projects |
| Slideshow | Low bandwidth | 5 photos → light video |
| Advantage+ / dynamic creative | Finding the winning message | 3 images × 3 headlines × 2 texts |
| Catalogue ads | Retail/e-com with feed + pixel | Not for services |
| Partnership ads | Creator credibility | Decor creator shows a makeover |
| Boosted post | Quick social proof | Boost a happy-customer reel |
| Lead ad / click-to-message | Any format + form or WhatsApp button | "Hi, I'd like a free quote for my home in Bangalore" |
Ad elements: identity (Page + Instagram — link Instagram), primary text (offer in first line), headline (5-8 words), CTA, WhatsApp greeting + quick replies, multi-advertiser ads toggle, Advantage+ enhancements (review; switch off anything that alters brand or claims).

## 7. Placements
Advantage+ placements by default: more inventory, cheaper, faster learning. Manual only with a reason (e.g. Audience Network producing junk leads, only 9:16 assets available). Supply 1:1/4:5 and 9:16, or use placement asset customisation; otherwise Meta crops/pads. Brand-safety controls under "Show more options".

## 8. Audiences
| Option | Hard limit or suggestion |
|---|---|
| Locations | Hard limit (even with Advantage+) |
| Location type (living in / recently in / travelling) | Hard limit |
| "Reach more people likely to respond" (location expansion) | Expands beyond location — untick for hard boundary |
| Minimum age 18+ | Hard; age range otherwise a suggestion under Advantage+ unless restricted in controls |
| Gender | Suggestion under Advantage+ |
| Languages | Hard (only if different from area default) |
| Detailed targeting | Suggestion under Advantage+; many interests removed/consolidated (latest Jan 2026); exclusions removed |
| Custom audiences | Include = suggestion; exclude = strict |
| Lookalikes | Suggestion under Advantage+ |
| Original audience options | Strict — needed for true retargeting-only |
Multiple location pins: merged into one area, overlaps counted once, gaps excluded. Many small circles shrink the pool and slow learning; prefer one city/radius unless the business truly serves only specific areas.

## 9. Budget and bidding
- Campaign budget (Advantage campaign budget / CBO): default. Ad set budgets (ABO): to guarantee spend on a specific audience.
- Daily budget: average; up to ~1.75× on a day; weekly cap 7×. Lifetime budget: fixed-length promos; needed for ad scheduling.
- Bid strategies: Highest volume (start) · Cost per result goal (known stable CPL; too low = underdelivery) · ROAS goal (sales with value) · Bid cap (advanced; can stop delivery).
- Standard delivery (default). Accelerated only for time-critical events.
- Guidance: daily budget per ad set ≥ 7 × cost per result (≈50 events/week); see references/budget-allocation.md. Example: WhatsApp conversation ~₹60-120 → ₹1,000/day ≈ 8-16/day ≈ 56-112/week, enough to learn; ₹200/day ≈ 2-3/day, too little.

## 10. Advantage+ automation
| Type | Automates | Notes |
|---|---|---|
| Advantage+ leads campaign | Audience, placements, budget; can test channels | Location controls stay strict |
| Advantage+ sales campaign | Audience, creative, placements | Replaced Advantage+ shopping |
| Advantage+ app campaign | Installs/in-app events | Replaced app campaigns |
| Advantage+ audience | Audience expansion | Location + min age stay strict |
| Advantage+ placements | Placements | Manual only with reason |
| Advantage+ creative | Enhancements, variations, music | Review previews |
| Advantage campaign budget | Budget across ad sets | = CBO |
Turn automation off when: a strict list audience is required (retargeting only), legal/brand/capacity needs exact audience, a controlled single-variable test, or auto-creative changes claims/visuals.

## 11. After launch
| Metric | Read | Act |
|---|---|---|
| Results / cost per result | vs target | Don't judge in first 3-5 days |
| Frequency | >3-4/week with rising cost | Creative fatigue → refresh |
| Link CTR | <~0.8-1% | Weak creative or offer |
| CPM | High | Competitive audience or weak quality |
| Quality/engagement/conversion rankings | Below average | Improve creative/relevance |
| Lead quality (CRM) | Visits/jobs per lead | The real success measure |
Routine: Days 1-3 hands off · Days 4-7 pause clear losers · Week 2 add 2-3 new creatives (one new angle each) · Weeks 3-4 test one variable in a duplicate · Monthly lead-quality review.
Common mistakes: wrong objective, budget too low, over-narrow targeting, daily tinkering, slow WhatsApp replies, weak creative/no offer, ignoring India investment declaration, judging by cost per message not lead quality.

## 12. Pre-launch checklist
- Objective correct (breadcrumb checked)
- Conversion location and the right number/page linked
- Performance goal matches the plan
- Budget and bid strategy set; passes budget-allocation.md §1
- Location type and expansion per hard/soft boundary
- Age / Advantage+ audience / placements per plan
- Special ad category and India investment declaration answered correctly
- Creative in 4:5/1:1 and 9:16; offer clear; CTA correct
- WhatsApp greeting, quick replies, campaign code; named person replying fast
- URL parameters set (website campaigns)
- Previewed on Feed, Reels, Stories

## v0.5.3 additions
- Deposit/donation/booking events under 50/week: prefer Purchase (or Donate) with CAPI feedback at the learning-limited tier over defaulting to Lead or InitiateCheckout; use the proxy only as a labelled fallback.
- Partnership (creator) ads for awareness and franchise/branch networks; head-office page lends ads to local units.
- Click-to-WhatsApp: first-message campaign code, away message, automation when volume exceeds capacity.

## v0.5.5 additions
- Event/donation plans: upload the owned email/donor list as a Custom Audience (exclude buyers from prospecting).
- High-consideration sales: Click-to-WhatsApp option with CAPI lead marking.
