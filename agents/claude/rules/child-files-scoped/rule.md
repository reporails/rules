---
id: "CLAUDE:S:0005"
slug: child-files-scoped
title: Child CLAUDE.md Files Are Properly Scoped
category: structure
type: semantic
level: L3
backed_by:
- claude-code-memory
- monorepo-claude-md-organization
targets: '{{instruction_files}}'
checks:
- id: "CLAUDE:S:0005:check:0001"
  type: mechanical
  check: file_count
  args:
    pattern: "**/CLAUDE.md"
    min: 2
  severity: medium
- id: "CLAUDE:S:0005:check:0002"
  type: semantic
  prompt: "Do child CLAUDE.md files contain only directory-specific content without duplicating parent CLAUDE.md content?"
  severity: medium
question: "Do child CLAUDE.md files contain only directory-specific content without
  duplicating parent file content?"
criteria:
- Child CLAUDE.md files exist in subdirectories (project has hierarchical 
  instruction structure)
- Each child file addresses concerns specific to its directory scope
- No substantial content overlap between child and parent CLAUDE.md files
- Project-wide conventions, tech stack, and descriptions appear only in the root
  file
---

# Child CLAUDE.md Files Are Properly Scoped

Child CLAUDE.md files must contain only directory-specific content and must not duplicate content from parent CLAUDE.md files.

## Pass / Fail

**Pass:** Root CLAUDE.md defines the project description, tech stack, and global coding conventions.
services/api/CLAUDE.md contains only API-specific testing instructions, endpoint conventions,
and middleware configuration details not covered by the root file.
**Fail:** Root CLAUDE.md describes the project as a TypeScript monorepo with ESLint and Prettier.
services/api/CLAUDE.md repeats the same project description, tech stack, and linting rules
already present in the root file, adding only a single line about API routes.

## Limitations

Detecting content duplication between parent and child files requires semantic comparison.
Mechanical checks can verify file existence and basic structure but cannot assess whether
content is genuinely scoped or redundantly repeated. Minor paraphrasing of parent content
may not be detected as duplication.
