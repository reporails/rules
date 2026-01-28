---
id: G6
title: Architecture Tests
category: governance
type: deterministic
confidence: low
backed_by:
  - source: capability-levels
    claim: l6-arch-tests
checks:
  - id: G6-no-arch-tests
    name: No architecture test files found
    severity: medium
sources:
  - "docs/capability-levels.md"
see_also: [G5, G7]
---

# Architecture Tests

Test files exist and CI integration present.

## Pattern

**Good:** tests/architecture/*.test.ts with CI workflow
**Bad:** No automated architecture enforcement
