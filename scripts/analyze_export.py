#!/usr/bin/env python3
"""Read a campaign export (CSV) and compare it with the plan's monitor rules.

Usage:
  python3 analyze_export.py export.csv --plan plan.json [--flow FLOW_ID] [--today YYYY-MM-DD] [--json]
  python3 analyze_export.py export.csv --rules rules.json [--today YYYY-MM-DD] [--json]
  Extra options: --edit 2026-10-20="creative swap" (repeatable: before/after read), and --rules together with --plan
  (your monitor-brief rules are merged over the plan's: brief wins). --today defaults to the last date in the export.
  Brief-rule keys: cprAlertDays (N days above cprAlert = fix), dailyBudgetMax, allowedLocations ["Karnataka"].
  Campaign names match when the rule's match text is inside the export name or the reverse (case-insensitive).
  "Results" = the optimisation event (conversations, leads, purchases): cost per conversation = cost per result.

Works with Meta Ads Manager, Google Ads, LinkedIn Campaign Manager and X Ads CSV exports
(header names are matched by synonyms; extra columns are ignored). Aggregate numbers only:
exports with name/email/phone columns are refused (guardrails.md section 4).

Rules come from plan.flows[].monitor (see references/html-output.md) or a rules.json:
  {"campaigns": [{"id": "meta-wa", "match": "Meta | Leads", "cprLow": 80, "cprHigh": 160,
                  "cprAlert": 240, "ctrMin": 0.8, "freqMax": 3.5, "dailyBudget": 500,
                  "resultsPerDayMin": 2, "start": "2026-10-12", "end": "2026-11-10"}]}
Output: alerts (RED/AMBER/GREEN) with evidence and a ready-to-paste change prompt, plus
three projected scenarios to the end of the flight. This script never touches an ad account.
"""
import csv
import io
import json
import re
import sys
from collections import defaultdict
from datetime import date, datetime, timedelta
from pathlib import Path

SYN = {
    "campaign": ["campaign name", "campaign", "campaign_name"],
    "adset": ["ad set name", "adset name", "ad group", "ad group name", "adgroup", "ad_set_name"],
    "ad": ["ad name", "ad", "creative name", "ad_name"],
    "date": ["day", "date", "reporting starts", "start date", "date range start", "time period"],
    "spend": ["amount spent (inr)", "amount spent", "spend", "cost", "total spent", "billed charge local currency",
              "amount spent (usd)", "amount spent (aed)", "amount spent (gbp)", "amount spent (eur)", "cost (inr)"],
    "impressions": ["impressions", "impr.", "impr"],
    "clicks": ["link clicks", "clicks", "link click", "clicks (all)", "interactions", "outbound clicks"],
    "results": ["results", "conversions", "leads", "one-click leads", "all conv.", "messaging conversations started",
                "conversions (all)", "purchases", "website purchases", "website leads", "link clicks (results)"],
    "reach": ["reach"],
    "frequency": ["frequency"],
    "lost_is_budget": ["search lost top is (budget)", "search lost is (budget)", "search impr. share lost (budget)",
                       "search lost impression share (budget)"],
    "video_views": ["video plays", "thruplays", "video views", "views", "3-second video plays"],
    "qualified": ["qualified leads", "qualified", "qualified enquiries"],
    "location": ["region", "state", "country", "location", "city", "dma region", "geography", "delivery location"],
    "revenue": ["purchase conversion value", "conv. value", "revenue", "conversion value"],
}
FREQ_DAYS = defaultdict(dict)
LOCS = defaultdict(lambda: defaultdict(float))
PII = ["email", "phone", "mobile", "first name", "last name", "full name", "address"]


def norm(h):
    return re.sub(r"\s+", " ", h.strip().lower().lstrip("﻿"))


def num(v):
    if v is None:
        return 0.0
    v = str(v).strip().replace(",", "").replace("%", "")
    v = re.sub(r"[^\d.\-]", "", v)
    try:
        return float(v) if v not in ("", "-", ".") else 0.0
    except ValueError:
        return 0.0


