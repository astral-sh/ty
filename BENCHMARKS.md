# Benchmarks

Computed on October 28, 2026 (UTC), on macOS 26.5.2 with an Apple M3 Max (16 cores,
128 GB RAM).

The existing project revisions were measured first, followed by the updated
upstream revisions with dependencies resolved afresh. Both runs used the same
checker versions, Python versions, and dependency cutoff (`2026-10-24T19:50:00Z`).
Updated project requirements can still change the installed dependencies.

Timing cells show **existing revision → updated revision (percentage change)**.
Times are mean wall-clock milliseconds; negative changes mean faster checks.

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

For run instructions, see [`ty_benchmark/README.md`](https://github.com/astral-sh/ruff/blob/fc1f18e8512333b0fdb970249444686c3dcde100/scripts/ty_benchmark/README.md).

## CLI cold check

Three warmups and at least ten measured runs. The mypy cache is cleared before
every run.

| Project       |                     ty |                Pyrefly |                     mypy |                  Pyright |
| ------------- | ---------------------: | ---------------------: | -----------------------: | -----------------------: |
| black         |    81.5 → 89.4 (+9.7%) |  125.3 → 135.5 (+8.1%) |    917.3 → 946.5 (+3.2%) |    1,420 → 1,476 (+3.9%) |
| discord.py    |  184.7 → 184.1 (-0.3%) |  177.9 → 179.7 (+1.0%) |    2,128 → 2,127 (-0.0%) |    3,187 → 3,243 (+1.8%) |
| homeassistant | 2,621 → 3,119 (+19.0%) | 2,010 → 2,306 (+14.7%) | 23,756 → 30,181 (+27.0%) | 27,876 → 32,473 (+16.5%) |
| isort         | 106.3 → 134.3 (+26.3%) |  105.4 → 107.2 (+1.7%) |    446.9 → 441.1 (-1.3%) |   2,535 → 1,785 (-29.6%) |
| jinja         |    66.3 → 66.7 (+0.6%) |  105.2 → 106.1 (+0.9%) |    538.1 → 539.1 (+0.2%) |    1,333 → 1,311 (-1.7%) |
| pandas        |  506.4 → 540.6 (+6.8%) |  838.9 → 909.6 (+8.4%) |   9,718 → 10,586 (+8.9%) |    6,796 → 6,933 (+2.0%) |
| pandas-stubs  |  100.8 → 100.2 (-0.6%) |  197.6 → 203.3 (+2.9%) |    4,900 → 4,694 (-4.2%) |    2,449 → 2,496 (+1.9%) |
| prefect       |  136.9 → 138.0 (+0.8%) |  256.6 → 267.9 (+4.4%) |    501.0 → 501.3 (+0.1%) |    3,969 → 3,929 (-1.0%) |
| pytorch       | 1,509 → 1,725 (+14.3%) | 1,024 → 1,232 (+20.3%) | 22,688 → 29,908 (+31.8%) | 15,748 → 18,236 (+15.8%) |

## CLI peak RSS

Mean peak resident set size across the same measured CLI runs, collected by
[Hyperfine 2.0](https://github.com/sharkdp/hyperfine/releases/tag/v2.0.0). Values
retain the precision of its terminal summaries; GiB values are rounded to 0.1 GiB.

On macOS, Hyperfine uses [`ru_maxrss`](https://github.com/sharkdp/hyperfine/blob/v2.0.0/src/timer/unix_timer.rs).
This metric does not sum concurrent worker RSS; Pyright runs with `--threads`.
The LSP suites below measure latency.

Each cell shows **existing revision → updated revision**.

| Project       |                    ty |               Pyrefly |                  mypy |               Pyright |
| ------------- | --------------------: | --------------------: | --------------------: | --------------------: |
| black         | 130.2 MiB → 133.6 MiB | 156.0 MiB → 160.1 MiB | 196.4 MiB → 198.6 MiB | 290.1 MiB → 296.5 MiB |
| discord.py    | 228.6 MiB → 229.6 MiB | 216.1 MiB → 217.1 MiB | 279.1 MiB → 279.7 MiB | 429.8 MiB → 428.7 MiB |
| homeassistant |     3.1 GiB → 3.6 GiB |     2.5 GiB → 3.0 GiB |     1.8 GiB → 2.3 GiB |     1.6 GiB → 1.8 GiB |
| isort         |   91.5 MiB → 89.5 MiB | 104.1 MiB → 103.8 MiB | 122.1 MiB → 120.5 MiB | 299.0 MiB → 261.2 MiB |
| jinja         | 100.1 MiB → 100.0 MiB | 116.0 MiB → 116.3 MiB | 137.2 MiB → 137.1 MiB | 258.1 MiB → 256.9 MiB |
| pandas        | 572.9 MiB → 584.0 MiB | 554.4 MiB → 568.7 MiB | 922.4 MiB → 924.5 MiB | 747.2 MiB → 755.2 MiB |
| pandas-stubs  | 155.3 MiB → 158.2 MiB | 273.8 MiB → 275.3 MiB | 608.7 MiB → 615.3 MiB | 390.6 MiB → 396.5 MiB |
| prefect       | 222.4 MiB → 224.2 MiB | 292.3 MiB → 294.0 MiB | 134.8 MiB → 135.4 MiB | 562.3 MiB → 583.7 MiB |
| pytorch       |     1.5 GiB → 1.7 GiB |     0.8 GiB → 0.9 GiB |     1.6 GiB → 1.8 GiB |     1.4 GiB → 1.6 GiB |

## LSP: initial diagnostics

Two warmups and ten measured rounds per project and checker.

| Project       |                     ty |               Pyrefly |                Pyright |
| ------------- | ---------------------: | --------------------: | ---------------------: |
| black         |   64.6 → 76.5 (+18.4%) | 171.9 → 184.3 (+7.2%) |  298.7 → 308.0 (+3.1%) |
| discord.py    |  108.5 → 108.5 (-0.0%) | 193.3 → 190.9 (-1.3%) |  638.7 → 638.7 (-0.0%) |
| homeassistant |  95.1 → 104.5 (+10.0%) | 219.1 → 229.2 (+4.6%) | 1,683 → 1,981 (+17.7%) |
| isort         |    52.2 → 53.9 (+3.3%) | 100.6 → 102.8 (+2.2%) |  360.6 → 364.1 (+1.0%) |
| jinja         |    54.9 → 55.1 (+0.4%) | 127.7 → 127.4 (-0.2%) |  363.9 → 364.0 (+0.0%) |
| pandas        | 366.9 → 408.3 (+11.3%) | 534.4 → 549.7 (+2.9%) |  641.2 → 654.1 (+2.0%) |
| prefect       |  172.2 → 178.0 (+3.4%) | 463.1 → 464.2 (+0.2%) |  1,119 → 1,139 (+1.8%) |
| pytorch       |   58.4 → 70.5 (+20.8%) | 127.2 → 135.8 (+6.7%) |  704.7 → 740.1 (+5.0%) |

## LSP: incremental edit

Two warmups and ten measured rounds per project and checker. pandas-stubs has no
edit fixture and is omitted from both LSP suites.

| Project       |                   ty |               Pyrefly |                Pyright |
| ------------- | -------------------: | --------------------: | ---------------------: |
| black         | 16.9 → 18.7 (+11.3%) |  84.5 → 93.7 (+10.9%) |  511.5 → 558.8 (+9.3%) |
| discord.py    |  28.4 → 28.1 (-0.8%) |   81.4 → 83.0 (+2.0%) |  516.7 → 517.7 (+0.2%) |
| homeassistant |  30.8 → 32.3 (+4.9%) |   82.8 → 81.7 (-1.3%) |  580.2 → 588.9 (+1.5%) |
| isort         |  24.6 → 26.7 (+8.4%) |  47.6 → 56.0 (+17.7%) |  431.9 → 435.3 (+0.8%) |
| jinja         |  13.4 → 13.2 (-1.6%) |   65.7 → 68.4 (+4.1%) |  531.9 → 535.3 (+0.6%) |
| pandas        |  52.3 → 53.3 (+1.9%) | 238.2 → 257.5 (+8.1%) | 615.7 → 713.6 (+15.9%) |
| prefect       |    8.2 → 8.4 (+2.6%) |   59.3 → 59.9 (+1.1%) |  684.6 → 686.7 (+0.3%) |
| pytorch       |    4.2 → 4.3 (+4.2%) |   24.3 → 26.6 (+9.4%) |  409.0 → 399.7 (-2.3%) |

## Project revisions

| Project       | Existing                                   | Updated                                    |
| ------------- | ------------------------------------------ | ------------------------------------------ |
| black         | `ce1897a8f20d0f64844dd666d07f4003500d0e09` | `55996d1fb8342725c8a19b6023cd9439c3c1d6f7` |
| discord.py    | `2fbed9362422dad4f7850eb6c5d9b1f8bff7c71a` | `65232c38702be5844cf2ce865a4777eb1928b5d0` |
| homeassistant | `a0162d2ff0ed061501405a617961be149b15bd1f` | `c19ae285ede74cd64c3045a3a4aa43290c224f1b` |
| isort         | `87adfe4732548abff5010336f2fc4b5e8237407d` | `a514c71ed86c2216d0040c7d60e302ed76a4f7ab` |
| jinja         | `5ef70112a1ff19c05324ff889dd30405b1002044` | `5ef70112a1ff19c05324ff889dd30405b1002044` |
| pandas        | `e3a56513f27849f12265a14c814e02f4f408fb3d` | `a0225b65720018f4654390bb16d254daa6ee5e54` |
| pandas-stubs  | `1352ba3daa86f1c47a3cce5ad212a770cc693cb4` | `8dd6d91b1c05b26e30f7ddbe3dc3d4042a92bdd6` |
| prefect       | `db66b14dbaea18e726fc4ea0100fd194383c6c59` | `a9452ac21852755311913cb27887b083b5007c03` |
| pytorch       | `29d6170e7c79f2c71943692985a1546fb2bed28c` | `ab92945cea42e47ae398aead69af0872d340ea0f` |

The updated pandas revision removes `typings`, so its source list contains only
`pandas`. Jinja uses the same source revision in both runs.

Performance varies with hardware, operating system, dependencies, and background
load. Checkers can produce different diagnostics and do different amounts of work.
Comparisons with earlier published results also include tool and runtime changes.
