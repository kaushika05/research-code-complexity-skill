#!/usr/bin/env python3
"""Validate CITATION.cff against a caller-supplied official CFF schema."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import yaml
from jsonschema import Draft7Validator


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("cff", type=Path)
    parser.add_argument("schema", type=Path)
    args = parser.parse_args()

    # BaseLoader keeps ISO dates as JSON strings instead of Python date objects.
    document = yaml.load(args.cff.read_text(encoding="utf-8"), Loader=yaml.BaseLoader)
    schema = json.loads(args.schema.read_text(encoding="utf-8"))
    errors = sorted(Draft7Validator(schema).iter_errors(document), key=lambda error: list(error.path))
    if errors:
        for error in errors:
            path = ".".join(str(part) for part in error.path) or "$"
            print(f"{args.cff}:{path}: {error.message}")
        return 1
    print(f"OK: {args.cff}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
