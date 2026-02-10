---
id: "CORE:S:0002"
slug: instruction-file-is-markdown
title: Instruction File Is Markdown
category: structure
type: mechanical
level: L1
backed_by:
- agents-md-spec
- spec-writing-for-agents
targets: '{{instruction_files}}'
checks:
- id: "CORE:S:0002:check:0001"
  type: mechanical
  check: file_exists
  severity: critical
question: "Does every instruction file use the .md file extension?"
criteria:
- Every recognized instruction file has a .md file extension
- No instruction files use alternative extensions (.txt, .yaml, .rst, .org)
- The filename follows the expected naming convention for the agent
---

# Instruction File Is Markdown

Every instruction file must use Markdown format with a .md extension.

## Pass / Fail

**Pass:** The project root contains CLAUDE.md — a file with the .md extension
containing standard Markdown syntax (headings, lists, code blocks).
**Fail:** The project root contains a file named CLAUDE.txt or CLAUDE.yaml that
serves as the instruction file but does not use Markdown format or the
.md file extension.

## Limitations

Only checks the file extension, not whether the content is valid Markdown.
A file named CLAUDE.md containing raw JSON or binary data would pass this
check. Content validity is outside the scope of a mechanical extension check.
