---
id: CLAUDE_G1
title: Organization-Level Policies
category: governance
type: deterministic
confidence: high
backed_by:
  - source: claude-code-settings
    claim: settings-hierarchy
  - source: claude-code-memory
    claim: memory-hierarchy
checks:
  - id: CLAUDE_G1-no-managed-policy
    name: No organization-level policy file
    severity: medium
sources:
  - "https://code.claude.com/docs/en/settings"
  - "https://claude.com/blog/how-anthropic-teams-use-claude-code"
see_also: [G1, CLAUDE_S2]
---

# Organization-Level Policies

L5+ requires managed-settings.json in system directory.

## Pattern

**Good:** /etc/claude-code/managed-settings.json with org policies
**Bad:** No organization-level managed settings deployed
