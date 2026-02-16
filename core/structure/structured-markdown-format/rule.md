---
id: CORE:S:0003
slug: structured-markdown-format
title: Structured Markdown Formatting
category: structure
type: deterministic
level: L1
backed_by:
- agents-md-spec
- copilot-cli-best-practices
targets: '{{instruction_files}}'
checks:
- id: CORE.S.0003.file-exists
  type: mechanical
  severity: medium
  name: file-exists
  check: file_exists
- id: CORE.S.0003.wall-of-prose
  type: deterministic
  severity: medium
  name: wall-of-prose
---

# Structured Markdown Formatting

Instruction files SHOULD use markdown headings to organize sections and bullet points or numbered lists for individual instructions, rather than unstructured prose paragraphs

## Pass / Fail

### Pass

~~~~markdown
## Commands

- Build: `npm run build`
- Test: `npm test -- --coverage`
- Lint: `npm run lint --fix`

## Conventions

- Named exports only
- Error shape: {error, code}
~~~~

### Fail

~~~~markdown
This project uses npm for building. You should run npm run build to build it. For testing we use jest and you can run npm test with the coverage flag. The linter is eslint and prettier combined. We prefer named exports and our error responses use an error and code shape.
~~~~

## Limitations

Checks for heading and list markup presence. Cannot assess whether the structure is logical or whether sections are appropriately grouped. A file with headings but poor organization would pass.
