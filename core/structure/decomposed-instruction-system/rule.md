---
id: "CORE:S:0007"
slug: decomposed-instruction-system
title: Decomposed Instruction System
category: structure
type: mechanical
level: L3
backed_by:
- claude-md-guide
- dometrain-claude-md-guide
- instruction-limits-principles
- using-claude-md-files
targets: '{{instruction_files}}'
checks:
- id: "CORE:S:0007:check:0001"
  type: mechanical
  check: file_count
  args:
    pattern: "{{instruction_files}}"
    min: 2
  severity: medium
question: "Does the instruction system consist of at least two files?"
criteria:
- At least two files exist in the instruction system (main file + at least one 
  supplementary)
- Files are counted from the combined instruction_files template variable 
  resolution
- Both the main instruction file and supplementary files contribute to the count
---

# Decomposed Instruction System

The instruction system must consist of at least two files.

## Pass / Fail

**Pass:** A project has CLAUDE.md at the root containing high-level project guidance
and a .claude/rules/testing.md file with detailed testing instructions.
The instruction system consists of 2 files, meeting the minimum threshold.
**Fail:** A project has only a single CLAUDE.md file at the root. All instructions —
project description, coding standards, testing procedures, deployment notes —
are packed into one 280-line file. No supplementary files, no .claude/rules/
directory, no imported content.

## Limitations

Checks file count only, not whether decomposition is meaningful. A project
with CLAUDE.md and a trivially small .claude/rules/placeholder.md technically
passes but has not genuinely decomposed its instruction system. Cannot assess
whether the decomposition follows a logical separation of concerns.
