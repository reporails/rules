---
id: C10
title: NEVER with Alternative
category: content
type: deterministic
checks:
  - id: C10-never-no-alternative
    name: NEVER statement without positive alternative
    severity: medium
sources:
  - "https://blog.sshh.io/p/how-i-use-every-claude-code-feature"
  - "https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-4-best-practices"
see_also: [C4, C5]
---

# NEVER with Alternative

NEVER statements include positive alternative after em-dash.

## Pattern

**Good:** "NEVER use var — use const or let instead"
**Bad:** "NEVER use var" (no guidance on what to do)