def parse_date(v):
    v = str(v).strip()
    for fmt in ("%Y-%m-%d", "%d/%m/%Y", "%m/%d/%Y", "%d-%m-%Y", "%b %d, %Y", "%d %b %Y"):
        try:
            return datetime.strptime(v, fmt).date()
        except ValueError:
            continue
    return None


def load_csv(path):
    raw = Path(path).read_text(encoding="utf-8-sig", errors="replace")
    lines = raw.splitlines()
    # Google Ads exports start with title lines; find the header line (the one with most commas among first 5)
    start = 0
    for i, ln in enumerate(lines[:6]):
        if sum(1 for k in ("campaign", "impr", "cost", "spend", "amount spent") if k in ln.lower()) >= 2:
            start = i
            break
    text = "\n".join(lines[start:])
    try:
        dialect = csv.Sniffer().sniff(text[:2000], delimiters=",;\t")
    except csv.Error:
        dialect = csv.excel
    rows = list(csv.DictReader(io.StringIO(text), dialect=dialect))
    return rows


def map_columns(headers):
    low = {norm(h): h for h in headers}
    for h in low:
        if any(p == h or h.startswith(p + " ") or h.endswith(" " + p) for p in PII):
            raise SystemExit(f"Refused: column '{low[h]}' looks like personal data. Send a campaign-level export "
                             "(guardrails.md section 4).")
    m = {}
    for key, names in SYN.items():
        for n in names:
            if n in low:
                m[key] = low[n]
                break
    return m


def agg(rows, m, keyfn):
    out = defaultdict(lambda: defaultdict(float))
    days = defaultdict(lambda: defaultdict(lambda: defaultdict(float)))
    FREQ_DAYS.clear()
    LOCS.clear()
    for r in rows:
        k = keyfn(r)
        if not k or str(k).lower().startswith("total"):
            continue
        for f in ("spend", "impressions", "clicks", "results", "reach", "video_views", "qualified", "revenue"):
            if f in m:
                out[k][f] += num(r.get(m[f]))
        if "frequency" in m:
            out[k]["_freq_w"] += num(r.get(m["frequency"])) * max(num(r.get(m.get("impressions", ""))), 1)
            out[k]["_freq_n"] += max(num(r.get(m.get("impressions", ""))), 1)
        if "lost_is_budget" in m:
            out[k]["lost_is_budget"] = max(out[k]["lost_is_budget"], num(r.get(m["lost_is_budget"])))
        if "location" in m and r.get(m["location"], "").strip():
            LOCS[k][r[m["location"]].strip()] += num(r.get(m.get("spend", ""), 0)) or 1
        if "date" in m:
            d = parse_date(r.get(m["date"], ""))
            if d and "frequency" in m:
                FREQ_DAYS[k][d] = num(r.get(m["frequency"]))
            if d:
                for f in ("spend", "impressions", "clicks", "results"):
                    if f in m:
                        days[k][d][f] += num(r.get(m[f]))
    return out, days


def derive(a):
    d = dict(a)
    imp, clk, sp, res = a.get("impressions", 0), a.get("clicks", 0), a.get("spend", 0), a.get("results", 0)
    d["ctr"] = clk / imp * 100 if imp else 0
    d["cpc"] = sp / clk if clk else 0
    d["cpm"] = sp / imp * 1000 if imp else 0
    d["cpr"] = sp / res if res else 0
    d["cvr"] = res / clk * 100 if clk else 0
    d["freq"] = a["_freq_w"] / a["_freq_n"] if a.get("_freq_n") and a.get("_freq_w") else 0
    return d


def window(series, last_n):
    ds = sorted(series)
    cur, prev = ds[-last_n:], ds[-2 * last_n:-last_n]
    tot = lambda sel: {f: sum(series[x][f] for x in sel) for f in ("spend", "impressions", "clicks", "results")}
    return tot(cur), (tot(prev) if prev else None)


def recent_stats(series, n=3):
    if not series or len(series) < n + 2:
        return None
    cur, _ = window(series, n)
    imp, clk, res, sp = cur["impressions"], cur["clicks"], cur["results"], cur["spend"]
    return {"ctr": clk / imp * 100 if imp else 0, "cpr": sp / res if res else None, "results": res, "spend": sp}


