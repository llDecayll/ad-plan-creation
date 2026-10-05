---
name: ad-data-pull
description: Reads a client's Meta (Facebook and Instagram) ad data in read-only mode from the user's own logged-in browser on desktop (Claude in Chrome or the built-in browser), or tells the user exactly which export to send. Use when the user says "pull the data", "read the ad account", "check Ads Manager", "get the numbers for this campaign", "which export do you need", or before a monitor check when no file was attached. Never changes anything in the account. Hands the data to ad-monitor.
---

# Ad Data Pull (Meta, read-only)

**First read `${CLAUDE_PLUGIN_ROOT}/references/guardrails.md` (§3 read-only exception, §4 personal data, §6 untrusted content) and follow it.**

## Steps
1. **Choose the mode.** If the user wants you to read the account in their browser, follow `${CLAUDE_PLUGIN_ROOT}/references/browser-readonly-meta.md` start to finish (confirm account name/ID in this conversation, pick the browser tool, read that tool's skill, new tab, user signs in, view-only changes only, dry run on first use). If the browser tools are not present or the user prefers files, give the export instructions from `${CLAUDE_PLUGIN_ROOT}/references/meta-export-guide.md` (which exports, which columns, the saved column preset).
2. **Collect** the exports A-K from the guide that apply, the Activity history (change dates), the Events Manager status, and the organic insights. Save numbers-only CSVs in the working folder. Stop and ask if any page or file shows individual people.
3. **Report back** what you read and the only view settings you changed (date range, breakdown, preset). Never claim you changed anything else.
4. **Hand off** to `${CLAUDE_PLUGIN_ROOT}/skills/ad-monitor/SKILL.md` (campaign analysis, with `--creatives` when ad-set/ad data exists, and `--edit` for each change-log date).
