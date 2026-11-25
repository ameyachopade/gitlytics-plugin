---
name: gitlytics-badges
description: >-
  Generate clean, high-contrast GitHub README tech-stack badges, brand logo
  capsules (200 verified tech icons), custom concept capsules, live GitHub
  views/clones/stars badges, and live PyPI version badges using Gitlytics
  (api.gitlytics.dev). Trigger whenever the user asks for README badges, tech
  stack pills, Shields.io alternatives, PyPI version badges, license/status
  badges, or icon rows for a repository README.
---

# Gitlytics Badges Skill

Build cohesive, theme-adapted SVG badge strips for repository READMEs using the Gitlytics hosted badge engine (`https://api.gitlytics.dev`): 200 verified tech logos, 50 unified themes, 20 visual variants, and 8 badge shapes (`rounded`, `pill`, `square`, `chamfer`, `chevron`, `ticket`, `tag`, `shield`).

## Non-Negotiable Rules

1. **Always verify logo slugs first (in one batch call).** Call `search_tech_logos(queries=[...])` for the whole detected stack (up to 25 terms per call) before building badges. Never guess a slug like `nextjs` (the verified slug is `nextdotjs`) or `vue` (`vuedotjs`).
2. **Always validate via `build_widget_batch` (for 2+ badges) or `build_widget_embed` (for 1 badge).** Never hand-write raw query strings.
3. **Match one theme and one variant across the whole strip.** Pick one theme from `list_widget_catalog(sections=["themes", "variants", "shapes"], compact=True)` (e.g. `gitlytics-dark`, `tokyonight`, `dracula`, `catppuccin-mocha`, `nord`, `scientific-lab`) and one variant (`clay`, `bento`, `flat`, `glass`, `neobrutal`, `terminal`), and pass them once in `build_widget_batch(defaults={...})`.
4. **Use custom concept capsules for non-brand terms.** For architecture concepts without a brand logo (e.g. `MCP`, `RAG`, `GraphQL Federation`), use `kind="static_badge"` without inventing a fake logo slug.

## Workflow

### Step 1: Detect Real Stack from Manifests
Inspect `package.json`, `pyproject.toml`, `requirements.txt`, `Cargo.toml`, `go.mod`, `Dockerfile`, or `.github/workflows/` to gather exact versions, license, and PyPI package name (if applicable).

### Step 2: Resolve Verified Slugs and Theme (1-2 Calls Total)
- Call `search_tech_logos(queries=[...])` once with all detected technologies to resolve verified slugs and aliases (`postgres` -> `postgresql`, `nextjs` -> `nextdotjs`).
- Call `list_widget_catalog(sections=["themes", "variants", "shapes"], compact=True)` only if you need to confirm a theme ID, variant, or badge shape.

### Step 3: Generate Validated Badges in One Batch Call
Call `build_widget_batch` with shared `defaults` (e.g. `theme`, `variant`, `shape`, `owner`, `repo`), `format="markdown"` (or `"html"` / `"picture"`), `layout="inline_markdown"` (or `"centered_html"`), and up to 30 `items`:
- **Tech stack capsule (`kind="tech_badge"`)**: `slug`, `style="icon_label_value"` (or `"icon_label"`), `label`, `value`, optional `href`.
- **Static status / license / link badge (`kind="static_badge"`)**: `label`, `message`, optional `slug`, `color`, `href`.
- **Live GitHub repo metric (`kind="live_badge"`)**: `owner`, `repo`, `metric` (`views`, `clones`, or `stars`), optional `href`.
- **Live PyPI version (`kind="pypi_badge"`)**: `package_name`, optional `label="PyPI"`, `href`.

For a single standalone badge, call `build_widget_embed` directly.

### Step 4: Format Cleanly
Use the ready-to-paste `combined_snippet` returned by `build_widget_batch`, or consult [references/badge-recipes.md](references/badge-recipes.md) for grouped badge rows (top status strip vs. dedicated tech-stack section) and crisp spacing patterns.
