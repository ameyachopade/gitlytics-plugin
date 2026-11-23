# GitHub Traffic Diagnostics & Archiving Playbook

## Core Metrics and Interpretation

| Metric / Ratio | Formula | What It Signals |
| :--- | :--- | :--- |
| **Unique Visitor Share** | `unique_visitors / views` | > 0.60 indicates broad new discovery (social/search); < 0.35 indicates repeat visits by existing users or contributors. |
| **Clone-to-Visitor Ratio** | `unique_cloners / unique_visitors` | > 0.25 signals strong developer intent or CI/CD automation; > 1.0 almost always indicates automated CI bots or mirror polling. |
| **Referrer Concentration** | `top_referrer_views / total_views` | > 0.70 from a single external source (HN, Reddit, X, blog) signals a spike that will decay unless README conversion converts visitors to stars/installs. |
| **Path Engagement** | Share of views on `/blob/.../README.md`, `/releases`, `/issues` | High `/releases` share shows active consumers; high root-only share with low clones suggests README onboarding friction. |

## Diagnosing Spikes vs. Drops

1. **Sudden View Spike + Flat Clones**: External link/post drove curiosity, but install steps or hero clarity did not convert visitors. Check `top_referrer` and suggest adding a quick-start block and clear badges.
2. **Sudden Clone Spike + Flat Views**: CI pipeline, package build, or automated scraper polling the repo. Verify `unique_cloners` vs raw `clones`.
3. **Steady Drop Over > 14 Days**: Check `last_synced_at` first to ensure it is not a sync gap, then compare recent release cadence and AI health recommendations.

## Defeating GitHub's 14-Day Traffic Cliff

### Option A: Companion GitHub Action (Recommended for Cloudless Archiving)
Add `.github/workflows/gitlytics-traffic.yml` running every 13 days (or weekly) using `ameyachopade/gitlytics-github-traffic-automation@v1.2.0` with a repository secret (`TRAFFIC_TOKEN` stored in GitHub Actions Secrets - never hardcoded).

### Option B: Local Scheduled Cron (`gitlytics` CLI)
```bash
export GITLYTICS_TOKEN="your_token_in_env_only"
gitlytics sync --data-dir "./data" --schedule-cron "0 23 * * *"
```

### Option C: Gitlytics Cloud Automatic Nightly Sync
Connect up to 3 repositories in `https://dashboard.gitlytics.dev` for automatic nightly archiving into Supabase and instant MCP access via `get_repo_traffic`.
