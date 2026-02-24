---
name: add-changelog-entry
description: Add a changelog entry to UNRELEASED.md
---

# /add-changelog-entry

Automatically add a changelog entry to PROJECT_ROOT/UNRELEASED.md.

## Process

1. Check git diff or recent file modifications
2. Determine the area from the file path:
   - core/**/rule.md → [RULES]
   - registry/ → [REGISTRY]
   - schemas/ → [SCHEMAS]
   - agents/ → [AGENTS]
   - docs/ → [DOCS]
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

- [RULES] – Rule definitions (structure, content, efficiency, maintenance, governance)
- [REGISTRY] – Capabilities, levels, coordinate map, tombstones
- [SCHEMAS] – Schema definitions
- [AGENTS] – Agent configurations and agent-specific rules
- [DOCS] – Documentation
- [META] – CLAUDE.md, backbone.yml, repo structure

## Example

```markdown
### Added
- [RULES]: CORE:G:0001 rule for governance policy validation
- [REGISTRY]: Added new capability to L4

### Changed
- [SCHEMAS]: Updated rule schema to v0.1.0
```

Do not ask for confirmation. Just do it.