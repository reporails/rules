---
id: S4
title: YAML Backbone
category: structure
type: deterministic
backed_by: []  # Tier: experimental (community pattern, L6-only)
checks:
  - id: S4-backbone-no-maps
    name: Backbone missing 'maps:' section
    severity: critical
  - id: S4-backbone-no-contracts
    name: Backbone missing 'contracts:' section
    severity: high
  - id: S4-backbone-no-quick-ref
    name: Backbone missing 'quick_ref:' section
    severity: high
  - id: S4-maps-no-components
    name: Maps section missing 'components:' key
    severity: high
  - id: S4-maps-no-platform
    name: Maps section missing 'platform:' key
    severity: low
  - id: S4-empty-backbone
    name: Backbone file appears empty or minimal
    severity: critical
sources: []
see_also: [E2, G4, M5]
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
