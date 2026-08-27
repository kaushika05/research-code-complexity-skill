---
name: research-code-complexity
description: Audits and refactors scientific research code to reduce accidental control-flow complexity while preserving scientific intent, numerical behavior, stochastic validity, provenance, reproducibility, and manuscript traceability. Use for computational research repositories, notebooks, analysis scripts, simulations, ML experiments, data pipelines, reference implementations, or publication code when reviewing, simplifying, hardening, or measuring complexity.
license: Apache-2.0
metadata:
  author: Kay Wijerathne
---

# Research Code Complexity

Reduce accidental complexity without erasing scientific intent. Cyclomatic complexity is the primary quantitative signal, not an instruction to rewrite every high-scoring function.

## Choose the mode and scope

Infer the narrowest mode authorized by the request:

- **Audit:** read, measure, classify, and recommend. Do not edit repository files.
- **Plan:** audit, order proposed changes, and define verification. Do not edit code unless separately requested.
- **Refactor:** the user explicitly requested modification, cleanup, simplification, hardening, or another code change. Establish a baseline, edit incrementally, verify, and re-measure.

Automatic activation never authorizes Refactor mode. Scan an entire repository only when the user explicitly requests repository-wide scope; otherwise limit work to the named file, function, notebook cells, subsystem, or diff.

## Load only relevant guidance

- Read [references/configuration.md](references/configuration.md) when any profile exists or the user asks to tailor behavior.
- Read [references/artifact-roles.md](references/artifact-roles.md) when artifact role or project lifecycle is uncertain, or before interpreting a hotspot in generated, vendored, raw, frozen, or manuscript-linked material.
- Read [references/measurement-tools.md](references/measurement-tools.md) before selecting an analyzer for an unfamiliar language or comparing analyzer results.
- Read [references/scientific-verification.md](references/scientific-verification.md) before changing numerical, stochastic, statistical, machine-learning, notebook, figure, table, published, or archived artifacts.
- Read only the relevant section of [references/domain-overlays.md](references/domain-overlays.md) after repository evidence identifies a domain.

Do not treat these overlays as a substitute for a qualified domain researcher.

## Resolve the profile

Apply configuration in this order, with earlier sources winning:

1. Explicit instructions in the current request.
2. `.research-code-complexity.local.yaml`.
3. `.research-code-complexity.yaml`.
4. `~/.config/research-code-complexity/config.yaml`.
5. Repository evidence and conservative inferred defaults.

Never let a lower-precedence value silently override an explicit instruction. Record which sources were present, which values won, and any merge ambiguity. A local profile should normally be gitignored. Validate profiles with `scripts/validate_profile.py`; if its development dependencies are unavailable, inspect the YAML and schema transparently rather than altering the research environment.

## Establish context before counting

1. Inspect scoped READMEs, configuration, entrypoints, imports, comments, manuscript links, tests, and relevant history.
2. Infer lifecycle: exploratory, active research, collaborative internal research, pre-publication, published, archived, or reusable community software. If evidence is insufficient, say `uncertain` and use conservative defaults.
3. Classify each scoped artifact by role. Do not use directory names alone.
4. Identify protected content: raw data, generated or vendored code, frozen outputs, archived snapshots, published reproduction paths, and files with a restrictive mutation policy.

Exclude generated, vendored, and raw artifacts unless explicitly targeted. Never modify raw data during complexity refactoring. Treat canonical published code as frozen unless the user authorizes a new version.

## Distinguish two kinds of complexity

**Essential scientific complexity** expresses a model, equation, experimental design, inclusion rule, boundary condition, solver, statistic, protocol, or literal reference implementation. It may warrant names, annotations, characterization, a wrapper, or no change.

**Accidental implementation complexity** comes from orchestration, repeated validation or transformations, hidden mutable state, manual experiment switches, Boolean-flag combinations, configuration embedded in code, mixed I/O/modeling/analysis/presentation, notebook execution order, or repeated path/seed/split handling. Reduce this first.

Never collapse these judgments into a single research-quality score. Report cyclomatic complexity, scientific risk, verification strength, and secondary observations separately.

## Measure before recommending

1. Prefer the repository's configured analyzer and threshold.
2. Run the analyzer without mutating the project's research environment. Prefer an existing executable or isolated temporary environment.
3. Record tool name, version, command, exclusions, threshold, and counting variant.
4. Measure per function or equivalent executable unit. For notebooks, distinguish functions in cells, top-level cell flow, and hidden cross-cell state.
5. Rank hotspots, but order recommendations by both complexity and scientific risk.

