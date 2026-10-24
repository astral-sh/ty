# Benchmarks

Computed on October 24, 2026, on macOS 26.5.2 with an Apple M3 Max (16 cores,
128 GB RAM).

The existing project revisions were measured first, followed by the updated
upstream revisions with dependencies resolved afresh. Both runs used the same
checker versions, Python versions, and dependency cutoff (`2026-10-24T19:50:00Z`).
Updated project requirements can still change the installed dependencies.

Each cell shows **existing revision → updated revision (percentage change)**.
Times are mean wall-clock milliseconds; negative changes mean faster checks.

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

For run instructions, see [`ty_benchmark/README.md`](https://github.com/astral-sh/ruff/blob/6b55217a73f66710184789bf60a8412df30995d0/scripts/ty_benchmark/README.md).

## CLI cold check

Three warmups and at least ten measured runs. The mypy cache is cleared before
every run.

| Project       |                     ty |                Pyrefly |                     mypy |                  Pyright |
| ------------- | ---------------------: | ---------------------: | -----------------------: | -----------------------: |
| black         |    79.1 → 86.5 (+9.4%) |  123.7 → 131.7 (+6.5%) |    899.4 → 952.3 (+5.9%) |    1,383 → 1,418 (+2.5%) |
| discord.py    |  171.5 → 169.8 (-1.0%) |  176.4 → 174.2 (-1.2%) |    2,086 → 2,103 (+0.8%) |    3,098 → 3,062 (-1.2%) |
| homeassistant | 2,683 → 3,004 (+12.0%) | 2,044 → 2,290 (+12.0%) | 25,247 → 30,517 (+20.9%) | 27,990 → 32,169 (+14.9%) |
| isort         | 130.9 → 178.8 (+36.6%) |  104.2 → 106.0 (+1.7%) |    443.1 → 440.6 (-0.6%) |   2,514 → 1,780 (-29.2%) |
| jinja         |    64.2 → 64.4 (+0.3%) |  104.4 → 105.2 (+0.8%) |    535.1 → 528.7 (-1.2%) |    1,278 → 1,290 (+1.0%) |
| pandas        | 451.7 → 524.9 (+16.2%) | 834.5 → 953.4 (+14.2%) |   9,858 → 10,630 (+7.8%) |    6,647 → 7,174 (+7.9%) |
| pandas-stubs  |  104.3 → 105.5 (+1.2%) |  196.9 → 200.1 (+1.6%) |    4,873 → 4,683 (-3.9%) |    2,410 → 2,462 (+2.2%) |
| prefect       |  131.5 → 133.8 (+1.7%) |  255.6 → 263.6 (+3.1%) |    494.9 → 491.2 (-0.7%) |    3,876 → 3,821 (-1.4%) |
| pytorch       | 1,305 → 1,552 (+18.9%) | 1,039 → 1,198 (+15.3%) | 22,555 → 29,475 (+30.7%) |  15,388 → 16,815 (+9.3%) |

## LSP: initial diagnostics

Two warmups and ten measured rounds per project and checker.

| Project       |                     ty |                Pyrefly |                Pyright |
| ------------- | ---------------------: | ---------------------: | ---------------------: |
| black         |   62.6 → 73.6 (+17.6%) |  162.7 → 174.5 (+7.2%) |  287.8 → 300.0 (+4.2%) |
| discord.py    |  103.7 → 102.4 (-1.2%) |  188.3 → 188.7 (+0.2%) |  621.0 → 634.3 (+2.1%) |
| homeassistant | 302.9 → 361.4 (+19.3%) |  213.9 → 230.2 (+7.6%) | 1,655 → 1,996 (+20.6%) |
| isort         |    55.0 → 59.7 (+8.7%) |   99.6 → 106.9 (+7.3%) |  353.0 → 368.9 (+4.5%) |
| jinja         |    57.3 → 56.9 (-0.6%) |  126.4 → 128.4 (+1.6%) |  359.3 → 364.3 (+1.4%) |
| pandas        | 403.3 → 451.5 (+12.0%) |  529.5 → 546.6 (+3.2%) |  635.2 → 649.1 (+2.2%) |
| prefect       |  177.1 → 185.1 (+4.5%) |  444.8 → 453.5 (+2.0%) |  1,094 → 1,150 (+5.1%) |
| pytorch       | 100.4 → 117.3 (+16.9%) | 111.4 → 126.2 (+13.2%) |  688.3 → 737.6 (+7.2%) |

## LSP: incremental edit

Two warmups and ten measured rounds per project and checker. pandas-stubs has no
edit fixture and is omitted from both LSP suites.

| Project       |                   ty |               Pyrefly |                Pyright |
| ------------- | -------------------: | --------------------: | ---------------------: |
| black         | 16.0 → 18.4 (+15.3%) |  99.6 → 102.1 (+2.4%) |  519.7 → 562.9 (+8.3%) |
| discord.py    |  25.6 → 25.9 (+1.0%) |   98.4 → 97.2 (-1.3%) |  536.0 → 527.8 (-1.5%) |
| homeassistant |  31.7 → 34.3 (+8.2%) |   98.7 → 98.1 (-0.6%) |  605.7 → 603.5 (-0.4%) |
| isort         |  25.6 → 27.9 (+8.9%) |   64.3 → 69.5 (+8.2%) |  443.8 → 453.5 (+2.2%) |
| jinja         |  13.7 → 13.8 (+0.2%) |   83.4 → 82.2 (-1.5%) |  544.0 → 549.4 (+1.0%) |
| pandas        |  77.6 → 80.3 (+3.5%) | 250.9 → 272.3 (+8.5%) | 604.0 → 707.4 (+17.1%) |
| prefect       |    8.3 → 8.6 (+3.0%) |   76.2 → 74.2 (-2.7%) |  698.5 → 699.2 (+0.1%) |
| pytorch       |    5.6 → 5.9 (+5.4%) |   38.5 → 34.8 (-9.6%) |  427.3 → 414.5 (-3.0%) |

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
