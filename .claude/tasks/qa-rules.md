# QA Rules

Validate all rules against schema, contracts, and patterns.

Workflow: `.shared/workflows/rule-validation.md`
Checklist: `.shared/knowledge/qa-checklist.md`

## Tasks

### Sequential
- [ ] `/validate-rules` — get full error list
- [ ] Triage errors by type (schema / contract / pattern)

### Parallel (run simultaneously)
- [ ] Fix schema errors (missing fields, invalid values)
- [ ] Fix contract errors (.md ↔ .yml mismatches)
- [ ] Fix pattern errors (pattern syntax, exit 2/7)

### Sequential (after parallel)
- [ ] `/validate-rules` — confirm all pass

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
- Pattern errors: ___

**After:**
- Schema errors: ___
- Contract errors: ___
- Pattern errors: ___

## Run History

| Run | Date | Result | Notes |
|-----|------|--------|-------|
| 1   | 2026-01-28 | PASS | Fixed schema issues, documented exceptions |

## Reset

To re-run: `sed -i 's/\[x\]/[ ]/g' .claude/tasks/qa-rules.md`

## Notes

_Progress notes written during execution:_
