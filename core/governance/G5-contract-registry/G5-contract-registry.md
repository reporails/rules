---
id: G5
title: Contract Registry
category: governance
type: deterministic
confidence: low
backed_by:
  - source: capability-levels
    claim: l6-contracts
checks:
  - id: G5-no-contracts
    name: Backbone lacks contracts key
    severity: medium
sources:
  - "docs/capability-levels.md"
see_also: [S6, G6]
---

# Contract Registry

L6 backbone.yml has quick_ref and contracts keys.

## Pattern

**Good:** backbone.yml with contracts: section listing interfaces
**Bad:** backbone.yml with no contract definitions
