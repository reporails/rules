# Reporails Rules Framework

Framework for validating AI agent instruction files. Community-maintained rule definitions with Docker-based test harness.

## Tech Stack

- **Markdown + YAML**: Rule definitions with OpenGrep patterns
- **Python**: Test harness and mechanical checks
- **Docker**: Isolated test environment
- **No application code**: Framework/schema repository only

## Test Commands

```bash
# Build test image (first time or after runtime/ changes)
docker compose -f runtime/docker-compose.yml build

# Run all rules
docker compose -f runtime/docker-compose.yml run test

# Run single rule
docker compose -f runtime/docker-compose.yml run test --rule CORE:S:0001

# Run category
docker compose -f runtime/docker-compose.yml run test core/structure/

# Verbose (shows OpenGrep matches)
docker compose -f runtime/docker-compose.yml run test --verbose

# Test with codex agent variables
docker compose -f runtime/docker-compose.yml run test --agent codex
```

All tests must pass before submitting changes.

## Architecture

### Project Topology

**Read `.reporails/backbone.yml` first** before exploring paths — it's the single source of truth for all directory structures, schemas, and registry locations. Never use exploratory commands to find paths already mapped in backbone.yml.

### Rule Structure

Each rule lives in its own directory:

```
core/structure/instruction-file-size-limit/
  rule.md          # Frontmatter (id, type, level, checks) + prose
  rule.yml         # OpenGrep patterns (or empty `rules: []` for mechanical)
  tests/
    pass/          # Fixture that should pass
    fail/          # Fixture that should fail
```

### Rule Types

| Type | Detection Method | Example |
|------|------------------|---------|
| **mechanical** | Python structural checks (file exists, line count, byte size) | CORE:S:0001 — instruction file exists |
| **deterministic** | OpenGrep pattern matching on file content | CORE:C:0006 — specificity over vagueness |
| **semantic** | OpenGrep pre-filter + LLM evaluation | CORE:C:0017 — repo-specific content |

Mechanical rules have `rules: []` in rule.yml.

### Coordinates

Every rule has a coordinate like `CORE:S:0005`:
- **Namespace**: `CORE` (cross-agent), `CLAUDE`, `CODEX`
- **Category**: `S` (structure), `C` (content), `E` (efficiency), `M` (maintenance), `G` (governance)
- **Slot**: `0001`–`9999`

Check `registry/coordinate-map.yml` before picking a slot.

### Capability Model

Levels L1-L6 describe what an instruction setup enables:
- **L1 Basic**: Tracked instruction file exists
- **L2 Scoped**: Project-specific constraints, size controlled
- **L3 Structured**: External references, multiple files
- **L4 Abstracted**: Path-scoped rules (.claude/rules/)
- **L5 Maintained**: Structural integrity, governance, navigation
- **L6 Adaptive**: Dynamic context, extensibility, persistence

Defined in:
- `registry/capabilities.yml` — Capability taxonomy
- `registry/levels.yml` — Level definitions
- `docs/capability-levels.md` — Detailed explanations

## Key Conventions

### Path Resolution
Always resolve paths from `.reporails/backbone.yml` rather than using find/grep/ls to discover project structure. The backbone maps all schemas, registries, rule directories, and agent configs.

### Changelog Updates
- **NEVER** read or edit `CHANGELOG.md` (historical record)
- **ALWAYS** update `UNRELEASED.md` when modifying rules
- Use `/add-changelog-entry` skill for proper formatting

### Schema References
- **NEVER** duplicate schema definitions in rules
- **ALWAYS** reference `schemas/` for canonical definitions
- Core rules use `{{instruction_files}}` placeholder, not hardcoded agent paths

### Required Files
When creating a rule:
1. `rule.md` with proper frontmatter
2. `rule.yml` with OpenGrep patterns (or `rules: []`)
3. `tests/pass/` and `tests/fail/` fixtures
4. Update `registry/coordinate-map.yml` with new coordinate

### Shared Resources
Agent-agnostic content lives in `.shared/`:
- `.shared/workflows/` — Process definitions (mermaid flowcharts)
- `.shared/knowledge/` — Domain reference (facts, patterns, validation)

Skills in `.claude/skills/` reference shared workflows.

## Skills

| Skill | Purpose | Example |
|-------|---------|---------|
| `/generate-rule` | Create rule skeleton | `/generate-rule CORE:C:0026 core "My Rule"` |
| `/implement-rule` | Implement checks/fixtures | `/implement-rule CORE:C:0026` |
| `/validate-rules` | Validate against schema | `/validate-rules` or `/validate-rules CORE:C:0026` |
| `/manage-levels` | Sync level definitions | `/manage-levels diff` |
| `/manage-agent-config` | Validate agent configs | `/manage-agent-config` |
| `/add-changelog-entry` | Log changes | `/add-changelog-entry` |

Skills walk through the process interactively — use them for rule work.

## Efficiency Tips

- Read files based on purpose: full view for editing, partial for understanding
- Reference from memory instead of re-reading unchanged files
- For rule work, check `.claude/rules/` for task-specific constraints first
- Use `wc -l core/**/*/rule.md agents/**/rules/*/rule.md` to check rule lengths

## Related Files

- `README.md` — Public quickstart and overview
- `CONTRIBUTING.md` — Detailed contributor guide
- `CLAUDE.md` — Claude Code-specific initialization and constraints
- `.github/workflows/` — CI/CD definitions
