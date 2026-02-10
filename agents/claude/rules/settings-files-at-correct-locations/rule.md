---
id: "CLAUDE:S:0010"
slug: settings-files-at-correct-locations
title: Settings Files at Correct Locations
category: structure
type: mechanical
level: L4
backed_by:
- claude-code-settings
targets: '{{instruction_files}}'
checks:
- id: "CLAUDE:S:0010:check:0001"
  type: mechanical
  check: file_exists
  args:
    path: ".claude/settings.json"
  severity: medium
question: "Are all Claude Code configuration files placed at their documented discovery
  locations?"
criteria:
- settings.json for project scope exists at .claude/settings.json, not at the 
  project root
- settings.local.json exists at .claude/settings.local.json if present
- .mcp.json exists at the project root if MCP configuration is used
- No Claude Code configuration files exist at non-standard locations where they 
  would be ignored
---

# Settings Files at Correct Locations

Claude Code configuration files (.claude/settings.json, .mcp.json) must be at their documented locations.

## Pass / Fail

**Pass:** Project settings are at ./.claude/settings.json. MCP configuration is at ./.mcp.json in
the project root. Local overrides are at ./.claude/settings.local.json. All files are at
their documented discovery paths.
**Fail:** A file named settings.json exists at the project root (./) instead of ./.claude/settings.json.
Claude Code does not discover it, so the project's permission allowlist and tool configuration
are not applied. Alternatively, .mcp.json exists inside .claude/ instead of the project root.

## Limitations

This check verifies that configuration files found in the repository are at recognized
paths. It does not validate the content or schema of those files. It also cannot detect
the absence of configuration files that should exist — only misplacement of files that
do exist. Custom configuration file locations set via environment variables are not covered.
