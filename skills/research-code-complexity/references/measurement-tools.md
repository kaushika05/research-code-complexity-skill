# Measurement tools

Read this reference before choosing an analyzer for an unfamiliar language. Tool support was checked against linked project or vendor documentation on 2026-08-27; verify again when practical because versions and syntax change.

## Selection rules

1. Prefer a repository-pinned analyzer, configuration, and threshold.
2. Record the exact executable version and command actually used.
3. Run an unpinned tool only in an isolated environment; do not alter the research environment merely to obtain a metric.
4. Treat values from different analyzers or counting variants as non-equivalent.
5. If a parser cannot handle the language version, macros, generated constructs, or notebook magics, disclose the gap and use a transparent manual count for affected units.

## Language matrix

| Language/artifact | Viable primary approach | Example after confirming local setup | Important limits |
|---|---|---|---|
| Python | [Radon](https://radon.readthedocs.io/en/latest/commandline.html) | `radon cc -s path` | `assert`, comprehensions, and Boolean handling follow Radon's convention; record flags. |
| R | CRAN [`cyclocomp`](https://cran.r-project.org/web/packages/cyclocomp/index.html) | `Rscript -e "print(cyclocomp::cyclocomp_package_dir('.'))"` for a package | A loose script may require parsing functions/expressions and calling `cyclocomp()` individually; say when top-level flow is manual. |
| JavaScript / TypeScript | ESLint [`complexity`](https://eslint.org/docs/latest/rules/complexity) when configured | `npx eslint path` using the repository config | The classic/modified variant and newer constructs such as optional chaining affect counts. Do not inject a temporary rule into project config. |
| Go | [`gocyclo`](https://github.com/fzipp/gocyclo) | `gocyclo -top 20 path` | Counts `if`, `for`, `case`, `&&`, and `||` plus one. Record ignored paths. |
| C / C++ | [`Lizard`](https://github.com/terryyin/lizard) | `lizard -l cpp path` | Parser-based and header-independent; macros and preprocessing can change what is visible. Record extensions and classic/modified mode. |
| Rust | [`rust-code-analysis-cli`](https://mozilla.github.io/rust-code-analysis/) or repository-configured Lizard | Run the pinned CLI and export per-function metrics | Confirm the installed version supports the repository's Rust syntax. Clippy's cognitive-complexity lint is secondary, not cyclomatic complexity. |
| Java | [PMD `CyclomaticComplexity`](https://docs.pmd-code.org/latest/pmd_rules_java_design.html#cyclomaticcomplexity) | Run the repository's PMD ruleset/build task | PMD configuration controls class/method reporting and thresholds. A standalone Lizard result is an alternative, not directly comparable. |
| Julia | [`CodeComplexity.jl`](https://github.com/charleskawczynski/CodeComplexity.jl) when already adopted or isolated | `measure_file(CyclomaticComplexity(), "file.jl")` | This is a young ecosystem tool. Record package version and parser limitations; otherwise use a Julia parser or manual per-definition count. |
| MATLAB | MathWorks [`checkcode`](https://www.mathworks.com/help/matlab/ref/checkcode.html) | `checkcode('file.m','-cyc')` or `'-modcyc'` | Requires MATLAB. Record classic versus modified complexity and MATLAB release. `codeIssues` does not provide this metric. |
| Fortran | [Lizard](https://github.com/terryyin/lizard) when the file dialect parses correctly | `lizard path/to/source.f90` | Verify dialect and function recognition on representative files; fall back to manual/parser-assisted counting for unsupported syntax or preprocessing. |
| Shell | [`ShellMetrics`](https://github.com/shellspec/shellmetrics) for supported POSIX-like shells | `shellmetrics script.sh` | Values can vary by parser shell. ShellCheck is useful lint evidence but does not report cyclomatic complexity. |
| Jupyter notebooks | Radon for Python cell functions, plus notebook-state inspection | `radon cc -s --include-ipynb --ipynb-cells notebook.ipynb` | Optional `nbformat` is required. Radon does not establish execution order, hidden state, or reproducibility; inspect top-level cell flow separately. |

Lizard documents support for C/C++, Fortran, Go, Java, JavaScript/TypeScript, Python, R, Rust, and other languages, but its generic support should not automatically displace a repository's language-native analyzer. Confirm file recognition and function boundaries before relying on its output.

## Manual convention

When no verified tool is available, state the syntax and convention. A reasonable classic count is `1 + each decision point` within one function or equivalent unit. List what counts: `if`/`elseif`, loop, `case` or pattern arm, `catch`, ternary, and short-circuit Boolean decisions as applicable. Explain whether `else`, comprehensions, default arguments, exceptions, and macros count. Show enough of the count to reproduce it.

For notebooks, report three distinct observations:

1. Complexity of functions defined in cells.
2. Top-level cell control flow.
3. Hidden cross-cell state, duplicate definitions, and execution-order dependencies.

## Interpreting results

Use repository thresholds first. Without them, ranges may prioritize review, but never create a universal refactor mandate. Scientific role and risk can reverse the apparent priority: a runner with CC 12 may be safer to refactor before a literal solver kernel with CC 25.

Secondary metrics such as nesting depth, cognitive complexity, parameter/flag count, coupling, and dataflow opacity can explain why code is difficult. Report them independently; do not combine them into a weighted quality score.
