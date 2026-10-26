# Benchmarks

Computed on October 26, 2026, on macOS 26.5.2 with an Apple M3 Max (16 cores,
128 GB RAM).

These results retain the existing project revisions while updating the checkers
and benchmark tools. Project dependencies were resolved with the cutoff
`2026-10-24T19:50:00Z`. Times are mean ± standard deviation in milliseconds.

Detailed statistics, repetition counts, tool versions, and exact revisions are
available in [BENCHMARKS.json](BENCHMARKS.json).

- ty: 0.0.92, built with `cargo build --release --bin ty --locked` from the
    [release source archive](https://github.com/astral-sh/ty/releases/tag/0.0.92),
    which contains Ruff commit `e139fbd6e8ddd5a1653d2f2c15c1123c090a3456`.
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

| Project       |            ty |      Pyrefly |           mypy |        Pyright |
| ------------- | ------------: | -----------: | -------------: | -------------: |
| black         |    78.1 ± 3.0 |  123.2 ± 2.5 |    900.6 ± 3.1 |   1,382 ± 18.1 |
| discord.py    |   182.7 ± 4.6 |  176.7 ± 5.6 |   2,076 ± 15.0 |   3,048 ± 23.0 |
| homeassistant | 2,607 ± 122.0 | 2,008 ± 27.0 | 23,310 ± 103.0 | 27,020 ± 247.0 |
| isort         |   129.7 ± 1.4 |  104.7 ± 1.3 |   449.9 ± 26.2 |   2,500 ± 14.8 |
| jinja         |    66.5 ± 1.6 |  105.7 ± 2.0 |    532.5 ± 5.0 |   1,283 ± 16.0 |
| pandas        |  481.4 ± 14.6 | 824.3 ± 52.9 |   9,478 ± 44.0 |   6,454 ± 81.3 |
| pandas-stubs  |   100.6 ± 3.4 |  195.6 ± 2.6 |   4,806 ± 23.5 |   2,396 ± 17.3 |
| prefect       |   133.0 ± 6.4 |  250.0 ± 5.8 |    492.6 ± 4.0 |   3,809 ± 54.4 |
| pytorch       |  1,462 ± 73.0 | 1,017 ± 18.0 |  22,298 ± 63.0 | 14,840 ± 131.0 |

## CLI peak RSS

Mean peak resident set size across the same measured CLI runs, collected by
[Hyperfine 2.0](https://github.com/sharkdp/hyperfine/releases/tag/v2.0.0). Values
retain the precision of its terminal summaries; GiB values are rounded to 0.1 GiB.

On macOS, Hyperfine uses [`ru_maxrss`](https://github.com/sharkdp/hyperfine/blob/v2.0.0/src/timer/unix_timer.rs).
This metric does not sum concurrent worker RSS; Pyright runs with `--threads`.
The LSP suites below measure latency.

| Project       |        ty |   Pyrefly |      mypy |   Pyright |
| ------------- | --------: | --------: | --------: | --------: |
| black         | 131.2 MiB | 155.7 MiB | 196.3 MiB | 292.4 MiB |
| discord.py    | 229.5 MiB | 216.7 MiB | 279.5 MiB | 430.5 MiB |
| homeassistant |   3.1 GiB |   2.5 GiB |   1.8 GiB |   1.6 GiB |
| isort         |  93.4 MiB | 104.2 MiB | 122.2 MiB | 292.8 MiB |
| jinja         | 100.1 MiB | 116.1 MiB | 137.1 MiB | 256.1 MiB |
| pandas        | 572.5 MiB | 553.8 MiB | 920.4 MiB | 758.6 MiB |
| pandas-stubs  | 154.9 MiB | 272.6 MiB | 608.8 MiB | 386.5 MiB |
| prefect       | 222.9 MiB | 292.1 MiB | 134.8 MiB | 575.8 MiB |
| pytorch       |   1.5 GiB |   0.8 GiB |   1.6 GiB |   1.4 GiB |

## LSP: initial diagnostics

Two warmups and ten measured rounds per project and checker.

| Project       |          ty |      Pyrefly |      Pyright |
| ------------- | ----------: | -----------: | -----------: |
| black         |  63.1 ± 0.1 |  168.2 ± 0.5 |  292.9 ± 2.1 |
| discord.py    | 106.7 ± 0.6 |  188.4 ± 1.2 |  626.3 ± 4.6 |
| homeassistant |  94.2 ± 0.7 |  215.8 ± 1.1 | 1,672 ± 13.2 |
| isort         |  51.6 ± 1.1 |   97.9 ± 4.8 |  355.3 ± 3.1 |
| jinja         |  54.9 ± 0.5 |  125.8 ± 0.5 |  356.4 ± 1.0 |
| pandas        | 358.8 ± 1.8 |  529.7 ± 2.5 |  630.3 ± 7.7 |
| prefect       | 174.1 ± 0.6 |  461.0 ± 4.3 |  1,100 ± 2.5 |
| pytorch       |  57.7 ± 0.4 | 115.1 ± 11.2 |  690.6 ± 3.8 |

## LSP: incremental edit

Two warmups and ten measured rounds per project and checker. pandas-stubs has no
edit fixture and is omitted from both LSP suites.

| Project       |         ty |     Pyrefly |      Pyright |
| ------------- | ---------: | ----------: | -----------: |
| black         | 16.4 ± 0.1 |  78.5 ± 3.9 |  502.9 ± 4.1 |
| discord.py    | 27.1 ± 0.3 |  75.3 ± 6.7 |  509.0 ± 7.1 |
| homeassistant | 30.3 ± 1.2 |  77.5 ± 4.0 | 582.4 ± 12.8 |
| isort         | 24.7 ± 1.1 |  45.0 ± 3.1 |  424.5 ± 6.4 |
| jinja         | 13.0 ± 0.4 |  62.1 ± 3.7 | 511.9 ± 13.0 |
| pandas        | 51.0 ± 0.8 | 232.9 ± 4.9 |  598.4 ± 5.6 |
| prefect       |  7.8 ± 0.1 |  57.2 ± 3.6 |  677.1 ± 7.5 |
| pytorch       | 9.4 ± 15.4 |  21.7 ± 2.9 |  409.4 ± 9.9 |

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
