# Gitlytics Badge Strip Recipes

Use these patterns with validated embeds returned by `build_widget_batch` (preferred for 2+ badges) or `build_widget_embed` (for a single badge).

## 0. One-Call Batch Badge Row (`build_widget_batch`)

Pass shared styling once in `defaults` and set `layout="inline_markdown"` or `layout="centered_html"` to get a ready-to-paste `combined_snippet`:

```json
{
  "defaults": {
    "theme": "gitlytics-dark",
    "variant": "clay",
    "owner": "owner",
    "repo": "repo"
  },
  "format": "markdown",
  "layout": "inline_markdown",
  "items": [
    {"kind": "tech_badge", "slug": "python", "href": "https://python.org"},
    {"kind": "tech_badge", "slug": "fastapi"},
    {"kind": "live_badge", "metric": "stars"},
    {"kind": "static_badge", "label": "License", "message": "Apache 2.0"}
  ]
}
```

## 1. Repository Header Status Strip (PyPI + License + Live Metrics)

Keep the top header strip to 4 to 6 high-signal badges:

```markdown
[![PyPI](PYPI_BADGE_URL)](https://pypi.org/project/your-pkg/)
[![License](LICENSE_BADGE_URL)](LICENSE)
[![Views](LIVE_VIEWS_BADGE_URL)](https://dashboard.gitlytics.dev)
[![Stars](LIVE_STARS_BADGE_URL)](https://github.com/owner/repo/stargazers)
```

## 2. Centered Tech Stack Row

Group stack capsules cleanly with uniform `theme`, `variant`, and `shape`:

```html
<div align="center">
  <img src="PYTHON_BADGE_URL" alt="Python" />
  <img src="FASTAPI_BADGE_URL" alt="FastAPI" />
  <img src="REACT_BADGE_URL" alt="React" />
  <img src="DOCKER_BADGE_URL" alt="Docker" />
</div>
```

## 3. Common Verified Logo Slug Reminders

Always confirm with `search_tech_logos`:
- Next.js -> `nextdotjs`
- Node.js -> `nodedotjs`
- Vue.js -> `vuedotjs`
- C++ -> `cplusplus`
- C# -> `csharp`
- Tailwind CSS -> `tailwindcss`
- PostgreSQL -> `postgresql`
- GitHub Actions -> `githubactions`
