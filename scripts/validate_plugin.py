"""Offline validator for gitlytics-plugin (Antigravity Plugin + Vercel npx skills)."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

PLUGIN_ROOT = Path(__file__).resolve().parents[1]

ALLOWED_PLUGIN_KEYS = {
    "name",
    "displayName",
    "version",
    "description",
    "logo",
    "author",
    "homepage",
    "repository",
    "suggestedPrompts",
    "disabled",
}
ALLOWED_LOGO_SUFFIXES = {".png", ".svg", ".jpg", ".jpeg", ".webp"}
KEBAB_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def _fail(errors: list[str], msg: str) -> None:
    errors.append(msg)


def _parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n") and not text.startswith("---\r\n"):
        return {}
    lines = text.splitlines()
    end_idx = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end_idx = i
            break
    if end_idx is None:
        return {}
    fm: dict[str, str] = {}
    current_key: str | None = None
    for line in lines[1:end_idx]:
        if ":" in line and not line.startswith((" ", "\t")):
            key, _, val = line.partition(":")
            current_key = key.strip()
            fm[current_key] = val.strip()
        elif current_key is not None:
            fm[current_key] = (fm[current_key] + " " + line.strip()).strip()
    return fm


def validate() -> list[str]:
    errors: list[str] = []

    # 1. Validate plugin.json
    plugin_json_path = PLUGIN_ROOT / "plugin.json"
    if not plugin_json_path.exists():
        _fail(errors, "Missing plugin.json")
        return errors

    plugin_data = json.loads(plugin_json_path.read_text(encoding="utf-8"))
    unknown_keys = set(plugin_data.keys()) - ALLOWED_PLUGIN_KEYS
    if unknown_keys:
        _fail(errors, f"plugin.json contains unsupported top-level keys: {sorted(unknown_keys)}")

    name = str(plugin_data.get("name", ""))
    if not KEBAB_RE.match(name):
        _fail(errors, f"plugin.json name must be lowercase kebab-case, got {name!r}")

    prompts = plugin_data.get("suggestedPrompts", [])
    if not isinstance(prompts, list) or not (1 <= len(prompts) <= 3):
        _fail(errors, "plugin.json suggestedPrompts must contain 1 to 3 entries")

    logo_rel = plugin_data.get("logo")
    if logo_rel:
        if str(logo_rel).startswith(("http://", "https://", "/")):
            _fail(errors, f"plugin.json logo must be a relative path, got {logo_rel!r}")
        logo_path = PLUGIN_ROOT / str(logo_rel)
        if not logo_path.exists():
            _fail(errors, f"plugin.json logo target does not exist: {logo_path}")
        if logo_path.suffix.lower() not in ALLOWED_LOGO_SUFFIXES:
            _fail(errors, f"Unsupported logo extension: {logo_path.suffix}")

    # 2. Validate mcp_config.json and mcp_config.local.json
    for cfg_name in ("mcp_config.json", "mcp_config.local.json"):
        cfg_path = PLUGIN_ROOT / cfg_name
        if not cfg_path.exists():
            _fail(errors, f"Missing {cfg_name}")
            continue
        cfg_data = json.loads(cfg_path.read_text(encoding="utf-8"))
        servers = cfg_data.get("mcpServers")
        if not isinstance(servers, dict) or not servers:
            _fail(errors, f"{cfg_name} must define a non-empty mcpServers map")
            continue
        for srv_name, srv_cfg in servers.items():
            if not srv_name.startswith("gitlytics"):
                _fail(errors, f"{cfg_name} server '{srv_name}' must be prefixed with 'gitlytics'")
            if not isinstance(srv_cfg, dict) or ("url" not in srv_cfg and "command" not in srv_cfg):
                _fail(errors, f"{cfg_name} server '{srv_name}' must specify 'url' or 'command'")

    # 3. Validate rules/AGENTS.md (no YAML frontmatter)
    rules_path = PLUGIN_ROOT / "rules" / "AGENTS.md"
    if not rules_path.exists():
        _fail(errors, "Missing rules/AGENTS.md")
    else:
        rules_text = rules_path.read_text(encoding="utf-8")
        if rules_text.startswith("---"):
            _fail(errors, "rules/AGENTS.md must not include YAML frontmatter")

    # 4. Validate skills/* for Antigravity + Vercel npx skills (skills.sh)
    skills_dir = PLUGIN_ROOT / "skills"
    if not skills_dir.is_dir():
        _fail(errors, "Missing skills/ directory")
    else:
        skill_dirs = [p for p in sorted(skills_dir.iterdir()) if p.is_dir()]
        if not skill_dirs:
            _fail(errors, "skills/ contains no skill subdirectories")
        for sdir in skill_dirs:
            skill_md = sdir / "SKILL.md"
            if not skill_md.exists():
                _fail(errors, f"Missing SKILL.md in {sdir}")
                continue
            text = skill_md.read_text(encoding="utf-8")
            line_count = len(text.splitlines())
            if line_count >= 500:
                _fail(errors, f"{skill_md} has {line_count} lines (must be < 500)")
            fm = _parse_frontmatter(text)
            if fm.get("name") != sdir.name:
                _fail(errors, f"{skill_md} frontmatter name {fm.get('name')!r} must match folder {sdir.name!r}")
            if not fm.get("description"):
                _fail(errors, f"{skill_md} frontmatter is missing description")

            # Verify relative markdown reference links exist
            for match in re.finditer(r"\[[^\]]+\]\((references/[^)]+)\)", text):
                ref_target = sdir / match.group(1)
                if not ref_target.exists():
                    _fail(errors, f"{skill_md} broken reference link: {match.group(1)}")

            evals_path = sdir / "evals" / "evals.json"
            if not evals_path.exists():
                _fail(errors, f"Missing evals/evals.json in {sdir}")
            else:
                evals_data = json.loads(evals_path.read_text(encoding="utf-8"))
                if evals_data.get("skill_name") != sdir.name:
                    _fail(errors, f"{evals_path} skill_name mismatch")
                if not evals_data.get("evals"):
                    _fail(errors, f"{evals_path} has no evals")

    # 5. Enforce zero em/en dashes across all text files in gitlytics-plugin/
    for path in PLUGIN_ROOT.rglob("*"):
        if not path.is_file() or path.suffix.lower() in ALLOWED_LOGO_SUFFIXES:
            continue
        content = path.read_text(encoding="utf-8", errors="ignore")
        if "\u2013" in content or "\u2014" in content:
            _fail(errors, f"Em or en dash found in {path.relative_to(PLUGIN_ROOT)}")

    return errors


if __name__ == "__main__":
    found_errors = validate()
    if found_errors:
        for err in found_errors:
            print(f"FAIL: {err}", file=sys.stderr)
        sys.exit(1)
    print("PASS: All plugin and npx skills validation checks succeeded.")
