# Reporails Rules

Validation rules for AI agent instruction files (CLAUDE.md, .cursorrules, copilot-instructions.md).
Community-maintained.

**Version:** 0.5.0 <!-- source of truth: VERSION file -->

### Pre-1.0 — moving fast, API still evolving, feedback welcome.

## Quickstart

```bash
npx @reporails/cli install
```

This registers the MCP server with Claude Code. Then ask Claude:
```
> What ails claude?
```

Or run directly without MCP:
```bash
npx @reporails/cli check
```

## What's here
```
core/
  structure/       # 25 rules: File presence, nesting, format, hooks, skills
  content/         # 32 rules: Context, commands, conventions, constraints
  context_quality/ # 7 rules: Architecture, tech stack, directory layout
  efficiency/      # 5 rules: Size limits, redundancy, grouping
  governance/      # 8 rules: Credentials, permissions, MCP, self-contained config
  maintenance/     # 1 rule: Freshness markers

agents/
  claude/          # 8 rules: Hooks, skills, frontmatter
  codex/           # 2 rules: File priority, skill structure
  copilot/         # 2 rules: applyTo scope, setup steps
  generic/         # Config only (default agent)

schemas/           # Rule, agent, and config schemas
registry/          # Capabilities, levels, coordinate map
docs/              # Capability levels, sources
```

90 rules. For additional recommended rules, see [reporails/recommended](https://github.com/reporails/recommended).

> **Tombstones**: Old coordinate slots from pre-0.4.0 rules will be backfilled in `registry/tombstones.yml` after 0.5.0.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md)

Supported agents: **Claude Code**, **Codex**, **Copilot CLI**, **Generic** (AGENTS.md)

## Documentation

- [Capability Levels](docs/capability-levels.md) — L1-L6 capability model
- [Rule Schema](schemas/rule.schema.yml) — How rules are structured

## License

[CC BY-SA 4.0](LICENSE)
