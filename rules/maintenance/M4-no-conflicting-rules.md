---
id: M4
title: No Conflicting Rules
category: maintenance
type: heuristic
detection: Text similarity detection; true conflicts require semantic understanding
level: L3+
scoring: 10
sources: [9]
see_also: [C6]
antipatterns:
  - id: A8
    name: Conflicting rules
    severity: high
    points: -15
---

# No Conflicting Rules

Predictable behavior, no ambiguity.

When rules conflict, Claude's behavior becomes unpredictable.

## Audit Checklist

- Contradictory instructions across files
- Rules that override each other in unexpected ways
- Duplicate instructions with different details