def consecutive_days_above(series, limit):
    """Longest current run (ending on the last day) of daily cost per result above limit."""
    run, first = 0, None
    for d in sorted(series, reverse=True):
        r = series[d]
        cpr = r["spend"] / r["results"] if r["results"] else (float("inf") if r["spend"] > 0 else None)
        if cpr is not None and cpr > limit:
            run, first = run + 1, d
        else:
            break
    return run, first


def alerts_for(rule, a, series, today, name=None):
    A = []
    days_live = len(series) if series else None
    start = date.fromisoformat(rule["start"]) if rule.get("start") else None
    if start and today:
        days_live = max(days_live or 0, (today - start).days + 1)
    res, spend = a.get("results", 0), a.get("spend", 0)

    def add(sev, code, evidence, why, prompt):
        A.append({"severity": sev, "code": code, "evidence": evidence, "why": why, "change_prompt": prompt})

    if days_live is not None and days_live < 3:
        add("AMBER", "TOO_EARLY", f"{days_live} day(s) of data",
            "Under 3 days the platform is still learning; verdicts would be noise.",
            "Do not edit anything. Check delivery, approvals and that the tracked event fires; re-send the export on day 3.")
        return A
    if a.get("clicks", 0) < 30 and a.get("impressions", 0) < 3000:
        add("AMBER", "LOW_DATA", f"{int(a.get('clicks', 0))} clicks, {int(a.get('impressions', 0))} impressions",
            "Too little data for a verdict.", "Hold. Re-send the export in 3-4 days.")
        return A

    cpr, ctr, freq, cvr = a["cpr"], a["ctr"], a["freq"], a["cvr"]
    lo, hi, alert = rule.get("cprLow"), rule.get("cprHigh"), rule.get("cprAlert")
    if res == 0 and spend > 0:
        if rule.get("cprAlert") and spend >= rule["cprAlert"]:
            add("RED", "NO_RESULTS", f"spend {spend:,.0f} with 0 results (alert level {rule['cprAlert']:,.0f})",
                "Spend has passed one alert-level cost per result with no result: tracking or offer problem.",
                "Verify the tracked event fires (test conversion) and that the landing page/WhatsApp reply works. "
                "If it fires, duplicate the ad set with a new offer and pause the original after 48 hours.")
    elif cpr:
        if alert and cpr > alert:
            add("RED", "CPR_OVER_ALERT", f"cost per result {cpr:,.0f} vs alert {alert:,.0f}",
                "Cost per result is past the kill/fix line set in the plan.",
                ("Do not raise budget. Diagnose in order: " +
                 ("CTR is low -> new hook/creative in a duplicate ad set. " if ctr and rule.get("ctrMin") and ctr < rule["ctrMin"] else
                  "CTR is fine, so look after the click: landing page speed, form length, WhatsApp first-reply time. ") +
                 "If still above alert after 7 more days, cut budget 30-50%."))
        elif hi and cpr > hi:
            add("AMBER", "CPR_ABOVE_RANGE", f"cost per result {cpr:,.0f} vs forecast range {lo or '-'}-{hi}",
                "Above the forecast range but under the alert line.",
                "Hold budget. Add one new creative angle to the ad set (duplicate, do not edit the winner).")
        elif lo and cpr < lo * 0.7:
            add("AMBER", "CPR_TOO_GOOD", f"cost per result {cpr:,.0f} is far below forecast low {lo}",
                "Suspiciously cheap: often low-quality results or double-counted events.",
                "Check result quality (qualified %) and event de-duplication before scaling.")
        elif hi and cpr <= hi:
            add("GREEN", "CPR_ON_TARGET", f"cost per result {cpr:,.0f} within {lo or '-'}-{hi}",
                "On target.", "Scale +20% every 3-4 days only if frequency and quality hold.")
    rc = recent_stats(series)
    if rc and rule.get("ctrMin") and rc["ctr"] and rc["ctr"] < rule["ctrMin"] and not (ctr < rule["ctrMin"]):
        add("AMBER", "CTR_LOW_RECENT", f"last-3-day CTR {rc['ctr']:.2f}% vs minimum {rule['ctrMin']}% (campaign-to-date {ctr:.2f}% hides it)",
            "Attention has already dropped below the floor.",
            "Brief a new hook in 2-3 variants as new ads in a duplicate ad set before cost per result follows.")
    fd = FREQ_DAYS.get(name)
    if fd and rule.get("freqMax"):
        ds = sorted(fd)
        vals = [fd[d] for d in ds]
        cumulative = len(vals) >= 5 and all(b >= a_ - 1e-9 for a_, b in zip(vals, vals[1:]))
        recent_f = vals[-1] if cumulative else sum(vals[-3:]) / len(vals[-3:])
        if recent_f > rule["freqMax"] and not (freq > rule["freqMax"]):
            add("RED" if recent_f > rule["freqMax"] * 1.15 else "AMBER", "FREQUENCY_HIGH_RECENT",
                f"recent frequency {recent_f:.1f} ({'latest cumulative' if cumulative else 'last-3-day average'}) vs max {rule['freqMax']}",
                "The same people are now seeing the ad too often; the campaign average hides it.",
                "Refresh creative (new angle, not a re-crop) and widen the audience inside the hard boundary; do not raise budget.")
    if rule.get("cprAlertDays") and rule.get("cprAlert") and series:
        run, first = consecutive_days_above(series, rule["cprAlert"])
        if run >= rule["cprAlertDays"]:
            add("RED", "BRIEF_RULE_CPR_DAYS", f"daily cost per result above {rule['cprAlert']:,.0f} for {run} consecutive days (since {first})",
                f"Your rule: {rule['cprAlertDays']}+ days above the alert line means fix. It has triggered.",
                "Fix now (your brief outranks the default ladder): diagnose tracking/delivery, then creative/audience in a duplicate; hold budget.")
    if rule.get("dailyBudgetMax") and series:
        mx = max((v["spend"] for v in series.values()), default=0)
        if mx > rule["dailyBudgetMax"]:
            add("RED", "BRIEF_RULE_BUDGET_CAP", f"a day's spend reached {mx:,.0f} vs cap {rule['dailyBudgetMax']:,.0f}",
                "Your daily budget cap was exceeded.", "Lower the budget setting to the cap and check for auto-scaling or bid changes.")
    locs = LOCS.get(name)
    if rule.get("allowedLocations"):
        if not locs:
            add("AMBER", "LOCATION_UNVERIFIED", "the export has no location column",
                "Your location rule cannot be checked from this file.", "Re-export with a region/state breakdown.")
        else:
            allowed = [x.lower() for x in rule["allowedLocations"]]
            bad = {k: v for k, v in locs.items() if not any(x in k.lower() for x in allowed)}
            if bad:
                add("RED", "LOCATION_BREACH", "delivery outside the allowed area: " + ", ".join(f"{k} ({v:,.0f})" for k, v in bad.items()),
                    "Spend is reaching places outside the hard boundary.",
                    "Switch the location setting to 'living in', turn expansion off and exclude these regions.")
    if rule.get("ctrMin") and ctr and ctr < rule["ctrMin"] and a.get("impressions", 0) >= 3000:
        add("AMBER", "CTR_LOW", f"CTR {ctr:.2f}% vs minimum {rule['ctrMin']}%",
            "The ad is not earning attention; cost per result will drift up.",
            "Brief a new hook (first 2 seconds / first line) in 2-3 variants; add them as new ads in the same ad set.")
    if rule.get("freqMax") and freq and freq > rule["freqMax"]:
        add("AMBER" if freq < rule["freqMax"] * 1.3 else "RED", "FREQUENCY_HIGH",
            f"frequency {freq:.1f} vs max {rule['freqMax']}",
            "The same people are seeing the ad too often: fatigue, rising CPM, falling CTR.",
            "Refresh creative (new angle, not a re-crop) and/or widen the audience; avoid raising budget until frequency falls.")
    if cvr and clk_ok(a) and rule.get("cvrMin") and cvr < rule["cvrMin"]:
        add("AMBER", "CVR_LOW", f"click-to-result {cvr:.1f}% vs minimum {rule['cvrMin']}%",
            "Clicks arrive but do not convert: the problem is after the ad.",
            "Audit landing page load time, form length and first-reply time; compare mobile vs desktop.")
    if rule.get("dailyBudget") and days_live:
        pace = spend / (rule["dailyBudget"] * days_live) if rule["dailyBudget"] * days_live else 0
        if pace < 0.7:
            add("AMBER", "UNDERSPEND", f"spent {pace*100:.0f}% of planned budget",
                "Not spending: learning limited, audience too small, bid cap or ads in review.",
                "Check delivery status and audience size; widen location/audience within the hard boundary; remove any bid cap.")
        elif pace > 1.2:
            add("AMBER", "OVERSPEND", f"spent {pace*100:.0f}% of planned budget",
                "Spending faster than planned.", "Confirm the budget setting; lower it to the planned daily value.")
    if rule.get("resultsPerDayMin") and days_live and res / days_live < rule["resultsPerDayMin"] and days_live >= 7:
        add("AMBER", "RESULTS_PACE", f"{res/days_live:.1f} results/day vs minimum {rule['resultsPerDayMin']}",
            "Volume is below the plan; the platform may be learning-limited (< ~50 results/week).",
            "Consolidate ad sets, or move to a nearer-funnel optimisation event for now.")
    if a.get("lost_is_budget", 0) > 20:
        add("AMBER", "IS_LOST_BUDGET", f"impression share lost to budget {a['lost_is_budget']:.0f}%",
            "Demand exists that the budget cannot serve.", "If cost per result is on target, raise budget 20% or tighten match types.")
    if series and len(series) >= 6:
        cur, prev = window(series, 3)
        if prev and prev["clicks"] and cur["clicks"]:
            c_ctr = cur["clicks"] / max(cur["impressions"], 1) * 100
            p_ctr = prev["clicks"] / max(prev["impressions"], 1) * 100
            c_cpr = cur["spend"] / cur["results"] if cur["results"] else None
            p_cpr = prev["spend"] / prev["results"] if prev["results"] else None
            if c_cpr and alert and c_cpr > alert and not any(x["code"] in ("CPR_OVER_ALERT", "NO_RESULTS") for x in A):
                add("RED", "RECENT_CPR_OVER_ALERT", f"last-3-day cost per result {c_cpr:,.0f} vs alert {alert:,.0f} (campaign-to-date looks fine)",
                    "The average hides a recent collapse; it is already past the kill/fix line.",
                    "Treat as an incident: check approvals/delivery, frequency and tracking first; hold budget; launch a fresh creative in a duplicate ad set now.")
            if c_cpr and p_cpr and c_cpr > p_cpr * 1.25:
                add("AMBER", "TREND_WORSENING", f"last-3-day cost per result {c_cpr:,.0f} vs previous 3 days {p_cpr:,.0f}",
                    "Cost is drifting up: early sign of fatigue or auction pressure (festivals, competitors).",
                    "Compare CPM and frequency this week vs last; if CPM is up, hold; if frequency is up, refresh creative.")
            if p_ctr and c_ctr < p_ctr * 0.75:
                add("AMBER", "CTR_FALLING", f"CTR {c_ctr:.2f}% vs {p_ctr:.2f}% in the previous 3 days",
                    "Attention is falling.", "Queue a fresh creative now, before cost per result moves.")
    if any(x["code"] == "BRIEF_RULE_CPR_DAYS" for x in A):
        dup = [x for x in A if x["code"] in ("RECENT_CPR_OVER_ALERT", "CPR_OVER_ALERT")]
        A = [x for x in A if x not in dup]
        if dup:
            next(x for x in A if x["code"] == "BRIEF_RULE_CPR_DAYS")["evidence"] += " | " + "; ".join(d["evidence"] for d in dup)
    if any(x["severity"] == "RED" for x in A):
        ctx = [x for x in A if x["code"] in ("CPR_ABOVE_RANGE", "TREND_WORSENING", "CPR_ON_TARGET")]
        A = [x for x in A if x not in ctx]
        if ctx:
            first_red = next(x for x in A if x["severity"] == "RED")
            first_red["evidence"] += " | context: " + "; ".join(x["evidence"] for x in ctx if x["code"] != "CPR_ON_TARGET")
        for x in A:
            if x["severity"] == "RED" and today:
                x["act_by"] = (today + timedelta(days=7)).isoformat()
                x["act_by_note"] = "If still RED on this date, cut budget 30-50% (escalation ladder); re-check every 2-3 days until then."
    if not any(x["severity"] in ("RED", "AMBER") for x in A) and not any(x["severity"] == "GREEN" for x in A):
        add("GREEN", "NO_ISSUES", "no rule triggered", "Nothing to change.", "Hold; re-send the export in 3-4 days.")
    return A


