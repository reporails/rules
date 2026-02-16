---
id: CORE:C:0001
slug: include-project-context
title: Project Context Specification
category: content
type: deterministic
level: L1
backed_by:
- agents-md-spec
- dometrain-claude-md-guide
- instruction-limits-principles
- spec-writing-for-agents
targets: '{{instruction_files}}'
checks:
- id: CORE.C.0001.file-exists
  type: mechanical
  severity: medium
  name: file-exists
  check: file_exists
- id: CORE.C.0001.has-required-sections
  type: deterministic
  severity: medium
  name: has-required-sections
- id: CORE.C.0001.no-generic-advice
  type: deterministic
  severity: medium
  name: no-generic-advice
- id: CORE.C.0001.no-anti-sections
  type: deterministic
  severity: medium
  name: no-anti-sections
---

# Project Context Specification

Root instruction files SHOULD include the project's technology stack, key dependencies, and project-specific conventions

## Pass / Fail

### Pass

~~~~markdown
# Project

Next.js 14 with TypeScript 5.4, Prisma ORM, PostgreSQL 15. Monorepo managed by Turborepo.

## Conventions
- Functional components with hooks
- API routes return {data, error} shape
- Feature flags via LaunchDarkly SDK
~~~~

### Fail

~~~~markdown
# My Project

This is a web application.

## Rules
- Write clean code
- Follow best practices
~~~~

## Limitations

Cannot verify version numbers are current. Cannot verify conventions match actual codebase. Pattern matching may miss non-standard formatting of tech stack sections.
