---
id: S3
title: No Embedded Code Snippets
category: structure
type: deterministic
detection: Regexp for markdown code blocks (triple backticks)
level: L2+
antipatterns:
  - id: A4
    name: Embedded code snippets
    severity: critical
    points: -25
sources: [1]
see_also: [E6]
---

# No Embedded Code Snippets

Prevents stale examples, reduces maintenance burden.

Code examples become outdated. Reference actual files instead.

## Pattern

**Good:** Reference actual code
- `See src/api/auth.ts:45 for authentication pattern`

**Acceptable:** Minimal command/config examples (< 10 lines, see E7)
- Single-line command syntax
- Short config snippets that won't change

**Bad:** Embedded snippet
- Code block with function definition that may become outdated
