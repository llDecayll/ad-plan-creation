# Google Ads playbook: front end → back end

Baseline as of 2026-10-04. Verify menu labels and recent changes live.

## 1. Structure
| Layer | Holds |
|---|---|
| Account | Auto-tagging, conversion actions and goals, enhanced conversions, consent settings, account-level negatives, brand exclusions |
| Campaign | Type, goal, budget, bidding, networks, locations + location option, languages, schedule, AI Max, brand settings |
| Ad group / asset group | Keywords or audience signals, ads/assets, final URLs |
| Ads & assets | RSAs, images, videos, logos, sitelinks, callouts, call, lead form, location |

## 2. What happens behind the scenes
1. Someone searches (or browses YouTube/Discover/Gmail/sites).
2. Eligible ads collected: keyword/query match (or audience/signals for PMax/Demand Gen), location option, language, schedule, budget.
3. Auction ranks by **Ad Rank** = bid × quality (expected CTR, ad relevance, landing page experience) + asset and context effects. Better quality → lower actual CPC.
4. Smart bidding sets a bid per auction using signals (device, location, time, query, audience, browser, etc.) to hit the goal.
5. Click charged (Search: CPC). Daily budget can overspend up to 2× on a day; monthly spend capped at ~30.4× daily.
6. Conversion recorded via Google tag / enhanced conversions / call tracking / offline import, fed back to bidding.
Implication: tight keyword–ad–landing page relevance lowers costs; tracking quality decides how well smart bidding works.

## 3. Campaign types and when to use
| Type | Inventory | Use for | Needs | Avoid when |
|---|---|---|---|---|
| Search (+ optional AI Max) | Google Search, search partners, AI Overviews | Capturing existing demand; local services; B2B; healthcare | Keywords, RSAs, landing page | Nobody searches for the offer |
| Performance Max | Search, Shopping, YouTube, Display, Discover, Gmail, Maps | Max conversions across channels once tracking is solid | Strong conversion data (~30+/month ideal), assets, audience signals, brand exclusions | Weak tracking, tiny budget, need for keyword control |
| Demand Gen | YouTube (incl. Shorts, in-stream), Discover, Gmail, Display | Visual demand creation, remarketing, mid-funnel; Meta-style creative | Strong images/video, audiences or lookalikes | Expecting instant search-like results |
| Video (YouTube reach/views) | YouTube | Awareness, recall | Video | Lead gen with small budget |
| Display | Google Display Network | Remarketing, cheap reach | Images | Lead gen prospecting (low quality) |
| Shopping | Shopping tab, Search | E-commerce with Merchant Center feed | Feed | Services |
| App | All | App installs | App | — |
| Local Services Ads (where available) | Top of SERP, pay per lead | Home services, some professions | Verification | Unavailable category/market |
Notes: AI Max is a feature set on Search, not a campaign type; DSA auto-upgraded to AI Max from Sept 2026. PMax has channel-level reporting, negative keywords and brand exclusions. Demand Gen supports view-through conversion optimisation for YouTube.

## 4. Search setup rules
- Ad groups: one tight theme each (service × intent). 2-4 to start; 5-20 keywords each.
- Match types: phrase + exact at launch on small budgets; broad match only with smart bidding and good conversion data.
- RSA: 15 headlines (≤30 chars), 4 descriptions (≤90). Include keyword in 2-3 headlines; offer, proof (rating, years, projects), location, CTA, differentiator, price clarity. Pin only what must stay (e.g. compliance).
- Ad strength "Good"+; don't chase "Excellent" at the cost of message.
- Assets: sitelinks, callouts, structured snippets, call, location, image, lead form, price/promotion.
- Landing page: matches the ad group's promise; fast on mobile; one clear CTA; trust signals.
- Search terms report weekly at first; add negatives.

## 5. Locations
- Location option: **Presence** (people in or regularly in) = hard boundary. **Presence or interest** = soft (default).
- Radius targeting around the business works for local services; add excluded locations if needed.

## 6. Conversions
- Primary conversions drive bidding; secondary are observed only.
- Lead gen: form submit (thank-you page or event), calls from ads (min duration, e.g. 60s), website calls (forwarding numbers), lead form asset submits, WhatsApp clicks (usually secondary).
- Enhanced conversions for leads; offline conversion import (qualified/closed from CRM via gclid) to optimise for quality.
- Consent mode v2 for UK/EEA users.

## 7. Bidding progression
| Situation | Strategy |
|---|---|
| No working conversion tracking | Maximise clicks with max CPC cap — temporary only |
| Tracking, <~30 conv/month | Maximise conversions (optionally with target CPA later) |
| ≥30 conv/month, stable | Target CPA near observed CPA |
| Revenue/value tracked | Maximise conversion value / target ROAS |
Avoid changing strategy and budget together; give 1-2 weeks after a change.

## 8. Budget
- Search: aim for ≥10-20 clicks/day per campaign at expected CPC to learn within weeks.
- Smart bidding: ≥ 1 × CPA per day (≈30 conv/month); PMax/Demand Gen ≥ 1.5 × CPA (budget-allocation.md).
- Fewer campaigns with more budget beat many thin ones.

## 9. After launch
| Metric | Read | Act |
|---|---|---|
| Search terms | Irrelevant queries | Add negatives |
| Impression share lost (budget) | High | Budget too low for scope → narrow keywords/locations or raise budget |
| Impression share lost (rank) | High | Improve ad relevance/landing page or bids |
| CTR | Search <~3-5% on non-brand lead gen | Weak ad copy/relevance |
| Conversion rate | Low | Landing page/offer issue |
| Cost per conversion | vs target | Adjust after 2 weeks of data |
| Lead quality (CRM) | — | Import offline conversions |
Routine: Week 1 search terms + negatives; Week 2 ad copy pruning; Weeks 3-4 bidding move if conversion volume allows; monthly lead-quality review.

## 10. Pre-launch checklist
- Auto-tagging on; conversion actions verified (Tag Assistant or test conversion); enhanced conversions on
- Correct campaign type and goal; networks (search partners/display) set deliberately
- Location + location option per hard/soft boundary; exclusions
- Language and schedule
- Keywords and match types; negatives (campaign + account lists)
- RSAs approved; assets added (sitelinks, callouts, call, lead form, image)
- Bid strategy and budget per plan
- Final URL suffix / tracking template set
- Policy: certifications/verification for regulated categories
- Brand exclusions in PMax if running brand Search separately

## v0.5.3 additions
- Add location assets tied to the Google Business Profile and message/WhatsApp assets for local services.
- Use Auction Insights to monitor brand cannibalisation (franchisee or competitor bidding); gate PMax store-visit goals on a fixed, verified GBP.
- Ad Grants: separate ₹0 account/budget, text-only Search, ≥5% CTR, multi-word keywords.

## v0.5.4 additions
- Link all business locations in one GBP location group before adding location assets.
- Add negatives for event and job terms (jobs, volunteer, vendor, free, stall) on event/consumer Search.
- Message/WhatsApp assets for local services.

## v0.5.5 additions
- Location assets require the GBP link (location group verified first).
- Event Search: add event-intent keywords and negatives (see vertical-playbooks.md).

## v0.6.0 additions
- PMax/Demand Gen travel-feed option for hotels; near-me and location assets only after the GBP location-group check; exact/phrase themes sized to the actual keyword volume.
