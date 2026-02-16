---
id: CORE:M:0001
slug: valid-internal-references
title: Valid Internal File References
category: maintenance
type: deterministic
level: L2
backed_by:
- enterprise-claude-usage
- instruction-limits-principles
- rules-directory-mechanics
targets: '{{instruction_files}}'
checks:
- id: CORE.M.0001.file-exists
  type: mechanical
  severity: high
  name: file-exists
  check: file_exists
---

# Valid Internal File References

Instruction files that reference other files by path MUST reference files that actually exist in the repository

## Pass / Fail

### Pass

~~~~markdown
See docs/api-patterns.md for API conventions.
For the auth flow, see src/auth/README.md.

(Both files exist in the repo)
~~~~

### Fail

~~~~markdown
(File does not exist at expected path)
~~~~

## Limitations

Can only verify file existence at check time. Files may be created or deleted between checks. Cannot verify the content of referenced files is still relevant.
