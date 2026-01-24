---
id: C6
title: Single Source of Truth
category: content
type: heuristic
detection: Cross-file text similarity check for repeated phrases
question: Is information duplicated or conflicting across instruction files?
criteria: Pass if each concept appears once; fail if same instruction appears in multiple files
level: L3+
sources: [9]
see_also: [M4]
antipatterns:
  - id: A7
    name: Duplicate information
    severity: high
  - id: A8
    name: Conflicting rules
    severity: high
---

# Single Source of Truth

Eliminates conflicting instructions.

Each piece of information should exist in exactly one place.
