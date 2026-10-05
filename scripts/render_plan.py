#!/usr/bin/env python3
"""Render an ad plan JSON into the single-file HTML plan.

Usage:
  python3 render_plan.py plan.json output.html [--template path/to/plan-template.html]

The template defaults to ../references/html/plan-template.html relative to this script.
"""
import json
import sys
from datetime import date
from pathlib import Path

PLATFORMS = {"meta", "google", "youtube", "tiktok", "linkedin", "x", "snapchat",
             "pinterest", "microsoft", "amazon", "whatsapp", "other"}
FORMATS = {"video", "image", "carousel", "collection", "text", "search", "slideshow", "story"}


def validate(plan):
    errs = []
    meta = plan.get("meta", {})
    for k in ("client", "title", "overallConfidence"):
        if k not in meta:
            errs.append(f"meta.{k} is missing")
    flows = plan.get("flows", [])
    if not flows:
        errs.append("flows is empty")
    stages = [s.lower() for s in plan.get("stages", ["Awareness", "Consideration", "Conversion", "Retention"])]
    ids = set()
    for i, f in enumerate(flows):
        where = f"flows[{i}]"
        if f.get("id") in ids or not f.get("id"):
            errs.append(f"{where}.id missing or duplicate")
        ids.add(f.get("id"))
        if str(f.get("platform", "")).lower() not in PLATFORMS:
            errs.append(f"{where}.platform '{f.get('platform')}' not one of {sorted(PLATFORMS)}")
        if str(f.get("stage", "")).lower() not in stages:
            errs.append(f"{where}.stage '{f.get('stage')}' not in stages {stages}")
        fl = f.get("flight")
        launch = str(f.get("status", "launch")).lower() == "launch"
        if launch and not fl:
            errs.append(f"{where}.flight is required for launch flows (start, end, days, endAction)")
        if fl:
            try:
                if fl.get("start") and fl.get("end"):
                    d0, d1 = date.fromisoformat(fl["start"]), date.fromisoformat(fl["end"])
                    if d1 < d0:
                        errs.append(f"{where}.flight.end is before start")
                    elif fl.get("days") and (d1 - d0).days + 1 != int(fl["days"]):
                        errs.append(f"{where}.flight.days ({fl['days']}) does not match start/end ({(d1 - d0).days + 1})")
                elif launch:
                    errs.append(f"{where}.flight needs ISO start and end dates (YYYY-MM-DD)")
                elif not fl.get("trigger"):
                    errs.append(f"{where}.flight for a planned flow needs a trigger")
            except ValueError:
                errs.append(f"{where}.flight dates must be ISO YYYY-MM-DD")
            if launch and not fl.get("endAction"):
                errs.append(f"{where}.flight.endAction missing (renew, scale, stop, or review)")
        if not launch:
            if not f.get("budget"):
                errs.append(f"{where}.budget is required for planned flows (amount needed)")
            if not f.get("targets"):
                errs.append(f"{where}.targets is required for planned flows (success target and kill rule)")
        for j, a in enumerate(f.get("adsets", [])):
            for k, ad in enumerate(a.get("ads", [])):
                if ad.get("confidence") is not None and not isinstance(ad["confidence"], (int, float)):
                    errs.append(f"{where}.adsets[{j}].ads[{k}].confidence must be a number")
            if a.get("confidence") is not None and not isinstance(a["confidence"], (int, float)):
                errs.append(f"{where}.adsets[{j}].confidence must be a number")
        if launch and not (f.get("monitor") or {}).get("match"):
            errs.append(f"{where}.monitor.match is required for launch flows (campaign-name text the export will contain)")
        if launch and not f.get("targets"):
            errs.append(f"{where}.targets is required for launch flows (metric, range, alert rule)")
        for j, a in enumerate(f.get("adsets", [])):
            if len(a.get("facts", [])) > 3:
                errs.append(f"{where}.adsets[{j}].facts has more than 3 items (80/20 rule)")
            for k, ad in enumerate(a.get("ads", [])):
                if str(ad.get("format", "image")).lower() not in FORMATS:
                    errs.append(f"{where}.adsets[{j}].ads[{k}].format not one of {sorted(FORMATS)}")
                if len(str(ad.get("angle", ""))) > 28:
                    errs.append(f"{where}.adsets[{j}].ads[{k}].angle longer than 28 chars (card face is visual-first)")
    return errs


def main():
    args = sys.argv[1:]
    if len(args) < 2:
        print(__doc__)
        sys.exit(1)
    src, out = Path(args[0]), Path(args[1])
    tpl = Path(__file__).resolve().parent.parent / "references" / "html" / "plan-template.html"
    if "--template" in args:
        tpl = Path(args[args.index("--template") + 1])
    plan = json.loads(src.read_text(encoding="utf-8"))
    errs = validate(plan)
    if errs:
        print("Plan JSON problems:\n- " + "\n- ".join(errs))
        sys.exit(2)
    data = json.dumps(plan, ensure_ascii=False).replace("</", "<\\/")
    html = tpl.read_text(encoding="utf-8")
    if "/*__PLAN_DATA__*/" not in html:
        print("Template is missing the /*__PLAN_DATA__*/ placeholder")
        sys.exit(3)
    html = html.replace("/*__PLAN_DATA__*/", data)
    title = f"{plan['meta'].get('client', '')} · {plan['meta'].get('title', 'Ad Plan')}".strip(" ·")
    html = html.replace("<title>Ad Plan</title>", f"<title>{title.replace('<', '&lt;')}</title>", 1)
    out.write_text(html, encoding="utf-8")
    print(f"Wrote {out} ({len(html)//1024} KB)")


if __name__ == "__main__":
    main()
