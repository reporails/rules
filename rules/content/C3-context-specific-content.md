---
id: C3
title: Context-Specific Content
category: content
type: heuristic
detection: pattern-regex for domain keywords (api/, tests/, components/) in root CLAUDE.md
question: Does the root file contain context-specific content that belongs in @imports?
criteria: Pass if root is general; fail if contains domain-specific rules (>5 lines about specific paths)
level: L3+
sources: [2, 15]
antipatterns:
  - id: A6
    name: Context-specific content in root file
    severity: high
---

# Context-Specific Content

Improves relevance and reduces noise.

Instructions that apply only to specific files or domains should live in @imports or .claude/rules/, not in the root file.
