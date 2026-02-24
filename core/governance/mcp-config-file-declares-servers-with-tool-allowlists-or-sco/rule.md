---
id: CORE:G:0008
slug: mcp-config-file-declares-servers-with-tool-allowlists-or-sco
title: Mcp Config File Declares Servers With Tool Allowlists Or Scope 
  Constraints
category: governance
type: deterministic
level: L2
backed_by:
- claude-code-settings
- enterprise-claude-usage
- fowler-context-engineering-agents
targets: '{{mcp_config}}'
checks:
- id: CORE.G.0008.mcp_config_exists
  type: mechanical
  severity: medium
  name: mcp_config_exists
  check: file_exists
- id: CORE.G.0008.server_declarations
  type: deterministic
  severity: medium
  name: server_declarations
---

# Mcp Config File Declares Servers With Tool Allowlists Or Scope Constraints

Instruction files SHOULD unconstrained MCP servers can expose unintended tools to agents — explicit configuration prevents capability sprawl

## Pass / Fail

### Pass

````
Configure MCP servers in .mcp.json with explicit tool scoping
````

### Fail

````
# Instruction file content
````

## Limitations


