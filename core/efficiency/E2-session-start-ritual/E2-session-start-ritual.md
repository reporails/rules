---
id: E2
title: Session Start Ritual
category: efficiency
type: deterministic
backed_by: []  # Tier: experimental (community pattern, L6-only)
checks:
  - id: E2-no-ritual-section
    name: No session start ritual section in instructions
    severity: critical
  - id: E2-ritual-no-backbone-ref
    name: Session ritual does not reference backbone.yml
    severity: high
  - id: E2-ritual-no-numbered-steps
    name: Session ritual lacks numbered steps (1. 2. 3.)
    severity: high
  - id: E2-ritual-no-map-reference
    name: Session ritual does not mention maps or navigation
    severity: high
  - id: E2-ritual-no-before-searching
    name: Session ritual missing 'before searching' guidance
    severity: low
  - id: E2-no-context-loading
    name: No context loading instructions for session start
    severity: high
sources: []
see_also: [S4, G4]
---

# Session Start Ritual

L6 projects require explicit session start rituals with numbered steps referencing backbone/maps.

## Pattern

**Good:** "## Session Start\n1. Read backbone.yml\n2. Identify relevant maps\n3. Load context before searching"
**Bad:** No guidance on how to start a session, or ritual without backbone/map references

## Required Elements

- Dedicated section header (Session Start, Initialization, Before You Begin)
- Reference to backbone.yml or .reporails/backbone
- Numbered steps (1. 2. 3.)
- Map/navigation references
- "Before searching" or "read first" guidance
- Context loading instructions
