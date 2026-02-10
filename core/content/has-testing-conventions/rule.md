---
id: "CORE:C:0004"
slug: has-testing-conventions
title: Has Testing Conventions
category: content
type: deterministic
level: L2
backed_by:
- claude-md-optimization-study
- osmani-ai-coding-workflow
- spec-writing-for-agents
targets: '{{instruction_files}}'
checks:
- id: "CORE:C:0004:check:0001"
  type: deterministic
  negate: true
  severity: high
question: "Do the instruction files describe testing conventions, test frameworks,
  or how to run tests?"
criteria:
- At least one instruction file mentions a test framework, test runner, or test 
  execution command
- "Testing information includes at least one of: how to run tests, how to name test
  files, or which framework to use"
- The testing content is specific to the project (not generic advice like "write
  tests")
---

# Has Testing Conventions

The instruction files must describe testing conventions, frameworks, or test execution
commands.

## Pass / Fail

**Pass:** The instruction file contains:
```
## Testing
Run `pytest tests/` for unit tests. Name test files `test_*.py`. Each test
function should start with `test_`. Use fixtures from `conftest.py` for
database setup.
```
Covers framework, execution command, naming convention, and shared fixtures.
**Fail:** The instruction file has commands and style guides but no mention of testing. The agent
does not know which test framework to use, how to name test files, or how to run the
test suite.

## Limitations

Cannot verify that described testing conventions match the actual test infrastructure.
A project claiming to use pytest while actually using unittest would still pass. Cannot
assess whether the conventions are complete enough for the project's test complexity.
