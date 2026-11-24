# Gitlytics Plugin Guardrails

- Always call `list_widget_catalog` or `search_tech_logos` before choosing a Gitlytics card ID, theme name, visual variant, shape, or tech logo slug. Never invent or guess widget identifiers from memory.
- Always generate hosted Gitlytics SVG URLs and Markdown through `build_widget_embed` so every parameter is validated against the live renderer.
- Never ask the user to paste a raw GitHub Personal Access Token (PAT) into chat. For Gitlytics Cloud MCP (`https://api.gitlytics.dev/mcp`), public widget/badge/profile/star tools work with zero login; private workspace tools use OAuth 2.1 + PKCE direct sign-in in IDEs (primary) or scoped `glt_live_...` API keys minted at https://dashboard.gitlytics.dev/integrations (headless CI/CD fallback). For local stdio MCP (`gitlytics mcp` or `npx -y @gitlytics/cli mcp --mode local`), guide the user to set `GITLYTICS_TOKEN` in process environment variables.
- Keep the product boundary clear: hosted SVG cards, tech logos, badges, and Cloud MCP are served by `https://api.gitlytics.dev`; local CSV vaults, CLI, SDK, local dashboard, and offline stdio MCP are provided by PyPI `gitlytics` (`pip install gitlytics` / `uvx gitlytics`) and npm `@gitlytics/cli` (`npm install -g @gitlytics/cli` / `npx @gitlytics/cli`).
- Do not use em dashes or en dashes in generated README snippets or reports. Use regular hyphens (-).
