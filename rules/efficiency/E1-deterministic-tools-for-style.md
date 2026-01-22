---
id: E1
title: Deterministic Tools for Style
category: efficiency
type: heuristic
detection: Grep for indentation/style patterns; may have false positives
level: L3+
scoring: 5
sources: [3, 1]
see_also: [C1]
antipatterns:
  - id: A2
    name: Code style enforcement rules
    severity: critical
    points: -25
---

# Deterministic Tools for Style

Eliminates style enforcement rules from CLAUDE.md.

Code formatting **enforcement** belongs in tools (Prettier, ESLint, Black), not instructions. Style **guidance** (patterns, conventions) is acceptable.

## Pattern

**Good:** Delegate enforcement to tools
- "Code formatting handled by Prettier via pre-commit hooks"
- "Run `npm run lint:fix` to auto-fix issues"

**Good:** Style guidance (acceptable)
- "Prefer named exports over default exports"
- "Use descriptive variable names that indicate purpose"

**Bad:** Making Claude the linter
- "Use 2 spaces for indentation"
- "Max line length 100 characters"
