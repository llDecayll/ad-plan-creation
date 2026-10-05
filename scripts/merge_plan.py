#!/usr/bin/env python3
"""Merge a plan delta (new campaigns, ad sets, updated flights, Results tab) into a plan, then validate it.

Usage:
  python3 merge_plan.py plan.json delta.json merged.json

delta.json (all keys optional):
{
  "addFlows":    [ {full flow object, status "planned" or "launch"} ],
  "addAdsets":   [ {"flowId": "meta-wa", "adset": {adset object}} ],
  "updateFlows": [ {"id": "meta-wa", "set": {"flight": {...}, "monitor": {...}, "confidence": 55}} ],
  "addSections": [ {"title": "Results", "blocks": [ ... ]} ],     # replaces a section with the same title
  "meta":        {"overallConfidence": 55, "headline": "..."}
}
The merged plan is validated with the same rules as render_plan.py; problems are printed and nothing is written.
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from render_plan import validate  # noqa: E402


def main():
    if len(sys.argv) != 4:
        print(__doc__)
        sys.exit(1)
    plan = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    delta = json.loads(Path(sys.argv[2]).read_text(encoding="utf-8"))
    flows = {f["id"]: f for f in plan.get("flows", [])}
    for f in delta.get("addFlows", []):
        if f["id"] in flows:
            print(f"addFlows: id '{f['id']}' already exists; use updateFlows"); sys.exit(2)
        plan["flows"].append(f); flows[f["id"]] = f
    for a in delta.get("addAdsets", []):
        f = flows.get(a["flowId"])
        if not f:
            print(f"addAdsets: flow '{a['flowId']}' not found"); sys.exit(2)
        f.setdefault("adsets", []).append(a["adset"])
    for u in delta.get("updateFlows", []):
        f = flows.get(u["id"])
        if not f:
            print(f"updateFlows: flow '{u['id']}' not found"); sys.exit(2)
        f.update(u["set"])
    for sec in delta.get("addSections", []):
        plan["sections"] = [s for s in plan.get("sections", []) if s.get("title") != sec["title"]] + [sec]
    plan["meta"].update(delta.get("meta", {}))
    errs = validate(plan)
    if errs:
        print("Merged plan has problems; nothing written:\n- " + "\n- ".join(errs)); sys.exit(3)
    Path(sys.argv[3]).write_text(json.dumps(plan, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote {sys.argv[3]} ({len(plan['flows'])} flows)")


if __name__ == "__main__":
    main()
