---
id: "CORE:C:0002"
slug: has-project-structure
title: Has Project Structure
category: content
type: deterministic
level: L2
backed_by:
- claude-md-optimization-study
- dometrain-claude-md-guide
- spec-writing-for-agents
targets: '{{instruction_files}}'
checks:
- id: "CORE:C:0002:check:0001"
  type: deterministic
  negate: true
  severity: high
question: "Do the instruction files describe the project's directory layout or file
  organization?"
criteria:
- At least one instruction file contains a section describing directory 
  structure or file organization
- The description maps directory or file paths to their purpose
- At least two directories or file locations are described
---

# Has Project Structure

The instruction files must describe the project's directory structure or file organization.

## Pass / Fail

**Pass:** The instruction file contains:
```
## Structure
src/           - Application source code
src/models/    - Database models
tests/         - Test suite (mirrors src/ layout)
docs/          - Project documentation
scripts/       - Build and deployment scripts
```
Directories are listed with their purpose, giving the agent a map of the codebase.
**Fail:** The instruction file contains commands, style guides, and constraints but never mentions
where source code lives, where tests go, or how the repository is organized. The agent
must guess file placement from existing code.

## Limitations

Cannot verify the documented structure matches the actual filesystem. A stale structure
section that lists directories that no longer exist would still pass. Cannot assess
whether the structure description is complete enough for the project's complexity.
