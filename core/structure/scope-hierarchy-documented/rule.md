---
id: "CORE:S:0008"
slug: scope-hierarchy-documented
title: Scope Hierarchy Documented
category: structure
type: deterministic
level: L4
backed_by:
- claude-code-memory
- claude-code-settings
- codex-agent-loop
targets: '{{instruction_files}}'
checks:
- id: "CORE:S:0008:check:0001"
  type: deterministic
  negate: true
  severity: medium
question: "Do the instruction files document or reference the scope precedence hierarchy?"
criteria:
- At least one instruction file contains a section or paragraph describing scope
  precedence
- The documentation mentions override behavior (more specific overrides broader)
- Keywords indicating hierarchy are present (e.g., precedence, override, 
  hierarchy, scope, priority)
- The hierarchy documentation appears in a structurally prominent location 
  (heading or dedicated section)
---

# Scope Hierarchy Documented

Instruction files in a multi-file system must document or respect the scope precedence hierarchy.

## Pass / Fail

**Pass:** A CLAUDE.md file contains a section titled "## Instruction Hierarchy" or
"## Scope Precedence" that explains: "Project-level rules in .claude/rules/
override general guidance in this file. Local overrides in CLAUDE.local.md
take highest precedence." The hierarchy is explicitly stated.
**Fail:** A project has CLAUDE.md, three .claude/rules/ files, and nested CLAUDE.md
files in subdirectories. None of the files mention which takes precedence.
A rule in .claude/rules/style.md contradicts guidance in the root CLAUDE.md,
and there is no documentation of which instruction wins.

## Limitations

Pattern-based detection can only check for the presence of hierarchy-related
keywords and section headings. Cannot verify that the documented hierarchy
is correct or matches the agent runtime's actual precedence behavior. A file
that mentions "precedence" in an unrelated context may produce a false positive.
