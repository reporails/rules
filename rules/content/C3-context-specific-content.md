---
id: C3
title: Context-Specific Content
category: content
type: semantic
detection: Requires AI to determine what content belongs in root vs imports
level: L3+
scoring: 10
sources: [2, 15]
antipatterns:
  - id: A6
    name: Context-specific content in root file
    severity: high
    points: -15
---

# Context-Specific Content

Improves relevance and reduces noise.

Instructions that apply only to specific files or domains should live in @imports or .claude/rules/, not in the root file.
