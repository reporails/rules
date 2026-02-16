---
id: CORE:C:0002
slug: verification-build-commands
title: Verification and Build Command Documentation
category: content
type: deterministic
level: L1
backed_by:
- agents-md-spec
- copilot-cli-best-practices
- copilot-custom-instructions
- instruction-limits-principles
targets: '{{instruction_files}}'
checks:
- id: CORE.C.0002.file-exists
  type: mechanical
  severity: medium
  name: file-exists
  check: file_exists
- id: CORE.C.0002.has-required-sections
  type: deterministic
  severity: medium
  name: has-required-sections
- id: CORE.C.0002.no-anti-sections
  type: deterministic
  severity: medium
  name: no-anti-sections
---

# Verification and Build Command Documentation

Root instruction files SHOULD document the project's build, test, and lint commands with full flags and expected behavior

## Pass / Fail

### Pass

~~~~markdown
## Commands

- Build: `npm run build` (compiles TS to dist/)
- Test: `npm test -- --coverage` (Jest, must pass before commit)
- Lint: `npm run lint` (ESLint + Prettier, auto-fix with --fix)
- Dev: `npm run dev` (port 3000, hot reload)
~~~~

### Fail

~~~~markdown
## Development

Use the standard build tools.
Run tests before committing.
Make sure linting passes.
~~~~

## Limitations

Cannot verify commands are syntactically valid or runnable. Cannot detect outdated commands that no longer work.
