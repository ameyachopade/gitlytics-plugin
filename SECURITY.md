# Security Policy - Gitlytics Agent Plugin & Skills

This repository is part of the **Gitlytics Ecosystem** and distributes the official Antigravity plugin, MCP configurations, and 4 Vercel Agent Skills (`npx skills add ameyachopade/gitlytics-plugin -g`).

## Supported Versions

| Version | Supported |
| :--- | :--- |
| `0.9.x` (latest) | Yes |
| `< 0.9.0` | No |

## Security Controls & Credential Safety

- **Zero-Auth Public Tools**: All 5 public widget, badge, tech-logo, and star-history tools on `https://api.gitlytics.dev/mcp` require zero credentials.
- **OAuth 2.1 + PKCE Primary Auth**: `mcp_config.json` connects directly to `https://api.gitlytics.dev/mcp` without embedded secrets; private workspace tools trigger standard OAuth 2.1 + PKCE browser sign-in in supported IDEs.
- **No Hardcoded Secrets**: Never commit `glt_live_...` API keys, OAuth tokens, GitHub Personal Access Tokens (`ghp_...` / `github_pat_...`), or `.env` files. For headless CI/CD fallback or local stdio (`gitlytics mcp`), always pass `GITLYTICS_API_KEY` or `GITLYTICS_TOKEN` via process environment variables.
- **Instant Revocation**: If a `glt_live_...` API key or OAuth session is ever exposed, revoke it immediately at https://dashboard.gitlytics.dev/integrations.
- **Prompt & Tool Guardrails**: `rules/AGENTS.md` enforces catalog discovery before generating embeds and explicitly forbids asking users to paste raw GitHub PATs into chat.

## Reporting a Vulnerability

**Do not open a public GitHub issue for security vulnerabilities.**

Please report vulnerabilities privately using either:
1. GitHub's **Private Vulnerability Reporting** (**Security** tab -> **Advisories** -> **Report a vulnerability**).
2. Email **contact@gitlytics.dev** (or **ameyasanjaychopade@gmail.com**) with `[SECURITY]` in the subject line.

Please include:
- **Affected File or Skill** (e.g. `mcp_config.json`, `rules/AGENTS.md`, or a specific `skills/<name>/`)
- **Impact & Detailed Description**
- **Steps to Reproduce**

## Response SLA

1. **Acknowledgment**: Within 72 hours.
2. **Triage & Investigation**: Severity assessment and root-cause analysis.
3. **Fix & Advisory**: Coordinated patch release and credit (if desired).
