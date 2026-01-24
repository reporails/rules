---
id: G5
title: Contract Registry
category: governance
type: deterministic
detection: YAML parse for quick_ref and contracts keys in registry file
level: L6
sources: [25]
validation: first-party
see_also: [G6]
---

# Contract Registry

O(1) contract lookup, segment-aware loading.

## Contents

Registry contains:
- `quick_ref` — Contract ID to path mapping
- `contracts` — Full contract definitions with consumers
