---
id: "CORE:S:0009"
slug: local-files-not-committed
title: Local Instruction Files Not Committed
category: structure
type: mechanical
level: L2
backed_by:
- claude-code-memory
- claude-code-settings
- claude-md-guide
targets: '{{instruction_files}}'
checks:
- id: "CORE:S:0009:check:0001"
  type: mechanical
  check: file_count
  args:
    pattern: "**/*.local.md"
    max: 0
  severity: high
question: "Do any local instruction files (.local variants) exist in the project tree?"
criteria:
- No file matching the *.local.md pattern exists anywhere in the project tree
- Local file patterns include CLAUDE.local.md and similar .local.md variants
- Local files are developer-specific and should not be present in shared project
  trees
---

# Local Instruction Files Not Committed

Local instruction files (.local variants) should not exist in the project tree.

## Pass / Fail

**Pass:** The project contains no files matching `**/*.local.md`. Developers
keep local instruction files outside the project tree, or the project has
never used local overrides. The file count check finds zero matches.
**Fail:** A file matching `**/*.local.md` exists in the project tree (e.g.,
CLAUDE.local.md in the project root). The file count check finds one or more
matches, exceeding the maximum of zero. Local files risk being shared with
other developers or committed to version control.

## Limitations

Checks for file existence via glob pattern matching, not git tracking status.
A local file that exists on disk but is properly gitignored will still trigger
this rule. Git-tracking verification (via `git ls-files`) would require
runtime shell access, which the fixture-based test harness cannot provide.
Cannot detect local files with non-standard names outside the `*.local.md`
pattern.
