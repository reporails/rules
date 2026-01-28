# Release Prep

Run before publishing a new version.

Workflow: `.shared/workflows/rule-validation.md` + `.shared/workflows/evidence-audit.md`

## Tasks

### Parallel (run simultaneously)
- [ ] `/validate-rules` — all rules pass
- [ ] `/audit-evidence-chain --report` — trust score acceptable

### Sequential (after parallel)
- [ ] Review `.reporails/audit-report.md`
- [ ] Update `CHANGELOG.md` with version
- [ ] Update version in `package.json` (if applicable)
- [ ] `git tag vX.Y.Z`

## Result

**Status:** ☐ PASS ☐ FAIL
**Run #:** ___

**Trust Score:** ___
**Rules Passing:** ___/___
**Version:** ___

**Ready to release:** ☐ YES ☐ NO

## Run History

| Run | Date | Result | Notes |
|-----|------|--------|-------|
| 1   |      |        |       |

## Reset

To re-run: `sed -i 's/\[x\]/[ ]/g' .claude/tasks/release-prep.md`

## Notes

_Progress notes written during execution:_
