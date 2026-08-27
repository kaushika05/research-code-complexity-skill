# Artifact roles and lifecycle

Read this reference when role or lifecycle is uncertain, or when protected artifacts may be in scope.

## Evidence order

Classify from the strongest available combination of README statements, execution entrypoints, manuscript or protocol links, imports and callers, comments and docstrings, configuration, tests, data lineage, release tags, archive metadata, and relevant git history. Paths and extensions are clues, not proof. Record conflicts and uncertainty.

## Roles and default posture

| Role | Evidence to seek | Default posture |
|---|---|---|
| Exploratory notebook | Narrative cells, ad hoc inspection, interactive state | Proportional changes; prioritize restartability and clarity. Do not force packaging. |
| Exploratory script | One-off analysis, local parameters, limited reuse | Remove harmful branching only when the verification cost is proportionate. |
| Data ingestion | External formats, checksums, source IDs | Protect source identity, parsing rules, schemas, and error behavior. |
| Data cleaning or preprocessing | Missing-data and transformation rules | Preserve fit boundaries, exclusions, units, categories, and row identities. |
| Experiment orchestration | Configuration loops, runners, job launch | Strong candidate for reducing flags, nested dispatch, and mixed responsibilities. |
| Analysis or statistics | Models, contrasts, grouping, correction | Preserve formula, sample definition, weights, missingness, and derived quantities. |
| Visualization or figure generation | Plotting plus transformations | Trace source data and aggregation; pixel equality alone is weak evidence. |
| Scientific kernel | Domain equations or method steps | Preserve literal meaning and operation order; consider annotate, characterize, or wrap. |
| Numerical kernel | Solver or performance-sensitive numeric loop | Protect precision, convergence, layout, parallelism, and performance. |
| Simulation | State transitions and RNG | Preserve state semantics, RNG, scheduling, and aggregate behavior. |
| Reference implementation | Explicit source-method correspondence | Prefer a wrapper and annotations over abstraction. |
| Reusable library | Stable API and multiple consumers | Apply stronger maintainability expectations while protecting compatibility. |
| CLI or infrastructure | Argument parsing, filesystem, scheduling | Refactor accidental orchestration while preserving interfaces and exit behavior. |
| Test or verification | Fixtures, oracles, property checks | Do not lower complexity by weakening independent checks. |
| Manuscript-linked reproduction | Figure/table/paper mapping | Preserve mappings and canonical entrypoints; version intentional changes. |
| Published or archived snapshot | Release, DOI, archival or frozen marker | Leave canonical snapshot unchanged unless a new version is explicitly authorized. |
| Generated code | Generator headers or reproducible generation | Exclude; modify the generator if that is the task. |
| Vendored third-party code | License/vendor metadata, external source | Exclude unless explicitly targeted and legally appropriate. |
| Raw data | Source measurements or immutable acquisition | Never modify during complexity work. |
| Derived data or generated output | Reproducible product of a pipeline | Usually regenerate rather than hand-edit; preserve provenance. |

One file can contain multiple roles. Classify the relevant function, cell, or region when file-level classification would hide that distinction.

## Lifecycle

- **Exploratory:** questions and methods are still fluid; optimize for legible, rerunnable learning.
- **Active research:** results may change; preserve experiment provenance and allow careful iteration.
- **Collaborative internal research:** add stronger shared configuration, interfaces, and reviewability.
- **Pre-publication:** protect analysis decisions, manuscript mappings, and candidate outputs.
- **Published:** preserve a canonical reproduction route and version changes.
- **Archived:** default to documentation or wrapping; avoid mutation.
- **Reusable community software:** apply public API, compatibility, testing, and maintainability expectations.

If evidence cannot distinguish lifecycle, report `uncertain` and use the more conservative posture for potentially published, sensitive, or expensive artifacts.

## Risk cues

Raise scientific risk when a change touches equations, eligibility criteria, data splits, randomization, preprocessing fit, solver control, operation ordering, precision, sample identity, privacy boundaries, frozen outputs, or paper-linked entrypoints. High complexity plus high scientific risk is often a reason to characterize or wrap before refactoring, not a reason to edit first.
