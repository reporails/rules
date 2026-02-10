---
id: "CORE:C:0023"
slug: explain-reasoning
title: Explain Reasoning
category: content
type: deterministic
level: L2
backed_by:
- osmani-ai-coding-workflow
targets: '{{instruction_files}}'
checks:
- id: "CORE:C:0023:check:0001"
  type: deterministic
  negate: true
  severity: high
question: "Does this instruction file tell the agent to explain its reasoning when
  making changes?"
criteria:
- File contains a directive to explain, document, or describe reasoning behind 
  changes
- The directive applies to code changes, bug fixes, or architectural decisions 
  (not just documentation tasks)
- The directive asks for the "why" (root cause, tradeoffs) not just the "what" 
  (description of change)
---

# Explain Reasoning

Instruction files must include a directive for the agent to explain its reasoning
or changes.

## Pass / Fail

**Pass:** "When fixing bugs, briefly explain the root cause and why this fix works. When
making architectural decisions, document the tradeoffs considered."
**Fail:** An instruction file that describes coding standards and testing requirements but
contains no directive about explaining reasoning. The agent silently changes a
function signature without explaining why the original was wrong.

## Limitations

Pattern-matches for keywords like "explain", "reasoning", "why", "document",
"comment", "describe". May miss semantically equivalent phrasing (e.g., "show your
work"). May false-positive on unrelated uses of "explain" (e.g., "explain the API
to new developers" as a documentation task). Cannot assess whether the agent actually
follows the directive.
