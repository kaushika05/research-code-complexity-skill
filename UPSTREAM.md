# Upstream provenance

- Original project: `cyclomatic-complexity-skill`
- Original repository: https://github.com/saurabhkumar8112/cyclomatic-complexity-skill
- Original author: Saurabh Kumar
- Upstream commit: `567886f485063c5f5f94503d5712ef75cbcbbd94`
- Date forked: 2026-08-27
- Upstream license: Apache License 2.0

## Retained ideas

This fork retains the upstream project's useful complexity-first core: measure before editing, prefer a real analyzer, respect repository configuration, rank per-function hotspots, refactor incrementally, re-measure with the same tool, report before/after evidence, preserve behavior and public interfaces, and refuse to hide branches in clever expressions or inappropriate abstractions.

## Substantial modifications

The upstream `skills/cyclomatic-complexity/SKILL.md`, root `README.md`, and marketplace manifest were substantially changed or replaced. This fork adds a research-aware decision model; audit, plan, and refactor modes; artifact/lifecycle classification; scientific-contract discovery; deterministic, numerical, stochastic, statistical, ML, notebook, and publication verification; layered profiles with schema validation; verified language tooling guidance; domain overlays; evals and fixtures; tests and CI; plugin metadata; citation and contribution files; release packaging; and social assets.

The absolute upstream rule `15+: must split, no debate` is not retained. High complexity is a triage signal whose recommended action depends on artifact role, scientific risk, and available verification.

No upstream `NOTICE` file existed at the recorded commit, so this fork does not invent one. Attribution here and in the README does not imply upstream endorsement.