Analyzers count Boolean operators, exceptions, pattern matching, comprehensions, defaults, and other constructs differently. Do not compare values from different analyzers as equivalent. If no verified analyzer is available, count manually and state the convention, for example `1 + if/elseif/case/loop/catch/ternary/short-circuit decision`.

Use numerical ranges only as triage guidance. A high value means investigate with priority; it never means split regardless of role. Track nesting, hidden state, flag proliferation, dataflow opacity, configuration scattering, cognitive complexity, or coupling separately when evidence supports them.

## Establish the scientific contract before editing

For every scientifically relevant hotspot, identify as much as repository evidence permits:

- Inputs, accepted ranges, outputs, schemas, file names, and downstream interfaces.
- Units, coordinates, dtypes, precision, devices, memory layout, missing-value behavior, and operation order.
- Dataset identities and versions; split and sample IDs; inclusion and exclusion criteria; preprocessing fit boundaries.
- RNG family, seed derivation, sampling order, trial assignment, and parallel-worker behavior.
- Solver, optimizer, tolerance, stopping, checkpoint, resume, and performance constraints.
- Invariants, conservation laws, expected aggregates, and figure/table/equation/protocol/manuscript mappings.

Tests are contract evidence, not proof of scientific correctness. If the contract is unclear and risk is high, do not make an aggressive refactor; characterize, document, wrap, or request domain review first.

## Decide explicitly for each hotspot

Use exactly one primary outcome, with evidence:

- Refactor now
- Refactor after characterization
- Document or annotate
- Wrap without changing the core
- Defer because scientific review is required
- Leave as-is
- Exclude as generated, vendored, raw, or out of scope

Prefer separating orchestration from scientific transformations, guard clauses for non-scientific validation, domain-named predicates, pure transformations where practical, explicit versioned configuration, clear I/O/model/analysis boundaries, and adapters around frozen code. Preserve equation and manuscript mappings.

Do not add architecture for its own sake, scatter a clear equation across helpers to lower a number, hide branches in expressions or metaprogramming, or change randomness, units, dtypes, splits, schemas, file names, APIs, or operation order accidentally.

## Refactor incrementally

In Refactor mode:

1. Save baseline analyzer results and run applicable baseline commands.
2. Add characterization first when tests do not cover the scientific contract.
3. Change one coherent hotspot at a time.
4. Run the strongest affordable check after each material change.
5. Re-measure with the same analyzer and settings.
6. Review the diff for accidental contract changes and revert unsafe changes.

Do not delete prior experiments or overwrite frozen artifacts merely because code appears duplicated.

## Verify at the right strength

Use exact comparisons for deterministic discrete behavior. For floating-point work, use tolerances only from project tests, configuration, domain documentation, or an explicitly justified baseline; also check invariants. For stochastic work, use fixed-seed characterization and, when feasible, multi-seed checks of selected metrics or distributions. Preserve statistical formulas and never treat `p > 0.05` as equivalence. For ML, protect split identity, leakage boundaries, metric definitions, evaluation mode, checkpoints, device, and precision.

Restart and run notebooks top to bottom when data and environment permit. For figures and tables, compare source data, transforms, categories, axes, units, and aggregation rules; pixel equality is usually insufficient. Benchmark performance-sensitive kernels before and after.

State exactly what was not rerun. A smoke test is not a full experiment, and a passing test suite does not guarantee scientific validity.

## Report

Use [assets/research-complexity-report.md](assets/research-complexity-report.md) as a starting structure, removing irrelevant empty sections but never omitting uncertainty or checks not run. Include:

- Mode, scope, profile source, lifecycle, analyzer/version, and baseline commands.
- Scientific contract and protected artifacts.
- A hotspot table with artifact role, location, CC before/after, scientific risk, decision, and evidence.
- Changes made or proposed.
- Exact, numerical, stochastic, notebook/reproduction, performance, and test evidence as applicable.
- Remaining risks and a reproduction command, or why one could not be established.

Do not claim behavior, numerical, statistical, or scientific equivalence beyond the checks actually run.

> This skill is a substantial research-aware adaptation of Saurabh Kumar's Apache-2.0 `cyclomatic-complexity` skill. It retains measure-first, incremental refactoring, re-measurement, and anti-metric-gaming principles while changing the decision model and verification requirements.
