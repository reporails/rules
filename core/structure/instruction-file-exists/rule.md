---
id: "CORE:S:0001"
slug: instruction-file-exists
title: Instruction File Exists
category: structure
type: mechanical
level: L1
backed_by:
- agents-md-spec
- claude-md-guide
- dometrain-claude-md-guide
- using-claude-md-files
targets: '{{instruction_files}}'
checks:
- id: "CORE:S:0001:check:0001"
  type: mechanical
  check: file_exists
  severity: critical
question: "Does at least one recognized instruction file exist in the project?"
criteria:
- A file matching a recognized instruction filename pattern exists in the 
  project root
- The recognized filenames include CLAUDE.md, AGENTS.md, and agent-equivalent 
  files
- The file is not empty (has at least 1 byte of content)
---

# Instruction File Exists

At least one recognized instruction file must exist in the project.

## Pass / Fail

**Pass:** A repository contains a CLAUDE.md file at the project root with at least
10 lines of project-specific content. The file is committed to git.
Alternatively, an AGENTS.md file exists at the root.
**Fail:** A repository has no CLAUDE.md, no AGENTS.md, and no other recognized
instruction file anywhere in the project tree. The agent must operate
without any project-specific guidance.

## Limitations

Cannot verify the instruction file contains meaningful content — only that
a file with a recognized name exists at the expected location. An empty or
trivially small file passes this rule but would fail content-level checks.
Does not check for agent-specific variants (e.g., .cursorrules) beyond the
recognized set.
