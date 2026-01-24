---
name: add-changelog-entry
description: Add a changelog entry to UNRELEASED.md
---

# /add-changelog-entry

Automatically add a changelog entry to PROJECT_ROOT/UNRELEASED.md.

## Instructions

1. Check git diff or recent file modifications
2. Determine the area from the file path:
   - rules/*.md → [RULES]
   - capability-levels.md with L1-L6 changes → [L1]-[L6]
   - README.md → [DOCS]
   - CLAUDE.md, backbone.yml, .claude/, .reporails/ → [META]
3. Determine the category:
   - New files/content → Added
   - Modified existing → Changed
   - Marked as deprecated/obsolete → Deprecated
   - Removed content → Removed
   - Bug fixes → Fixed
   - Security-related changes → Security
4. Write a concise description (3-7 words)
5. Append to UNRELEASED.md under the correct category section
6. Create the category section if it doesn't exist

## Format

```markdown
### [Category]
- [Area]: [Description]
```

## Categories

Added, Changed, Deprecated, Removed, Fixed, Security

## Areas

- [RULES] – Rule definitions (S, C, M, G, E)
- [L1]-[L6] – Level-specific changes
- [DOCS] – README, general documentation
- [META] – CLAUDE.md, backbone.yml, repo structure

## Example

```markdown
### Added
- [RULES]: S5 rule for import depth validation
- [L4]: Added hooks requirement to level definition

### Changed
- [DOCS]: Updated README with CLI link
```

Do not ask for confirmation. Just do it.
