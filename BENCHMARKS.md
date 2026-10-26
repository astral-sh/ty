# Benchmarks

Computed on October 26, 2026, on macOS 26.5.2 with an Apple M3 Max (16 cores,
128 GB RAM).

The existing project revisions were measured first, followed by the updated
upstream revisions with dependencies resolved afresh. Both runs used the same
checker versions, Python versions, and dependency cutoff (`2026-10-24T19:50:00Z`).
Updated project requirements can still change the installed dependencies.

Timing cells show **existing revision → updated revision (percentage change)**.
Times are mean wall-clock milliseconds; negative changes mean faster checks.

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

For run instructions, see [`ty_benchmark/README.md`](https://github.com/astral-sh/ruff/blob/fc1f18e8512333b0fdb970249444686c3dcde100/scripts/ty_benchmark/README.md).

## CLI cold check

Three warmups and at least ten measured runs. The mypy cache is cleared before
every run.

| Project       |                     ty |                Pyrefly |                     mypy |                  Pyright |
| ------------- | ---------------------: | ---------------------: | -----------------------: | -----------------------: |
| black         |   78.1 → 86.9 (+11.3%) |  123.2 → 133.6 (+8.4%) |    900.6 → 931.3 (+3.4%) |    1,382 → 1,430 (+3.5%) |
| discord.py    |  182.7 → 180.3 (-1.3%) |  176.7 → 176.0 (-0.4%) |    2,076 → 2,083 (+0.3%) |    3,048 → 3,091 (+1.4%) |
| homeassistant | 2,607 → 3,042 (+16.7%) | 2,008 → 2,300 (+14.5%) | 23,310 → 29,763 (+27.7%) | 27,020 → 31,076 (+15.0%) |
| isort         | 129.7 → 177.7 (+37.0%) |  104.7 → 106.5 (+1.7%) |    449.9 → 437.9 (-2.7%) |   2,500 → 1,761 (-29.6%) |
| jinja         |    66.5 → 66.4 (-0.2%) |  105.7 → 104.6 (-1.0%) |    532.5 → 532.4 (-0.0%) |    1,283 → 1,286 (+0.3%) |
| pandas        |  481.4 → 520.5 (+8.1%) |  824.3 → 891.4 (+8.1%) |   9,478 → 10,325 (+8.9%) |    6,454 → 6,929 (+7.4%) |
| pandas-stubs  |  100.6 → 101.3 (+0.7%) |  195.6 → 200.4 (+2.5%) |    4,806 → 4,614 (-4.0%) |    2,396 → 2,449 (+2.2%) |
| prefect       |  133.0 → 139.9 (+5.2%) |  250.0 → 266.1 (+6.4%) |    492.6 → 501.5 (+1.8%) |    3,809 → 3,862 (+1.4%) |
| pytorch       | 1,462 → 1,669 (+14.2%) | 1,017 → 1,218 (+19.8%) | 22,298 → 29,410 (+31.9%) | 14,840 → 16,855 (+13.6%) |

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
| black         | 131.2 MiB → 134.9 MiB | 155.7 MiB → 159.5 MiB | 196.3 MiB → 198.7 MiB | 292.4 MiB → 289.4 MiB |
| discord.py    | 229.5 MiB → 229.5 MiB | 216.7 MiB → 216.9 MiB | 279.5 MiB → 279.8 MiB | 430.5 MiB → 428.5 MiB |
| homeassistant |     3.1 GiB → 3.6 GiB |     2.5 GiB → 3.0 GiB |     1.8 GiB → 2.3 GiB |     1.6 GiB → 1.8 GiB |
| isort         |   93.4 MiB → 90.6 MiB | 104.2 MiB → 103.8 MiB | 122.2 MiB → 120.4 MiB | 292.8 MiB → 263.6 MiB |
| jinja         | 100.1 MiB → 100.0 MiB | 116.1 MiB → 116.0 MiB | 137.1 MiB → 137.0 MiB | 256.1 MiB → 255.9 MiB |
| pandas        | 572.5 MiB → 584.7 MiB | 553.8 MiB → 571.7 MiB | 920.4 MiB → 925.8 MiB | 758.6 MiB → 755.1 MiB |
| pandas-stubs  | 154.9 MiB → 157.8 MiB | 272.6 MiB → 275.1 MiB | 608.8 MiB → 614.8 MiB | 386.5 MiB → 393.8 MiB |
| prefect       | 222.9 MiB → 224.3 MiB | 292.1 MiB → 294.1 MiB | 134.8 MiB → 135.5 MiB | 575.8 MiB → 573.2 MiB |
| pytorch       |     1.5 GiB → 1.7 GiB |     0.8 GiB → 0.9 GiB |     1.6 GiB → 1.8 GiB |     1.4 GiB → 1.5 GiB |

## LSP: initial diagnostics

Two warmups and ten measured rounds per project and checker.

| Project       |                     ty |               Pyrefly |                Pyright |
| ------------- | ---------------------: | --------------------: | ---------------------: |
| black         |   63.1 → 74.2 (+17.5%) | 168.2 → 182.1 (+8.2%) |  292.9 → 302.9 (+3.4%) |
| discord.py    |  106.7 → 108.8 (+2.0%) | 188.4 → 188.5 (+0.0%) |  626.3 → 628.6 (+0.4%) |
| homeassistant |   94.2 → 102.9 (+9.2%) | 215.8 → 228.0 (+5.7%) | 1,672 → 1,962 (+17.3%) |
| isort         |    51.6 → 53.9 (+4.5%) |  97.9 → 100.1 (+2.2%) |  355.3 → 357.2 (+0.5%) |
| jinja         |    54.9 → 54.6 (-0.5%) | 125.8 → 126.1 (+0.2%) |  356.4 → 357.4 (+0.3%) |
| pandas        | 358.8 → 399.0 (+11.2%) | 529.7 → 543.8 (+2.7%) |  630.3 → 632.1 (+0.3%) |
| prefect       |  174.1 → 180.5 (+3.7%) | 461.0 → 451.5 (-2.1%) |  1,100 → 1,117 (+1.5%) |
| pytorch       |   57.7 → 70.3 (+21.8%) | 115.1 → 122.2 (+6.2%) |  690.6 → 722.3 (+4.6%) |

## LSP: incremental edit

Two warmups and ten measured rounds per project and checker. pandas-stubs has no
edit fixture and is omitted from both LSP suites.

| Project       |                   ty |               Pyrefly |                Pyright |
| ------------- | -------------------: | --------------------: | ---------------------: |
| black         | 16.4 → 19.3 (+17.6%) |  78.5 → 91.9 (+17.1%) |  502.9 → 546.4 (+8.7%) |
| discord.py    |  27.1 → 27.0 (-0.5%) |   75.3 → 77.7 (+3.2%) |  509.0 → 512.9 (+0.8%) |
| homeassistant |  30.3 → 31.6 (+4.3%) |   77.5 → 80.6 (+3.9%) |  582.4 → 572.7 (-1.7%) |
| isort         |  24.7 → 26.3 (+6.3%) |   45.0 → 49.4 (+9.7%) |  424.5 → 430.0 (+1.3%) |
| jinja         |  13.0 → 12.8 (-1.4%) |   62.1 → 60.6 (-2.3%) |  511.9 → 507.6 (-0.8%) |
| pandas        |  51.0 → 51.5 (+0.9%) | 232.9 → 251.4 (+8.0%) | 598.4 → 689.7 (+15.2%) |
| prefect       |    7.8 → 7.9 (+1.2%) |   57.2 → 57.0 (-0.4%) |  677.1 → 679.2 (+0.3%) |
| pytorch       |   9.4 → 4.1 (-55.7%) |   21.7 → 22.8 (+5.1%) |  409.4 → 400.4 (-2.2%) |

The existing-revision `pytorch` incremental result for ty has a
mean of 9.4 ms and a median of 4.0 ms; its slowest round took
53.0 ms. All rounds are retained. The before-and-after percentage for
this case is sensitive to that outlier.

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
