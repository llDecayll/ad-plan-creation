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
| ad-strategy | Full plan across Facebook/Instagram, Google/YouTube, LinkedIn and X, with feasibility verdict, channel roles, flights and targets per campaign (start here) |
| meta-ads-planner | Meta-only plan |
| google-ads-planner | Google-only plan |
| ad-monitor | Keeps watch: reads your campaign exports (Meta, Google, LinkedIn, X) against the plan and your own brief, alerts, gives three outlooks and ready-to-paste change prompts |
| ad-next-moves | Market and trend research (video, audio, formats) plus your existing channels, to recommend the next campaign, ad set or creative |
| ad-data-pull | Meta only: reads the ad account in your own browser in read-only mode (desktop), or tells you exactly which export to send |
| ad-creative-review | Reviews images you generated in ChatGPT and writes edit prompts to send back |
| ad-results-review | Ledger-focused predicted-vs-actual review |

**How "keep an eye" works:** the plugin cannot watch an ad account (no account access, by design). You send the export on a cadence (day 3, 7, 14, 21, 30, then weekly; every 2-3 days when RED). `scripts/analyze_export.py` reads it, applies the plan's `monitor` rules plus the rules you explain in a brief (`references/monitor-brief-template.md`), and the skill adds judgement. Updates go back into the plan with `scripts/merge_plan.py`.

Example prompts:
- "Plan ads for paintkraft.in — we want WhatsApp enquiries in Bangalore, ₹1,000/day."
- "Just the Google Ads plan for toothlyfedentalclinic.com."
- "Here's last week's Meta export for Paintkraft — review it against the plan."

## Built-in rules
- Never touches the Iugale Workspace (no reading unless you explicitly ask; never writing or pushing).
- Independent: does not use or change any other Iugale skill.
- No ad-account connection; performance data only from files you attach.
- Aggregate numbers only; no individual lead data.

## Claude + ChatGPT workflow
Claude does analytics, strategy and text; ChatGPT makes the images. The plan's image prompts are written paste-ready for ChatGPT (`references/chatgpt-image-handoff.md`); you bring the generated images back and `ad-creative-review` checks them and writes edit prompts. Naming convention `<client>_<campaign>_<angle>_<version>_<ratio>` lets exports map results back to creative angles.

## Desktop setup after you clone (read-only account access)
1. Run the plugin in the Claude desktop app and connect a browser tool: Claude in Chrome (your real Chrome and sign-ins) or the built-in browser.
2. Say in the conversation that Claude may read a named Meta ad account in read-only mode. It then follows `references/browser-readonly-meta.md` (guardrails §3): you sign in yourself; it only reads; it never publishes, edits, pauses or opens individual leads.
3. Create the "Claude Monitor" column preset once in Ads Manager (`references/meta-export-guide.md` §3) so every read and export has the same columns.
4. Do the one-time dry run in `browser-readonly-meta.md` §5 per client (watch the browser, compare totals) before trusting it. **This browser flow has not been tested in the cloud build; test it on first use.**
5. No browser tool? Use the export route: `references/meta-export-guide.md` lists which exports to send and the columns needed.
Scope today: Meta (Facebook and Instagram) only. Google, LinkedIn and X use attached exports.

