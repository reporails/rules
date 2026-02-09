---
id: "CORE:C:0017"
slug: repo-specific-content
title: Repo-Specific Content
category: content
type: semantic
level: L2
backed_by:
- claude-md-optimization-study
- using-claude-md-files
targets: '{{instruction_files}}'
checks:
- id: "CORE:C:0017:check:0001"
  type: deterministic
  negate: true
  severity: medium
- id: "CORE:C:0017:check:0002"
  type: semantic
  prompt: "Does the instruction file contain content specific to this repository rather than generic advice?"
  severity: medium
question: "Does this instruction file contain content that is specific to its repository
  rather than generic advice?"
criteria:
- File references specific file paths, module names, or API endpoints from the 
  project
- Constraints address real problems encountered in this repository (not 
  theoretical concerns)
- Generic programming advice (SOLID, clean code, meaningful names) is absent or 
  minimal
- Instructions would not make sense if copy-pasted into a different repository 
  without modification
---

# Repo-Specific Content

Instruction file content must be specific to the repository rather than generic
advice applicable to any project.

## Pass / Fail

**Pass:** "This project uses a custom ORM wrapper in `lib/db.ts`. Always use `db.query()`
instead of raw SQL. The wrapper handles connection pooling and parameter escaping."
References a specific file, a specific API, and a specific reason.
**Fail:** "Write clean, maintainable code. Follow SOLID principles. Use meaningful variable
names. Keep functions short and focused." — this advice applies to every project
and provides no repo-specific value.

## Limitations

Requires semantic judgment — an LLM must assess whether content is repo-specific
or generic. Some instruction files legitimately contain a mix of both (e.g., a
project-specific section plus a brief general coding standard). Cannot verify that
referenced files or paths actually exist in the repository. Cannot detect generic
advice that has been superficially personalized (e.g., "In this project, write
clean code").
