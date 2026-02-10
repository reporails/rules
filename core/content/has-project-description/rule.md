---
id: "CORE:C:0001"
slug: has-project-description
title: Has Project Description
category: content
type: deterministic
level: L1
backed_by:
- claude-md-guide
- instruction-limits-principles
- spec-writing-for-agents
targets: '{{instruction_files}}'
checks:
- id: "CORE:C:0001:check:0001"
  type: deterministic
  severity: critical
question: "Does the instruction file contain a project description near the top?"
criteria:
- The first or second section after the title heading contains prose describing 
  the project
- The description includes at least one sentence about what the project is or 
  does
- The description appears before any commands, constraints, or configuration 
  sections
---

# Has Project Description

The main instruction file must contain a project description within the first two sections
after the title heading.

## Pass / Fail

**Pass:** CLAUDE.md starts with:
```
# MyProject
A REST API for inventory management built with FastAPI and PostgreSQL.
```
The project description immediately follows the title, giving the agent enough context
to understand what the codebase does.
**Fail:** CLAUDE.md starts with:
```
# CLAUDE.md

## Commands
npm run build
npm run test
```
Jumps straight to commands with no description of what the project is or does.

## Limitations

Cannot evaluate whether the description is accurate or sufficiently detailed for the
project's complexity. A one-word description like "A server" would pass the structural
check despite being nearly useless. Does not verify the description matches the actual
codebase contents.
