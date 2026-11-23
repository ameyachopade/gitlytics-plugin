# GitHub README Widget Layout Recipes

Use these GitHub-compatible HTML and Markdown templates with URLs returned by `build_widget_embed`.

## 1. Centered Repository Header + Badge Strip

```html
<div align="center">
  <h1>Project Name</h1>
  <p>Concise one-line value proposition.</p>
  <p>
    <!-- Replace with validated URLs from build_widget_embed -->
    <img src="BADGE_1_URL" alt="Badge 1" />
    <img src="BADGE_2_URL" alt="Badge 2" />
    <img src="BADGE_3_URL" alt="Badge 3" />
  </p>
</div>
```

## 2. Dual Light/Dark Mode Profile Card (`<picture>`)

GitHub honors `<source media="(prefers-color-scheme: dark)">` and `light` automatically. Request `dark_theme` and `light_theme` in `build_widget_embed` (for example `dark_theme="tokyonight"` and `light_theme="gitlytics-light"` or `dark_theme="gitlytics-dark"` and `light_theme="gitlytics-light"`):

```html
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="DARK_CARD_URL" />
  <source media="(prefers-color-scheme: light)" srcset="LIGHT_CARD_URL" />
  <img alt="GitHub Profile Card" src="DARK_CARD_URL" width="100%" />
</picture>
```

## 3. Two-Column Profile Card Grid

```html
<div align="center">
  <table>
    <tr>
      <td align="center" width="50%">
        <img src="LEFT_CARD_URL" alt="Left Card" width="98%" />
      </td>
      <td align="center" width="50%">
        <img src="RIGHT_CARD_URL" alt="Right Card" width="98%" />
      </td>
    </tr>
  </table>
</div>
```

## 4. Recommended Theme & Variant Pairings

- **Warm Studio Default**: `gitlytics-dark` / `gitlytics-light` with `variant="clay"` and `shape="squircle"`.
- **Developer Dark Classic**: `tokyonight`, `dracula`, `catppuccin-mocha`, or `nord` with `variant="bento"` or `variant="flat"`.
- **Crisp Technical / Docs**: `scientific-lab` or `professional-ivory` with `variant="professional"` and `shape="rounded"`.
- **High-Energy / Terminal**: `synthwave84` or `cyberpunk-2077` with `variant="terminal"` or `variant="neobrutal"`.
