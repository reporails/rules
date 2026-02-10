---
id: "CLAUDE:S:0004"
slug: path-targeting-syntax
title: Path Targeting Syntax
category: structure
type: mechanical
level: L4
backed_by:
- claude-code-memory
- rules-directory-mechanics
targets: '{{instruction_files}}'
checks:
- id: "CLAUDE:S:0004:check:0001"
  type: mechanical
  check: frontmatter_valid_glob
  args:
    path: "{{rules_dir}}"
  severity: medium
question: "Do all path-targeted rules have valid YAML frontmatter with syntactically
  correct glob patterns?"
criteria:
- The file begins with a valid YAML frontmatter block delimited by --- lines
- The frontmatter contains a paths key with a list value
- Each paths entry is a syntactically valid glob pattern
- Brace expansion expressions are properly closed and contain at least two 
  alternatives
- No other unexpected keys appear in the frontmatter block
---

# Path Targeting Syntax

Rules with path targeting must use valid YAML frontmatter with a paths key containing valid glob patterns.

## Pass / Fail

**Pass:** A rule file .claude/rules/api-conventions.md begins with:
---
paths:
  - src/api/**/*.ts
  - src/api/**/*.{js,jsx}
---
The frontmatter is valid YAML and both patterns use correct glob syntax with brace expansion.
**Fail:** A rule file .claude/rules/api-conventions.md begins with:
---
paths:
  - src/api/**/*.{ts,
---
The brace expansion is unclosed, making the glob pattern syntactically invalid. Claude Code
may ignore this rule or apply it incorrectly.

## Limitations

This check validates syntactic correctness of glob patterns but cannot verify semantic
correctness (i.e., whether the pattern actually matches the intended files). It also cannot
detect patterns that are valid but overly broad (e.g., **/*). Brace expansion validation
covers nesting up to one level; deeply nested braces may not be fully validated.
