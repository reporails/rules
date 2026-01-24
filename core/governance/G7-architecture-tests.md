---
id: G7
title: Architecture Tests
category: governance
type: deterministic
checks:
  - id: G7-no-arch-tests
    name: No architecture test files found
    severity: medium
sources:
  - "docs/capability-levels.md"
see_also: [G6, G8]
---

# Architecture Tests

Test files exist and CI integration present.

## Pattern

**Good:** tests/architecture/*.test.ts with CI workflow
**Bad:** No automated architecture enforcement
