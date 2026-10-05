---
name: ad-results-review
description: Reviews real Meta Ads or Google Ads results against the plan's predictions and turns them into lessons. Use when the user shares campaign screenshots, CSV exports or typed numbers and asks "how is the campaign doing", "review these ad results", "what should we change", "compare with the plan", or wants to update the ad learnings ledger. Compares predicted vs actual, explains the gaps, recommends the next changes, and proposes ledger entries for approval.
---

# Ad Results Review (learning loop)

For ongoing monitoring with alerts, outlook scenarios and change prompts use `${CLAUDE_PLUGIN_ROOT}/skills/ad-monitor/SKILL.md`; this skill is for the ledger-focused predicted-vs-actual review.

**First read `${CLAUDE_PLUGIN_ROOT}/references/guardrails.md` and follow it.** No Iugale Workspace (read-only only if the user explicitly asks to read a named item there; never write), no other Iugale skills, no ad-account access, no individual lead data.

## Inputs
- The original plan (attached, or earlier in the conversation). If absent, ask for it or for the key predictions (cost per result range, results/week, confidence).
- Results: campaign/ad set/ad-level export (CSV preferred) or screenshots of Ads Manager / Google Ads, with the date range.
- Optional: outcome counts per campaign from the CRM (leads, qualified, visits/appointments, closed, revenue).
- Optional: the learnings ledger file (`${CLAUDE_PLUGIN_ROOT}/references/learnings-ledger.md` explains it).

If a file has individual lead details, stop and ask for an aggregate version.
If reading screenshots, restate the key numbers read and ask the user to confirm before analysing.

## Steps
1. **Context check**: how many days live, learning status, any edits made (they reset learning). Under ~3 days or still learning: give a delivery/health read only, not verdicts.
2. **Predicted vs actual table**: metric | predicted range | actual | within/above/below. Metrics: spend, impressions, CPM, CTR, results, cost per result, frequency (Meta); clicks, CPC, CTR, conversion rate, impression share lost (Google); plus cost per qualified lead and cost per closed job where outcome counts exist.
3. **Diagnose gaps** with the funnel: delivery (CPM/impression share) → attention (CTR/hook rate) → action (conversion rate/conversation start) → quality (qualified %) → close rate. Name the weakest stage and evidence.
4. **Creative read**: which angle/creative wins on cost per result AND quality; fatigue signals (frequency >3-4/week, rising CPM, falling CTR).
5. **Recommendations**: max 3-5, ordered by impact, each with expected effect and whether it resets learning. Prefer duplicating to test over editing winners. Never recommend changes the user would need to make inside the Workspace.
6. **Re-score** the plan's confidence with real data (cost evidence factor rises with own data).
7. **Proposed ledger entries** in the ledger format. Ask the user to approve. On approval, update their ledger file (create it if none) and send it back. Mark lessons seen 3+ times across clients as "Pattern".
8. **Next data request**: what to send next and when (e.g. "day 14: same export + qualified and visit counts by campaign").

## Output
Short summary in chat (verdict, weakest stage, top 3 actions, updated confidence). If the user wants a document, re-render the plan's HTML journey board with an added "Results" section tab (predicted vs actual table, diagnosis, actions) and updated confidence scores; Word only on request. Updated ledger file sent only after approval.
