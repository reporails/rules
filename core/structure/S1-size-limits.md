---
id: S1
title: Size Limits
category: structure
type: deterministic
checks:
  - id: S1-root-too-long
    name: Root instruction file exceeds 200 lines
    severity: critical
sources:
  - "https://www.anthropic.com/engineering/claude-code-best-practices"
  - "https://www.humanlayer.dev/blog/writing-a-good-claude-md"
  - "docs/methodology-thresholds.md"
see_also: [S2]
---

# Size Limits

Prevents instruction degradation from token bloat.

## Pattern

**Good:** Root file under 100 lines with @imports for details
**Bad:** 300-line monolithic instruction file
