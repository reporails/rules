---
id: CORE:S:0002
slug: monorepo-nested-instruction-files
title: Monorepo Nested Instruction Files
category: structure
type: deterministic
level: L2
backed_by:
- agents-md-spec
- claude-md-guide
- instruction-limits-principles
targets: '{{instruction_files}}'
checks:
- id: CORE.S.0002.file-exists
  type: mechanical
  severity: medium
  name: file-exists
  check: file_exists
---

# Monorepo Nested Instruction Files

Projects with multiple distinct components (monorepos, multi-service repos) SHOULD place nested instruction files in component subdirectories rather than maintaining one monolithic root file

## Pass / Fail

### Pass

~~~~markdown
AGENTS.md (shared conventions, 80 lines)
frontend/AGENTS.md (React patterns, 60 lines)
backend/AGENTS.md (API conventions, 70 lines)
core/AGENTS.md (shared library rules, 40 lines)
~~~~

### Fail

~~~~markdown
(File does not exist at expected path)
~~~~

## Limitations

Cannot reliably detect whether a project is a monorepo. Heuristics like multiple package.json or Cargo.toml files may produce false positives for simple projects with dev tooling.
