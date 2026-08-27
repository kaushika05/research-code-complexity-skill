#!/usr/bin/env python3
"""Validate release-critical repository structure without network access."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "research-code-complexity"
LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
VERSION_RE = re.compile(r"^## \[([^]]+)\]", re.MULTILINE)


def fail(message: str, failures: list[str]) -> None:
    failures.append(message)


def check_json_and_yaml(failures: list[str]) -> None:
    for path in ROOT.rglob("*.json"):
        if ".git" not in path.parts:
            try:
                json.loads(path.read_text(encoding="utf-8"))
            except (OSError, json.JSONDecodeError) as exc:
                fail(f"Invalid JSON {path.relative_to(ROOT)}: {exc}", failures)
    for pattern in ("*.yaml", "*.yml", "*.cff"):
        for path in ROOT.rglob(pattern):
            if ".git" not in path.parts:
                try:
                    yaml.safe_load(path.read_text(encoding="utf-8"))
                except (OSError, yaml.YAMLError) as exc:
                    fail(f"Invalid YAML {path.relative_to(ROOT)}: {exc}", failures)


def check_skill(failures: list[str]) -> None:
    entrypoint = SKILL / "SKILL.md"
    text = entrypoint.read_text(encoding="utf-8")
    if len(text.splitlines()) >= 500:
        fail("SKILL.md must remain below 500 lines", failures)
    if not text.startswith("---\n"):
        fail("SKILL.md is missing YAML frontmatter", failures)
        return
    _, frontmatter, _ = text.split("---", 2)
    metadata = yaml.safe_load(frontmatter)
    if metadata.get("name") != SKILL.name:
        fail("SKILL.md name must match its directory", failures)
    if metadata.get("license") != "Apache-2.0":
        fail("SKILL.md license must be Apache-2.0", failures)


def check_evals(failures: list[str]) -> None:
    path = SKILL / "evals" / "evals.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    evals = data.get("evals", [])
    if data.get("skill_name") != SKILL.name:
        fail("evals.json skill_name mismatch", failures)
    if len(evals) != 14:
        fail(f"Expected 14 evals, found {len(evals)}", failures)
    for case in evals:
        case_id = case.get("id", "unknown")
        for key in ("prompt", "expected_output", "assertions"):
            if not case.get(key):
                fail(f"Eval {case_id} is missing {key}", failures)
        for fixture in case.get("files", []):
            if not (SKILL / fixture).is_file():
                fail(f"Eval {case_id} fixture does not exist: {fixture}", failures)


def check_metadata(failures: list[str]) -> None:
    plugin = json.loads((ROOT / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))
    market = json.loads((ROOT / ".claude-plugin" / "marketplace.json").read_text(encoding="utf-8"))
    cff = yaml.safe_load((ROOT / "CITATION.cff").read_text(encoding="utf-8"))
    changelog = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
    match = VERSION_RE.search(changelog)
    versions = {str(plugin.get("version")), str(cff.get("version")), match.group(1) if match else "missing"}
    if versions != {"0.1.0"}:
        fail(f"Release versions disagree: {sorted(versions)}", failures)
    if market.get("plugins", [{}])[0].get("version") is not None:
        fail("Marketplace must not duplicate the authoritative plugin version", failures)
    if plugin.get("name") != SKILL.name or market.get("plugins", [{}])[0].get("name") != SKILL.name:
        fail("Plugin, marketplace, and skill names must agree", failures)
    for path in (ROOT / ".claude-plugin" / "plugin.json", ROOT / ".claude-plugin" / "marketplace.json", ROOT / "CITATION.cff", ROOT / "UPSTREAM.md"):
        text = path.read_text(encoding="utf-8")
        if re.search(r"\b(TODO|TBD|CHANGEME|YOUR[-_ ]NAME)\b", text, re.IGNORECASE):
            fail(f"Release-critical placeholder in {path.relative_to(ROOT)}", failures)


def check_markdown_links(failures: list[str]) -> None:
    for path in ROOT.rglob("*.md"):
        if ".git" in path.parts:
            continue
        text = path.read_text(encoding="utf-8")
        for raw_target in LINK_RE.findall(text):
            target = raw_target.strip().split(maxsplit=1)[0].strip("<>")
            if not target or target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            file_part = target.split("#", 1)[0]
            if file_part and not (path.parent / file_part).resolve().exists():
                fail(f"Broken link in {path.relative_to(ROOT)}: {target}", failures)


def main() -> int:
    failures: list[str] = []
    check_json_and_yaml(failures)
    check_skill(failures)
    check_evals(failures)
    check_metadata(failures)
    check_markdown_links(failures)
    if failures:
        for message in failures:
            print(f"ERROR: {message}")
        return 1
    print("OK: repository structure, metadata, eval fixtures, syntax, and internal links")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
