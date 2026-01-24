---
id: G7
title: Architecture Tests
category: governance
type: deterministic
detection: Test file existence and CI integration check
level: L6
sources: [25]
validation: first-party
antipatterns:
  - id: A16
    name: Missing architecture tests
    severity: medium
---

# Architecture Tests

Enforces contracts through automated validation.

## Verification

Architecture tests verify:
- Boundary violations (layers don't bypass contracts)
- Import rules (modules only import from allowed dependencies)
- Contract compliance (implementations match interfaces)