def edit_effect(series, edit_date, label):
    ds = sorted(series)
    before = [d for d in ds if d < edit_date][-4:]
    after = [d for d in ds if d >= edit_date]
    if len(before) < 2 or len(after) < 2:
        return {"edit": label, "date": edit_date.isoformat(), "note": "not enough days before/after to read the effect"}
    agg_ = lambda sel: {f: sum(series[x][f] for x in sel) for f in ("spend", "impressions", "clicks", "results")}
    b, a_ = agg_(before), agg_(after)
    f = lambda t: {"ctr": round(t["clicks"] / t["impressions"] * 100, 2) if t["impressions"] else 0,
                   "cpr": round(t["spend"] / t["results"]) if t["results"] else None}
    return {"edit": label, "date": edit_date.isoformat(), "before": f(b), "after": f(a_),
            "note": "an edit resets learning; read at least 3 days before judging"}


def clk_ok(a):
    return a.get("clicks", 0) >= 100


def scenarios(rule, a, series, today):
    if not series or len(series) < 3 or not rule.get("end"):
        return None
    end = date.fromisoformat(rule["end"])
    remaining = (end - (today or max(series))).days  # days after today up to and including the end date
    if remaining <= 0:
        return None
    n = min(7, len(series))
    cur, _ = window(series, n)
    d = max(n, 1)
    spend_d, res_d = cur["spend"] / d, cur["results"] / d
    if not res_d:
        return None
    base_cpr = cur["spend"] / cur["results"]
    out = []
    rc = recent_stats(series)
    recent_cpr = rc["cpr"] if rc and rc["cpr"] else None
    worse = recent_cpr and recent_cpr > base_cpr * 1.25
    base_ref = recent_cpr if worse else base_cpr
    base_note = ("the last 3 days continue (they are >25% worse than the last 7)" if worse else "last 7 days continue unchanged")
    target = rule.get("cprHigh")
    for name, cpr, note in (
        ("Optimistic", (target if target and target < base_ref else base_ref * 0.9),
         "the fix works: cost per result returns to the forecast high end" if target and target < base_ref else "cost per result improves ~10%"),
        ("Base", base_ref, base_note),
        ("Pessimistic", base_ref * 1.25, "fatigue/auction pressure: cost per result drifts ~25% above the base"),
    ):
        spend_total = a.get("spend", 0) + spend_d * remaining
        results_total = a.get("results", 0) + spend_d * remaining / cpr
        out.append({"scenario": name, "assumption": note, "projected_results": round(results_total),
                    "projected_spend": round(spend_total), "projected_cpr": round(cpr)})
    return {"days_remaining": remaining, "note": "days after today through the flight end date", "scenarios": out}


