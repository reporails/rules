---
id: E5
title: Grep Efficiency
category: efficiency
type: deterministic
checks:
  - id: E5-no-grep-guidance
    name: No grep efficiency guidance
    severity: low
sources:
  - "https://github.com/anthropics/claude-code/issues/13579"
see_also: [E3, E4]
---

# Grep Efficiency

Instructions document grep guidelines (files_with_matches, head_limit).

## Pattern

**Good:** "Use files_with_matches mode, limit with head_limit"
**Bad:** No guidance on efficient search patterns
