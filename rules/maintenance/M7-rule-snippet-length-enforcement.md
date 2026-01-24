---
id: M7
title: Rule Snippet Length Enforcement
category: maintenance
type: deterministic
detection: Line count per file in CI
level: L4+
sources: [1]
see_also: [S1]
antipatterns:
  - id: A14
    name: Rule snippets > 40 lines
    severity: medium
---

# Rule Snippet Length Enforcement

Prevents instruction dilution from bloated rules.

## CI Validation

1. Count lines in `.claude/rules/*.md`
2. Warn if > 40 lines
3. Fail if > 60 lines
