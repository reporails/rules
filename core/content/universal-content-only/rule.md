---
id: "CORE:C:0007"
slug: universal-content-only
title: Universal Content Only
category: content
type: semantic
level: L2
backed_by:
- enterprise-claude-usage
- instruction-limits-principles
- using-claude-md-files
targets: '{{instruction_files}}'
checks:
- id: "CORE:C:0007:check:0001"
  type: deterministic
  severity: medium
- id: "CORE:C:0007:check:0002"
  type: semantic
  prompt: "Does the main instruction file contain only universal content, or does it include domain-specific content that belongs in supplementary files?"
  severity: medium
question: "Does the main instruction file contain only content relevant to most agent
  tasks?"
criteria:
- The main instruction file focuses on project-wide conventions, commands, and 
  constraints
- Specialized or niche content is either absent from the main file or referenced
  via imports
- The main file does not contain lengthy reference documentation for narrow use 
  cases
---

# Universal Content Only

The main instruction file must contain only guidance that applies to the majority of
agent tasks.

## Pass / Fail

**Pass:** The main CLAUDE.md contains project-wide conventions (structure, commands, style, boundaries)
and imports specialized content:
```
# MyProject
A REST API for order management.

## Commands
npm run test -- --coverage
npm run build

## Constraints
- NEVER modify generated files in src/generated/

See docs/api-setup.md for API gateway configuration.
See docs/database.md for migration procedures.
```
Niche setup guides live in imported files, keeping the main file focused.
**Fail:** The main CLAUDE.md is 2000 lines long and includes detailed API documentation for a
rarely-used internal service, step-by-step database migration guides, historical
architecture decisions, and onboarding instructions for a specific CI provider --
alongside the core project conventions. Most of this content is irrelevant to typical
agent tasks.

## Limitations

"Universally applicable" is context-dependent. In a small project with one developer,
everything might be universally applicable. The semantic gate must judge relevance
relative to the project's scope. Cannot determine actual task frequency distribution
to verify whether content truly applies to "the majority" of tasks.
