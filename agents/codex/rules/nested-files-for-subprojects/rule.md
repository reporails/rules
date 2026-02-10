---
id: "CODEX:S:0005"
slug: nested-files-for-subprojects
title: Nested AGENTS.md for Subprojects
category: structure
type: mechanical
level: L3
backed_by:
- agents-md-spec
- codex-agent-loop
- codex-agents-md
targets: '{{instruction_files}}'
checks:
- id: "CODEX:S:0005:check:0001"
  type: mechanical
  check: file_count
  args:
    pattern: "**/AGENTS.md"
    min: 2
  severity: medium
question: "Do subproject directories in a monorepo have their own AGENTS.md when they
  have distinct conventions?"
criteria:
- Directories with project manifest files (package.json, setup.py, etc.) are 
  identified as subprojects
- Each subproject directory contains an AGENTS.md or AGENTS.override.md file
- Subproject AGENTS.md files contain conventions specific to that subproject's 
  stack
- The root AGENTS.md covers only shared, cross-subproject conventions
---

# Nested AGENTS.md for Subprojects

In monorepo setups, each subproject directory with distinct conventions must have its own AGENTS.md.

## Pass / Fail

**Pass:** A monorepo has packages/api/ (Python, FastAPI) and packages/web/ (TypeScript, React). Both
directories contain AGENTS.md files with stack-specific conventions. The root AGENTS.md
covers shared conventions. Codex loads the appropriate instructions when working in either
subproject.
**Fail:** A monorepo has packages/api/ (Python) and packages/web/ (TypeScript). Only the root
AGENTS.md exists with TypeScript conventions. When Codex works in packages/api/, it applies
TypeScript conventions to Python code because no api-specific AGENTS.md overrides the root.

## Limitations

Identifying "subproject directories with distinct conventions" requires heuristics: presence
of package.json, setup.py, Cargo.toml, or other project manifests. The check cannot
determine whether a subproject's conventions actually differ from the root without semantic
analysis. Some monorepos have uniform conventions across all subprojects, making per-
subproject AGENTS.md unnecessary. The check flags subprojects without AGENTS.md as warnings,
not errors.
