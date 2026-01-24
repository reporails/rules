---
id: S7
title: Clear Markdown Structure
category: structure
type: heuristic
detection: pattern-regex for heading hierarchy gaps (e.g., # followed by ###)
question: Does this file have clear markdown structure with consistent heading hierarchy?
criteria: Pass if headings follow hierarchy (# → ## → ###); fail if levels skipped or content orphaned
level: L3+
sources: [1]
---

# Clear Markdown Structure

Improves parseability and navigation.

## Requirements

- Use headings to organize sections
- Consistent heading hierarchy
- No orphan content outside sections
