---
name: gitlytics-automation
description: >-
  Set up automated GitHub traffic archiving to defeat GitHub's 14-day traffic
  retention limit, configure the Gitlytics GitHub Action workflow, schedule
  local CLI CSV vault syncs (`gitlytics sync`), export historical CSV archives
  to JSON, and safely run the self-hosted `gitlytics dashboard`. Trigger
  whenever the user wants to back up GitHub traffic automatically, set up a
  GitHub Action for traffic history, configure cron syncs, migrate CSV traffic
  data, or self-host the Gitlytics dashboard.
---

# Gitlytics Automation & Archiving Skill

Automate indefinite GitHub traffic retention and secure local/self-hosted Gitlytics deployments without leaking tokens or exposing unauthenticated dashboards.

## Security Rules

1. **Never hardcode tokens** in workflow YAML, shell scripts, or committed files. Always use `${{ secrets.TRAFFIC_TOKEN }}` in GitHub Actions or `GITLYTICS_TOKEN` in local environment variables.
2. **Dashboard loopback safety:** `gitlytics dashboard` binds to `127.0.0.1` by default. Never pass `--public-bind` unless the user explicitly places it behind a trusted reverse proxy with authentication, and remind them that `--token` / `GITLYTICS_TOKEN` is intentionally disabled on non-loopback binds.
3. **Private repo hygiene:** Default to `--public-only` / `export_public_only=True` when committing traffic CSVs or JSON exports to a public repository so private repository names never leak.

## Workflow

### Step 1: Choose the Right Archiving Strategy
Ask or infer which mode fits the user's setup:
1. **GitHub Action (recommended for zero-server archiving):** Runs every 13 days (or weekly) using `ameyachopade/gitlytics-github-traffic-automation@v1.2.0` and commits deduplicated monthly CSVs (`traffic_YYYY-MM.csv`) into the repo.
2. **Local CLI Cron (`gitlytics sync`):** Runs locally via `pip install gitlytics` with `--schedule-cron "0 23 * * *"` and optional `--export-json ./data/export.json`.
3. **Gitlytics Cloud (`https://dashboard.gitlytics.dev`):** Managed nightly archiving into Supabase with automatic MCP access via `https://api.gitlytics.dev/mcp`.

### Step 2: Generate Verified Configs
Consult [references/automation-templates.md](references/automation-templates.md) for the exact GitHub Action YAML, local cron CLI flags, Python SDK pipeline snippet, and safe self-hosted dashboard startup commands.

### Step 3: Verify Output Contract
- Confirm workflow permissions are minimal (`contents: write` only on the archiving job).
- Confirm token secret setup instructions clearly state required fine-grained or classic scopes (`Administration: Read` / `repo` traffic read).
- Confirm `gitlytics fetch ... > out.csv` stdout/stderr separation when building shell pipelines.
