<div align="center">

<img src="assets/logo.png" alt="Gitlytics Logo" width="120" />

# Gitlytics Agent Plugin & Skills

### Official MCP Server Config, Agent Skills (`npx skills`), and Antigravity Plugin for Gitlytics

<p align="center">
  <a href="https://api.gitlytics.dev/mcp-oauth"><img src="https://api.gitlytics.dev/api/badge/static.svg?label=MCP&message=OAuth%202.1%20%2B%20Streamable%20HTTP&theme=gitlytics-dark&variant=clay" alt="MCP Spec" height="28" /></a>
  <a href="https://skills.sh/ameyachopade/gitlytics-plugin"><img src="https://api.gitlytics.dev/api/badge/tech.svg?slug=vercel&style=icon_label_value&label=skills.sh&value=4%20Agent%20Skills&theme=gitlytics-dark&variant=clay" alt="Agent Skills" height="28" /></a>
  <a href="LICENSE"><img src="https://api.gitlytics.dev/api/badge/static.svg?label=License&message=Apache%202.0&theme=gitlytics-dark&variant=clay" alt="License" height="28" /></a>
  <a href="https://dashboard.gitlytics.dev"><img src="https://api.gitlytics.dev/api/badge/static.svg?label=Dashboard&message=dashboard.gitlytics.dev&theme=gitlytics-dark&variant=clay" alt="Dashboard" height="28" /></a>
  <a href="https://docs.gitlytics.dev"><img src="https://api.gitlytics.dev/api/badge/static.svg?label=Docs&message=docs.gitlytics.dev&theme=gitlytics-dark&variant=clay" alt="Docs" height="28" /></a>
</p>

Connect **Antigravity**, **Claude Code**, **Cursor**, **Windsurf**, **Codex**, and **OpenCode** to Gitlytics' GitHub traffic analytics, star history, AI health scorecards, and 50-theme dynamic SVG README widgets.

</div>

---

## Quick Start

### 1. Install Agent Skills via Vercel CLI (`skills.sh`)

Works across Claude Code, Cursor, Codex, OpenCode, and Antigravity:

```bash
npx skills add ameyachopade/gitlytics-plugin -g
```

Install an individual skill:

```bash
npx skills add ameyachopade/gitlytics-plugin@gitlytics-widgets -g
npx skills add ameyachopade/gitlytics-plugin@gitlytics-badges -g
npx skills add ameyachopade/gitlytics-plugin@gitlytics-analytics -g
npx skills add ameyachopade/gitlytics-plugin@gitlytics-automation -g
```

### 2. Connect the Hosted Cloud MCP Server (Zero Python / Zero Key Required)

