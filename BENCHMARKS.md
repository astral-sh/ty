# Benchmarks

Measured on November 3, 2026 (UTC), on macOS 26.5.2 with an Apple M3 Max
(16 cores: 12 performance and 4 efficiency; 128 GB RAM).

The existing revisions were measured before the updated source revisions. Both
cohorts use the same corrected harness, checker versions, Python targets, worker
limits and dependency cutoff. Dependencies were resolved from each revision’s
requirements with `--exclude-newer=2026-10-24T19:50:00Z`. Changed requirements can
change installed dependencies.

Timing cells show **existing → updated (percentage change)**. Negative changes
mean faster checks. HTTPX, NumPy, FastAPI, SQLAlchemy, Rich and Jinja have identical
inputs across cohorts and reuse the same measured samples, so their deltas are zero.

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

| Project       |                     ty |                Pyrefly |                     mypy |                  Pyright |
| ------------- | ---------------------: | ---------------------: | -----------------------: | -----------------------: |
| black         |    63.3 → 69.1 (+9.2%) |  124.6 → 134.1 (+7.6%) |    656.0 → 683.8 (+4.2%) |    1,371 → 1,433 (+4.5%) |
| discord.py    |  137.3 → 137.3 (-0.0%) |  176.6 → 176.3 (-0.2%) |    1,946 → 1,981 (+1.8%) |    3,080 → 3,021 (-1.9%) |
| homeassistant | 1,788 → 2,085 (+16.6%) | 1,992 → 2,308 (+15.9%) |  9,550 → 13,599 (+42.4%) | 25,637 → 29,820 (+16.3%) |
| isort         |    83.4 → 91.5 (+9.7%) |  104.9 → 106.7 (+1.7%) |    466.0 → 495.5 (+6.3%) |   2,501 → 1,744 (-30.3%) |
| jinja         |    56.0 → 56.0 (+0.0%) |  105.0 → 105.0 (+0.0%) |    624.3 → 624.3 (+0.0%) |    1,348 → 1,348 (+0.0%) |
| pandas        |  373.0 → 387.8 (+3.9%) | 772.0 → 910.8 (+18.0%) |    6,949 → 7,570 (+8.9%) |    7,311 → 7,797 (+6.6%) |
| pandas-stubs  |    86.2 → 85.7 (-0.6%) |  205.0 → 197.2 (-3.8%) |    3,592 → 3,569 (-0.6%) |    2,188 → 2,240 (+2.4%) |
| prefect       |  109.5 → 111.5 (+1.9%) |  258.2 → 273.9 (+6.1%) |    4,404 → 4,712 (+7.0%) |    3,848 → 3,912 (+1.7%) |
| pytorch       | 1,122 → 1,310 (+16.8%) | 1,022 → 1,225 (+19.8%) | 18,884 → 21,916 (+16.1%) | 16,193 → 18,060 (+11.5%) |
| httpx         |    67.1 → 67.1 (+0.0%) |  120.4 → 120.4 (+0.0%) |    658.8 → 658.8 (+0.0%) |    1,084 → 1,084 (+0.0%) |
| numpy         |  395.2 → 395.2 (+0.0%) |  565.2 → 565.2 (+0.0%) |  80,800 → 80,800 (+0.0%) |    8,102 → 8,102 (+0.0%) |
| fastapi       |    89.9 → 89.9 (+0.0%) |  299.5 → 299.5 (+0.0%) |    1,141 → 1,141 (+0.0%) |    2,175 → 2,175 (+0.0%) |
| sqlalchemy    |  280.7 → 280.7 (+0.0%) |  306.3 → 306.3 (+0.0%) |    2,666 → 2,666 (+0.0%) |    4,862 → 4,862 (+0.0%) |
| rich          |    64.2 → 64.2 (+0.0%) |  122.8 → 122.8 (+0.0%) |    1,002 → 1,002 (+0.0%) |    1,776 → 1,776 (+0.0%) |

