# Tracking audit

Goal: know whether the platforms can see conversions. If they can't, smart bidding is blind and the plan must route conversions somewhere the platform can count (WhatsApp conversations, instant forms, lead form assets, calls) until tracking is fixed.

**Core rule: never report a tag as "Not found" from one method alone.** Browsers with ad blockers or privacy extensions silently stop analytics and pixel requests, and tags loaded through Google Tag Manager don't appear in raw HTML. Run the methods in order and combine them.

## Method 1: page source (quick, incomplete)
Fetch the landing page HTML and look for:
| Signal | What to search for |
|---|---|
| Meta Pixel | `fbq(`, `connect.facebook.net/en_US/fbevents.js`, `facebook.com/tr?id=` |
| Google tag / GA4 | `gtag(`, `googletagmanager.com/gtag/js?id=G-` |
| Google Ads tag | `AW-` IDs inside gtag config, `googleadservices.com` |
| Google Tag Manager | `googletagmanager.com/gtm.js?id=GTM-` |
| Consent mode / banner | `gtag('consent'`, cookie banner scripts (Cookiebot, OneTrust, CookieYes, etc.) |
| Server-side / CAPI hints | Platform plugins (e.g. WordPress "PixelYourSite", Shopify native Meta channel), a first-party tagging subdomain |

If a GTM container ID is found, Method 2 is mandatory.

## Method 2: GTM container inspection (blocker-proof)
Fetch the container script with the web fetch tool: `https://www.googletagmanager.com/gtm.js?id=GTM-XXXXXXX` (also try `&l=dataLayer`). The shell is usually blocked from this host; use the web fetch tool. Ask it to list:
- GA4 measurement IDs (`G-…`) and tag types (`__googtag`, `__gaawe` = GA4 event)
- Google Ads IDs (`AW-…`), conversion labels, remarketing (`__awct`, `__sp`)
- Meta Pixel (custom HTML containing `fbq`, `fbevents.js`) or a Meta template
- Other vendors (LinkedIn, Clarity, Hotjar, TikTok)
- Event/trigger names (form_submit, generate_lead, click on wa.me / tel:)

This shows what is **configured**, independent of any browser. It cannot prove tags fire; combine with Method 3.
For a Google tag loaded directly, the same works for `https://www.googletagmanager.com/gtag/js?id=G-XXXX` or `AW-XXXX`.

## Method 3: browser network requests (shows firing, but blocker-sensitive)
If a browser tool is available:
1. **Blocker check first.** After the page loads, read network requests and look for:
   - `chrome-extension://…` requests whose path names an analytics or ads script (e.g. `google-analytics_analytics.js`, `googletagmanager_gtm.js`, `fbevents`): a content blocker is replacing tracking scripts with stubs.
   - Tracking requests with status `(failed)`, `blocked`, `net::ERR_BLOCKED_BY_CLIENT`, or stuck on `pending`.
   - A GTM script returned 200 but `window.google_tag_manager` has no keys for that container, or `window.dataLayer` holds only the `gtm.js` event: GTM was neutralised.
   - Run in the page: `({fbq: typeof fbq, gtag: typeof gtag, gtm: Object.keys(window.google_tag_manager||{}), dl: (window.dataLayer||[]).length})`.
   If any signal appears, set **blocker_detected = true** and state it in the audit.
2. Filter network requests for `facebook.com/tr`, `google-analytics.com/g/collect`, `region1.google-analytics.com`, `googleadservices`, `googlesyndication`, `doubleclick`.
3. Trigger a harmless interaction (click a WhatsApp/call button; do NOT submit any form with data) and check for event hits.
4. If blocker_detected and another browser is available (e.g. the built-in browser, a separate profile), repeat there. Otherwise rely on Method 2 for configuration and ask the user to confirm firing.
Never log in, accept non-essential cookies, or submit forms.

## Method 4: ask
If still unknown, ask the user (or their developer) to check with GTM Preview / Tag Assistant / Meta Pixel Helper / Events Manager test events:
- "Is a Meta Pixel installed? Which events (Lead, Contact, Purchase)? Is Conversions API set up?"
- "Is there a Google Ads conversion action? Is GA4 linked to Google Ads? Enhanced conversions on?"
- "Do form submissions go to a thank-you page or fire an event?"

## Status vocabulary (use exactly these)
| Status | Meaning |
|---|---|
| Verified firing | Seen in network requests (no blocker), or confirmed by the user via Tag Assistant / Events Manager |
| Configured, firing unverified | Found in the GTM container or page source, but not seen firing (blocker present or no event triggered) |
| Configured, not firing | Found in configuration; seen not firing in a clean, blocker-free browser |
| Not found | Absent from page source AND GTM container AND network (blocker-free), or the user confirms it's absent |
| Unknown | Methods inconclusive; say which check would settle it |

## Output
A table: tool / status / methods used / blocker_detected (Y/N) / impact on plan / fix. Under the table, one line if blocker_detected: "An ad-blocking extension was active in the audit browser; firing could not be verified, and configuration was read from the GTM container instead."
Typical fixes to recommend:
- Install Meta Pixel + Conversions API; track Lead/Contact on form success, Contact on WhatsApp/call clicks.
- Google tag with a Google Ads conversion on form success; enhanced conversions for leads; call conversions from ads and website.
- Consent mode v2 where EEA/UK users are targeted.
- A distinct thank-you URL or a success event for every form.

Tracking status feeds the "Tracking" factor in confidence-rubric.md. "Configured, firing unverified" scores 5, not 0.

## v0.5 additions
- Extra statuses: **Events exist, not linked** (events fire but are not connected to the ad account/campaign goal) and **Consent-gated** (fires only after consent; unverified until the CMP is checked).
- Score tracking twice when it is a fixable blocker: **now** and **after the fix**. Headline the post-fix score only as "if the blocker is fixed before launch".
- WhatsApp-native with manual tally: the native conversation count is valid for optimisation (counts as "Configured"), but outcome tracking is manual; score the tracking factor 5-7 (no separate cap) once orders are logged against campaign codes; if no tally exists, the "not trackable" cap of 60 applies.
- If the ATS or checkout cannot be tagged: use offline conversion import (Google) / Conversions API (Meta) from the CRM, or a cross-domain GTM fix; state which.

## v0.5.2 additions
- Extra statuses: **Thank-you-only pixel on an external domain** (the pixel sees only the final page; upstream steps are invisible) and **Wrong trigger / duplicate primary** (counts inflate; treat as broken, fix before scaling).
- Tracking factor definitions: click-to-WhatsApp with native conversation count = "Configured" (see v0.5 WhatsApp rule); no website + manual tally = 5-6 of 10; "event verified, CRM unlinked" = 8 of 10 for the event and the real-outcome part scored 5-7.
