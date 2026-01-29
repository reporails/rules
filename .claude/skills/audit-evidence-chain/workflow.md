# Evidence Audit Workflow

```mermaid
flowchart TD
    START([/audit-evidence-chain]) --> LOAD[Load rules + sources.yml]
    LOAD --> MAPS[Build lookup maps]
    MAPS --> CHECK1[Check 1: backed_by references exist]
    CHECK1 --> CHECK2[Check 2: Bidirectional consistency<br/>rule.backed_by and claim.rules]
    CHECK2 --> CHECK3[Check 3: Confidence alignment<br/>matches source weights]
    CHECK3 --> CHECK4[Check 4: Orphaned claims<br/>claims with no rules]
    CHECK4 --> CHECK5[Check 5: Source admission<br/>weight >= 0.4]
    CHECK5 --> SCORE[Calculate trust score]
    SCORE --> OUTPUT[Generate metrics + report]
    OUTPUT --> CI{--fail-below N?}
    CI -->|yes| THRESH{score >= N?}
    THRESH -->|yes| EXIT0([Exit 0])
    THRESH -->|no| EXIT1([Exit 1])
    CI -->|no| EXIT0
```

## Trust Score Calculation

```python
weights = {
    'confirmed': 1.0,    # Official + research validated
    'high': 0.8,         # Official recommendation
    'medium': 0.5,       # Community consensus
    'experimental': 0.2  # Community-only or no backing
}

weighted_sum = sum(max(source.weight for source in rule.backed_by) or 0 for rule in rules)
trust_score = (weighted_sum / len(rules)) * 100
```

## Output Files

| File | Purpose |
|------|---------|
| `.reporails/trust-metrics.yml` | Machine-readable metrics for CI |
| `.reporails/audit-report.md` | Human-readable report (with `--report`) |

## When to Run

- After rule changes (create, update, delete)
- After source changes (new claims, weight updates)
- In CI pipeline (PR checks)
- Before releases (quality gate)
