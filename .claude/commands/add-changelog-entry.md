Automatically add a changelog entry to PROJECT_ROOT/UNRELEASED.md.

Instructions:
1. Check git diff or recent file modifications
2. Determine the area from the file path:
   - rules/*.md → [RULES]
   - maturity-model.md with L1-L6 changes → [L1]-[L6]
   - templates/*.md → [TEMPLATES]
   - README.md → [DOCS]
   - CLAUDE.md, backbone.yml, .claude/, .reporails/ → [META]
3. Determine the category:
   - New files/content → Added
   - Modified existing → Changed
   - Marked as deprecated/obsolete → Deprecated
   - Removed content → Removed
   - Bug fixes → Fixed
   - Security-related changes, vulnerability fixes → Security
4. Write a concise, short (minimum 3, maximum 7, short-mid length words) description of what changed
5. Append to UNRELEASED.md under the correct category section
6. Create the category section if it doesn't exist

Format:
### [Category]
- [Area]: [Description]

Categories: Added, Changed, Deprecated, Removed, Fixed, Security

Areas:
- [RULES] – Rule definitions (S, C, M, G, E)
- [L1]-[L6] – Level-specific changes
- [TEMPLATES] – Template files
- [DOCS] – README, general documentation
- [META] – CLAUDE.md, backbone.yml, repo structure

Example:
### Added
- [RULES]: S5 rule for import depth validation
- [L4]: Added hooks requirement to level definition
- [TEMPLATES]: L4 modular template

### Changed
- [DOCS]: Updated README with CLI link

Do not ask for confirmation. Just do it.
