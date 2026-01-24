---
id: M6
title: Map Staleness Prevention
category: maintenance
type: deterministic
checks:
  - id: M6-stale-path
    name: Path in backbone.yml may not exist
    severity: high
sources:
  - "docs/capability-levels.md"
see_also: [S6, C11]
---

# Map Staleness Prevention

Paths in backbone.yml exist on filesystem.

## Pattern

**Good:** All paths in backbone.yml resolve to files
**Bad:** backbone.yml references deleted directories
