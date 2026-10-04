# Learnings ledger

The plugin cannot remember between conversations by itself. Learning is kept in a ledger file that the user owns and attaches to future runs.

## Where it lives
- File name: `ad-learnings-ledger.md`.
- The user keeps it (their own folder or drive). If a folder on the user's computer is connected and the user has said where the ledger lives, read and update it there. Never store it in the Iugale Workspace (see guardrails).
- If the user doesn't have one yet, create it after the first results review and send it to them.

## Rules
- Add entries only after the user approves them in chat.
- Aggregate numbers only. No individual lead data.
- Each entry is one observation with the evidence behind it. Keep entries short.
- When the same lesson appears in 3+ entries across clients, mark it "Pattern" — candidates to fold into benchmarks.md / playbooks in the next plugin version.

## Entry format
```
### <YYYY-MM-DD> — <Client> — <Platform> — <Campaign name>
Context: <vertical, city, budget/day, objective, conversion location, goal>
Predicted: <metric range + confidence score from the plan>
Actual (<date range>): <spend, results, cost per result, CTR, CPM, frequency; qualified / visits / closed counts if known>
Gap: <within range / above / below, by how much>
Why (best explanation): <evidence-based reason>
Lesson: <one sentence that would change a future plan>
Applies to: <this client only / vertical / platform-wide>
Status: Single observation | Pattern (n=<count>)
```

## Sections in the file
1. Patterns (cross-client lessons)
2. Benchmarks observed (vertical × city × conversion location → cost per result, cost per qualified lead)
3. Entries (newest first)
