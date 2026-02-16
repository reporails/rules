---
id: CORE:C:0005
slug: boundary-constraints
title: Explicit Boundary Constraints
category: content
type: deterministic
level: L2
backed_by:
- claude-code-issue-13579
- copilot-cli-best-practices
- spec-writing-for-agents
targets: '{{instruction_files}}'
checks:
- id: CORE.C.0005.file-exists
  type: mechanical
  severity: medium
  name: file-exists
  check: file_exists
- id: CORE.C.0005.has-required-sections
  type: deterministic
  severity: medium
  name: has-required-sections
- id: CORE.C.0005.no-anti-sections
  type: deterministic
  severity: medium
  name: no-anti-sections
---

# Explicit Boundary Constraints

Root instruction files SHOULD include explicit boundary constraints specifying files, directories, or actions the agent must avoid or seek approval for

## Pass / Fail

### Pass

~~~~markdown
## Boundaries

- NEVER commit .env files or API keys
- NEVER modify vendor/ or node_modules/
- ASK before changing database migrations or CI config
- ALWAYS run tests before committing
~~~~

### Fail

~~~~markdown
## Guidelines

- Use TypeScript
- Write tests
- Follow the style guide

(No mention of what the agent should avoid or what requires approval)
~~~~

## Limitations

Checks for prohibition language patterns (never, must not, do not, avoid) but cannot verify the constraints are complete or appropriate for the project. A file discussing boundaries conceptually without applying them would pass incorrectly.
