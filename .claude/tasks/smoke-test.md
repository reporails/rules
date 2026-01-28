# Smoke Test

Run after structural changes to `.shared/` or `.claude/skills/`.

Workflow: `.shared/workflows/qa-smoke-test.md`
Checklist: `.shared/knowledge/qa-checklist.md`

## Tasks

### Sequential
- [ ] `/generate-rule SMOKE1 core "Smoke Test"`

### Parallel (run simultaneously)
- [ ] `/validate-rules`
- [ ] `/audit-evidence-chain`

### Sequential (after parallel)
- [ ] `/update-rule SMOKE1 "Add pattern for SMOKETEST keyword"`
- [ ] `/validate-rules`
- [ ] `rm core/*/SMOKE1-*`

## Result

**Status:** ☐ PASS ☐ FAIL
**Run #:** ___

| Task | Status |
|------|--------|
| generate-rule | ☐ |
| validate-rules | ☐ |
| audit-evidence-chain | ☐ |
| update-rule | ☐ |
| re-validate | ☐ |
| cleanup | ☐ |

## Run History

| Run | Date | Result | Notes |
|-----|------|--------|-------|
| 1   |      |        |       |

## Reset

To re-run: `sed -i 's/\[x\]/[ ]/g' .claude/tasks/smoke-test.md`

## Notes

_Progress notes written during execution:_
