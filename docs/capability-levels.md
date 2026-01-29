# Capability Levels

Capability levels describe what your AI instruction setup enables — not how "mature" it is. Different projects need different capabilities. L3 is perfect for a solo project; L6 fits complex monorepos.

## 6-Level Scale

The level detection decides which rules are relevant based on detected features.

| Level | Name | What It Enables | Key Indicators |
|-------|------|-----------------|----------------|
| **L1** | Absent | No AI instructions | Missing or unmodified `/init` output |
| **L2** | Basic | Single-file instructions | 30-200 lines, stack + commands + constraints |
| **L3** | Structured | External references, organized content | @imports, < 200 lines root |
| **L4** | Abstracted | Path-scoped rules, context-aware loading | .claude/rules/, hierarchical memory |
| **L5** | Governed | Team policies, compliance tracking | Org policies deployed, metrics |
| **L6** | Adaptive | Map-driven navigation, contracts | YAML backbone, component-contract binding |

> **Note:** L1-L4 patterns are documented in official sources. L5-L6 patterns are Reporails methodology derived from enterprise software practices.

---

## Level Descriptions

### Level 1: Absent/Generated
- No CLAUDE.md file, or unreviewed `/init` output
- Contains auto-detected info (often wrong or redundant)
- **Risk:** Inconsistent behavior, wasted tokens on irrelevant context
- **Fix:** Review and customize within 30 minutes
- **Primary rules:** None (file doesn't exist or isn't functional)

### Level 2: Basic
- Contains core sections: stack, commands, constraints
- 30-200 lines, may include code style rules (antipattern)
- Version controlled but no @imports
- **Risk:** Token bloat, instruction dilution as file grows
- **Fix:** Extract details to @imports, remove code style rules
- **Primary rules:** S1, C1, C2, C4, C7, C8, C9, C10, C12, CLAUDE_M1

### Level 3: Structured
- Uses @imports to external documentation
- Root file focuses on pointers, not content
- No embedded code snippets
- Clear markdown structure with headings
- **Risk:** Import references may become stale
- **Fix:** Implement .claude/rules/ for path-scoped loading
- **Primary rules:** S2, S3, S5, C3, C6, C11, E6, E7, M1, M2

### Level 4: Abstracted
- Implements .claude/rules/ directory
- Path-scoped rules for different code areas
- Hooks handle formatting/linting
- Root file < 100 lines
- CLAUDE.local.md for personal preferences
- **Risk:** Complexity if not well-documented
- **Fix:** Add governance processes for enterprise scale
- **Primary rules:** CLAUDE_S2, CLAUDE_S3, E1, E3, E4, E5, E8, CLAUDE_M2

### Level 5: Governed
- Organization-level policies deployed
- All changes go through PR review
- Metrics dashboard tracking compliance
- Automated CI/CD checks
- ROI documented
- **Risk:** Process overhead if not automated
- **Fix:** Add navigation maps for complex codebases
- **Primary rules:** CLAUDE_G1, G1, G2, G3, G7, M3, M4

