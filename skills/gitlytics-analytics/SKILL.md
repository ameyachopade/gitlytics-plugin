---
name: gitlytics-analytics
description: >-
  Audit GitHub repository traffic trends, diagnose view/clone spikes or drops,
  inspect top referrers and paths, project stargazer milestones, interpret AI
  health scorecards, and configure indefinite archiving to defeat GitHub's
  14-day traffic limit. Trigger whenever the user asks about GitHub repo views,
  clones, referrers, star growth, repository health, traffic anomalies, or
  backing up GitHub traffic data.
---

# Gitlytics Analytics Skill

Turn GitHub traffic snapshots, star trajectories, and AI health diagnostics into actionable engineering and distribution insights while protecting credentials and defeating GitHub's 14-day rolling data cliff.

## Security Rules

1. **Never ask for raw GitHub PATs in chat.**
   - For **Gitlytics Cloud MCP** (`https://api.gitlytics.dev/mcp`): public tools (`list_widget_catalog`, `search_tech_logos`, `build_widget_embed`, `build_widget_batch`, `get_public_github_profile`, `get_public_star_history`) require **zero login**. For private workspace tools, prefer **OAuth 2.1 + PKCE direct sign-in** in IDEs (zero config), or guide headless/CI users to mint a scoped `glt_live_...` key at `https://dashboard.gitlytics.dev/integrations` (`Authorization: Bearer ${GITLYTICS_API_KEY}`).
   - For **Local Stdio MCP** (`uvx gitlytics mcp` or `npx -y @gitlytics/cli mcp --mode local`): instruct the user to export `GITLYTICS_TOKEN` in their environment rather than passing secrets in prompts.
2. **Respect least privilege.** Request only `read:traffic` and `read:analysis` unless the user explicitly asks to trigger on-demand syncs (`write:refresh`).

## Workflow

### Step 1: Identify Available Mode
- **Cloud Workspace Mode (`gitlytics` HTTP MCP):** Call `list_connected_repos` to see tracked repositories and `last_synced_at`.
  - If `401` / `auth_required` is returned, explain that public tools (`get_public_github_profile`, `get_public_star_history`, widget/badge tools) work immediately with zero auth, and guide the user to sign in via OAuth 2.1 in their MCP client (or mint a scoped `glt_live_...` key on `https://dashboard.gitlytics.dev/integrations` for headless clients).
- **Local Vault Mode (`gitlytics-local` stdio via Python `uvx gitlytics mcp` or Node `npx -y @gitlytics/cli mcp --mode local`):** Call `local_query_csv_vault` first (works 100% offline with zero token). Use `local_fetch_traffic` or `local_sync_archive` only when live GitHub refresh is needed.

### Step 2: Gather Data Efficiently
- **Workspace overview (multi-repo)**: Call `get_workspace_summary(days=30)` to aggregate traffic and stars across all connected repositories in 1 call instead of looping per repo.
- **Single-repo traffic audit**: Call `get_repo_traffic(owner, repo, days=30)` (or `90` / `365` with `granularity="weekly"` or `"summary"` to keep context compact when looking beyond GitHub's 14-day window).
- **Health scorecard**: Call `get_ai_health_analysis(owner, repo, days=30, include_history=True)` to inspect `health_score`, `ai_overview`, `ai_key_areas`, `ai_dev_focus`, and `ai_recommendations` without burning extra LLM quota.
- **Star trajectory**: Call `get_public_star_history(owner, repo)` to calculate milestone ETA and correlate star surges with referrer spikes.
- **On-demand refresh**: Call `trigger_repo_refresh(owner, repo)` only when the user explicitly requests a fresh sync (note the 5-minute per-repo cooldown).

### Step 3: Diagnose and Report
Consult [references/traffic-diagnostics.md](references/traffic-diagnostics.md) for conversion benchmarks, anomaly triage, and 14-day backup automation templates. Present findings in this exact structure:
1. **Executive Summary** (date window, total views, unique visitors, clones, unique cloners, clone-to-visitor ratio, current stars).
2. **Traffic & Referrer Diagnostics** (top referrers, top paths, spike/drop root causes).
3. **Health & Growth Actions** (top 3 concrete, prioritized engineering or distribution actions).
4. **Data Retention Check** (if historical coverage is <= 14 days, recommend automated archiving via the GitHub Action or `gitlytics sync`).
