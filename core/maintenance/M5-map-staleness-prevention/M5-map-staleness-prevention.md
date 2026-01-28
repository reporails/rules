---
id: M5
title: Map Staleness Prevention
category: maintenance
type: deterministic
confidence: low
backed_by:
  - source: capability-levels
    claim: l6-staleness
checks:
  - id: M5-stale-path
    name: Path in backbone.yml may not exist
    severity: high
sources:
  - "docs/capability-levels.md"
see_also: [S4, C11]
---

# Map Staleness Prevention

Paths in backbone.yml exist on filesystem.

## Pattern

**Good:** All paths in backbone.yml resolve to files
**Bad:** backbone.yml references deleted directories
