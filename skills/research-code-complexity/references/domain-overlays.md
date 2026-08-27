# Domain overlays

Read only the section supported by repository evidence. These prompts refine contract discovery; they do not replace expert review.

## Generic computational research

Trace inputs to outputs, environments, parameters, units, seeds, intermediate schemas, canonical entrypoints, and publication mappings. Separate scientific transformations from file handling and orchestration. Preserve the ability to reproduce the relevant version, while acknowledging unavailable data, services, or hardware.

## Machine learning

Identify dataset and split IDs, leakage boundaries, preprocessing fit scope, feature and label order, augmentation, RNG sources, worker seeds, evaluation mode, metric definitions, checkpoints, device, and precision. Refactor runners and configuration aggressively only after these contracts are explicit. Treat a smoke run as mechanics verification, not model equivalence.

## Numerical simulation and HPC

Protect units, coordinates, boundary/initial conditions, discretization, solver and convergence settings, operation and reduction order, precision, memory layout, decomposition, parallel nondeterminism, checkpoint/resume behavior, and representative performance. A lower CC implementation can be scientifically worse if it changes floating-point order or obscures a published algorithm.

## Empirical, behavioral, or HCI research

Protect participant privacy, de-identification, consent-related boundaries, eligibility and exclusion rules, randomization, counterbalancing, preregistered decisions, instrument scoring, missing-data treatment, and analysis populations. Avoid exposing sensitive paths or values in reports. Domain review may be required before simplifying branching that encodes protocol decisions.

## Bioinformatics or data-intensive life science

Protect sample identity, reference genome/database and annotation versions, coordinate conventions, read/group metadata, filters, normalization, pipeline provenance, environment/tool versions, and intermediate schema. Do not rewrite vendored workflow components or raw biological data. Keep explicit conversions when they make coordinate or reference changes auditable.
