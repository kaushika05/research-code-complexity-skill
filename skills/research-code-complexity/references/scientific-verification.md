# Scientific verification

Read this reference before changing numerical, stochastic, statistical, machine-learning, notebook, figure/table, published, or archived artifacts.

## Match evidence to behavior

| Behavior | Preferred evidence | Common overclaim to avoid |
|---|---|---|
| Deterministic discrete | Exact values, schemas, row/sample IDs, serialization, CLI output and exit codes | Declaring all output unverifiable because timestamps differ |
| Floating point | Project-sourced tolerances, invariant checks, environment record, sensitivity and performance checks | Inventing a tolerance after observing a failure |
| Stochastic | Fixed-seed characterization plus multi-seed metrics/distributions when feasible | Calling one visually similar run equivalent |
| Statistical analysis | Formula, coding, grouping, weights, missingness, corrections, estimates, intervals, sample sizes | Treating non-significance as proof of equivalence |
| Machine learning | Split/sample identity, leakage checks, preprocessing fit boundary, seeds, metrics, modes, checkpoints, device/precision | Calling a smoke run a reproduced training result |
| Notebook | Restart-and-run-all, defined-cell checks, hidden-state review, key outputs | Treating saved cell outputs as evidence of reproducibility |
| Figure or table | Source data, transformations, values, labels, units, categories, aggregation | Using pixel equality as the only scientific check |
| Performance-sensitive kernel | Correctness evidence plus representative benchmark and resource envelope | Assuming vectorization preserves numerical semantics |

## Deterministic comparisons

Compare stable fields exactly. Normalize only known nondeterministic metadata and name each ignored field. Preserve ordering when it is part of the contract. Check negative/error paths, file names, and downstream interfaces as well as successful return values.

## Numerical comparisons

Record dtype, precision, hardware, device, libraries, solver settings, and nondeterminism that can affect results. Preserve operation order when rounding, convergence, overflow, cancellation, or parallel reduction may matter. Derive tolerances only from repository tests, documented domain requirements, a configured profile, or a justified characterization baseline; record the provenance. Check invariants such as conservation, monotonicity, bounds, symmetry, or dimensional consistency in addition to elementwise error.

## Stochastic comparisons

Identify RNG family, seed derivation, stream/substream use, sampling order, worker seeding, trial assignment, randomization, and counterbalancing. A fixed-seed check detects accidental call-order changes. A multi-seed check evaluates selected aggregate properties. Predefine metrics and any equivalence margin from project or domain evidence; do not choose them after seeing the new output.

## Statistical analyses

Protect model formulas, contrast/reference levels, grouping, weighting, exclusion criteria, missing-data treatment, multiple-comparison corrections, and sample sizes. Compare estimates, intervals, test statistics, and derived quantities as appropriate. A result with `p > 0.05` does not establish equivalence; use an evidence-backed equivalence margin when equivalence testing is warranted.

## Machine learning

Record dataset/version, sample IDs for each split, label and feature ordering, preprocessing fit scope, leakage barriers, seed controls, evaluation mode, metric implementations, checkpoint and resume formats, device and precision. Run a cheap smoke check only to verify mechanics. Clearly distinguish it from full retraining, benchmark replication, or statistical parity across runs.

## Notebooks, figures, and tables

Inspect cell order, duplicate definitions, global mutation, manual steps, and values read from prior sessions. Prefer a thin narrative notebook calling importable scientific logic when reuse justifies it, but do not automatically convert an exploration into a package. When possible, restart the kernel and execute top-to-bottom in a clean environment. For figures and tables, compare the upstream data and transformation semantics: plotted values, category order, units, axes, filters, joins, and aggregation. Use pixel comparison only when visual rendering itself is the defined contract.

## Published and archived work

Do not overwrite the canonical snapshot. Work in a new version or branch, keep the original reproduction route, and record intentional output changes. If data, software, credentials, or hardware required for verification are unavailable, state the exact missing dependency and cap the conclusion accordingly.

## Characterization when evidence is weak

Before a high-risk refactor with inadequate tests, capture bounded behavior from representative, permitted inputs. Include edge cases tied to known scientific rules. Label characterization as observed behavior, not scientific truth. If sensitive or unavailable data prevents adequate characterization, recommend documentation, a wrapper, or domain review instead of aggressive editing.
