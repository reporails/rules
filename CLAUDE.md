# Reporails Framework
<!-- Last updated: 2026-02-24 -->

## Overview

This project is a rule-based evaluation framework for AI agent instruction files (CLAUDE.md, AGENTS.md, copilot-instructions.md). We define rules that check structure, content quality, governance, and efficiency of these instruction files. The framework uses regex pattern matching and mechanical checks — no application code, only markdown definitions and YAML schemas.

## Tech Stack

- Markdown documentation with YAML frontmatter
- YAML schemas and configuration (`schemas/*.schema.yml`)
- Regex patterns for deterministic detection (`rule.yml`)
- Docker Compose test harness (`runtime/`)
- `reporails-cli` (Python) for validation runtime

## Terminology

In our system we define these domain-specific terms:

- **Rule**: A check definition with coordinate (e.g., `CORE:S:0001`), markdown description (`rule.md`), and patterns (`rule.yml`)
- **Coordinate**: Unique identifier in `NAMESPACE:CATEGORY:SLOT` format (e.g., `CORE:C:0013`)
- **Backbone**: The `.reporails/backbone.yml` file — single source of truth for all project paths
- **Level**: Capability tier (L0–L6) that determines which rules apply — level is input to rule selection, not output of scoring
- **Capability**: A feature detected in the instruction system (e.g., `path_scoping`, `multiple_files`)
- **Fixture**: Test directory (`tests/pass/`, `tests/fail/`) containing sample instruction files for rule validation
- **Coordinate map**: Registry mapping slugs to coordinates (`registry/coordinate-map.yml`)
- **Check**: A single verification within a rule — typed as `mechanical`, `deterministic`, or `semantic`
- **Skeleton**: A generated rule directory with scaffold files before implementation

## File Discovery

Claude Code checks instruction files in this priority order, with earlier files taking precedence:

1. `CLAUDE.md` (root instruction file — checked first)
2. `.claude/rules/*.md` (path-scoped rules — loaded by file context)
3. `.claude/skills/*/SKILL.md` (skill entry points — loaded on skill invocation)

## Initialization

Run `/bootstrap` before any work to load project context, or manually read:

1. `.reporails/backbone.yml` — project structure and path resolution
2. `registry/capabilities.yml` and `registry/levels.yml` — architecture
3. `.claude/rules/` — context-specific constraints for the current task

## Structure

Defined in `.reporails/backbone.yml` — the single source of truth for project topology, paths, schemas, and registry locations.

**BEFORE** running `find`, `grep`, `ls`, or glob to locate project files, you **MUST** read `.reporails/backbone.yml` first. All schema paths, registry paths, rule directories, agent configs, and doc locations are mapped there. You **MUST NOT** use exploratory commands to discover paths that the backbone already provides.

## Navigation

Key paths (resolve from backbone, do not hardcode):

- `registry/` — Capabilities, levels, coordinate map, tombstones
- `core/` — Core rules organized by category (structure, content, governance, efficiency, maintenance, context_quality)
- `agents/` — Agent-specific config and rules (claude, codex, copilot, generic)
- `schemas/` — Machine-readable contracts (8 schemas: rule, capability, levels, agent, package, project, sources, user)
- `docs/` — Contributor guides and source registry

