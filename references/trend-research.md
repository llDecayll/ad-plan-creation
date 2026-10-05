# Market and trend research (what to launch, change or add next)

Used by `skills/ad-next-moves` and by Phase B of ad-strategy for the Channel-role plan. Everything here is research for a human to act on: no ad-account access, aggregate data only, public pages and user-supplied exports only. Mark each finding "verified live <date>" (searched today) or "from playbook/benchmark".

## 1. Inputs
1. The current plan and the latest monitor reads (what is working or failing).
2. **Existing channels**, read only through: the client's public pages (website, Facebook, Instagram, LinkedIn page, X profile), the Ad Library / Transparency Center, and **aggregate exports the user attaches** (page/post insights: reach, views, saves, shares, watch time, clicks; GA4 or site analytics summaries). No logins, no individual follower or lead data.
3. Competitors and category leaders (Ad Library, YouTube search, competitor posts).
4. Demand signals: Google Trends and live SERPs for the main topics, seasonality, festivals/events for the next 90 days, news.

## 2. What to research (run the searches live)
- **Format and media trends in the client's category, last 60-90 days:** short vertical video (Reels, Shorts, X video, LinkedIn video), creator/UGC and partnership ads, carousels/documents (LinkedIn), static vs video mix, **audio**: trending/original audio on Reels and Shorts, voice-over-led explainers, podcast or audio-first clips, audio-only placements where available, captions for sound-off viewing. Search the platforms' own ad/creative best-practice pages and trade coverage; confirm with competitors' running ads.
- **Own organic winners:** which posts/videos earn the highest watch time, saves, shares and link clicks on each existing channel. Winners become paid creative tests (boost what already works).
- **Demand shifts:** rising and falling queries, seasonality, new objections, pricing or policy changes.
- **Competitor moves:** new offers, formats, long-running ads (30+ days = likely profitable), new channels.
- **Platform changes in the last 60 days** (policy-watch.md baseline plus live search).

## 2b. Rules for evidence quality
- **Dates:** search snippets are often undated. Fetch the primary page (platform newsroom, Meta for Business, Google Ads, LinkedIn Marketing and X Business blogs) to confirm the date. A finding you cannot date is marked "date unverified" and scored as low-confidence; vendor blogs are weak evidence. Never quote a statistic from a single secondary blog as fact.
- **Existing channels unreachable** (blocked pages, logins, no access): say so, ask the user for aggregate exports (page/post insights, site analytics) and proceed with the plan, the ad monitor read and public search, with confidence reduced and "organic winners unknown" stated.
- **Plateau first:** if the trigger is a plateau, read the latest ad-monitor output (frequency, CTR trend, click-to-result, qualified %) before choosing moves: creative fatigue → new creative; audience saturation → new ad set; post-click leak → website/WhatsApp fix, not new media.

## 2c. Audio and video guidance
- Short video (6-30s, 9:16 first): hook in 2 seconds, captions burned in (most views are sound-off), but build the sound (voice-over or original audio) because sound-on viewers convert better.
- Voice-over in the audience's language (e.g. Kannada, Hindi, Arabic) usually beats subtitles alone for regional audiences; test one language variant per ad set.
- Music: use platform-licensed libraries (e.g. Meta's Sound Collection, YouTube Audio Library) for ads; trending commercial tracks are often not licensed for ads. Confirm rights before launch.
- Audio-first formats (podcast clips, audio ads, voice notes) are a test line, not a core campaign, unless the audience is audio-native.
- Always provide a still/static fallback and a version without audio dependence.

## 3. Turn findings into moves
For each finding, choose the smallest move that tests it. Move types, in order of preference:
1. **New creative or format** in an existing ad set (duplicate, never edit a winner).
2. **New ad set** in an existing campaign (new audience, location slice, placement, language).
3. **New campaign** (new objective, conversion location, or channel) as a `planned` flow with a trigger and flight.
4. **Retire or pause** (fatigued creative, losing audience, saturated format).
5. **Website/tracking change** (landing page for the new offer, event, form, WhatsApp flow).

Score each move: impact, confidence (confidence-rubric.md), effort, budget needed, risk. Keep the top 5. Respect budget-allocation.md (learning minimum, test cap), policy-watch.md and claims-and-compliance.md. Every move names its trigger, test length (flight), success target and kill rule.

## 4. Output (the "next moves" brief)
- Findings table (source, date, so-what).
- Ranked moves with change prompts (see ad-monitor's prompt format): where to change, exactly what, creative brief with format (including audio/video direction), budget, flight, target, kill rule.
- Plan delta: a JSON file for `scripts/merge_plan.py` (`addFlows` for planned campaigns, `addAdsets` for new ad sets in an existing flow, `updateFlows`, `addSections`). Apply: `python3 ${CLAUDE_PLUGIN_ROOT}/scripts/merge_plan.py plan.json delta.json plan.json`, then render. Planned flows must carry budget, a flight trigger and a target with kill rule.
- A data request in this format: channel | export or screenshot | metrics | date range | by when (e.g. "Instagram | post insights | reach, saves, shares, watch time | last 30 days | before the next check").
