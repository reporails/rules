---
id: CORE:M:0002
slug: valid-glob-patterns-in-frontmatter
title: Valid Glob Patterns in Frontmatter
category: maintenance
type: deterministic
level: L2
backed_by:
- awesome-copilot-meta-instructions
- copilot-coding-agent-best-practices
targets: '{{supplementary_files}}'
checks:
- id: CORE.M.0002.file-exists
  type: mechanical
  severity: medium
  name: file-exists
  check: file_exists
---

# Valid Glob Patterns in Frontmatter

When instruction files use glob or applyTo patterns in frontmatter to scope their applicability, the patterns SHOULD match at least one existing file in the project so the instructions are not silently ignored

## Pass / Fail

### Pass

~~~~markdown
---
applyTo: "src/**/*.test.ts"
---

## Testing Standards

- Use describe/it blocks...

(Glob matches 47 test files in the project)
~~~~

### Fail

~~~~markdown
(File does not exist at expected path)
~~~~

## Limitations

Cannot distinguish between intentionally aspirational patterns (scoping rules for files that will exist after a migration) and stale patterns left over from a refactor. Projects with no matching files yet may legitimately have zero-match patterns.
