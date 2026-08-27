#!/usr/bin/env python3
"""Validate research-code-complexity YAML profiles against the bundled schema."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

try:
    import yaml
    from jsonschema import Draft202012Validator
except ImportError as exc:  # pragma: no cover - exercised in dependency-free use
    print(
        "Missing development dependency. Install requirements-dev.txt in an "
        f"isolated environment ({exc.name}).",
        file=sys.stderr,
    )
    raise SystemExit(2) from exc


DEFAULT_SCHEMA = Path(__file__).resolve().parents[1] / "assets" / "research-code-complexity.schema.json"


def format_path(parts: list[Any]) -> str:
    result = "$"
    for part in parts:
        if isinstance(part, int):
            result += f"[{part}]"
        elif str(part).isidentifier():
            result += f".{part}"
        else:
            result += f"[{json.dumps(str(part))}]"
    return result


def load_yaml(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def load_schema(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        schema = json.load(handle)
    Draft202012Validator.check_schema(schema)
    return schema


def validate_profile(path: Path, schema: dict[str, Any]) -> list[str]:
    try:
        document = load_yaml(path)
    except FileNotFoundError:
        return [f"{path}: file not found"]
    except OSError as exc:
        return [f"{path}: cannot read file: {exc}"]
    except yaml.YAMLError as exc:
        mark = getattr(exc, "problem_mark", None)
        location = f" line {mark.line + 1}, column {mark.column + 1}" if mark else ""
        return [f"{path}:{location}: invalid YAML: {exc}"]

    validator = Draft202012Validator(schema)
    errors = sorted(validator.iter_errors(document), key=lambda item: list(item.absolute_path))
    return [f"{path}:{format_path(list(error.absolute_path))}: {error.message}" for error in errors]


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("profiles", nargs="+", type=Path, help="YAML profile(s) to validate")
    parser.add_argument("--schema", type=Path, default=DEFAULT_SCHEMA, help="JSON Schema path")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        schema = load_schema(args.schema)
    except (FileNotFoundError, OSError, json.JSONDecodeError) as exc:
        print(f"Cannot load schema {args.schema}: {exc}", file=sys.stderr)
        return 2
    except Exception as exc:  # jsonschema raises several schema-specific subclasses
        print(f"Invalid schema {args.schema}: {exc}", file=sys.stderr)
        return 2

    failures = 0
    for profile in args.profiles:
        errors = validate_profile(profile, schema)
        if errors:
            failures += 1
            for error in errors:
                print(error, file=sys.stderr)
        else:
            print(f"OK: {profile}")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
