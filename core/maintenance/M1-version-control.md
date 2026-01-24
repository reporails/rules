---
id: M1
title: Version Control
category: maintenance
type: deterministic
checks:
  - id: M1-not-tracked
    name: Instruction file not in git
    severity: high
sources:
  - "https://www.anthropic.com/engineering/claude-code-best-practices"
see_also: [M2, C12]
---

# Version Control

Instruction files are git-tracked for change history.

## Pattern

**Good:** CLAUDE.md committed and tracked in git
**Bad:** Instruction file in .gitignore
