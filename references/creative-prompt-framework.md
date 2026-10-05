# Creative prompt framework

At least five prompts per campaign. Each prompt is ready to paste into an AI image or video generator, plus the copy pack to run it. This framework is self-contained; do not hand off to any other Iugale creative skill. Images are generated in ChatGPT, not here: write every image prompt paste-ready for ChatGPT per `${CLAUDE_PLUGIN_ROOT}/references/chatgpt-image-handoff.md`, and review what comes back with `skills/ad-creative-review`.

## 1. Pick five different angles (one per prompt)
| Angle | Psychology | Typical hook |
|---|---|---|
| Pain / problem | Loss aversion, recognition | "Peeling walls before Diwali guests arrive?" |
| Proof | Social proof, seeing is believing | Before/after, real customer, star rating |
| Offer / urgency | Scarcity, reciprocity | "Free site visit this week only" |
| Authority / process | Competence, reduces risk | Expert on camera, "our 5-step process" |
| Objection-killer | Removes the main reason not to act | Price clarity, warranty, "no mess, done in 3 days" |
Optional extras for larger budgets: identity/aspiration ("the home you've been waiting for"), comparison (us vs typical), UGC-style testimonial, founder story.

Use the research: claim gaps competitors leave open; avoid the hook style every competitor already uses.

## 2. Choose image or video per prompt, and say why
- Video (9:16 first, 6-15s) for proof and process: transformations, demos, testimonials. Strongest on Reels/Stories/Shorts.
- Static image (4:5 and 1:1, plus 9:16 variant) for offer, price, simple claims; fast to produce and test.
- Carousel for multiple services or a step sequence.
- Google Search has no creative image; for Search write RSA text (in the Google skill). PMax/Demand Gen need images (1.91:1, 1:1, 4:5) and video (16:9, 9:16, 1:1), logos.

## 3. Prompt structure (fill every field)
```
CREATIVE <n> — <Angle> — <Image|Video> — for <Campaign name>
Why this format: <one line>
Ratios: <e.g. 9:16 master, 4:5 and 1:1 crops>; keep key text inside the central safe area (avoid top ~14% and bottom ~20% on 9:16).

GENERATION PROMPT:
<For image> Subject, setting, composition, camera/lens feel, lighting, colour palette (brand colours if known), mood, people (age range, local look appropriate to the market), what text space to leave, style (photoreal / editorial / UGC phone-shot), what to avoid (no logos of other brands, no distorted hands, no fake certificates).
<For video> Shot list with timings: 0-2s hook shot (pattern interrupt), 2-8s proof/demonstration, 8-12s offer + CTA end card. Camera movement, pacing, on-screen text per beat, voiceover line or "no VO, captions only", music mood, sound-off readability.

ON-SCREEN TEXT: <max ~7 words per frame>
PRIMARY TEXT (Meta) / DESCRIPTION: <first line = hook/offer; ≤125 chars before truncation>
HEADLINE: <5-8 words>
CTA BUTTON: <Send WhatsApp message / Get quote / Book now / Learn more / Call now>
WHATSAPP GREETING (if WhatsApp): <pre-filled message with campaign code> + quick replies (2-4)
EXPECTED OUTCOME: <what this creative should do: e.g. "highest CTR, lower lead quality"; "fewer but warmer leads"> and the metric to judge it by.
POLICY CHECK: <any risk: health claims, before/after rules, special ad category>
```

## 4. Quality bar
- No personal-attribute phrasing: never imply the viewer has a condition, debt, age, religion, etc. ("your acne", "struggling with debt?", "are you depressed?"). Speak about the product or a general situation instead.
- Every claim must be substantiated by the client; mark unverifiable claims "client to confirm".
- Hook in the first 1-2 seconds / first line. The offer visible without sound.
- One message per creative.
- Real-looking local context (homes, streets, clinics in the target city), not generic stock.
- Visually distinct concepts across the five (platform delivery systems group look-alike ads).
- Brand identity consistent: logo small, colours from the website.
- No unverifiable claims ("best in Bangalore", "100% guaranteed") unless the client can prove them.

## 5. Testing plan for the five
Launch 3-5 at once in one ad set (Meta) or one asset group (PMax/Demand Gen). After ~7 days or ~2× target CPA spend per creative, pause clear losers; replace with a new angle, not a minor edit.
