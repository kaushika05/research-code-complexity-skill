# Configuration

Read this reference when a profile exists or the user asks to customize scope, thresholds, contracts, commands, or protection rules.

## Locations and precedence

Resolve values in this order: current request, local project override, shared project profile, user defaults, repository evidence/inference.

- User defaults: `~/.config/research-code-complexity/config.yaml`
- Shared profile: `.research-code-complexity.yaml`
- Local override: `.research-code-complexity.local.yaml` (normally gitignored)

Merge mappings recursively. A higher-precedence scalar or list replaces the lower-precedence value; do not silently concatenate lists because order and exclusions may carry meaning. Match `artifacts` by their `path` value when an override clearly updates the same artifact; otherwise retain distinct entries and report ambiguity. Explicit user instructions remain authoritative even if they are not written to a file.

## Format

The bundled [schema](../assets/research-code-complexity.schema.json) defines supported keys and types. Only `schema_version` is universally required. Use fields only when the repository or user supplies meaningful values.

- `project`: discipline, lifecycle, audience, research outputs.
- `scope`: include/exclude globs.
- `artifacts`: path/glob, role, mutation policy, optional rationale.
- `complexity`: review/refactor triage thresholds and per-role overrides.
- `scientific_contract`: invariants, units, schemas, frozen outputs, manuscript/equation mappings.
- `verification`: exact checks, numerical tolerances with provenance, stochastic seeds/metrics, equivalence margins, performance requirements.
- `commands`: baseline, test, reproduce, benchmark.
- `data`: raw, sensitive, and generated paths.
- `publication`: frozen refs, archived paths, canonical reproduction entrypoints.

Unknown ordinary keys are errors. Extension keys beginning with `x-` are accepted at defined object levels so future or domain-specific additions do not bypass typo detection.

Never invent a numerical tolerance, statistical equivalence margin, project lifecycle, mutation permission, or command. Use `null`, omission, or an explanatory comment in a template until evidence supplies the value.

## Validate

From the repository root, in an isolated development environment with dependencies from `requirements-dev.txt`:

```text
python skills/research-code-complexity/scripts/validate_profile.py .research-code-complexity.yaml
```

The validator reports each error with a JSON-style field path and exits nonzero. Multiple profile paths may be supplied. Validation checks syntax and shape; it does not prove that scientific values are correct.

## Templates

- Start a shared profile from `assets/research-code-complexity.example.yaml`.
- Start a machine-local override from `assets/research-code-complexity.local.example.yaml`.
- See the root `examples/profiles/` directory for distinct research contexts.

When reporting, list the loaded profile sources, winning values relevant to the decision, ignored lower-precedence conflicts, and any repository evidence used for inference.
