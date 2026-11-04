# Benchmarks

We ran these benchmarks on November 3, 2026, on a 16-core Apple M3 Max
with 128 GB of RAM running macOS 26.5.2.

- [Pyrefly](https://pypi.org/project/pyrefly/) 1.4.0
- [Pyright](https://www.npmjs.com/package/pyright) 1.1.414
- [mypy](https://pypi.org/project/mypy/) 2.4.0 (compiled)
- [ty](https://pypi.org/project/ty/) 0.0.96

For the commands and source revisions, see the [benchmark runner](https://github.com/astral-sh/ruff/blob/5ca55b2baffd6200b61c540c17255d9e20055272/scripts/ty_benchmark/README.md)
and [project definitions](https://github.com/astral-sh/ruff/blob/73eaa13076c8df139c980d71c34d378d9048c812/scripts/ty_benchmark/src/benchmark/projects.py).

## CLI cold check

Each checker discovers the same input files, checks unannotated function bodies,
and can use up to 16 workers. We ran at least ten cold checks after three
warmups, clearing mypy’s cache before each run. Timings below are means ± one
standard deviation in milliseconds.

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

Mean peak resident memory in MiB across the same CLI runs. On macOS, peak RSS
covers a single process, so mypy and Pyright can use more memory across all
their workers.

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

Each server opens the same files. We measure the time to the first diagnostic
response for each file, which can be empty or partial. Both editor benchmarks
use two warmups and ten measured rounds. pandas-stubs has no editor fixture.

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

Each server receives the same edit. We measure how long it takes to report
diagnostics for the affected files.

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

These are the files each checker starts from. A stub takes precedence over the
corresponding implementation, which accounts for most of the omitted lines in
NumPy. The pandas benchmark excludes `pandas/tests`. Checkers may also follow
imports outside these roots.

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

## Comparison with ty

Each value is the geometric mean of the other checker’s time divided by ty’s
time. Each row includes the projects where all checkers in that row finished.
A value above 1 means ty was faster.

| Metric      | Common projects | Pyrefly |   mypy | Pyright |
| ----------- | --------------: | ------: | -----: | ------: |
| cli         |              14 |   1.66× | 16.34× |  21.62× |
| initial     |              13 |   2.08× |      — |   5.34× |
| incremental |              13 |   5.31× |      — |  42.03× |
