---
id: M3
title: Change Management
category: maintenance
type: heuristic
detection: pattern-regex for approval matrix table or change process documentation
question: Is there a documented change management process for instruction files?
criteria: Pass if approval matrix or process exists; fail if no documented change control
level: L5+
sources: [7]
---

# Change Management

Predictable, controlled updates.

## Approval Matrix

| Change Type | Approval | Timeline |
|-------------|----------|----------|
| Org policy | Security + Platform | 1 week |
| Project CLAUDE.md | Tech lead | 1-2 days |
| Personal preferences | Self-service | Immediate |
