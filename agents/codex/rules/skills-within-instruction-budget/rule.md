---
id: "CODEX:S:0007"
slug: skills-within-instruction-budget
title: Skills Within Instruction Budget
category: structure
type: mechanical
level: L6
backed_by:
- codex-agent-loop
targets: '{{instruction_files}}'
checks:
- id: "CODEX:S:0007:check:0001"
  type: mechanical
  check: aggregate_byte_size
  args:
    pattern: "**/AGENTS.md"
    max: 32768
  severity: medium
question: "Does the combined size of AGENTS.md files and configured skill content
  fit within the 32 KiB budget?"
criteria:
- The sum of all AGENTS.md file sizes plus skill content sizes does not exceed 
  32768 bytes
- Skill content includes preamble, metadata, and usage text as injected by Codex
- The calculation uses the worst-case directory chain for AGENTS.md sizing
- Empty AGENTS.md files and unconfigured skills are excluded from the 
  calculation
---

# Skills Within Instruction Budget

The combined size of AGENTS.md files plus configured skill content must not exceed the 32 KiB instruction budget.

## Pass / Fail

**Pass:** AGENTS.md files total 12 KiB. Three configured skills contribute 6 KiB of preamble,
metadata, and usage text. The combined total is 18 KiB, within the 32 KiB budget. All
instructions and skill definitions are fully loaded.
**Fail:** AGENTS.md files total 24 KiB. Four configured skills contribute 12 KiB. The combined
total is 36 KiB, exceeding the 32 KiB budget. Skill definitions loaded last are truncated,
causing incomplete or broken skill behavior during task execution.

## Limitations

Skill content size depends on the configured skills at runtime, which may vary per user
or environment. This check measures the skill content from the project's skill configuration
files but cannot account for user-level or dynamically added skills. The 32 KiB default
budget can be changed via configuration; this rule uses the default value. The exact
serialization overhead (metadata headers, separators) added by Codex may vary across
versions, introducing a small margin of error.
