# Possible narrow upstream contribution — draft only

No upstream contact, issue, or pull request was made for v0.1.0. This draft is intentionally separate from the research-specific fork.

## Proposed small patch

Replace the upstream threshold language:

> `15+: must split, no debate`

with:

> `15+: investigate with priority. Refactor when the branches are accidental implementation complexity; document, wrap, or leave unchanged when a literal reference implementation, numerical kernel, or published artifact would become less traceable or less safely verifiable.`

## Proposed pull-request text

This change keeps the skill's concise complexity-first scope while making the highest threshold contextual. Some high-CC functions deliberately mirror a reference algorithm, numerical method, or published artifact. In those cases an unconditional split can reduce traceability or alter behavior. The revised text still prioritizes investigation and refactoring of accidental control-flow complexity.

## Release assessment

The patch is small and independently useful, but no actual upstream PR is opened automatically. Before any future submission, re-check upstream contribution norms and current text, ensure the change is not promotional, and confirm the fork's release and attribution remain complete.