### Level 6: Adaptive
- YAML backbone (`.reporails/backbone.yml`) as complete path index
- Navigation maps for components, platform, contracts
- Session start ritual: read maps before searching
- Component-contract binding for segment-aware loading
- MUST/MUST NOT rule format with source traceability
- Architecture tests enforce contracts
- **Risk:** Map staleness; requires maintenance discipline
- **Applicability:** See "When to Use Level 6" below
- **Primary rules:** S4, C5, E2, G4, G5, G6, M5

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
| File exists | — | - | + | + | + | + | + |
| Manually reviewed | CLAUDE_M1 | - | + | + | + | + | + |
| Core sections present | C1 | - | + | + | + | + | + |
| Explicit instructions | C2 | - | + | + | + | + | + |
| Antipatterns documented | C4 | - | + | + | + | + | + |
| Emphasis discipline | C7 | - | + | + | + | + | + |
| Instructions not philosophy | C8 | - | + | + | + | + | + |
| Project description | C9 | - | + | + | + | + | + |
| Has NEVER statements | C10 | - | + | + | + | + | + |
| Has version/date | C12 | - | + | + | + | + | + |
| Size limits | S1 | - | + | + | + | + | + |
| Uses @imports | S2 | - | - | + | + | + | + |
| No code snippets | S3 | - | - | + | + | + | + |
| Clear markdown structure | S5 | - | - | + | + | + | + |
| Context-specific content | C3 | - | - | + | + | + | + |
| Single source of truth | C6 | - | - | + | + | + | + |
| Links valid | C11 | - | - | + | + | + | + |
| Code block limit | E6 | - | - | + | + | + | + |
| Import count | E7 | - | - | + | + | + | + |
| Version controlled | M1 | - | - | + | + | + | + |
| Review process | M2 | - | - | + | + | + | + |
| .claude/rules/ used | CLAUDE_S2 | - | - | - | + | + | + |
| Path-scoped rules | CLAUDE_S3 | - | - | - | + | + | + |
| Deterministic tools | E1 | - | - | - | + | + | + |
| Purpose-based reading | E3 | - | - | - | + | + | + |
| Memory reference | E4 | - | - | - | + | + | + |
| Grep efficiency | E5 | - | - | - | + | + | + |
| Context window awareness | E8 | - | - | - | + | + | + |
| Rule snippet length | CLAUDE_M2 | - | - | - | + | + | + |
| Org policies deployed | CLAUDE_G1 | - | - | - | - | + | + |
| Team governance | G1 | - | - | - | - | + | + |
| Security rules ownership | G2 | - | - | - | - | + | + |
| Ownership assignment | G3 | - | - | - | - | + | + |
| Metrics/CI checks | G7 | - | - | - | - | + | + |
| Change management | M3 | - | - | - | - | + | + |
| No conflicting rules | M4 | - | - | - | - | + | + |
| YAML backbone | S4 | - | - | - | - | - | + |
| MUST/MUST NOT format | C5 | - | - | - | - | - | + |
| Session start ritual | E2 | - | - | - | - | - | + |
| Contract registry | G4 | - | - | - | - | - | + |
| Component-contract binding | G5 | - | - | - | - | - | + |
| Architecture tests | G6 | - | - | - | - | - | + |
| Map staleness prevention | M5 | - | - | - | - | - | + |

**Legend:** `+` Required | `-` Not expected

---

## Level Progression

| Transition | Key Actions | Effort |
|------------|-------------|--------|
| L1 → L2 | Review /init output, add core sections | 1-2 hours |
| L2 → L3 | Extract to @imports, remove code style rules | 2-4 hours |
| L3 → L4 | Implement .claude/rules/, configure hooks | 1-2 days |
| L4 → L5 | Deploy org policies, build metrics dashboard | 2-4 weeks |
| L5 → L6 | Design YAML backbone, implement contract registry | 4-8 weeks |

---

## Recommended Levels by Context

| Context | Target | Rationale |
|---------|--------|-----------|
| Solo developer | L3 | Structure without overhead |
| Small team (2-5) | L3-L4 | Shared standards, modular ownership |
| Medium team (6-20) | L4 | Full optimization |
| Large team (20+) | L5 | Governance required |
| Complex monorepo | L6 | Map-driven navigation essential |
| Platform/SDK teams | L6 | Contract enforcement needed |

---

## Assessment

**Score** and **Level** are independent metrics:

- **Level (L1-L6)**: Capability tier — determined by detected features
- **Score (0-10)**: Compliance — how well you follow rules at your level

A simple CLAUDE.md project (L2) can score 10/10 if it follows all L2 rules perfectly.

### Step 1: Detect Level

Level is determined by **features present**, not by score:

| Feature | Detected Level |
|---------|---------------|
| backbone.yml present | L6 (Adaptive) |
| 3+ components or shared files | L5 (Governed) |
| `.claude/rules/` directory | L4 (Abstracted) |
| @imports or multiple instruction files | L3 (Structured) |
| CLAUDE.md exists | L2 (Basic) |
| No CLAUDE.md | L1 (Absent) |

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

**Example:** 10 rules checked, 1 critical violation
- Possible: 10 × 2.5 = 25 points
- Lost: 5.5 (one critical)
- Earned: 25 - 5.5 = 19.5
- Score: (19.5 / 25) × 10 = **7.8**

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
| Deterministic | 32 | OpenGrep pattern match | None |
| Semantic | 10 | OpenGrep gate + LLM evaluation | Per check |

### Deterministic Rules (32)

100% certainty via OpenGrep pattern matching. No LLM needed.

### Semantic Rules (10)

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