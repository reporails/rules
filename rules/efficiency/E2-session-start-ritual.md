---
id: E2
title: Session Start Ritual
category: efficiency
type: semantic
detection: Behavioral rule about AI usage patterns
level: L6
sources: [25, 9]
see_also: [S6]
antipatterns:
  - id: A12
    name: Skipping session ritual
    severity: medium
    points: -10
---

# Session Start Ritual

2,000-3,000 tokens saved per session.

## Steps

1. Read `.reporails/backbone.yml` (comprehensive path index)
2. Based on task, read ONE relevant map (platform.yml or components.yml)
3. Only use grep/find when maps don't cover target
