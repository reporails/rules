# Create Release: {VERSION}

Prepare and tag a new release.

## Setup

**Version:** ___ (e.g., 0.2.0)
**Headline:** ___ (e.g., Trust Architecture Foundation)

## Tasks

### Sequential
- [ ] Read `UNRELEASED.md`
- [ ] Group similar changes by theme (not every file — summarize)
- [ ] Create release entry in `CHANGELOG.md`:
  - Use [Keep a Changelog](https://keepachangelog.com/) format
  - Sections: Added, Changed, Fixed, Removed
  - Lead with headline feature
  - Include key metrics (trust score, rule count, etc.)
- [ ] Clear `UNRELEASED.md` (keep `# Unreleased` header only)
- [ ] Update version in relevant files (if any)
- [ ] Review diff before committing

### Commit & Tag
- [ ] `git add CHANGELOG.md UNRELEASED.md`
- [ ] `git commit -m "Release {VERSION}: {HEADLINE}"`
- [ ] `git tag {VERSION}`
- [ ] `git push && git push --tags`

## Changelog Entry Template

```markdown
## [{VERSION}] - {YYYY-MM-DD}

{One-line summary of the release}

### Added
- **{Theme}**: {Summary of what was added}

### Changed
- **{Theme}**: {Summary of what changed}

### Fixed
- **{Theme}**: {Summary of what was fixed}

### Metrics
- Trust Score: {X}%
- Evidence Coverage: {Y}% core, {Z}% experimental
- Rules: {N} total ({P} passing)
```

## Result

**Version tagged:** ☐ YES ☐ NO
**Pushed:** ☐ YES ☐ NO

## Run History

| Run | Date | Version | Notes |
|-----|------|---------|-------|
| 1   |      |         |       |

## Reset

To re-run: `sed -i 's/\[x\]/[ ]/g' .claude/tasks/create-release.md`

## Notes

_Progress notes written during execution:_