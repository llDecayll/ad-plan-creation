---
name: ad-monitor
description: Watches running campaigns by reading the exports the user shares (Meta, Google, LinkedIn, X) against the plan's targets and alert rules, then says how each campaign could go and writes ready-to-paste change prompts. Use when the user shares campaign data or screenshots and asks "how are the campaigns doing", "keep an eye on this", "what should I change", "is this campaign on track", "alert me if something is off", or sends a weekly export. Reads the plan, the data and the user's own monitor brief, runs scripts/analyze_export.py, adds judgement, and updates the plan. Never connects to an ad account.
---

# Ad Monitor (keep an eye on every campaign)

**First read `${CLAUDE_PLUGIN_ROOT}/references/guardrails.md` and follow it.** No Iugale Workspace, no other Iugale skills, no ad-account access (you only read files the user attaches), aggregate numbers only (refuse files with names, emails or phone numbers).

Be honest about "always": you cannot watch an account between conversations. You watch what is shared, on a cadence, and you can offer a recurring reminder that asks the user for the next export.

## Getting the data
If no export is attached, use `${CLAUDE_PLUGIN_ROOT}/skills/ad-data-pull/SKILL.md`: either read the account in the user's browser in read-only mode (desktop, only when the user has allowed it in this conversation) or tell the user which export to send (`${CLAUDE_PLUGIN_ROOT}/references/meta-export-guide.md`).

## Inputs
- The plan JSON (flights, targets, `monitor` rules per flow). If none, ask for it or build the rules from the key predictions.
- The export(s): CSV/XLSX or screenshots (restate the numbers you read and ask the user to confirm), with the date range.
- Optional: outcome counts per campaign from the CRM (aggregate), the learnings ledger, the user's monitor brief (`${CLAUDE_PLUGIN_ROOT}/references/monitor-brief-template.md`). Rules the user explains in words become `monitor` thresholds.

## Steps
Follow `${CLAUDE_PLUGIN_ROOT}/references/monitoring-playbook.md`:
1. Turn the user's brief into rules (the brief outranks plan defaults) and run `python3 ${CLAUDE_PLUGIN_ROOT}/scripts/analyze_export.py <export.csv> --plan <plan.json> [--rules brief.json] [--edit DATE="what changed"]` (convert XLSX to CSV first; add `--creatives` when ad-set/ad data exists; add every edit date the user mentions or the Activity history shows). Fix any "no rule" or "refused" message first. If the export lacks a daily column, ad-set level or a location column the brief needs, ask for it.
1b. For a quick read run `--briefing` (the five daily questions); use `${CLAUDE_PLUGIN_ROOT}/references/pixel-capi-checklist.md` to read tracking health from Events Manager (read only).
2. Add judgement the script cannot: seasonality, recent edits, tracking, stock/capacity, creative uploads, competitors.
3. Diagnose by funnel stage (delivery → attention → action → quality → close).
4. For each campaign give **three outlooks** (if nothing changes, if the fix works, if it worsens) with assumptions and the date a kill rule would trigger.
5. Write at most five **change prompts**, ranked by impact: where (campaign > ad set > ad), what exactly, expected effect, whether it resets learning, rollback or next-check date. One structural change per campaign per week; duplicate-and-test over editing winners.
6. Cross-channel read (Meta, Google, LinkedIn, X, website): cost per real outcome, overlap and frequency, brand-search lift. Re-split budget only per budget-allocation.md.
7. Update the plan: write a delta (forecasts, confidence, `flight`, `monitor`, and a `Results` section) and apply it with `${CLAUDE_PLUGIN_ROOT}/scripts/merge_plan.py`, then re-render with `render_plan.py` (monitoring-playbook.md step 8). Propose ledger entries for approval.
8. Hand off to `${CLAUDE_PLUGIN_ROOT}/skills/ad-next-moves/SKILL.md` when the user wants new campaigns, ad sets or formats; hand off to `ad-results-review` for ledger-only reviews.

## Output
Chat: one verdict colour per campaign, weakest stage, the three outlooks, the change prompts, and the date and data for the next check. Never change, pause or publish anything, even with read-only browser access: the output is instructions for a human. New creative needs go to ChatGPT through `${CLAUDE_PLUGIN_ROOT}/references/chatgpt-image-handoff.md` (write the image prompts) and come back through `ad-creative-review`.
