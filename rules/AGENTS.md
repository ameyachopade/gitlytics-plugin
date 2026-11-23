# Gitlytics Plugin Guardrails

- Always call `list_widget_catalog` or `search_tech_logos` before choosing a Gitlytics card ID, theme name, visual variant, shape, or tech logo slug. Never invent or guess widget identifiers from memory.
- Always generate hosted Gitlytics SVG URLs and Markdown through `build_widget_embed` so every parameter is validated against the live renderer.
- Never ask the user to paste a raw GitHub Personal Access Token (PAT) into chat. For Gitlytics Cloud MCP, guide them to mint a scoped `glt_live_...` API key at https://dashboard.gitlytics.dev/integrations. For local stdio MCP (`gitlytics mcp`), guide them to set `GITLYTICS_TOKEN` in process environment variables.
- Keep the product boundary clear: the hosted SVG cards, tech logos, and badges are served by `https://api.gitlytics.dev`; the `pip install gitlytics` wheel provides the traffic CLI, Python SDK, local dashboard, and optional local stdio MCP server (`gitlytics mcp`).
- Do not use em dashes or en dashes in generated README snippets or reports. Use regular hyphens (-).
