---
id: E1
title: Deterministic Tools for Style
category: efficiency
type: deterministic
checks:
  - id: E1-formatting-in-instructions
    name: Formatting rules in instruction file
    severity: medium
sources:
  - "https://www.anthropic.com/engineering/claude-code-best-practices"
  - "https://code.claude.com/docs/en/hooks-guide"
see_also: [CLAUDE_S4, C2]
---

# Deterministic Tools for Style

Delegate formatting to tools (prettier, eslint), not instructions.

## Pattern

**Good:** "Run `npm run lint` before committing"
**Bad:** "Use 2-space indentation, max 80 chars per line"
