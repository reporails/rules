---
id: CORE:X:0001
slug: architecture-overview-present
title: Architecture Overview Present
category: context_quality
type: semantic
level: L4
backed_by:
- agent-readmes-empirical-study
- agentic-coding-adoption-github
- agents-md-impact-efficiency
- awesome-copilot-meta-instructions
- claude-code-memory
- claudemd-best-practices-backbone-yml-pattern
- codex-exec-plans
- copilot-cli-best-practices
- copilot-custom-instructions
- copilot-custom-instructions-vscode
- developer-context-cursor-study
- dometrain-claude-md-guide
- evaluating-agents-md
- fowler-pushing-ai-autonomy
- osmani-ai-coding-workflow
- sewell-agents-md-tips
- spec-writing-for-agents
- using-claude-md-files
targets: '{{main_instruction_file}}'
checks:
- id: CORE.X.0001.file_in_scope
  type: mechanical
  severity: medium
  name: file_in_scope
  check: file_exists
- id: CORE.X.0001.extract_architecture_content
  type: deterministic
  severity: medium
  name: extract_architecture_content
- id: CORE.X.0001.architecture_describes_relationships
  type: semantic
  severity: medium
  name: architecture_describes_relationships
question: Does the architecture section describe how components relate to each 
  other, not just list what exists?
criteria:
- Explains relationships between components (calls, depends on, produces, 
  consumes)
- Goes beyond listing technologies — describes how they fit together
- Provides enough context for an agent to understand where new code should go
choices:
- value: pass
  label: Passes
- value: fail
  label: Fails
pass_value: pass
---

# Architecture Overview Present

Instruction files SHOULD agents need to understand how the system fits together to make changes that integrate correctly

## Pass / Fail

### Pass

````
## Architecture

The system uses a hexagonal architecture with ports and adapters.
# === SEMANTIC JUDGMENT REQUIRED ===
# Write content satisfying all prior M/D checks,
# but testing the specific semantic question at this stage.
# One judgment call per rule — do not generate.
````

### Fail

````
(File does not exist at expected path)
````

## Limitations


