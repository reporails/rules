---
id: "CORE:C:0022"
slug: ask-not-guess
title: Ask Not Guess
category: content
type: deterministic
level: L2
backed_by:
- claude-code-issue-13579
- osmani-ai-coding-workflow
targets: '{{instruction_files}}'
checks:
- id: "CORE:C:0022:check:0001"
  type: deterministic
  negate: true
  severity: high
question: "Does this instruction file tell the agent to ask for clarification rather
  than guessing?"
criteria:
- File contains a directive to ask, confirm, or clarify when context is missing 
  or ambiguous
- The directive contrasts asking with guessing, assuming, or inferring
- The directive is framed as a general workflow principle (not specific to one 
  scenario)
---

# Ask Not Guess

Instruction files must include a directive for the agent to ask for clarification
rather than guessing when context is insufficient.

## Pass / Fail

**Pass:** "When unsure about requirements or design decisions, ask for clarification instead
of guessing. It's faster to ask one question than to redo an incorrect implementation."
**Fail:** An instruction file that describes the project thoroughly but contains no directive
about asking vs guessing. The agent encounters an ambiguous requirement and reads
50 files trying to infer the answer instead of asking the user.

## Limitations

Pattern-matches for keywords like "ask", "clarif", "instead of guessing", "when
unsure", "when unclear". May miss semantically equivalent instructions (e.g., "check
with me before making assumptions"). May false-positive on unrelated uses of "ask"
(e.g., "ask the API for a token"). Cannot verify that the directive is followed at
runtime.
