---
name: generate-rule
description: Generate a new rule with proper schema and OpenGrep patterns
---

# /generate-rule

Generate a new rule with proper schema and OpenGrep patterns.

## Usage

```
/generate-rule <id> <scope> <title> [--agent <name>]
```

- `<id>`: Rule ID (e.g., S1, C1, CLAUDE_S1)
- `<scope>`: `core` or agent name (e.g., `claude`)
- `<title>`: Short title for the rule
- `--agent <name>`: Agent for template resolution during validation (default: `claude`)

## Examples

```
/generate-rule S1 core "Size Limits"
/generate-rule CLAUDE_S4 claude "Hierarchical Memory"
/generate-rule S1 core "Size Limits" --agent cursor
```

## Workflow

### Step 1: Gather Information

Before generating, collect:

1. **What it checks** — specific, measurable criteria
2. **Why it matters** — one sentence impact
3. **Type decision** — can OpenGrep fully decide?
4. **Good/Bad patterns** — concrete examples
5. **Sources** — find relevant URLs from `docs/sources.yml`

### Step 2: Determine Type

| Question | Answer | Type |
|----------|--------|------|
| Can OpenGrep fully decide? | Yes | `deterministic` |
| OpenGrep partial, LLM fills gaps? | Yes | `semantic` |

Refer to `.claude/rules/opengrep.md` for decision guide.

### Step 2b: Source-Claim Linking

Link rules to specific claims in `docs/sources.yml`:

1. **Find backing claims** — Search sources.yml for claims that support this rule
2. **Add `backed_by`** — Reference source ID + claim ID pairs in frontmatter
3. **Update source claims** — Add rule ID to claim's `rules:` array if not present

```yaml
# In rule frontmatter
backed_by:
  - source: claude-code-best-practices
    claim: keep-concise
  - source: instruction-limits-principles
    claim: line-limit
```

**Bidirectional consistency required:**
- Rule's `backed_by` must reference existing source + claim
- Source's claim `rules:` array must include this rule ID

### Step 2c: Determine Confidence

Based on backing source weights from `docs/sources.yml`:

| Weight | Authority | Rule Extraction |
|--------|-----------|-----------------|
| 1.0 | Official | MUST include if source explicitly states pattern |
| 0.8 | Research | SHOULD include if data supports pattern |
| 0.6 | Methodology | Include as Reporails recommendation |
| 0.4 | Community | MAY include if corroborated by weight >= 0.6 source |

Set `confidence` in frontmatter based on `backed_by` sources:

**Confidence Levels (v2):**

| Level | Requirements | Example |
|-------|--------------|---------|
| confirmed | Official (1.0) + Research validates (0.8+) | S1: Anthropic says + Arize measured |
| high | Official source (1.0) | C9: Anthropic recommends |
| medium | Research (0.8+) OR 2+ community (0.4+) | Pattern from multiple blogs |
| low | Methodology only or no backing | G5: Reporails pattern |

**Confidence Decision Tree:**

```
Has official backing (weight 1.0)?
├── Yes
│   └── Has research validation (weight 0.8+)?
│       ├── Yes → confirmed
│       └── No → high
└── No
    └── Has research backing (weight 0.8+)?
        ├── Yes → medium
        └── No
            └── Has 2+ community sources (weight 0.4+)?
                ├── Yes → medium
                └── No → low
```

**Confidence Level Details:**

**confirmed:**
- Has official backing (weight 1.0) that STATES the recommendation
- Has research backing (weight 0.8+) that VALIDATES it works
- Research must measure impact, not just repeat the official claim
- Example: "Keep under 300 lines" (official) + "+5.19% improvement" (research)

**high:**
- Has `backed_by` with at least one official source (weight 1.0)
- Source claim explicitly states the pattern/threshold
- No contradicting sources
- Does NOT require research validation

**medium:**
- Has `backed_by` with at least one research source (weight 0.8+)
- OR multiple community sources (weight 0.4+) agree
- Pattern is inferred but reasonable

**low:**
- Based primarily on methodology sources (weight 0.6)
- OR Reporails methodology without external validation
- OR pattern is extrapolated beyond source claims
- OR no `backed_by` references (methodology-only rule)

### Step 3: Generate Files

Create both .md and .yml files. For templates, see [templates.md](templates.md).

### Step 4: Resolve Templates & Validate

**Do not save files until all validations pass.**

1. Load agent config: `agents/{agent}/config.yml` (default: `claude`)
2. Replace `{{var}}` placeholders with values from `vars:` section
3. Run OpenGrep validation on resolved file:
   ```bash
   ~/.reporails/bin/opengrep scan --config {resolved.yml} .
   ```
4. Exit 0 or 1 = valid, Exit 2 or 7 = fix before saving

See [opengrep-patterns.md](opengrep-patterns.md) for validation details.

### Step 5: Save Files

| Scope | Location |
|-------|----------|
| core | `core/{category}/{id}-{slug}.md` and `.yml` |
| claude | `agents/claude/rules/{id}-{slug}.md` and `.yml` |

### Step 6: Update References

- [ ] Add to `see_also` in related rules if cross-referenced
- [ ] Update `capability-levels.md` if affects level detection
- [ ] Run `/add-changelog-entry`

## Reference Files

- [templates.md](templates.md) — Frontmatter and file templates
- [opengrep-patterns.md](opengrep-patterns.md) — OpenGrep pattern examples
- [common-mistakes.md](common-mistakes.md) — Common mistakes and fixes
- [evidence-chain.md](evidence-chain.md) — Source-claim linking guide
