---
id: "CORE:S:0006"
slug: total-instruction-budget
title: Total Instruction Budget
category: structure
type: mechanical
level: L2
backed_by:
- codex-agent-loop
- codex-agents-md
- monorepo-claude-md-organization
targets: '{{instruction_files}}'
checks:
- id: "CORE:S:0006:check:0001"
  type: mechanical
  check: aggregate_byte_size
  args:
    pattern: "{{instruction_files}}"
    max: 32768
  severity: high
question: "Does the combined size of all instruction files stay within the instruction
  budget?"
criteria:
- The sum of byte sizes across all instruction files is at most 32,768 bytes (32
  KiB)
- All files resolved from the instruction_files template variable are included 
  in the sum
- The check aggregates across the full instruction file set, not per-file
---

# Total Instruction Budget

The combined size of all instruction files must stay within the agent's instruction budget.

## Pass / Fail

**Pass:** A project has CLAUDE.md (8 KiB), .claude/rules/testing.md (2 KiB), and
.claude/rules/style.md (1.5 KiB). The combined total is 11.5 KiB, well
under the 32 KiB ceiling. Word count is approximately 2,000 words, under
the 10k word ideal.
**Fail:** A monorepo has a root CLAUDE.md (12 KiB), three nested CLAUDE.md files
(6 KiB each), and eight .claude/rules/ files (2 KiB each). The combined
total is 46 KiB, exceeding the 32 KiB Codex limit. The agent silently
stops loading files after the budget is exhausted.

## Limitations

The 32 KiB limit is Codex-specific; Claude Code does not enforce a hard
byte ceiling (though performance degrades). The check uses byte size as the
metric, but actual context consumption depends on tokenization. Cannot
predict which files the agent will drop when the budget is exceeded — that
is runtime-specific behavior.
