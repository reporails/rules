# Reporails Thresholds

Where sources say "concise" or "sparingly," we made it measurable.

This document is the source of truth for Reporails threshold interpretations. When external sources provide qualitative guidance, we define specific, enforceable thresholds.

## Threshold Decisions

| Rule | Threshold | Source says | Our interpretation |
|------|-----------|-------------|-------------------|
| S1 | 200 lines max | "< 300 lines is best" | Stricter threshold provides safety margin; 200 encourages @imports earlier |
| C7 | 5 emphases max | "use sparingly" | 5 is practical limit before emphasis loses meaning |
| S3 | 10 lines max | "keep concise" | Code blocks should be examples, not implementations |
| E6 | 10 lines max | "keep concise" | Same as S3 — code blocks are examples |
| E7 | 10 imports max | "hierarchical structure" | Practical limit before import chains become confusing |
| CLAUDE_M7 | 40 lines max | — | Rule files should be focused; longer rules should split |
| C12 | Has version/date | — | Change tracking enables maintenance discipline |

## Rationale

### Why stricter than sources?

Sources provide general guidance. We provide enforcement.

"Keep files concise" doesn't fail a lint check. "Over 200 lines" does.

Our thresholds are:
- **Measurable** — OpenGrep can detect them
- **Enforceable** — Clear pass/fail
- **Conservative** — Better to split early than refactor later

### Why these specific numbers?

| Threshold | Derivation |
|-----------|------------|
| 200 lines | ~150-200 instructions is frontier LLM attention limit (humanlayer research) |
| 5 emphases | Empirical: beyond 5, agents treat nothing as important |
| 10 lines code | Code blocks are examples; full implementations belong in actual code |
| 10 imports | Cognitive limit; deeper hierarchies need .claude/rules/ instead |
| 40 lines rule | Rule files are focused instructions, not documentation |

### Adjusting thresholds

These are defaults. Users can override via `.reporails/config.yml`:

```yaml
overrides:
  S1-root-too-long:
    disabled: true  # "I know my file is long"
  C7-too-many-emphases:
    severity: low   # "I use emphasis differently"
```

## Governance Best Practices

Rules without external sources but based on enterprise patterns:

| Rule | Pattern | Source |
|------|---------|--------|
| G3 | Security rules need qualified owners | Standard governance practice |
| C12 | Version/date enables change tracking | Maintenance discipline |

These are marked as "Reporails governance recommendations" rather than source-backed requirements.

## Sources

This document is cited by rules that use Reporails-defined thresholds:
- S1, S3, C7, C12, E6, E7, CLAUDE_M7, G3

For rules backed by external sources, see `docs/sources.yml`.
