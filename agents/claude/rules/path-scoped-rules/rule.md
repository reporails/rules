---
id: CLAUDE:S:0002
slug: path-scoped-rules
title: Path-Scoped Rules via Frontmatter
category: structure
type: mechanical
level: L3
backed_by:
- claude-code-memory
- claude-md-guide
- rules-directory-mechanics
targets: '{{supplementary_files}}'
checks:
- id: CLAUDE.S.0002.file-exists
  type: mechanical
  severity: medium
  name: file-exists
  check: file_exists
---

# Path-Scoped Rules via Frontmatter

Claude Code .claude/rules/ files that apply only to specific file types or directories SHOULD use YAML frontmatter with a paths field to scope when the rule activates

## Pass / Fail

### Pass

~~~~markdown
---
paths:
  - src/api/**/*.ts
---
# API Development Rules
- Validate all input with Zod
- Return consistent error shape
~~~~

### Fail

~~~~markdown
(File does not exist at expected path)
~~~~

## Limitations

Can only check for frontmatter presence and valid glob syntax. Cannot verify the paths actually match existing project files or that the rule content is truly scoped to those paths.
