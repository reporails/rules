---
id: CLAUDE_S5
title: Path-Scoped Rules
category: structure
type: deterministic
confidence: high
backed_by:
  - source: claude-code-memory
    claim: path-scoped-rules
  - source: claude-code-settings
    claim: rules-dir-config
checks:
  - id: CLAUDE_S5-no-paths-frontmatter
    name: Rule file missing paths key in frontmatter
    severity: medium
sources:
  - "https://code.claude.com/docs/en/settings"
  - "https://claudefa.st/blog/guide/mechanics/rules-directory"
see_also: [CLAUDE_S4, S2]
---

# Path-Scoped Rules

Rule files use YAML frontmatter with `paths:` for scoped loading.

## Pattern

**Good:** Frontmatter with `paths: ["src/api/**"]`
**Bad:** Rule file with no path scoping
