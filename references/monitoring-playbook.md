# Monitoring playbook (the "keep an eye" brain)

Used by `skills/ad-monitor`. The plugin cannot watch an ad account (guardrails §3) and cannot run by itself between conversations. It watches **what the user shares**: a campaign export (CSV/XLSX/screenshots), on a cadence. It reads the data, compares it with the plan, says how the campaign could go, and writes change prompts for a human to apply.

## 1. Cadence
- Day 3 health check; day 7 first read; day 14 decision point; day 21; day 30 flight review; then weekly. During festivals or budget changes, check every 2-3 days.
- If the session has a scheduler, offer to create a recurring reminder ("send this week's export for <client>") at the cadence. The reminder asks the user for data; it does not fetch it.

## 2. Inputs per check
1. Plan JSON (flights, targets, `monitor` rules).
2. Export at campaign level, ideally with ad set and ad level and a daily breakdown (the Day column gives trends). CSV is best; screenshots are read, restated and confirmed with the user first.
3. Outcome counts per campaign from CRM/backend (qualified, visits, closed): aggregate only.
4. The user's own monitor brief (`monitor-brief-template.md`): rules they explain in plain words.
No individual lead data. Refuse files with name/email/phone columns.

## 3. Procedure
1. **Turn the user's brief into rules** (monitor-brief-template.md) as a small JSON, e.g. `{"campaigns":[{"id":"meta-wa","cprAlert":240,"cprAlertDays":3,"dailyBudgetMax":800,"allowedLocations":["Karnataka"]}]}`. Keys: cprLow/cprHigh/cprAlert, cprAlertDays (N days above alert = fix), ctrMin, cvrMin, freqMax, dailyBudget, dailyBudgetMax, resultsPerDayMin, allowedLocations. **Precedence: the user's brief outranks the plan's defaults and the escalation ladder; where they conflict, follow the brief and say so.** Save accepted rules into the plan's `monitor` block (via `scripts/merge_plan.py` updateFlows) so the next check uses them.
2. **Run the script** (Meta, Google, LinkedIn and X exports; CSV):
   `python3 ${CLAUDE_PLUGIN_ROOT}/scripts/analyze_export.py <export.csv> --plan <plan.json> [--rules brief.json] [--edit YYYY-MM-DD="creative swap"] [--flow <id>] [--today YYYY-MM-DD]`
   It prints per-campaign metrics, RED/AMBER/GREEN alerts (campaign-to-date **and** last-3-day windows, so a recent collapse is not hidden by the average), evidence, a ready-to-paste change prompt, an "act by" date for RED, before/after reads for each edit you list, and three outlooks to the flight end (days after today through the end date). `--today` defaults to the last date in the export. Daily "Frequency" is averaged over the last 3 days; a column that only rises is treated as cumulative. A location rule needs a region/state column in the export (otherwise it says unverified: ask for the breakdown). "Cost per conversation" = cost per result when conversations are the optimisation event. If a campaign has no rule, build it from the plan targets first.
2. **Read around the script.** It applies numbers; you apply judgement: seasonality (Diwali/Ramadan), edits that reset learning, tracking changes, creative uploads, audience overlap, competitor moves, stock/capacity limits.
3. **Context first:** days live, learning phase, recent edits. Under 3 days: health only.
4. **Funnel diagnosis (weakest stage first):** delivery (CPM, impression share) → attention (CTR, hook rate) → action (click-to-result, conversation start) → quality (qualified %) → close rate. Name the weakest stage with evidence.
5. **Possible ways the campaign could go (always give three):**
   - *If nothing changes* (base): run-rate to flight end.
   - *If the fix works* (optimistic): the named change and its expected effect.
   - *If it worsens* (pessimistic): what drift (fatigue, CPM rise, tracking loss) would do and the date the kill rule would trigger.
   State the assumption for each and what data would tell which path is real.
6. **Decisions, ranked by impact** (max 5): scale, hold, fix creative, fix audience/location, fix landing/handling, restructure, pause. Each decision is a **change prompt**: where to change it (campaign > ad set > ad), exactly what, the expected effect, whether it resets learning, and the rollback/ checkpoint date. Prefer duplicate-and-test over editing winners; never more than one structural change per campaign per week.
7. **Cross-channel read:** compare channels on cost per real outcome; check overlap and frequency; re-split budget only by budget-allocation.md rules (move ≤20% per 3-4 days).
8. **Update the plan:** write a delta (revised forecast rows, confidence, `flight` end/endAction, `monitor` thresholds, and a `Results` section with the predicted-vs-actual table, alerts, outlooks and actions as `table`/`list` blocks) and apply it: `python3 ${CLAUDE_PLUGIN_ROOT}/scripts/merge_plan.py plan.json delta.json plan.json`, then re-render with `render_plan.py`. Propose ledger entries after approval (`learnings-ledger.md`).

## 4. Alert rules (what the script flags)
RECENT variants (CTR_LOW_RECENT, FREQUENCY_HIGH_RECENT) · BRIEF_RULE_CPR_DAYS · BRIEF_RULE_BUDGET_CAP · LOCATION_BREACH / LOCATION_UNVERIFIED · EDIT effect lines. Base alerts: TOO_EARLY / LOW_DATA (no verdict) · NO_RESULTS · CPR_OVER_ALERT · RECENT_CPR_OVER_ALERT (recent days collapse while the average looks fine) · CPR_ABOVE_RANGE · CPR_TOO_GOOD (check quality and double-counting) · CPR_ON_TARGET · CTR_LOW · CTR_FALLING · FREQUENCY_HIGH · CVR_LOW · UNDERSPEND · OVERSPEND · RESULTS_PACE (learning-limited) · IS_LOST_BUDGET (Google) · TREND_WORSENING.

## 5. Escalation ladder (how hard to act)
GREEN: hold or scale ≤20% per 3-4 days. AMBER: one change at a time in a duplicate, 3-4 day read. RED: stop scaling, diagnose tracking/delivery/creative in that order, cut budget 30-50% after 7 more days if unresolved (the script prints the date). Never respond to one bad day. **Cadence:** RED = re-check every 2-3 days until it clears; AMBER = every 3-4 days; GREEN = weekly. A RED overrides the day-14/weekly schedule. The user's brief rules override this ladder where they differ.

## 6. Output
Short chat summary: verdict per campaign (colour), weakest stage, the three scenarios, top actions as change prompts, and the next export date. A Results tab (predicted vs actual, alerts, scenarios, actions) can be added to the HTML board.
