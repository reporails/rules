---
name: audit-evidence-chain
description: Audit trust architecture and generate metrics for source-claim-rule integrity
---

# /audit-evidence-chain

Audit the evidence chain and generate trust metrics.

## Usage

```
/audit-evidence-chain [options]
```

**Options:**
- `--output <path>`: Output metrics file (default: `.reporails/trust-metrics.yml`)
- `--report`: Generate human-readable report (`.reporails/audit-report.md`)
- `--fail-below <n>`: Exit non-zero if trust score < n (for CI)
- `--verbose`: Show detailed validation for each rule

## Examples

```
/audit-evidence-chain                      # Run audit, output metrics
/audit-evidence-chain --report             # Include human-readable report
/audit-evidence-chain --fail-below 70      # CI gate at 70% trust score
/audit-evidence-chain --verbose            # Show all rule details
```

## Workflow

Follow: [@.shared/workflows/evidence-audit.md](../../../.shared/workflows/evidence-audit.md)

## Reference

- [@.shared/knowledge/evidence-chain.md](../../../.shared/knowledge/evidence-chain.md) - Validation checks
- [trust-metrics-schema.md](trust-metrics-schema.md) - Metrics file schema

## Quick Reference

**Trust score weights:**

| Confidence | Weight |
|------------|--------|
| confirmed | 1.0 |
| high | 0.8 |
| medium | 0.5 |
| low | 0.2 |

**Error codes:** E4001-E4011 (errors), W4001-W4002 (warnings)
