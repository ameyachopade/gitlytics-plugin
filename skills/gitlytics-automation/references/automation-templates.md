# Gitlytics Automation & Self-Hosting Templates

## 1. Companion GitHub Action (`.github/workflows/gitlytics-traffic.yml`)

Runs every Sunday at 00:00 UTC (well inside GitHub's 14-day window) and supports manual triggers:

```yaml
name: Gitlytics Traffic Archive

on:
  schedule:
    - cron: "0 0 * * 0"
  workflow_dispatch:

permissions:
  contents: write

jobs:
  snapshot:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Sync GitHub traffic archive
        uses: ameyachopade/gitlytics-github-traffic-automation@v1.2.0
        with:
          github_token: ${{ secrets.TRAFFIC_TOKEN }}
          data_dir: "./data"
          public_only: "true"
```

Setup checklist:
1. Create a GitHub Personal Access Token with repository traffic read access.
2. Save it under **Repository Settings -> Secrets and variables -> Actions** as `TRAFFIC_TOKEN`.
3. Run the workflow once via **Actions -> Gitlytics Traffic Archive -> Run workflow**.

## 2. Local CLI Scheduled Sync

```bash
pip install gitlytics
export GITLYTICS_TOKEN="your_token_in_env_only"

# One-shot snapshot + React dashboard JSON export
gitlytics sync --data-dir "./data" --public-only --export-json "./data/export.json"

# Continuous daily sync at 11:00 PM
gitlytics sync --data-dir "./data" --public-only --schedule-cron "0 23 * * *"
```

## 3. Local / Self-Hosted Dashboard

```bash
pip install "gitlytics[dashboard]"

# Safe default: loopback only (127.0.0.1:8000)
gitlytics dashboard --data-dir "./data"

# Non-loopback bind (ONLY behind an authenticated reverse proxy / private VPN)
gitlytics dashboard --host 0.0.0.0 --port 8000 --public-bind --data-dir "./data"
```

## 4. Python SDK Pipeline

```python
import os
import gitlytics

gitlytics.sync(
    token=os.environ["GITLYTICS_TOKEN"],
    data_dir="./data",
    output_mode="monthly",
    export_json="./data/export.json",
    export_public_only=True,
    public_only=True,
)
```
