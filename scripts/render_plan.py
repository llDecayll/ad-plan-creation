#!/usr/bin/env python3
"""Render an ad plan JSON into the single-file HTML plan.

Usage:
  python3 render_plan.py plan.json output.html [--template path/to/plan-template.html]

The template defaults to ../references/html/plan-template.html relative to this script.
"""
import json
import sys
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
