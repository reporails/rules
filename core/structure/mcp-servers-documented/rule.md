---
id: "CORE:S:0011"
slug: mcp-servers-documented
title: MCP Servers Documented
category: structure
type: deterministic
level: L6
backed_by:
- claude-code-settings
- dometrain-claude-md-guide
targets: '{{instruction_files}}'
checks:
- id: "CORE:S:0011:check:0001"
  type: mechanical
  check: file_exists
  args:
    path: ".mcp.json"
  severity: medium
- id: "CORE:S:0011:check:0002"
  type: deterministic
  negate: true
  severity: medium
question: "If MCP server configuration exists, do the instruction files document their
  usage?"
criteria:
- An MCP configuration file (.mcp.json or equivalent) exists in the project
- At least one instruction file contains documentation referencing MCP servers 
  or tools
- The MCP documentation describes purpose or usage guidance for the configured 
  servers
- The rule is not applicable if no MCP configuration file exists
---

# MCP Servers Documented

If MCP server configuration exists, the instruction files must document MCP server usage.

## Pass / Fail

**Pass:** A project has .mcp.json defining a PostgreSQL MCP server and a GitHub MCP
server. The CLAUDE.md file contains a section "## Available Tools" or
"## MCP Servers" that explains: "Use the postgres MCP server for database
queries. Use the github MCP server for issue management. Do not use MCP
servers for tasks that can be done with standard CLI tools."
**Fail:** A project has .mcp.json with three MCP server configurations. None of the
instruction files (CLAUDE.md, .claude/rules/*.md) mention MCP, tools, or
servers. The agent discovers MCP servers at runtime but has no guidance on
when or how to use them.

## Limitations

Cannot verify that the documentation accurately describes the configured
MCP servers. A mention of "MCP" in any context (even unrelated) in the
instruction file would satisfy the pattern check. Cannot assess whether the
documentation provides sufficient detail for the agent to use the servers
correctly. Only triggers when .mcp.json or equivalent config exists —
projects without MCP config are not evaluated.
