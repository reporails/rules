---
id: M3
title: Map Staleness Prevention
category: maintenance
type: deterministic
backed_by: []
checks:
  - id: M3-stale-path
    name: Path in backbone.yml may not exist
    severity: high
    pattern_confidence: low
sources: []
see_also: [C4]
---

# Map Staleness Prevention

Paths in backbone.yml exist on filesystem.

## Pattern

**Good:** All paths in backbone.yml resolve to files
**Bad:** backbone.yml references deleted directories
