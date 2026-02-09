---
id: "CLAUDE:S:0001"
slug: claude-md-file-placement
title: CLAUDE.md File Placement
category: structure
type: mechanical
level: L1
backed_by:
- claude-code-memory
- claude-code-settings
- claude-md-guide
targets: '{{instruction_files}}'
checks:
- id: "CLAUDE:S:0001:check:0001"
  type: mechanical
  check: file_exists
  args:
    path: "CLAUDE.md"
  severity: critical
question: "Does a case-sensitive CLAUDE.md file exist at a recognized project-level
  location?"
criteria:
- A file named exactly CLAUDE.md exists at ./CLAUDE.md or ./.claude/CLAUDE.md
- The filename uses uppercase CLAUDE and lowercase .md extension
- At least one of the two recognized locations contains the file
---

# CLAUDE.md File Placement

A CLAUDE.md file must exist at the project root or in the .claude/ subdirectory with exact case-sensitive naming.

## Pass / Fail

**Pass:** A repository contains ./CLAUDE.md (uppercase CLAUDE, lowercase .md) at the project root.
Alternatively, the file exists at ./.claude/CLAUDE.md. Either location satisfies the rule.
**Fail:** A repository has no CLAUDE.md at either ./CLAUDE.md or ./.claude/CLAUDE.md. Variants such
as claude.md, Claude.md, CLAUDE.MD, or README-claude.md do not satisfy the requirement.

## Limitations

This check verifies file existence and exact filename casing only. It does not validate the
content of the CLAUDE.md file, nor does it check whether the file contains meaningful
instructions. An empty CLAUDE.md passes this rule.
