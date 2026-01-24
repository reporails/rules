---
id: C4
title: Anti-Pattern Documentation
category: content
type: deterministic
checks:
  - id: C4-no-antipatterns
    name: No NEVER or AVOID statements
    severity: medium
sources:
  - "https://www.anthropic.com/engineering/claude-code-best-practices"
  - "https://blog.sshh.io/p/how-i-use-every-claude-code-feature"
see_also: [C10, C5]
---

# Anti-Pattern Documentation

At least one NEVER/AVOID keyword exists to prevent mistakes.

## Pattern

**Good:** "NEVER commit .env files"
**Bad:** File with no anti-pattern guidance
