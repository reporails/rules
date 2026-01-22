---
id: M5
title: Auto-Generated Content Review
category: maintenance
type: semantic
detection: Requires understanding if content was customized vs left as-is
level: L2+
sources: [1, 7]
antipatterns:
  - id: A1
    name: Auto-generated without review
    severity: critical
    points: -25
---

# Auto-Generated Content Review

Removes incorrect/irrelevant auto-detected information.

The `/init` command generates content that is often:
- Wrong (detects patterns that don't apply)
- Redundant (states obvious information)
- Missing (doesn't know your actual constraints)

Review and customize within 30 minutes of generation.
