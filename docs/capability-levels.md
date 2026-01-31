# Capability Levels

Capability levels describe what your AI instruction setup enables — not how "mature" it is. Different projects need different capabilities. L3 is perfect for a solo project; L6 fits complex monorepos.

## 6-Level Scale

L0 (Absent) means no instruction file exists — nothing to evaluate. Levels L1–L6 are the capability levels:

| Level | Name | What It Enables | Key Indicators |
|-------|------|-----------------|----------------|
| **L1** | Basic | Reviewed, tracked instruction file | Customized (not raw `/init` output), version controlled |
| **L2** | Scoped | Project-specific constraints | Size limits, core sections, content quality |
| **L3** | Structured | External references, organized content | @imports, heading hierarchy, single source of truth |
| **L4** | Abstracted | Path-scoped rules, context-aware loading | .claude/rules/, hierarchical memory |
| **L5** | Maintained | Map and index maintenance discipline | Staleness prevention, backbone completeness |
| **L6** | Adaptive | Map-driven navigation, contracts | YAML backbone, component-contract binding |

> **Note:** L1-L4 patterns are documented in official sources. L5-L6 patterns are community patterns (experimental tier) derived from enterprise software practices.

---

## Level Descriptions

### Level 1: Basic
- Instruction file exists and has been manually reviewed
- No longer raw `/init` boilerplate
- Version controlled (tracked in git)
- **Risk:** File exists but may lack structure or project-specific content
- **Fix:** Add core sections, constraints, and project description
- **Primary rules:** CLAUDE_M1, M1

### Level 2: Scoped
- Contains core sections: stack, commands, constraints
- 30-200 lines, project-specific content quality
- MUST/MUST NOT with rationale
- **Risk:** Token bloat, instruction dilution as file grows
- **Fix:** Extract details to @imports
- **Primary rules:** S1, S2, S3, S4, C1, C3, C5

### Level 3: Structured
- Uses @imports to external documentation
- Root file focuses on pointers, not content
- Single source of truth across files
- **Risk:** Import references may become stale
- **Fix:** Implement .claude/rules/ for path-scoped loading
- **Primary rules:** C2, C4, E1, E2, M2

### Level 4: Abstracted
- Implements .claude/rules/ directory
- Path-scoped rules for different code areas
- Efficiency strategies documented (reading, memory, grep)
- Root file < 100 lines
- **Risk:** Complexity if not well-documented
- **Fix:** Add governance processes for enterprise scale
- **Primary rules:** CLAUDE_S1, CLAUDE_S2

### Level 5: Maintained
- Map staleness prevention enforced
- Backbone index kept complete and accurate
- Structural changes tracked and validated
- **Risk:** Index drift if maintenance discipline lapses
- **Fix:** Automate backbone sync checks in CI
- **Primary rules:** M3, M4

### Level 6: Adaptive
- YAML backbone (`.reporails/backbone.yml`) as complete path index
- Navigation maps for components, platform, contracts
- Session start ritual: read maps before searching
- Component-contract binding for segment-aware loading
- **Risk:** Map staleness; requires maintenance discipline
- **Applicability:** See "When to Use Level 6" below
- **Primary rules:** Detection-only (backbone.yml present)

---

## When to Use Level 6

**Appropriate when:**
- Monorepo with 3+ distinct components
- Hexagonal or layered architecture with enforced boundaries
- Multiple developers needing consistent context loading
- Codebase > 50k lines with distinct domains

**Overkill when:**
- Single-component projects
- Solo developer projects
- Simple CRUD applications
- Codebases < 10k lines

---

## Capability Assessment Matrix

| Criteria | Rule | L1 | L2 | L3 | L4 | L5 | L6 |
|----------|------|----|----|----|----|----|----|
| Manually reviewed | CLAUDE_M1 | + | + | + | + | + | + |
| Size limits | S1 | - | + | + | + | + | + |
| Progressive disclosure | S2 | - | + | + | + | + | + |
| No code snippets | S3 | - | + | + | + | + | + |
| Clear markdown structure | S4 | - | + | + | + | + | + |
| Core sections present | C1 | - | + | + | + | + | + |
| Has project description | C3 | - | + | + | + | + | + |
| Has version/date | C5 | - | + | + | + | + | + |
| Single source of truth | C2 | - | - | + | + | + | + |
| Links valid | C4 | - | - | + | + | + | + |
| Code block limit | E1 | - | - | + | + | + | + |
| Import count | E2 | - | - | + | + | + | + |
| No conflicting rules | M2 | - | - | + | + | + | + |
| Version controlled | M1 | + | + | + | + | + | + |
| Hierarchical memory | CLAUDE_S1 | - | - | - | + | + | + |
| Path-scoped rules | CLAUDE_S2 | - | - | - | + | + | + |
| Map staleness prevention | M3 | - | - | - | - | + | + |
| Backbone index completeness | M4 | - | - | - | - | + | + |

**Legend:** `+` Required | `-` Not expected

