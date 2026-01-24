---
id: S1
title: Size Limits
category: structure
type: deterministic
detection: Line count, depth counting
level: L2+
antipatterns:
  - id: A3
    name: Root file > 200 lines
    severity: critical
sources: [1, 10, 11]
see_also: [M7, C1]
---

# Size Limits

Prevents instruction degradation from token bloat.

## Thresholds

| Metric | Target | Warning | Critical |
|--------|--------|---------|----------|
| Root CLAUDE.md lines | < 100 | 100-200 | > 200 |
| Rule snippet lines | < 40 | 40-60 | > 60 |
| Total instruction count | < 50 | 50-100 | > 100 |
| Import depth | ≤ 2 | 3 | > 3 |

## Section Requirements

Files under 100 lines are exempt from C1 (Core Sections) structure requirement. Small files can use any organization that fits the content.

## Rationale

Frontier LLMs can follow ~150-200 instructions with reasonable consistency [11]. Claude Code's system prompt already contains ~50 instructions, leaving ~100-150 for your CLAUDE.md.

## Pattern

**Good:** Root file under 100 lines with @imports
**Bad:** 300-line monolithic CLAUDE.md