## CLI peak RSS

Mean peak RSS from the same Hyperfine runs, in MiB. On macOS this uses
`wait4`/`ru_maxrss` and **does not sum concurrent worker processes**. In particular,
mypy and Pyright values are not total process-tree memory. The LSP suites measure
latency only.

| Project       |            ty |       Pyrefly |          mypy |       Pyright |
| ------------- | ------------: | ------------: | ------------: | ------------: |
| black         | 132.7 → 136.8 | 155.9 → 160.0 | 105.7 → 106.5 | 290.0 → 289.6 |
| discord.py    | 222.8 → 223.5 | 216.5 → 216.5 | 211.4 → 212.1 | 426.2 → 432.1 |
| homeassistant | 2,986 → 3,497 | 2,579 → 3,031 | 958.5 → 1,234 | 1,713 → 1,899 |
| isort         |   93.6 → 90.5 | 103.8 → 103.8 |   89.7 → 89.8 | 297.3 → 263.8 |
| jinja         |   99.9 → 99.9 | 116.0 → 116.0 |   90.4 → 90.4 | 257.0 → 257.0 |
| pandas        | 570.1 → 588.0 | 563.1 → 570.4 | 550.9 → 573.9 | 750.5 → 753.3 |
| pandas-stubs  | 155.6 → 157.9 | 273.6 → 273.9 | 387.2 → 389.4 | 374.0 → 381.0 |
| prefect       | 221.4 → 223.3 | 291.8 → 293.7 | 433.1 → 439.7 | 571.5 → 571.8 |
| pytorch       | 1,440 → 1,646 | 800.3 → 904.9 | 1,483 → 1,667 | 1,570 → 1,746 |
| httpx         | 105.5 → 105.5 | 129.8 → 129.8 |   96.6 → 96.6 | 258.1 → 258.1 |
| numpy         | 285.5 → 285.5 | 519.2 → 519.2 | 566.4 → 566.4 | 632.9 → 632.9 |
| fastapi       | 142.5 → 142.5 | 194.0 → 194.0 | 133.1 → 133.1 | 333.9 → 333.9 |
| sqlalchemy    | 405.5 → 405.5 | 301.0 → 301.0 | 271.4 → 271.4 | 549.8 → 549.8 |
| rich          | 122.1 → 122.1 | 133.3 → 133.3 | 119.3 → 119.3 | 284.4 → 284.4 |

## LSP: initial diagnostics

Two warmups and ten measured rounds. Every server opens the same fixture files
and receives the same edit. pandas-stubs has no edit fixture and is omitted.

Initial latency ends at the first diagnostic response for each open file. Push
notifications can be empty or partial, so this does not establish completion of
all background analysis.

| Project       |                     ty |               Pyrefly |                Pyright |
| ------------- | ---------------------: | --------------------: | ---------------------: |
| black         |   58.7 → 67.8 (+15.5%) | 167.2 → 180.5 (+8.0%) |  289.7 → 300.9 (+3.9%) |
| discord.py    |  104.6 → 104.7 (+0.1%) | 187.7 → 188.4 (+0.4%) |  623.4 → 630.3 (+1.1%) |
| homeassistant |   94.3 → 101.6 (+7.7%) | 220.2 → 237.7 (+7.9%) | 1,617 → 1,905 (+17.8%) |
| isort         |    47.1 → 50.3 (+6.8%) | 97.2 → 134.1 (+38.1%) |  352.3 → 358.1 (+1.6%) |
| jinja         |    51.5 → 51.5 (+0.0%) | 126.4 → 126.4 (+0.0%) |  356.4 → 356.4 (+0.0%) |
| pandas        | 335.9 → 371.4 (+10.6%) | 528.1 → 543.9 (+3.0%) |  626.3 → 639.1 (+2.1%) |
| prefect       |  169.8 → 176.5 (+3.9%) | 460.3 → 452.5 (-1.7%) |  1,088 → 1,113 (+2.3%) |
| pytorch       |   58.1 → 71.7 (+23.5%) | 117.1 → 128.7 (+9.9%) |  677.2 → 705.5 (+4.2%) |
| httpx         |    46.5 → 46.5 (+0.0%) | 115.3 → 115.3 (+0.0%) |  226.4 → 226.4 (+0.0%) |
| numpy         |  308.3 → 308.3 (+0.0%) | 564.4 → 564.4 (+0.0%) |  1,200 → 1,200 (+0.0%) |
| fastapi       |  102.0 → 102.0 (+0.0%) | 200.4 → 200.4 (+0.0%) |  465.9 → 465.9 (+0.0%) |
| sqlalchemy    |  216.3 → 216.3 (+0.0%) | 251.9 → 251.9 (+0.0%) |  272.7 → 272.7 (+0.0%) |
| rich          |    43.1 → 43.1 (+0.0%) | 111.0 → 111.0 (+0.0%) |  311.3 → 311.3 (+0.0%) |

