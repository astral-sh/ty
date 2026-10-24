# Benchmarks

Computed on October 24, 2026, on macOS 26.5.2 with an Apple M3 Max (16 cores,
128 GB RAM).

These results retain the existing project revisions while updating the checkers
and benchmark tools. Project dependencies were resolved with the cutoff
`2026-10-24T19:50:00Z`. Times are mean ± standard deviation in milliseconds.

Detailed statistics, repetition counts, tool versions, and exact revisions are
available in [BENCHMARKS.json](BENCHMARKS.json).

- ty: 0.0.91 source, built with `cargo build --release --bin ty --locked` from
    Ruff commit `59a9e85a7b6dc4e4592cd29de32a214c150d663c`. The local binary reports
    `0.0.91+7`.
- Pyrefly: 1.4.0
- Pyright: 1.1.414
- mypy: 2.4.0
- hyperfine: 2.0.0
- uv: 0.13.5
- Node.js: 26.12.1; npm: 12.2.1
- Harness Python: 3.15.1. Project environments use Python 3.11.17, except Home
    Assistant, which uses Python 3.14.9.

For run instructions, see [`ty_benchmark/README.md`](https://github.com/astral-sh/ruff/blob/64cbba5d7babb4bc46a7c674a5903323ae42ab78/scripts/ty_benchmark/README.md).

## CLI cold check

Three warmups and at least ten measured runs. The mypy cache is cleared before
every run.

| Project       |            ty |      Pyrefly |           mypy |        Pyright |
| ------------- | ------------: | -----------: | -------------: | -------------: |
| black         |    79.1 ± 3.0 |  123.7 ± 1.9 |    899.4 ± 3.8 |   1,383 ± 13.6 |
| discord.py    |   171.5 ± 6.3 |  176.4 ± 3.8 |   2,086 ± 18.0 |   3,098 ± 51.2 |
| homeassistant | 2,683 ± 152.0 | 2,044 ± 39.0 | 25,247 ± 502.0 | 27,990 ± 488.0 |
| isort         |   130.9 ± 1.1 |  104.2 ± 1.7 |    443.1 ± 2.1 |   2,514 ± 13.8 |
| jinja         |    64.2 ± 0.9 |  104.4 ± 1.4 |    535.1 ± 3.8 |   1,278 ± 18.6 |
| pandas        |  451.7 ± 18.1 | 834.5 ± 43.2 |  9,858 ± 484.5 |   6,647 ± 90.1 |
| pandas-stubs  |   104.3 ± 3.9 |  196.9 ± 2.5 |   4,873 ± 16.0 |   2,410 ± 23.6 |
| prefect       |   131.5 ± 5.7 |  255.6 ± 9.7 |    494.9 ± 3.6 |   3,876 ± 44.6 |
| pytorch       |  1,305 ± 64.0 | 1,039 ± 21.0 | 22,555 ± 132.0 | 15,388 ± 117.0 |

## LSP: initial diagnostics

Two warmups and ten measured rounds per project and checker.

| Project       |          ty |      Pyrefly |     Pyright |
| ------------- | ----------: | -----------: | ----------: |
| black         |  62.6 ± 1.2 |  162.7 ± 0.5 | 287.8 ± 5.8 |
| discord.py    | 103.7 ± 1.1 |  188.3 ± 0.8 | 621.0 ± 6.0 |
| homeassistant | 302.9 ± 5.5 |  213.9 ± 0.4 | 1,655 ± 6.4 |
| isort         |  55.0 ± 0.7 |   99.6 ± 4.8 | 353.0 ± 1.4 |
| jinja         |  57.3 ± 0.9 |  126.4 ± 0.4 | 359.3 ± 5.3 |
| pandas        | 403.3 ± 0.9 |  529.5 ± 1.4 | 635.2 ± 7.7 |
| prefect       | 177.1 ± 1.1 | 444.8 ± 39.9 | 1,094 ± 4.1 |
| pytorch       | 100.4 ± 1.1 |  111.4 ± 8.6 | 688.3 ± 3.2 |

## LSP: incremental edit

Two warmups and ten measured rounds per project and checker. pandas-stubs has no
edit fixture and is omitted from both LSP suites.

| Project       |         ty |     Pyrefly |      Pyright |
| ------------- | ---------: | ----------: | -----------: |
| black         | 16.0 ± 0.3 |  99.6 ± 2.4 |  519.7 ± 2.0 |
| discord.py    | 25.6 ± 0.2 |  98.4 ± 1.5 | 536.0 ± 11.4 |
| homeassistant | 31.7 ± 1.2 |  98.7 ± 2.1 |  605.7 ± 4.6 |
| isort         | 25.6 ± 0.2 |  64.3 ± 1.9 |  443.8 ± 4.4 |
| jinja         | 13.7 ± 0.6 |  83.4 ± 2.1 | 544.0 ± 10.2 |
| pandas        | 77.6 ± 0.7 | 250.9 ± 2.5 |  604.0 ± 7.2 |
| prefect       |  8.3 ± 0.1 |  76.2 ± 1.6 |  698.5 ± 3.4 |
| pytorch       |  5.6 ± 0.1 |  38.5 ± 1.5 |  427.3 ± 5.9 |

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
