# Extract Claims: agents.md

Add agents.md as the canonical source for universal agent patterns.

Workflow: `.shared/workflows/claim-extraction.md`

## Source Info

- **URL:** https://agents.md/
- **Type:** official (de facto standard)
- **Weight:** 1.0
- **Section:** generic

## Tasks

### Sequential
- [ ] `/extract-claims https://agents.md/ --source-id agents-md-spec`
- [ ] Review extracted claims

### Parallel (run simultaneously)
- [ ] Map claims to existing rules
- [ ] Add to `docs/sources.yml` under `generic:`

### Sequential (after parallel)
- [ ] Update rules with `backed_by` references
- [ ] `/audit-evidence-chain` — verify links

## Expected Claims

Based on agents.md spec, expect claims about:

| Topic | Likely Rules |
|-------|--------------|
| Markdown instruction file | S1, C1 |
| Project description | C9, C1 |
| Explicit instructions | C2, C5 |
| File structure guidance | S2, C1 |
| Anti-patterns | C4, C10 |

## Result

**Status:** ☐ PASS ☐ FAIL
**Run #:** ___

**Claims extracted:** ___
**Rules updated:** ___
**New trust score:** ___

## Run History

| Run | Date | Result | Notes |
|-----|------|--------|-------|
| 1   |      |        |       |

## Reset

To re-run: `sed -i 's/\[x\]/[ ]/g' .claude/tasks/extract-claims-agents-md.md`

## Notes

_Progress notes written during execution:_
