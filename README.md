# Ad Creation plugin

Senior performance-marketing planner for Meta Ads and Google Ads. Built for Iugale Services Pvt Ltd.

## What it does
Give it a website URL and a business goal. It:
1. Asks only what it can't find: goal, social profiles, location (hard or soft boundary), budget, placement preferences.
2. Researches before recommending: the website and offer, tracking (Pixel, Google tag, GTM, CAPI hints), URL parameters, competitors on Meta Ad Library, Google Ads Transparency Center and the live SERP, seasonality, and current platform policy.
3. Decides like a performance marketer: which platforms, how many campaigns, objectives, conversion locations (website, WhatsApp, instant forms, calls), budget split, bidding, audiences, placements.
4. Writes at least five creative prompts per campaign (image or video, chosen per angle), lead-form questions, WhatsApp scripts and URL parameter strings.
5. Gives every recommendation and forecast a confidence score with what would raise it.
6. Delivers an interactive HTML journey board: one horizontal flow per campaign (campaign → ad sets → ads, joined by dotted lines), platform and objective on the left rail, click any card for full settings and prompts. Word on request.

After launch, share results (exports or screenshots, aggregate only) and it compares predicted vs actual, recommends changes, and proposes lessons for a learnings ledger you keep.

## Skills
| Skill | Use it for |
|---|---|
| ad-strategy | Full plan across Meta and Google (start here) |
| meta-ads-planner | Meta-only plan |
| google-ads-planner | Google-only plan |
| ad-results-review | Reviewing real results and updating the learnings ledger |

Example prompts:
- "Plan ads for paintkraft.in — we want WhatsApp enquiries in Bangalore, ₹1,000/day."
- "Just the Google Ads plan for toothlyfedentalclinic.com."
- "Here's last week's Meta export for Paintkraft — review it against the plan."

## Built-in rules
- Never touches the Iugale Workspace (no reading unless you explicitly ask; never writing or pushing).
- Independent: does not use or change any other Iugale skill.
- No ad-account connection; performance data only from files you attach.
- Aggregate numbers only; no individual lead data.

## Learnings ledger
The plugin can't remember between chats on its own. After each results review it proposes entries for `ad-learnings-ledger.md`; you approve them and keep the file. Attach it to future runs so plans start from Iugale's real results. Lessons seen across 3+ clients should be folded into `references/benchmarks.md` in the next plugin version.

## Keeping it current
Platform rules change monthly. The plugin checks policy and platform changes live on every run; `references/policy-watch.md` and the playbooks hold the baseline (last reviewed 4 Oct 2026). Update them when Meta or Google make major changes.

## Changing the design
The look lives in `references/html/plan-template.html`. Edit the design tokens at the top of its `<style>` block (font, `--brand` colour, `--flow-base-h` flow height, card widths) or the layout itself. Plans keep working as long as the `/*__PLAN_DATA__*/` placeholder stays. The data format is in `references/html-output.md`.

## Changelog
**0.4.0 (4 Oct 2026)**: new rulebooks (budget-allocation, scope-and-channels, vertical-playbooks, quality-gate), confidence caps, expanded India benchmarks, policy decline table, test-and-scale schedule. Blind-test round 1 only partly run; further test/fix rounds planned.

**0.3.1 (4 Oct 2026)**: HTML plan uses the light theme by default, regardless of the viewer's system setting.

**0.3.0 (4 Oct 2026)**
- Default output is now an HTML journey board (Poppins, Meta blue, light theme), built from plan JSON by `scripts/render_plan.py`. Fixed-height flows scroll sideways; the left rail shows platform, stage, objective and goal; cards follow the 80/20 visual rule with details in a click-open drawer; detail tabs for summary, confidence, research, tracking, policy and launch.
- Example plan: `examples/agrovest-plan.json`.

**0.2.0 (4 Oct 2026)**, from the Agrovest test run:
- Tracking audit detects ad-blocking browser extensions and never reports "Not found" from a blocked browser. It reads the Google Tag Manager container directly to see which tags are configured, and uses a fixed status vocabulary (Verified firing / Configured, firing unverified / Configured, not firing / Not found / Unknown).
- New Ad Library search protocol (`references/ad-library-search.md`): query set with exact-phrase and local-language searches, advertiser lookups, a 4-point relevance filter, and a confidence rating for the competitor read.
- Special ad categories are decided by audience country (housing, employment and credit categories are required only in the US, Canada and Europe; optional elsewhere), with split-campaign guidance for mixed audiences.

**0.1.0 (4 Oct 2026)**: first version.
