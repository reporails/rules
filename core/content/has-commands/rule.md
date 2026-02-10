---
id: "CORE:C:0003"
slug: has-commands
title: Has Commands
category: content
type: deterministic
level: L2
backed_by:
- claude-md-optimization-study
- dometrain-claude-md-guide
- instruction-limits-principles
- spec-writing-for-agents
targets: '{{instruction_files}}'
checks:
- id: "CORE:C:0003:check:0001"
  type: deterministic
  negate: true
  severity: high
question: "Do the instruction files include runnable project commands with full syntax?"
criteria:
- At least one instruction file contains executable command strings (not just 
  tool names)
- Commands include flags or parameters where applicable (not bare command names 
  like `npm test`)
- At least two distinct commands are documented
---

# Has Commands

The instruction files must include commonly-used project commands with full invocation
syntax including flags and parameters.

## Pass / Fail

**Pass:** The instruction file contains:
```
## Commands
npm run test -- --coverage
npm run lint -- --fix
docker compose up -d
```
Commands are complete with flags and ready to copy-paste into a terminal.
**Fail:** The instruction file has no commands section. Or it lists tool names without invocation
syntax:
```
We use npm for testing and docker for deployment.
```
The agent cannot execute anything from this.

## Limitations

Cannot verify that documented commands are valid or currently functional. Cannot assess
whether the command set covers the right subset of commonly-used operations versus being
exhaustive or too sparse. Cannot detect commands that are missing critical flags.
