# Meta Ads export guide: where to get the data and what the plugin needs

For Facebook and Instagram ads (Meta only). Menu names change; verify live. Aggregate numbers only: never export individual leads, names, emails or phone numbers.

## 1. The one export that matters most (do this every check)
**Ads Manager → pick the ad account (top-left) → set the date range (flight start → today) → Campaigns tab → Breakdown → Time → Day → Reports → Export table data → CSV.**

Send me that CSV. With a Day breakdown I can see trends (the last 3 days vs the average), not just totals.

## 2. What information I need (columns)
**Must have:** Day · Campaign name · Delivery (status) · Amount spent · Impressions · Reach · Frequency · Link clicks (or Clicks) · Results · Result type (the optimisation event).
**Strongly recommended:** Cost per result · CPM · CTR (link click-through rate) · CPC (link) · Budget · Ad set name · Ad name · Messaging conversations started (and cost) · Leads (and cost) · Purchases / Purchase ROAS (e-commerce) · Video plays / ThruPlays / 3-second plays (video).
**Useful extras:** Quality ranking, Engagement-rate ranking, Conversion-rate ranking (ad level) · Learning-phase/"Learning limited" status (in Delivery) · Start/end dates · Bid strategy.

## 3. Save the columns once (so exports are identical every time)
Ads Manager → Columns → Customize columns → tick the fields above → Save as preset "Claude Monitor". Use that preset for every export. (In read-only browser mode I only select this preset; I do not build columns.)

## 4. The set of exports (send what applies)
| # | Export | How | Why I need it |
|---|---|---|---|
| A | Campaign level, by Day | Section 1 | Trend, alerts, outlook |
| B | Ad set level, by Day (or totals) | Ad sets tab → same Day breakdown → Export | Which audience wins; learning status |
| C | Ad level, totals (add Day if short) | Ads tab → Export | Which creative wins/fatigues; what to refresh |
| D | By Region (state/city) | Breakdown → Delivery → Region | Checks the hard location rule |
| E | By Placement (Feed, Reels, Stories) | Breakdown → Delivery → Placement | Where the money goes; Reels vs Feed |
| F | By Age and Gender | Breakdown → Delivery → Age / Gender | Audience fit; minors/age rules |
| G | Account history (change log) | Ads Manager → Account overview / Activity history → filter dates → screenshot | Creative swaps, budget edits, pauses (resets learning) |
| H | Events Manager screenshot | Events Manager → Data sources → your pixel/dataset → Overview | Tracking health: Lead/Purchase/Contact events active and not duplicated |
| I | Organic insights (existing channels) | Meta Business Suite → Insights → last 30 days: reach, views, watch time, saves, shares, link clicks; top 5 posts/reels | Which content to boost; trends |
| J | Business outcomes (aggregate) | Your CRM/sheet: per campaign and week: leads, qualified, site visits/appointments, closed, revenue | Real cost per outcome, not platform results |
| K | Delivery screenshot | Ads Manager main table showing Delivery/status | "Learning limited", "In review", "Rejected" |

## 5. Alternative: Meta Business Suite → Ads Reporting
Create report → choose the same metrics and a Day breakdown → Export. Same fields apply.

## 6. Each check, send
- The newest A (and C every week), plus D/E/F when I ask.
- The change log since the last check, plus anything you changed by hand (dates).
- One line per client: "Goal this week", and your monitor brief if rules changed (`monitor-brief-template.md`).

## 7. Privacy rules
No names, phone numbers, emails or lead-form answers. If the file has such columns, I will stop and ask for an aggregate version.

## 8. Read-only browser mode (desktop)
If you allow it (guardrails §3, `browser-readonly-meta.md`), I can open Ads Manager in your browser and do sections 1-4 myself, read only, then run the analysis. You still sign in yourself.
