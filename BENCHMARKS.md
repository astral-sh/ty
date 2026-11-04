# Benchmarks

We ran the CLI benchmarks on November 4, 2026 (UTC) and the LSP
benchmarks on November 3, 2026, on a 16-core Apple M3 Max with 128 GB of RAM
running macOS 26.5.2.

- [Pyrefly](https://pypi.org/project/pyrefly/) 1.4.0
- [Pyright](https://www.npmjs.com/package/pyright) 1.1.414
- [mypy](https://pypi.org/project/mypy/) 2.4.0 (compiled)
- [ty](https://pypi.org/project/ty/) 0.0.96
- [Zuban](https://pypi.org/project/zuban/) 0.10.2

For the commands and source revisions, see the [benchmark runner](https://github.com/astral-sh/ruff/blob/f62ae0859ac2ce0bf983b64c414be6fb2fa6f546/scripts/ty_benchmark/README.md)
and [project definitions](https://github.com/astral-sh/ruff/blob/f62ae0859ac2ce0bf983b64c414be6fb2fa6f546/scripts/ty_benchmark/src/benchmark/projects.py).

## CLI cold check

Each checker discovers the same input files and checks unannotated function
bodies. We use one concurrency limit per checker across all projects:
ty 16, Pyrefly 16, mypy 8, Pyright 8, and Zuban 4. The
[concurrency calibration](https://github.com/astral-sh/ruff/blob/f62ae0859ac2ce0bf983b64c414be6fb2fa6f546/scripts/ty_benchmark/concurrency.md) explains the selection and
Home Assistant tradeoffs. We ran at least ten cold checks after three warmups,
clearing mypy’s cache before each run. Timings below are means ± one standard
deviation in milliseconds.

| Project       |           ty |      Pyrefly |           mypy |        Pyright |        Zuban |
| ------------- | -----------: | -----------: | -------------: | -------------: | -----------: |
| black         |   67.9 ± 2.9 |  129.3 ± 2.8 |    633.9 ± 6.6 |   1,099 ± 10.0 |  125.5 ± 0.8 |
| discord.py    |  138.9 ± 3.4 |  174.5 ± 3.2 |   1,919 ± 12.3 |   2,075 ± 21.4 |  330.2 ± 4.8 |
| homeassistant | 2,104 ± 80.9 | 2,296 ± 24.8 |  15,331 ± 63.9 | 33,766 ± 454.9 | 7,004 ± 35.7 |
| isort         |   91.0 ± 1.8 |  106.9 ± 2.1 |    462.0 ± 9.2 |   1,394 ± 15.2 |   54.9 ± 1.0 |
| jinja         |   56.2 ± 1.3 |  104.9 ± 1.4 |    568.1 ± 8.0 |   963.4 ± 24.0 |   69.1 ± 0.4 |
| pandas        | 396.0 ± 20.4 | 887.3 ± 45.5 |   7,453 ± 40.1 |   5,945 ± 52.3 |  1,343 ± 5.3 |
| pandas-stubs  |   84.9 ± 3.4 |  200.1 ± 2.4 |   3,480 ± 19.3 |   1,585 ± 27.4 |  251.1 ± 1.9 |
| prefect       |  113.8 ± 5.8 |  276.0 ± 9.2 |   4,667 ± 47.9 |   2,285 ± 47.6 |  929.5 ± 3.1 |
| pytorch       | 1,281 ± 29.8 | 1,214 ± 22.2 |  21,730 ± 62.9 |  16,409 ± 78.7 | 3,167 ± 20.8 |
| httpx         |   66.6 ± 1.8 |  119.0 ± 3.1 |    588.7 ± 5.8 |    768.1 ± 3.7 |   91.6 ± 0.8 |
| numpy         | 396.0 ± 15.6 | 595.3 ± 22.6 | 80,584 ± 542.1 |   7,617 ± 62.4 |       failed |
| fastapi       |   89.8 ± 2.4 |  298.5 ± 2.2 |   1,056 ± 16.2 |   1,617 ± 14.4 |  168.6 ± 0.9 |
| sqlalchemy    | 289.7 ± 12.7 |  304.4 ± 6.6 |   2,612 ± 18.1 |   3,762 ± 44.7 |  605.7 ± 4.0 |
| rich          |   64.5 ± 2.8 |  122.0 ± 3.6 |    936.5 ± 6.7 |   1,283 ± 20.1 |  110.8 ± 1.1 |
| django        |  241.9 ± 5.2 |  259.0 ± 2.2 |    1,373 ± 7.9 |   4,207 ± 29.2 |  456.7 ± 9.8 |
| sympy         | 718.0 ± 25.0 |  530.0 ± 7.8 |   5,100 ± 23.3 |  11,034 ± 81.2 |  1,117 ± 7.7 |
| openai        | 287.9 ± 16.9 | 457.2 ± 13.0 |   5,550 ± 34.9 |   5,024 ± 66.1 |  814.0 ± 7.3 |
| pytest        | 160.1 ± 17.0 | 240.6 ± 10.7 |    1,244 ± 9.0 |   2,080 ± 23.5 |  548.3 ± 1.6 |

## CLI peak RSS

Mean peak resident memory in MiB across the same CLI runs. On macOS, peak RSS
covers a single process, so mypy and Pyright can use more memory across all
their workers.

| Project       |    ty | Pyrefly |  mypy | Pyright |  Zuban |
| ------------- | ----: | ------: | ----: | ------: | -----: |
| black         | 136.7 |   159.9 | 109.7 |   304.9 |   70.3 |
| discord.py    | 223.1 |   216.3 | 216.5 |   480.0 |   92.9 |
| homeassistant | 3,497 |   3,031 | 1,421 |   2,789 |  1,817 |
| isort         |  90.6 |   103.7 |  90.0 |   265.9 |   47.6 |
| jinja         |  99.9 |   116.1 |  91.7 |   265.9 |   52.2 |
| pandas        | 591.0 |   571.1 | 585.6 |   1,041 |  288.9 |
| pandas-stubs  | 157.8 |   275.2 | 402.1 |   386.7 |   85.8 |
| prefect       | 223.5 |   294.5 | 479.2 |   579.7 |  214.0 |
| pytorch       | 1,642 |   909.8 | 1,664 |   2,306 |  703.3 |
| httpx         | 105.2 |   130.0 | 101.2 |   256.5 |   58.6 |
| numpy         | 284.5 |   518.5 | 567.8 |   699.3 | failed |
| fastapi       | 142.9 |   192.9 | 144.0 |   335.1 |   80.1 |
| sqlalchemy    | 405.3 |   299.3 | 271.2 |   700.5 |  154.3 |
| rich          | 121.7 |   133.9 | 122.1 |   328.0 |   69.8 |
| django        | 344.3 |   262.3 | 168.9 |   599.6 |  160.0 |
| sympy         | 726.4 |   509.2 | 540.9 |   1,318 |  276.8 |
| openai        | 348.9 |   407.9 | 525.3 |   728.3 |  193.5 |
| pytest        | 247.2 |   245.8 | 162.8 |   502.1 |  153.3 |

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
| cli         |              17 |   1.54× | 11.97× |  15.80× | 2.18× |
| initial     |              17 |   2.16× |      — |   5.53× | 2.66× |
| incremental |              14 |   6.19× |      — |  52.10× | 2.31× |
