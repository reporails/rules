---
id: M6
title: Map Staleness Prevention
category: maintenance
type: deterministic
detection: Path existence validation in CI
level: L6
sources: [25]
see_also: [S6]
antipatterns:
  - id: A11
    name: Stale navigation maps
    severity: medium
    points: -10
---

# Map Staleness Prevention

Ensures navigation maps remain accurate.

## CI Validation

1. Extract paths from backbone.yml
2. Check each path exists on filesystem
3. Fail build if any missing
