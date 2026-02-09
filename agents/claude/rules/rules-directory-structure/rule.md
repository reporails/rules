---
id: "CLAUDE:S:0003"
slug: rules-directory-structure
title: Rules Directory Structure
category: structure
type: mechanical
level: L4
backed_by:
- claude-code-memory
- rules-directory-mechanics
targets: '{{instruction_files}}'
checks:
- id: "CLAUDE:S:0003:check:0001"
  type: mechanical
  check: directory_file_types
  args:
    path: "{{rules_dir}}"
    extensions: [".md"]
  severity: medium
question: "Does the .claude/rules/ directory follow single-concern and scoping conventions?"
criteria:
- The .claude/rules/ directory contains only .md files (no other formats)
- Each .md file addresses a focused, single concern
- Files without a paths frontmatter key contain only universally applicable 
  guidance
- Subdirectory organization is permitted for grouping related rules
---

# Rules Directory Structure

If .claude/rules/ exists, every .md file in it must address a single concern and files without paths frontmatter must contain only universally applicable rules.

## Pass / Fail

**Pass:** .claude/rules/testing.md has paths frontmatter scoped to tests/**/*.py and contains only
testing conventions. .claude/rules/commit-style.md has no paths frontmatter and contains
a universal commit message format that applies to all files. Each file addresses one concern.
**Fail:** .claude/rules/everything.md has no paths frontmatter and contains testing conventions,
deployment procedures, and database migration rules all in one file. The testing conventions
are irrelevant when editing frontend code, but they load unconditionally.

## Limitations

Determining whether a file addresses "a single concern" is subjective at the mechanical
level. This check uses heuristics: multiple H2 headings on unrelated topics, excessive file
length, or mixed domain keywords. It cannot perfectly judge concern boundaries. The universal
applicability check for unscoped files relies on keyword heuristics rather than semantic
understanding.
