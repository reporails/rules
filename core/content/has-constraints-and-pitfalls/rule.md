---
id: "CORE:C:0010"
slug: has-constraints-and-pitfalls
title: Has Constraints and Pitfalls
category: content
type: deterministic
level: L2
backed_by:
- claude-md-optimization-study
- osmani-ai-coding-workflow
targets: '{{instruction_files}}'
checks:
- id: "CORE:C:0010:check:0001"
  type: deterministic
  negate: true
  severity: high
question: "Do the instruction files document project-specific pitfalls, constraints,
  or anti-patterns?"
criteria:
- At least one instruction file describes a known pitfall, technical constraint,
  or approach to avoid
- Pitfalls are project-specific (reference specific libraries, APIs, or codebase
  patterns)
- At least one pitfall includes the correct alternative approach or workaround
---

# Has Constraints and Pitfalls

The instruction files must describe project-specific constraints, known pitfalls, or
approaches to avoid.

## Pass / Fail

**Pass:** The instruction file contains:
```
## Pitfalls
- The ORM does not support nested transactions. Always use `db.begin_nested()` for
  savepoints instead of nested `db.begin()` calls.
- The Redis client silently reconnects on timeout. Always check `client.connected`
  before assuming a failed operation truly failed.
- NEVER use `datetime.now()` -- always use `datetime.utcnow()` or the project's
  `get_current_time()` helper which respects timezone configuration.
```
Each pitfall is specific, explains the problem, and gives the correct approach.
**Fail:** The instruction file documents commands, structure, and style conventions but has no
mention of things to avoid, known issues, gotchas, or anti-patterns. The agent has no
way to avoid known mistakes without discovering them through trial and error.

## Limitations

Cannot verify that documented pitfalls are still relevant or accurate. A pitfall fixed
three versions ago would still pass. Cannot assess whether the pitfall set is complete
for the project's complexity. Cannot distinguish between genuine project pitfalls and
generic programming advice.
