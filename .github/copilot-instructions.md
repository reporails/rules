# Reporails Rules Framework

Framework for validating AI agent instruction files. Community-maintained rule definitions with Docker-based test harness.

## Tech Stack

- **Markdown + YAML**: Rule definitions with regex patterns
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

# Verbose
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
  rule.yml         # Regex patterns (or empty `rules: []` for mechanical)
  tests/
    pass/          # Fixture that should pass
    fail/          # Fixture that should fail
```

### Rule Types

| Type | Detection Method | Example |
|------|------------------|---------|
| **mechanical** | Python structural checks (file exists, line count, byte size) | CORE:S:0007 — root instruction file exists |
| **deterministic** | Regex pattern matching on file content | CORE:C:0018 — constraint keywords present |
| **semantic** | Regex pre-filter + LLM evaluation | CORE:C:0026 — cross-agent compatibility |

Mechanical rules have `rules: []` in rule.yml.

### Coordinates

Every rule has a coordinate like `CORE:S:0001`:
- **Namespace**: `CORE` (cross-agent), `CLAUDE`, `CODEX`, `COPILOT`
- **Category**: `S` (structure), `C` (content), `X` (context_quality), `E` (efficiency), `G` (governance), `M` (maintenance)
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
2. `rule.yml` with regex patterns (or `rules: []`)
3. `tests/pass/` and `tests/fail/` fixtures
4. Update `registry/coordinate-map.yml` with new coordinate

### Shared Resources
Agent-agnostic content lives in `.shared/`:
- `.shared/workflows/` — Process definitions (mermaid flowcharts)
- `.shared/knowledge/` — Domain reference (facts, patterns, validation)

Skills in `.claude/skills/` reference shared workflows.

## Skills

GitHub Copilot CLI supports Agent Skills stored in `.claude/skills/` (same as Claude Code). Skills reference shared workflows in `.shared/workflows/`.

| Skill | Purpose | Usage |
|-------|---------|-------|
| `generate-rule` | Create rule skeleton | Ask: "Generate rule CORE:C:0026 for 'My Rule'" |
| `implement-rule` | Implement checks/fixtures | Ask: "Implement rule CORE:C:0026" |
| `validate-rules` | Validate against schema | Ask: "Validate rules" |
| `manage-levels` | Sync level definitions | Ask: "Sync level definitions" |
| `manage-agent-config` | Validate agent configs | Ask: "Validate agent config" |
| `add-changelog-entry` | Log changes | Ask: "Add changelog entry" |

Copilot will automatically use the appropriate skill based on your request.

## Workflows (Manual Reference)

### Generate a Rule
When asked to generate a new rule:
1. Read `.shared/workflows/rule-creation.md` for the complete process
2. Reference `.shared/knowledge/rule-authoring.md` for authoring guidelines
3. Reference `.shared/knowledge/backbone-resolution.md` for path resolution

### Implement a Rule
When asked to implement checks for an existing rule skeleton:
1. Read `.shared/workflows/rule-implementation.md` for the process
2. Ensure tests/pass/ and tests/fail/ fixtures are created

### Validate Rules
When asked to validate rules:
1. Read `.shared/workflows/rule-validation.md` for validation process
2. Run test harness: `docker compose -f runtime/docker-compose.yml run test`

### Sync Level Definitions
When asked to sync or manage capability levels:
1. Read `.shared/workflows/level-sync.md` for the sync process
2. Update `registry/levels.yml` and `registry/capabilities.yml`

### Add Changelog Entry
When making changes to rules:
1. Read `.shared/knowledge/changelog.md` for format requirements
2. **ALWAYS** update `UNRELEASED.md` (never CHANGELOG.md)

## Context-Specific Constraints

Apply additional constraints based on the work area:

**When working on core rules** (`core/`):
- Read `.shared/knowledge/rule-authoring.md` for authoring standards
- Use `{{instruction_files}}` placeholder, never hardcode agent paths
- Check `registry/coordinate-map.yml` before picking a coordinate slot

**When working on schemas** (`schemas/`):
- All schemas are defined in `schemas/*.schema.yml`
- Never duplicate schema definitions in rules
- Reference canonical schema files only

**When working on agent configs** (`agents/*/config.yml`):
- Read `.shared/knowledge/backbone-resolution.md` for path resolution
- Validate against `schemas/agent.schema.yml`
- Test with `--agent <name>` flag

**When creating or editing workflows** (`.shared/workflows/`):
- Keep workflows agent-agnostic
- Both Claude skills and Copilot instructions reference these
- Use Mermaid flowcharts for complex processes

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
