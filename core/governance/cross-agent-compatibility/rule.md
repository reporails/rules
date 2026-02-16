---
id: CORE:G:0001
slug: cross-agent-compatibility
title: Cross-Agent Compatibility
category: governance
type: semantic
level: L2
backed_by:
- agents-md-spec
- copilot-custom-instructions
- enterprise-claude-usage
targets: '{{instruction_files}}'
checks:
- id: CORE.G.0001.file-exists
  type: mechanical
  severity: medium
  name: file-exists
  check: file_exists
- id: CORE.G.0001.agent-specific-syntax
  type: deterministic
  severity: medium
  name: agent-specific-syntax
- id: CORE.G.0001.semantic-evaluation
  type: semantic
  severity: medium
  name: semantic-evaluation
question: Does this shared instruction file avoid agent-specific syntax and 
  features that would not be understood by other coding agents?
criteria:
- File uses standard markdown without agent-specific syntax (@import, YAML 
  frontmatter path scoping)
- No references to agent-specific directories (.claude/rules/, 
  .github/instructions/)
- Agent-specific features appear only in agent-specific files, not shared 
  AGENTS.md
choices:
- value: pass
  label: Passes
- value: fail
  label: Fails
pass_value: pass
---

# Cross-Agent Compatibility

Shared instruction files (AGENTS.md, files read by multiple agents) SHOULD use generic terminology rather than agent-specific features when the same file will be consumed by different tools

## Pass / Fail

### Pass

~~~~markdown
## File Organization

Store task-specific instructions in separate files referenced from the root instruction file.
Agents discover the nearest instruction file in the directory tree.
~~~~

### Fail

~~~~markdown
## File Organization

Use @import syntax to include other files.
Put path-scoped rules in .claude/rules/ with YAML frontmatter.
(This is AGENTS.md but uses Claude-specific features)
~~~~

## Limitations

Only applies to shared files (AGENTS.md). Agent-specific files (CLAUDE.md, copilot-instructions.md) are expected to use agent-specific features. Requires understanding which file is being checked and whether multiple agents consume it.
