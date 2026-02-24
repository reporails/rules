---
id: CORE:S:0014
slug: descriptive-filenames
title: Descriptive Filenames
category: structure
type: semantic
level: L5
backed_by:
- awesome-copilot-meta-instructions
- building-skills-for-claude
- claude-code-memory
- copilot-coding-agent-tasks
- copilot-custom-instructions
- copilot-custom-instructions-vscode
- instruction-limits-principles
- microsoft-awesome-copilot-blog
- rules-directory-mechanics
- spec-writing-for-agents
- using-claude-md-files
targets: '{{main_instruction_file}}'
checks:
- id: CORE.S.0014.file_in_scope
  type: mechanical
  severity: medium
  name: file_in_scope
  check: glob_match
- id: CORE.S.0014.extract_filenames
  type: deterministic
  severity: medium
  name: extract_filenames
- id: CORE.S.0014.names_are_descriptive
  type: semantic
  severity: medium
  name: names_are_descriptive
question: Do the filenames describe their content or purpose, rather than using 
  generic names (rule-1.md, config.md, notes.md)?
criteria:
- Names indicate what topic or concern the file covers
- Names use domain-specific terms, not generic labels
- A developer could guess the file's purpose from its name alone
choices:
- value: pass
  label: Passes
- value: fail
  label: Fails
pass_value: pass
---

# Descriptive Filenames

Instruction files SHOULD generic or numbered filenames force agents to open files to understand them — semantic names enable direct navigation

## Pass / Fail

### Pass

````
See CLAUDE.md and config.yml for details.
# === SEMANTIC JUDGMENT REQUIRED ===
# Write content satisfying all prior M/D checks,
# but testing the specific semantic question at this stage.
# One judgment call per rule — do not generate.
````

### Fail

````
# === EXTERNAL STRUCTURE CHECK ===
# Fixture requires external repo structure (directories, files, imports).
# Cannot be represented as instruction file content alone.
````

## Limitations


