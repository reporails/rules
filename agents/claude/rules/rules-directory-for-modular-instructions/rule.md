---
id: CLAUDE:S:0001
slug: rules-directory-for-modular-instructions
title: Rules Directory for Modular Instructions
category: structure
type: mechanical
level: L2
backed_by:
- claude-code-memory
- claude-md-guide
- rules-directory-mechanics
targets: '{{main_instruction_file}}'
checks:
- id: CLAUDE.S.0001.file-exists
  type: mechanical
  severity: medium
  name: file-exists
  check: file_exists
---

# Rules Directory for Modular Instructions

Claude Code projects SHOULD use .claude/rules/ directory with separate files per concern rather than a monolithic CLAUDE.md when the project has multiple distinct instruction domains

## Pass / Fail

### Pass

~~~~markdown
A project with:
  CLAUDE.md (60 lines — core workflow)
  .claude/rules/testing.md
  .claude/rules/security.md
  .claude/rules/api-patterns.md
~~~~

### Fail

~~~~markdown
(File does not exist at expected path)
~~~~

## Limitations

Can check for directory existence and file count but cannot assess whether the project actually has multiple distinct instruction domains. Small projects may legitimately use CLAUDE.md alone.
