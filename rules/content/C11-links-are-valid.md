---
id: C11
title: Links Are Valid
category: content
type: deterministic
detection: Regex extract links, check file exists
level: L3+
sources: [2]
antipatterns:
  - id: A17
    name: Broken file references
    severity: high
---

# Links Are Valid

Prevents broken @imports and dead references.

All file references and @imports must point to existing files.

## Pattern

**Good:** Valid reference
- "See @docs/api.md for API documentation"

**Bad:** Broken link
- Reference to non-existent file
