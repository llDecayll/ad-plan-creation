# HTML plan output (default)

The default deliverable is one self-contained HTML file: a customer-journey board where each campaign is a horizontal flow (campaign → ad sets → ads, joined by dotted lines), followed by tabbed detail sections. Produce a Word (.docx) or Markdown version only when the user asks for that format.

## How to build it
1. Write the plan as JSON following the schema below (save as `<client>-plan.json` in the working directory).
2. Run: `python3 ${CLAUDE_PLUGIN_ROOT}/scripts/render_plan.py <client>-plan.json <Client>_Ad_Plan.html`
   The script validates the JSON (platforms, stages, 80/20 limits) and injects it into `${CLAUDE_PLUGIN_ROOT}/references/html/plan-template.html`. Fix any errors it prints and re-run.
3. If a browser or screenshot tool is available, open the file and check: no clipped cards, connectors drawn, drawer opens on click.
4. Deliver: if an Artifact/publish tool exists in the session, publish the HTML file as a private page; otherwise send the file. Never publish or push anywhere else (see guardrails.md).

Do not hand-write a different layout. The design lives in the template; if the user wants a different look, edit the template's design tokens (top of its `<style>`) or the template itself.

## Design rules (already built into the template)
- Font: Poppins. Primary colour: Meta blue `#0866FF`. Light theme by default (dark tokens remain in the template, off unless `data-theme` is changed).
- Each flow has a fixed height and scrolls horizontally. A flow grows taller only when it holds 3+ ad sets, so cards never clip.
- Left rail per flow, top to bottom: platform badge (Meta, Google, TikTok, LinkedIn…), journey stage, objective, goal, budget, confidence, status.
- 80/20 rule: card faces are ~80% visual (colour, format glyph, ratio, angle) and ~20% text (a title and one line). All detail sits in the drawer that opens on click.
- Flows are ordered by journey stage (Awareness → Consideration → Conversion → Retention), launch flows before planned ones.

## JSON schema
```json
{
  "meta": {
    "client": "Agrovest",
    "title": "Paid Ads Plan: Landowner Listings",
    "date": "4 Oct 2026",
    "overallConfidence": 58,
    "headline": "One or two sentences: the recommendation.",
    "chips": [["Goal", "Landowner listings"], ["Budget", "₹500/day"], ["Location", "Karnataka · hard"]],
    "footer": "Prepared by … Benchmarks are planning estimates, not facts."
  },
  "stages": ["Awareness", "Consideration", "Conversion", "Retention"],
  "flows": [
    {
      "id": "meta-wa",                       // unique, no spaces
      "platform": "meta",                    // meta | google | youtube | tiktok | linkedin | x | snapchat | pinterest | microsoft | amazon | whatsapp | other
      "channel": "WhatsApp",                 // short qualifier shown in the badge
      "stage": "Conversion",                 // must be one of stages
      "objective": "Leads",
      "goal": "Business result this flow drives (≤ 3 lines).",
      "budget": "₹500/day",
      "confidence": 58,
      "status": "launch",                    // launch | planned
      "statusLabel": "Phase 2",              // shown when status is planned
      "forecast": [["Metric", "Range", "Source/why", 50]],
      "campaign": {
        "name": "AGV | Meta | Leads | WhatsApp | KA",
        "headline": "Leads → WhatsApp",      // big text on the card visual
        "optimise": "Maximise conversations",
        "sub": "Manual Leads · CBO · Highest volume",
        "settings": [["Setting", "Recommendation", "Why", 85]],
        "raise": ["What would raise confidence (+n)"],
        "notes": ["Blockers or notes"]
      },
      "adsets": [
        {
          "name": "Karnataka landowners · broad",   // Google: ad group name
          "confidence": 66,
          "facts": [["💬", "WhatsApp · conversations"], ["📍", "Karnataka · living in"], ["👥", "Advantage+ · 30-65"]],  // max 3
          "settings": [["Setting", "Value", "Why", 70]],
          "scriptTitle": "WhatsApp greeting + first reply",
          "script": "Multi-line text with a Copy button",
          "form": [["Question", "Type / options"]],
          "notes": [],
          "ads": [
            {
              "name": "Broker commission pain",
              "format": "video",             // video | image | carousel | collection | text | search | slideshow | story
              "ratio": "9:16",
              "angle": "Pain / problem",     // ≤ 28 characters
              "color": "linear-gradient(140deg,#E0465B,#7C3AED)",  // optional
              "why": "", "prompt": "", "onscreen": "", "primaryText": "",
              "headline": "", "cta": "", "outcome": "", "policy": ""
            }
          ]
        }
      ]
    }
  ],
  "sections": [
    {"title": "Summary", "blocks": [
      {"type": "list", "title": "Top 3 blockers", "items": ["…"]},
      {"type": "table", "title": "…", "headers": ["Item", "Score", "Reason"], "rows": [["…", "58", "…"]], "scoreCol": 1},
      {"type": "code", "title": "URL parameters", "text": "utm_source=…"},
      {"type": "steps", "items": ["…"]},
      {"type": "text", "text": "…"}
    ]}
  ]
}
```

## What goes where
| Plan content (output-template.md) | HTML location |
|---|---|
| Executive summary, overall score, chips | Header (`meta`) |
| Funnel map / customer journey | Journey strip + one flow per campaign |
| Platform plans (settings) | Campaign and ad-set drawers |
| Creative prompts | Ad cards and their drawers (≥5 per launch campaign) |
| Lead forms, WhatsApp scripts | Ad-set drawer (`script`, `form`) |
| Forecasts | Campaign drawer (`forecast`) |
| Deferred campaigns (₹ needed, client decision), Other channels to consider, Client asks declined + alternatives | `sections` → Summary tab (lists/tables) |
| Test-and-scale table (day 3/7/14/30) | `sections` → Launch tab (table) |
| Confidence summary, research, tracking & URLs, policy, launch timeline | `sections` tabs: Summary · Confidence · Research · Tracking & URLs · Policy · Launch |

Planned or later campaigns are still shown as flows (status `planned`) so the whole customer journey is visible, with their trigger in the campaign settings. A planned flow may have no ad sets yet.

A worked example is in `${CLAUDE_PLUGIN_ROOT}/examples/agrovest-plan.json`.
