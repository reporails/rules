---
id: G6
title: Architecture Tests
category: governance
type: deterministic
backed_by: []
checks:
  - id: G6-no-arch-tests
    name: No architecture test files found
    severity: medium
sources: []
see_also: [G5, G7]
---

# Architecture Tests

Test files exist and CI integration present.

## Pattern

**Good:** tests/architecture/*.test.ts with CI workflow
**Bad:** No automated architecture enforcement
