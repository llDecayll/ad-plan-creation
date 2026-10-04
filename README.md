# Ad Creation plugin

Senior performance-marketing planner for Meta Ads and Google Ads. Built for Iugale Services Pvt Ltd.

## What it does
Give it a website URL and a business goal. It:
1. Asks only what it can't find: goal, social profiles, location (hard or soft boundary), budget, placement preferences.
2. Researches before recommending: the website and offer, tracking (Pixel, Google tag, GTM, CAPI hints), URL parameters, competitors on Meta Ad Library, Google Ads Transparency Center and the live SERP, seasonality, and current platform policy.
3. Decides like a performance marketer: which platforms, how many campaigns, objectives, conversion locations (website, WhatsApp, instant forms, calls), budget split, bidding, audiences, placements.
4. Writes at least five creative prompts per campaign (image or video, chosen per angle), lead-form questions, WhatsApp scripts and URL parameter strings.
5. Gives every recommendation and forecast a confidence score with what would raise it.
6. Delivers an interactive HTML journey board: one horizontal flow per campaign (campaign → ad sets → ads, joined by dotted lines), platform and objective on the left rail, click any card for full settings and prompts. Word on request.

After launch, share results (exports or screenshots, aggregate only) and it compares predicted vs actual, recommends changes, and proposes lessons for a learnings ledger you keep.

## Skills
| Skill | Use it for |
|---|---|
| ad-strategy | Full plan across Meta and Google (start here) |
| meta-ads-planner | Meta-only plan |
| google-ads-planner | Google-only plan |
| ad-results-review | Reviewing real results and updating the learnings ledger |

Example prompts:
- "Plan ads for paintkraft.in — we want WhatsApp enquiries in Bangalore, ₹1,000/day."
- "Just the Google Ads plan for toothlyfedentalclinic.com."
- "Here's last week's Meta export for Paintkraft — review it against the plan."

## Built-in rules
- Never touches the Iugale Workspace (no reading unless you explicitly ask; never writing or pushing).
- Independent: does not use or change any other Iugale skill.
- No ad-account connection; performance data only from files you attach.
- Aggregate numbers only; no individual lead data.

## Learnings ledger
The plugin can't remember between chats on its own. After each results review it proposes entries for `ad-learnings-ledger.md`; you approve them and keep the file. Attach it to future runs so plans start from Iugale's real results. Lessons seen across 3+ clients should be folded into `references/benchmarks.md` in the next plugin version.

## Keeping it current
Platform rules change monthly. The plugin checks policy and platform changes live on every run; `references/policy-watch.md` and the playbooks hold the baseline (last reviewed 4 Oct 2026). Update them when Meta or Google make major changes.

## Changing the design
The look lives in `references/html/plan-template.html`. Edit the design tokens at the top of its `<style>` block (font, `--brand` colour, `--flow-base-h` flow height, card widths) or the layout itself. Plans keep working as long as the `/*__PLAN_DATA__*/` placeholder stays. The data format is in `references/html-output.md`.

## Continuation plan (for a cloud session)
Status at v0.5.1 (4 Oct 2026): plugin built, rules in. Blind-test scores so far: original regression set 89.8% (v0.4), fresh Set A 89.8% (v0.4). Round-1 runs on v0.5.1 (S1–S5, A1–A6) are done and saved in `dev/evals/runs/r1_*.md` but **not yet graded**. Set B (B1–B3) ran on v0.5 (`v05_B*.md`), ungraded; B4–B6 not run.

**Hard rules (do not change):** never add or push anything to the Iugale Workspace unless Deepak says so; plugin stays independent of other Iugale skills; no ad-account connections (aggregate numbers only, no lead PII); push only to this repo's `main` when asked.

### Steps
1. **Grade Round 1.** Two independent grader agents: one for S1–S5 against `dev/evals/setS_key.md`, one for A1–A6 against `setA_key.md`. Save to `dev/evals/grade_r1_S.md` and `grade_r1_A.md`. Target ≥ 92%.
2. **Fix round 1.** Apply the gaps reported (see "Known open gaps"), bump to 0.5.2, validate (`claude plugin validate .`).
3. **Round 2: Set B.** Run B1–B6 blind with `dev/evals/runner_prompt.txt` (replace `<REPO_ROOT>`; ID, FILE, RUN set per run). Run 3–4 agents at a time. Grade against `setB_key.md`, fix, bump to 0.5.3.
4. **Round 3: fresh Set C.** Have an independent agent write 6 new scenarios and a key (different goals/industries: e.g. SaaS free-trial, restaurant chain, legal/financial advisory, tourism/hospitality, B2B manufacturing export, healthcare multi-clinic). Run blind, grade, fix, bump to 0.6.0. Stop when two consecutive rounds gain < 1 point.
5. **Final.** Update the changelog, regenerate the example plan with `scripts/render_plan.py`, run `claude plugin validate .`, zip (exclude `dev/`), push to `main`, attach `.plugin` and `.zip`.

