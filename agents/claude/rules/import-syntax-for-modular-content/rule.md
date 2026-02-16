---
id: CLAUDE:C:0001
slug: import-syntax-for-modular-content
title: Import Syntax for Modular Content
category: content
type: deterministic
level: L2
backed_by:
- claude-code-memory
targets: '{{main_instruction_file}}'
checks:
- id: CLAUDE.C.0001.file-exists
  type: mechanical
  severity: medium
  name: file-exists
  check: file_exists
- id: CLAUDE.C.0001.unlinked-file-reference
  type: deterministic
  severity: medium
  name: unlinked-file-reference
---

# Import Syntax for Modular Content

CLAUDE.md files that reference detailed external documentation SHOULD use @path/to/file import syntax so Claude loads the content automatically, rather than relying on the agent to voluntarily read a mentioned file path

## Pass / Fail

### Pass

~~~~markdown
## Resources

See @docs/api-patterns.md for API conventions.
See @docs/testing.md for test framework details.

 (Claude loads these automatically when CLAUDE.md is read)
~~~~

### Fail

~~~~markdown
## Resources

See docs/api-patterns.md for API conventions.
See docs/testing.md for test framework details.

 (Claude may or may not read these files — no guarantee of loading)
~~~~

## Limitations

Can check for @-prefixed file paths but cannot verify the referenced files exist or contain useful content. Import chains have a max depth of 5 hops. Over-importing defeats the purpose of keeping CLAUDE.md lean.
