---
id: "CORE:S:0010"
slug: cross-agent-compatibility
title: Cross-Agent Compatibility
category: structure
type: mechanical
level: L3
backed_by:
- agents-md-spec
- enterprise-claude-usage
targets: '{{instruction_files}}'
checks:
- id: "CORE:S:0010:check:0001"
  type: mechanical
  check: file_exists
  args:
    path: "CLAUDE.md"
  severity: medium
- id: "CORE:S:0010:check:0002"
  type: mechanical
  check: file_exists
  args:
    path: "AGENTS.md"
  severity: medium
question: "Does the project provide instruction files for more than one AI agent?"
criteria:
- At least two distinct agent instruction file types are present in the project
- Recognized file types include CLAUDE.md, AGENTS.md, .cursorrules, 
  .github/copilot-instructions.md
- Both files contain non-trivial content (not empty)
- Files are tracked by version control
---

# Cross-Agent Compatibility

Projects with instruction files for one agent should also provide an instruction file for at least one other major agent.

## Pass / Fail

**Pass:** A project contains both CLAUDE.md (Claude-specific instructions) and
AGENTS.md (vendor-neutral instructions). The AGENTS.md file provides
equivalent guidance that Codex, Copilot, or Cursor agents can consume.
Both files are committed and tracked.
**Fail:** A project contains only CLAUDE.md with no AGENTS.md, no .cursorrules, and
no other agent instruction file. Developers using Codex or Copilot receive
no project-specific guidance. The instruction system is locked to a single
agent vendor.

## Limitations

Checks for the presence of multiple agent instruction file types but cannot
verify that their content is consistent or equivalent. A project with
CLAUDE.md containing detailed instructions and an empty AGENTS.md technically
passes. Cannot assess whether the instruction files provide equivalent
guidance quality across agents.
