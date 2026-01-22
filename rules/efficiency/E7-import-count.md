---
id: E7
title: Import Count
category: efficiency
type: deterministic
detection: Count @imports relative to file line count
level: L3+
scoring: 5
sources: [2]
see_also: [S2]
---

# Import Count

Ensures progressive disclosure scales with file size.

Larger CLAUDE.md files should have proportionally more @imports to offload content.

## Thresholds

| File Size | Minimum @imports |
|-----------|------------------|
| < 50 lines | 0 |
| 50-100 lines | 1 |
| 100-150 lines | 2 |
| > 150 lines | 3+ |