## Related open-source projects
Other projects work in this space. They differ in approach: several connect to ad-account APIs and can change campaigns, while this plugin plans first and stays read-only by default.
- [meta-ads-kit](https://github.com/TheMattBerman/meta-ads-kit) (MIT): daily Meta monitoring, fatigue, budget shifts, copy and uploads via Meta's CLI. Some ideas here are adapted from it (see `NOTICE.md`).
- [claude-ads](https://github.com/AgriciDaniel/claude-ads), [claude-marketing](https://github.com/thatrebeccarae/claude-marketing), [goose-skills](https://github.com/gooseworks-ai/goose-skills), [Pipeboard meta-ads-mcp](https://github.com/pipeboard-co/meta-ads-mcp): not reviewed in detail; check their licences and permissions before using alongside this plugin.

## Learnings ledger
The plugin can't remember between chats on its own. After each results review it proposes entries for `ad-learnings-ledger.md`; you approve them and keep the file. Attach it to future runs so plans start from Iugale's real results. Lessons seen across 3+ clients should be folded into `references/benchmarks.md` in the next plugin version.

## Keeping it current
Platform rules change monthly. The plugin checks policy and platform changes live on every run; `references/policy-watch.md` and the playbooks hold the baseline (last reviewed 4 Oct 2026). Update them when Meta or Google make major changes.

## Changing the design
The look lives in `references/html/plan-template.html`. Edit the design tokens at the top of its `<style>` block (font, `--brand` colour, `--flow-base-h` flow height, card widths) or the layout itself. Plans keep working as long as the `/*__PLAN_DATA__*/` placeholder stays. The data format is in `references/html-output.md`.

## Continuation plan (for a cloud session)
Status at v0.9.0 (4 Oct 2026): plugin built and rules updated after Round 4.

| Test | Version | Score |
|---|---|---|
| Regression set S1–S5 | v0.3 | 87.5% |
| Regression set S1–S5 | v0.4 | 39.5/44 = 89.8% |
| Fresh Set A (A1–A6) | v0.4 | 48.5/54 = 89.8% |
| Regression S1–S5 (Round 1) | v0.5.1 | 39/44 = 88.6% |
| Fresh Set A (Round 1) | v0.5.1 | 50/54 = 92.6% |
| Set B (B1–B3 run only, ungraded) | v0.5 | n/a |
| Set B (Round 2, B1–B6) | v0.5.2 | 46/56 = 82.1% |
| Set B re-run (Round 2b) | v0.5.3 | 48/56 = 85.7% |
| Set B re-run (Round 2c) | v0.5.4 | 49.5/56 = 88.4% |
| Fresh Set C (Round 3) | v0.5.5 | 47.5/59 = 80.5% |
| Fresh Set D (Round 4) | v0.6.0 | 54.0/59 = 91.5% (all traps passed) |

**Round 1 is complete and graded** (`dev/evals/grade_r1_S.md`, `grade_r1_A.md`; runs in `dev/evals/runs/r1_*.md`). v0.5.2 applies its fixes. **Round 2 (Set B on v0.5.2) is complete and graded at 82.1%** (`dev/evals/grade_r2_B.md`; runs in `dev/evals/runs/r2_*.md`). v0.5.3 applies its fixes. Re-runs of Set B scored 85.7% (v0.5.3) and 88.4% (v0.5.4). **Round 3 (fresh Set C on v0.5.5) scored 80.5%** (`dev/evals/grade_r3_C.md`); v0.6.0 applies its fixes. **Round 4 (fresh Set D on v0.6.0) scored 91.5%** (`dev/evals/grade_r4_D.md`), 0.3 points under the 92% target; v0.6.1 applies its small fixes (untested). **Next: a fresh Set E to test v0.7.0 (planning) and a monitoring test set of 5-6 real-shaped exports (monitoring and next-moves are only smoke-tested) (earlier note: a fresh Set D to test v0.6.0 (Set B is now tuned-to; run-to-run noise is about ±1.5 points). The 92% target has not yet been met on a fresh set since v0.5.1 Set A.**

**Hard rules (do not change):** never add or push anything to the Iugale Workspace unless Deepak says so; plugin stays independent of other Iugale skills; no ad-account connections (aggregate numbers only, no lead PII); push only to this repo's `main` when asked.

### Steps
1. ~~**Grade Round 1.**~~ DONE (88.6% / 92.6%). Two independent grader agents: one for S1–S5 against `dev/evals/setS_key.md`, one for A1–A6 against `setA_key.md`. Save to `dev/evals/grade_r1_S.md` and `grade_r1_A.md`. Target ≥ 92%.
2. ~~**Fix round 1.**~~ DONE in v0.5.2. Apply the gaps reported (see "Known open gaps"), bump to 0.5.2, validate (`claude plugin validate .`).
3. ~~**Round 2: Set B.**~~ DONE (82.1% → 85.7% → 88.4%, fixes in v0.5.3-0.5.5). Run B1–B6 blind with `dev/evals/runner_prompt.txt` (replace `<REPO_ROOT>`; ID, FILE, RUN set per run). Run 3–4 agents at a time. Grade against `setB_key.md`, fix, bump to 0.5.3.
4. ~~**Round 3: fresh Set C.**~~ DONE (80.5%, fixes in v0.6.0). Have an independent agent write 6 new scenarios and a key (different goals/industries: e.g. SaaS free-trial, restaurant chain, legal/financial advisory, tourism/hospitality, B2B manufacturing export, healthcare multi-clinic). Run blind, grade, fix, bump to 0.6.0. Stop when two consecutive rounds gain < 1 point.
5. **Final.** Update the changelog, regenerate the example plan with `scripts/render_plan.py`, run `claude plugin validate .`, zip (exclude `dev/`), push to `main`, attach `.plugin` and `.zip`.

Estimated time in a cloud session: about 55–60 minutes.

### Known open gaps (after v0.5.2; check these first in Round 2)
- Round 1 regression S5 (tiny-budget bakery) dropped to 6/8; v0.5.2 adds the tiny-budget rule but it is untested.
- A1: health-data limit on lower-funnel events as a confidence reducer (rule added, untested); UK diaspora test sizing.
- A5: lending: web Conversions API, take-up/credit-risk benchmarks, state-exclusion list under "living in".
- Apps: Google App campaign section in the playbook, SKAN/AEM details, Meta app-campaign minimum.
- Recruitment: lead-form library section (knock-out questions), US RN benchmark, ATS-on-external-domain tracking path.
- Multi-state, multi-language splits (education); capacity sizing rules.
- FMCG/awareness: reach CPM benchmarks exist (v0.5.1); per-campaign real-outcome forecast for awareness is plan-wide only.
- The "five creatives per campaign" gate vs the 1,000-word test cap: tests accept one line each for the lead campaign.
- Benchmarks: all non-India rows are derived ranges; replace with client or live data when available.

### Repo layout
- Plugin: `.claude-plugin/`, `skills/`, `references/`, `scripts/`, `examples/`.
- Dev only (exclude from the packaged plugin): `dev/evals/` (scenarios, answer keys, runner prompt, grades, run outputs).
- Runner agents must not open files with "key" in the name or any `grade_*` file.

## Changelog
**0.9.0 (6 Oct 2026)**: ideas adapted from meta-ads-kit (MIT, credited in `NOTICE.md`): `--briefing` mode (the five daily questions), fatigue alerts on the daily series (CTR decay, CPC inflation, delivery decline), bleeder flag in `--creatives`, and a read-only pixel + Conversions API checklist (`references/pixel-capi-checklist.md`) wired into monitoring and the browser read. README lists related projects.

**0.8.0 (5 Oct 2026)**: Claude + ChatGPT image workflow (paste-ready image prompts, return-leg review skill `ad-creative-review`); read-only browser mode for Meta on desktop (guardrails §3 exception, `browser-readonly-meta.md`, skill `ad-data-pull`); Meta export guide (where to export, columns, 11 exports); `analyze_export.py` now reads Delivery status (learning limited, rejected, in review), location breaches and ranks ad sets and ads (`--creatives`). Browser flow untested in the cloud build: first-use dry run required.

**0.7.0 (5 Oct 2026)**: whole-funnel feasibility verdict; per-campaign flight dates (start, end, length, phases, end action), target tables and machine-readable `monitor` rules, enforced by the renderer and shown on the board; Channel-role plan (`references/omnipresence.md`) across Facebook, Instagram, Google, YouTube, LinkedIn, X and the website; LinkedIn/X playbook (derived ranges); new skills `ad-monitor` (export reader with RED/AMBER/GREEN alerts on campaign-to-date and recent windows, brief rules, edit before/after reads, three outlooks, change prompts) and `ad-next-moves` (trend and audio/video research, existing-channel read, ranked moves); `scripts/analyze_export.py` and `scripts/merge_plan.py`. Tested on a synthetic degrading Meta export and a Google-style export; the two new skills were each run once blind and their gaps fixed. Not yet scored on a fresh Set.

**0.6.1 (4 Oct 2026)**: Round 4 fixes (fresh Set D 91.5%): LTV-based scale thresholds, qualified-enquiry definition and reply targets, space-operator, marketplace and fixed-inventory service rules.

**0.6.0 (4 Oct 2026)**: Round 3 fixes (fresh Set C 80.5%): playbooks for hotels, multi-outlet restaurants, financial advisory, healthcare/fertility, B2B export and SaaS; new `references/claims-and-compliance.md`; staged-start, 3:1 LTV:CAC verdict, capacity weighting and a final minimum-budget ladder; booking-widget and offline-sales tracking; more derived benchmarks and intake questions. Not yet re-tested on a fresh set.

**0.5.5 (4 Oct 2026)**: Round 2c fixes (Set B 88.4%): Arabic fund-vs-park conflict resolved, GBP gate, email Custom Audience, event keywords, NGO seasonality and funded retargeting, soft-metro weighting, minimum-budget ladder, no-pixel status, WhatsApp lead marking, special-category consistency, launch creative spec.

**0.5.4 (4 Oct 2026)**: Round 2b fixes (Set B 85.7%): franchise pilot/weighting/creative kit/lead form, Gulf home-services Arabic/seasonality/AMC LTV, event keyword and ticket maths, launch lift KPIs, NGO nurture, resolved conflicts (brand share, reserve, 7x CPR vs budget, peak shift, Grants roll-up).

**0.5.3 (4 Oct 2026)**: Round 2 fixes (Set B 82.1%): new playbooks (regulated consumables/launch phasing, franchise networks, nonprofits/Ad Grants, travel, UAE home services, hard-date events), history-beats-default and brand-share rules, ramp vs step cap, reserve, currency rule, five-creative gate clarified for written answers, margin/unit/sign-off gates, third-party ticketing and not-linked tracking rules, more benchmark rows, competitor-without-scan scoring, age/claims/cultural guardrails.

**0.5.2 (4 Oct 2026)**: Round 1 fixes (regression 88.6%, Set A 92.6%): cap clarifications (manual tally, declined asks, per-campaign, band widening), tiny-budget and joint-pool rules, split shift, seasonality front-loading, Search keyword/negative requirement, D2C creative volume, brand Search default, suspended-account and minors rules, unified diaspora rule, always-state declarations for credit/employment/housing, extra tracking statuses, margin intake question.

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
