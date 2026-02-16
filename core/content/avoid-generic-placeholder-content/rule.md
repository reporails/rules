---
id: CORE:C:0004
slug: avoid-generic-placeholder-content
title: Avoid Generic Placeholder Content
category: content
type: deterministic
level: L1
backed_by:
- claude-md-guide
- enterprise-claude-usage
- instruction-limits-principles
targets: '{{instruction_files}}'
checks:
- id: CORE.C.0004.file-exists
  type: mechanical
  severity: medium
  name: file-exists
  check: file_exists
- id: CORE.C.0004.no-generic-advice
  type: deterministic
  severity: medium
  name: no-generic-advice
---

# Avoid Generic Placeholder Content

Root instruction files SHOULD NOT contain auto-generated boilerplate, template markers, or vague guidance that adds no project-specific information

## Pass / Fail

### Pass

~~~~markdown
## Code Style

- Use named exports, never default exports
- Error responses: `{error: string, code: number}`
- Components under 200 lines; extract hooks at 50 lines
~~~~

### Fail

~~~~markdown
## Code Style

- Write clean, maintainable code
- Follow best practices
- Be consistent with existing patterns
- TODO: Add project-specific conventions
~~~~

## Limitations

Pattern matching for template markers (TODO, placeholder, TBD) may produce false positives in files that legitimately discuss those concepts. Cannot assess whether non-template content is truly project-specific.
