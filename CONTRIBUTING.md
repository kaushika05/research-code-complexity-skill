# Contributing

Contributions should keep the project complexity-first and preserve the distinction between essential scientific complexity and accidental implementation complexity. Do not add universal refactor mandates, arbitrary tolerances or equivalence margins, unsupported analyzer claims, domain personas, or guarantees of scientific correctness or reproducibility.

## Development setup

Use an isolated Python environment; normal skill use does not require these dependencies.

```bash
python -m venv .venv
# Windows
.venv\Scripts\python -m pip install -r requirements-dev.txt
# POSIX
.venv/bin/python -m pip install -r requirements-dev.txt
```

## Validation

Run the checks available in your environment:

```bash
python -m unittest discover -s tests -v
python skills/research-code-complexity/scripts/validate_profile.py \
  skills/research-code-complexity/assets/research-code-complexity.example.yaml \
  skills/research-code-complexity/assets/research-code-complexity.local.example.yaml \
  examples/profiles/*.yaml
python scripts/validate_repository.py
skills-ref validate skills/research-code-complexity
claude plugin validate .
git diff --check
```

On PowerShell, enumerate example paths rather than relying on wildcard expansion for Python commands. Record any unavailable validator instead of replacing it with a green claim.

## Changes to guidance

Link primary or authoritative documentation for new analyzer support. Add a realistic eval that would fail without the change and assert observable decisions rather than exact prose. If scientific behavior might change, describe the contract, evidence, and limits in the pull request.

By contributing, you agree that your contribution is licensed under Apache-2.0 as described in [LICENSE](LICENSE).
