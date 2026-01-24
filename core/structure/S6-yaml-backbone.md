---
id: S6
title: YAML Backbone
category: structure
type: deterministic
checks:
  - id: S6-backbone-missing
    name: L6 project missing .reporails/backbone.yml
    severity: critical
  - id: S6-backbone-no-maps
    name: Backbone lacks navigation maps
    severity: high
sources:
  - "docs/capability-levels.md"
see_also: [E2, G5, M6]
---

# YAML Backbone

L6 projects require `.reporails/backbone.yml` with navigation maps.

## Pattern

**Good:** backbone.yml with quick_ref, maps, and contracts keys
**Bad:** Large codebase with no navigation structure
