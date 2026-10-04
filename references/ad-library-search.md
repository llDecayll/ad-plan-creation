# Ad Library search protocol

Keyword searches in the Meta Ad Library match loosely: any ad containing one of the words can appear, sorted by impressions. Unfiltered results mix in big unrelated advertisers (e.g. a bank's agriculture blog, a DNA-test ad). Follow this protocol so the competitor picture is accurate.

## 1. Build the query set before searching
Write 4-8 queries, from most to least specific:
| Type | Example (landowner sourcing, Karnataka) |
|---|---|
| Exact phrase of the offer | "sell your land", "sell agricultural land" |
| Local-language phrase | Kannada "ಜಮೀನು ಮಾರಾಟ", Telugu "భూమి అమ్మ", Tamil "நிலம் விற்க", Hindi "ज़मीन बेचें" |
| Audience + location | "land owners Bangalore", "farm land Mysore" |
| Known competitor names | from SERP, Google Maps, Transparency Center, the client |
| Category term (broad, last) | "farmland", "agricultural land" |

## 2. Use the tightest URL settings
`https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=<CC>&q=<query>&search_type=keyword_exact_phrase&media_type=all`
- `search_type=keyword_exact_phrase` for phrases (wrap the phrase in quotes in the q value); `keyword_unordered` only for single-word or local-language queries that return nothing exact.
- `country` = the target country. Set `active_status=active` for what's working now; check `all` only for the client's own history.
- For a named competitor, search by advertiser: open the result whose Page name matches, then use that Page's "See all ads" (view_all_page_id) rather than a keyword search.

## 3. Read results with the page rendered
Ad Library is JavaScript-rendered: use the browser, wait ~3 seconds, then read the page text. Scroll or "See more" once if fewer than ~10 results are visible.

## 4. Relevance filter (apply to every ad before using it)
Keep an ad only if it passes at least 3 of 4:
1. **Same job:** the ad asks the same audience to take the same action (e.g. landowners → sell/list land), not merely the same topic.
2. **Same geography:** the copy, landing page or advertiser is in or targets the client's area or country.
3. **Comparable advertiser:** a business type that competes for the same customer (platform, broker, developer, clinic, agency), not a bank, NGO, government or unrelated brand.
4. **Commercial intent:** has a lead CTA (WhatsApp, Call, Apply now, Get quote, Sign up, Learn more to a lead page).
Discard the rest and note how many were discarded ("~75 results; 9 relevant after filtering").

## 5. Record each relevant ad
| Advertiser | Started running | Days live | Format | Offer / hook | CTA / conversion location | Language | Versions | Relevance score (3/4 or 4/4) |
Ads live 30+ days, or with multiple versions, are the strongest signal that an approach works.

## 6. Cross-check
- Confirm 2-3 key competitors in the Google Ads Transparency Center (search by domain).
- If the client has no ads, say so explicitly (useful: no account history, no creative fatigue).

## 7. Summary for the plan
- Common offers and hooks (what is saturated).
- Gaps nobody claims.
- The dominant conversion location (WhatsApp / form / call) in this niche and region.
- Language mix used by competitors.
- Confidence of the competitor read: high (8+ relevant ads), medium (3-7), low (0-2). This feeds the "Competitor evidence" factor.
