<div align="center">

<img src="https://raw.githubusercontent.com/ameyachopade/gitlytics/main/assets/logo.png" alt="Gitlytics Logo" width="140" />

# Gitlytics Agent Plugin & Skills

### Official MCP Server Config, Agent Skills (`npx skills`), and Antigravity Plugin for Gitlytics

<!-- GITLYTICS:ECOSYSTEM_BADGES:START -->
[![PyPI](https://api.gitlytics.dev/api/badge/pypi/gitlytics.svg?label=PyPI&color=E25A1C&theme=gitlytics-dark&variant=clay)](https://pypi.org/project/gitlytics/)
[![npm](https://api.gitlytics.dev/api/badge/npm/@gitlytics/cli.svg?label=npm&color=E25A1C&theme=gitlytics-dark&variant=clay)](https://www.npmjs.com/package/@gitlytics/cli)
[![License](https://api.gitlytics.dev/api/badge/static.svg?label=License&message=Apache+2.0&color=334155&theme=gitlytics-dark&variant=clay)](LICENSE)
[![Agent Skills](https://api.gitlytics.dev/api/badge/skills/ameyachopade/gitlytics-plugin.svg?label=skills.sh&color=334155&theme=gitlytics-dark&variant=clay)](https://skills.sh/ameyachopade/gitlytics-plugin)
[![MCP](https://api.gitlytics.dev/api/badge/static.svg?label=MCP&message=OAuth+2.1&color=E25A1C&theme=gitlytics-dark&variant=clay)](https://docs.gitlytics.dev/mcp)

<br/>

[![Home](https://api.gitlytics.dev/api/badge/static.svg?label=Site&message=gitlytics.dev&color=334155&theme=gitlytics-dark&variant=clay)](https://gitlytics.dev)
[![Dashboard](https://api.gitlytics.dev/api/badge/static.svg?label=App&message=dashboard.gitlytics.dev&color=334155&theme=gitlytics-dark&variant=clay)](https://dashboard.gitlytics.dev)
[![Widgets](https://api.gitlytics.dev/api/badge/static.svg?label=Widgets&message=widgets.gitlytics.dev&color=334155&theme=gitlytics-dark&variant=clay)](https://widgets.gitlytics.dev)
[![Docs](https://api.gitlytics.dev/api/badge/static.svg?label=Docs&message=docs.gitlytics.dev&color=334155&theme=gitlytics-dark&variant=clay)](https://docs.gitlytics.dev)
[![Blog](https://api.gitlytics.dev/api/badge/static.svg?label=Blog&message=blog.gitlytics.dev&color=334155&theme=gitlytics-dark&variant=clay)](https://blog.gitlytics.dev)
<!-- GITLYTICS:ECOSYSTEM_BADGES:END -->

<br/>

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
* **1-Click OAuth 2.1 Sign-In (All 12 tools - public + private workspace):** `https://api.gitlytics.dev/mcp-oauth`
* **Zero-Login Public Mode (6 public widget, batch badge, logo, profile & star-history tools immediately):** `https://api.gitlytics.dev/mcp`
* **Headless / CI Fallback:** `https://api.gitlytics.dev/mcp` with a scoped `glt_live_...` API key from [dashboard.gitlytics.dev/integrations](https://dashboard.gitlytics.dev/integrations).

**Antigravity / Cursor / Windsurf / VS Code / OpenCode (`mcp_config.json` / `mcp.json` - 1-Click OAuth 2.1 Sign-In):**
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

**CLI Agents (Claude Code / Codex):**
```bash
# Claude Code - 1-click OAuth 2.1 sign-in (all 12 tools)
claude mcp add --transport http gitlytics https://api.gitlytics.dev/mcp-oauth

# Claude Code - zero-login public tools only
claude mcp add --transport http gitlytics https://api.gitlytics.dev/mcp

# Codex - 1-click OAuth 2.1 sign-in
codex mcp add gitlytics --url https://api.gitlytics.dev/mcp-oauth
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
| `list_widget_catalog` | Lists all 50 profile cards, 50 themes, 20 visual variants, shapes, and tech logo totals (supports `sections` and `compact` filters). |
| `search_tech_logos` | Searches the 200 verified tech logo slugs by single `query` or batch `queries` (up to 25 technologies in 1 call, with alias resolution). |
| `build_widget_embed` | Validates parameters and generates SVG URLs, Markdown, HTML, and light/dark `<picture>` embeds for a single widget (cards, tech/static/live/PyPI/npm/skills badges, logos, charts, star history; supports `href` and `format`). |
| `build_widget_batch` | Validates and generates up to 30 badges, cards, logos, or charts in 1 call with shared `defaults`, README `layout` assembly, `include_items`, and partial error recovery. |
| `get_public_github_profile` | Fetches cached public GitHub user stats and top public repositories. |
| `get_public_star_history` | Returns cached cumulative star history and next star milestone projection. |

### Authenticated Cloud Tools (OAuth 2.1 or `glt_live_...` Scoped API Key)

| Tool | Required Scope | Purpose |
| :--- | :--- | :--- |
| `list_connected_repos` | `read:traffic` | Lists repositories connected to your Gitlytics Cloud workspace. |
| `get_workspace_summary` | `read:traffic` | Aggregates views, visitors, clones, stars, forks, and optional cached AI health scores (`include_health=true`, requires `read:analysis`) across all connected repositories in 1 call. |
| `get_repo_traffic` | `read:traffic` | Queries archived views, unique visitors, clones, referrers, and top paths (up to 365 days; supports `daily`, `weekly`, or `summary` granularity). |
| `get_ai_health_analysis` | `read:analysis` | Reads cached AI health scorecards, key areas, dev focus, and recommendations (falls back to last saved run with `stale: true` if >24h old). |
| `trigger_ai_analysis` | `write:refresh` | Runs an on-demand Deep AI Health Analysis when no fresh (<24h) cache exists (6h per-repo cooldown + daily budget). |
| `trigger_repo_refresh` | `write:refresh` | Triggers a cooldown-bounded on-demand traffic sync from GitHub. |

### Interactive MCP Apps (SEP-1865)

Clients that support MCP Apps (`text/html;profile=mcp-app`, such as Antigravity) automatically render interactive UI views while CLI and text-only agents continue receiving compact structured JSON:

| MCP App (`ui://` Resource) | Triggered By | Highlights |
| :--- | :--- | :--- |
| **Gitlytics Traffic Dashboard** (`ui://gitlytics/traffic-dashboard.html`) | `get_workspace_summary`, `get_repo_traffic` | Interactive Line/Bar charts with click-to-pin HUD, Views/Uniques/Clones/Avg toggles, clickable Referrers & Paths, Star History curve, AI Health sub-tab, Markdown export, and both Side Pane (`aux_pane`) + Full-Page Sidebar (`global`) entrypoints. |
| **Gitlytics AI Health Scorecard** (`ui://gitlytics/health-scorecard.html`) | `get_ai_health_analysis`, `trigger_ai_analysis` | Radial health gauge with tier badge, expandable directory Key Areas, interactive Action Checklist with progress bar and per-item chat actions, plus an on-demand Traffic Snapshot tab. |
| **Gitlytics Badge & Widget Studio** (`ui://gitlytics/badge-studio.html`) | `build_widget_embed`, `build_widget_batch` | Dynamic catalog loading (all 50 themes, 20 variants, valid shapes), searchable warm popover dropdowns, Dark/Light/Clay/Grid canvases, Zoom, Dual Light/Dark Split View, per-item batch reordering, and live `+ Add Tech Badge` search composer. |

All three apps also implement SEP-1865 `inline`, `fullscreen`, and `pip` display mode negotiation automatically when advertised by the host.

### MCP Resources & Prompts

* **Resources:**
  * `gitlytics://catalog/widgets` - Complete JSON catalog of cards, variants, and shapes.
  * `gitlytics://catalog/themes` - Complete JSON catalog of all 50 unified themes.
  * `gitlytics://catalog/logos` - Complete JSON catalog of all verified technology SVG logos.
  * `gitlytics://catalog/logos/{category}` & `gitlytics://catalog/cards/{category}` - Category-filtered resource templates.
* **Prompts:** `create_badge_row`, `upgrade_readme`, `audit_repo_traffic`.

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
| **Gitlytics Web & Docs** | Official Homepage, Docs Hub & Engineering Blog | [gitlytics.dev](https://gitlytics.dev) / [docs.gitlytics.dev](https://docs.gitlytics.dev) / [blog.gitlytics.dev](https://blog.gitlytics.dev) |
| **Gitlytics Cloud Dashboard** | Hosted Analytics Dashboard, Embed Studio & MCP OAuth Consent UI | [dashboard.gitlytics.dev](https://dashboard.gitlytics.dev) |
| **Gitlytics Hosted API & MCP** | 50-card / 200-logo SVG engine & Streamable HTTP MCP server (`/mcp-oauth` & `/mcp`) | [api.gitlytics.dev](https://api.gitlytics.dev) |

---

## 🤝 Contributing, Security & License

- **Contributing**: See [`CONTRIBUTING.md`](CONTRIBUTING.md) for skill guidelines and validator checks.
- **Security**: See [`SECURITY.md`](SECURITY.md) for credential safety and private vulnerability reporting.
- **License**: Licensed under the [Apache License 2.0](LICENSE).
