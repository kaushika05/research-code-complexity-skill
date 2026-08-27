# Evals

`evals.json` follows the current Agent Skills evaluation guide: each case has a realistic prompt, human-readable expected outcome, optional fixture files, and observable assertions. The cases emphasize decisions and safety rather than exact wording.

Run each case in a clean workspace twice: once with this skill available and once without it (or against a pinned earlier version). Save outputs, timing, and assertion grading outside the skill directory so generated results are not packaged as runtime resources.

Model-based evals are intentionally absent from public CI because they require a model account and incur variable cost. See the root `VALIDATION.md` for the comparisons actually executed for this release. Static CI verifies that all 14 definitions contain prompts, expected outcomes, and assertions and that referenced fixtures exist.

Grade a PASS only with concrete output evidence. In particular, check that the agent does not refactor every high-CC function, modify raw/generated/frozen artifacts, invent tolerances, use non-significance as equivalence, or claim checks it did not run.
