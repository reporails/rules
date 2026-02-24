---
id: CORE:M:0001
slug: freshness-marker-present
title: Freshness Marker Present
category: maintenance
type: deterministic
level: L2
backed_by:
- agent-readmes-empirical-study
- agents-md-impact-efficiency
- agents-md-spec
- awesome-copilot-meta-instructions
- builder-ai-instruction-best-practices
- building-skills-for-claude
- claude-code-memory
- claude-md-guide
- claudemd-best-practices-backbone-yml-pattern
- codex-exec-plans
- codex-skills-shell-compaction
- developer-context-cursor-study
- dometrain-claude-md-guide
- enterprise-claude-usage
- openai-community-agents-md-optimization
- osmani-ai-coding-workflow
- prompthub-cursor-rules-analysis
- spec-writing-for-agents
- using-claude-md-files
targets: '{{main_instruction_file}}'
checks:
- id: CORE.M.0001.file_in_scope
  type: mechanical
  severity: medium
  name: file_in_scope
  check: file_exists
- id: CORE.M.0001.has_freshness_marker
  type: deterministic
  severity: medium
  name: has_freshness_marker
---

# Freshness Marker Present

Instruction files SHOULD instruction files need freshness markers so reviewers know when they were last validated

## Pass / Fail

### Pass

````
<!-- Last updated: 2026-01-01 -->
````

### Fail

````
# Instruction file content
````

## Limitations


