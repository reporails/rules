---
id: "CODEX:S:0003"
slug: instruction-size-within-32kib
title: Instruction Size Within 32 KiB
category: structure
type: mechanical
level: L2
backed_by:
- codex-agent-loop
- codex-agents-md
targets: '{{instruction_files}}'
checks:
- id: "CODEX:S:0003:check:0001"
  type: mechanical
  check: aggregate_byte_size
  args:
    pattern: "**/AGENTS.md"
    max: 32768
  severity: high
question: "Does the combined size of AGENTS.md files in any directory chain stay within
  32 KiB?"
criteria:
- The sum of byte sizes for all AGENTS.md files from root to any leaf directory 
  is at most 32768 bytes
- Empty AGENTS.md files are excluded from the size calculation
- The check evaluates all possible directory paths, not just the current working
  directory
- Override files (AGENTS.override.md) replace their AGENTS.md counterpart in the
  size calculation
---

# Instruction Size Within 32 KiB

The combined size of all AGENTS.md files in the directory chain must not exceed 32 KiB.

## Pass / Fail

**Pass:** The repository has AGENTS.md at the root (8 KiB), packages/AGENTS.md (4 KiB), and
packages/api/AGENTS.md (6 KiB). Combined size is 18 KiB, well under the 32 KiB limit.
All files are fully loaded by Codex.
**Fail:** The repository has AGENTS.md at the root (20 KiB) and packages/api/AGENTS.md (15 KiB).
Combined size is 35 KiB, exceeding the 32 KiB budget. The api-specific AGENTS.md is
partially loaded or skipped, losing the most contextually relevant instructions.

## Limitations

This check computes the worst-case directory chain (root to deepest leaf with an AGENTS.md).
Actual budget consumption depends on the specific working directory path at runtime, which
varies per task. The check flags any chain that could exceed the budget. The 32 KiB default
can be changed via configuration, but this rule uses the default value. Empty files are
excluded from the size calculation per Codex behavior.
