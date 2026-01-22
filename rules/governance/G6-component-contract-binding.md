---
id: G6
title: Component-Contract Binding
category: governance
type: heuristic
detection: YAML structure validation; cannot verify bindings are correct
level: L6
sources: [25]
validation: first-party
see_also: [G5]
---

# Component-Contract Binding

Rules load based on what contracts a change affects.

## Component Types

Component types define:
- `contracts` — Which contracts the component uses
- `rules` — Path to component-specific rules
- `tests` — Path to component tests
