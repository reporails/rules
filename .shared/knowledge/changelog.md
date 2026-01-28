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

**Categories:** STRUCTURE, SKILLS, TASKS, WORKFLOWS, KNOWLEDGE, SCHEMA, RULES, SOURCES, DOCS, META, QA

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
- [REPORTING]: Trust Score with Evidence Coverage breakdown (81% official, 19% methodology)
```

**Bad:**
```markdown
- Added file .shared/workflows/rule-creation.md
- Added file .shared/workflows/rule-validation.md
- Added file .shared/workflows/evidence-audit.md
- Changed evidence-chain.md
```

## Creating a Release

Use task: `.claude/tasks/create-release.md`

**Process:**
1. Review `UNRELEASED.md`
2. Group similar changes by theme
3. Write release summary for `CHANGELOG.md`
4. Include key metrics (trust score, rule count, etc.)
5. Clear `UNRELEASED.md` (keep header)
6. Commit, tag, push

**Release entry template:**

```markdown
## [vX.Y.Z] - YYYY-MM-DD

One-line summary of the release.

### Added
- **Theme**: Summary

### Changed
- **Theme**: Summary

### Fixed
- **Theme**: Summary

### Metrics
- Trust Score: X%
- Evidence Coverage: Y% official, Z% methodology
- Rules: N total (P passing)
```

## Tagging

```bash
git tag vX.Y.Z
git push origin vX.Y.Z
```

Tag format: `v` prefix + [SemVer](https://semver.org/) (e.g., `v0.1.0`)

GitHub Actions (`.github/workflows/release.yml`) triggers on `v*` tags.

## Version Numbering

| Change Type | Bump | Example |
|-------------|------|---------|
| Breaking changes | Major | v1.0.0 → v2.0.0 |
| New features (backwards compatible) | Minor | v0.1.0 → v0.2.0 |
| Bug fixes | Patch | v0.1.0 → v0.1.1 |

Pre-1.0: Minor bumps for features, patch for fixes. Breaking changes OK.