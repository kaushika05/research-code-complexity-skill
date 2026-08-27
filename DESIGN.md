# Design

## Product boundary

Research Code Complexity remains a cyclomatic-complexity skill. Reproducibility, provenance, statistics, data governance, and publication traceability appear only where they determine whether a hotspot may be safely changed and how the change can be checked.

The central design decision is to separate **measurement** from **action**. Cyclomatic complexity ranks control-flow hotspots; artifact role, lifecycle, scientific contract, mutation policy, and available evidence determine whether the result should be refactored, characterized, documented, wrapped, deferred, left alone, or excluded. This removes the upstream absolute `15+: must split` rule without discarding its useful measure-first workflow.

## Architecture

The portable entrypoint is `skills/research-code-complexity/SKILL.md`. It contains mode selection, safety invariants, the shared workflow, required decision outcomes, and report requirements. Conditional detail is one link away:

- `references/artifact-roles.md`: classification and lifecycle.
- `references/measurement-tools.md`: analyzer selection and counting limits.
- `references/scientific-verification.md`: verification by behavior class.
- `references/configuration.md`: layered profiles and merge rules.
- `references/domain-overlays.md`: evidence-triggered domain questions.

Assets hold the report and profile templates/schema. The validator is a deterministic development helper, and `evals/` is development-time evidence rather than runtime instruction. This matches the [Agent Skills specification](https://agentskills.io/specification): required frontmatter, a matching directory/name, a sub-500-line entrypoint, relative resource links, and progressive disclosure. The eval definitions follow the current non-normative [Agent Skills evaluation guide](https://agentskills.io/skill-creation/evaluating-skills), including prompts, expected outcomes, fixtures, and observable assertions.

Claude-specific packaging is isolated in `.claude-plugin/`. Current [Claude plugin documentation](https://code.claude.com/docs/en/plugins) and the [plugin reference](https://code.claude.com/docs/en/plugins-reference) make `plugin.json` the plugin identity. Version `0.1.0` is authoritative there; the marketplace entry intentionally omits a duplicate plugin version because `plugin.json` wins version resolution. The repository-root marketplace uses the documented relative `./` source and installation flow from the [marketplace guide](https://code.claude.com/docs/en/plugin-marketplaces).

## Modes and authority

Audit and Plan are read-only. Refactor requires an explicit modification request; automatic skill activation is not authorization. A narrow user request remains narrow, and full-repository scans are opt-in. These rules prevent a broad skill description from causing unintended code or data changes.

Published snapshots, raw data, generated code, and vendored code have distinct default postures. Configuration can tighten protection, but a lower-precedence profile cannot loosen an explicit current instruction. The precedence order is explicit request, local override, shared profile, user defaults, then evidence-based inference.

## Profiles

The schema requires only `schema_version`. Ordinary unknown keys fail so typos are actionable, while `x-...` keys create a visible extension path. Lists replace rather than silently concatenate across precedence layers because ordering, exclusions, and seed lists may be semantically meaningful. Artifact entries can express `allow`, `characterize-first`, `wrap-only`, `frozen`, or `exclude` mutation policies.

Numerical tolerances and equivalence margins accept `null`; the templates do not provide generic values. A value without meaningful provenance remains an unresolved contract field, not permission for the agent to choose one.

## Scientific behavior

The contract-first workflow translates established research-software principles into refactoring decisions:

- The [FAIR Principles for Research Software](https://doi.org/10.1038/s41597-022-01710-x) motivate explicit identifiers, provenance, accessible metadata, dependencies, and reusable conditions, but the skill does not claim that refactoring makes a repository FAIR.
- [Best Practices for Scientific Computing](https://doi.org/10.1371/journal.pbio.1001745) and [Good Enough Practices in Scientific Computing](https://doi.org/10.1371/journal.pcbi.1005510) support small testable changes, automation, version control, clear data handling, and reproducible workflows.
- The [Ten Simple Rules for Reproducible Computational Research](https://doi.org/10.1371/journal.pcbi.1003285) support preserving inputs, intermediate results, parameters, seeds, and the route from data to result.
- [Citation File Format](https://citation-file-format.github.io/) supplies machine-readable release citation metadata; this project uses CFF 1.2.0 without inventing a DOI, ORCID, or affiliation.

The skill turns those sources into bounded behavior: establish contracts before editing, preserve raw and frozen artifacts, record unavailable reproduction, and avoid claiming that tests prove scientific correctness.

## Measurement choices

Language support is documented only where current tool or vendor documentation confirms a viable approach. The primary sources are:

- Python and notebooks: [Radon command-line documentation](https://radon.readthedocs.io/en/latest/commandline.html).
- R: [CRAN `cyclocomp`](https://cran.r-project.org/web/packages/cyclocomp/index.html).
- JavaScript/TypeScript: [ESLint `complexity`](https://eslint.org/docs/latest/rules/complexity).
- Go: [`gocyclo`](https://github.com/fzipp/gocyclo).
- C/C++ and Fortran fallback: [Lizard](https://github.com/terryyin/lizard).
- Rust parser-based metrics: [`rust-code-analysis`](https://mozilla.github.io/rust-code-analysis/).
- Java: [PMD `CyclomaticComplexity`](https://docs.pmd-code.org/latest/pmd_rules_java_design.html#cyclomaticcomplexity).
- Julia: [`CodeComplexity.jl`](https://github.com/charleskawczynski/CodeComplexity.jl), identified as young tooling and subject to explicit parser/version caveats.
- MATLAB: MathWorks [`checkcode`](https://www.mathworks.com/help/matlab/ref/checkcode.html), including classic and modified cyclomatic options.
- Shell: [`ShellMetrics`](https://github.com/shellspec/shellmetrics); ShellCheck is lint evidence, not a CC analyzer.

The skill prefers repository-configured tools, versions, and thresholds. It records analyzer semantics and avoids cross-tool comparison. A manual, per-unit convention is an explicit fallback rather than a fabricated tool result.

## Verification strength

Deterministic discrete behavior uses exact comparisons after excluding named nondeterministic metadata. Numerical behavior uses project- or domain-sourced tolerances plus invariants and environment records. Stochastic behavior combines fixed-seed characterization with preselected multi-seed metrics when feasible. Statistical equivalence requires a justified margin; non-significance alone is not evidence. Notebook and figure checks prioritize execution order, source data, transformation semantics, labels, units, and aggregation over saved metadata or pixels.

Tests remain evidence about a contract, not proof of scientific validity. When contract evidence is weak and risk is high, the intended result is characterization, wrapping, documentation, deferral, or leaving the code unchanged.

## Licensing and attribution

The complete upstream Apache-2.0 license is retained. The replaced upstream skill and substantially rewritten README/marketplace are marked through file notices and `UPSTREAM.md`, which records commit `567886f485063c5f5f94503d5712ef75cbcbbd94`, retained ideas, and modifications. The upstream project had no `NOTICE` file at that commit, so none was fabricated.