Estimated time in a cloud session: about 55–60 minutes.

### Known open gaps (from graded runs)
- D2C: break-even rule applied inconsistently (playbook subtracts shipping/RTO; v0.5 says base margin only); Standard Shopping vs PMax overlap; retargeting vs existing-customer cap when pool size unknown; brand Search without data.
- Test cap vs 3× CPR minimum (which wins, what counts as the "total"); learning-limited tier for Google.
- "Capped score widens band" is ambiguous (use one step: ±35% → ±50%).
- Lending/credit: always state the declaration vs "not required, do not opt in" wording; no lending benchmarks; take-up rate anchor; Google suspension process.
- Apps: no Google App campaign section; "events exist, not linked" has no score mapping; iOS SKAN rules; unspent buffer and 7-day trial lag in day-14 gates.
- Diaspora/NRI: scope-and-channels says "living in", policy-watch says interest-based; reconcile to one rule.
- Hard boundary with several pins vs "prefer one radius"; US special categories override hard boundary (15-mile minimum).
- Quality gate: "five creatives per funded campaign" cannot fit a 1,000-word answer cap (the HTML board has no such cap; keep, but let test answers give one line each).
- Recruitment: no lead-form library section (knock-out questions); no US RN benchmark; no ATS-on-external-domain tracking path.
- Multi-state, multi-language splitting (education); minor-protection settings; capacity sizing.
- Awareness campaigns: tracking score and per-campaign real-outcome forecast (partly fixed in 0.5.1).

### Repo layout
- Plugin: `.claude-plugin/`, `skills/`, `references/`, `scripts/`, `examples/`.
- Dev only (exclude from the packaged plugin): `dev/evals/` (scenarios, answer keys, runner prompt, grades, run outputs).
- Runner agents must not open files with "key" in the name or any `grade_*` file.

## Changelog
**0.5.1 (4 Oct 2026)**: added UAE/KSA/UK/US/AU/NZ planning anchors, reach and funnel benchmarks, FMCG/beverage, third-party-ticketing events and Gulf-language playbooks, awareness tracking scoring, caffeine/alcohol and UAE/KSA policy notes.

**0.5.0 (4 Oct 2026)**: from graded blind tests (regression 89.8%, fresh set A 89.8%): D2C break-even and existing-audience rules, health/lending/app/recruitment/food playbooks, consent-gated and WhatsApp tracking statuses, policy-cap scoping and forecast widening, budget cost-point and test-cap rules, hard-boundary wording unified.

**0.4.0 (4 Oct 2026)**: new rulebooks (budget-allocation, scope-and-channels, vertical-playbooks, quality-gate), confidence caps, expanded India benchmarks, policy decline table, test-and-scale schedule. Blind-test round 1 only partly run; further test/fix rounds planned.

**0.3.1 (4 Oct 2026)**: HTML plan uses the light theme by default, regardless of the viewer's system setting.

**0.3.0 (4 Oct 2026)**
- Default output is now an HTML journey board (Poppins, Meta blue, light theme), built from plan JSON by `scripts/render_plan.py`. Fixed-height flows scroll sideways; the left rail shows platform, stage, objective and goal; cards follow the 80/20 visual rule with details in a click-open drawer; detail tabs for summary, confidence, research, tracking, policy and launch.
- Example plan: `examples/agrovest-plan.json`.

**0.2.0 (4 Oct 2026)**, from the Agrovest test run:
- Tracking audit detects ad-blocking browser extensions and never reports "Not found" from a blocked browser. It reads the Google Tag Manager container directly to see which tags are configured, and uses a fixed status vocabulary (Verified firing / Configured, firing unverified / Configured, not firing / Not found / Unknown).
- New Ad Library search protocol (`references/ad-library-search.md`): query set with exact-phrase and local-language searches, advertiser lookups, a 4-point relevance filter, and a confidence rating for the competitor read.
- Special ad categories are decided by audience country (housing, employment and credit categories are required only in the US, Canada and Europe; optional elsewhere), with split-campaign guidance for mixed audiences.

**0.1.0 (4 Oct 2026)**: first version.
