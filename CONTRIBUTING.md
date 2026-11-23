# Contributing to Gitlytics Agent Plugin & Skills

Thanks for helping improve the Gitlytics MCP configuration, skills, and plugin bundle.

## Local Validation

Before opening a pull request, run the offline validator from the repository root:

```bash
python scripts/validate_plugin.py
```

This verifies:
- `plugin.json` conforms strictly to the Antigravity plugin schema.
- `mcp_config.json` and `mcp_config.local.json` are valid and properly namespaced.
- Every `skills/<name>/SKILL.md` has valid YAML frontmatter matching its directory name, stays under 500 lines, has valid relative `references/` links, and includes `evals/evals.json`.
- `rules/AGENTS.md` has no YAML frontmatter.
- Zero em dashes or en dashes appear in any text file.

## Style Guidelines

- Keep `SKILL.md` files concise and imperative (under 350 lines preferred) and move long examples or playbooks into `references/`.
- Never hardcode or invent Gitlytics card slugs, theme IDs, variants, or tech logo slugs; always instruct agents to discover via `list_widget_catalog` and `search_tech_logos`.
- Never commit secrets or API keys.
