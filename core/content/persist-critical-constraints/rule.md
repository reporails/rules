---
id: "CORE:C:0016"
slug: persist-critical-constraints
title: Persist Critical Constraints
category: content
type: semantic
level: L2
backed_by:
- claude-code-issue-13579
- claude-md-optimization-study
targets: '{{instruction_files}}'
checks:
- id: "CORE:C:0016:check:0001"
  type: deterministic
  negate: true
  severity: medium
- id: "CORE:C:0016:check:0002"
  type: semantic
  prompt: "Are critical constraints and important directives persisted in the instruction file rather than only in conversation context?"
  severity: medium
question: "Does this instruction file contain persistent, specific constraints rather
  than relying on session memory for critical rules?"
criteria:
- File contains at least one explicit constraint or prohibition specific to the 
  project
- Constraints are stated as persistent directives (not conditional on session 
  context)
- Critical patterns are documented with enough detail to survive context 
  compaction (include the "why" not just the "what")
---

# Persist Critical Constraints

Critical constraints and recurring correction patterns must be documented in the
instruction files, not left to session memory.

## Pass / Fail

**Pass:** "IMPORTANT: This project uses ESM modules only. Never use require() — it will fail
silently in production. Use `import` / `export` syntax exclusively."
The constraint is persisted in CLAUDE.md where it survives session compaction.
**Fail:** A developer repeatedly tells the agent "don't use require()" in chat messages across
multiple sessions, but the instruction file contains no mention of the ESM-only
constraint. After each compaction, the agent reverts to using require().

## Limitations

Cannot detect what constraints are missing — only evaluates whether the file contains
the kind of persistent, specific constraints described. Cannot compare the instruction
file against chat history to find unpersisted corrections. Cannot distinguish between
a genuinely complete instruction file and one that is missing critical constraints the
author has not yet identified.
