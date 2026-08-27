# Research Code Complexity v0.1.0

Research Code Complexity adapts Saurabh Kumar's cyclomatic-complexity skill for scientific repositories. It reduces accidental control-flow complexity while protecting scientific intent, numerical and stochastic behavior, provenance, reproducibility evidence, and manuscript traceability.

## Highlights

- Audit, plan, and explicitly authorized refactor modes.
- Essential-versus-accidental complexity classification with seven evidence-backed decisions, including **Leave as-is**.
- Scientific contracts and verification guidance for deterministic, numerical, stochastic, statistical, ML, notebook, figure/table, and published artifacts.
- Layered user/shared/local YAML profiles, JSON Schema, validator, examples, and tests.
- Verified complexity-tool guidance across Python, R, JavaScript/TypeScript, Go, C/C++, Rust, Java, Julia, MATLAB, Fortran, Shell, and Jupyter.
- Fourteen decision-focused eval definitions and fixtures.
- Portable Agent Skill plus Claude Code plugin and marketplace packaging.

## Install in Claude Code

```text
/plugin marketplace add kaushika05/research-code-complexity-skill
/plugin install research-code-complexity@research-code-complexity-skill
```

The release asset `research-code-complexity-0.1.0.zip` contains the complete portable skill directory. Verify it with the accompanying SHA-256 checksum file before unpacking.

## Known limitations

- Complexity scores from different analyzers are not interchangeable.
- Static analysis and tests do not establish scientific correctness or reproducibility.
- Some notebook, MATLAB, full-experiment, restricted-data, GPU, or HPC checks require environments not bundled with the skill.
- Julia cyclomatic-complexity tooling is comparatively young and requires explicit version/parser caveats.
- Public CI runs static and deterministic checks only; it does not make paid model calls.

## Attribution

This project is a substantial Apache-2.0 fork of Saurabh Kumar's [cyclomatic-complexity-skill](https://github.com/saurabhkumar8112/cyclomatic-complexity-skill) at commit `567886f485063c5f5f94503d5712ef75cbcbbd94`. It retains the upstream measure-first, incremental, re-measure, and anti-metric-gaming principles. The upstream author has not endorsed this fork.
