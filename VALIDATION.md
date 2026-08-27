# Validation record for v0.1.0

Validation date: 2026-08-27
Local platform: Windows, Python 3.14.2, Claude Code 2.0.76

## Passed locally

- `python -m unittest discover -s tests -v`: 7 tests passed. Coverage includes valid, partial, invalid, malformed, and `x-` extension profiles plus release repository consistency.
- `python scripts/validate_repository.py`: JSON/YAML syntax, release metadata consistency, 14 eval definitions/fixtures, `SKILL.md` limits, and internal Markdown links passed.
- `skills-ref validate skills/research-code-complexity`: passed using `skills-ref` 0.1.0 installed from Agent Skills commit `69ef37e9424c0a7ea9dd2293b559e43ec8176379`.
- Profile validation: both bundled templates, four domain examples, and two eval precedence profiles passed the bundled 2020-12 JSON Schema.
- `CITATION.cff`: passed against the official schema pinned at Citation File Format commit `0c5b4aa07071490eaf261775ce96ccdd13a6e2d5`.
- `claude plugin validate .`: marketplace manifest passed.
- `claude plugin validate .claude-plugin/plugin.json`: plugin manifest passed.
- Social card: rendered from repository SVG to a 1280×640 PNG and visually reviewed for legibility, contrast, clipping, and content.

## Attempted but unavailable or inapplicable

- `claude plugin validate ./skills`: attempted as requested and failed because `skills/` is a portable Agent Skills container with no `.claude-plugin` manifest. The portable skill itself passed the official `skills-ref` validator. This is a command/scope mismatch, not a hidden green result.
- Representative with-skill/without-skill model evals: the environment supports non-interactive runs and a first with-skill call was attempted. It returned `Credit balance is too low` before any model tokens or tool use (`total_cost_usd: 0`). No model-based eval result is claimed. All 14 eval definitions remain available for a funded clean-context run.
- Scientific analyzers and workloads: no target research repository is part of this product release, so no Radon/R/ML/notebook/HPC workload was fabricated.
- GitHub Actions, public installation, release download, tag, and asset verification are recorded in the release/PR checks and final handoff after publication.
