# Pixel + Conversions API checklist (Meta, read-only audit)

Adapted from the approach in the MIT-licensed [meta-ads-kit](https://github.com/TheMattBerman/meta-ads-kit) (© 2026 Matt Berman); rewritten for this plugin's read-only rules. We only **read** Events Manager (browser-readonly-meta.md §4 step 6, or screenshots the user sends) and report what a human should fix. We never change pixels, domains or settings, and never send test events to an account. Targets are planning guidance; verify live.

## 1. Why this matters
Browser-only tracking loses a large share of signal (iOS limits, ad blockers, cookie loss). Meta's optimisation and your cost-per-result read both depend on events being received. Pixel (browser) plus Conversions API (server) running together, with shared event IDs for de-duplication, is the standard setup. Without it, a campaign's real results can look worse (or better) than they are.

## 2. What to read in Events Manager (Data sources → your pixel/dataset → Overview)
| Check | Pass | Warning | Fail |
|---|---|---|---|
| Key event present (Lead / Purchase / Contact / Schedule …) | Received in the last 24h | Received but older than 24h | Never received |
| Browser and server both sending | Both shown for the key event | Browser only | Neither |
| De-duplication | Event IDs match; no doubled counts | Counts look high vs backend | Browser + server counted twice |
| Event Match Quality (key events) | Purchase ≥ 9.3, Lead ≥ 8.0 | Purchase 8.0-9.2, Lead 6.5-7.9 | Purchase < 8.0, Lead < 6.5 |
| Match keys sent (email, phone, name, location, fbp/fbc, IP+user agent) | email + phone + fbc/fbp | email only | none |
| Event volume vs backend | Within ~20% | 20-40% gap | > 40% gap |
| Aggregated Event Measurement / priority events (apps, iOS) | Configured | Partly | Not configured |
Quote EMQ as read from Events Manager; do not estimate it.

## 3. Map findings to the plugin
- Status words: use tracking-audit.md's vocabulary (Verified firing / Configured, firing unverified / Configured, not firing / Not found / Unknown).
- Scoring: pixel only or events not linked → tracking score ≤ 4 and campaign cap 45 (confidence-rubric.md); no pixel or no key event → cap 40; both verified and EMQ in range → tracking 8-9.
- Monitor: if platform results exceed backend by > 20% suspect double counting; if far below, suspect lost signal.

## 4. Fix list for a human (report, do not do)
1. Add or repair the server-side (Conversions API) path for the key event; send the same event ID from browser and server.
2. Pass hashed email and phone where the user has consent; normalise (lowercase, trim) before hashing; never send raw personal data.
3. Pass fbp/fbc and the click ID from the landing page into the form and CRM.
4. Check consent banners and ad blockers are not suppressing the pixel on the landing page.
5. Re-test in Events Manager (Test Events) by the human, then recheck volume vs backend after 3-7 days.
6. Platform gotchas (Shopify checkout, Next.js hydration, WordPress/WooCommerce, GoHighLevel, ClickFunnels): verify live on the platform's own docs.
