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
   - For **Gitlytics Cloud MCP** (`https://api.gitlytics.dev/mcp`): instruct the user to generate a scoped, revocable `glt_live_...` key at `https://dashboard.gitlytics.dev/integrations` and configure it in their MCP client headers (`Authorization: Bearer ${GITLYTICS_API_KEY}`).
   - For **Local Stdio MCP** (`gitlytics mcp`): instruct the user to export `GITLYTICS_TOKEN` in their environment rather than passing secrets in prompts.
2. **Respect least privilege.** Request only `read:traffic` and `read:analysis` unless the user explicitly asks to trigger on-demand syncs (`write:refresh`).

## Workflow

### Step 1: Identify Available Mode
- **Cloud Workspace Mode (default):** Call `list_connected_repos` to see tracked repositories and `last_synced_at`.
  - If `auth_required` is returned, explain that public tools (`get_public_github_profile`, `get_public_star_history`) work immediately, and guide the user to mint a scoped `glt_live_...` key on `https://dashboard.gitlytics.dev/integrations` for private traffic/AI analysis.
- **Local Vault Mode (`gitlytics-local` stdio):** Call `local_query_csv_vault` first (works 100% offline with zero token). Use `local_fetch_traffic` or `local_sync_archive` only when live GitHub refresh is needed.

### Step 2: Gather Data Efficiently
- **Traffic audit**: Call `get_repo_traffic(owner, repo, days=30)` (or `90` / `365` when looking beyond GitHub's 14-day window).
- **Health scorecard**: Call `get_ai_health_analysis(owner, repo, days=30, include_history=True)` to inspect `health_score`, `ai_overview`, `ai_key_areas`, `ai_dev_focus`, and `ai_recommendations` without burning extra LLM quota.
- **Star trajectory**: Call `get_public_star_history(owner, repo)` to calculate milestone ETA and correlate star surges with referrer spikes.
- **On-demand refresh**: Call `trigger_repo_refresh(owner, repo)` only when the user explicitly requests a fresh sync (note the 5-minute per-repo cooldown).

### Step 3: Diagnose and Report
Consult [references/traffic-diagnostics.md](references/traffic-diagnostics.md) for conversion benchmarks, anomaly triage, and 14-day backup automation templates. Present findings in this exact structure:
1. **Executive Summary** (date window, total views, unique visitors, clones, unique cloners, clone-to-visitor ratio, current stars).
2. **Traffic & Referrer Diagnostics** (top referrers, top paths, spike/drop root causes).
3. **Health & Growth Actions** (top 3 concrete, prioritized engineering or distribution actions).
4. **Data Retention Check** (if historical coverage is <= 14 days, recommend automated archiving via the GitHub Action or `gitlytics sync`).
