# Benchmarks

Computed on October 29, 2026 (UTC), on macOS 26.5.2 with an Apple M3 Max (16 cores,
128 GB RAM).

The existing project revisions were measured first, followed by the updated
upstream revisions with dependencies resolved afresh. Both runs used the same
checker versions, Python versions, and dependency cutoff (`2026-10-24T19:50:00Z`).
Updated project requirements can still change the installed dependencies. Both
cohorts use ty 0.0.94. HTTPX, NumPy, FastAPI, SQLAlchemy, and Jinja have the same
source and dependency inputs in both cohorts; their timing differences reflect
run-to-run variation.

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
    Assistant, which uses Python 3.14.9, and NumPy, which uses Python 3.12.15.

For run instructions, see [`ty_benchmark/README.md`](https://github.com/astral-sh/ruff/blob/14ae772168ec5876b6f1a869e72fb3431f4953dc/scripts/ty_benchmark/README.md).

NumPy checks Python and stub sources with tests excluded; its C extensions are
not built. SQLAlchemy adds a typed ORM and SQL expression workload.

## CLI cold check

Three warmups and at least ten measured runs. The mypy cache is cleared before
every run.

| Project       |                     ty |                Pyrefly |                     mypy |                  Pyright |
| ------------- | ---------------------: | ---------------------: | -----------------------: | -----------------------: |
| black         |   80.0 → 89.0 (+11.3%) |  124.2 → 134.5 (+8.3%) |    893.3 → 925.7 (+3.6%) |    1,378 → 1,433 (+4.0%) |
| discord.py    |  183.7 → 184.8 (+0.6%) |  175.6 → 175.1 (-0.3%) |    2,067 → 2,081 (+0.7%) |    3,064 → 3,128 (+2.1%) |
| homeassistant |  2,785 → 3,006 (+7.9%) | 2,020 → 2,317 (+14.7%) | 23,392 → 29,597 (+26.5%) | 27,168 → 31,131 (+14.6%) |
| isort         | 105.2 → 131.6 (+25.1%) |  104.5 → 106.5 (+1.9%) |    454.1 → 452.6 (-0.3%) |   2,499 → 1,774 (-29.0%) |
| jinja         |    66.2 → 66.2 (+0.0%) |  105.3 → 104.9 (-0.4%) |    530.9 → 533.7 (+0.5%) |    1,276 → 1,279 (+0.3%) |
| pandas        |  483.8 → 505.1 (+4.4%) | 786.4 → 906.5 (+15.3%) |   9,489 → 10,341 (+9.0%) |    6,484 → 7,036 (+8.5%) |
| pandas-stubs  |    99.2 → 98.8 (-0.4%) |  195.9 → 199.6 (+1.9%) |    4,824 → 4,613 (-4.4%) |    2,429 → 2,462 (+1.4%) |
| prefect       |  134.3 → 135.2 (+0.7%) |  254.6 → 263.1 (+3.3%) |    493.5 → 497.7 (+0.9%) |    3,840 → 3,843 (+0.1%) |
| pytorch       | 1,431 → 1,673 (+16.9%) | 1,026 → 1,220 (+18.9%) | 22,319 → 29,444 (+31.9%) | 15,018 → 17,099 (+13.9%) |
| httpx         |    71.7 → 71.8 (+0.1%) |  120.8 → 120.3 (-0.4%) |    860.8 → 866.1 (+0.6%) |    1,087 → 1,093 (+0.6%) |
| numpy         |  2,462 → 2,471 (+0.4%) |  1,523 → 1,475 (-3.2%) |  80,798 → 81,156 (+0.4%) |    8,848 → 8,919 (+0.8%) |
| fastapi       |  106.8 → 107.8 (+0.9%) |  301.1 → 297.4 (-1.2%) |    1,906 → 1,903 (-0.1%) |    2,163 → 2,178 (+0.7%) |
| sqlalchemy    |  382.9 → 386.1 (+0.8%) |  319.0 → 323.2 (+1.3%) |    3,058 → 3,049 (-0.3%) |    4,382 → 4,387 (+0.1%) |

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
| black         | 130.5 MiB → 134.0 MiB | 155.7 MiB → 159.9 MiB | 196.3 MiB → 198.7 MiB | 291.4 MiB → 292.6 MiB |
| discord.py    | 228.6 MiB → 229.8 MiB | 216.0 MiB → 217.0 MiB | 279.0 MiB → 279.4 MiB | 429.3 MiB → 428.5 MiB |
| homeassistant |     3.1 GiB → 3.6 GiB |     2.5 GiB → 3.0 GiB |     1.8 GiB → 2.3 GiB |     1.6 GiB → 1.8 GiB |
| isort         |   91.6 MiB → 89.4 MiB | 104.0 MiB → 103.9 MiB | 122.2 MiB → 120.4 MiB | 296.2 MiB → 265.4 MiB |
| jinja         |   99.9 MiB → 99.9 MiB | 116.4 MiB → 116.0 MiB | 137.2 MiB → 137.2 MiB | 257.6 MiB → 255.7 MiB |
| pandas        | 572.6 MiB → 588.0 MiB | 558.1 MiB → 570.6 MiB | 922.0 MiB → 926.2 MiB | 734.0 MiB → 784.8 MiB |
| pandas-stubs  | 155.5 MiB → 158.2 MiB | 273.5 MiB → 274.6 MiB | 608.9 MiB → 615.3 MiB | 386.4 MiB → 393.0 MiB |
| prefect       | 222.5 MiB → 224.2 MiB | 292.4 MiB → 294.4 MiB | 134.7 MiB → 135.5 MiB | 572.7 MiB → 567.7 MiB |
| pytorch       |     1.5 GiB → 1.7 GiB |     0.8 GiB → 0.9 GiB |     1.6 GiB → 1.8 GiB |     1.3 GiB → 1.5 GiB |
| httpx         | 102.4 MiB → 102.0 MiB | 129.9 MiB → 130.1 MiB | 190.5 MiB → 190.8 MiB | 261.5 MiB → 257.9 MiB |
| numpy         | 520.9 MiB → 520.7 MiB | 681.8 MiB → 681.7 MiB | 644.0 MiB → 645.4 MiB | 673.4 MiB → 692.1 MiB |
| fastapi       | 142.7 MiB → 142.6 MiB | 193.4 MiB → 193.6 MiB | 336.9 MiB → 337.1 MiB | 332.5 MiB → 335.4 MiB |
| sqlalchemy    | 422.6 MiB → 423.5 MiB | 295.7 MiB → 296.6 MiB | 370.3 MiB → 370.3 MiB | 544.4 MiB → 538.6 MiB |

## LSP: initial diagnostics

Two warmups and ten measured rounds per project and checker.

| Project       |                     ty |                Pyrefly |                Pyright |
| ------------- | ---------------------: | ---------------------: | ---------------------: |
| black         |   63.8 → 74.8 (+17.3%) |  169.8 → 181.8 (+7.1%) |  292.7 → 303.6 (+3.7%) |
| discord.py    |  106.2 → 105.4 (-0.7%) |  187.3 → 188.9 (+0.9%) |  627.1 → 625.5 (-0.2%) |
| homeassistant |   94.0 → 101.6 (+8.1%) |  219.4 → 228.7 (+4.2%) | 1,677 → 1,965 (+17.2%) |
| isort         |    50.6 → 53.7 (+6.0%) |  95.6 → 110.1 (+15.2%) |  354.2 → 357.3 (+0.9%) |
| jinja         |    53.8 → 54.6 (+1.5%) |  129.8 → 124.9 (-3.8%) |  354.3 → 354.9 (+0.2%) |
| pandas        | 354.5 → 394.1 (+11.2%) |  528.9 → 540.0 (+2.1%) |  628.5 → 637.8 (+1.5%) |
| prefect       |  171.9 → 174.9 (+1.7%) |  433.2 → 458.6 (+5.9%) |  1,101 → 1,113 (+1.1%) |
| pytorch       |   57.2 → 68.4 (+19.6%) | 116.3 → 134.4 (+15.5%) |  694.0 → 716.0 (+3.2%) |
| httpx         |    48.0 → 46.8 (-2.7%) |  114.0 → 113.4 (-0.5%) |  226.7 → 223.8 (-1.3%) |
| numpy         |  510.0 → 507.7 (-0.5%) |  566.3 → 564.6 (-0.3%) |  1,193 → 1,193 (+0.0%) |
| fastapi       |  101.3 → 101.1 (-0.2%) |  204.7 → 201.2 (-1.7%) |  471.0 → 476.7 (+1.2%) |
| sqlalchemy    |  216.8 → 221.6 (+2.2%) |  246.3 → 246.3 (+0.0%) |  273.4 → 272.9 (-0.2%) |

## LSP: incremental edit

Two warmups and ten measured rounds per project and checker. pandas-stubs has no
edit fixture and is omitted from both LSP suites.

| Project       |                   ty |               Pyrefly |                Pyright |
| ------------- | -------------------: | --------------------: | ---------------------: |
| black         | 16.1 → 20.4 (+26.7%) |  80.0 → 93.1 (+16.4%) |  504.5 → 551.1 (+9.3%) |
| discord.py    |  27.1 → 27.2 (+0.3%) |   78.3 → 78.6 (+0.4%) |  517.2 → 514.8 (-0.5%) |
| homeassistant |  29.9 → 31.6 (+5.6%) |   74.5 → 79.1 (+6.1%) |  580.4 → 574.7 (-1.0%) |
| isort         | 23.7 → 26.5 (+11.6%) |   45.9 → 48.2 (+5.1%) |  421.1 → 427.7 (+1.6%) |
| jinja         |  12.7 → 12.6 (-0.8%) |   63.9 → 62.6 (-2.0%) |  502.7 → 504.3 (+0.3%) |
| pandas        |  50.6 → 50.8 (+0.5%) | 230.3 → 250.8 (+8.9%) | 592.4 → 677.7 (+14.4%) |
| prefect       |    7.9 → 7.7 (-2.3%) |   57.7 → 55.8 (-3.3%) |  674.4 → 674.7 (+0.0%) |
| pytorch       |    4.0 → 4.3 (+8.8%) |   22.8 → 23.4 (+2.8%) |  403.6 → 404.3 (+0.2%) |
| httpx         |    8.3 → 8.2 (-1.0%) |   49.8 → 50.3 (+1.1%) |  425.0 → 428.0 (+0.7%) |
| numpy         |  35.8 → 35.9 (+0.4%) | 345.6 → 342.8 (-0.8%) |  1,226 → 1,198 (-2.3%) |
| fastapi       |    8.1 → 8.2 (+0.7%) |   67.6 → 67.7 (+0.1%) |  617.6 → 615.5 (-0.3%) |
| sqlalchemy    |  12.7 → 12.7 (-0.2%) |   79.1 → 78.5 (-0.8%) |  634.9 → 635.2 (+0.0%) |

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
| httpx         | `b5addb64f0161ff6bfe94c124ef76f6a1fba5254` | `b5addb64f0161ff6bfe94c124ef76f6a1fba5254` |
| numpy         | `f9f1772ce010001208475f751d19253469788410` | `f9f1772ce010001208475f751d19253469788410` |
| fastapi       | `7a0a3f0b286c6c865cf4398ea0e957a87b8bffa4` | `7a0a3f0b286c6c865cf4398ea0e957a87b8bffa4` |
| sqlalchemy    | `10f4d1e2d706a7722ca78e79ce05b00333a7aa5b` | `10f4d1e2d706a7722ca78e79ce05b00333a7aa5b` |

The updated pandas revision removes `typings`, so its source list contains only
`pandas`. Jinja and the four added projects use the same source revisions in
both runs.

Performance varies with hardware, operating system, dependencies, and background
load. Checkers can produce different diagnostics and do different amounts of work.
Comparisons with earlier published results also include tool and runtime changes.
