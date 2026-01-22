---
id: G5
title: Contract Registry
category: governance
type: heuristic
detection: YAML structure validation; cannot verify contracts are meaningful
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
