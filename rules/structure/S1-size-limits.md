---
id: S1
title: Size Limits
category: structure
type: deterministic
detection: Line count, depth counting
level: L2+
scoring: 10
antipatterns:
  - id: A3
    name: Root file > 200 lines
    severity: critical
    points: -25
sources: [1, 10, 11]
see_also: [M7]
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

## Rationale

Frontier LLMs can follow ~150-200 instructions with reasonable consistency [11]. Claude Code's system prompt already contains ~50 instructions, leaving ~100-150 for your CLAUDE.md. Exceeding this causes instruction degradation where later rules are ignored or inconsistently followed.

## Scoring

- Lines < 100: +10 points
- Lines < 200: +5 points
