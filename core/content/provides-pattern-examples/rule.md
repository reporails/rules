---
id: "CORE:C:0025"
slug: provides-pattern-examples
title: Provides Pattern Examples
category: content
type: deterministic
level: L2
backed_by:
- osmani-ai-coding-workflow
- spec-writing-for-agents
targets: '{{instruction_files}}'
checks:
- id: "CORE:C:0025:check:0001"
  type: deterministic
  negate: true
  severity: high
question: "Does this instruction file include concrete examples of desired code patterns
  from the project?"
criteria:
- File contains at least one code fence (```) or inline code example showing a 
  desired pattern
- Examples demonstrate project-specific patterns (component structure, naming, 
  API usage) not generic syntax
- Examples are presented as exemplary ("like this", "follow this pattern") not 
  just documentation of commands
- Prose descriptions of style without accompanying code examples do not satisfy 
  this rule
---

# Provides Pattern Examples

Instruction files must include concrete examples of desired code patterns or output
formats from the project.

## Pass / Fail

**Pass:** "Example component:\n```tsx\nexport function UserCard({ user }: Props) {\n  return
<Card title={user.name} />\n}\n```\nFollow this pattern for all new components:
named export, destructured props, single return."
**Fail:** "Follow the patterns used in the codebase. Components should be clean and follow
our conventions." — no actual examples of what those patterns or conventions look
like.

## Limitations

Pattern-matches for code fences (```), inline code backticks used as examples, or
phrases like "example", "pattern", "like this". May false-positive on code fences
used for non-exemplary purposes (e.g., documenting a command to run). Cannot assess
whether examples are representative of the codebase's actual style. Cannot
distinguish between exemplary patterns (good) and linter-enforceable formatting
rules (should use a linter instead, per conflict 0001).
