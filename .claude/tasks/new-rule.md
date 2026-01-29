# New Rule: {ID}

Create a new rule with full evidence chain.

Workflow: `.shared/workflows/rule-creation.md`
Knowledge: `.shared/knowledge/rule-authoring.md`

## Setup

**Rule ID:** ___
**Scope:** core | claude | copilot | cursor
**Title:** ___
**Category:** structure | content | efficiency | governance | maintenance

## Tasks

### Sequential
- [ ] Find backing sources in `docs/sources.yml`
- [ ] Determine type: deterministic | semantic
- [ ] Check backing sources → tier is derived (core if max weight >= 0.8, else experimental)
- [ ] `/generate-rule {ID} {scope} "{title}"`
- [ ] Verify OpenGrep validates (exit 0 or 1)

### Parallel (run simultaneously)
- [ ] Update `docs/sources.yml` — add rule to claim.rules[]
- [ ] Update `CHANGELOG.md`

### Sequential (after parallel)
- [ ] `/validate-rules` — new rule passes
- [ ] `/audit-evidence-chain` — no broken links

## Result

**Status:** ☐ PASS ☐ FAIL
**Run #:** ___

**Files created:**
- [ ] `core/{category}/{ID}-{slug}/{ID}-{slug}.md`
- [ ] `core/{category}/{ID}-{slug}/{ID}-{slug}.yml`
- [ ] `core/{category}/{ID}-{slug}/tests/fail.md`
- [ ] `core/{category}/{ID}-{slug}/tests/pass.md`

**Validation:** ☐ PASS ☐ FAIL

## Run History

| Run | Date | Result | Notes |
|-----|------|--------|-------|
| 1   |      |        |       |

## Reset

To re-run: `sed -i 's/\[x\]/[ ]/g' .claude/tasks/new-rule.md`

## Notes

_Progress notes written during execution:_