## LSP: incremental edit

Two warmups and ten measured rounds. Every server opens the same fixture files
and receives the same edit. pandas-stubs has no edit fixture and is omitted.

| Project       |                  ty |               Pyrefly |                Pyright |
| ------------- | ------------------: | --------------------: | ---------------------: |
| black         | 14.9 → 16.2 (+8.6%) |  78.1 → 91.4 (+17.0%) |  500.0 → 549.4 (+9.9%) |
| discord.py    | 25.5 → 25.7 (+1.0%) |   77.3 → 76.5 (-1.0%) |  521.8 → 517.2 (-0.9%) |
| homeassistant | 28.2 → 30.0 (+6.4%) |   78.3 → 75.7 (-3.3%) |  583.8 → 574.5 (-1.6%) |
| isort         | 19.6 → 21.4 (+9.3%) |  42.3 → 52.9 (+25.2%) |  420.5 → 425.1 (+1.1%) |
| jinja         | 12.3 → 12.3 (+0.0%) |   60.3 → 60.3 (+0.0%) |  503.9 → 503.9 (+0.0%) |
| pandas        | 42.8 → 43.8 (+2.5%) | 229.4 → 248.6 (+8.4%) | 603.1 → 691.2 (+14.6%) |
| prefect       |   8.0 → 8.0 (+0.1%) |   57.4 → 56.3 (-1.9%) |  670.8 → 680.9 (+1.5%) |
| pytorch       |   3.7 → 4.0 (+7.5%) |   22.1 → 22.8 (+3.0%) |  404.0 → 416.3 (+3.0%) |
| httpx         |   7.5 → 7.5 (+0.0%) |   51.7 → 51.7 (+0.0%) |  426.5 → 426.5 (+0.0%) |
| numpy         | 29.8 → 29.8 (+0.0%) | 343.8 → 343.8 (+0.0%) |  1,188 → 1,188 (+0.0%) |
| fastapi       |   7.3 → 7.3 (+0.0%) |   65.8 → 65.8 (+0.0%) |  614.2 → 614.2 (+0.0%) |
| sqlalchemy    | 11.6 → 11.6 (+0.0%) |   76.4 → 76.4 (+0.0%) |  639.1 → 639.1 (+0.0%) |
| rich          |   5.9 → 5.9 (+0.0%) |   31.1 → 31.1 (+0.0%) |  440.8 → 440.8 (+0.0%) |

## Root scope

Stub counts and omitted implementation-line fractions describe only the authored
include/exclude scope. Imported modules can add work beyond these roots.

