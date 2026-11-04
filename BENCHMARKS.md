# Benchmarks

Measured on November 3, 2026 (UTC), on macOS 26.5.2 with an Apple M3 Max
(16 cores: 12 performance and 4 efficiency; 128 GB RAM).

These results retain the existing project revisions and update the checkers and
runtimes. They use the controlled workloads described below. The stacked
[project refresh](https://github.com/astral-sh/ty/pull/4819) measures updated
source revisions with the same checker versions and dependency cutoff.

All ty LSP measurements were collected again with canonical workspace/document
paths. A paired URI control found duplicate SQLAlchemy module identities under
the lexical path spelling, which changed ty diagnostics and timing. The ty,
Pyrefly, mypy and Pyright CLI samples and the Pyrefly/Pyright LSP samples are
retained unchanged from the previous controlled collection, using the same
physical source files and dependency environments.

Times are wall-clock milliseconds. Single-cohort timings show mean ± standard
deviation. RSS values are in MiB.

- ty: [0.0.96](https://github.com/astral-sh/ty/releases/tag/0.0.96), published PyPI
    macOS arm64 binary (`ty 0.0.96 (53a7844b8 2026-11-02)`).
- Pyrefly: 1.4.0; Pyright: 1.1.414; mypy: 2.4.0 (compiled).
- Hyperfine: 2.0.0; uv: 0.13.5; Node.js: 26.12.1; npm: 12.2.1.
- Harness Python: 3.15.1. Project Python: 3.11.17, except Home Assistant
    (3.14.9) and NumPy (3.12.15).
- Dependency cutoff: `2026-10-24T19:50:00Z`. Project environments include mypy
    regardless of which checker is selected.

## Workload and measurement controls

Each CLI discovers directories inside the timed command. An untimed manifest and
compact exclusions align the expected **roots**; a preflight rejects empty or
mismatched discovery. Counts describe roots, not all files analyzed: imported
dependencies may still be checked. Discovery cost is included. Expanded lists of
individual targets can themselves bias runtime.

Adjacent stubs replace implementation roots for every checker. Packages take
precedence over same-named modules; modules take precedence over non-package
build directories. Symlinks, untracked Python files and notebooks are excluded.
This is a controlled module workload, not default full-project discovery.

Unannotated-body checking is enabled. Whole-file checker overrides are neutralized
in disposable source copies; ordinary line-level suppressions remain. Every
checker receives additional first-party import roots, including `src/` layouts
and SQLAlchemy’s `lib/`, so installed releases cannot take precedence over the
checkout. Project/user configs and checker environment overrides cannot silently
narrow the CLI scope; ty and Pyrefly ignore discovery ignore files. Imported
dependencies, inferred types, platform branches and diagnostic coverage can still
differ between checkers.

Multicore CLI limits are explicit: 16 mypy workers, 16 Pyright workers, 16 Pyrefly
threads, and 16-thread pool limit for ty. This differs from earlier
runs where mypy defaulted to zero external workers; these results cannot isolate
only the effect of a checker release or native discovery.

NumPy has **205 roots: 167 stubs and 38 implementations**. Its compiled-extension
stub `numpy/linalg/lapack_lite.pyi` is included; the same-named build directory is
excluded. Stub preference omits **89.9%** of otherwise eligible implementation
lines. NumPy’s C extensions are not built. This timing therefore describes the
shared stub-heavy workload, not checking every NumPy implementation body.

The pandas workload excludes `pandas/tests` for every checker. Timings from suites
that include those tests use a broader scope; selected modules, including
clipboard, use the common unannotated-body policy here.

A separate lexical/physical LSP URI control covers isort and SQLAlchemy with ty,
Pyrefly and Pyright: 24 initial/edit cases pass across the two path spellings.
For ty/SQLAlchemy initial diagnostics, canonical paths remove seven duplicate
module-identity errors (58 diagnostics versus 51) and materially reduce latency.
Initial diagnostic responses can be partial. We reran the ty LSP benchmarks for
each project input and excluded the separate path comparison from the timings below.

Run instructions: [`ty_benchmark/README.md`](https://github.com/astral-sh/ruff/blob/5ca55b2baffd6200b61c540c17255d9e20055272/scripts/ty_benchmark/README.md).

## CLI cold check

Three warmups and at least ten measured runs; the mypy cache is cleared before
every warmup and measured run.

| Project       |           ty |      Pyrefly |           mypy |        Pyright |
| ------------- | -----------: | -----------: | -------------: | -------------: |
| black         |   63.3 ± 2.3 |  124.6 ± 2.1 |   656.0 ± 13.6 |    1,371 ± 6.3 |
| discord.py    |  137.3 ± 5.8 |  176.6 ± 5.8 |   1,946 ± 16.3 |   3,080 ± 24.5 |
| homeassistant | 1,788 ± 57.2 | 1,992 ± 27.0 |   9,550 ± 62.8 | 25,637 ± 185.8 |
| isort         |   83.4 ± 1.9 |  104.9 ± 1.8 |   466.0 ± 11.3 |   2,501 ± 19.0 |
| jinja         |   56.0 ± 1.3 |  105.0 ± 1.2 |   624.3 ± 12.4 |    1,348 ± 6.9 |
| pandas        | 373.0 ± 18.8 | 772.0 ± 59.9 |  6,949 ± 107.5 |   7,311 ± 54.9 |
| pandas-stubs  |   86.2 ± 3.4 |  205.0 ± 2.0 |   3,592 ± 36.9 |   2,188 ± 16.7 |
| prefect       |  109.5 ± 6.6 |  258.2 ± 9.7 |   4,404 ± 32.2 |   3,848 ± 25.4 |
| pytorch       | 1,122 ± 36.1 | 1,022 ± 18.7 |  18,884 ± 67.7 | 16,193 ± 118.5 |
| httpx         |   67.1 ± 1.5 |  120.4 ± 3.1 |   658.8 ± 16.6 |    1,084 ± 6.3 |
| numpy         | 395.2 ± 15.6 |  565.2 ± 9.9 | 80,800 ± 487.7 |   8,102 ± 95.3 |
| fastapi       |   89.9 ± 3.0 |  299.5 ± 3.7 |   1,141 ± 13.2 |   2,175 ± 24.0 |
| sqlalchemy    | 280.7 ± 12.7 |  306.3 ± 6.3 |    2,666 ± 6.7 |   4,862 ± 29.7 |
| rich          |   64.2 ± 3.1 |  122.8 ± 3.2 |    1,002 ± 8.3 |   1,776 ± 56.7 |

## CLI peak RSS

Mean peak RSS from the same Hyperfine runs, in MiB. On macOS this uses
`wait4`/`ru_maxrss` and **does not sum concurrent worker processes**. In particular,
mypy and Pyright values are not total process-tree memory. The LSP suites measure
latency only.

| Project       |    ty | Pyrefly |  mypy | Pyright |
| ------------- | ----: | ------: | ----: | ------: |
| black         | 132.7 |   155.9 | 105.7 |   290.0 |
| discord.py    | 222.8 |   216.5 | 211.4 |   426.2 |
| homeassistant | 2,986 |   2,579 | 958.5 |   1,713 |
| isort         |  93.6 |   103.8 |  89.7 |   297.3 |
| jinja         |  99.9 |   116.0 |  90.4 |   257.0 |
| pandas        | 570.1 |   563.1 | 550.9 |   750.5 |
| pandas-stubs  | 155.6 |   273.6 | 387.2 |   374.0 |
| prefect       | 221.4 |   291.8 | 433.1 |   571.5 |
| pytorch       | 1,440 |   800.3 | 1,483 |   1,570 |
| httpx         | 105.5 |   129.8 |  96.6 |   258.1 |
| numpy         | 285.5 |   519.2 | 566.4 |   632.9 |
| fastapi       | 142.5 |   194.0 | 133.1 |   333.9 |
| sqlalchemy    | 405.5 |   301.0 | 271.4 |   549.8 |
| rich          | 122.1 |   133.3 | 119.3 |   284.4 |

## LSP: initial diagnostics

Two warmups and ten measured rounds. Every server opens the same fixture files
and receives the same edit. pandas-stubs has no edit fixture and is omitted.

Initial latency ends at the first diagnostic response for each open file. Push
notifications can be empty or partial, so this does not establish completion of
all background analysis.

| Project       |          ty |      Pyrefly |      Pyright |
| ------------- | ----------: | -----------: | -----------: |
| black         |  58.7 ± 0.1 |  167.2 ± 0.4 |  289.7 ± 1.4 |
| discord.py    | 104.6 ± 0.3 |  187.7 ± 1.2 |  623.4 ± 5.1 |
| homeassistant |  94.3 ± 0.9 |  220.2 ± 5.2 | 1,617 ± 10.4 |
| isort         |  47.1 ± 0.2 |   97.2 ± 3.8 |  352.3 ± 2.0 |
| jinja         |  51.5 ± 0.1 |  126.4 ± 0.4 |  356.4 ± 2.3 |
| pandas        | 335.9 ± 1.6 |  528.1 ± 3.0 |  626.3 ± 5.6 |
| prefect       | 169.8 ± 0.2 |  460.3 ± 1.3 |  1,088 ± 5.2 |
| pytorch       |  58.1 ± 0.1 | 117.1 ± 13.1 |  677.2 ± 3.1 |
| httpx         |  46.5 ± 0.1 |  115.3 ± 1.2 |  226.4 ± 1.1 |
| numpy         | 308.3 ± 1.3 |  564.4 ± 1.4 |  1,200 ± 9.0 |
| fastapi       | 102.0 ± 3.3 |  200.4 ± 0.6 |  465.9 ± 4.0 |
| sqlalchemy    | 216.3 ± 0.6 |  251.9 ± 1.7 |  272.7 ± 1.6 |
| rich          |  43.1 ± 0.4 |  111.0 ± 5.6 |  311.3 ± 1.3 |

## LSP: incremental edit

Two warmups and ten measured rounds. Every server opens the same fixture files
and receives the same edit. pandas-stubs has no edit fixture and is omitted.

| Project       |         ty |     Pyrefly |      Pyright |
| ------------- | ---------: | ----------: | -----------: |
| black         | 14.9 ± 0.7 |  78.1 ± 3.9 |  500.0 ± 5.7 |
| discord.py    | 25.5 ± 0.2 |  77.3 ± 4.5 | 521.8 ± 14.3 |
| homeassistant | 28.2 ± 0.2 |  78.3 ± 5.1 |  583.8 ± 5.8 |
| isort         | 19.6 ± 0.1 |  42.3 ± 2.2 |  420.5 ± 8.4 |
| jinja         | 12.3 ± 0.6 |  60.3 ± 4.6 | 503.9 ± 14.2 |
| pandas        | 42.8 ± 2.6 | 229.4 ± 3.8 |  603.1 ± 7.7 |
| prefect       |  8.0 ± 0.3 |  57.4 ± 2.9 |  670.8 ± 5.7 |
| pytorch       |  3.7 ± 0.1 |  22.1 ± 3.7 | 404.0 ± 10.4 |
| httpx         |  7.5 ± 0.2 |  51.7 ± 2.8 | 426.5 ± 10.5 |
| numpy         | 29.8 ± 0.4 | 343.8 ± 6.4 | 1,188 ± 10.3 |
| fastapi       |  7.3 ± 0.2 |  65.8 ± 3.4 |  614.2 ± 5.6 |
| sqlalchemy    | 11.6 ± 0.2 |  76.4 ± 8.0 |  639.1 ± 5.7 |
| rich          |  5.9 ± 0.2 |  31.1 ± 7.2 |  440.8 ± 4.4 |

## Root scope

Stub counts and omitted implementation-line fractions describe only the authored
include/exclude scope. Imported modules can add work beyond these roots.

| Project       | Roots | Stubs | Eligible implementation lines omitted |
| ------------- | ----: | ----: | ------------------------------------: |
| black         |    42 |     1 |                                  0.0% |
| discord.py    |   144 |     0 |                                  0.0% |
| homeassistant | 9,586 |     3 |                                  0.0% |
| isort         |    44 |     0 |                                  0.0% |
| jinja         |    25 |     0 |                                  0.0% |
| pandas        |   335 |    41 |                                  0.0% |
| pandas-stubs  |   184 |   184 |                                  0.0% |
| prefect       |    57 |     0 |                                  0.0% |
| pytorch       | 2,213 |    36 |                                  0.4% |
| httpx         |    23 |     0 |                                  0.0% |
| numpy         |   205 |   167 |                                 89.9% |
| fastapi       |    52 |     0 |                                  0.0% |
| sqlalchemy    |   258 |     0 |                                  0.0% |
| rich          |   100 |     0 |                                  0.0% |

## Project revisions

| Project       | Revision                                   |
| ------------- | ------------------------------------------ |
| black         | `ce1897a8f20d0f64844dd666d07f4003500d0e09` |
| discord.py    | `2fbed9362422dad4f7850eb6c5d9b1f8bff7c71a` |
| homeassistant | `a0162d2ff0ed061501405a617961be149b15bd1f` |
| isort         | `87adfe4732548abff5010336f2fc4b5e8237407d` |
| jinja         | `5ef70112a1ff19c05324ff889dd30405b1002044` |
| pandas        | `e3a56513f27849f12265a14c814e02f4f408fb3d` |
| pandas-stubs  | `1352ba3daa86f1c47a3cce5ad212a770cc693cb4` |
| prefect       | `db66b14dbaea18e726fc4ea0100fd194383c6c59` |
| pytorch       | `29d6170e7c79f2c71943692985a1546fb2bed28c` |
| httpx         | `b5addb64f0161ff6bfe94c124ef76f6a1fba5254` |
| numpy         | `f9f1772ce010001208475f751d19253469788410` |
| fastapi       | `7a0a3f0b286c6c865cf4398ea0e957a87b8bffa4` |
| sqlalchemy    | `10f4d1e2d706a7722ca78e79ce05b00333a7aa5b` |
| rich          | `9d8f9a372cc5916fd4781fec207ced7ddac2f08f` |

## Comparison with ty

Geometric mean of competitor time divided by ty time on the common successful
projects for each metric. A value above 1 means ty is faster.

| Metric      | Common projects | Pyrefly |   mypy | Pyright |
| ----------- | --------------: | ------: | -----: | ------: |
| cli         |              14 |   1.66× | 16.34× |  21.62× |
| initial     |              13 |   2.08× |      — |   5.34× |
| incremental |              13 |   5.31× |      — |  42.03× |

Performance varies with hardware, dependencies and background load. Matching
root scope and settings does not establish equivalent inference or diagnostic
quality. Earlier datasets with different workloads or worker settings are not
directly comparable.
