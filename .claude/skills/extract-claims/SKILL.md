---
name: extract-claims
description: Extract claims from a source URL for sources.yml
---

# /extract-claims

Extract specific claims from a source document for the evidence chain.

## Usage

```
/extract-claims <url> [--source-id <id>]
```

- `<url>`: Source URL to fetch and analyze
- `--source-id <id>`: Optional source ID (defaults to derived from URL)

## Examples

```
/extract-claims https://code.claude.com/docs/en/best-practices
/extract-claims https://arize.com/blog/claude-md-optimization-study --source-id arize-study
```

## Process

### Step 1: Source Admission Check

Before extracting, validate source meets admission criteria.

**Admission threshold:** weight >= 0.4

See [evidence-chain.md](evidence-chain.md) for weight table and auto-reject criteria.

**If rejected:** Stop. Do not proceed to claim extraction.

### Step 2: Extract Claims

1. Fetch source content from URL
2. Identify enforceable claims:
   - Specific recommendations ("Keep under 300 lines")
   - Thresholds ("No more than 5 emphases")
   - Patterns ("Use @imports for...")
   - Anti-patterns ("Don't include style rules")

### Step 3: Output YAML

```yaml
claims:
  - id: claim-id
    text: "The specific claim"
    quote: true
    section: "Section Name"
    rules: [S1, C2]
```

## Reference

- [Evidence chain](evidence-chain.md) - Admission criteria and weights

> **Path resolution:** Sources path from `backbone.artifacts.sources`. See [@.shared/knowledge/backbone-resolution.md](../../../.shared/knowledge/backbone-resolution.md).

## Quick Reference

**Good claims:**
- "Keep CLAUDE.md under 300 lines"
- "Use @imports for documentation"
- "5 IMPORTANT markers maximum"

**Bad claims:**
- "Has advice about file size"
- "Talks about imports"
- "Mentions emphasis"

**Rule mapping:**

| Category | Rules | Topics |
|----------|-------|--------|
| Structure | S1-S5 | Size, imports, hierarchy |
| Content | C1-C12 | Sections, emphasis, patterns |
| Efficiency | E1-E8 | Tools, reading, grep |
| Governance | G1-G7 | Teams, security, CI |
| Maintenance | M1-M5 | Version, review, change |
