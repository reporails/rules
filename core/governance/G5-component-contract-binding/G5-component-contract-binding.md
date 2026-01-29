---
id: G5
title: Component-Contract Binding
category: governance
type: deterministic
backed_by: []
checks:
  - id: G5-component-no-binding
    name: Component definition lacks contracts/rules/tests
    severity: medium
sources: []
see_also: [G4, G6]
---

# Component-Contract Binding

Component definitions have contracts/rules/tests keys.

## Pattern

**Good:** Component with contracts:, rules:, tests: keys
**Bad:** Component definition with only path
