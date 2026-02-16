---
id: CODEX:S:0001
slug: combined-instruction-size-limit
title: Combined Instruction File Size Limit
category: structure
type: mechanical
level: L1
backed_by:
- codex-agent-loop
- codex-agents-md
targets: '{{instruction_files}}'
checks:
- id: CODEX.S.0001.file-exists
  type: mechanical
  severity: high
  name: file-exists
  check: file_exists
---

# Combined Instruction File Size Limit

Codex projects MUST keep the combined size of all discovered instruction files (AGENTS.md from global to cwd) under 32 KiB, because Codex stops reading once this threshold is reached

## Pass / Fail

### Pass

~~~~markdown
Total instruction file size across all discovered AGENTS.md files: 18 KiB (well under 32 KiB limit)
~~~~

### Fail

~~~~markdown
Total instruction file size across all discovered AGENTS.md files: 45 KiB (exceeds 32 KiB limit — Codex will truncate content, potentially dropping critical instructions)
~~~~

## Limitations

Can only measure file size; cannot predict which files Codex will discover in a given execution context (depends on working directory). The 32 KiB limit may change in future Codex versions.
