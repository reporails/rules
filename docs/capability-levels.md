# Capability Levels

Capability levels describe what your AI instruction setup enables — not how "mature" it is. Different projects need different capabilities. L3 is perfect for a solo project; L6 fits complex monorepos.

## 6-Level Scale

L0 (Absent) means no instruction file exists — nothing to evaluate. Levels L1–L6 are the capability levels:

| Level | Name | What It Enables | Key Indicators |
|-------|------|-----------------|----------------|
| **L1** | Basic | Reviewed, tracked instruction file | Customized (not raw `/init` output), version controlled |
| **L2** | Scoped | Project-specific constraints | Size limits, core sections, content quality |
| **L3** | Structured | External references, organized content | @imports, multiple files, single source of truth |
| **L4** | Abstracted | Path-scoped rules, context-aware loading | .claude/rules/, hierarchical memory |
| **L5** | Maintained | Structural integrity, governance, navigation | Reference validation, org policy, backbone maps |
| **L6** | Adaptive | Dynamic context, extensibility, persistence | Skills, hooks, MCP servers, memory files |

> **Note:** L1-L4 patterns are documented in official sources. L5-L6 patterns are community patterns (experimental tier) derived from enterprise software practices.

---

## Level Descriptions

### Level 1: Basic
- Instruction file exists and has been manually reviewed
- No longer raw `/init` boilerplate
- Version controlled (tracked in git)
- **Risk:** File exists but may lack structure or project-specific content
- **Fix:** Add core sections, constraints, and project description

### Level 2: Scoped
- Contains core sections: stack, commands, constraints
- Concise and focused, project-specific content quality
- MUST/MUST NOT with rationale
- **Risk:** Token bloat, instruction dilution as file grows
- **Fix:** Extract details to @imports

### Level 3: Structured
- Uses @imports to external documentation
- Multiple instruction-related files
- Single source of truth across files
- **Risk:** Import references may become stale
- **Fix:** Implement path-scoped loading for different code areas

### Level 4: Abstracted
- Implements path-scoped rules (e.g., `.claude/rules/` directory)
- Different instructions load based on which files the agent works with
- Root file stays lean
- **Risk:** Complexity if not well-documented
- **Fix:** Add governance processes for enterprise scale

### Level 5: Maintained
- References resolve, indexes are current, no orphaned files
- Organization-level governance is deployed
- Structural maps guide the agent through the codebase
- **Risk:** Index drift if maintenance discipline lapses
- **Fix:** Automate validation checks in CI

### Level 6: Adaptive
- Agent discovers and loads context based on current task
- Capabilities extended via plugins, tool servers, hooks
- State persists across sessions (memory files, learnings)
- **Risk:** Map staleness; requires maintenance discipline
- **Applicability:** See "When to Use Level 6" below

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

Capabilities are structural features detected in your project. A project must have at least one capability at every level from L1 through N to qualify as level N (cumulative).

| Capability | Level | What It Detects |
|------------|-------|-----------------|
| `instruction_file` | L1 | Non-trivial (≥10 lines), tracked instruction file exists |
| `project_constraints` | L2 | Project-specific substance: language, framework, commands, constraints |
| `size_controlled` | L2 | Instruction file is concise, not bloated |
| `external_references` | L3 | Content references files outside the primary instruction file |
| `multiple_files` | L3 | More than one instruction-related file exists |
| `path_scoping` | L4 | Different instructions load based on working file location |
| `structural_integrity` | L5 | References resolve, indexes current, no orphaned files |
| `org_policy` | L5 | Organization-level governance deployed |
| `navigation` | L5 | Structural map provides O(1) lookup (backbone, component maps) |
| `dynamic_context` | L6 | Agent discovers context based on task, not just file location |
| `extensibility` | L6 | Plugins, tool servers, hooks extend agent capabilities |
| `state_persistence` | L6 | State persists across sessions (memory files, learnings) |

**Detection order:** Capabilities are checked from L1 up. The project level is the highest N where at least one capability is detected at every level L1 through N.

See `registry/capabilities.yml` for the machine-readable taxonomy and `registry/levels.yml` for level definitions.

---

## How Rules Use Levels

Rules and capabilities are **separate systems** connected only by the level identifier:

- **Capabilities** are detected → determine your project's level
- **Rules** declare a concern level (e.g., `level: L2`) in their frontmatter
- A rule fires when `rule.level ≤ project_level`

This means an L3 project is checked against all rules at L1, L2, and L3 — not just L3 rules.

**90 rules** across 3 types:

| Type | Detection Method | LLM Cost |
|------|------------------|----------|
| Mechanical | Python structural checks | None |
| Deterministic | Regex pattern match | None |
| Semantic | Regex gate + LLM evaluation | Per check |

---

## Level Progression

| Transition | Key Actions |
|------------|-------------|
| L1 → L2 | Add core sections, constraints, project description |
| L2 → L3 | Extract to @imports, distribute across multiple files |
| L3 → L4 | Implement path-scoped rules, configure context-aware loading |
| L4 → L5 | Add structural validation, org policy, navigation maps |
| L5 → L6 | Add skills, hooks, MCP servers, persistent memory |

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

- **Level (L1-L6)**: Capability tier — determined by detected capabilities
- **Score (0-10)**: Compliance — how well you follow rules at your level

A simple instruction file (L2) can score 10/10 if it follows all L2 rules perfectly.

### Step 1: Detect Level

Level is determined by **capabilities present**, not by score:

| Capability Detected | Minimum Level |
|---------------------|--------------|
| `state_persistence`, `extensibility`, `dynamic_context` | L6 (Adaptive) |
| `structural_integrity`, `org_policy`, `navigation` | L5 (Maintained) |
| `path_scoping` | L4 (Abstracted) |
| `external_references`, `multiple_files` | L3 (Structured) |
| `project_constraints`, `size_controlled` | L2 (Scoped) |
| `instruction_file` | L1 (Basic) |

**Assignment:** The project level is the highest N where at least one capability is detected at every level L1 through N.

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

See `docs/sources.yml` for full source registry.
