---
id: G6
title: Component-Contract Binding
category: governance
type: deterministic
checks:
  - id: G6-component-no-binding
    name: Component definition lacks contracts/rules/tests
    severity: medium
sources:
  - "docs/capability-levels.md"
see_also: [G5, G7]
---

# Component-Contract Binding

Component definitions have contracts/rules/tests keys.

## Pattern

**Good:** Component with contracts:, rules:, tests: keys
**Bad:** Component definition with only path
