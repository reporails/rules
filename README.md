# Reporails Rules

Validation rules for AI agent instruction files (CLAUDE.md, .cursorrules, copilot-instructions.md).
Community-maintained.

**Version:** 0.4.1 <!-- source of truth: VERSION file -->

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
  structure/     # 3 rules: File presence, nesting, format
  content/       # 5 rules: Context, commands, architecture, constraints
  governance/    # 1 rule: Cross-agent compatibility
  maintenance/   # 2 rules: Reference integrity, glob validation

agents/
  claude/        # 3 rules: Claude Code specific
  codex/         # 1 rule: OpenAI Codex specific
  copilot/       # 2 rules: GitHub Copilot CLI specific

schemas/         # Rule, agent, and config schemas
registry/        # Capabilities, levels, coordinate map
docs/            # Capability levels, sources
```

17 rules. For additional recommended rules, see [reporails/recommended](https://github.com/reporails/recommended).

> **Tombstones**: Old coordinate slots from pre-0.4.0 rules will be backfilled in `registry/tombstones.yml` after 0.5.0.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md)

Supported agents: **Claude Code**, **Codex**, **Copilot CLI**

## Documentation

- [Capability Levels](docs/capability-levels.md) — L1-L6 capability model
- [Rule Schema](schemas/rule.schema.yml) — How rules are structured

## License

[CC BY-SA 4.0](LICENSE)
