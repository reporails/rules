---
id: "CORE:C:0011"
slug: has-workflow-instructions
title: Has Workflow Instructions
category: content
type: deterministic
level: L2
backed_by:
- dometrain-claude-md-guide
- spec-writing-for-agents
- using-claude-md-files
targets: '{{instruction_files}}'
checks:
- id: "CORE:C:0011:check:0001"
  type: deterministic
  negate: true
  severity: high
question: "Do the instruction files describe development workflows like branching,
  review, or deployment?"
criteria:
- At least one instruction file describes a development workflow (branching, PR 
  process, deployment, or release)
- Workflows include concrete steps or conventions (not just "we use git")
- At least one workflow topic includes enough detail for the agent to follow it 
  independently
---

# Has Workflow Instructions

The instruction files must describe development workflows such as branching, deployment,
or review processes.

## Pass / Fail

**Pass:** The instruction file contains:
```
## Workflow
- Create feature branches from `develop` with prefix: `feat/`, `fix/`, `chore/`
- PR requires 1 approval before merge
- Squash merge to main
- Tag releases with `vX.Y.Z` format
- Run `make deploy-staging` to deploy to staging after merge
```
Covers branching, review, merge strategy, and deployment.
**Fail:** The instruction file documents code conventions and commands but never mentions how to
branch, what the PR process is, how to deploy, or any development workflow. The agent
creates branches with arbitrary names and has no idea how to get code reviewed or
released.

## Limitations

Cannot verify that documented workflows match actual team practice. A project
documenting a PR-based workflow while actually committing directly to main would still
pass. Cannot assess whether workflows are complete for the project's deployment
complexity. Projects with no deployment (e.g., libraries) may legitimately have minimal
workflow documentation.
