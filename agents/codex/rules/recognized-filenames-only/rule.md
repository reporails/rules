---
id: "CODEX:S:0004"
slug: recognized-filenames-only
title: Recognized Filenames Only
category: structure
type: mechanical
level: L2
backed_by:
- codex-agents-md
targets: '{{instruction_files}}'
checks:
- id: "CODEX:S:0004:check:0001"
  type: mechanical
  check: file_count
  args:
    pattern: "**/INSTRUCTIONS.md"
    max: 0
  severity: medium
question: "Do all instruction-intent files use filenames that Codex recognizes for
  automatic discovery?"
criteria:
- All instruction files are named AGENTS.md or AGENTS.override.md
- No files with instruction content use alternative names that Codex would 
  ignore
- Configured fallback filenames (if any) are on the recognized list
- Files named similarly but incorrectly (agents.md, AGENT.md) are flagged as 
  likely mistakes
---

# Recognized Filenames Only

Codex instruction files must use recognized filenames (AGENTS.md, AGENTS.override.md, or configured fallbacks).

## Pass / Fail

**Pass:** All instruction files are named AGENTS.md or AGENTS.override.md. No files with instruction
content use non-standard names. Codex discovers and loads every intended instruction file.
**Fail:** A directory contains INSTRUCTIONS.md with coding conventions intended for Codex. Because
the filename is not on the recognized list, Codex ignores it entirely. The developer
believes the instructions are active, but they are never loaded.

## Limitations

This check identifies files that appear to contain instruction content but use unrecognized
filenames. Detecting "instruction intent" in non-standard files requires heuristics (e.g.,
files mentioning "Codex", "agent", or "instructions" in their content). Files with
ambiguous purpose may produce false positives. The recognized filename list may change
across Codex versions; this rule uses the documented set as of the backing claims.
