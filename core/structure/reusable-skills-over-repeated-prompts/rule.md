---
id: "CORE:S:0012"
slug: reusable-skills-over-repeated-prompts
title: Reusable Skills Over Repeated Prompts
category: structure
type: semantic
level: L6
backed_by:
- dometrain-claude-md-guide
- osmani-ai-coding-workflow
targets: '{{instruction_files}}'
checks:
- id: "CORE:S:0012:check:0001"
  type: deterministic
  severity: medium
- id: "CORE:S:0012:check:0002"
  type: semantic
  prompt: "Are repeatable multi-step procedures extracted into reusable skills rather than inlined in instruction files?"
  severity: medium
question: "Are repeatable multi-step procedures extracted into reusable skills rather
  than inlined?"
criteria:
- No instruction file contains inline numbered procedures exceeding 10 steps
- Multi-step workflows reference skill files rather than embedding full 
  procedures
- A skills directory exists if the instruction file references workflow-like 
  operations
- Repeated procedural content across instruction files is consolidated into a 
  single skill
---

# Reusable Skills Over Repeated Prompts

Repeatable multi-step procedures in instruction files should be extracted into reusable skills.

## Pass / Fail

**Pass:** A CLAUDE.md file says "For deployment, use the /deploy skill" and the
detailed deployment procedure lives in .claude/skills/deploy/SKILL.md with
step-by-step instructions. The root instruction file references the skill
rather than inlining the procedure. Common workflows (testing, releasing,
reviewing) are similarly extracted into skill files.
**Fail:** A CLAUDE.md file contains three inline multi-step procedures: a 25-line
deployment checklist, a 20-line release workflow, and a 15-line review
process — all written as numbered prose steps directly in the file. No
skills directory exists. The same deployment steps are also repeated in
.claude/rules/ops.md with slight variations.

## Limitations

Requires semantic evaluation (LLM judgment) to determine whether an inline
procedure is genuinely repeatable and would benefit from extraction versus
being a one-off instruction. Cannot establish a bright-line threshold for
"multi-step" — a 3-step process may or may not warrant skill extraction.
Cannot detect procedures that should exist as skills but are simply absent
from the instruction file entirely.
