---
id: "CORE:S:0003"
slug: instruction-file-version-controlled
title: Instruction File Is Version Controlled
category: structure
type: mechanical
level: L1
backed_by:
- claude-code-settings
- claude-md-guide
- dometrain-claude-md-guide
targets: '{{instruction_files}}'
checks:
- id: "CORE:S:0003:check:0001"
  type: mechanical
  check: git_tracked
  severity: critical
question: "Is every instruction file tracked by version control (git)?"
criteria:
- Every recognized instruction file is tracked in the git index
- The file appears in `git ls-files` output
- The file is not listed as untracked or ignored by git
---

# Instruction File Is Version Controlled

Every instruction file must be tracked by version control.

## Pass / Fail

**Pass:** The CLAUDE.md file at the project root is tracked by git. Running
`git ls-files --error-unmatch CLAUDE.md` exits with code 0. The file
appears in `git status` as tracked (not under "Untracked files").
**Fail:** A CLAUDE.md file exists at the project root but is listed under
"Untracked files" in `git status`. The file was created locally but
never staged or committed. Team members pulling the repo do not receive it.

## Limitations

Cannot detect files that were committed but later removed from tracking
via `git rm --cached` while still present on disk. The check queries
current git index state only. Also cannot verify the file is on the
default branch — it may be tracked only on a feature branch.
