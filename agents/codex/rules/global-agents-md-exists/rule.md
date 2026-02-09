---
id: "CODEX:S:0006"
slug: global-agents-md-exists
title: Global AGENTS.md Exists
category: structure
type: mechanical
level: L5
backed_by:
- codex-agent-loop
targets: '{{instruction_files}}'
checks:
- id: "CODEX:S:0006:check:0001"
  type: mechanical
  check: file_exists
  args:
    path: "AGENTS.md"
  severity: medium
question: "Does a global AGENTS.md exist in $CODEX_HOME for user-level instruction
  defaults?"
criteria:
- An AGENTS.md or AGENTS.override.md file exists in $CODEX_HOME
- The file is not empty (contains meaningful user-level defaults)
- The $CODEX_HOME path resolves to an existing directory
---

# Global AGENTS.md Exists

A global AGENTS.md should exist in $CODEX_HOME for user-level defaults.

## Pass / Fail

**Pass:** $CODEX_HOME/AGENTS.md exists and contains user-level conventions: preferred coding style,
organization security policies, and default review expectations. These load as baseline
instructions before any project-specific AGENTS.md.
**Fail:** $CODEX_HOME contains no AGENTS.md or AGENTS.override.md. Codex starts every project
with zero user-level defaults. The developer relies entirely on per-project AGENTS.md
files, missing an opportunity to enforce personal or organizational standards globally.

## Limitations

This check verifies file existence at $CODEX_HOME but cannot determine the correct value
of $CODEX_HOME across environments (it defaults to ~/.codex but may be overridden). The
check cannot validate the content quality of the global file. A global AGENTS.md is a
recommendation (L5), not a hard requirement — some workflows intentionally omit it to
avoid interference with project-level instructions. Note that developer_instructions from
config.toml outranks AGENTS.md, which may make the global file redundant in some setups.
