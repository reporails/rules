---
id: "CORE:C:0009"
slug: has-style-conventions
title: Has Style Conventions
category: content
type: deterministic
level: L2
backed_by:
- claude-md-optimization-study
- dometrain-claude-md-guide
- osmani-ai-coding-workflow
- spec-writing-for-agents
targets: '{{instruction_files}}'
checks:
- id: "CORE:C:0009:check:0001"
  type: deterministic
  negate: true
  severity: high
question: "Do the instruction files describe coding style conventions beyond linter
  scope?"
criteria:
- At least one instruction file describes naming patterns, architectural 
  preferences, or design conventions
- Conventions are project-specific (not generic advice like "use good names")
- At least two distinct convention topics are covered (e.g., naming and 
  architecture, or naming and patterns)
---

# Has Style Conventions

The instruction files must describe coding style conventions such as naming patterns,
architectural preferences, or output examples.

## Pass / Fail

**Pass:** The instruction file contains:
```
## Conventions
- Name React components PascalCase (e.g., UserProfileCard)
- Use custom hooks for shared state (useAuth, useCart)
- Prefer composition over inheritance
- Service functions return Result<T, Error>, never throw
- Example:
  ```ts
  export function getUser(id: string): Result<User, NotFoundError> {
    // ...
  }
  ```
```
Covers naming, patterns, and includes a concrete example.
**Fail:** The instruction file documents commands and project structure but has no mention of
coding style, naming conventions, component patterns, or architectural preferences.
The agent must reverse-engineer conventions from existing code.

## Limitations

Cannot verify that documented conventions are consistently followed in the codebase.
A project claiming PascalCase components while having snake_case components everywhere
would still pass. Cannot assess whether the conventions are complete for the project's
technology stack.
