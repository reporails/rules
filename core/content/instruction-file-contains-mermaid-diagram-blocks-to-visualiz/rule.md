---
id: CORE:C:0031
slug: instruction-file-contains-mermaid-diagram-blocks-to-visualiz
title: Instruction File Contains Mermaid Diagram Blocks To Visualize Workflows, 
  State Machines, Or Decision Flows
category: content
type: deterministic
level: L2
backed_by:
- claudemd-best-practices-mermaid-for-workflows
- flowbench-workflow-format-benchmark
- fowler-pushing-ai-autonomy
targets: '{{instruction_files}}'
checks:
- id: CORE.C.0031.file_in_scope
  type: mechanical
  severity: medium
  name: file_in_scope
  check: file_exists
- id: CORE.C.0031.discusses_multi_step_processes
  type: deterministic
  severity: medium
  name: discusses_multi_step_processes
- id: CORE.C.0031.has_mermaid_blocks
  type: deterministic
  severity: medium
  name: has_mermaid_blocks
---

# Instruction File Contains Mermaid Diagram Blocks To Visualize Workflows, State Machines, Or Decision Flows

Instruction files SHOULD mermaid diagrams are parseable by both humans and agents — they encode workflow logic more precisely than prose descriptions

## Pass / Fail

### Pass

````
# Workflow
The deployment pipeline follows these steps:
```mermaid
flowchart TD
  A[Build] --> B[Test] --> C[Deploy]
```
````

### Fail

````
# Workflow Overview
The pipeline has multiple steps and decision points.
````

## Limitations


