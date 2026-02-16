---
id: COPILOT:C:0001
slug: copilot-path-specific-instructions
title: Path-Specific Instructions with Glob Patterns
category: content
type: mechanical
level: L3
backed_by:
- copilot-coding-agent-best-practices
- copilot-custom-instructions
targets: '{{instruction_files}}'
checks:
- id: COPILOT.C.0001.file-exists
  type: mechanical
  severity: medium
  name: file-exists
  check: file_exists
---

# Path-Specific Instructions with Glob Patterns

Copilot projects with domain-specific conventions SHOULD use .github/instructions/*.instructions.md files with applyTo frontmatter to scope instructions to relevant file patterns

## Pass / Fail

### Pass

~~~~markdown
---
applyTo: "**/tests/*.spec.ts"
---

## Playwright Tests
- Use getByRole() over CSS selectors
- Each test must be independent
~~~~

### Fail

~~~~markdown
All testing instructions embedded in the root copilot-instructions.md, loading for every Copilot interaction regardless of whether the user is working on tests
~~~~

## Limitations

Can check for file existence and frontmatter format but cannot verify glob patterns match actual project files or that the content is appropriately scoped.
