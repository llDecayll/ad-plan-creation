---
name: ad-next-moves
description: Researches the market, trends (short video, audio, creator/UGC, document and carousel formats) and the client's existing channels (website, Facebook, Instagram, LinkedIn, X) to recommend which campaign to launch next, which ad set or creative to add, and what to retire. Use when the user asks "what should we run next", "add an ad set", "what's trending for this category", "plan the next campaign", "use our social content in ads", "should we add LinkedIn or X", or after an ad-monitor read shows a plateau. Produces ranked next moves with change prompts and planned flows for the board. Never touches ad accounts.
---

# Ad Next Moves (research → next campaign, ad set or creative)

**First read `${CLAUDE_PLUGIN_ROOT}/references/guardrails.md` and follow it.** No Iugale Workspace, no other Iugale skills, no ad-account or social-account logins (public pages and attached aggregate exports only), no personal data.

## Steps
Follow `${CLAUDE_PLUGIN_ROOT}/references/trend-research.md`, with `${CLAUDE_PLUGIN_ROOT}/references/omnipresence.md` and `${CLAUDE_PLUGIN_ROOT}/references/linkedin-x-playbook.md` for channels.
1. **Load context and diagnose the plateau:** current plan, latest ad-monitor read (frequency, CTR trend, click-to-result, qualified %), learnings ledger, the user's attached aggregate exports (post/page insights, site analytics). Decide first whether the problem is creative fatigue, audience saturation or a post-click leak; only then choose moves.
2. **Read the existing channels** (public): website, Facebook, Instagram, LinkedIn page, X profile. List the top organic winners by watch time, saves, shares and link clicks, and the formats and audio styles they use. If pages are blocked or need a login, say so, ask for aggregate exports, and lower confidence (trend-research.md §2b).
3. **Research live:** category and format trends from the last 60-90 days (video, audio, creator/UGC, documents, carousels), competitor ads and long-running ads, demand shifts (Trends, SERP), seasonality and events, platform/policy changes. Record source and date; confirm dates on primary pages and mark undated findings "date unverified" (trend-research.md §2b).
4. **Choose moves** (smallest test first): new creative/format in an existing ad set → new ad set → new campaign (`planned` flow with trigger and flight) → retire/pause → website/tracking change. Check each against budget-allocation.md (learning minimum, test cap), policy-watch.md, claims-and-compliance.md and the channel qualification rules in omnipresence.md.
5. **Brief each move as a change prompt:** where, what exactly, creative direction (format, hook, audio/voice-over, captions, ratio), budget, flight (start, end, endAction), success target, kill rule, confidence with what would raise it.
6. **Plan delta:** write a delta JSON (`addFlows`, `addAdsets`, `updateFlows`, `addSections`) and apply it with `${CLAUDE_PLUGIN_ROOT}/scripts/merge_plan.py plan.json delta.json plan.json`, which validates it; then render the board. Planned flows need budget, a flight trigger and a target with kill rule.
7. **Data request** in the table format of trend-research.md §4 (channel | export | metrics | date range | by when).

## Output
Chat: top 3-5 ranked moves, the research findings that justify them, the plan delta file, the next data request. Do not repeat the whole document.
