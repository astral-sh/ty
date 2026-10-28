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

For run instructions, see [`ty_benchmark/README.md`](https://github.com/astral-sh/ruff/blob/fc1f18e8512333b0fdb970249444686c3dcde100/scripts/ty_benchmark/README.md).

## CLI cold check

Three warmups and at least ten measured runs. The mypy cache is cleared before
every run.

| Project       |                     ty |                Pyrefly |                     mypy |                  Pyright |
| ------------- | ---------------------: | ---------------------: | -----------------------: | -----------------------: |
| black         |   78.9 → 89.4 (+13.3%) |  122.9 → 133.4 (+8.5%) |    890.0 → 929.6 (+4.4%) |    1,382 → 1,427 (+3.3%) |
| discord.py    |  183.7 → 181.7 (-1.1%) |  175.0 → 177.8 (+1.6%) |    2,080 → 2,087 (+0.4%) |    3,069 → 3,123 (+1.8%) |
| homeassistant | 2,541 → 3,027 (+19.1%) | 2,011 → 2,301 (+14.4%) | 23,377 → 29,933 (+28.0%) | 27,055 → 31,255 (+15.5%) |
| isort         | 105.5 → 132.9 (+26.0%) |  104.7 → 107.4 (+2.6%) |    445.8 → 438.0 (-1.7%) |   2,501 → 1,762 (-29.5%) |
| jinja         |    66.4 → 66.2 (-0.3%) |  104.6 → 106.3 (+1.6%) |    533.4 → 531.1 (-0.4%) |    1,286 → 1,284 (-0.1%) |
| pandas        | 482.3 → 537.9 (+11.5%) |  833.5 → 885.8 (+6.3%) |   9,502 → 10,406 (+9.5%) |    6,456 → 7,018 (+8.7%) |
| pandas-stubs  |   101.0 → 98.8 (-2.2%) |  195.5 → 198.3 (+1.4%) |    4,809 → 4,614 (-4.1%) |    2,395 → 2,464 (+2.9%) |
| prefect       |  132.8 → 136.8 (+3.0%) |  255.8 → 265.3 (+3.7%) |    492.4 → 494.4 (+0.4%) |    3,821 → 3,862 (+1.1%) |
| pytorch       | 1,436 → 1,677 (+16.8%) | 1,020 → 1,205 (+18.1%) | 22,329 → 29,484 (+32.0%) | 14,986 → 16,984 (+13.3%) |

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
| black         | 130.4 MiB → 133.4 MiB | 156.0 MiB → 159.9 MiB | 196.3 MiB → 198.6 MiB | 289.0 MiB → 290.7 MiB |
| discord.py    | 228.8 MiB → 229.6 MiB | 216.6 MiB → 216.9 MiB | 278.7 MiB → 280.2 MiB | 436.2 MiB → 431.8 MiB |
| homeassistant |     3.1 GiB → 3.6 GiB |     2.5 GiB → 3.0 GiB |     1.8 GiB → 2.3 GiB |     1.6 GiB → 1.8 GiB |
| isort         |   91.8 MiB → 89.5 MiB | 104.2 MiB → 104.1 MiB | 122.2 MiB → 120.7 MiB | 290.8 MiB → 264.2 MiB |
| jinja         | 100.2 MiB → 100.2 MiB | 116.1 MiB → 116.1 MiB | 137.3 MiB → 137.2 MiB | 255.3 MiB → 257.2 MiB |
| pandas        | 575.8 MiB → 583.6 MiB | 556.4 MiB → 571.6 MiB | 924.9 MiB → 926.2 MiB | 719.2 MiB → 735.7 MiB |
| pandas-stubs  | 155.9 MiB → 158.5 MiB | 273.4 MiB → 274.6 MiB | 608.8 MiB → 615.3 MiB | 383.8 MiB → 390.7 MiB |
| prefect       | 222.8 MiB → 224.1 MiB | 292.3 MiB → 293.4 MiB | 134.6 MiB → 135.3 MiB | 560.5 MiB → 565.5 MiB |
| pytorch       |     1.5 GiB → 1.7 GiB |     0.8 GiB → 0.9 GiB |     1.6 GiB → 1.8 GiB |     1.4 GiB → 1.5 GiB |

## LSP: initial diagnostics

Two warmups and ten measured rounds per project and checker.

| Project       |                     ty |               Pyrefly |                Pyright |
| ------------- | ---------------------: | --------------------: | ---------------------: |
| black         |   65.2 → 74.9 (+14.9%) | 169.7 → 183.2 (+7.9%) |  293.4 → 302.0 (+2.9%) |
| discord.py    |  106.3 → 107.6 (+1.2%) | 189.0 → 189.9 (+0.5%) |  632.4 → 631.0 (-0.2%) |
| homeassistant |   94.3 → 102.3 (+8.4%) | 215.5 → 228.2 (+5.9%) | 1,672 → 1,968 (+17.7%) |
| isort         |    50.8 → 54.1 (+6.5%) |  97.3 → 100.9 (+3.8%) |  353.3 → 357.5 (+1.2%) |
| jinja         |    53.8 → 53.9 (+0.3%) | 123.9 → 126.1 (+1.7%) |  353.8 → 355.9 (+0.6%) |
| pandas        | 355.4 → 395.6 (+11.3%) | 529.8 → 543.6 (+2.6%) |  624.5 → 631.7 (+1.2%) |
| prefect       |  169.5 → 175.0 (+3.2%) | 458.7 → 458.1 (-0.1%) |  1,103 → 1,115 (+1.1%) |
| pytorch       |   57.3 → 68.8 (+20.0%) | 117.3 → 123.6 (+5.4%) |  692.8 → 717.2 (+3.5%) |

## LSP: incremental edit

Two warmups and ten measured rounds per project and checker. pandas-stubs has no
edit fixture and is omitted from both LSP suites.

| Project       |                   ty |                Pyrefly |                Pyright |
| ------------- | -------------------: | ---------------------: | ---------------------: |
| black         | 16.3 → 18.1 (+10.9%) |   79.5 → 92.6 (+16.4%) | 502.3 → 555.9 (+10.7%) |
| discord.py    |  27.4 → 27.3 (-0.1%) |    76.7 → 77.7 (+1.3%) |  522.9 → 508.2 (-2.8%) |
| homeassistant |  30.0 → 32.8 (+9.2%) |    78.0 → 79.8 (+2.3%) |  580.1 → 577.1 (-0.5%) |
| isort         |  24.0 → 26.0 (+8.3%) |   44.8 → 51.1 (+14.0%) |  423.6 → 430.2 (+1.6%) |
| jinja         |  12.6 → 12.8 (+1.7%) |    61.8 → 64.0 (+3.6%) |  507.0 → 504.1 (-0.6%) |
| pandas        |  50.3 → 50.5 (+0.5%) | 233.2 → 258.1 (+10.7%) | 598.3 → 681.9 (+14.0%) |
| prefect       |    7.7 → 7.7 (-0.8%) |    57.3 → 56.5 (-1.4%) |  677.7 → 674.9 (-0.4%) |
| pytorch       |    3.9 → 4.1 (+3.8%) |    22.9 → 22.7 (-1.1%) |  406.2 → 400.7 (-1.3%) |

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
