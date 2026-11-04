# Benchmarks

Measured on November 3, 2026 (UTC), on macOS 26.5.2 with an Apple M3 Max
(16 cores: 12 performance and 4 efficiency; 128 GB RAM).

This 18-project suite adds Zuban, Django, SymPy, the OpenAI SDK, and pytest to the
[14-project revision comparison](https://github.com/astral-sh/ty/pull/4819). All
results use the corrected native-discovery harness and published ty 0.0.96.

Zuban CLI and LSP measurements were collected again with canonical import roots
and LSP workspace/document paths. This prevents `/tmp` and `/private/tmp` aliases
from loading the same physical project as separate workspaces.

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
- Zuban: 0.10.2, using mypy-compatible semantics and untyped-body checking.
- Hyperfine: 2.0.0; uv: 0.13.5; Node.js: 26.12.1; npm: 12.2.1.
- Harness Python: 3.15.1. Project Python: 3.11.17, except Home Assistant
    (3.14.9) and NumPy and Django (3.12.15).
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
threads, and 16-thread pool limits for ty and Zuban. This differs from earlier
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

Django adds a dynamic web framework; SymPy adds symbolic pure-Python code; the
OpenAI SDK adds generated typed models and clients; pytest includes its actual
test suite. SymPy excludes tests/benchmarks, the SDK excludes vendored code, and
pytest excludes nested test-input programs under `testing/example_scripts`.

An additional isort audit checked all 40 implementation roots (10,871 lines).
In separate copies, both ty and Zuban detected deliberate errors inside all 177
existing function bodies and inside typed and untyped probe functions in every
root. Contradictory project mypy settings did not change their diagnostics.
We timed only the original copies. These checks address the workload discrepancies in
[lolpack/type_coverage_py#160](https://github.com/lolpack/type_coverage_py/issues/160),
without asserting identical inference or diagnostic quality.

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

| Project       |           ty |      Pyrefly |           mypy |        Pyright |        Zuban |
| ------------- | -----------: | -----------: | -------------: | -------------: | -----------: |
| black         |   69.1 ± 3.1 |  134.1 ± 2.6 |   683.8 ± 10.6 |   1,433 ± 25.7 |  144.7 ± 2.3 |
| discord.py    |  137.3 ± 6.1 |  176.3 ± 4.0 |   1,981 ± 17.2 |   3,021 ± 34.4 |  356.5 ± 3.0 |
| homeassistant | 2,085 ± 10.4 | 2,308 ± 38.7 | 13,599 ± 116.4 | 29,820 ± 104.0 | 7,607 ± 40.2 |
| isort         |   91.5 ± 2.3 |  106.7 ± 1.8 |   495.5 ± 11.3 |   1,744 ± 22.0 |   68.6 ± 1.4 |
| jinja         |   56.0 ± 1.3 |  105.0 ± 1.2 |   624.3 ± 12.4 |    1,348 ± 6.9 |   86.3 ± 2.0 |
| pandas        | 387.8 ± 18.7 |  910.8 ± 7.7 |   7,570 ± 29.5 |   7,797 ± 94.9 | 1,449 ± 10.7 |
| pandas-stubs  |   85.7 ± 3.2 |  197.2 ± 2.8 |   3,569 ± 19.5 |   2,240 ± 16.6 |  279.7 ± 3.9 |
| prefect       |  111.5 ± 8.1 |  273.9 ± 9.1 |   4,712 ± 18.9 |   3,912 ± 31.0 |  980.2 ± 5.4 |
| pytorch       | 1,310 ± 41.2 | 1,225 ± 20.8 |  21,916 ± 70.8 | 18,060 ± 185.0 | 3,553 ± 76.7 |
| httpx         |   67.1 ± 1.5 |  120.4 ± 3.1 |   658.8 ± 16.6 |    1,084 ± 6.3 |  108.1 ± 1.9 |
| numpy         | 395.2 ± 15.6 |  565.2 ± 9.9 | 80,800 ± 487.7 |   8,102 ± 95.3 |       failed |
| fastapi       |   89.9 ± 3.0 |  299.5 ± 3.7 |   1,141 ± 13.2 |   2,175 ± 24.0 |  196.0 ± 2.6 |
| sqlalchemy    | 280.7 ± 12.7 |  306.3 ± 6.3 |    2,666 ± 6.7 |   4,862 ± 29.7 |  675.1 ± 8.7 |
| rich          |   64.2 ± 3.1 |  122.8 ± 3.2 |    1,002 ± 8.3 |   1,776 ± 56.7 |  135.9 ± 2.9 |
| django        |  248.2 ± 8.9 |  261.7 ± 2.2 |   1,455 ± 12.0 |   6,321 ± 44.7 |  520.4 ± 7.6 |
| sympy         | 739.7 ± 20.2 |  528.9 ± 9.5 |   5,173 ± 26.2 | 13,876 ± 122.4 | 1,241 ± 13.0 |
| openai        | 290.1 ± 16.0 | 456.6 ± 12.1 |   5,669 ± 35.8 |   5,808 ± 61.2 |  882.6 ± 6.5 |
| pytest        | 164.6 ± 15.3 | 235.0 ± 17.3 |   1,319 ± 21.5 |   2,708 ± 11.8 |  602.6 ± 4.4 |

## CLI peak RSS

Mean peak RSS from the same Hyperfine runs, in MiB. On macOS this uses
`wait4`/`ru_maxrss` and **does not sum concurrent worker processes**. In particular,
mypy and Pyright values are not total process-tree memory. The LSP suites measure
latency only.

| Project       |    ty | Pyrefly |  mypy | Pyright |  Zuban |
| ------------- | ----: | ------: | ----: | ------: | -----: |
| black         | 136.8 |   160.0 | 106.5 |   289.6 |   79.3 |
| discord.py    | 223.5 |   216.5 | 212.1 |   432.1 |  103.8 |
| homeassistant | 3,497 |   3,031 | 1,234 |   1,899 |  1,943 |
| isort         |  90.5 |   103.8 |  89.8 |   263.8 |   55.7 |
| jinja         |  99.9 |   116.0 |  90.4 |   257.0 |   60.7 |
| pandas        | 588.0 |   570.4 | 573.9 |   753.3 |  306.4 |
| pandas-stubs  | 157.9 |   273.9 | 389.4 |   381.0 |   95.9 |
| prefect       | 223.3 |   293.7 | 439.7 |   571.8 |  224.5 |
| pytorch       | 1,646 |   904.9 | 1,667 |   1,746 |  749.6 |
| httpx         | 105.5 |   129.8 |  96.6 |   258.1 |   66.2 |
| numpy         | 285.5 |   519.2 | 566.4 |   632.9 | failed |
| fastapi       | 142.5 |   194.0 | 133.1 |   333.9 |   89.1 |
| sqlalchemy    | 405.5 |   301.0 | 271.4 |   549.8 |  168.8 |
| rich          | 122.1 |   133.3 | 119.3 |   284.4 |   79.9 |
| django        | 344.6 |   263.1 | 166.7 |   520.6 |  180.6 |
| sympy         | 727.8 |   507.6 | 537.1 |   999.4 |  298.5 |
| openai        | 347.5 |   411.0 | 516.6 |   599.8 |  209.8 |
| pytest        | 247.5 |   245.6 | 151.4 |   378.4 |  166.4 |

## LSP: initial diagnostics

Two warmups and ten measured rounds. Every server opens the same fixture files
and receives the same edit. pandas-stubs has no edit fixture and is omitted.

Initial latency ends at the first diagnostic response for each open file. Push
notifications can be empty or partial, so this does not establish completion of
all background analysis.

| Project       |          ty |      Pyrefly |      Pyright |         Zuban |
| ------------- | ----------: | -----------: | -----------: | ------------: |
| black         |  67.8 ± 0.1 |  180.5 ± 0.4 |  300.9 ± 0.7 |    71.2 ± 1.5 |
| discord.py    | 104.7 ± 0.4 |  188.4 ± 0.3 | 630.3 ± 12.7 |   180.0 ± 2.1 |
| homeassistant | 101.6 ± 1.5 |  237.7 ± 1.0 | 1,905 ± 10.8 |   217.1 ± 1.7 |
| isort         |  50.3 ± 0.4 |  134.1 ± 6.0 |  358.1 ± 1.4 |    41.3 ± 1.4 |
| jinja         |  51.5 ± 0.1 |  126.4 ± 0.4 |  356.4 ± 2.3 |    87.0 ± 0.7 |
| pandas        | 371.4 ± 2.6 |  543.9 ± 7.0 |  639.1 ± 5.7 |   673.8 ± 4.5 |
| prefect       | 176.5 ± 0.3 | 452.5 ± 42.1 | 1,113 ± 10.0 |   863.4 ± 2.3 |
| pytorch       |  71.7 ± 0.2 | 128.7 ± 14.0 |  705.5 ± 2.5 |   1,836 ± 9.9 |
| httpx         |  46.5 ± 0.1 |  115.3 ± 1.2 |  226.4 ± 1.1 |    70.3 ± 0.7 |
| numpy         | 308.3 ± 1.3 |  564.4 ± 1.4 |  1,200 ± 9.0 | 36,194 ± 98.9 |
| fastapi       | 102.0 ± 3.3 |  200.4 ± 0.6 |  465.9 ± 4.0 |   173.5 ± 1.8 |
| sqlalchemy    | 216.3 ± 0.6 |  251.9 ± 1.7 |  272.7 ± 1.6 |   386.9 ± 4.6 |
| rich          |  43.1 ± 0.4 |  111.0 ± 5.6 |  311.3 ± 1.3 |    80.8 ± 0.8 |
| django        |  41.1 ± 0.1 |   94.2 ± 2.2 |  593.7 ± 8.7 |    46.3 ± 0.7 |
| sympy         |  75.4 ± 0.1 |  180.5 ± 1.1 |  396.7 ± 2.8 |   266.0 ± 4.5 |
| openai        |  70.6 ± 0.4 |  199.4 ± 5.1 |  515.8 ± 2.2 |   141.1 ± 1.4 |
| pytest        |  79.0 ± 0.2 |  185.1 ± 1.0 |  290.7 ± 0.8 |   134.2 ± 1.1 |

## LSP: incremental edit

Two warmups and ten measured rounds. Every server opens the same fixture files
and receives the same edit. pandas-stubs has no edit fixture and is omitted.

| Project       |         ty |     Pyrefly |      Pyright |        Zuban |
| ------------- | ---------: | ----------: | -----------: | -----------: |
| black         | 16.2 ± 0.7 |  91.4 ± 3.0 |  549.4 ± 6.7 |   19.4 ± 0.6 |
| discord.py    | 25.7 ± 0.5 |  76.5 ± 3.8 | 517.2 ± 16.5 | server error |
| homeassistant | 30.0 ± 0.3 |  75.7 ± 8.1 |  574.5 ± 5.0 |   57.0 ± 0.4 |
| isort         | 21.4 ± 0.2 |  52.9 ± 4.5 |  425.1 ± 2.9 |    5.7 ± 0.1 |
| jinja         | 12.3 ± 0.6 |  60.3 ± 4.6 | 503.9 ± 14.2 |   20.1 ± 0.1 |
| pandas        | 43.8 ± 2.2 | 248.6 ± 4.2 | 691.2 ± 11.7 |  254.1 ± 2.2 |
| prefect       |  8.0 ± 0.2 |  56.3 ± 3.5 | 680.9 ± 10.5 |  132.0 ± 0.4 |
| pytorch       |  4.0 ± 0.1 |  22.8 ± 1.9 |  416.3 ± 2.2 | server error |
| httpx         |  7.5 ± 0.2 |  51.7 ± 2.8 | 426.5 ± 10.5 |    9.9 ± 0.6 |
| numpy         | 29.8 ± 0.4 | 343.8 ± 6.4 | 1,188 ± 10.3 | server error |
| fastapi       |  7.3 ± 0.2 |  65.8 ± 3.4 |  614.2 ± 5.6 |    8.5 ± 0.1 |
| sqlalchemy    | 11.6 ± 0.2 |  76.4 ± 8.0 |  639.1 ± 5.7 |  199.6 ± 1.0 |
| rich          |  5.9 ± 0.2 |  31.1 ± 7.2 |  440.8 ± 4.4 |   13.1 ± 0.6 |
| django        |  4.0 ± 0.1 |  25.5 ± 3.2 | 354.1 ± 21.4 |    1.8 ± 0.1 |
| sympy         |  3.4 ± 0.1 |  33.1 ± 3.0 |  479.8 ± 7.3 |   63.8 ± 1.3 |
| openai        |  4.1 ± 0.1 |  82.7 ± 5.1 |  478.8 ± 8.7 |    3.5 ± 0.1 |
| pytest        |  9.0 ± 0.2 |  58.5 ± 2.2 |  481.3 ± 8.7 |   26.3 ± 0.2 |

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
| django        |    907 |     0 |                                  0.0% |
| sympy         |    835 |     0 |                                  0.0% |
| openai        |  2,053 |     0 |                                  0.0% |
| pytest        |    172 |     0 |                                  0.0% |

Zuban reports a syntax error for a module-level type-ignore in PyTorch’s 13-line
`torch/_dynamo/backends/tensorrt.py` placeholder. It contains no executable
implementation body; this negligible checker difference is retained. SQLAlchemy’s
`util/cython.py` shadows `int`, so its ordinary diagnostics supplement the
assignment-marker root audit.

## Project revisions

| Project       | Revision                                   |
| ------------- | ------------------------------------------ |
| black         | `55996d1fb8342725c8a19b6023cd9439c3c1d6f7` |
| discord.py    | `65232c38702be5844cf2ce865a4777eb1928b5d0` |
| homeassistant | `c19ae285ede74cd64c3045a3a4aa43290c224f1b` |
| isort         | `a514c71ed86c2216d0040c7d60e302ed76a4f7ab` |
| jinja         | `5ef70112a1ff19c05324ff889dd30405b1002044` |
| pandas        | `a0225b65720018f4654390bb16d254daa6ee5e54` |
| pandas-stubs  | `8dd6d91b1c05b26e30f7ddbe3dc3d4042a92bdd6` |
| prefect       | `a9452ac21852755311913cb27887b083b5007c03` |
| pytorch       | `ab92945cea42e47ae398aead69af0872d340ea0f` |
| httpx         | `b5addb64f0161ff6bfe94c124ef76f6a1fba5254` |
| numpy         | `f9f1772ce010001208475f751d19253469788410` |
| fastapi       | `7a0a3f0b286c6c865cf4398ea0e957a87b8bffa4` |
| sqlalchemy    | `10f4d1e2d706a7722ca78e79ce05b00333a7aa5b` |
| rich          | `9d8f9a372cc5916fd4781fec207ced7ddac2f08f` |
| django        | `b501b8493f31cf8cba31211d59b3b78642b8cb02` |
| sympy         | `85d3998a4517ffbc8a9709b8efa769bb417c174a` |
| openai        | `f6e8480f9a5b2a4d02b17a1da54a1e57964bc312` |
| pytest        | `8b005ed7f972987033ec34dc1e68b0635fb8142b` |

## Failed cases

- LSP `test_incremental_edit[updated-discord.py-zuban]`: server/test failure; no timing published.
- LSP `test_incremental_edit[updated-pytorch-zuban]`: server/test failure; no timing published.
- CLI `numpy` / Zuban: Untimed root preflight failed or timed out; no timing published.
- LSP `test_incremental_edit[updated-numpy-zuban]`: server/test failure; no timing published.

For each metric, the averages below include only projects where every checker
in that comparison completed the benchmark.

## Comparison with ty

Geometric mean of competitor time divided by ty time on the common successful
projects for each metric. A value above 1 means ty is faster.

| Metric      | Common projects | Pyrefly |   mypy | Pyright | Zuban |
| ----------- | --------------: | ------: | -----: | ------: | ----: |
| cli         |              17 |   1.54× | 12.39× |  20.64× | 2.47× |
| initial     |              17 |   2.16× |      — |   5.53× | 2.66× |
| incremental |              14 |   6.19× |      — |  52.10× | 2.31× |

Performance varies with hardware, dependencies and background load. Matching
root scope and settings does not establish equivalent inference or diagnostic
quality. Earlier datasets with different workloads or worker settings are not
directly comparable.
