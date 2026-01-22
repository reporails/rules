---
id: C1
title: Core Sections
category: content
type: heuristic
detection: Section heading grep; cannot verify content quality
level: L2+
scoring: 10
sources: [1, 6, 11]
see_also: [E1]
---

# Core Sections

Ensures minimum viable instruction set.

## Required Sections

| Section | Required | Description |
|---------|----------|-------------|
| Project Context | Yes | One-liner describing the project |
| Tech Stack | Yes | Versions and key technologies |
| Commands | Yes | Build, test, lint, deploy |
| Architecture | Recommended | Key directories and patterns |
| Constraints | Yes | Critical rules and warnings |
| Code Style | No | Defer to linters/hooks |
