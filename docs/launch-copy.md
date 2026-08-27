# Launch copy for v0.1.0

## Standalone Twitter/X post

Research code isn’t just messy production code. I released a skill for notebooks, simulations and ML experiments: Reduce accidental complexity without erasing scientific intent. Built from Saurabh Kumar’s original. https://github.com/kaushika05/research-code-complexity-skill

## Five-post launch thread

1. Research code isn’t simply messy production code. A high-complexity function may encode a published method, numerical kernel, or experimental protocol. I built Research Code Complexity to separate essential scientific complexity from accidental branching.

2. The rule is: Reduce accidental complexity without erasing scientific intent. The skill measures per-function CC, classifies artifact role and lifecycle, identifies the scientific contract, and can decide to refactor, characterize, wrap, defer—or leave the core unchanged.

3. It covers notebooks, simulations, ML experiments and analysis pipelines. Verification changes with the artifact: exact outputs, sourced numerical tolerances, fixed- and multi-seed checks, leakage boundaries, restart-and-run-all, or source-data checks for figures.

4. v0.1.0 includes portable Agent Skills packaging, Claude Code plugin/marketplace manifests, layered YAML profiles and schema validation, 14 safety-focused eval cases, CI, citation metadata, and honest limitations. No paid model calls run in public CI.

5. This is a substantial Apache-2.0 fork of Saurabh Kumar’s original cyclomatic-complexity skill, retaining its measure-first and anti-metric-gaming core. Source, install commands, release, and attribution: https://github.com/kaushika05/research-code-complexity-skill

## LinkedIn

Research code is not simply messy production code. A high-complexity function may encode a published method, a numerical kernel, an experimental protocol, or a frozen reproduction path.

I released Research Code Complexity v0.1.0: an Agent Skill for notebooks, simulations, ML experiments, and analysis pipelines. Its rule is “Reduce accidental complexity without erasing scientific intent.” It measures cyclomatic complexity, establishes the scientific contract, and supports evidence-backed outcomes from refactoring through characterization, wrapping, and leaving a literal kernel unchanged.

The release includes portable skill packaging, a Claude Code marketplace/plugin, layered research profiles with JSON Schema validation, language-tool guidance, 14 decision-focused evals, CI, citation metadata, and explicit limitations. It is a substantial Apache-2.0 fork of Saurabh Kumar’s original cyclomatic-complexity skill.

https://github.com/kaushika05/research-code-complexity-skill

## Social-card alt text

Dark teal card titled “Research Code Complexity.” A branching control-flow diagram resolves into a four-step pipeline labeled measure, classify, protect, and verify. Text reads “Reduce accidental complexity without erasing scientific intent” and lists notebooks, simulations, ML experiments, and analysis pipelines.

## Installation reply

```text
/plugin marketplace add kaushika05/research-code-complexity-skill
/plugin install research-code-complexity@research-code-complexity-skill
```
