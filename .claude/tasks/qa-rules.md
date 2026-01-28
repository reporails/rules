# QA Rules

Validate all rules against schema, contracts, and OpenGrep.

Workflow: `.shared/workflows/rule-validation.md`
Checklist: `.shared/knowledge/qa-checklist.md`

## Tasks

### Sequential
- [ ] `/validate-rules` — get full error list
- [ ] Triage errors by type (schema / contract / OpenGrep)

### Parallel (run simultaneously)
- [ ] Fix schema errors (missing fields, invalid values)
- [ ] Fix contract errors (.md ↔ .yml mismatches)
- [ ] Fix OpenGrep errors (pattern syntax, exit 2/7)

### Sequential (after parallel)
- [ ] `/validate-rules` — confirm all pass
- [ ] `/audit-evidence-chain` — verify trust score

## Error Triage

| Rule | Error Type | Issue | Fixed |
|------|------------|-------|-------|
|      |            |       |       |

## Result

**Status:** ☐ PASS ☐ FAIL
**Run #:** ___

**Before:**
- Schema errors: ___
- Contract errors: ___
- OpenGrep errors: ___

**After:**
- Schema errors: ___
- Contract errors: ___
- OpenGrep errors: ___

**Trust Score:** ___

## Run History

| Run | Date | Result | Notes |
|-----|------|--------|-------|
| 1   | 2026-01-28 | PASS | Fixed CLAUDE_G1 schema, M1/CLAUDE_S2 documented as exceptions |

## Reset

To re-run: `sed -i 's/\[x\]/[ ]/g' .claude/tasks/qa-rules.md`

## Notes

_Progress notes written during execution:_
