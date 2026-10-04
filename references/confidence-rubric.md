# Confidence rubric

Score every major recommendation (platform split, each campaign, conversion location, budget sufficiency) and every forecast, plus the plan overall. 0-100.

## Factors and weights
Rate each factor 0-10, multiply by weight, sum, divide by the total weight of the factors that apply.

| Factor | Weight | 10 | 7 | 5 | 3 | 0 |
|---|---|---|---|---|---|---|
| Tracking of the optimisation event AND the real outcome | 20 | Both verified (event firing + CRM/backend reconciled) | Event verified, real outcome tracked manually | Event configured but firing unverified | Platform-native only (e.g. WhatsApp conversations) with no downstream tracking | Optimising for an untracked or broken event |
| Budget sufficiency (budget-allocation.md §1) | 20 | ≥ comfortable level | ≥ minimum | learning-limited test level | below test level but some data in 30 days | can't produce meaningful data |
| Cost evidence | 15 | Client's own recent data, same channel and offer | Client's data, different channel/offer, or Iugale learnings ledger for the vertical | Live-searched current benchmark, same vertical and region | Plugin benchmark table only | No benchmark (improvised) |
| Offer & conversion experience | 15 | Clear offer, fast path, replies in minutes | Good, minor gaps | Average | Weak offer or slow replies | No offer and broken path |
| Competitor evidence (ad-library-search.md) | 10 | 8+ relevant ads, 30+ days | 3-7 relevant | some activity | little | none / unknown |
| Policy risk | 10 | Normal category, clean claims | Restricted category handled | Grey area handled with fallback | Open issue needing client action | Likely rejection/suspension |
| Seasonality / market | 10 | Clear tailwind | Mild tailwind | Neutral | Mild headwind | Strong headwind |
Interpolate between columns.

## Caps (apply after the weighted score)
- Optimisation event untracked or broken → campaign capped at **40**.
- Real outcome not trackable even manually (no CRM, no tally, no reconciliation) → capped at **60**.
- No client data and no live benchmark (plugin table only) → forecasts capped at **60**; campaign recommendations at **75**.
- Open policy blocker the client must fix before launch → capped at **55** until fixed.
- Learning-limited test budget → capped at **60**.

## Plan overall
Spend-weighted average of funded campaigns, then the lowest applicable cap among plan-level issues (e.g. tracking broken across the account). Deferred campaigns are scored but not averaged.

## Bands
- **80-100: Launch as planned.** · **60-79: Launch with the listed fixes.** · **40-59: Fix blockers first, or run as a small test.** · **Below 40: Don't spend yet.**

## Forecast ranges
Range width tracks confidence: 80+ ±20% · 60-79 ±35% · below 60 ±50% or wider ("rough"). Centre the range on the stated benchmark/history value. Never show a single number.

## Every score states what would raise it
Format: `62/100 → ~78 if: Meta Pixel confirmed firing on form success (+8); last 90 days' cost per lead shared (+8).`

## v0.5 additions
- A policy or tracking cap applies to the **campaign it affects**. State "per campaign" or "account-wide" explicitly.
- For "launch with fixes", show both scores: now (capped) and after fixes (uncapped), and headline the capped one.
- A capped score widens the forecast band by one step (±35% → ±50%). Forecast confidence never exceeds the band edge.
- Overall score weights funded campaigns by budget; planned/deferred campaigns are listed but do not count. With one funded campaign, overall = that campaign.

## v0.5.1 additions
- **Awareness campaigns:** the Tracking factor measures whether the intended read exists (platform reach/frequency verified = 6 of 10; plus brand lift or matched-market lift set up = 8-10; nothing planned = 3). The "offer" factor measures message clarity and distribution readiness for offline products.
- **Unknown tracking** scores 5 of 10 and is stated as "Unknown", never as Not found.
- **Real-outcome forecast for awareness:** a plan-wide hypothesis range is acceptable; the per-campaign requirement applies to performance campaigns only.
