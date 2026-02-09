---
id: "CLAUDE:S:0009"
slug: project-rules-override-user
title: Project Rules Do Not Depend on User Settings
category: structure
type: mechanical
level: L4
backed_by:
- claude-code-memory
- claude-code-settings
targets: '{{instruction_files}}'
checks:
- id: "CLAUDE:S:0009:check:0001"
  type: mechanical
  check: content_absent
  args:
    pattern: "~/\\.claude"
  severity: medium
question: "Are project-level instruction files self-contained without dependencies
  on user-level configuration?"
criteria:
- No project-level files reference ~/.claude/ or $HOME/.claude/ paths as 
  operational dependencies
- No project-level files reference user-level settings.json keys as required 
  configuration
- Project CLAUDE.md does not instruct collaborators to modify their user-level 
  settings
- All necessary configuration is defined at project or local scope
---

# Project Rules Do Not Depend on User Settings

Project-level instruction files must not depend on user-level settings or instructions that may not be present for all collaborators.

## Pass / Fail

**Pass:** .claude/settings.json defines all necessary project permissions. CLAUDE.md contains all
project conventions without referencing ~/.claude/CLAUDE.md or user-level settings. The
project works identically for any collaborator regardless of their personal Claude Code
configuration.
**Fail:** CLAUDE.md contains "See ~/.claude/CLAUDE.md for API key configuration" or references
user-level settings with "Ensure your user settings have allowedTools: ['bash']". New
collaborators without this user-level setup receive incomplete or broken instructions.

## Limitations

This check scans for explicit references to user-level paths (~/, $HOME/.claude/) and
user-level setting keys. Implicit dependencies (e.g., assuming a user-level MCP server
is configured without referencing it by path) cannot be detected mechanically. The check
also cannot distinguish between documentation mentioning user settings (acceptable) and
operational dependencies on them (violation).
