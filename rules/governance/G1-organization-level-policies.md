---
id: G1
title: Organization-Level Policies
category: governance
type: deterministic
detection: File existence check at policy paths
level: L5+
scoring: 5
sources: [2, 4]
---

# Organization-Level Policies

Consistent rules across all projects.

## Deployment

Deploy organization-wide policies via MDM, Group Policy, or config management:
- Linux/macOS: `/etc/claude/managed-policy.md`
- Windows: `%PROGRAMDATA%\claude\managed-policy.md`
