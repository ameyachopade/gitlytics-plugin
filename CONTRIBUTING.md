# Contributing to Gitlytics Agent Plugin & Skills

Thank you for contributing to the **Gitlytics Ecosystem**. This repository distributes the official Antigravity plugin, MCP configurations (`https://api.gitlytics.dev/mcp` and local stdio), and 4 Vercel Agent Skills (`npx skills add ameyachopade/gitlytics-plugin -g`).

## Getting Started

1. Fork and clone the repository:
   ```bash
   git clone https://github.com/ameyachopade/gitlytics-plugin.git
   cd gitlytics-plugin
   ```
2. Create a feature branch:
   ```bash
   git checkout -b feat/your-change
   ```

## Local Verification

Before opening a pull request, run the offline validator from the repository root:

```bash
python scripts/validate_plugin.py
```

This verifies:
- `plugin.json` conforms strictly to the Antigravity plugin schema.
- `mcp_config.json` and `mcp_config.local.json` are valid JSON and properly namespaced.
- Every `skills/<name>/SKILL.md` has valid YAML frontmatter matching its directory name, stays under 500 lines, has valid relative `references/` links, and includes `evals/evals.json`.
- `rules/AGENTS.md` has no YAML frontmatter.
- Zero em dashes or en dashes appear in any text file.

## Standards & Guardrails

- **Concise Skills**: Keep `SKILL.md` files concise and imperative (under 350 lines preferred) and move long examples or playbooks into `references/`.
- **Live Catalog Discovery**: Never invent or guess Gitlytics card slugs, theme IDs, variants, or tech logo slugs; always instruct agents to discover via `list_widget_catalog` and `search_tech_logos` and validate via `build_widget_embed`.
- **Zero Secrets**: Never commit API keys, OAuth tokens, or GitHub PATs.
- **Security Issues**: Follow [SECURITY.md](SECURITY.md) and report vulnerabilities privately.

## Pull Request Checklist

- [ ] `python scripts/validate_plugin.py` prints `PASS`
- [ ] Any new or updated skill includes realistic test prompts in `evals/evals.json`
- [ ] No secrets or hardcoded tokens are staged

## The Gitlytics Ecosystem

| Project | Role | Link |
| :--- | :--- | :--- |
| [gitlytics](https://github.com/ameyachopade/gitlytics) | Core Python library, CLI, local stdio MCP & local dashboard | [PyPI](https://pypi.org/project/gitlytics) |
| [gitlytics-plugin](https://github.com/ameyachopade/gitlytics-plugin) *(this repo)* | Official Antigravity plugin, MCP config & 4 `npx skills` | [skills.sh](https://skills.sh/ameyachopade/gitlytics-plugin) |
| [gitlytics-github-traffic-automation](https://github.com/ameyachopade/gitlytics-github-traffic-automation) | Composite GitHub Action for automated CSV backups | [GitHub Action](https://github.com/ameyachopade/gitlytics-github-traffic-automation) |
| **Gitlytics Web & Docs** | Homepage, Docs Hub & Engineering Blog | [gitlytics.dev](https://gitlytics.dev) / [docs.gitlytics.dev](https://docs.gitlytics.dev) / [blog.gitlytics.dev](https://blog.gitlytics.dev) |
| Gitlytics Cloud Dashboard & API | Hosted Analytics Dashboard, SVG Engine & MCP Server | [dashboard.gitlytics.dev](https://dashboard.gitlytics.dev) / [api.gitlytics.dev](https://api.gitlytics.dev) |
