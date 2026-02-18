---
name: implement-rule
description: Implement checks, patterns, and fixtures for an existing rule skeleton
---

# /implement-rule

Implement checks, regex patterns, and test fixtures for an existing rule that has a skeleton but empty `checks: []`.

## Usage

```
/implement-rule <coordinate> [--agent <name>] [--dry-run]
```

- `<coordinate>`: Rule coordinate (e.g., CORE:C:0001, CLAUDE:S:0001)
- `--agent <name>`: Agent for template var resolution (default: `claude`)
- `--dry-run`: Show what would be generated without writing files

## Examples

```
/implement-rule CORE:S:0002
/implement-rule CORE:M:0003 --agent codex
/implement-rule CLAUDE:S:0001 --dry-run
```

## Workflow

Follow: [@.shared/workflows/rule-implementation.md](../../../.shared/workflows/rule-implementation.md)

### 1. Locate

Resolve rule directory from coordinate:
1. Look up slug in `registry/coordinate-map.yml` (backbone key: `registry.coordinate_map`)
2. Determine category from coordinate letter: S=structure, C=content, E=efficiency, M=maintenance, G=governance
3. For core rules: `{categories.{category}}/{slug}/`
4. For agent rules: `{agent_rules.{agent}}/{slug}/`

### 2. Read

Parse `rule.md` frontmatter and body:
- Extract: `id`, `type`, `level`, `targets`, `question`, `criteria`, Pass/Fail examples from body
- **Abort if `checks:` is already non-empty** — rule is already implemented
- Identify the **violation class**: what structural or content pattern makes an instruction file FAIL this rule? The Pass/Fail examples are illustrations, not specifications.

### 3. Analyze — Pattern Design

This is the critical step. The goal is to design a check that catches the **class of violation**, not a regex that discriminates between two fixture files.

#### How to use frontmatter fields

| Field | Design role |
|-------|------------|
| `title` | Names the concern — what property should instruction files have? |
| `question` | Defines the evaluation question — what are we asking about the file? |
| `criteria` | Lists observable properties of a PASSING file — invert each to get violation indicators |
| Pass example | ONE illustration of a good file — extract the structural pattern that makes it good |
| Fail example | ONE illustration of a bad file — extract the structural pattern that makes it bad |

**Think in terms of violation structure, not fixture discrimination.**

#### Mechanical rules

- Select check function(s) from the 10 available: `file_exists`, `directory_exists`, `directory_contains`, `git_tracked`, `frontmatter_key`, `file_count`, `line_count`, `byte_size`, `path_resolves`, `extract_imports`
- Derive `args` from rule description (e.g., `max: 300` for `line_count`)
- No regex patterns needed

#### Deterministic rules — violation detection

Design a pattern that matches the **structural signature of the violation**:

1. Read the Fail example. Ask: what STRUCTURAL pattern makes this file bad? Not "what text does it contain?" but "what is the shape of the problem?"
2. Read the `criteria` (if present). Each criterion describes a PASSING property. Invert: what does a file look like when it LACKS this property?
3. Design a regex that matches the structural signature, not a specific keyword.

**Two violation types:**

| Type | Approach | Example |
|------|----------|---------|
| **Presence of bad content** | Pattern matches the violation directly | Secrets: `(?i)(api[_-]?key\|secret)\s*[=:]\s*['"]?[A-Za-z0-9]{8,}` |
| **Absence of good content** | Pattern matches the structural gap left by the missing content | Missing description: `^#\s+[^\n]+\n\s*\n##` (title followed immediately by section heading, no prose between) |

**NEVER use presence-then-negate as the primary strategy.** A pattern with `negate: true` that looks for "does good content exist?" is fragile — any incidental keyword match satisfies it. Instead, find the structural shape of the violation itself.

`negate: true` is acceptable ONLY when:
- The violation is purely about absence AND
- No structural signature exists (the bad file is structurally identical to the good file, just missing a keyword) AND
- You've confirmed there is no structural pattern to detect

For core rules: use `{{instruction_files}}` in paths (not `**/*.md`).

#### Semantic rules — candidate surfacing

Semantic rules have two phases: deterministic pre-check → semantic evaluation.

**Pre-check purpose**: Find text that EXHIBITS the violation pattern — content that needs human/LLM judgment to determine if it's actually a violation.

**Pre-check design**:
1. Read the `question` field. What kind of content needs to be EVALUATED?
2. Read the `criteria` field. What observable text patterns MIGHT indicate a violation but need context to confirm?
3. Design a pattern that matches these ambiguous indicators — not content matching the rule's topic, but content matching the violation's surface appearance.

Example: Rule "no-linter-enforceable-style"
- BAD pre-check: `(?i)(style|format|indent)` — matches the rule's topic, not violation indicators
- GOOD pre-check: `(?i)(indent|tab|space|bracket|semicolon|line.length|80.char|120.char)` — matches specific linter-enforceable patterns

Terminal semantic check uses `prompt` derived from rule's `question`/`criteria` fields.

### 4. Generate checks

Write `checks:` array in `rule.md` frontmatter:
- IDs follow `{NAMESPACE}.{CATEGORY}.{SLOT}.{descriptive-name}` format (e.g., `CORE.S.0005.file-exists`)
- Check types must not exceed rule type ceiling:
  - `mechanical` rule → only `mechanical` checks
  - `deterministic` rule → `mechanical` + `deterministic` checks
  - `semantic` rule → any types, semantic must be last
