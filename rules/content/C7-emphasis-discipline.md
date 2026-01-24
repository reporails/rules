---
id: C7
title: Emphasis Discipline
category: content
type: deterministic
detection: pattern-regex count for IMPORTANT|CRITICAL (threshold: ≤5 per file)
level: L2+
sources: [1, 8]
antipatterns:
  - id: A9
    name: Everything emphasized
    severity: high
---

# Emphasis Discipline

Ensures critical rules stand out.

When everything is emphasized, nothing stands out.

## Guidelines

- Maximum 3-5 IMPORTANT/CRITICAL items per file
- Reserve emphasis for truly critical constraints
- Use regular formatting for standard rules
