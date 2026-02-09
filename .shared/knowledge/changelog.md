# Changelog

How to maintain the changelog and create releases.

## Format

[Keep a Changelog](https://keepachangelog.com/) with project-specific conventions.

## Files

| File | Purpose |
|------|---------|
| `UNRELEASED.md` | Accumulates changes during development |
| `CHANGELOG.md` | Released versions (moved from UNRELEASED) |

## Adding Entries

Add to `UNRELEASED.md` as you work:

```markdown
### Added
- [CATEGORY]: Brief description of what was added

### Changed
- [CATEGORY]: Brief description of what changed

### Fixed
- [CATEGORY]: Brief description of what was fixed

### Removed
- [CATEGORY]: Brief description of what was removed
```

**Areas:** RULES, L1-L6, DOCS, META

## Writing Good Entries

**Do:**
- Group by theme, not by file
- Lead with what matters to users
- Include metrics where relevant
- Be specific but concise

**Don't:**
- List every file changed
- Use commit-message style entries
- Bury important changes in lists

**Good:**
```markdown
- [STRUCTURE]: Introduced `.shared/` for agent-agnostic workflows and knowledge
- [REPORTING]: Schema validation with rule count breakdown
```

**Bad:**
```markdown
- Added file .shared/workflows/rule-creation.md
- Added file .shared/workflows/rule-validation.md
- Added file .shared/workflows/rule-update.md
- Changed qa-checklist.md
```

## Creating a Release

Use task: `.claude/tasks/create-release.md`

**Process:**
1. Review `UNRELEASED.md`
2. Group similar changes by theme
3. Write release summary for `CHANGELOG.md`
4. Include key metrics (rule count, schema version, etc.)
5. Clear `UNRELEASED.md` (keep header)
6. Commit, tag, push

**Release entry template:**

```markdown
## [X.Y.Z] - YYYY-MM-DD

One-line summary of the release.

### Added
- **Theme**: Summary

### Changed
- **Theme**: Summary

### Fixed
- **Theme**: Summary

### Metrics
- Rules: N total (P passing)
- Schema version: X
```

## Releasing

Release is automated via GitHub Actions:

1. Create a release branch named `X.Y.Z` (e.g., `0.3.0`)
2. Update version in `README.md` and finalize `UNRELEASED.md`
3. Merge to `main` — the release workflow detects the version-branch merge
4. CI runs the Docker test harness as a QA gate
5. On pass: tag is created, tarball is built, GitHub release is published

Tag format: [SemVer](https://semver.org/) (e.g., `0.3.0`)

See `.github/workflows/release.yml` for the full pipeline.

## Version Numbering

| Change Type | Bump | Example |
|-------------|------|---------|
| Breaking changes | Major | 1.0.0 → 2.0.0 |
| New features (backwards compatible) | Minor | 0.1.0 → 0.2.0 |
| Bug fixes | Patch | 0.1.0 → 0.1.1 |

Pre-1.0: Minor bumps for features, patch for fixes. Breaking changes OK.