# Evidence Chain Guide

How to link rules to source claims for auditable traceability.

## Structure

```
Source (docs/sources.yml)
  └── Claims (id, text, rules[])
        └── Rules (backed_by: source + claim)
```

## Finding Backing Claims

1. **Search sources.yml** for relevant claims:
   ```bash
   grep -i "your-keyword" docs/sources.yml
   ```

2. **Check claim text** matches rule's intent

3. **Verify source weight** aligns with desired confidence

## Adding backed_by to Rules

```yaml
# Rule frontmatter
backed_by:
  - source: source-id-from-sources-yml
    claim: claim-id-within-that-source
```

Multiple claims can back a single rule:

```yaml
backed_by:
  - source: claude-code-best-practices
    claim: keep-concise
  - source: instruction-limits-principles
    claim: line-limit
```

## Updating Source Claims

When adding `backed_by`, ensure the claim's `rules:` array includes your rule:

```yaml
# In sources.yml
claims:
  - id: keep-concise
    text: "Keep CLAUDE.md files concise"
    rules: [S1]  # Add your rule ID here
```

## Confidence Derivation (v2)

| Backing Sources | Confidence |
|-----------------|------------|
| Official (1.0) + Research (0.8+) | confirmed |
| Official (1.0) alone | high |
| Research (0.8+) or 2+ community (0.4+) | medium |
| Methodology only or no backed_by | low |

**Confirmed requires BOTH:**
1. Official source (weight 1.0) that STATES the recommendation
2. Research source (weight 0.8+) that VALIDATES it works with data

**Example upgrade path:**
```
S1 starts with:
  backed_by: [{source: claude-code-best-practices, claim: keep-concise}]
  confidence: high  # official only

Add research:
  backed_by:
    - {source: claude-code-best-practices, claim: keep-concise}
    - {source: claude-md-optimization-study, claim: optimization-improvement}
  confidence: confirmed  # official + research validation
```

## Creating New Claims

If no existing claim backs your rule:

1. Use `/extract-claims <url>` to extract claims from source
2. Add claim to appropriate source in sources.yml
3. Reference in rule's `backed_by`

## Validation

Run `/validate-rules --source-check` to verify:
- All `backed_by` references resolve
- Bidirectional links are consistent
- Confidence aligns with source weights
