---
id: CORE:C:0003
slug: project-architecture-documentation
title: Project Architecture Documentation
category: content
type: deterministic
level: L1
backed_by:
- agents-md-spec
- copilot-cli-best-practices
- instruction-limits-principles
targets: '{{instruction_files}}'
checks:
- id: CORE.C.0003.file-exists
  type: mechanical
  severity: medium
  name: file-exists
  check: file_exists
- id: CORE.C.0003.has-required-sections
  type: deterministic
  severity: medium
  name: has-required-sections
- id: CORE.C.0003.no-anti-sections
  type: deterministic
  severity: medium
  name: no-anti-sections
---

# Project Architecture Documentation

Root instruction files SHOULD describe the project's directory structure and major architectural components so agents know where to find and place code

## Pass / Fail

### Pass

~~~~markdown
## Architecture

- `src/` — application source code
- `src/api/` — REST endpoints (Express)
- `src/models/` — Prisma schema and DB access
- `src/components/` — React components
- `tests/` — unit and integration tests
- `docs/` — architecture decisions and API docs

The API layer calls models directly; no service layer.
~~~~

### Fail

~~~~markdown
## Project

This is a standard web application with frontend and backend components.
~~~~

## Limitations

Cannot verify directory paths actually exist. Cannot assess whether the description is complete relative to the actual project structure. Detects section presence, not accuracy.
