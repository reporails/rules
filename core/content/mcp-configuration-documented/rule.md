---
id: CORE:C:0027
slug: mcp-configuration-documented
title: MCP Configuration Documented
category: content
type: deterministic
level: L6
backed_by:
- building-skills-for-claude
- claude-code-settings
- codex-developers-2025
- copilot-about-coding-agent
- copilot-coding-agent-best-practices
- copilot-coding-agent-results
- copilot-coding-agent-tasks
- dometrain-claude-md-guide
- enterprise-claude-usage
- fowler-context-engineering-agents
- fowler-pushing-ai-autonomy
- microsoft-awesome-copilot-blog
- spec-writing-for-agents
- using-claude-md-files
targets: '{{main_instruction_file}}'
checks:
- id: CORE.C.0027.file_in_scope
  type: mechanical
  severity: medium
  name: file_in_scope
  check: file_exists
- id: CORE.C.0027.has_mcp_reference
  type: deterministic
  severity: medium
  name: has_mcp_reference
---

# MCP Configuration Documented

Instruction files SHOULD agents need to know which MCP servers are available and what tools they provide

## Pass / Fail

### Pass

````
Document available MCP servers and their capabilities
````

### Fail

````
# Instruction file content
````

## Limitations