> **Note:** Additional recommended rules available in [reporails/recommended](https://github.com/reporails/recommended).

---

## Level Progression

| Transition | Key Actions |
|------------|-------------|
| L1 → L2 | Add core sections, constraints, project description |
| L2 → L3 | Extract to @imports, remove code style rules |
| L3 → L4 | Implement .claude/rules/, configure hooks |
| L4 → L5 | Add map staleness prevention, backbone index completeness |
| L5 → L6 | Presence of backbone.yml triggers L6 detection |

---

## Recommended Levels by Context

| Context | Target | Rationale |
|---------|--------|-----------|
| Solo developer | L3 | Structure without overhead |
| Small team (2-5) | L3-L4 | Shared standards, modular ownership |
| Medium team (6-20) | L4 | Full optimization |
| Large team (20+) | L4 + recommended | Add governance rules from reporails/recommended |
| Complex monorepo | L5-L6 | Map maintenance + navigation essential |
| Platform/SDK teams | L6 | Contract enforcement needed |

---

## Assessment

**Score** and **Level** are independent metrics:

- **Level (L1-L6)**: Capability tier — determined by detected features
- **Score (0-10)**: Compliance — how well you follow rules at your level

A simple instruction file (L2) can score 10/10 if it follows all L2 rules perfectly.

### Step 1: Detect Level

Level is determined by **features present**, not by score:

| Feature | Detected Level |
|---------|---------------|
| backbone.yml present | L6 (Adaptive) |
| Map staleness + backbone index rules | L5 (Maintained) |
| `.claude/rules/` directory | L4 (Abstracted) |
| @imports or multiple instruction files | L3 (Structured) |
| Instruction file exists and customized | L2 (Scoped) |
| Instruction file exists (uncustomized) | L1 (Basic) |

**Detection order:** Check from L6 down. First match = detected level.

### Step 2: Calculate Score (0-10)

Weighted pass-rate scoring:

```
Score = (earned / possible) × 10
```

- `possible = rules_checked × 2.5` (default weight per rule)
- `earned = possible - violation_weights` (floored at 0)

**Severity Weights:**

| Severity | Weight | Impact |
|----------|--------|--------|
| Critical | 5.5 | Clarification loop + partial redo |
| High | 4.0 | Clarification loop |
| Medium | 2.5 | Brief clarification |
| Low | 1.0 | Minor friction |

**Example:** 18 rules checked, 1 critical violation
- Possible: 18 × 2.5 = 45 points
- Lost: 5.5 (one critical)
- Earned: 45 - 5.5 = 39.5
- Score: (39.5 / 45) × 10 = **8.8**

### Step 3: Estimate Friction

Friction estimates rework time from re-explanation loops:

| Level | Total Time | Meaning |
|-------|------------|---------|
| High | ≥20 min | Significant rework expected |
| Medium | 10-19 min | Moderate rework |
| Low | 5-9 min | Minor friction |

---

## Rule Detection Types

Rules are classified by detection method:

| Type | Count | Detection Method | LLM Cost |
|------|-------|------------------|----------|
| Deterministic | 15 | OpenGrep pattern match | None |
| Semantic | 3 | OpenGrep gate + LLM evaluation | Per check |

### Deterministic Rules (15)

100% certainty via OpenGrep pattern matching. No LLM needed.

### Semantic Rules (3)

Two-stage validation:

```
OpenGrep pattern match (gate)
    │
    ├── No match → Pass (zero LLM cost)
    │
    └── Match → LLM evaluates question + criteria
                    │
                    ├── Confirmed → Violation
                    └── Dismissed → Pass
```

Each semantic rule has:
- `question`: What to evaluate
- `criteria`: Pass/fail definition

---

## Rule Tiers

Rules are classified into tiers based on evidence backing. Tier is **derived** from backing source weights, not stored:

| Tier | Condition | Sources | Meaning |
|------|-----------|---------|---------|
| **core** | max(weights) >= 0.8 | Official (1.0), Research (0.8) | Vendor-confirmed or empirically validated |
| **experimental** | max(weights) < 0.8 | Community (0.4) only | Community patterns, not yet validated |

### Tier Derivation

```
Rule tier = core         if max(backing_source_weights) >= 0.8
          = experimental if max(backing_source_weights) < 0.8
```

**Examples:**
- Rule backed by Official (1.0) + Community (0.4) → **core** (max = 1.0)
- Rule backed by Research (0.8) → **core** (max = 0.8)
- Rule backed by Community (0.4) only → **experimental** (max = 0.4)

### Tier Filtering

Projects can filter rules by tier via `.reporails/config.yml`:

```yaml
# Only enforce validated rules (default for strict projects)
tiers:
  core: true
  experimental: false

# Include experimental patterns (default)
tiers:
  core: true
  experimental: true  # opt-out individually via CLI
```

### Promotion Path

Experimental rules can be promoted to core when external validation is added:

```
Community pattern (experimental)
    │
    ├── Vendor adopts → Official source (1.0) → core
    │
    └── Study measures impact → Research source (0.8) → core
```

This ensures core remains rock-solid while experimental patterns can mature through evidence.

---

## Sources

| Concept | Source |
|---------|--------|
| Level structure inspiration | CMMI Maturity Levels, CNCF Cloud Native Maturity Model |
| Capability (not maturity) framing | Community pattern |
| L1-L4 patterns | Official documentation (Anthropic, OpenAI, GitHub), community best practices |
| L5-L6 patterns | Community patterns (experimental tier) |

See `docs/sources.yml` for full source registry with evidence chain.
