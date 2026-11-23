# Security Policy

## Credential Safety

- **Never commit** `glt_live_...` Gitlytics API keys, GitHub Personal Access Tokens (`ghp_...` / `github_pat_...`), or `.env` files to this repository.
- Always pass credentials through environment variables (`GITLYTICS_API_KEY` for Cloud MCP, `GITLYTICS_TOKEN` for local stdio MCP) rather than hardcoding secrets in `mcp_config.json` or pasting them into chat.
- Gitlytics Cloud stores only SHA-256 hashes of `glt_live_...` API keys. If a key is ever exposed, revoke it immediately at https://dashboard.gitlytics.dev/integrations.

## Reporting a Vulnerability

If you discover a security issue in the Gitlytics MCP server, skills, or plugin bundle, please report it privately to **contact@gitlytics.dev** with reproduction steps. Do not open public issues for unpatched security vulnerabilities.
