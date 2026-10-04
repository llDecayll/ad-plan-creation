# Research checklist

Do all of this before recommending campaigns. Record findings with source and "verified live on <date>" or "from playbook/benchmark".

## 1. Website audit
Fetch the home page and the likely landing page (web fetch first; if the page is JavaScript-rendered or blocked, use the browser).
Note:
- What is sold, to whom, price signals, service area.
- The clearest offer and USP. If none, flag it: weak offer is the most common reason ads fail.
- Conversion points present: contact form, WhatsApp button (wa.me link), click-to-call (tel:), booking widget, cart/checkout.
- Trust signals: reviews, ratings, before/after, certifications, years in business, team photos, guarantees.
- Mobile experience and speed. If possible, run a speed check (e.g. PageSpeed Insights). Slow mobile pages (LCP > 4s) push the plan towards WhatsApp/instant forms/calls.
- Policy-sensitive content: health claims, financial returns, before/after body images, housing, employment, credit (see policy-watch.md).

## 2. Tracking audit
Follow tracking-audit.md, including the ad-blocker check and GTM container inspection. Output a short table: Meta Pixel, Conversions API hint, Google tag / GA4, Google Ads conversion tag, GTM, consent banner, each with a status from the tracking-audit vocabulary, the methods used, and whether a blocker was detected. Never write "Not found" based on a browser that had a blocker active.

## 3. URL parameters
Follow url-parameters.md. Check whether links on the site or the landing page strip query strings or redirect (which can drop gclid/fbclid/UTMs).

## 4. Competitors
Find 3-6 real competitors in the same service and location (search "<service> in <city>", Google Maps results, and the businesses bidding on the main keywords).
For each:
- **Meta Ad Library**: follow `ad-library-search.md` (query set incl. local language, exact-phrase searches, advertiser lookups, and the relevance filter). Never summarise unfiltered keyword results. Record: are they running ads, how many, how long (ads live 30+ days are likely profitable), formats, offer, CTA (WhatsApp, Learn more, Get quote), hook style, language.
- **Google Ads Transparency Center** (adstransparency.google.com): are they advertising, formats, rough recency.
- **Live SERP** for 3-5 main keywords: who appears in ads, their headlines and offers, sitelinks, whether Local Services Ads or map pack dominate.
Summarise: common offers, gaps nobody is claiming, creative styles that look saturated, price positioning.

## 5. Market context
- Seasonality: search trend direction for main keywords (Google Trends if reachable), festivals and seasons in the target region over the next 90 days (e.g. in India: Diwali/wedding season for home services and jewellery, monsoon for waterproofing, academic year for education, financial year-end for B2B and investments).
- Category news that changes demand or messaging.
- Live policy check per policy-watch.md.
- Consumer psychology notes for this audience: main fear, main desire, main objection, decision maker, typical decision time.

## 6. Learnings
If a learnings ledger or past results are attached, read them. Real past results override benchmarks; say which numbers came from where.
