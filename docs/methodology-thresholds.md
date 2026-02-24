# Reporails Thresholds

Where sources say "concise" or "sparingly," we made it measurable.

This document is the source of truth for Reporails threshold interpretations. When external sources provide qualitative guidance, we define specific, enforceable thresholds.

## Threshold Decisions

| Rule | Threshold | Source says | Our interpretation |
|------|-----------|-------------|-------------------|
| CORE:E:0002 Per-file size limit | 300 lines max | "< 300 lines is best" | Per-file limit encourages @imports earlier |
| CORE:E:0001 Total instruction budget | 32 KiB total | "hierarchical structure" | Total instruction budget across all files |

## Rationale

### Why stricter than sources?

Sources provide general guidance. We provide enforcement.

"Keep files concise" doesn't fail a lint check. "Over 300 lines" does.

Our thresholds are:
- **Measurable** — Regex or mechanical checks can detect them
- **Enforceable** — Clear pass/fail
- **Conservative** — Better to split early than refactor later

### Why these specific numbers?

| Threshold | Derivation |
|-----------|------------|
| 300 lines | ~150-300 instructions is frontier LLM attention limit (humanlayer research) |
| 32 KiB | Codex hard budget limit; effective ceiling for all agents |
| 5 hops | Cognitive limit; deeper chains need .claude/rules/ instead |

### Adjusting thresholds

These are defaults. Users can override via `.reporails/config.yml`:

```yaml
overrides:
  CORE:E:0002:
    disabled: true  # "I know my file is long"
```

## Sources

This document is cited by rules that use Reporails-defined thresholds:
- CORE:E:0002 (per-file size limit), CORE:E:0001 (total instruction budget)

For rules backed by external sources, see `docs/sources.yml`.
