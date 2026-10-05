# Claude + ChatGPT workflow: Claude plans, ChatGPT makes the images

Claude (this plugin) handles analytics, strategy and text. ChatGPT generates the images. Do not try to generate images here; hand off prompts and review what comes back. No ad-account or social-account access is needed on the ChatGPT side.

## 1. Handoff: how Claude writes an image prompt
Every image prompt in the plan (`ads[].prompt`) must be **paste-ready for ChatGPT**:
1. One self-contained prompt per image: subject, setting, composition, lighting/mood, colour palette (give hex codes of the brand), camera/style cues (e.g. "photographic, natural light, shallow depth of field" or "clean flat illustration"), and what is *not* in the image.
2. **Format:** state the target ratio and where it will be used (Feed 1:1 or 4:5, Reels/Stories 9:16, LinkedIn 1.91:1 or 1:1, X 16:9 or 1:1). ChatGPT outputs a limited set of sizes (square, portrait, landscape): ask for the closest size and tell it to keep the key subject and any text inside a central safe zone (about the middle 80%, and clear of the top/bottom ~14% for Stories/Reels UI) so it can be cropped to the target ratio.
3. **Text in the image:** keep it minimal (a headline of ≤ 6 words at most). Put the exact text in quotes and say "render exactly, no other text". Image generators still misspell sometimes: ask for 2 variants, and plan to add the final headline and logo as an overlay (Meta's own text/creative tools, Canva) when spelling or fonts matter. Faces, logos and prices should be checked by a human.
4. **Compliance lines** in the prompt: adults only where required, no before/after body or health claims, no identifiable real people or children for distress themes, culturally appropriate dress and imagery, no competitor logos, no fake UI. These come from policy-watch.md and claims-and-compliance.md.
5. **Video:** ChatGPT is for stills. For video give a storyboard (6-15s, scene by scene: image prompt, on-screen text, voice-over line, audio direction) that can be shot, edited or animated with a video tool. The voice-over/script text is Claude's job.
6. **Variants:** ask for a set (e.g. 3 images per angle: hero, close-up, lifestyle) so Claude can pick winners by plan angle, not taste.
7. Include a short "edit prompt kit": 3 ready follow-ups to paste if the first result misses ("make the product larger and centred", "remove all text", "use warmer light, keep the layout").

## 2. Return: bring images back for review
The user attaches the generated images (or screenshots) to Claude. Use `skills/ad-creative-review/SKILL.md`: legibility on a phone, text spelling, 80/20 visual-first composition, safe zones per placement, brand colours, policy and claim checks, face/minor rules, similarity to competitors, and fit with the angle. Output: pass/fix per image, ranked picks, and exact **edit prompts** for ChatGPT.

## 3. Measuring creative
Name files and ads with the plan code: `<client>_<campaign>_<angle>_<version>_<ratio>` (e.g. `AGV_MetaWA_BrokerPain_v2_9x16`). Use the same name as the Ad name in Ads Manager so exports map back to the creative angle and the monitor can rank angles, not just ads.

## 4. Loop
Plan (Claude) → prompts (Claude) → images (ChatGPT) → review and edit prompts (Claude) → upload by a human → export (Meta) → monitor (Claude) → next moves (Claude) → new prompts.