- Severity from rule context: `critical` for L1, `high`/`medium` for L2+

### 5. Generate patterns

For deterministic/semantic rules, write regex patterns in `rule.yml`:
- `id` matches the check ID from frontmatter
- `languages: [generic]` for markdown targets
- `paths.include` uses template vars (`{{instruction_files}}`)
- Pattern captures the violation, not the desired state
- Severity mapping: critical→ERROR, high/medium/low→WARNING

For mechanical-only rules: leave `rule.yml` as `rules: []`.

### 6. Generate fixtures

Fixtures simulate REAL instruction files, not minimal test content.

**Pass fixture** (`tests/pass/`):
- A realistic instruction file (30-80 lines) that a real project might have
- Contains the structural patterns that satisfy the rule
- Include realistic sections, commands, and project context — not just the minimum to pass
- File names match resolved template vars (e.g., `CLAUDE.md` for claude agent)

**Fail fixture** (`tests/fail/`):
- A realistic instruction file that exhibits the specific violation
- The violation should be the ONLY difference from a reasonable file — don't make the fail fixture obviously broken in multiple ways
- Must trigger the pattern's structural signature, not just be "bad in general"

**Fixture quality check**: After generating fixtures, re-read them and ask:
- Does the pass fixture look like a real CLAUDE.md from a real project?
- Does the fail fixture look like a plausible mistake someone would make?
- Would the pattern catch the fail fixture for the RIGHT reason (structural violation match), not an incidental one?

Remove `.gitkeep` from directories that now have real fixture content.

### 7. Verify

Run the test harness:
```bash
docker compose -f runtime/docker-compose.yml run --rm test --rule <coordinate>
```
- All checks must pass for both pass and fail fixtures
- If test fails: re-examine the violation class analysis (step 3), not just the regex. The pattern may be structurally wrong, not just syntactically wrong.

## Reference

- Schema: `schemas/rule.schema.yml` — check field definitions, mechanical check names, severity enum
- Patterns: `docs/pattern-guide.md` — pattern syntax, generic mode, combining patterns
- Runtime: `runtime/` — test runner, fixture format, mechanical check implementations
- Agent config: `agents/{agent}/config.yml` — template var values per agent
- Path resolution: `.shared/knowledge/backbone-resolution.md`

## Quick Reference

| Rule type | Modifies rule.md | Modifies rule.yml | Fixture content |
|-----------|-----------------|-------------------|-----------------|
| mechanical | checks with `check` + `args` | No change (`rules: []`) | Files/dirs matching check function expectations |
| deterministic | checks with `pattern` + `message` | Regex patterns | Content triggering/not triggering pattern |
| semantic | pre-checks + terminal `prompt` | Regex patterns for pre-checks | Content producing/not producing candidates |

## Severity Mapping

| rule.md severity | rule.yml severity |
|------------------|-------------------|
| critical | ERROR |
| high | WARNING |
| medium | WARNING |
| low | WARNING |

## Pattern Design Examples

### Good: Structural violation detection

Rule: "has-project-description" — file must open with a project description.

**Violation structure**: Title exists, but next non-blank line is a section heading (no description prose between).

```yaml
pattern-regex: "^#\\s+[^\\n]+\\n\\s*\\n##"
message: "Title followed immediately by section heading — no project description"
```

This catches the SHAPE of the problem: `# Title\n\n## Section` with nothing between.

### Bad: Minimal fixture discrimination

Same rule, but designed to discriminate fixtures:

```yaml
pattern-regex: "\\A## "
message: "File opens with H2 instead of project description"
```

This only catches files starting with `##` — misses the primary failure mode (title present, description absent).

### Good: Absence via structural gap

Rule: "has-commands" — file must document executable commands.

**Violation structure**: File has sections but none contain backtick-wrapped commands.

```yaml
# Combined pattern: file has 2+ sections but zero backtick commands
patterns:
  - pattern-regex: "^## "
  - pattern-not-regex: "`[a-z]+ .+`"
```

This requires both conditions: structured file (has sections) AND no commands. A file with no structure at all fails a different rule.

### Bad: Presence check with negate

Same rule, but as a negated presence check:

```yaml
pattern-regex: "`[a-z]+ .+`"
negate: true  # fragile — any backtick content satisfies this
```

A file containing `` `see above` `` or `` `my-var` `` passes this check despite having no actual commands.

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Pattern discriminates fixtures instead of catching violation class | Re-analyze: what is the STRUCTURAL SHAPE of the violation? |
| Using `negate: true` as primary strategy | Find the structural gap pattern. Negate is last resort only. |
| Pre-check matches rule topic instead of violation indicators | Pre-check should find text that NEEDS judgment, not text about the topic |
| Fixture is minimal synthetic content | Write realistic 30-80 line instruction files |
| Fail fixture is broken in multiple ways | One specific violation in an otherwise reasonable file |
| Pattern matches desired state | Invert: pattern must match the violation |
| Using `**/*.md` in paths | Use `{{instruction_files}}` template var |
| Missing `cross_file: true` | Add when pattern operates across target set |
| Semantic rule without pre-checks | Always add deterministic pre-check before semantic |
| Fixture file named wrong | Must match resolved template var (e.g., `CLAUDE.md`) |
| Leaving `.gitkeep` alongside real fixtures | Remove `.gitkeep` when adding content |