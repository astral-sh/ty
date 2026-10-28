# Benchmarks

Computed on October 28, 2026 (UTC), on macOS 26.5.2 with an Apple M3 Max (16 cores,
128 GB RAM).

These results retain the existing project revisions while updating the checkers
and benchmark tools. Project dependencies were resolved with the cutoff
`2026-10-24T19:50:00Z`. Times are mean ± standard deviation in milliseconds.

Detailed statistics, repetition counts, tool versions, and exact revisions are
available in [BENCHMARKS.json](BENCHMARKS.json).

- ty: 0.0.93, built with `cargo build --release --bin ty --locked` from the
    [release source archive](https://github.com/astral-sh/ty/releases/tag/0.0.93),
    which contains Ruff commit `48630fbedd706272d489f81bbcb308b27feb4174`.
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

| Project       |           ty |      Pyrefly |          mypy |        Pyright |
| ------------- | -----------: | -----------: | ------------: | -------------: |
| black         |   78.9 ± 2.9 |  122.9 ± 2.7 |   890.0 ± 4.8 |   1,382 ± 13.2 |
| discord.py    |  183.7 ± 5.1 |  175.0 ± 4.6 |  2,080 ± 15.0 |   3,069 ± 36.3 |
| homeassistant | 2,541 ± 20.0 | 2,011 ± 28.0 | 23,377 ± 86.0 | 27,055 ± 220.0 |
| isort         |  105.5 ± 2.3 |  104.7 ± 2.0 |  445.8 ± 14.0 |   2,501 ± 16.0 |
| jinja         |   66.4 ± 1.1 |  104.6 ± 1.0 |   533.4 ± 5.0 |    1,286 ± 9.8 |
| pandas        | 482.3 ± 19.7 | 833.5 ± 35.6 |  9,502 ± 22.3 |   6,456 ± 67.4 |
| pandas-stubs  |  101.0 ± 7.1 |  195.5 ± 2.3 |  4,809 ± 16.7 |   2,395 ± 36.3 |
| prefect       |  132.8 ± 6.2 |  255.8 ± 8.5 |   492.4 ± 4.2 |   3,821 ± 38.5 |
| pytorch       | 1,436 ± 59.0 | 1,020 ± 18.0 | 22,329 ± 68.0 |  14,986 ± 93.0 |

## CLI peak RSS

Mean peak resident set size across the same measured CLI runs, collected by
[Hyperfine 2.0](https://github.com/sharkdp/hyperfine/releases/tag/v2.0.0). Values
retain the precision of its terminal summaries; GiB values are rounded to 0.1 GiB.

On macOS, Hyperfine uses [`ru_maxrss`](https://github.com/sharkdp/hyperfine/blob/v2.0.0/src/timer/unix_timer.rs).
This metric does not sum concurrent worker RSS; Pyright runs with `--threads`.
The LSP suites below measure latency.

| Project       |        ty |   Pyrefly |      mypy |   Pyright |
| ------------- | --------: | --------: | --------: | --------: |
| black         | 130.4 MiB | 156.0 MiB | 196.3 MiB | 289.0 MiB |
| discord.py    | 228.8 MiB | 216.6 MiB | 278.7 MiB | 436.2 MiB |
| homeassistant |   3.1 GiB |   2.5 GiB |   1.8 GiB |   1.6 GiB |
| isort         |  91.8 MiB | 104.2 MiB | 122.2 MiB | 290.8 MiB |
| jinja         | 100.2 MiB | 116.1 MiB | 137.3 MiB | 255.3 MiB |
| pandas        | 575.8 MiB | 556.4 MiB | 924.9 MiB | 719.2 MiB |
| pandas-stubs  | 155.9 MiB | 273.4 MiB | 608.8 MiB | 383.8 MiB |
| prefect       | 222.8 MiB | 292.3 MiB | 134.6 MiB | 560.5 MiB |
| pytorch       |   1.5 GiB |   0.8 GiB |   1.6 GiB |   1.4 GiB |

## LSP: initial diagnostics

Two warmups and ten measured rounds per project and checker.

| Project       |          ty |      Pyrefly |      Pyright |
| ------------- | ----------: | -----------: | -----------: |
| black         |  65.2 ± 2.5 |  169.7 ± 0.9 |  293.4 ± 1.3 |
| discord.py    | 106.3 ± 0.6 |  189.0 ± 0.6 | 632.4 ± 10.7 |
| homeassistant |  94.3 ± 0.5 |  215.5 ± 0.7 | 1,672 ± 12.0 |
| isort         |  50.8 ± 0.4 |   97.3 ± 4.5 |  353.3 ± 1.7 |
| jinja         |  53.8 ± 0.3 |  123.9 ± 0.4 |  353.8 ± 3.7 |
| pandas        | 355.4 ± 1.6 |  529.8 ± 2.2 |  624.5 ± 6.2 |
| prefect       | 169.5 ± 0.9 |  458.7 ± 1.8 |  1,103 ± 4.4 |
| pytorch       |  57.3 ± 0.2 | 117.3 ± 13.0 |  692.8 ± 3.7 |

## LSP: incremental edit

Two warmups and ten measured rounds per project and checker. pandas-stubs has no
edit fixture and is omitted from both LSP suites.

| Project       |         ty |     Pyrefly |      Pyright |
| ------------- | ---------: | ----------: | -----------: |
| black         | 16.3 ± 0.2 |  79.5 ± 4.6 |  502.3 ± 3.8 |
| discord.py    | 27.4 ± 0.2 |  76.7 ± 3.5 | 522.9 ± 14.0 |
| homeassistant | 30.0 ± 0.4 |  78.0 ± 4.3 |  580.1 ± 5.5 |
| isort         | 24.0 ± 0.2 |  44.8 ± 3.3 |  423.6 ± 6.0 |
| jinja         | 12.6 ± 0.1 |  61.8 ± 3.8 | 507.0 ± 12.7 |
| pandas        | 50.3 ± 0.9 | 233.2 ± 4.1 |  598.3 ± 7.7 |
| prefect       |  7.7 ± 0.1 |  57.3 ± 4.1 |  677.7 ± 4.7 |
| pytorch       |  3.9 ± 0.1 |  22.9 ± 1.7 |  406.2 ± 8.8 |

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
