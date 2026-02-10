---
id: "CORE:C:0006"
slug: specificity-over-vagueness
title: Specificity Over Vagueness
category: content
type: semantic
level: L2
backed_by:
- claude-code-memory
- spec-writing-for-agents
- using-claude-md-files
targets: '{{instruction_files}}'
checks:
- id: "CORE:C:0006:check:0001"
  type: deterministic
  severity: medium
- id: "CORE:C:0006:check:0002"
  type: semantic
  prompt: "Are the instructions specific and actionable, avoiding vague qualifiers like 'properly', 'well', 'clean'?"
  severity: medium
question: "Are the instructions in the file specific and actionable rather than vague?"
criteria:
- Instructions reference concrete values, paths, commands, or patterns rather 
  than abstract qualities
- Directives are testable -- an observer could determine whether the agent 
  followed them
- The file does not contain platitudes like "write clean code" or "follow best 
  practices" as standalone instructions
---

# Specificity Over Vagueness

Instructions must be specific and actionable rather than vague or generic.

## Pass / Fail

**Pass:** The instruction file contains specific, actionable directives:
```
- Use 2-space indentation for TypeScript files
- Always run `npm test` before committing
- Name database migration files with timestamp prefix: `YYYYMMDD_HHMMSS_description.sql`
- Error responses must use the ApiError class from src/errors.ts
```
Each instruction tells the agent exactly what to do with no ambiguity.
**Fail:** The instruction file contains vague, unactionable guidance:
```
- Write clean code
- Follow best practices
- Format code properly
- Keep things simple
- Use good naming conventions
```
None of these tell the agent what to actually do. "Clean code" and "best practices"
are subjective and produce inconsistent behavior.

## Limitations

Specificity exists on a spectrum. Some instructions are partially specific ("use
meaningful variable names" is more specific than "write clean code" but less specific
than "prefix boolean variables with is/has/should"). The semantic gate must make a
judgment call on borderline cases. Cannot assess whether specific instructions are
correct or appropriate for the project.
