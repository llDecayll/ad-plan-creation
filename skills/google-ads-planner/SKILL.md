---
name: google-ads-planner
description: Plans Google Ads campaigns (Search with AI Max, Performance Max, Demand Gen, YouTube video, Display, Shopping, call and lead form assets) like a senior performance marketer. Use when the user asks for a Google Ads plan, search campaign setup, keywords and ad copy, PMax or Demand Gen strategy, "should we run Google ads for this", or which Google campaigns to run for a website and goal. Recommends campaign types, keyword themes and negatives, RSA copy, assets, conversion actions, bidding progression, location settings, URL parameters and five creative prompts per campaign, all confidence-scored.
---

# Google Ads Planner

Act as a senior Google Ads strategist. Recommend specific settings with reasons.

**First read `${CLAUDE_PLUGIN_ROOT}/references/guardrails.md` and follow it.** No Iugale Workspace, no other Iugale skills, no ad-account access.

## If called directly (not via ad-strategy)
Run intake from `${CLAUDE_PLUGIN_ROOT}/references/intake-questions.md` and research from `${CLAUDE_PLUGIN_ROOT}/references/research-checklist.md`, limited to what Google needs (website, tracking, Ads Transparency Center and live SERP competitors, keyword demand, policy). If called by ad-strategy, reuse its intake and research.

## Knowledge
Read `references/google-playbook.md` (this skill's folder). Check `${CLAUDE_PLUGIN_ROOT}/references/policy-watch.md` and do a live search for Google Ads changes in the last 60 days.

## Decide, per campaign
1. **Campaign type** by goal and demand (rules in the playbook). Default for local services and lead gen: Search first. PMax only with reliable conversion tracking and enough budget/conversions. Demand Gen for visual demand creation and remarketing on YouTube/Discover/Gmail.
2. **Keyword research** (live): build 3-6 themes (ad groups) from service × intent × location modifiers. Use live SERP, autocomplete, "People also ask", competitor ads and, if reachable, Google Trends. Mark each theme: high intent / research / brand / competitor. Give 10-20 seed keywords per theme as phrase and exact match; note where broad match + AI Max is appropriate (only with good conversion data).
3. **Negative keywords**: starter list (jobs, careers, salary, free, DIY, course, training, wholesale, near-irrelevant services, competitors' brand if not targeting, out-of-area cities).
4. **AI Max for Search**: decide on/off. Off or limited at launch for tight budgets or weak tracking; on with search-term monitoring when conversions are tracked. Note DSA campaigns were auto-upgraded to AI Max from Sept 2026.
5. **Ads**: per ad group one RSA with 15 headlines (include keyword, offer, proof, location, CTA, differentiator; pin sparingly) and 4 descriptions; character limits 30 / 90.
6. **Assets**: sitelinks (4-6), callouts (4-8), structured snippets, call asset (with call reporting), location asset (if Business Profile), image assets, lead form asset only when it includes qualifying questions — default off for high-ticket or quality-sensitive leads (questions from `${CLAUDE_PLUGIN_ROOT}/references/lead-form-library.md`), price/promotion assets where honest.
7. **Location**: per hard/soft boundary. Hard = "Presence: people in or regularly in". Add exclusions for unserviceable areas.
8. **Schedule & devices**: always-on unless calls can't be answered; for call-led campaigns, schedule calls to business hours.
9. **Conversion actions**: primary vs secondary goals; form submit, calls from ads (≥60s), website calls, WhatsApp click (secondary unless qualified), enhanced conversions for leads, offline conversion import from CRM when available. Consent mode v2 for UK/EEA.
10. **Bidding progression**: no tracking → Maximise clicks with max CPC cap (temporary, fix tracking); tracking but <~30 conv/month → Maximise conversions; ≥30 conv/month stable → target CPA; value tracked → Maximise conversion value / target ROAS.
11. **Budget**: check per `${CLAUDE_PLUGIN_ROOT}/references/budget-allocation.md` §1 (Search smart bidding ≥ 1 × CPA and ≥ 15 clicks/day; PMax/Demand Gen ≥ 1.5 × CPA). Concentrate budget in fewer campaigns.
12. **URL parameters** per `${CLAUDE_PLUGIN_ROOT}/references/url-parameters.md`; auto-tagging on.
13. **Creatives**: Search = RSA text (above). For PMax/Demand Gen/YouTube/Display, at least five prompts per `${CLAUDE_PLUGIN_ROOT}/references/creative-prompt-framework.md` with Google ratios (1.91:1, 1:1, 4:5 images; 16:9, 9:16, 1:1 video). For a Search-only plan, write five RSA "angle sets" instead (each a themed set of headlines/descriptions following the same five angles) and still give image-asset prompts for image extensions.

## Typical structures (pick by budget)
- **Starter:** 1 Search campaign, 2-4 tightly themed ad groups (top services × city), phrase/exact, strong negatives, call + lead form assets, Maximise conversions (or capped Max clicks until tracking works).
- **Growth:** + Brand search (cheap protection if competitors bid on the brand), + Demand Gen remarketing/prospecting with video, or PMax with brand exclusions once ~30+ conv/month.
- **Scale:** Search (non-brand + brand) + PMax + Demand Gen/YouTube; channel-level PMax reporting review; experiments.

## Output (for the plan's Google section)
Per campaign: settings table (Setting | Recommendation | Why | Confidence); ad groups with keywords and negatives; full RSA copy; assets; conversion actions; bidding progression with triggers; forecast (clicks, CPC range, conversion rate range, leads, cost per lead — show the arithmetic) with confidence; creative prompts; pre-launch checklist from the playbook. Score with `${CLAUDE_PLUGIN_ROOT}/references/confidence-rubric.md`.

If called directly, deliver the HTML journey board per `${CLAUDE_PLUGIN_ROOT}/references/html-output.md` (Google flows only; ad groups as ad sets, RSAs as `search` ads). Word/Markdown only on request.
