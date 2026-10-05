---
name: ad-creative-review
description: Reviews ad images and videos that the user generated in ChatGPT (or elsewhere) before they are uploaded to Meta, and writes edit prompts to send back to ChatGPT. Use when the user attaches generated creatives and asks "is this ready", "review these images", "which one should we use", "fix this creative", or after the plan's image prompts were run in ChatGPT. Checks legibility, text spelling, safe zones per placement, brand fit, policy and claims, and the intended angle. Does not generate images.
---

# Ad Creative Review (ChatGPT handoff, return leg)

**First read `${CLAUDE_PLUGIN_ROOT}/references/guardrails.md` and `${CLAUDE_PLUGIN_ROOT}/references/chatgpt-image-handoff.md`.** Claude does not generate images; ChatGPT does. You review and write the edit prompts.

## Inputs
The generated image(s) or screenshots, the plan (campaign, ad set, angle, ratio, placement, offer and claims), and brand colours/logo notes.

## Steps
For each image:
1. **Angle fit:** does it express the planned angle (pain, proof, offer, authority, objection-killer) in the first second?
2. **Phone legibility:** subject clear at thumbnail size, contrast, text readable; headline ≤ 6 words; spelling and numbers exactly as in the plan (read the text in the image and compare character by character).
3. **Composition and safe zones:** key subject and text inside the central safe zone for the target ratio; clear of the Stories/Reels UI areas; croppable to 1:1, 4:5 and 9:16 as needed.
4. **Brand and quality:** palette, logo placement, distorted hands/faces/products, artefacts, fake UI.
5. **Policy and claims:** policy-watch.md and claims-and-compliance.md (before/after, personal-attribute phrasing, minors, health/finance claims, identifiable people, competitor marks, culturally appropriate imagery).
6. **Distinctiveness:** compared with competitor ads you have seen, does it stand out or look generic?

## Output
A table: image | verdict (PASS / FIX / REJECT) | the issue | ranked pick per angle. For each FIX, write an exact **edit prompt** to paste into ChatGPT (keep what works, change one thing), and say when text should instead be added as an overlay. End with the file names to use (`<client>_<campaign>_<angle>_<version>_<ratio>`) so Ads Manager exports map back to the angle.