Additional rules available in [reporails/recommended](https://github.com/reporails/recommended).

## Conventions

We use these project-specific patterns:

- Rule directories follow the pattern `{category}/{slug}/` with `rule.md`, `rule.yml`, `tests/pass/`, `tests/fail/`
- Coordinate format: `NAMESPACE:CATEGORY:SLOT` where NAMESPACE is `CORE`, `CLAUDE`, `CODEX`, `COPILOT`, or `RRAILS`
- Category letters: `S` (structure), `C` (content), `X` (context_quality), `E` (efficiency), `G` (governance), `M` (maintenance)
- Template variables in rules use `{{instruction_files}}` — never hardcode agent-specific paths in core rules
- Slugs are kebab-case, derived from the rule title, truncated to fit directory name limits
- YAML frontmatter in `rule.md` defines identity; `rule.yml` defines patterns and checks

## Workflow

When working on rules, follow this process:

1. **Investigate first** — read the existing rule or related rules before writing. Understand the check type (mechanical, deterministic, semantic) and what patterns already exist
2. **Plan the approach** — for new rules, decide the check type, write the criteria, and identify what the pass/fail fixtures should contain before implementing
3. **Implement incrementally** — create the skeleton (`/generate-rule`), then implement checks and fixtures (`/implement-rule`), then test (`/test-rules`). One rule at a time
4. **Validate before committing** — run `/validate-rules` for schema compliance, then `/test-rules` for fixture correctness

```mermaid
flowchart TD
    A[Read existing rules + backbone] --> B{New rule or modify?}
    B -->|New| C[/generate-rule — skeleton]
    B -->|Modify| D[Read rule.md + rule.yml]
    C --> E[/implement-rule — checks + fixtures]
    D --> E
    E --> F[/test-rules — verify fixtures]
    F -->|Fail| E
    F -->|Pass| G[/validate-rules — schema check]
    G -->|Fail| E
    G -->|Pass| H[Update UNRELEASED.md + commit]
```

When unsure about a rule's scope, check type, or whether it overlaps with an existing rule, ask for clarification rather than guessing — ambiguous rules create false positives that erode trust.

## Testing

The test framework uses Docker Compose with two harnesses:

```bash
# Local harness (mounts local cli/ source) — use during development
docker compose -f runtime/docker-compose.yml -f runtime/docker-compose.dev.yml run --rm test

# Run a single rule by coordinate
docker compose -f runtime/docker-compose.yml -f runtime/docker-compose.dev.yml run --rm test --rule CORE:S:0001

# Verbose output with per-check detail
docker compose -f runtime/docker-compose.yml -f runtime/docker-compose.dev.yml run --rm test --verbose

# CI harness (installs reporails-cli from PyPI) — mirrors CI pipeline
docker compose -f runtime/docker-compose.yml run --rm test
```

Test contract: pass fixtures must produce zero violations; fail fixtures must trigger at least one check.

Run `ails check .` to validate the project's own instruction files against the rule catalog. Use `ails check . -v` for verbose output with per-file, per-rule detail.

## Commands

```bash
# Check rule definition line counts
wc -l core/**/*/rule.md agents/**/rules/*/rule.md

# List all rule definitions (excluding test fixtures)
find core agents -name "rule.md" | grep -v tests

# List rule directories
find core agents -name "rule.yml" -exec dirname {} \;

# Validate own instruction files
ails check . -v
```

## Security

When writing rule patterns:

- NEVER include credentials, API keys, or secrets in rule fixtures or examples
- Regex patterns in `rule.yml` must not be vulnerable to ReDoS — avoid nested quantifiers like `(a+)+`
- Fixture files in `tests/pass/` and `tests/fail/` must not contain real project data or sensitive paths

## Error Handling

When a rule test fails, diagnose by failure type:

- **"Fail fixture: no check detected a violation"** — fix the regex pattern in `rule.yml` or update the fail fixture content to match
- **"Unknown mechanical check: X"** — the check function name is not registered in the CLI; fix the name in `rule.md` or add to CLI
- **"[FAIL] ... (mechanical, pass): ..."** — pass fixture violates a mechanical check; fix the fixture or adjust check args
- **"no pattern specified"** — mechanical check is missing required `args`; add them to the check definition in `rule.md`

When `ails check` reports violations, read the rule definition (`rule.md`) to understand what the check expects before attempting fixes.

## Permissions

Allowed operations:

- Read any file in the repository
- Edit rule definitions (`rule.md`, `rule.yml`), fixtures, schemas, registry files, and docs
- Run docker compose test harness and `ails` CLI commands
- Create new rule directories with standard structure

Forbidden operations:

- NEVER run `rm -rf` on rule directories without explicit confirmation
- NEVER force-push to main branch
- NEVER modify `.reporails/backbone.yml` without confirming the change — it is the project's routing table
- NEVER delete entries from `registry/coordinate-map.yml` without adding them to `registry/tombstones.yml`
- NEVER execute destructive git operations (`reset --hard`, `checkout .`, `clean -f`) without explicit user confirmation

## Self-Contained Configuration

This project is self-contained and does not rely on user-level settings. All configuration lives within the repository:

- `.reporails/backbone.yml` — project topology and path resolution
- `agents/*/config.yml` — agent-specific rule configuration
- `.claude/settings.json` — Claude Code project settings
- `runtime/docker-compose*.yml` — test harness configuration

No personal setup, user-level config, or external dependencies are required beyond Docker.

## Output Format

When reporting rule changes, respond with:

- Coordinate and rule title (e.g., `CORE:S:0001 Import References Used`)
- What changed and why
- Whether fixtures need updating

When reporting validation results, use the same format as `ails check -v`: file path, rule coordinate, pass/fail status.

## Explain Reasoning

When making non-obvious changes to rule definitions — especially modifying regex patterns, changing check types, or adjusting severity levels — explain the rationale: what the pattern catches, why the severity was chosen, and what false positives or negatives were considered.

## Efficiency

- Read files based on purpose: full for EDIT, partial for UNDERSTAND
- Reference from memory instead of re-reading unchanged files
- Use `files_with_matches` mode for searches, `head_limit` to cap results
- For rule work, start with `.claude/rules/` instructions
- Do not duplicate content from `docs/` or `schemas/` — reference via `@import` or path

## Constraints

- NEVER duplicate schema definitions — reference `schemas/` instead
- NEVER hardcode agent paths in core rules — use `{{instruction_files}}`
- NEVER read CHANGELOG.md — use UNRELEASED.md instead
- ALWAYS update UNRELEASED.md when modifying rules
- ALWAYS create both rule.md and rule.yml for each rule
- ALWAYS create tests/pass/ and tests/fail/ fixture directories for each rule
- ALWAYS update registry/coordinate-map.yml when adding or removing rules
- ALWAYS resolve paths from `.reporails/backbone.yml` before using exploratory commands

## Shared Resources

Agent-agnostic workflows and knowledge live in `.shared/`:

- `.shared/workflows/` — Process definitions (mermaid flowcharts)
- `.shared/knowledge/` — Domain reference (facts, patterns, validation)

Skills in `.claude/skills/` are entry points that reference shared content.

## Skills

Skills in `.claude/skills/` — each has a SKILL.md linking to shared workflows.

| Skill | Purpose |
|-------|---------|
| `/bootstrap` | Load project context — backbone, registry, and constraints — before any work |
| `/generate-rule` | Create rule skeleton with coordinate, directory, and scaffold files |
| `/implement-rule` | Implement checks, patterns, and fixtures for an existing rule skeleton |
| `/test-rules` | Run rules against pass/fail fixtures using the local CLI |
| `/validate-rules` | Validate rules against schema and contracts |
| `/manage-levels` | Sync level definitions with capability model |
| `/manage-agent-config` | Create, update, and validate agent configurations |
| `/add-changelog-entry` | Add changelog entry to UNRELEASED.md |