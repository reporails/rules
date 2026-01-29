# Trust Metrics Schema

Schema for `.reporails/trust-metrics.yml` output file.

## Schema Version

```yaml
schema_version: 1
```

## Full Schema

```yaml
# Metadata
generated: string (ISO 8601 timestamp)
schema_version: 1

# Summary metrics
summary:
  total_rules: integer
  trust_score: integer (0-100)

# Rule breakdown
rules:
  by_tier:
    confirmed: integer
    high: integer
    medium: integer
    low: integer
  
  by_backing:
    official: integer      # Rules with at least one official source
    research: integer      # Rules with at least one research source
    community: integer     # Rules with at least one community source
    experimental: integer   # Rules with no official backing
    unbacked: integer      # Rules with no backed_by

# Claim breakdown
claims:
  total: integer
  enforced: integer        # Claims with non-empty rules[]
  orphaned: integer        # Claims with empty rules[]

# Source breakdown
sources:
  total: integer
  by_type:
    official: integer
    research: integer
    community: integer
    experimental: integer

# Validation results
validation:
  errors: integer
  warnings: integer
  issues:
    - type: enum (error, warning)
      code: string (E4001, W4001, etc.)
      rule: string (optional, rule ID)
      source: string (optional, source ID)
      claim: string (optional, claim ID)
      message: string
```

## Trust Score Calculation

```python
weights = {
    'confirmed': 1.0,
    'high': 0.8,
    'medium': 0.5,
    'low': 0.2
}

weighted_sum = sum(max(source.weight for source in rule.backed_by) or 0 for rule in rules)
max_possible = len(rules) * 1.0  # If all were confirmed

trust_score = round((weighted_sum / max_possible) * 100)
```

## Example Output

```yaml
generated: "2025-01-28T12:00:00Z"
schema_version: 1

summary:
  total_rules: 42
  trust_score: 71

rules:
  by_tier:
    confirmed: 5
    high: 18
    medium: 7
    low: 12
  
  by_backing:
    official: 24
    research: 12
    community: 8
    experimental: 12
    unbacked: 0

claims:
  total: 87
  enforced: 74
  orphaned: 13

sources:
  total: 21
  by_type:
    official: 12
    research: 3
    community: 5
    experimental: 1

validation:
  errors: 0
  warnings: 2
  issues:
    - type: warning
      code: W4001
      source: keepachangelog
      claim: unreleased-section
      message: "Claim has no rules referencing it"
    - type: warning
      code: W4001
      source: jetbrains-junie-guidelines
      claim: guidelines-structure
      message: "Claim has no rules referencing it"
```

## CI Usage

```yaml
# GitHub Actions example
- name: Audit evidence chain
  run: |
    ails audit-evidence-chain --fail-below 70
    
# The command exits:
#   0 if trust_score >= threshold
#   1 if trust_score < threshold
#   2 if validation errors exist
```

## Thresholds

| Level | Trust Score | Meaning |
|-------|-------------|---------|
| Excellent | 90+ | Most rules confirmed or high |
| Good | 70-89 | Strong evidence backing |
| Acceptable | 50-69 | Mixed backing |
| Poor | < 50 | Mostly experimental/unbacked |

Recommended CI threshold: **70%**