Choose the endpoint that matches your workflow:
* **1-Click OAuth 2.1 Sign-In (All 9 tools - public + private workspace):** `https://api.gitlytics.dev/mcp-oauth`
* **Zero-Login Public Mode (5 public widget, badge, logo, profile & star-history tools immediately):** `https://api.gitlytics.dev/mcp`
* **Headless / CI Fallback:** `https://api.gitlytics.dev/mcp` with a scoped `glt_live_...` API key from [dashboard.gitlytics.dev/integrations](https://dashboard.gitlytics.dev/integrations).

**Antigravity / Cursor / Windsurf (`mcp_config.json` - 1-Click OAuth 2.1 Sign-In):**
```json
{
  "mcpServers": {
    "gitlytics": {
      "type": "http",
      "url": "https://api.gitlytics.dev/mcp-oauth"
    }
  }
}
```

**Public Widgets & Badges Only (Zero Login Required):**
```json
{
  "mcpServers": {
    "gitlytics": {
      "type": "http",
      "url": "https://api.gitlytics.dev/mcp"
    }
  }
}
```

**Claude Code:**
```bash
# 1-click OAuth 2.1 sign-in (all 9 tools)
claude mcp add --transport http gitlytics https://api.gitlytics.dev/mcp-oauth

# Or zero-login public tools only
claude mcp add --transport http gitlytics https://api.gitlytics.dev/mcp
```

**Headless / CI API Key Fallback:**
Pass `Authorization: Bearer ${GITLYTICS_API_KEY}` in your client's `headers` on `https://api.gitlytics.dev/mcp` (or `--header "Authorization: Bearer ${GITLYTICS_API_KEY}"` in Claude Code).

### 3. Optional Local/Offline Stdio Mode (`gitlytics[mcp]`)

For privacy-first users querying local `traffic_*.csv` archives without touching Gitlytics Cloud:

```bash
pip install "gitlytics[mcp]"
export GITLYTICS_TOKEN="your_github_token_in_env"
gitlytics mcp --data-dir ./data
```

See [mcp_config.local.json](mcp_config.local.json) for the local stdio configuration template.

---

## Exposed MCP Tools

### Public Tools (No API Key Needed)

| Tool | Purpose |
| :--- | :--- |
| `list_widget_catalog` | Lists all 50 profile cards, 50 themes, 20 visual variants, shapes, and tech logo totals. |
| `search_tech_logos` | Searches the 200 verified tech logo slugs by keyword or category. |
| `build_widget_embed` | Validates parameters and generates SVG URLs, Markdown, HTML, and light/dark `<picture>` embeds. |
| `get_public_github_profile` | Fetches cached public GitHub user stats and top public repositories. |
| `get_public_star_history` | Returns cached cumulative star history and next star milestone projection. |

### Authenticated Cloud Tools (`glt_live_...` Scoped API Key)

| Tool | Required Scope | Purpose |
| :--- | :--- | :--- |
| `list_connected_repos` | `read:traffic` | Lists repositories connected to your Gitlytics Cloud workspace. |
| `get_repo_traffic` | `read:traffic` | Queries archived views, unique visitors, clones, referrers, and top paths (up to 365 days). |
| `get_ai_health_analysis` | `read:analysis` | Reads cached AI health scorecards, key areas, dev focus, and recommendations. |
| `trigger_repo_refresh` | `write:refresh` | Triggers a cooldown-bounded on-demand traffic sync from GitHub. |

### MCP Resources

* `gitlytics://catalog/widgets` - Complete JSON catalog of cards, variants, and shapes.
* `gitlytics://catalog/themes` - Complete JSON catalog of all 50 unified themes.

---

## Included Skills (4)

| Skill | Focus |
| :--- | :--- |
| [`gitlytics-widgets`](skills/gitlytics-widgets/SKILL.md) | GitHub profile README cards (50 cards), 50 unified themes, 20 visual variants, charts, and light/dark `<picture>` layouts. |
| [`gitlytics-badges`](skills/gitlytics-badges/SKILL.md) | Tech-stack logo capsules (200 verified icons), custom concept badges, live views/clones/stars badges, and PyPI version badges. |
| [`gitlytics-analytics`](skills/gitlytics-analytics/SKILL.md) | Traffic anomaly diagnostics, clone-to-visitor conversion analysis, star projections, and AI health scorecards. |
| [`gitlytics-automation`](skills/gitlytics-automation/SKILL.md) | Defeating GitHub's 14-day traffic limit via GitHub Actions, local `gitlytics sync` cron jobs, and safe self-hosted dashboards. |

---

## Repository Structure

```text
gitlytics-plugin/
├── plugin.json                  # Antigravity plugin manifest
├── mcp_config.json              # Hosted Streamable HTTP MCP config
├── mcp_config.local.json        # Optional local stdio MCP template
├── rules/AGENTS.md              # Always-on agent guardrails
├── assets/logo.png              # Plugin icon
├── skills/
│   ├── gitlytics-widgets/       # SKILL.md + references + evals
│   ├── gitlytics-badges/        # SKILL.md + references + evals
│   ├── gitlytics-analytics/     # SKILL.md + references + evals
│   └── gitlytics-automation/    # SKILL.md + references + evals
├── scripts/validate_plugin.py   # Offline schema & lint validator
├── SECURITY.md
├── CONTRIBUTING.md
└── LICENSE
```

## Validation

```bash
python scripts/validate_plugin.py
```

---

## 🔗 The Gitlytics Ecosystem

| Project | Role | Link |
| :--- | :--- | :--- |
| **[gitlytics](https://github.com/ameyachopade/gitlytics)** | Core Python library, CLI (`fetch`, `sync`, `stars`, `dashboard`, `mcp`), and self-hosted local dashboard | [PyPI](https://pypi.org/project/gitlytics/) |
| **[gitlytics-npm](https://github.com/ameyachopade/gitlytics-npm)** | Zero-dependency Node.js CLI, JS/TS SDK, dual-mode MCP & local dashboard | [npm (`@gitlytics/cli`)](https://www.npmjs.com/package/@gitlytics/cli) |
| **[gitlytics-plugin](https://github.com/ameyachopade/gitlytics-plugin)** *(this repo)* | Official Antigravity plugin, MCP configs & 4 Vercel Agent Skills | [skills.sh](https://skills.sh/ameyachopade/gitlytics-plugin) |
| **[gitlytics-github-traffic-automation](https://github.com/ameyachopade/gitlytics-github-traffic-automation)** | Composite GitHub Action for automated CSV traffic backups | [GitHub Action](https://github.com/ameyachopade/gitlytics-github-traffic-automation) |
| **[gitlytics-metadata-pages](https://github.com/ameyachopade/gitlytics-metadata-pages)** | Official Homepage, Docs Hub & Engineering Blog | [gitlytics.dev](https://gitlytics.dev) / [docs.gitlytics.dev](https://docs.gitlytics.dev) |
| **Gitlytics Cloud Dashboard** | Hosted Analytics Dashboard, Embed Studio & MCP OAuth Consent UI | [dashboard.gitlytics.dev](https://dashboard.gitlytics.dev) |
| **Gitlytics Hosted API & MCP** | 50-card / 200-logo SVG engine & Streamable HTTP MCP server (`/mcp`) | [api.gitlytics.dev](https://api.gitlytics.dev) |

---

## 🤝 Contributing, Security & License

- **Contributing**: See [`CONTRIBUTING.md`](CONTRIBUTING.md) for skill guidelines and validator checks.
- **Security**: See [`SECURITY.md`](SECURITY.md) for credential safety and private vulnerability reporting.
- **License**: Licensed under the [Apache License 2.0](LICENSE).
