---
id: C1
title: Core Sections
category: content
type: heuristic
detection: pattern-regex for section headings in files ≥ 100 lines
question: Does this file contain the required core sections?
criteria: Pass if has Project Context, Tech Stack, Commands, Constraints; fail if missing required sections
level: L2+
sources: [1, 6, 11]
see_also: [E1, S1]
---

# Core Sections

Ensures minimum viable instruction set.

**Note:** Files under 100 lines are exempt from this rule (see S1).

## Required Sections

| Section | Required | Description |
|---------|----------|-------------|
| Project Context | Yes | One-liner describing the project |
| Tech Stack | Yes | Versions and key technologies |
| Commands | Yes | Build, test, lint, deploy |
| Architecture | Recommended | Key directories and patterns |
| Constraints | Yes | Critical rules and warnings |
| Code Style | No | Defer to linters/hooks |