def main():
    args = sys.argv[1:]
    if not args or args[0].startswith("-"):
        print(__doc__)
        sys.exit(1)
    src = args[0]

    def opt(name):
        return args[args.index(name) + 1] if name in args else None

    today = date.fromisoformat(opt("--today")) if opt("--today") else None
    if opt("--plan"):
        plan = json.loads(Path(opt("--plan")).read_text(encoding="utf-8"))
        rules = []
        for f in plan.get("flows", []):
            mon = f.get("monitor")
            if mon and (not opt("--flow") or f["id"] == opt("--flow")):
                r = dict(mon)
                r["id"] = f["id"]
                fl = f.get("flight") or {}
                r.setdefault("start", fl.get("start"))
                r.setdefault("end", fl.get("end"))
                rules.append(r)
    else:
        rules = []
    if opt("--rules"):  # brief rules: standalone, or merged over the plan's monitor rules (brief wins)
        extra = json.loads(Path(opt("--rules")).read_text(encoding="utf-8")).get("campaigns", [])
        for e in extra:
            base = next((r for r in rules if r.get("id") == e.get("id") or (e.get("match") and r.get("match") == e.get("match"))), None)
            if base:
                base.update(e)
            else:
                rules.append(e)
    edits = []
    for i, a_ in enumerate(args):
        if a_ == "--edit" and i + 1 < len(args) and "=" in args[i + 1]:
            dt, lab = args[i + 1].split("=", 1)
            edits.append((date.fromisoformat(dt), lab))
    rows = load_csv(src)
    if not rows:
        raise SystemExit("No rows found in the export.")
    m = map_columns(rows[0].keys())
    if "campaign" not in m:
        raise SystemExit("No campaign-name column found. Send a campaign-level export.")
    key_campaign = lambda r: r.get(m["campaign"], "").strip()
    camp, camp_days = agg(rows, m, key_campaign)
    if today is None:
        all_days = [d for c in camp_days.values() for d in c]
        today = max(all_days) if all_days else None
    report = []
    for name, a in camp.items():
        a = derive(a)
        rule = next((r for r in rules if r.get("match") and (r["match"].lower() in name.lower() or name.lower() in r["match"].lower())), {})
        series = camp_days.get(name)
        item = {"campaign": name, "rule": rule.get("id"), "metrics": {k: round(v, 2) for k, v in a.items()
                                                                       if not k.startswith("_")}}
        item["alerts"] = alerts_for(rule, a, series, today, name) if rule else [
            {"severity": "AMBER", "code": "NO_RULE", "evidence": "no monitor rule matches this campaign name",
             "why": "Cannot judge without the plan's targets.",
             "change_prompt": "Add a monitor block for this campaign to the plan (match, cprLow, cprHigh, cprAlert, ...)."}]
        sc = scenarios(rule, a, series, today) if rule else None
        if sc:
            item["scenarios"] = sc
        if series and edits:
            item["edits"] = [edit_effect(series, d, lab) for d, lab in edits]
        report.append(item)
    if "--json" in args:
        print(json.dumps(report, indent=2, ensure_ascii=False))
        return
    order = {"RED": 0, "AMBER": 1, "GREEN": 2}
    for it in report:
        mt = it["metrics"]
        print(f"\n## {it['campaign']}  (rule: {it['rule'] or 'none'})")
        print(f"spend {mt.get('spend', 0):,.0f} | results {mt.get('results', 0):,.0f} | CPR {mt.get('cpr', 0):,.0f} | "
              f"CTR {mt.get('ctr', 0):.2f}% | CPM {mt.get('cpm', 0):,.0f} | freq {mt.get('freq', 0):.1f}")
        for al in sorted(it["alerts"], key=lambda x: order[x["severity"]]):
            print(f"- [{al['severity']}] {al['code']}: {al['evidence']}\n    why: {al['why']}\n    change prompt: {al['change_prompt']}")
            if al.get("act_by"):
                print(f"    act by: {al['act_by']} ({al['act_by_note']})")
        for e in it.get("edits", []):
            if "before" in e:
                print(f"  Edit '{e['edit']}' on {e['date']}: before CTR {e['before']['ctr']}% / CPR {e['before']['cpr']} -> after CTR {e['after']['ctr']}% / CPR {e['after']['cpr']} ({e['note']})")
            else:
                print(f"  Edit '{e['edit']}' on {e['date']}: {e['note']}")
        sc = it.get("scenarios")
        if sc:
            print(f"  Outlook to flight end ({sc['days_remaining']} days left):")
            for s in sc["scenarios"]:
                print(f"    {s['scenario']}: ~{s['projected_results']} results, ~{s['projected_spend']:,} spend, CPR ~{s['projected_cpr']:,} ({s['assumption']})")


if __name__ == "__main__":
    main()
