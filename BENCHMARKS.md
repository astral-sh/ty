# Benchmarks

Computed on October 29–30, 2026 (UTC), on macOS 26.5.2 with an Apple M3 Max (16 cores,
128 GB RAM).

All projects except Rich were measured on October 29. Rich was measured
in two passes on October 30 with the same benchmark settings.
Collection times and raw-result hashes are recorded separately for Rich.

These results retain the existing revisions for the original nine projects and
add HTTPX, NumPy, FastAPI, SQLAlchemy, and Rich. The five additions use identical
source revisions in both cohorts. Project dependencies were resolved with the cutoff
`2026-10-24T19:50:00Z`. Times are mean ± standard deviation in milliseconds.

Detailed statistics, repetition counts, tool versions, and exact revisions are
available in [BENCHMARKS.json](BENCHMARKS.json).

- ty: 0.0.94, built with `cargo build --release --bin ty --locked` from the
    [release source archive](https://github.com/astral-sh/ty/releases/tag/0.0.94),
    which contains Ruff commit `3937a41cabc973efd859800cc68bef96f62fbf45`.
- Pyrefly: 1.4.0
- Pyright: 1.1.414
- mypy: 2.4.0
- hyperfine: 2.0.0
- uv: 0.13.5
- Node.js: 26.12.1; npm: 12.2.1
- Harness Python: 3.15.1. Project environments use Python 3.11.17, except Home
    Assistant, which uses Python 3.14.9, and NumPy, which uses Python 3.12.15.

For run instructions, see [`ty_benchmark/README.md`](https://github.com/astral-sh/ruff/blob/73eaa13076c8df139c980d71c34d378d9048c812/scripts/ty_benchmark/README.md).

NumPy checks Python and stub sources with tests excluded; its C extensions are
not built. SQLAlchemy adds a typed ORM and SQL expression workload.
Rich checks its Python package, including optional notebook integrations.

## CLI cold check

Three warmups and at least ten measured runs. The mypy cache is cleared before
every run.

| Project       |            ty |      Pyrefly |           mypy |        Pyright |
| ------------- | ------------: | -----------: | -------------: | -------------: |
| black         |    80.0 ± 3.8 |  124.2 ± 2.8 |    893.3 ± 2.6 |   1,378 ± 11.3 |
| discord.py    |   183.7 ± 4.5 |  175.6 ± 4.6 |    2,067 ± 8.1 |   3,064 ± 28.4 |
| homeassistant | 2,785 ± 234.0 | 2,020 ± 29.0 | 23,392 ± 131.0 | 27,168 ± 332.0 |
| isort         |   105.2 ± 1.2 |  104.5 ± 1.2 |   454.1 ± 16.8 |    2,499 ± 9.5 |
| jinja         |    66.2 ± 1.4 |  105.3 ± 1.3 |    530.9 ± 3.2 |   1,276 ± 10.4 |
| pandas        |  483.8 ± 15.2 | 786.4 ± 59.8 |   9,489 ± 40.8 |   6,484 ± 55.6 |
| pandas-stubs  |    99.2 ± 3.3 |  195.9 ± 2.7 |   4,824 ± 20.8 |   2,429 ± 27.7 |
| prefect       |   134.3 ± 5.2 |  254.6 ± 9.8 |    493.5 ± 7.8 |   3,840 ± 42.5 |
| pytorch       |  1,431 ± 46.0 | 1,026 ± 17.0 |  22,319 ± 45.0 | 15,018 ± 140.0 |
| httpx         |    71.7 ± 1.4 |  120.8 ± 2.7 |    860.8 ± 3.8 |   1,087 ± 16.5 |
| numpy         | 2,462 ± 208.0 | 1,523 ± 31.0 | 80,798 ± 632.0 |   8,848 ± 91.0 |
| fastapi       |   106.8 ± 2.0 |  301.1 ± 3.7 |   1,906 ± 21.2 |   2,163 ± 23.3 |
| sqlalchemy    |  382.9 ± 19.2 |  319.0 ± 9.5 |   3,058 ± 19.0 |   4,382 ± 45.3 |
| rich          |    74.0 ± 3.1 |  118.3 ± 2.7 |    1,104 ± 8.2 |   1,744 ± 44.2 |

## CLI peak RSS

Mean peak resident set size across the same measured CLI runs, collected by
[Hyperfine 2.0](https://github.com/sharkdp/hyperfine/releases/tag/v2.0.0). Values
retain the precision of its terminal summaries; GiB values are rounded to 0.1 GiB.

On macOS, Hyperfine uses [`ru_maxrss`](https://github.com/sharkdp/hyperfine/blob/v2.0.0/src/timer/unix_timer.rs).
This metric does not sum concurrent worker RSS; Pyright runs with `--threads`.
The LSP suites below measure latency.

| Project       |        ty |   Pyrefly |      mypy |   Pyright |
| ------------- | --------: | --------: | --------: | --------: |
| black         | 130.5 MiB | 155.7 MiB | 196.3 MiB | 291.4 MiB |
| discord.py    | 228.6 MiB | 216.0 MiB | 279.0 MiB | 429.3 MiB |
| homeassistant |   3.1 GiB |   2.5 GiB |   1.8 GiB |   1.6 GiB |
| isort         |  91.6 MiB | 104.0 MiB | 122.2 MiB | 296.2 MiB |
| jinja         |  99.9 MiB | 116.4 MiB | 137.2 MiB | 257.6 MiB |
| pandas        | 572.6 MiB | 558.1 MiB | 922.0 MiB | 734.0 MiB |
| pandas-stubs  | 155.5 MiB | 273.5 MiB | 608.9 MiB | 386.4 MiB |
| prefect       | 222.5 MiB | 292.4 MiB | 134.7 MiB | 572.7 MiB |
| pytorch       |   1.5 GiB |   0.8 GiB |   1.6 GiB |   1.3 GiB |
| httpx         | 102.4 MiB | 129.9 MiB | 190.5 MiB | 261.5 MiB |
| numpy         | 520.9 MiB | 681.8 MiB | 644.0 MiB | 673.4 MiB |
| fastapi       | 142.7 MiB | 193.4 MiB | 336.9 MiB | 332.5 MiB |
| sqlalchemy    | 422.6 MiB | 295.7 MiB | 370.3 MiB | 544.4 MiB |
| rich          | 120.2 MiB | 133.9 MiB | 226.5 MiB | 286.0 MiB |

## LSP: initial diagnostics

Two warmups and ten measured rounds per project and checker.

| Project       |          ty |      Pyrefly |      Pyright |
| ------------- | ----------: | -----------: | -----------: |
| black         |  63.8 ± 0.2 |  169.8 ± 1.2 |  292.7 ± 1.6 |
| discord.py    | 106.2 ± 0.4 |  187.3 ± 0.7 |  627.1 ± 6.9 |
| homeassistant |  94.0 ± 0.4 |  219.4 ± 3.9 | 1,677 ± 11.5 |
| isort         |  50.6 ± 0.2 |   95.6 ± 2.9 |  354.2 ± 2.1 |
| jinja         |  53.8 ± 0.6 |  129.8 ± 3.5 |  354.3 ± 3.6 |
| pandas        | 354.5 ± 3.2 |  528.9 ± 1.7 |  628.5 ± 8.6 |
| prefect       | 171.9 ± 3.3 | 433.2 ± 54.1 |  1,101 ± 5.9 |
| pytorch       |  57.2 ± 0.2 | 116.3 ± 12.6 |  694.0 ± 2.6 |
| httpx         |  48.0 ± 0.3 |  114.0 ± 0.5 |  226.7 ± 1.2 |
| numpy         | 510.0 ± 1.7 |  566.3 ± 2.5 |  1,193 ± 8.5 |
| fastapi       | 101.3 ± 0.6 |  204.7 ± 5.1 |  471.0 ± 4.5 |
| sqlalchemy    | 216.8 ± 1.4 |  246.3 ± 0.5 |  273.4 ± 1.7 |
| rich          |  43.6 ± 0.1 |  103.2 ± 5.2 |  316.3 ± 3.8 |

## LSP: incremental edit

Two warmups and ten measured rounds per project and checker. pandas-stubs has no
edit fixture and is omitted from both LSP suites.

| Project       |         ty |     Pyrefly |      Pyright |
| ------------- | ---------: | ----------: | -----------: |
| black         | 16.1 ± 0.2 |  80.0 ± 6.0 |  504.5 ± 5.3 |
| discord.py    | 27.1 ± 0.1 |  78.3 ± 3.9 | 517.2 ± 14.2 |
| homeassistant | 29.9 ± 0.3 |  74.5 ± 8.9 |  580.4 ± 3.4 |
| isort         | 23.7 ± 0.2 |  45.9 ± 2.8 |  421.1 ± 8.0 |
| jinja         | 12.7 ± 0.2 |  63.9 ± 4.1 |  502.7 ± 9.7 |
| pandas        | 50.6 ± 0.9 | 230.3 ± 5.7 | 592.4 ± 10.1 |
| prefect       |  7.9 ± 0.1 |  57.7 ± 4.2 |  674.4 ± 7.8 |
| pytorch       |  4.0 ± 0.1 |  22.8 ± 2.0 | 403.6 ± 10.3 |
| httpx         |  8.3 ± 0.1 |  49.8 ± 7.0 | 425.0 ± 10.2 |
| numpy         | 35.8 ± 0.7 | 345.6 ± 3.7 | 1,226 ± 43.3 |
| fastapi       |  8.1 ± 0.1 |  67.6 ± 3.2 |  617.6 ± 1.5 |
| sqlalchemy    | 12.7 ± 0.4 |  79.1 ± 3.1 |  634.9 ± 8.5 |
| rich          |  6.2 ± 0.1 |  38.5 ± 4.3 |  441.2 ± 8.4 |

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

Performance varies with hardware, operating system, dependencies, and background
load. Checkers can produce different diagnostics and do different amounts of work.
Comparisons with earlier published results also include tool and runtime changes.
