# Contributing

Rules define what Reporails checks in AI instruction files (CLAUDE.md, AGENTS.md, .cursorrules, copilot-instructions.md). This repo is where those rules live.

## Setup

**Prerequisites:**
- **Docker** — for running the test harness
- **A coding agent** — rules are created and validated through agent workflows

Currently supported: **Claude Code**, **Codex**, **GitHub Copilot CLI**, **Generic** (AGENTS.md)

**Developer setup:**
```bash
git clone git@github.com:reporails/framework.git rules
cd rules
git config core.hooksPath .githooks
```

The pre-commit hook enforces that `UNRELEASED.md` is staged alongside changes to `core/`, `agents/`, `schemas/`, `registry/`, or `docs/`.

## Rule anatomy

Each rule lives in its own directory with three parts:

```
core/structure/root-instruction-file-presence/
  rule.md          # Definition: frontmatter (id, type, level, checks) + prose
  rule.yml         # Regex patterns (or empty `rules: []` for mechanical)
  tests/
    pass/          # Fixture that should pass the rule
    fail/          # Fixture that should fail the rule
```

## Coordinates

Every rule has a coordinate like `CORE:S:0001` — three parts:

| Part | Meaning | Values |
|------|---------|--------|
| Namespace | Who owns it | `CORE`, `CLAUDE`, `CODEX`, `COPILOT` |
| Category | What it checks | `S` (structure), `C` (content), `X` (context_quality), `E` (efficiency), `G` (governance), `M` (maintenance) |
| Slot | Sequence number | `0001`–`9999` |

Check IDs within a rule use dots and a descriptive name: `CORE.S.0001.file-exists`

Check `registry/coordinate-map.yml` to see which slots are taken before picking a new one.

## Rule types

| Type | How it detects | Example |
|------|---------------|---------|
| **mechanical** | Python structural checks (file exists, line count, byte size) | CORE:S:0007 — root instruction file exists |
| **deterministic** | Regex pattern matching on file content | CORE:C:0018 — constraint keywords present |
| **semantic** | Regex pre-filter + LLM evaluation | CORE:C:0026 — cross-agent compatibility |

Mechanical rules have `rules: []` in their rule.yml. Deterministic and semantic rules have regex patterns.

## Creating a rule

**For Claude Code:**
```
/generate-rule CORE:C:0026 core "My New Rule"
```

**For Copilot CLI:**
Ask "Generate rule CORE:C:0026" and Copilot will follow `.shared/workflows/rule-creation.md`

**For other agents:**
Manually follow `.shared/workflows/rule-creation.md`

The workflow creates the directory, rule.md, rule.yml, and test fixtures. It walks you through choosing the type, writing patterns, and finding backing sources.

To implement checks and wire up an existing skeleton:

**For Claude Code:**
```
/implement-rule CORE:C:0026
```

**For Copilot CLI:**
Ask "Implement rule CORE:C:0026" and Copilot will follow `.shared/workflows/rule-implementation.md`

## Testing

Build and run the Docker test harness:

```bash
# Build the test image (first time, or after runtime/ changes)
docker compose -f runtime/docker-compose.yml build

# Run all rules
docker compose -f runtime/docker-compose.yml run --rm test

# Run one rule
docker compose -f runtime/docker-compose.yml run --rm test --rule CORE:S:0001

# Run one category
docker compose -f runtime/docker-compose.yml run --rm test core/structure/

# Verbose output
docker compose -f runtime/docker-compose.yml run --rm test --verbose
```

All tests must pass before submitting.

## Submitting changes

1. Create a branch from `main`
2. Make your changes
3. Add a changelog entry to `UNRELEASED.md` (the pre-commit hook enforces this for rule/schema/registry changes)
4. Run the test harness — all rules must pass
5. Open a pull request

**Changelog format** — use the existing sections in `UNRELEASED.md`:
- `## Added` — new rules, new capabilities
- `## Changed` — modifications to existing rules, schemas, docs
- `## Fixed` — bug fixes in patterns, fixtures, or workflows
- `## Removed` — tombstoned rules, deleted files

## Rule layout

```
core/
  structure/       # 25 rules — file presence, nesting, format, hooks, skills
  content/         # 32 rules — context, commands, conventions, constraints
  context_quality/ # 7 rules — architecture, tech stack, directory layout
  efficiency/      # 5 rules — size limits, redundancy, grouping
  governance/      # 8 rules — credentials, permissions, MCP, self-contained config
  maintenance/     # 1 rule — freshness markers

agents/
  claude/rules/    # 8 rules — hooks, skills, frontmatter
  codex/rules/     # 2 rules — file priority, skill structure
  copilot/rules/   # 2 rules — applyTo scope, setup steps
  generic/         # config only (default agent)
```

Opinionated rules (governance, style) live in [reporails/recommended](https://github.com/reporails/recommended) with the `RRAILS_` namespace.

## Workflows

All agents share workflows in `.shared/`:
- `.shared/workflows/` — Step-by-step process definitions (Mermaid flowcharts)
- `.shared/knowledge/` — Domain reference (authoring, validation, patterns)

**Claude Code** invokes workflows via `/skills` (e.g., `/generate-rule`)
**Copilot CLI** reads instructions that reference workflows (e.g., "Follow `.shared/workflows/rule-creation.md`")
**Other agents** can manually follow workflow files

## Skills (Claude Code)

For Claude Code users, skills provide interactive workflows:

| Task | Skill | Example |
|------|-------|---------|
| Create a rule | `/generate-rule` | `/generate-rule CORE:C:0026 core "My Rule"` |
| Implement checks | `/implement-rule` | `/implement-rule CORE:C:0026` |
| Validate all rules | `/validate-rules` | `/validate-rules` |
| Validate one rule | `/validate-rules` | `/validate-rules CORE:C:0026` |
| Level mappings | `/manage-levels` | `/manage-levels diff` |
| Log a change | `/add-changelog-entry` | `/add-changelog-entry` |

For Copilot CLI and other agents, follow workflows in `.shared/workflows/` directly.

## Questions?

[Open an issue](https://github.com/reporails/rules/issues).