| Project       |  Roots | Stubs | Eligible implementation lines omitted |
| ------------- | -----: | ----: | ------------------------------------: |
| black         |     42 |     1 |                                  0.0% |
| discord.py    |    144 |     0 |                                  0.0% |
| homeassistant | 10,765 |     3 |                                  0.0% |
| isort         |     40 |     0 |                                  0.0% |
| jinja         |     25 |     0 |                                  0.0% |
| pandas        |    337 |    41 |                                  0.0% |
| pandas-stubs  |    183 |   183 |                                  0.0% |
| prefect       |     58 |     0 |                                  0.0% |
| pytorch       |  2,416 |    37 |                                  0.3% |
| httpx         |     23 |     0 |                                  0.0% |
| numpy         |    205 |   167 |                                 89.9% |
| fastapi       |     52 |     0 |                                  0.0% |
| sqlalchemy    |    258 |     0 |                                  0.0% |
| rich          |    100 |     0 |                                  0.0% |

## Project revisions

| Project       | Existing                                   | Updated                                    |
| ------------- | ------------------------------------------ | ------------------------------------------ |
| black         | `ce1897a8f20d0f64844dd666d07f4003500d0e09` | `55996d1fb8342725c8a19b6023cd9439c3c1d6f7` |
| discord.py    | `2fbed9362422dad4f7850eb6c5d9b1f8bff7c71a` | `65232c38702be5844cf2ce865a4777eb1928b5d0` |
| homeassistant | `a0162d2ff0ed061501405a617961be149b15bd1f` | `c19ae285ede74cd64c3045a3a4aa43290c224f1b` |
| isort         | `87adfe4732548abff5010336f2fc4b5e8237407d` | `a514c71ed86c2216d0040c7d60e302ed76a4f7ab` |
| jinja         | `5ef70112a1ff19c05324ff889dd30405b1002044` | `5ef70112a1ff19c05324ff889dd30405b1002044` |
| pandas        | `e3a56513f27849f12265a14c814e02f4f408fb3d` | `a0225b65720018f4654390bb16d254daa6ee5e54` |
| pandas-stubs  | `1352ba3daa86f1c47a3cce5ad212a770cc693cb4` | `8dd6d91b1c05b26e30f7ddbe3dc3d4042a92bdd6` |
| prefect       | `db66b14dbaea18e726fc4ea0100fd194383c6c59` | `a9452ac21852755311913cb27887b083b5007c03` |
| pytorch       | `29d6170e7c79f2c71943692985a1546fb2bed28c` | `ab92945cea42e47ae398aead69af0872d340ea0f` |
| httpx         | `b5addb64f0161ff6bfe94c124ef76f6a1fba5254` | `b5addb64f0161ff6bfe94c124ef76f6a1fba5254` |
| numpy         | `f9f1772ce010001208475f751d19253469788410` | `f9f1772ce010001208475f751d19253469788410` |
| fastapi       | `7a0a3f0b286c6c865cf4398ea0e957a87b8bffa4` | `7a0a3f0b286c6c865cf4398ea0e957a87b8bffa4` |
| sqlalchemy    | `10f4d1e2d706a7722ca78e79ce05b00333a7aa5b` | `10f4d1e2d706a7722ca78e79ce05b00333a7aa5b` |
| rich          | `9d8f9a372cc5916fd4781fec207ced7ddac2f08f` | `9d8f9a372cc5916fd4781fec207ced7ddac2f08f` |

Both pandas cohorts use the current `pandas` root; the older revision’s separate
`typings/numba.pyi` is outside this common authored scope.

## Comparison with ty

Geometric mean of competitor time divided by ty time on the common successful
projects for each metric. A value above 1 means ty is faster.

| Metric      | Common projects | Pyrefly |   mypy | Pyright |
| ----------- | --------------: | ------: | -----: | ------: |
| cli         |              14 |   1.67× | 16.61× |  20.84× |
| initial     |              13 |   2.08× |      — |   5.21× |
| incremental |              13 |   5.35× |      — |  41.77× |

Performance varies with hardware, dependencies and background load. Matching
root scope and settings does not establish equivalent inference or diagnostic
quality. Earlier datasets with different workloads or worker settings are not
directly comparable.
