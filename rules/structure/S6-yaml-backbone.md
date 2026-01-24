---
id: S6
title: YAML Backbone
category: structure
type: deterministic
detection: File existence check for .reporails/backbone.yml
level: L6
antipatterns:
  - id: A13
    name: Hard-linking rules
    severity: medium
sources: [25]
validation: first-party
see_also: [M6]
---

# YAML Backbone

Eliminates grep/find for navigation.

## Contents

backbone.yml contains:
- `working_dir` — Project root
- `navigation_maps` — Links to component/platform/contract maps
- `high_risk_areas` — Paths requiring extra caution

## Usage

At session start, read backbone.yml to understand project structure before exploring.
