# Benchmarks

Computed on October 28, 2026 (UTC), on macOS 26.5.2 with an Apple M3 Max (16 cores,
128 GB RAM).

These results retain the existing project revisions while updating the checkers
and benchmark tools. Project dependencies were resolved with the cutoff
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
    Assistant, which uses Python 3.14.9.

For run instructions, see [`ty_benchmark/README.md`](https://github.com/astral-sh/ruff/blob/94c7eca033ab0e8a45be87b670f0fede91b5470b/scripts/ty_benchmark/README.md).

## CLI cold check

Three warmups and at least ten measured runs. The mypy cache is cleared before
every run.

| Project       |           ty |      Pyrefly |           mypy |        Pyright |
| ------------- | -----------: | -----------: | -------------: | -------------: |
| black         |   81.5 ± 2.9 |  125.3 ± 2.5 |   917.3 ± 10.4 |   1,420 ± 13.6 |
| discord.py    |  184.7 ± 6.1 |  177.9 ± 4.2 |   2,128 ± 15.2 |   3,187 ± 54.2 |
| homeassistant | 2,621 ± 15.0 | 2,010 ± 31.0 | 23,756 ± 106.0 | 27,876 ± 139.0 |
| isort         |  106.3 ± 1.7 |  105.4 ± 1.8 |    446.9 ± 3.4 |   2,535 ± 31.9 |
| jinja         |   66.3 ± 0.8 |  105.2 ± 1.6 |    538.1 ± 5.5 |   1,333 ± 19.7 |
| pandas        | 506.4 ± 20.2 | 838.9 ± 43.4 |   9,718 ± 53.6 |   6,796 ± 90.4 |
| pandas-stubs  |  100.8 ± 3.3 |  197.6 ± 3.1 |   4,900 ± 30.6 |   2,449 ± 22.0 |
| prefect       |  136.9 ± 7.6 |  256.6 ± 4.8 |    501.0 ± 8.8 |   3,969 ± 52.9 |
| pytorch       | 1,509 ± 67.0 | 1,024 ± 22.0 |  22,688 ± 75.0 | 15,748 ± 147.0 |

## CLI peak RSS

Mean peak resident set size across the same measured CLI runs, collected by
[Hyperfine 2.0](https://github.com/sharkdp/hyperfine/releases/tag/v2.0.0). Values
retain the precision of its terminal summaries; GiB values are rounded to 0.1 GiB.

On macOS, Hyperfine uses [`ru_maxrss`](https://github.com/sharkdp/hyperfine/blob/v2.0.0/src/timer/unix_timer.rs).
This metric does not sum concurrent worker RSS; Pyright runs with `--threads`.
The LSP suites below measure latency.

| Project       |        ty |   Pyrefly |      mypy |   Pyright |
| ------------- | --------: | --------: | --------: | --------: |
| black         | 130.2 MiB | 156.0 MiB | 196.4 MiB | 290.1 MiB |
| discord.py    | 228.6 MiB | 216.1 MiB | 279.1 MiB | 429.8 MiB |
| homeassistant |   3.1 GiB |   2.5 GiB |   1.8 GiB |   1.6 GiB |
| isort         |  91.5 MiB | 104.1 MiB | 122.1 MiB | 299.0 MiB |
| jinja         | 100.1 MiB | 116.0 MiB | 137.2 MiB | 258.1 MiB |
| pandas        | 572.9 MiB | 554.4 MiB | 922.4 MiB | 747.2 MiB |
| pandas-stubs  | 155.3 MiB | 273.8 MiB | 608.7 MiB | 390.6 MiB |
| prefect       | 222.4 MiB | 292.3 MiB | 134.8 MiB | 562.3 MiB |
| pytorch       |   1.5 GiB |   0.8 GiB |   1.6 GiB |   1.4 GiB |

## LSP: initial diagnostics

Two warmups and ten measured rounds per project and checker.

| Project       |          ty |      Pyrefly |      Pyright |
| ------------- | ----------: | -----------: | -----------: |
| black         |  64.6 ± 0.3 |  171.9 ± 1.2 |  298.7 ± 3.5 |
| discord.py    | 108.5 ± 0.4 |  193.3 ± 2.0 |  638.7 ± 8.1 |
| homeassistant |  95.1 ± 1.0 |  219.1 ± 1.3 | 1,683 ± 25.3 |
| isort         |  52.2 ± 0.6 |  100.6 ± 4.7 |  360.6 ± 2.0 |
| jinja         |  54.9 ± 0.5 |  127.7 ± 0.8 |  363.9 ± 2.0 |
| pandas        | 366.9 ± 3.4 |  534.4 ± 1.9 |  641.2 ± 7.4 |
| prefect       | 172.2 ± 0.6 |  463.1 ± 1.5 |  1,119 ± 6.5 |
| pytorch       |  58.4 ± 0.4 | 127.2 ± 13.6 |  704.7 ± 4.9 |

## LSP: incremental edit

Two warmups and ten measured rounds per project and checker. pandas-stubs has no
edit fixture and is omitted from both LSP suites.

| Project       |         ty |     Pyrefly |      Pyright |
| ------------- | ---------: | ----------: | -----------: |
| black         | 16.9 ± 1.1 |  84.5 ± 1.5 |  511.5 ± 3.9 |
| discord.py    | 28.4 ± 0.4 |  81.4 ± 3.6 |  516.7 ± 2.7 |
| homeassistant | 30.8 ± 0.3 |  82.8 ± 1.0 | 580.2 ± 10.6 |
| isort         | 24.6 ± 0.5 |  47.6 ± 0.7 |  431.9 ± 4.3 |
| jinja         | 13.4 ± 0.2 |  65.7 ± 3.0 |  531.9 ± 9.1 |
| pandas        | 52.3 ± 0.8 | 238.2 ± 4.1 |  615.7 ± 9.8 |
| prefect       |  8.2 ± 0.1 |  59.3 ± 2.5 |  684.6 ± 3.1 |
| pytorch       |  4.2 ± 0.1 |  24.3 ± 2.2 |  409.0 ± 9.0 |

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

Performance varies with hardware, operating system, dependencies, and background
load. Checkers can produce different diagnostics and do different amounts of work.
Comparisons with earlier published results also include tool and runtime changes.
