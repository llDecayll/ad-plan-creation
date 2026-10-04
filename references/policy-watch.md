# Policy and platform watch

The platforms change monthly. Each run, do a quick live search ("Meta ads policy update <month year>", "Google Ads policy update <month year>", plus the client's category) and note anything new in the plan with the date checked. The list below is the known baseline as of 2026-10-04.

## Platform changes to respect (baseline)
**Meta**
- Advantage+ audience is the default for most objectives; age (above minimum), gender, detailed targeting and custom/lookalike audiences are treated as suggestions the system can expand beyond. Location and minimum age remain hard limits.
- Detailed-targeting exclusions were removed (2025) and many interest options were consolidated or removed (latest wave effective 15 January 2026). Do not build plans on narrow interests; ad sets using removed options stop delivering.
- True retargeting-only audiences require turning Advantage+ audience off (original audience options).
- Advantage+ campaign types (sales, app, leads) automate audience, placements and budget. Advantage+ shopping and app campaigns were replaced by Advantage+ sales/app.
- Meta's retrieval system groups visually similar ads; variety in creative concept (not just headline swaps) matters for delivery.
- Facebook video feeds placement was deprecated; ads in WhatsApp Status are available in many markets.

**Google**
- AI Max for Search is a feature set on Search campaigns (not a separate campaign type). Dynamic Search Ads, auto-created assets and campaign-level broad match settings auto-upgraded to AI Max from September 2026. Watch the search terms report closely; add negatives.
- Performance Max now has channel-level reporting, brand exclusions and negative keywords.
- Demand Gen has replaced older video action/Discovery campaigns for most video and visual-feed performance goals (YouTube incl. Shorts, Discover, Gmail).
- Ads can appear in AI Overviews from Search, Shopping and PMax campaigns.
- Responsive search ads: up to 15 headlines, 4 descriptions.

## Category restrictions

### Meta special ad categories: decide by audience country
Source: Meta Marketing API documentation on special ad categories (checked 2026-10-04). Re-check live each run; Meta has expanded these before.

**Step 1: Is the ad about a special-category topic?**
| Category | Covers | Not covered (usually) |
|---|---|---|
| Housing | Listings for sale or rent of homes/apartments, home insurance, mortgages, home repairs, home equity/appraisal | Agricultural land, commercial land, plots without a home, sourcing sellers for a marketplace (grey area: treat as possibly housing if the ad mentions homes, farmhouses or residential plots) |
| Employment | Job offers, internships, certification programmes, job boards | Training courses not tied to jobs |
| Financial products and services (credit) | Credit cards, loans, mortgages, insurance, investments, securities | Ads that only mention prices or free listings |
| Social issues, elections or politics | Political or social-issue advocacy | — |

**Step 2: Where are the people the ad reaches?**
| Audience location | Housing / Employment / Credit category |
|---|---|
| United States (required since Dec 2019) | **Required.** Restricted targeting applies. |
| Canada (required since Dec 2020) | **Required.** |
| Europe (required since Dec 2021) | **Required.** Includes UK clients' audiences per Meta's European scope; verify. |
| Rest of world (incl. India, UAE, Australia, New Zealand) | **Not required.** The advertiser may opt in. Recommend NOT opting in unless Ads Manager forces it, because the restrictions remove useful controls. |
| Mixed (e.g. India + US NRIs) | The required rules apply to the whole campaign. Split into separate campaigns by region so only the US/EU campaign carries restrictions. |

Social issues/elections/politics: authorisation and a disclaimer are required in most countries, including India.

**Step 3: If required, the plan must assume these restrictions.**
- Age fixed at 18-65+; all genders.
- Location: minimum ~15-mile (25 km) radius; no postcode, neighbourhood or exclusion targeting.
- No lookalikes or saved audiences; custom audiences and Advantage+ audience only.
- Detailed targeting limited to an approved list.

**Step 4: Write it in the plan**
In "Policy & risks": category (or "none"), the audience countries, required / not required / optional, the decision, and "checked live <date>". If the topic is a grey area, say what to do if Ads Manager prompts for the category anyway (accept it; confirm the plan still works under Step 3 restrictions).

Other Meta notes: real estate listings for homes → housing (required only in US/Canada/Europe). Loans, credit, insurance, investments → financial products and services.
- **India: securities and investments declaration** in Meta ads setup. Farmland/real estate "investment" messaging (e.g. Agrovest-type clients) may trigger it; answer accurately and avoid return promises.
- **Health (both platforms):** no claims of guaranteed results, no before/after that implies a body ideal on Meta, no targeting/asserting personal health conditions ("Do you have diabetes?"). Prescription drugs restricted. Google requires certification for some health categories.
- **Google financial services verification** required in many countries for financial services advertisers, including India.
- **Google Local Services / home services** may require advertiser verification in some markets.

## Data and privacy
- India DPDP Act: lead forms should state the purpose of data collection and link a privacy policy; collect only what's needed; offer a way to withdraw consent.
- UK/EEA: consent mode v2 for Google, cookie consent before pixels fire.

## How to report
In the plan's "Policy & risks" section: each relevant item, whether it applies, what to do, and "checked live on <date>" or "baseline from plugin".

### Google personalised-ads restrictions (housing, employment, credit)
For ads in these categories shown to users in the US and Canada, Google does not allow targeting by gender, age, parental status, marital status or ZIP/postal code. Similar sensitivity rules apply elsewhere; never use these to exclude people from housing, jobs or credit in any country.

## Client asks to rework or decline
When a client asks for something that breaks platform policy, law or basic ethics, the plan must say so plainly, decline that element, and offer the compliant alternative that still serves the goal. Typical cases:
| Client ask | Problem | Compliant alternative |
|---|---|---|
| Target people by health condition / "Are you depressed?" copy | Personal-attributes and health policy; ethics | Broad or interest-in-wellness targeting; benefit-led copy ("Sleep better tonight"); no cure claims |
| "Women 24-40 only" / exclude over-50s for jobs | Employment discrimination; special ad category | All ages/genders; qualify with licence/experience questions |
| Target low credit scores / financially vulnerable | Financial policy; ethics | Target by intent (search), disclose terms |
| "Guaranteed approval", "no credit check", "0% interest" (when not true for all) | Misleading financial claims; regulator rules | Accurate APR/fee disclosure, "check eligibility in 2 minutes" |
| "100% placement", "#1", "clears acne in 7 days", "free solar", "unlimited wine" | Unsubstantiated/misleading or irresponsible claims | Use verifiable facts (e.g. "64% placed in 2025, median ₹X LPA"), or remove |
| Earnings guarantees in franchise/investment ads | Misleading; franchise and securities rules | Disclose investment range and support; no income promises |
| Open a new ad account after suspension | Circumvention — leads to permanent bans | Appeal, fix the cause, wait for reinstatement |
| Show ads for alcohol / energy drinks / gambling to minors or minor-centric segments | Age-restricted policy | 18+/21+ targeting, adult-only creative |
| Identifiable children / patients in imagery without consent | Privacy, dignity, policy | Consented, non-identifying imagery |
| Advertise a service in a country where the business isn't licensed | Legal and policy risk | Defer that market until licensed |
| Culturally inappropriate creative for a market (e.g. swimwear in KSA) | Local norms, rejection risk | Market-appropriate creative per locale |
