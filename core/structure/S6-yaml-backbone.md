---
id: S6
title: YAML Backbone
category: structure
type: deterministic
checks:
  - id: S6-backbone-no-maps
    name: Backbone missing 'maps:' section
    severity: critical
  - id: S6-backbone-no-contracts
    name: Backbone missing 'contracts:' section
    severity: high
  - id: S6-backbone-no-quick-ref
    name: Backbone missing 'quick_ref:' section
    severity: high
  - id: S6-maps-no-components
    name: Maps section missing 'components:' key
    severity: high
  - id: S6-maps-no-platform
    name: Maps section missing 'platform:' key
    severity: low
  - id: S6-empty-backbone
    name: Backbone file appears empty or minimal
    severity: critical
sources:
  - "docs/capability-levels.md"
see_also: [E2, G5, M6]
---

# YAML Backbone

L6 projects require `.reporails/backbone.yml` with complete navigation structure.

## Pattern

**Good:** backbone.yml with maps (components, platform), contracts, and quick_ref sections
**Bad:** Missing or incomplete backbone structure

## Required Sections

- `maps:` — Navigation maps for codebase (required)
  - `components:` — Component location index
  - `platform:` — Platform/infrastructure paths
- `contracts:` — Contract registry for architecture enforcement
- `quick_ref:` — Quick reference for common operations
