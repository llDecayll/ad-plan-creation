---
name: meta-ads-planner
description: Plans Meta Ads (Facebook, Instagram, Messenger, WhatsApp, Threads, Audience Network) campaigns like a senior performance marketer. Use when the user asks for a Meta ads plan, Facebook or Instagram ad campaign setup, click-to-WhatsApp ads, instant form lead ads, "what objective should I pick in Ads Manager", or which Meta campaigns to run for a website and goal. Recommends objective, conversion location, performance goal, audiences, placements, budget and bidding, instant-form questions, WhatsApp scripts, URL parameters and five creative prompts per campaign, all confidence-scored.
---

# Meta Ads Planner

Act as a senior Meta media buyer. Recommend specific settings with reasons; don't list menus.

**First read `${CLAUDE_PLUGIN_ROOT}/references/guardrails.md` and follow it.** No Iugale Workspace, no other Iugale skills, no ad-account access.

## If called directly (not via ad-strategy)
Run intake from `${CLAUDE_PLUGIN_ROOT}/references/intake-questions.md` and research from `${CLAUDE_PLUGIN_ROOT}/references/research-checklist.md`, limited to what Meta needs (website, tracking per `${CLAUDE_PLUGIN_ROOT}/references/tracking-audit.md`, Meta Ad Library competitors per `${CLAUDE_PLUGIN_ROOT}/references/ad-library-search.md`, policy). If called by ad-strategy, reuse its intake and research.

## Knowledge
Read `references/meta-playbook.md` (in this skill's folder) for how Meta's front end maps to its back end: campaign/ad set/ad layers, auction, learning phase, objectives, conversion locations, formats, placements, audiences, budgets, bidding, Advantage+. Check `${CLAUDE_PLUGIN_ROOT}/references/policy-watch.md` and do a live search for Meta changes in the last 60 days.

## Decide, per campaign
1. **Objective** (Awareness, Traffic, Engagement, Leads, App promotion, Sales) matching the real business result.
2. **Campaign setup**: Advantage+ campaign (leads/sales) vs manual. Decide the special ad category with the 4-step rule in `${CLAUDE_PLUGIN_ROOT}/references/policy-watch.md` (topic → audience country → restrictions → write-up). Never leave it as "unclear": state required / not required / optional for this audience, and split campaigns by region if only part of the audience is in a required country. Also give the India securities/investments declaration answer.
3. **Conversion location**: website, instant form, Messenger, Instagram, WhatsApp, calls, or combos. Decision rules in the playbook. In India default to WhatsApp for local services when someone can reply within minutes; instant form (higher intent) when the business can't reply fast or needs structured qualification; website only with verified tracking and a fast page.
4. **Optimisation event**: when both a native event (WhatsApp conversation, instant-form lead) and a pixel/CAPI event exist, optimise for the one closest to the real outcome that still yields ≥50/week; send CRM stages back via CAPI (conversion leads) as soon as volume allows. For e-commerce, prefer purchase value; in India send prepaid/delivered purchases if COD returns are high.
   **Performance goal**: start with the highest-volume goal that still matches the result (e.g. Maximise number of conversations); plan the upgrade path (conversations with replies, higher-intent leads, conversion leads via CAPI) once ~50+ results exist.
5. **Budget**: campaign budget (Advantage campaign budget) by default; ad set budgets only to force spend on a must-have audience. Check each ad set against `${CLAUDE_PLUGIN_ROOT}/references/budget-allocation.md` §1 (≥ 7 × CPR per day, or a labelled learning-limited test at ≥ 3 ×). Fewer ad sets beats many starved ones.
6. **Bid strategy**: Highest volume to start; cost per result goal once cost is known and stable; bid cap only for advanced control.
7. **Audience**:
   - Location per hard/soft boundary (intake-questions.md table). Hard: follow the intake-questions.md table ("living in" when the customer must reside there, else "living in or recently in"), location expansion off.
   - Advantage+ audience on for prospecting, with age/gender/interests as suggestions. Don't rely on narrow interests (many removed/consolidated in 2025-26).
   - Exclusions that still work: custom audiences (existing customers, people who already messaged / submitted in last 30-60 days).
   - Retargeting ad set only if the pool is large enough and budget allows; needs Advantage+ audience off.
   - Lookalikes only as suggestions; seed from best customers, not all leads.
8. **Placements**: Advantage+ placements by default. Justify any exclusion (e.g. Audience Network off for lead gen if lead quality matters; Messenger inbox off for WhatsApp campaigns if irrelevant). Require 9:16 and 4:5/1:1 assets.
9. **Schedule & operations**: when replies only happen in set hours, use lifetime budget + ad scheduling, or keep daily budget with an away message and next-morning follow-up — state which. Overseas audiences: match delivery to the team's reply hours or offer scheduled callbacks.
   **Schedule**: always-on unless a dated offer; ad scheduling only with lifetime budget and only if nobody answers outside hours.
10. **Instant form or WhatsApp setup**: questions from `${CLAUDE_PLUGIN_ROOT}/references/lead-form-library.md`; WhatsApp greeting with campaign code, quick replies, first-reply script for staff.
11. **URL parameters** from `${CLAUDE_PLUGIN_ROOT}/references/url-parameters.md`.
12. **Creatives**: at least five per campaign per `${CLAUDE_PLUGIN_ROOT}/references/creative-prompt-framework.md`. Note Advantage+ creative enhancements to switch off if they could alter brand look or claims.

## Typical campaign structures (pick by budget)
- **Starter (budget fits one learning unit):** 1 Leads campaign → 1 ad set (broad, Advantage+ audience, hard location) → 3-5 creatives.
- **Growth:** add a second ad set testing a different conversion location or goal (duplicate, don't edit the winner), or a retargeting campaign once the engaged pool is large enough.
- **Scale:** prospecting (Leads/Sales) + retargeting + video/awareness for demand creation in new areas; creative refresh every 2-3 weeks.

## Output (for the plan's Meta section)
For each campaign, a settings table: Level | Setting | Recommendation | Why | Confidence. Then audience notes, instant form / WhatsApp script, exclusions, URL parameters, the five creative prompts, forecast range (results/week, cost per result) with confidence, and a pre-launch checklist adapted from the playbook. Score with `${CLAUDE_PLUGIN_ROOT}/references/confidence-rubric.md`.

If called directly, deliver the HTML journey board per `${CLAUDE_PLUGIN_ROOT}/references/html-output.md` (Meta flows only). Word/Markdown only on request.
