---
id: "CORE:C:0005"
slug: has-boundaries
title: Has Boundaries
category: content
type: deterministic
level: L2
backed_by:
- claude-code-settings
- osmani-ai-coding-workflow
- spec-writing-for-agents
targets: '{{instruction_files}}'
checks:
- id: "CORE:C:0005:check:0001"
  type: deterministic
  negate: true
  severity: high
question: "Do the instruction files define boundaries or prohibitions for the agent?"
criteria:
- At least one instruction file contains explicit prohibitions or off-limits 
  declarations
- Boundaries use imperative language (never, must not, do not) or equivalent 
  constraint syntax
- At least one boundary addresses files, directories, or operations the agent 
  must avoid
---

# Has Boundaries

The instruction files must define boundaries specifying what the agent should never do
or never touch.

## Pass / Fail

**Pass:** The instruction file contains:
```
## Constraints
- NEVER modify files in vendor/ or node_modules/
- NEVER push directly to main
- NEVER commit .env files or credentials
- Ask before deleting any file
```
Clear prohibitions that prevent the agent from causing damage.
**Fail:** The instruction file documents commands and project structure but includes no constraints,
prohibitions, or off-limits areas. The agent has no guardrails preventing it from modifying
generated code, pushing to production branches, or touching sensitive configuration.

## Limitations

Cannot verify that boundaries are comprehensive enough for the project's risk profile.
A project with database access that only restricts file modifications would pass despite
missing critical operational boundaries. Cannot detect boundaries that are too restrictive
and would prevent the agent from doing useful work.
