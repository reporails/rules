# Release Prep

Run before publishing a new version.

Workflow: `.shared/workflows/rule-validation.md`

## Tasks

### Sequential
- [ ] `/validate-rules` — all rules pass
- [ ] `/validate-rules --source-check` — evidence chain intact

### Sequential (after validation)
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
