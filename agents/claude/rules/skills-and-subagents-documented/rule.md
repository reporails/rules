---
id: "CLAUDE:S:0008"
slug: skills-and-subagents-documented
title: Skills and Subagents Are Documented
category: structure
type: deterministic
level: L6
backed_by:
- claude-code-settings
- osmani-ai-coding-workflow
- using-claude-md-files
targets: '{{instruction_files}}'
checks:
- id: "CLAUDE:S:0008:check:0001"
  type: deterministic
  negate: true
  severity: medium
question: "Do all skill and subagent files include documentation of their purpose
  and usage?"
criteria:
- Every SKILL.md file in .claude/skills/ contains a title and description 
  section
- Every subagent .md file in .claude/agents/ has YAML frontmatter with role 
  metadata
- Skill files describe expected inputs or parameters if applicable
- Subagent files explain when and how the subagent should be invoked
- No skill or subagent file is empty or contains only a single undescriptive 
  line
---

# Skills and Subagents Are Documented

If .claude/skills/ or .claude/agents/ directories exist, the instruction files must document their purpose and usage.

## Pass / Fail

**Pass:** .claude/skills/deploy/SKILL.md contains a title, a description of what the skill does,
expected inputs, step-by-step workflow, and example invocation. .claude/agents/reviewer.md
has YAML frontmatter with role description and a markdown body explaining when and how
to use the reviewer subagent.
**Fail:** .claude/skills/deploy/SKILL.md contains only "Deploy the app" with no description of
inputs, steps, or expected behavior. .claude/agents/reviewer.md exists but is empty.
Neither provides enough information for another developer or agent to use them correctly.

## Limitations

The check verifies presence of documentation elements (title, description, usage) using
pattern matching but cannot evaluate documentation quality or accuracy. A skill file that
contains boilerplate documentation with no real content will pass the structural check.
The minimum documentation threshold is a heuristic, not a guarantee of usefulness.
