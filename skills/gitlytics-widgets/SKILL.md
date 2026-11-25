---
name: gitlytics-widgets
description: >-
  Design, validate, and assemble GitHub README banners, developer profile SVG
  cards, tech-stack badge rows, live repo metric badges, PyPI badges, and star
  history charts powered by Gitlytics (api.gitlytics.dev). Trigger whenever the
  user wants to upgrade a README, decorate a GitHub profile, add tech stack
  badges, generate SVG stat cards, pick dark/light GitHub themes, or embed live
  views/clones/stars charts, even if they do not explicitly mention Gitlytics.
---

# Gitlytics Widgets Skill

Create cohesive, visually sharp, and 100% server-validated GitHub README widgets using the Gitlytics hosted rendering engine (`https://api.gitlytics.dev`): 50 profile cards, 50 unified themes, 20 visual variants, universal shapes, and 200 verified technology logos.

## Non-Negotiable Rules

1. **Discover before choosing.** Call `list_widget_catalog` (with `sections` / `compact=True` when you only need IDs) and `search_tech_logos(queries=[...])` before selecting any `card_type`, `theme`, `variant`, `shape`, or `slug`. Never guess identifiers from memory.
2. **Validate every URL.** Call `build_widget_batch` (preferred for 2+ cards, badges, or charts in 1 call) or `build_widget_embed` (for a single widget). Never hand-craft query strings that bypass validation.
3. **Visual coherence.** Pick ONE cohesive theme family (or a matched dark + light pair using `<picture>`) and ONE primary visual variant (`clay`, `bento`, `flat`, `glass`, `neobrutal`, `terminal`, etc.) across all widgets in the same README, passing them once in `build_widget_batch(defaults={...})`.
4. **No auth required.** All widget discovery and embed tools are public read-only endpoints and work even without a Gitlytics API key.

## Workflow

### Step 1: Audit Context
- For a **repository README**: inspect manifests (`package.json`, `pyproject.toml`, `Cargo.toml`, `go.mod`, `Dockerfile`, `.github/workflows/`) to identify the real tech stack, package name (PyPI if Python), and `owner/repo`.
- For a **GitHub profile README**: confirm the GitHub `username` and desired tone (clean studio, developer dark, retro terminal, high-contrast minimal, etc.).

### Step 2: Query Authoritative Registries
- Call `list_widget_catalog` (optionally filtering by `category`, `light_only`, `sections`, or `compact=True`) to inspect available card slugs, themes, variants, and shapes.
- Call `search_tech_logos(queries=[...])` once for all technologies in the stack to get verified `slug` values. For architecture concepts without a brand logo (e.g. `RAG`, `MCP`, `GraphQL Federation`), use `kind="static_badge"`.

### Step 3: Build Validated Embeds
Prefer `build_widget_batch` when creating multiple widgets (up to 30 per call, with shared `defaults`, `format`, and optional `layout="inline_markdown"` / `"centered_html"`), or `build_widget_embed` for a single widget:
- **Profile cards (`kind="card"`)**: pass `username`, `card_type`, `theme`, `variant`, optional `shape`, and optional `dark_theme` + `light_theme` to get ready-to-paste dual-theme `<picture>` HTML.
- **Tech badges (`kind="tech_badge"`)**: pass `slug`, `style="icon_label_value"` (or `"icon_label"`), `label`, `value`, `theme`, `variant`, optional `shape` and `href`.
- **Static badges (`kind="static_badge"`)**: pass `label`, `message`, `theme`, `variant`, and optional `slug`, `color`, `href`.
- **Live repo badges (`kind="live_badge"`)**: pass `owner`, `repo`, `metric` (`views`, `clones`, or `stars`), `theme`, and `variant`.
- **PyPI badges (`kind="pypi_badge"`)**: pass `package_name`, `theme`, and `variant`.
- **Traffic & star charts (`kind="chart"` / `kind="star_history"`)**: pass `owner`, `repo`, `metric` (for `chart`), `theme`, and `variant`.

### Step 4: Assemble GitHub-Safe Layout
Read [references/widget-layouts.md](references/widget-layouts.md) for proven GitHub Markdown and HTML layout patterns (centered badge strips, 2-column borderless card grids, and `<picture>` light/dark theme switching).

## Output Checklist
- Every embedded URL was produced by `build_widget_batch` or `build_widget_embed`.
- Theme and variant stay consistent across header badges, profile cards, and charts.
- If the user's audience uses both GitHub light and dark modes, prefer the `dual_theme_picture_html` snippet returned by `build_widget_batch` / `build_widget_embed`.
- Keep alt text descriptive and concise for accessibility.
