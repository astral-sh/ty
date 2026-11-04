# Benchmarks

We ran these benchmarks on November 3, 2026, on a 16-core Apple M3 Max
with 128 GB of RAM running macOS 26.5.2.

- [Pyrefly](https://pypi.org/project/pyrefly/) 1.4.0
- [Pyright](https://www.npmjs.com/package/pyright) 1.1.414
- [mypy](https://pypi.org/project/mypy/) 2.4.0 (compiled)
- [ty](https://pypi.org/project/ty/) 0.0.96

For the commands and source revisions, see the [benchmark runner](https://github.com/astral-sh/ruff/blob/5ca55b2baffd6200b61c540c17255d9e20055272/scripts/ty_benchmark/README.md)
and [project definitions](https://github.com/astral-sh/ruff/blob/8ab47843110fa4333cdcb117febf221db1165fc4/scripts/ty_benchmark/src/benchmark/projects.py).

## CLI cold check

Each checker discovers the same input files, checks unannotated function bodies,
and can use up to 16 workers. We ran at least ten cold checks after three
warmups, clearing mypy’s cache before each run. Timings below are means ± one
standard deviation in milliseconds.

| Project       |           ty |      Pyrefly |           mypy |        Pyright |
| ------------- | -----------: | -----------: | -------------: | -------------: |
| black         |   69.1 ± 3.1 |  134.1 ± 2.6 |   683.8 ± 10.6 |   1,433 ± 25.7 |
| discord.py    |  137.3 ± 6.1 |  176.3 ± 4.0 |   1,981 ± 17.2 |   3,021 ± 34.4 |
| homeassistant | 2,085 ± 10.4 | 2,308 ± 38.7 | 13,599 ± 116.4 | 29,820 ± 104.0 |
| isort         |   91.5 ± 2.3 |  106.7 ± 1.8 |   495.5 ± 11.3 |   1,744 ± 22.0 |
| jinja         |   56.0 ± 1.3 |  105.0 ± 1.2 |   624.3 ± 12.4 |    1,348 ± 6.9 |
| pandas        | 387.8 ± 18.7 |  910.8 ± 7.7 |   7,570 ± 29.5 |   7,797 ± 94.9 |
| pandas-stubs  |   85.7 ± 3.2 |  197.2 ± 2.8 |   3,569 ± 19.5 |   2,240 ± 16.6 |
| prefect       |  111.5 ± 8.1 |  273.9 ± 9.1 |   4,712 ± 18.9 |   3,912 ± 31.0 |
| pytorch       | 1,310 ± 41.2 | 1,225 ± 20.8 |  21,916 ± 70.8 | 18,060 ± 185.0 |
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
| black         | 136.8 |   160.0 | 106.5 |   289.6 |
| discord.py    | 223.5 |   216.5 | 212.1 |   432.1 |
| homeassistant | 3,497 |   3,031 | 1,234 |   1,899 |
| isort         |  90.5 |   103.8 |  89.8 |   263.8 |
| jinja         |  99.9 |   116.0 |  90.4 |   257.0 |
| pandas        | 588.0 |   570.4 | 573.9 |   753.3 |
| pandas-stubs  | 157.9 |   273.9 | 389.4 |   381.0 |
| prefect       | 223.3 |   293.7 | 439.7 |   571.8 |
| pytorch       | 1,646 |   904.9 | 1,667 |   1,746 |
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
| black         |  67.8 ± 0.1 |  180.5 ± 0.4 |  300.9 ± 0.7 |
| discord.py    | 104.7 ± 0.4 |  188.4 ± 0.3 | 630.3 ± 12.7 |
| homeassistant | 101.6 ± 1.5 |  237.7 ± 1.0 | 1,905 ± 10.8 |
| isort         |  50.3 ± 0.4 |  134.1 ± 6.0 |  358.1 ± 1.4 |
| jinja         |  51.5 ± 0.1 |  126.4 ± 0.4 |  356.4 ± 2.3 |
| pandas        | 371.4 ± 2.6 |  543.9 ± 7.0 |  639.1 ± 5.7 |
| prefect       | 176.5 ± 0.3 | 452.5 ± 42.1 | 1,113 ± 10.0 |
| pytorch       |  71.7 ± 0.2 | 128.7 ± 14.0 |  705.5 ± 2.5 |
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
| black         | 16.2 ± 0.7 |  91.4 ± 3.0 |  549.4 ± 6.7 |
| discord.py    | 25.7 ± 0.5 |  76.5 ± 3.8 | 517.2 ± 16.5 |
| homeassistant | 30.0 ± 0.3 |  75.7 ± 8.1 |  574.5 ± 5.0 |
| isort         | 21.4 ± 0.2 |  52.9 ± 4.5 |  425.1 ± 2.9 |
| jinja         | 12.3 ± 0.6 |  60.3 ± 4.6 | 503.9 ± 14.2 |
| pandas        | 43.8 ± 2.2 | 248.6 ± 4.2 | 691.2 ± 11.7 |
| prefect       |  8.0 ± 0.2 |  56.3 ± 3.5 | 680.9 ± 10.5 |
| pytorch       |  4.0 ± 0.1 |  22.8 ± 1.9 |  416.3 ± 2.2 |
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

## Comparison with ty

Each value is the geometric mean of the other checker’s time divided by ty’s
time. Each row includes the projects where all checkers in that row finished.
A value above 1 means ty was faster.

| Metric      | Common projects | Pyrefly |   mypy | Pyright |
| ----------- | --------------: | ------: | -----: | ------: |
| cli         |              14 |   1.67× | 16.61× |  20.84× |
| initial     |              13 |   2.08× |      — |   5.21× |
| incremental |              13 |   5.35× |      — |  41.77× |
