---
id: M4
title: No Conflicting Rules
category: maintenance
type: heuristic
detection: Cross-file text similarity for contradictory keywords (MUST vs MUST NOT on same topic)
question: Are there conflicting rules across instruction files?
criteria: Pass if rules are consistent; fail if same topic has contradictory instructions
level: L3+
sources: [9]
see_also: [C6]
antipatterns:
  - id: A8
    name: Conflicting rules
    severity: high
---

# No Conflicting Rules

Predictable behavior, no ambiguity.

When rules conflict, Claude's behavior becomes unpredictable.

## Audit Checklist

- Contradictory instructions across files
- Rules that override each other in unexpected ways
- Duplicate instructions with different details
