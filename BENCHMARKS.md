# Benchmarks

We ran the CLI benchmarks on November 4, 2026 (UTC) and the LSP
benchmarks on November 3, 2026, on a 16-core Apple M3 Max with 128 GB of RAM
running macOS 26.5.2.

- [Pyrefly](https://pypi.org/project/pyrefly/) 1.4.0
- [Pyright](https://www.npmjs.com/package/pyright) 1.1.414
- [mypy](https://pypi.org/project/mypy/) 2.4.0 (compiled)
- [ty](https://pypi.org/project/ty/) 0.0.96
- [Zuban](https://pypi.org/project/zuban/) 0.10.2

For the commands and source revisions, see the [benchmark runner](https://github.com/astral-sh/ruff/blob/504457130a2183e9f0c6f4e92ce1c43e970b70ca/scripts/ty_benchmark/README.md)
and [project definitions](https://github.com/astral-sh/ruff/blob/504457130a2183e9f0c6f4e92ce1c43e970b70ca/scripts/ty_benchmark/src/benchmark/projects.py).

## CLI cold check

Each checker discovers the same input files and checks unannotated function
bodies. CLI runs use each checker's default concurrency. On this host, ty,
Pyrefly, and Zuban automatically select 16 pool threads. mypy uses no external
checking workers; its native parser can use up to eight threads. Pyright
checks in one process. We ran at least ten cold checks after three warmups,
clearing mypy’s cache before each run. Timings below are means ± one standard
deviation in milliseconds.

| Project       |           ty |      Pyrefly |           mypy |         Pyright |        Zuban |
| ------------- | -----------: | -----------: | -------------: | --------------: | -----------: |
| black         |   66.9 ± 2.6 |  127.1 ± 1.7 |    921.0 ± 6.9 |    1,663 ± 11.7 |  143.8 ± 2.0 |
| discord.py    |  137.7 ± 5.2 |  173.4 ± 4.5 |   2,086 ± 11.9 |    3,986 ± 13.6 |  356.5 ± 3.5 |
| homeassistant | 2,092 ± 19.2 | 2,303 ± 30.8 | 52,028 ± 457.0 | 126,940 ± 7,192 | 7,454 ± 62.8 |
| isort         |   92.2 ± 1.7 |  105.5 ± 2.0 |    454.6 ± 3.2 |    1,629 ± 11.3 |   66.0 ± 1.4 |
| jinja         |   55.2 ± 1.2 |  104.1 ± 1.4 |    549.0 ± 9.1 |     1,178 ± 6.8 |   84.2 ± 1.6 |
| pandas        | 404.8 ± 27.7 | 888.1 ± 27.7 |  10,469 ± 39.5 |  15,790 ± 102.1 |  1,409 ± 6.2 |
| pandas-stubs  |   84.4 ± 3.5 |  196.0 ± 1.5 |   4,762 ± 45.1 |    2,170 ± 12.8 |  271.0 ± 1.9 |
| prefect       |  111.0 ± 6.2 | 271.4 ± 10.1 |   7,191 ± 91.7 |    2,824 ± 18.5 |  948.1 ± 2.5 |
| pytorch       | 1,313 ± 59.5 | 1,205 ± 14.6 |  25,373 ± 57.5 |  74,008 ± 1,512 | 3,464 ± 20.5 |
| httpx         |   66.4 ± 1.8 |  117.9 ± 2.5 |   901.8 ± 10.3 |    950.0 ± 12.4 |  104.8 ± 1.4 |
| numpy         | 391.9 ± 15.3 | 581.6 ± 29.3 | 80,920 ± 614.9 |   21,217 ± 79.0 |       failed |
| fastapi       |   89.0 ± 2.4 |  297.2 ± 3.5 |   1,953 ± 17.6 |    2,216 ± 11.6 |  191.1 ± 2.3 |
| sqlalchemy    | 289.8 ± 10.5 |  304.0 ± 7.3 |   3,932 ± 32.1 |    9,799 ± 75.7 |  660.8 ± 4.1 |
| rich          |   63.0 ± 3.0 |  122.8 ± 3.4 |   1,209 ± 14.4 |     2,511 ± 8.1 |  130.2 ± 2.3 |
| django        | 253.0 ± 26.2 |  259.8 ± 3.9 |   2,446 ± 17.9 |    6,931 ± 48.4 |  510.8 ± 6.1 |
| sympy         | 720.7 ± 14.5 |  527.0 ± 5.9 |   6,645 ± 28.0 |  30,048 ± 168.2 |  1,230 ± 8.5 |
| openai        | 294.1 ± 12.6 | 464.0 ± 11.7 |   6,770 ± 33.9 |    8,170 ± 67.3 |  861.1 ± 8.9 |
| pytest        | 164.8 ± 12.3 | 227.2 ± 21.9 |   2,381 ± 25.0 |    4,574 ± 29.7 |  590.6 ± 5.4 |

## CLI peak RSS

Mean peak resident memory in MiB across the same CLI runs. Hyperfine 2.0
reports peak process RSS on macOS and does not sum concurrent processes.

| Project       |    ty | Pyrefly |  mypy | Pyright |  Zuban |
| ------------- | ----: | ------: | ----: | ------: | -----: |
| black         | 136.2 |   159.6 | 198.7 |   427.1 |   79.4 |
| discord.py    | 222.9 |   217.2 | 279.5 |   778.9 |  103.6 |
| homeassistant | 3,497 |   3,031 | 4,189 |   4,208 |  1,943 |
| isort         |  90.5 |   103.7 | 120.3 |   293.9 |   55.8 |
| jinja         |  99.7 |   115.9 | 136.7 |   317.7 |   60.7 |
| pandas        | 590.3 |   570.3 | 923.7 |   2,360 |  306.8 |
| pandas-stubs  | 158.0 |   274.3 | 615.6 |   549.1 |   95.9 |
| prefect       | 224.2 |   294.0 | 837.3 |   749.2 |  224.4 |
| pytorch       | 1,646 |   908.9 | 1,845 |   4,179 |  752.5 |
| httpx         | 105.2 |   129.9 | 190.2 |   362.1 |   66.4 |
| numpy         | 284.9 |   518.6 | 642.5 |   1,536 | failed |
| fastapi       | 142.8 |   193.4 | 333.8 |   493.5 |   89.2 |
| sqlalchemy    | 404.2 |   298.7 | 422.6 |   1,429 |  168.8 |
| rich          | 121.6 |   133.5 | 226.2 |   498.1 |   79.7 |
| django        | 345.0 |   262.9 | 324.9 |   1,211 |  180.1 |
| sympy         | 728.0 |   509.3 | 652.8 |   3,323 |  299.8 |
| openai        | 349.3 |   409.3 | 651.0 |   1,424 |  209.5 |
| pytest        | 248.0 |   246.0 | 371.8 |   903.3 |  166.5 |

## LSP: initial diagnostics

Each server opens the same files. We measure the time to the first diagnostic
response for each file, which can be empty or partial. Both editor benchmarks
use two warmups and ten measured rounds. pandas-stubs has no editor fixture.

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

Each server receives the same edit. We measure how long it takes to report
diagnostics for the affected files.

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

Zuban failed the NumPy CLI preflight. Its language server crashed after edits
to discord.py, NumPy, and PyTorch.

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
| django        |    907 |     0 |                                  0.0% |
| sympy         |    835 |     0 |                                  0.0% |
| openai        |  2,053 |     0 |                                  0.0% |
| pytest        |    172 |     0 |                                  0.0% |

## Comparison with ty

Each value is the geometric mean of the other checker’s time divided by ty’s
time. Each row includes the projects where all checkers in that row finished.
A value above 1 means ty was faster.

| Metric      | Common projects | Pyrefly |   mypy | Pyright | Zuban |
| ----------- | --------------: | ------: | -----: | ------: | ----: |
| cli         |              17 |   1.52× | 17.26× |  29.56× | 2.41× |
| initial     |              17 |   2.16× |      — |   5.53× | 2.66× |
| incremental |              14 |   6.19× |      — |  52.10× | 2.31× |
