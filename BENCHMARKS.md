# Benchmarks

All benchmarks were computed on macOS (Apple M3 Max 16, 128 GB) with the following tool versions:

- [Pyrefly](https://pypi.org/project/pyrefly/) 1.4.0
- [Pyright](https://www.npmjs.com/package/pyright) 1.1.414
- [mypy](https://pypi.org/project/mypy/) 2.4.0
- [ty](https://pypi.org/project/ty/) 0.0.99
- [Zuban](https://pypi.org/project/zuban/) 0.10.2

ty was measured on November 6, 2026. The other CLI and LSP results are retained
from November 4 and November 3, respectively.

Benchmark performance may vary across operating systems, and from project to project. This document
includes benchmarks from a variety of projects to provide a representative example of real-world
usage: [Black](https://github.com/psf/black), [discord.py](https://github.com/Rapptz/discord.py),
[Home Assistant](https://github.com/home-assistant/core), [isort](https://github.com/pycqa/isort),
[Jinja](https://github.com/pallets/jinja), [pandas](https://github.com/pandas-dev/pandas),
[pandas-stubs](https://github.com/pandas-dev/pandas-stubs),
[Prefect](https://github.com/PrefectHQ/prefect), [PyTorch](https://github.com/pytorch/pytorch),
[HTTPX](https://github.com/encode/httpx), [NumPy](https://github.com/numpy/numpy),
[FastAPI](https://github.com/fastapi/fastapi), [SQLAlchemy](https://github.com/sqlalchemy/sqlalchemy),
[Rich](https://github.com/Textualize/rich), [Django](https://github.com/django/django),
[SymPy](https://github.com/sympy/sympy), [OpenAI Python SDK](https://github.com/openai/openai-python),
and [pytest](https://github.com/pytest-dev/pytest).

For instructions on running the benchmarks, see
[`ty_benchmark/README.md`](https://github.com/astral-sh/ruff/blob/504457130a2183e9f0c6f4e92ce1c43e970b70ca/scripts/ty_benchmark/README.md).

## CLI

CLI checks use each checker's default worker settings.

```text
black
-----

Benchmark 1: ty
  Time (mean ± σ):      65.8 ms ±   2.7 ms    [User: 457.3 ms, System: 26.9 ms]
  Range (min … max):    60.4 ms …  70.2 ms    34 runs
  Memory (peak RSS):  135.7 MiB

  Warning: Ignoring non-zero exit code.

Benchmark 2: Pyrefly
  Time (mean ± σ):     127.1 ms ±   1.7 ms    [User: 484.7 ms, System: 43.0 ms]
  Range (min … max):   123.8 ms … 130.1 ms    19 runs
  Memory (peak RSS):  159.6 MiB

  Warning: Ignoring non-zero exit code.

Benchmark 3: mypy
  Time (mean ± σ):     921.0 ms ±   6.9 ms    [User: 875.7 ms, System: 124.9 ms]
  Range (min … max):   906.9 ms … 932.0 ms    10 runs
  Memory (peak RSS):  198.7 MiB

  Warning: Ignoring non-zero exit code.

Benchmark 4: Pyright
  Time (mean ± σ):      1.663 s ±  0.012 s    [User: 3.257 s, System: 0.118 s]
  Range (min … max):    1.647 s …  1.689 s    10 runs
  Memory (peak RSS):  427.1 MiB

  Warning: Ignoring non-zero exit code.

Benchmark 5: Zuban
  Time (mean ± σ):     143.8 ms ±   2.0 ms    [User: 470.4 ms, System: 24.5 ms]
  Range (min … max):   140.0 ms … 146.7 ms    17 runs
  Memory (peak RSS):   79.4 MiB

  Warning: Ignoring non-zero exit code.

Summary
  ty ran
    1.93 ± 0.08 times faster than Pyrefly
    2.19 ± 0.09 times faster than Zuban
   14.00 ± 0.58 times faster than mypy
   25.29 ± 1.04 times faster than Pyright

-------------------------------------------------------------------------------

discord.py
----------

Benchmark 1: ty
  Time (mean ± σ):     136.4 ms ±   5.6 ms    [User: 1313.4 ms, System: 69.0 ms]
  Range (min … max):   126.0 ms … 148.8 ms    19 runs
  Memory (peak RSS):  223.7 MiB

  Warning: Ignoring non-zero exit code.

Benchmark 2: Pyrefly
  Time (mean ± σ):     173.4 ms ±   4.5 ms    [User: 1163.6 ms, System: 56.4 ms]
  Range (min … max):   168.0 ms … 179.6 ms    15 runs
  Memory (peak RSS):  217.2 MiB

  Warning: Ignoring non-zero exit code.

Benchmark 3: mypy
  Time (mean ± σ):      2.086 s ±  0.012 s    [User: 2.054 s, System: 0.131 s]
  Range (min … max):    2.071 s …  2.113 s    10 runs
  Memory (peak RSS):  279.5 MiB

  Warning: Ignoring non-zero exit code.

Benchmark 4: Pyright
  Time (mean ± σ):      3.986 s ±  0.014 s    [User: 7.760 s, System: 0.210 s]
  Range (min … max):    3.976 s …  4.012 s    10 runs
  Memory (peak RSS):  778.9 MiB

  Warning: Ignoring non-zero exit code.

Benchmark 5: Zuban
  Time (mean ± σ):     356.5 ms ±   3.5 ms    [User: 1039.1 ms, System: 37.0 ms]
  Range (min … max):   349.6 ms … 360.1 ms    10 runs
  Memory (peak RSS):  103.6 MiB

  Warning: Ignoring non-zero exit code.

Summary
  ty ran
    1.27 ± 0.06 times faster than Pyrefly
    2.61 ± 0.11 times faster than Zuban
   15.30 ± 0.64 times faster than mypy
   29.24 ± 1.21 times faster than Pyright

-------------------------------------------------------------------------------

homeassistant
-------------

Benchmark 1: ty
  Time (mean ± σ):      2.107 s ±  0.021 s    [User: 26.540 s, System: 3.767 s]
  Range (min … max):    2.072 s …  2.134 s    10 runs
  Memory (peak RSS):  3,463 MiB

  Warning: Ignoring non-zero exit code.

Benchmark 2: Pyrefly
  Time (mean ± σ):      2.303 s ±  0.031 s    [User: 24.094 s, System: 1.844 s]
  Range (min … max):    2.253 s …  2.347 s    10 runs
  Memory (peak RSS):  3,031 MiB

  Warning: Ignoring non-zero exit code.

Benchmark 3: mypy
  Time (mean ± σ):     52.028 s ±  0.457 s    [User: 49.512 s, System: 6.449 s]
  Range (min … max):   51.702 s … 53.104 s    10 runs
  Memory (peak RSS):  4,189 MiB

  Warning: Ignoring non-zero exit code.

Benchmark 4: Pyright
  Time (mean ± σ):    126.940 s ±  7.192 s    [User: 233.960 s, System: 4.819 s]
  Range (min … max):  118.428 s … 143.075 s    10 runs
  Memory (peak RSS):  4,208 MiB

  Warning: Ignoring non-zero exit code.

Benchmark 5: Zuban
  Time (mean ± σ):      7.454 s ±  0.063 s    [User: 24.984 s, System: 1.305 s]
  Range (min … max):    7.322 s …  7.534 s    10 runs
  Memory (peak RSS):  1,943 MiB

  Warning: Ignoring non-zero exit code.

Summary
  ty ran
    1.09 ± 0.02 times faster than Pyrefly
    3.54 ± 0.05 times faster than Zuban
   24.69 ± 0.33 times faster than mypy
   60.25 ± 3.47 times faster than Pyright

-------------------------------------------------------------------------------

isort
-----

Benchmark 1: ty
  Time (mean ± σ):      85.7 ms ±   2.1 ms    [User: 233.8 ms, System: 15.8 ms]
  Range (min … max):    82.5 ms …  90.5 ms    26 runs
  Memory (peak RSS):   90.7 MiB

  Warning: Ignoring non-zero exit code.

Benchmark 2: Pyrefly
  Time (mean ± σ):     105.5 ms ±   2.0 ms    [User: 267.5 ms, System: 32.4 ms]
  Range (min … max):   102.6 ms … 109.2 ms    23 runs
  Memory (peak RSS):  103.7 MiB

  Warning: Ignoring non-zero exit code.

Benchmark 3: mypy
  Time (mean ± σ):     454.6 ms ±   3.2 ms    [User: 414.4 ms, System: 61.4 ms]
  Range (min … max):   447.6 ms … 458.5 ms    10 runs
  Memory (peak RSS):  120.3 MiB

Benchmark 4: Pyright
  Time (mean ± σ):      1.629 s ±  0.011 s    [User: 2.989 s, System: 0.083 s]
  Range (min … max):    1.617 s …  1.653 s    10 runs
  Memory (peak RSS):  293.9 MiB

  Warning: Ignoring non-zero exit code.

Benchmark 5: Zuban
  Time (mean ± σ):      66.0 ms ±   1.4 ms    [User: 228.0 ms, System: 16.8 ms]
  Range (min … max):    63.2 ms …  68.5 ms    33 runs
  Memory (peak RSS):   55.8 MiB

  Warning: Ignoring non-zero exit code.

Summary
  Zuban ran
    1.30 ± 0.04 times faster than ty
    1.60 ± 0.05 times faster than Pyrefly
    6.89 ± 0.15 times faster than mypy
   24.69 ± 0.54 times faster than Pyright

-------------------------------------------------------------------------------

jinja
-----

Benchmark 1: ty
  Time (mean ± σ):      54.0 ms ±   1.1 ms    [User: 261.9 ms, System: 15.9 ms]
  Range (min … max):    52.2 ms …  56.4 ms    38 runs
  Memory (peak RSS):   99.8 MiB

  Warning: Ignoring non-zero exit code.

Benchmark 2: Pyrefly
  Time (mean ± σ):     104.1 ms ±   1.4 ms    [User: 261.7 ms, System: 34.8 ms]
  Range (min … max):   101.6 ms … 106.8 ms    23 runs
  Memory (peak RSS):  115.9 MiB

  Warning: Ignoring non-zero exit code.

Benchmark 3: mypy
  Time (mean ± σ):     549.0 ms ±   9.1 ms    [User: 515.0 ms, System: 70.7 ms]
  Range (min … max):   541.9 ms … 573.4 ms    10 runs
  Memory (peak RSS):  136.7 MiB

Benchmark 4: Pyright
  Time (mean ± σ):      1.178 s ±  0.007 s    [User: 2.363 s, System: 0.082 s]
  Range (min … max):    1.166 s …  1.186 s    10 runs
  Memory (peak RSS):  317.7 MiB

  Warning: Ignoring non-zero exit code.

Benchmark 5: Zuban
  Time (mean ± σ):      84.2 ms ±   1.6 ms    [User: 303.7 ms, System: 17.7 ms]
  Range (min … max):    81.2 ms …  88.9 ms    27 runs
  Memory (peak RSS):   60.7 MiB

  Warning: Ignoring non-zero exit code.

Summary
  ty ran
    1.56 ± 0.04 times faster than Zuban
    1.93 ± 0.05 times faster than Pyrefly
   10.16 ± 0.26 times faster than mypy
   21.81 ± 0.45 times faster than Pyright

-------------------------------------------------------------------------------

pandas
------

Benchmark 1: ty
  Time (mean ± σ):     409.7 ms ±  14.4 ms    [User: 4575.0 ms, System: 217.3 ms]
  Range (min … max):   390.4 ms … 442.6 ms    10 runs
  Memory (peak RSS):  589.6 MiB

  Warning: Ignoring non-zero exit code.

Benchmark 2: Pyrefly
  Time (mean ± σ):     888.1 ms ±  27.7 ms    [User: 8567.9 ms, System: 145.8 ms]
  Range (min … max):   818.8 ms … 905.8 ms    10 runs
  Memory (peak RSS):  570.3 MiB

  Warning: Ignoring non-zero exit code.

Benchmark 3: mypy
  Time (mean ± σ):     10.469 s ±  0.040 s    [User: 10.419 s, System: 0.581 s]
  Range (min … max):   10.415 s … 10.547 s    10 runs
  Memory (peak RSS):  923.7 MiB

  Warning: Ignoring non-zero exit code.

Benchmark 4: Pyright
  Time (mean ± σ):     15.790 s ±  0.102 s    [User: 24.782 s, System: 0.625 s]
  Range (min … max):   15.624 s … 15.981 s    10 runs
  Memory (peak RSS):  2,360 MiB

  Warning: Ignoring non-zero exit code.

Benchmark 5: Zuban
  Time (mean ± σ):      1.409 s ±  0.006 s    [User: 3.555 s, System: 0.102 s]
  Range (min … max):    1.397 s …  1.420 s    10 runs
  Memory (peak RSS):  306.8 MiB

  Warning: Ignoring non-zero exit code.

Summary
  ty ran
    2.17 ± 0.10 times faster than Pyrefly
    3.44 ± 0.12 times faster than Zuban
   25.55 ± 0.90 times faster than mypy
   38.54 ± 1.38 times faster than Pyright

-------------------------------------------------------------------------------

pandas-stubs
------------

Benchmark 1: ty
  Time (mean ± σ):      82.5 ms ±   2.9 ms    [User: 410.7 ms, System: 42.3 ms]
  Range (min … max):    77.0 ms …  89.6 ms    28 runs
  Memory (peak RSS):  159.9 MiB

Benchmark 2: Pyrefly
  Time (mean ± σ):     196.0 ms ±   1.5 ms    [User: 696.0 ms, System: 68.7 ms]
  Range (min … max):   193.7 ms … 199.0 ms    13 runs
  Memory (peak RSS):  274.3 MiB

Benchmark 3: mypy
  Time (mean ± σ):      4.762 s ±  0.045 s    [User: 4.623 s, System: 0.425 s]
  Range (min … max):    4.707 s …  4.832 s    10 runs
  Memory (peak RSS):  615.6 MiB

  Warning: Ignoring non-zero exit code.

Benchmark 4: Pyright
  Time (mean ± σ):      2.170 s ±  0.013 s    [User: 4.167 s, System: 0.147 s]
  Range (min … max):    2.157 s …  2.191 s    10 runs
  Memory (peak RSS):  549.1 MiB

Benchmark 5: Zuban
  Time (mean ± σ):     271.0 ms ±   1.9 ms    [User: 624.2 ms, System: 33.0 ms]
  Range (min … max):   267.8 ms … 273.5 ms    10 runs
  Memory (peak RSS):   95.9 MiB

  Warning: Ignoring non-zero exit code.

Summary
  ty ran
    2.38 ± 0.08 times faster than Pyrefly
    3.28 ± 0.12 times faster than Zuban
   26.29 ± 0.93 times faster than Pyright
   57.70 ± 2.08 times faster than mypy

-------------------------------------------------------------------------------

prefect
-------

Benchmark 1: ty
  Time (mean ± σ):     105.8 ms ±   5.8 ms    [User: 664.1 ms, System: 46.3 ms]
  Range (min … max):    97.3 ms … 122.0 ms    23 runs
  Memory (peak RSS):  225.1 MiB

  Warning: Ignoring non-zero exit code.

Benchmark 2: Pyrefly
  Time (mean ± σ):     271.4 ms ±  10.1 ms    [User: 1933.7 ms, System: 87.9 ms]
  Range (min … max):   258.3 ms … 292.2 ms    10 runs
  Memory (peak RSS):  294.0 MiB

  Warning: Ignoring non-zero exit code.

Benchmark 3: mypy
  Time (mean ± σ):      7.191 s ±  0.092 s    [User: 7.078 s, System: 0.780 s]
  Range (min … max):    7.116 s …  7.417 s    10 runs
  Memory (peak RSS):  837.3 MiB

  Warning: Ignoring non-zero exit code.

Benchmark 4: Pyright
  Time (mean ± σ):      2.824 s ±  0.019 s    [User: 5.539 s, System: 0.183 s]
  Range (min … max):    2.801 s …  2.862 s    10 runs
  Memory (peak RSS):  749.2 MiB

  Warning: Ignoring non-zero exit code.

Benchmark 5: Zuban
  Time (mean ± σ):     948.1 ms ±   2.5 ms    [User: 1404.3 ms, System: 56.5 ms]
  Range (min … max):   944.5 ms … 952.8 ms    10 runs
  Memory (peak RSS):  224.4 MiB

  Warning: Ignoring non-zero exit code.

Summary
  ty ran
    2.57 ± 0.17 times faster than Pyrefly
    8.96 ± 0.49 times faster than Zuban
   26.69 ± 1.47 times faster than Pyright
   67.98 ± 3.82 times faster than mypy

-------------------------------------------------------------------------------

pytorch
-------

Benchmark 1: ty
  Time (mean ± σ):      1.284 s ±  0.035 s    [User: 16.342 s, System: 0.992 s]
  Range (min … max):    1.243 s …  1.363 s    10 runs
  Memory (peak RSS):  1,595 MiB

  Warning: Ignoring non-zero exit code.

Benchmark 2: Pyrefly
  Time (mean ± σ):      1.205 s ±  0.015 s    [User: 14.735 s, System: 0.293 s]
  Range (min … max):    1.189 s …  1.230 s    10 runs
  Memory (peak RSS):  908.9 MiB

  Warning: Ignoring non-zero exit code.

Benchmark 3: mypy
  Time (mean ± σ):     25.373 s ±  0.057 s    [User: 25.604 s, System: 0.708 s]
  Range (min … max):   25.295 s … 25.455 s    10 runs
  Memory (peak RSS):  1,845 MiB

  Warning: Ignoring non-zero exit code.

Benchmark 4: Pyright
  Time (mean ± σ):     74.008 s ±  1.512 s    [User: 129.838 s, System: 2.101 s]
  Range (min … max):   72.061 s … 77.481 s    10 runs
  Memory (peak RSS):  4,179 MiB

  Warning: Ignoring non-zero exit code.

Benchmark 5: Zuban
  Time (mean ± σ):      3.464 s ±  0.020 s    [User: 14.275 s, System: 0.375 s]
  Range (min … max):    3.435 s …  3.502 s    10 runs
  Memory (peak RSS):  752.5 MiB

  Warning: Ignoring non-zero exit code.

Summary
  Pyrefly ran
    1.07 ± 0.03 times faster than ty
    2.87 ± 0.04 times faster than Zuban
   21.05 ± 0.26 times faster than mypy
   61.41 ± 1.46 times faster than Pyright

-------------------------------------------------------------------------------

httpx
-----

Benchmark 1: ty
  Time (mean ± σ):      64.6 ms ±   1.7 ms    [User: 221.4 ms, System: 17.5 ms]
  Range (min … max):    61.6 ms …  68.1 ms    34 runs
  Memory (peak RSS):  105.3 MiB

  Warning: Ignoring non-zero exit code.

Benchmark 2: Pyrefly
  Time (mean ± σ):     117.9 ms ±   2.5 ms    [User: 238.7 ms, System: 37.8 ms]
  Range (min … max):   115.5 ms … 123.5 ms    20 runs
  Memory (peak RSS):  129.9 MiB

  Warning: Ignoring non-zero exit code.

Benchmark 3: mypy
  Time (mean ± σ):     901.8 ms ±  10.3 ms    [User: 840.0 ms, System: 145.8 ms]
  Range (min … max):   886.7 ms … 919.9 ms    10 runs
  Memory (peak RSS):  190.2 MiB

  Warning: Ignoring non-zero exit code.

Benchmark 4: Pyright
  Time (mean ± σ):     950.0 ms ±  12.4 ms    [User: 1849.5 ms, System: 86.2 ms]
  Range (min … max):   937.0 ms … 982.0 ms    10 runs
  Memory (peak RSS):  362.1 MiB

  Warning: Ignoring non-zero exit code.

Benchmark 5: Zuban
  Time (mean ± σ):     104.8 ms ±   1.4 ms    [User: 259.2 ms, System: 18.4 ms]
  Range (min … max):   101.7 ms … 106.9 ms    23 runs
  Memory (peak RSS):   66.4 MiB

  Warning: Ignoring non-zero exit code.

Summary
  ty ran
    1.62 ± 0.05 times faster than Zuban
    1.82 ± 0.06 times faster than Pyrefly
   13.95 ± 0.40 times faster than mypy
   14.70 ± 0.43 times faster than Pyright

-------------------------------------------------------------------------------

numpy
-----

Benchmark 1: ty
  Time (mean ± σ):     353.7 ms ±  16.0 ms    [User: 1461.5 ms, System: 69.7 ms]
  Range (min … max):   329.6 ms … 383.3 ms    10 runs
  Memory (peak RSS):  294.1 MiB

  Warning: Ignoring non-zero exit code.

Benchmark 2: Pyrefly
  Time (mean ± σ):     581.6 ms ±  29.3 ms    [User: 3878.6 ms, System: 100.1 ms]
  Range (min … max):   557.8 ms … 637.3 ms    10 runs
  Memory (peak RSS):  518.6 MiB

  Warning: Ignoring non-zero exit code.

Benchmark 3: mypy
  Time (mean ± σ):     80.920 s ±  0.615 s    [User: 80.695 s, System: 0.315 s]
  Range (min … max):   79.889 s … 81.920 s    10 runs
  Memory (peak RSS):  642.5 MiB

  Warning: Ignoring non-zero exit code.

Benchmark 4: Pyright
  Time (mean ± σ):     21.217 s ±  0.079 s    [User: 26.500 s, System: 0.491 s]
  Range (min … max):   21.132 s … 21.345 s    10 runs
  Memory (peak RSS):  1,536 MiB

  Warning: Ignoring non-zero exit code.

Benchmark 5: Zuban
  Root preflight timed out after 600 seconds.

Summary
  ty ran
     1.64 ±  0.11 times faster than Pyrefly
    59.99 ±  2.72 times faster than Pyright
   228.80 ± 10.50 times faster than mypy

-------------------------------------------------------------------------------

fastapi
-------

Benchmark 1: ty
  Time (mean ± σ):      89.1 ms ±   2.7 ms    [User: 388.5 ms, System: 27.1 ms]
  Range (min … max):    85.6 ms …  96.7 ms    26 runs
  Memory (peak RSS):  143.3 MiB

  Warning: Ignoring non-zero exit code.

Benchmark 2: Pyrefly
  Time (mean ± σ):     297.2 ms ±   3.5 ms    [User: 713.6 ms, System: 53.1 ms]
  Range (min … max):   292.8 ms … 304.7 ms    10 runs
  Memory (peak RSS):  193.4 MiB

  Warning: Ignoring non-zero exit code.

Benchmark 3: mypy
  Time (mean ± σ):      1.953 s ±  0.018 s    [User: 1.866 s, System: 0.318 s]
  Range (min … max):    1.936 s …  1.986 s    10 runs
  Memory (peak RSS):  333.8 MiB

  Warning: Ignoring non-zero exit code.

Benchmark 4: Pyright
  Time (mean ± σ):      2.216 s ±  0.012 s    [User: 4.155 s, System: 0.153 s]
  Range (min … max):    2.196 s …  2.234 s    10 runs
  Memory (peak RSS):  493.5 MiB

  Warning: Ignoring non-zero exit code.

Benchmark 5: Zuban
  Time (mean ± σ):     191.1 ms ±   2.3 ms    [User: 586.4 ms, System: 32.0 ms]
  Range (min … max):   188.2 ms … 195.6 ms    14 runs
  Memory (peak RSS):   89.2 MiB

  Warning: Ignoring non-zero exit code.

Summary
  ty ran
    2.15 ± 0.07 times faster than Zuban
    3.34 ± 0.11 times faster than Pyrefly
   21.93 ± 0.68 times faster than mypy
   24.88 ± 0.75 times faster than Pyright

-------------------------------------------------------------------------------

sqlalchemy
----------

Benchmark 1: ty
  Time (mean ± σ):     305.6 ms ±  18.1 ms    [User: 3415.5 ms, System: 139.8 ms]
  Range (min … max):   289.8 ms … 337.6 ms    10 runs
  Memory (peak RSS):  412.0 MiB

  Warning: Ignoring non-zero exit code.

Benchmark 2: Pyrefly
  Time (mean ± σ):     304.0 ms ±   7.3 ms    [User: 2506.4 ms, System: 72.4 ms]
  Range (min … max):   291.3 ms … 318.0 ms    10 runs
  Memory (peak RSS):  298.7 MiB

  Warning: Ignoring non-zero exit code.

Benchmark 3: mypy
  Time (mean ± σ):      3.932 s ±  0.032 s    [User: 3.931 s, System: 0.162 s]
  Range (min … max):    3.894 s …  4.018 s    10 runs
  Memory (peak RSS):  422.6 MiB

  Warning: Ignoring non-zero exit code.

Benchmark 4: Pyright
  Time (mean ± σ):      9.799 s ±  0.076 s    [User: 15.914 s, System: 0.436 s]
  Range (min … max):    9.687 s …  9.903 s    10 runs
  Memory (peak RSS):  1,429 MiB

  Warning: Ignoring non-zero exit code.

Benchmark 5: Zuban
  Time (mean ± σ):     660.8 ms ±   4.1 ms    [User: 2308.5 ms, System: 63.6 ms]
  Range (min … max):   654.3 ms … 667.3 ms    10 runs
  Memory (peak RSS):  168.8 MiB

  Warning: Ignoring non-zero exit code.

Summary
  Pyrefly ran
    1.01 ± 0.06 times faster than ty
    2.17 ± 0.05 times faster than Zuban
   12.93 ± 0.33 times faster than mypy
   32.23 ± 0.81 times faster than Pyright

-------------------------------------------------------------------------------

rich
----

Benchmark 1: ty
  Time (mean ± σ):      63.0 ms ±   3.0 ms    [User: 401.0 ms, System: 30.9 ms]
  Range (min … max):    58.6 ms …  70.0 ms    35 runs
  Memory (peak RSS):  122.6 MiB

  Warning: Ignoring non-zero exit code.

Benchmark 2: Pyrefly
  Time (mean ± σ):     122.8 ms ±   3.4 ms    [User: 486.1 ms, System: 41.0 ms]
  Range (min … max):   115.1 ms … 127.8 ms    20 runs
  Memory (peak RSS):  133.5 MiB

  Warning: Ignoring non-zero exit code.

Benchmark 3: mypy
  Time (mean ± σ):      1.209 s ±  0.014 s    [User: 1.148 s, System: 0.190 s]
  Range (min … max):    1.198 s …  1.237 s    10 runs
  Memory (peak RSS):  226.2 MiB

  Warning: Ignoring non-zero exit code.

Benchmark 4: Pyright
  Time (mean ± σ):      2.511 s ±  0.008 s    [User: 4.533 s, System: 0.148 s]
  Range (min … max):    2.497 s …  2.520 s    10 runs
  Memory (peak RSS):  498.1 MiB

  Warning: Ignoring non-zero exit code.

Benchmark 5: Zuban
  Time (mean ± σ):     130.2 ms ±   2.3 ms    [User: 531.8 ms, System: 26.2 ms]
  Range (min … max):   125.4 ms … 133.9 ms    19 runs
  Memory (peak RSS):   79.7 MiB

  Warning: Ignoring non-zero exit code.

Summary
  ty ran
    1.95 ± 0.11 times faster than Pyrefly
    2.06 ± 0.11 times faster than Zuban
   19.19 ± 0.95 times faster than mypy
   39.85 ± 1.92 times faster than Pyright

-------------------------------------------------------------------------------

django
------

Benchmark 1: ty
  Time (mean ± σ):     243.4 ms ±   6.2 ms    [User: 2429.1 ms, System: 563.8 ms]
  Range (min … max):   233.9 ms … 253.3 ms    11 runs
  Memory (peak RSS):  340.8 MiB

  Warning: Ignoring non-zero exit code.

Benchmark 2: Pyrefly
  Time (mean ± σ):     259.8 ms ±   3.9 ms    [User: 1621.8 ms, System: 441.3 ms]
  Range (min … max):   254.3 ms … 266.2 ms    10 runs
  Memory (peak RSS):  262.9 MiB

  Warning: Ignoring non-zero exit code.

Benchmark 3: mypy
  Time (mean ± σ):      2.446 s ±  0.018 s    [User: 2.356 s, System: 0.259 s]
  Range (min … max):    2.423 s …  2.489 s    10 runs
  Memory (peak RSS):  324.9 MiB

  Warning: Ignoring non-zero exit code.

Benchmark 4: Pyright
  Time (mean ± σ):      6.931 s ±  0.048 s    [User: 11.601 s, System: 0.462 s]
  Range (min … max):    6.859 s …  6.999 s    10 runs
  Memory (peak RSS):  1,211 MiB

  Warning: Ignoring non-zero exit code.

Benchmark 5: Zuban
  Time (mean ± σ):     510.8 ms ±   6.1 ms    [User: 2330.7 ms, System: 135.1 ms]
  Range (min … max):   503.6 ms … 522.3 ms    10 runs
  Memory (peak RSS):  180.1 MiB

  Warning: Ignoring non-zero exit code.

Summary
  ty ran
    1.07 ± 0.03 times faster than Pyrefly
    2.10 ± 0.06 times faster than Zuban
   10.05 ± 0.27 times faster than mypy
   28.48 ± 0.75 times faster than Pyright

-------------------------------------------------------------------------------

sympy
-----

Benchmark 1: ty
  Time (mean ± σ):     727.9 ms ±  19.7 ms    [User: 8815.7 ms, System: 665.0 ms]
  Range (min … max):   695.0 ms … 763.5 ms    10 runs
  Memory (peak RSS):  718.0 MiB

  Warning: Ignoring non-zero exit code.

Benchmark 2: Pyrefly
  Time (mean ± σ):     527.0 ms ±   5.9 ms    [User: 5470.9 ms, System: 124.5 ms]
  Range (min … max):   518.6 ms … 537.1 ms    10 runs
  Memory (peak RSS):  509.3 MiB

  Warning: Ignoring non-zero exit code.

Benchmark 3: mypy
  Time (mean ± σ):      6.645 s ±  0.028 s    [User: 6.713 s, System: 0.229 s]
  Range (min … max):    6.604 s …  6.699 s    10 runs
  Memory (peak RSS):  652.8 MiB

  Warning: Ignoring non-zero exit code.

Benchmark 4: Pyright
  Time (mean ± σ):     30.048 s ±  0.168 s    [User: 42.705 s, System: 0.973 s]
  Range (min … max):   29.701 s … 30.307 s    10 runs
  Memory (peak RSS):  3,323 MiB

  Warning: Ignoring non-zero exit code.

Benchmark 5: Zuban
  Time (mean ± σ):      1.230 s ±  0.008 s    [User: 5.165 s, System: 0.134 s]
  Range (min … max):    1.221 s …  1.250 s    10 runs
  Memory (peak RSS):  299.8 MiB

  Warning: Ignoring non-zero exit code.

Summary
  Pyrefly ran
    1.38 ± 0.04 times faster than ty
    2.33 ± 0.03 times faster than Zuban
   12.61 ± 0.15 times faster than mypy
   57.02 ± 0.72 times faster than Pyright

-------------------------------------------------------------------------------

openai
------

Benchmark 1: ty
  Time (mean ± σ):     282.0 ms ±  13.4 ms    [User: 2457.0 ms, System: 454.5 ms]
  Range (min … max):   267.6 ms … 301.2 ms    10 runs
  Memory (peak RSS):  356.5 MiB

  Warning: Ignoring non-zero exit code.

Benchmark 2: Pyrefly
  Time (mean ± σ):     464.0 ms ±  11.7 ms    [User: 3734.1 ms, System: 152.2 ms]
  Range (min … max):   446.7 ms … 485.9 ms    10 runs
  Memory (peak RSS):  409.3 MiB

  Warning: Ignoring non-zero exit code.

Benchmark 3: mypy
  Time (mean ± σ):      6.770 s ±  0.034 s    [User: 6.600 s, System: 0.500 s]
  Range (min … max):    6.728 s …  6.834 s    10 runs
  Memory (peak RSS):  651.0 MiB

  Warning: Ignoring non-zero exit code.

Benchmark 4: Pyright
  Time (mean ± σ):      8.170 s ±  0.067 s    [User: 12.695 s, System: 0.467 s]
  Range (min … max):    8.015 s …  8.254 s    10 runs
  Memory (peak RSS):  1,424 MiB

  Warning: Ignoring non-zero exit code.

Benchmark 5: Zuban
  Time (mean ± σ):     861.1 ms ±   8.9 ms    [User: 2429.3 ms, System: 115.1 ms]
  Range (min … max):   848.4 ms … 874.6 ms    10 runs
  Memory (peak RSS):  209.5 MiB

  Warning: Ignoring non-zero exit code.

Summary
  ty ran
    1.65 ± 0.09 times faster than Pyrefly
    3.05 ± 0.15 times faster than Zuban
   24.00 ± 1.14 times faster than mypy
   28.97 ± 1.39 times faster than Pyright

-------------------------------------------------------------------------------

pytest
------

Benchmark 1: ty
  Time (mean ± σ):     168.1 ms ±  11.3 ms    [User: 1361.0 ms, System: 81.1 ms]
  Range (min … max):   139.6 ms … 181.6 ms    14 runs
  Memory (peak RSS):  249.3 MiB

  Warning: Ignoring non-zero exit code.

Benchmark 2: Pyrefly
  Time (mean ± σ):     227.2 ms ±  21.9 ms    [User: 1422.4 ms, System: 62.1 ms]
  Range (min … max):   191.5 ms … 252.9 ms    12 runs
  Memory (peak RSS):  246.0 MiB

  Warning: Ignoring non-zero exit code.

Benchmark 3: mypy
  Time (mean ± σ):      2.381 s ±  0.025 s    [User: 2.345 s, System: 0.215 s]
  Range (min … max):    2.361 s …  2.442 s    10 runs
  Memory (peak RSS):  371.8 MiB

  Warning: Ignoring non-zero exit code.

Benchmark 4: Pyright
  Time (mean ± σ):      4.574 s ±  0.030 s    [User: 8.547 s, System: 0.250 s]
  Range (min … max):    4.513 s …  4.610 s    10 runs
  Memory (peak RSS):  903.3 MiB

  Warning: Ignoring non-zero exit code.

Benchmark 5: Zuban
  Time (mean ± σ):     590.6 ms ±   5.4 ms    [User: 1659.5 ms, System: 59.6 ms]
  Range (min … max):   582.2 ms … 598.7 ms    10 runs
  Memory (peak RSS):  166.5 MiB

  Warning: Ignoring non-zero exit code.

Summary
  ty ran
    1.35 ± 0.16 times faster than Pyrefly
    3.51 ± 0.24 times faster than Zuban
   14.16 ± 0.96 times faster than mypy
   27.21 ± 1.84 times faster than Pyright
```

## LSP

### Incremental edit

Zuban's server crashed on the incremental edits in discord.py, NumPy, and PyTorch.

```shell
---------------------------------------------------------------------------------------- benchmark 'black': 4 tests ----------------------------------------------------------------------------------------
Name (time in ms)                             Min                 Max                Mean            StdDev              Median               IQR            Outliers      OPS            Rounds  Iterations
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_incremental_edit[black-ty]           14.9345 (1.0)       15.7683 (1.0)       15.2888 (1.0)      0.2579 (1.0)       15.2973 (1.0)      0.3725 (1.0)           3;0  65.4074 (1.0)          10           1
test_incremental_edit[black-zuban]        18.8832 (1.26)      20.8855 (1.32)      19.3794 (1.27)     0.6267 (2.43)      19.2328 (1.26)     0.5062 (1.36)          2;1  51.6012 (0.79)         10           1
test_incremental_edit[black-pyrefly]      86.7763 (5.81)      97.2985 (6.17)      91.4009 (5.98)     3.0032 (11.65)     91.2891 (5.97)     4.0361 (10.84)         2;0  10.9408 (0.17)         10           1
test_incremental_edit[black-pyright]     540.2310 (36.17)    562.2411 (35.66)    549.4405 (35.94)    6.7233 (26.07)    548.0737 (35.83)    8.5098 (22.85)         4;0   1.8200 (0.03)         10           1
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

----------------------------------------------------------------------------------------- benchmark 'discord.py': 3 tests -----------------------------------------------------------------------------------------
Name (time in ms)                                  Min                 Max                Mean             StdDev              Median                IQR            Outliers      OPS            Rounds  Iterations
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_incremental_edit[discord.py-ty]           25.5978 (1.0)       27.0605 (1.0)       25.8959 (1.0)       0.4492 (1.0)       25.6740 (1.0)       0.4117 (1.0)           1;1  38.6161 (1.0)          10           1
test_incremental_edit[discord.py-pyrefly]      72.6280 (2.84)      82.8766 (3.06)      76.5269 (2.96)      3.7789 (8.41)      74.9435 (2.92)      7.2071 (17.51)         4;0  13.0673 (0.34)         10           1
test_incremental_edit[discord.py-pyright]     488.6511 (19.09)    541.3492 (20.01)    517.2384 (19.97)    16.5382 (36.81)    512.2913 (19.95)    22.0510 (53.57)         3;0   1.9333 (0.05)         10           1
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

---------------------------------------------------------------------------------------- benchmark 'homeassistant': 4 tests ----------------------------------------------------------------------------------------
Name (time in ms)                                     Min                 Max                Mean            StdDev              Median               IQR            Outliers      OPS            Rounds  Iterations
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_incremental_edit[homeassistant-ty]           28.8210 (1.0)       29.8624 (1.0)       29.1548 (1.0)      0.3420 (1.0)       29.0025 (1.0)      0.3946 (1.00)          2;0  34.2997 (1.0)          10           1
test_incremental_edit[homeassistant-pyrefly]      55.8462 (1.94)      85.5288 (2.86)      75.6855 (2.60)     8.0570 (23.56)     76.3312 (2.63)     4.9400 (12.58)         3;1  13.2126 (0.39)         10           1
test_incremental_edit[homeassistant-zuban]        56.2561 (1.95)      57.5430 (1.93)      57.0332 (1.96)     0.3593 (1.05)      57.0851 (1.97)     0.3927 (1.0)           2;0  17.5336 (0.51)         10           1
test_incremental_edit[homeassistant-pyright]     564.8898 (19.60)    580.5012 (19.44)    574.4756 (19.70)    4.9935 (14.60)    573.7045 (19.78)    6.9113 (17.60)         3;0   1.7407 (0.05)         10           1
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

----------------------------------------------------------------------------------------- benchmark 'isort': 4 tests ----------------------------------------------------------------------------------------
Name (time in ms)                             Min                 Max                Mean            StdDev              Median               IQR            Outliers       OPS            Rounds  Iterations
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_incremental_edit[isort-zuban]         5.6747 (1.0)        5.9072 (1.0)        5.7474 (1.0)      0.0701 (1.0)        5.7302 (1.0)      0.0773 (1.0)           2;1  173.9902 (1.0)          10           1
test_incremental_edit[isort-ty]           21.2606 (3.75)      22.9108 (3.88)      21.7873 (3.79)     0.5132 (7.33)      21.6626 (3.78)     0.6240 (8.07)          2;0   45.8982 (0.26)         10           1
test_incremental_edit[isort-pyrefly]      42.7818 (7.54)      57.5799 (9.75)      52.8906 (9.20)     4.5220 (64.55)     54.9351 (9.59)     5.5654 (71.97)         2;0   18.9070 (0.11)         10           1
test_incremental_edit[isort-pyright]     419.7210 (73.96)    429.1457 (72.65)    425.1017 (73.96)    2.9371 (41.93)    424.9466 (74.16)    4.3485 (56.23)         3;0    2.3524 (0.01)         10           1
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

----------------------------------------------------------------------------------------- benchmark 'jinja': 4 tests -----------------------------------------------------------------------------------------
Name (time in ms)                             Min                 Max                Mean             StdDev              Median                IQR            Outliers      OPS            Rounds  Iterations
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_incremental_edit[jinja-ty]           11.7501 (1.0)       12.0747 (1.0)       11.9111 (1.0)       0.1135 (1.0)       11.9132 (1.0)       0.2005 (1.11)          3;0  83.9554 (1.0)          10           1
test_incremental_edit[jinja-zuban]        19.9754 (1.70)      20.4125 (1.69)      20.1366 (1.69)      0.1340 (1.18)      20.1239 (1.69)      0.1803 (1.0)           3;0  49.6609 (0.59)         10           1
test_incremental_edit[jinja-pyrefly]      53.2751 (4.53)      67.2008 (5.57)      60.3027 (5.06)      4.5815 (40.37)     59.1167 (4.96)      5.8406 (32.40)         4;0  16.5830 (0.20)         10           1
test_incremental_edit[jinja-pyright]     476.3300 (40.54)    530.7210 (43.95)    503.8855 (42.30)    14.1706 (124.87)   505.3668 (42.42)    11.4062 (63.28)         2;2   1.9846 (0.02)         10           1
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

---------------------------------------------------------------------------------------- benchmark 'pandas': 4 tests -----------------------------------------------------------------------------------------
Name (time in ms)                              Min                 Max                Mean             StdDev              Median               IQR            Outliers      OPS            Rounds  Iterations
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_incremental_edit[pandas-ty]           48.8566 (1.0)       61.1785 (1.0)       52.7416 (1.0)       4.6492 (2.08)      50.6834 (1.0)      5.0680 (2.45)          2;0  18.9604 (1.0)          10           1
test_incremental_edit[pandas-pyrefly]     243.4753 (4.98)     256.9783 (4.20)     248.6074 (4.71)      4.2473 (1.90)     247.6178 (4.89)     6.6526 (3.21)          2;0   4.0224 (0.21)         10           1
test_incremental_edit[pandas-zuban]       251.8713 (5.16)     259.0576 (4.23)     254.0977 (4.82)      2.2326 (1.0)      253.3567 (5.00)     2.0706 (1.0)           2;1   3.9355 (0.21)         10           1
test_incremental_edit[pandas-pyright]     662.6549 (13.56)    701.7632 (11.47)    691.2085 (13.11)    11.6618 (5.22)     695.5558 (13.72)    8.8209 (4.26)          1;1   1.4467 (0.08)         10           1
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

------------------------------------------------------------------------------------------ benchmark 'prefect': 4 tests -----------------------------------------------------------------------------------------
Name (time in ms)                               Min                 Max                Mean             StdDev              Median                IQR            Outliers       OPS            Rounds  Iterations
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_incremental_edit[prefect-ty]            7.7752 (1.0)        8.1272 (1.0)        7.9830 (1.0)       0.1016 (1.0)        7.9694 (1.0)       0.0893 (1.0)           3;1  125.2669 (1.0)          10           1
test_incremental_edit[prefect-pyrefly]      51.3062 (6.60)      61.9334 (7.62)      56.2614 (7.05)      3.5354 (34.79)     57.8409 (7.26)      5.8660 (65.69)         4;0   17.7742 (0.14)         10           1
test_incremental_edit[prefect-zuban]       131.5461 (16.92)    132.8311 (16.34)    132.0289 (16.54)     0.4032 (3.97)     131.9307 (16.55)     0.4938 (5.53)          3;0    7.5741 (0.06)         10           1
test_incremental_edit[prefect-pyright]     660.4608 (84.94)    695.6145 (85.59)    680.8583 (85.29)    10.4803 (103.14)   682.6589 (85.66)    14.5401 (162.84)        3;0    1.4687 (0.01)         10           1
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

----------------------------------------------------------------------------------------- benchmark 'pytorch': 3 tests ----------------------------------------------------------------------------------------
Name (time in ms)                               Min                 Max                Mean            StdDev              Median               IQR            Outliers       OPS            Rounds  Iterations
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_incremental_edit[pytorch-ty]            3.9069 (1.0)        4.3608 (1.0)        4.1409 (1.0)      0.1308 (1.0)        4.1477 (1.0)      0.0598 (1.0)           4;4  241.4929 (1.0)          10           1
test_incremental_edit[pytorch-pyrefly]      20.1780 (5.16)      25.2127 (5.78)      22.7988 (5.51)     1.8837 (14.40)     23.4518 (5.65)     3.4646 (57.90)         4;0   43.8619 (0.18)         10           1
test_incremental_edit[pytorch-pyright]     411.6034 (105.35)   420.5795 (96.45)    416.2569 (100.52)   2.2362 (17.10)    416.0866 (100.32)   1.0938 (18.28)         2;2    2.4024 (0.01)         10           1
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

------------------------------------------------------------------------------------------ benchmark 'httpx': 4 tests -----------------------------------------------------------------------------------------
Name (time in ms)                             Min                 Max                Mean             StdDev              Median                IQR            Outliers       OPS            Rounds  Iterations
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_incremental_edit[httpx-ty]            8.6818 (1.0)        9.1608 (1.0)        8.8883 (1.0)       0.1352 (1.0)        8.8819 (1.0)       0.0940 (1.0)           3;2  112.5077 (1.0)          10           1
test_incremental_edit[httpx-zuban]         9.5517 (1.10)      11.7660 (1.28)       9.9430 (1.12)      0.6486 (4.80)       9.7386 (1.10)      0.1877 (2.00)          1;1  100.5729 (0.89)         10           1
test_incremental_edit[httpx-pyrefly]      47.6866 (5.49)      57.0288 (6.23)      51.7039 (5.82)      2.8466 (21.05)     52.0920 (5.86)      3.3798 (35.96)         3;0   19.3409 (0.17)         10           1
test_incremental_edit[httpx-pyright]     414.3220 (47.72)    441.5353 (48.20)    426.5495 (47.99)    10.4990 (77.63)    426.0099 (47.96)    20.2930 (215.88)        5;0    2.3444 (0.02)         10           1
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------------- benchmark 'numpy': 3 tests --------------------------------------------------------------------------------------------
Name (time in ms)                               Min                   Max                  Mean             StdDev                Median               IQR            Outliers      OPS            Rounds  Iterations
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_incremental_edit[numpy-ty]             29.2499 (1.0)         30.1583 (1.0)         29.8652 (1.0)       0.2584 (1.0)         29.8794 (1.0)      0.2702 (1.0)           3;1  33.4838 (1.0)          10           1
test_incremental_edit[numpy-pyrefly]       330.8268 (11.31)      350.2634 (11.61)      343.7851 (11.51)     6.4024 (24.78)      346.1157 (11.58)    7.2750 (26.93)         3;0   2.9088 (0.09)         10           1
test_incremental_edit[numpy-pyright]     1,171.7334 (40.06)    1,205.3624 (39.97)    1,188.2385 (39.79)    10.2539 (39.69)    1,189.4224 (39.81)    9.2393 (34.20)         3;0   0.8416 (0.03)         10           1
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

----------------------------------------------------------------------------------------- benchmark 'fastapi': 4 tests ----------------------------------------------------------------------------------------
Name (time in ms)                               Min                 Max                Mean            StdDev              Median               IQR            Outliers       OPS            Rounds  Iterations
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_incremental_edit[fastapi-ty]            7.3193 (1.0)        8.4987 (1.0)        7.6943 (1.0)      0.3215 (2.51)       7.6806 (1.0)      0.2322 (1.30)          2;1  129.9665 (1.0)          10           1
test_incremental_edit[fastapi-zuban]         8.3563 (1.14)       8.7793 (1.03)       8.5171 (1.11)     0.1283 (1.0)        8.4884 (1.11)     0.1784 (1.0)           2;0  117.4108 (0.90)         10           1
test_incremental_edit[fastapi-pyrefly]      58.2667 (7.96)      69.4830 (8.18)      65.8294 (8.56)     3.4123 (26.60)     67.0105 (8.72)     4.0596 (22.76)         2;0   15.1908 (0.12)         10           1
test_incremental_edit[fastapi-pyright]     604.3037 (82.56)    621.4753 (73.13)    614.2073 (79.83)    5.5771 (43.48)    614.2024 (79.97)    8.3417 (46.76)         3;0    1.6281 (0.01)         10           1
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

---------------------------------------------------------------------------------------- benchmark 'sqlalchemy': 4 tests ----------------------------------------------------------------------------------------
Name (time in ms)                                  Min                 Max                Mean            StdDev              Median               IQR            Outliers      OPS            Rounds  Iterations
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_incremental_edit[sqlalchemy-ty]           12.7042 (1.0)       13.4422 (1.0)       13.0009 (1.0)      0.2226 (1.0)       12.9786 (1.0)      0.1323 (1.0)           4;2  76.9178 (1.0)          10           1
test_incremental_edit[sqlalchemy-pyrefly]      56.7484 (4.47)      84.5526 (6.29)      76.4313 (5.88)     7.9762 (35.83)     76.2125 (5.87)     7.9097 (59.77)         2;1  13.0836 (0.17)         10           1
test_incremental_edit[sqlalchemy-zuban]       198.5378 (15.63)    201.8470 (15.02)    199.5849 (15.35)    0.9838 (4.42)     199.1490 (15.34)    1.1792 (8.91)          2;0   5.0104 (0.07)         10           1
test_incremental_edit[sqlalchemy-pyright]     632.0858 (49.75)    647.3986 (48.16)    639.0595 (49.16)    5.6518 (25.39)    640.6409 (49.36)    9.4287 (71.25)         5;0   1.5648 (0.02)         10           1
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

----------------------------------------------------------------------------------------- benchmark 'rich': 4 tests -----------------------------------------------------------------------------------------
Name (time in ms)                            Min                 Max                Mean            StdDev              Median                IQR            Outliers       OPS            Rounds  Iterations
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_incremental_edit[rich-ty]            5.6801 (1.0)        6.0007 (1.0)        5.8440 (1.0)      0.0861 (1.0)        5.8600 (1.0)       0.0900 (1.0)           2;0  171.1165 (1.0)          10           1
test_incremental_edit[rich-zuban]        12.7459 (2.24)      14.8288 (2.47)      13.1219 (2.25)     0.6140 (7.13)      12.9070 (2.20)      0.2442 (2.71)          1;1   76.2082 (0.45)         10           1
test_incremental_edit[rich-pyrefly]      20.0278 (3.53)      41.4377 (6.91)      31.1428 (5.33)     7.2154 (83.77)     34.0170 (5.80)     12.2488 (136.03)        4;0   32.1102 (0.19)         10           1
test_incremental_edit[rich-pyright]     433.5527 (76.33)    446.9955 (74.49)    440.7714 (75.42)    4.4355 (51.50)    442.3849 (75.49)     6.2345 (69.24)         3;0    2.2687 (0.01)         10           1
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

----------------------------------------------------------------------------------------- benchmark 'django': 4 tests ------------------------------------------------------------------------------------------
Name (time in ms)                              Min                 Max                Mean             StdDev              Median                IQR            Outliers       OPS            Rounds  Iterations
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_incremental_edit[django-zuban]         1.7699 (1.0)        1.9427 (1.0)        1.8348 (1.0)       0.0613 (1.0)        1.8271 (1.0)       0.1039 (1.0)           4;0  545.0284 (1.0)          10           1
test_incremental_edit[django-ty]            3.8018 (2.15)       4.1381 (2.13)       3.9516 (2.15)      0.1394 (2.27)       3.9362 (2.15)      0.2693 (2.59)          5;0  253.0642 (0.46)         10           1
test_incremental_edit[django-pyrefly]      21.2110 (11.98)     29.9794 (15.43)     25.4880 (13.89)     3.1539 (51.45)     26.3823 (14.44)     5.5899 (53.81)         4;0   39.2342 (0.07)         10           1
test_incremental_edit[django-pyright]     330.7418 (186.87)   381.0605 (196.15)   354.0818 (192.98)   21.3677 (348.54)   341.3754 (186.84)   39.9063 (384.17)        5;0    2.8242 (0.01)         10           1
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

----------------------------------------------------------------------------------------- benchmark 'sympy': 4 tests -----------------------------------------------------------------------------------------
Name (time in ms)                             Min                 Max                Mean            StdDev              Median                IQR            Outliers       OPS            Rounds  Iterations
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_incremental_edit[sympy-ty]            3.3961 (1.0)        3.7663 (1.0)        3.5309 (1.0)      0.1102 (1.0)        3.5280 (1.0)       0.1257 (1.0)           3;0  283.2159 (1.0)          10           1
test_incremental_edit[sympy-pyrefly]      28.2025 (8.30)      38.2077 (10.14)     33.0703 (9.37)     3.0461 (27.65)     32.1000 (9.10)      4.1055 (32.67)         3;0   30.2386 (0.11)         10           1
test_incremental_edit[sympy-zuban]        62.8081 (18.49)     67.0972 (17.82)     63.7676 (18.06)    1.3140 (11.93)     63.3715 (17.96)     0.7175 (5.71)          1;2   15.6819 (0.06)         10           1
test_incremental_edit[sympy-pyright]     465.8610 (137.18)   487.8697 (129.54)   479.7846 (135.88)   7.3209 (66.45)    478.8293 (135.72)   10.6199 (84.51)         3;0    2.0843 (0.01)         10           1
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

---------------------------------------------------------------------------------------- benchmark 'openai': 4 tests -----------------------------------------------------------------------------------------
Name (time in ms)                              Min                 Max                Mean            StdDev              Median               IQR            Outliers       OPS            Rounds  Iterations
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_incremental_edit[openai-zuban]         3.4460 (1.0)        3.6128 (1.0)        3.5186 (1.0)      0.0547 (1.0)        3.5069 (1.0)      0.0987 (2.04)          4;0  284.2066 (1.0)          10           1
test_incremental_edit[openai-ty]            3.9765 (1.15)       4.2988 (1.19)       4.1426 (1.18)     0.0931 (1.70)       4.1343 (1.18)     0.0484 (1.0)           3;3  241.3936 (0.85)         10           1
test_incremental_edit[openai-pyrefly]      70.9413 (20.59)     87.7718 (24.30)     82.7103 (23.51)    5.0859 (93.06)     83.1189 (23.70)    5.0480 (104.26)        1;1   12.0904 (0.04)         10           1
test_incremental_edit[openai-pyright]     457.0089 (132.62)   489.3018 (135.44)   478.7871 (136.07)   8.6623 (158.50)   481.2125 (137.22)   7.4462 (153.79)        2;1    2.0886 (0.01)         10           1
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

---------------------------------------------------------------------------------------- benchmark 'pytest': 4 tests -----------------------------------------------------------------------------------------
Name (time in ms)                              Min                 Max                Mean            StdDev              Median               IQR            Outliers       OPS            Rounds  Iterations
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_incremental_edit[pytest-ty]            8.9083 (1.0)       10.6394 (1.0)        9.1831 (1.0)      0.5201 (2.96)       9.0129 (1.0)      0.1595 (1.0)           1;1  108.8960 (1.0)          10           1
test_incremental_edit[pytest-zuban]        26.0735 (2.93)      26.7175 (2.51)      26.3351 (2.87)     0.1758 (1.0)       26.3459 (2.92)     0.2007 (1.26)          2;1   37.9721 (0.35)         10           1
test_incremental_edit[pytest-pyrefly]      55.3168 (6.21)      62.2285 (5.85)      58.5314 (6.37)     2.2135 (12.59)     58.4364 (6.48)     2.6986 (16.91)         3;0   17.0848 (0.16)         10           1
test_incremental_edit[pytest-pyright]     458.6860 (51.49)    490.4299 (46.10)    481.3327 (52.42)    8.7184 (49.58)    483.3412 (53.63)    6.7729 (42.45)         2;1    2.0776 (0.02)         10           1
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
```

### Fetch diagnostics

```shell
----------------------------------------------------------------------------------------- benchmark 'black': 4 tests ----------------------------------------------------------------------------------------
Name (time in ms)                              Min                 Max                Mean            StdDev              Median               IQR            Outliers      OPS            Rounds  Iterations
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_fetch_diagnostics[black-ty]           64.8680 (1.0)       67.6588 (1.0)       65.7677 (1.0)      0.8953 (2.18)      65.3977 (1.0)      1.3043 (2.07)          2;0  15.2050 (1.0)          10           1
test_fetch_diagnostics[black-zuban]        68.9572 (1.06)      73.7763 (1.09)      71.2262 (1.08)     1.4690 (3.57)      71.0236 (1.09)     2.1367 (3.40)          2;0  14.0398 (0.92)         10           1
test_fetch_diagnostics[black-pyrefly]     179.8352 (2.77)     181.0037 (2.68)     180.5095 (2.74)     0.4111 (1.0)      180.5079 (2.76)     0.6513 (1.03)          4;0   5.5399 (0.36)         10           1
test_fetch_diagnostics[black-pyright]     299.9607 (4.62)     302.2230 (4.47)     300.9091 (4.58)     0.6684 (1.63)     300.8832 (4.60)     0.6293 (1.0)           3;0   3.3233 (0.22)         10           1
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

----------------------------------------------------------------------------------------- benchmark 'discord.py': 4 tests ------------------------------------------------------------------------------------------
Name (time in ms)                                   Min                 Max                Mean             StdDev              Median                IQR            Outliers      OPS            Rounds  Iterations
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_fetch_diagnostics[discord.py-ty]           98.0057 (1.0)      100.5603 (1.0)       98.6685 (1.0)       0.7777 (3.09)      98.3845 (1.0)       0.7399 (3.81)          1;1  10.1349 (1.0)          10           1
test_fetch_diagnostics[discord.py-zuban]       177.4120 (1.81)     184.2058 (1.83)     180.0302 (1.82)      2.0807 (8.26)     179.8533 (1.83)      1.9461 (10.03)         3;1   5.5546 (0.55)         10           1
test_fetch_diagnostics[discord.py-pyrefly]     187.9900 (1.92)     188.8244 (1.88)     188.3708 (1.91)      0.2520 (1.0)      188.3499 (1.91)      0.1941 (1.0)           4;2   5.3087 (0.52)         10           1
test_fetch_diagnostics[discord.py-pyright]     621.1201 (6.34)     663.5259 (6.60)     630.2578 (6.39)     12.6775 (50.30)    626.5515 (6.37)     11.5769 (59.64)         1;1   1.5867 (0.16)         10           1
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------------- benchmark 'homeassistant': 4 tests ---------------------------------------------------------------------------------------------
Name (time in ms)                                        Min                   Max                  Mean             StdDev                Median                IQR            Outliers     OPS            Rounds  Iterations
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_fetch_diagnostics[homeassistant-ty]             98.7151 (1.0)        103.3118 (1.0)        100.5832 (1.0)       1.6543 (1.58)       100.4520 (1.0)       2.1908 (2.13)          4;0  9.9420 (1.0)          10           1
test_fetch_diagnostics[homeassistant-zuban]         214.2382 (2.17)       219.2897 (2.12)       217.0925 (2.16)      1.7237 (1.65)       217.0206 (2.16)      2.0827 (2.02)          4;0  4.6063 (0.46)         10           1
test_fetch_diagnostics[homeassistant-pyrefly]       236.2060 (2.39)       239.4906 (2.32)       237.6687 (2.36)      1.0456 (1.0)        237.4407 (2.36)      1.0302 (1.0)           3;0  4.2075 (0.42)         10           1
test_fetch_diagnostics[homeassistant-pyright]     1,890.3885 (19.15)    1,924.0052 (18.62)    1,905.1369 (18.94)    10.7615 (10.29)    1,903.1950 (18.95)    14.3797 (13.96)         4;0  0.5249 (0.05)         10           1
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

----------------------------------------------------------------------------------------- benchmark 'isort': 4 tests -----------------------------------------------------------------------------------------
Name (time in ms)                              Min                 Max                Mean            StdDev              Median                IQR            Outliers      OPS            Rounds  Iterations
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_fetch_diagnostics[isort-zuban]        39.6183 (1.0)       44.7363 (1.0)       41.2833 (1.0)      1.4294 (4.39)      40.9556 (1.0)       1.3667 (2.77)          2;1  24.2229 (1.0)          10           1
test_fetch_diagnostics[isort-ty]           49.8754 (1.26)      50.7970 (1.14)      50.2233 (1.22)     0.3255 (1.0)       50.0905 (1.22)      0.4929 (1.0)           3;0  19.9111 (0.82)         10           1
test_fetch_diagnostics[isort-pyrefly]     126.7168 (3.20)     140.7936 (3.15)     134.1324 (3.25)     5.9800 (18.37)    134.6929 (3.29)     11.4701 (23.27)         4;0   7.4553 (0.31)         10           1
test_fetch_diagnostics[isort-pyright]     355.6153 (8.98)     360.0408 (8.05)     358.0638 (8.67)     1.4327 (4.40)     358.1251 (8.74)      2.5620 (5.20)          4;0   2.7928 (0.12)         10           1
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

----------------------------------------------------------------------------------------- benchmark 'jinja': 4 tests ----------------------------------------------------------------------------------------
Name (time in ms)                              Min                 Max                Mean            StdDev              Median               IQR            Outliers      OPS            Rounds  Iterations
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_fetch_diagnostics[jinja-ty]           50.0174 (1.0)       51.0060 (1.0)       50.4808 (1.0)      0.3032 (1.0)       50.4843 (1.0)      0.3701 (1.0)           3;0  19.8095 (1.0)          10           1
test_fetch_diagnostics[jinja-zuban]        85.7727 (1.71)      88.3310 (1.73)      86.9519 (1.72)     0.7278 (2.40)      87.0239 (1.72)     0.7648 (2.07)          2;0  11.5006 (0.58)         10           1
test_fetch_diagnostics[jinja-pyrefly]     125.6743 (2.51)     126.7780 (2.49)     126.3703 (2.50)     0.3741 (1.23)     126.4106 (2.50)     0.6636 (1.79)          4;0   7.9133 (0.40)         10           1
test_fetch_diagnostics[jinja-pyright]     353.2582 (7.06)     361.2105 (7.08)     356.3589 (7.06)     2.3240 (7.66)     355.8286 (7.05)     3.4593 (9.35)          2;0   2.8062 (0.14)         10           1
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

---------------------------------------------------------------------------------------- benchmark 'pandas': 4 tests ----------------------------------------------------------------------------------------
Name (time in ms)                               Min                 Max                Mean            StdDev              Median               IQR            Outliers     OPS            Rounds  Iterations
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_fetch_diagnostics[pandas-ty]          376.3471 (1.0)      385.9840 (1.0)      379.3929 (1.0)      3.2335 (1.0)      378.1837 (1.0)      3.6343 (1.48)          2;0  2.6358 (1.0)          10           1
test_fetch_diagnostics[pandas-pyrefly]     539.1561 (1.43)     562.5021 (1.46)     543.9112 (1.43)     6.9893 (2.16)     541.4131 (1.43)     2.4565 (1.0)           1;2  1.8385 (0.70)         10           1
test_fetch_diagnostics[pandas-pyright]     629.9906 (1.67)     647.6225 (1.68)     639.1170 (1.68)     5.6742 (1.75)     640.4880 (1.69)     9.5839 (3.90)          4;0  1.5647 (0.59)         10           1
test_fetch_diagnostics[pandas-zuban]       666.4379 (1.77)     680.6972 (1.76)     673.7827 (1.78)     4.4995 (1.39)     673.4846 (1.78)     6.0168 (2.45)          3;0  1.4842 (0.56)         10           1
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------------- benchmark 'prefect': 4 tests ---------------------------------------------------------------------------------------------
Name (time in ms)                                  Min                   Max                  Mean             StdDev                Median                IQR            Outliers     OPS            Rounds  Iterations
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_fetch_diagnostics[prefect-ty]            163.0807 (1.0)        169.1828 (1.0)        164.7914 (1.0)       1.8633 (1.0)        164.0297 (1.0)       1.0024 (1.0)           2;2  6.0683 (1.0)          10           1
test_fetch_diagnostics[prefect-pyrefly]       332.9010 (2.04)       467.9147 (2.77)       452.5213 (2.75)     42.0522 (22.57)      465.0061 (2.83)      2.8783 (2.87)          1;1  2.2098 (0.36)         10           1
test_fetch_diagnostics[prefect-zuban]         859.7134 (5.27)       865.6050 (5.12)       863.4421 (5.24)      2.2602 (1.21)       864.5682 (5.27)      3.9808 (3.97)          3;0  1.1582 (0.19)         10           1
test_fetch_diagnostics[prefect-pyright]     1,102.1569 (6.76)     1,130.7971 (6.68)     1,113.3106 (6.76)     10.0063 (5.37)     1,112.3842 (6.78)     16.5983 (16.56)         5;0  0.8982 (0.15)         10           1
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

---------------------------------------------------------------------------------------------- benchmark 'pytorch': 4 tests ---------------------------------------------------------------------------------------------
Name (time in ms)                                  Min                   Max                  Mean             StdDev                Median                IQR            Outliers      OPS            Rounds  Iterations
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_fetch_diagnostics[pytorch-ty]             69.7632 (1.0)         72.3987 (1.0)         71.4756 (1.0)       1.0381 (1.0)         71.9118 (1.0)       1.7270 (1.0)           2;0  13.9908 (1.0)          10           1
test_fetch_diagnostics[pytorch-pyrefly]       116.7863 (1.67)       145.4521 (2.01)       128.6864 (1.80)     14.0053 (13.49)      118.9156 (1.65)     27.4318 (15.88)         4;0   7.7708 (0.56)         10           1
test_fetch_diagnostics[pytorch-pyright]       702.6213 (10.07)      709.5476 (9.80)       705.4807 (9.87)      2.5295 (2.44)       704.5238 (9.80)      4.3440 (2.52)          3;0   1.4175 (0.10)         10           1
test_fetch_diagnostics[pytorch-zuban]       1,825.0715 (26.16)    1,860.6000 (25.70)    1,835.6793 (25.68)     9.9072 (9.54)     1,835.3201 (25.52)     8.8780 (5.14)          2;1   0.5448 (0.04)         10           1
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

----------------------------------------------------------------------------------------- benchmark 'httpx': 4 tests ----------------------------------------------------------------------------------------
Name (time in ms)                              Min                 Max                Mean            StdDev              Median               IQR            Outliers      OPS            Rounds  Iterations
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_fetch_diagnostics[httpx-ty]           45.9874 (1.0)       46.5405 (1.0)       46.1683 (1.0)      0.1601 (1.0)       46.1405 (1.0)      0.1353 (1.0)           2;1  21.6599 (1.0)          10           1
test_fetch_diagnostics[httpx-zuban]        69.2425 (1.51)      71.2874 (1.53)      70.2522 (1.52)     0.6870 (4.29)      70.2971 (1.52)     0.9758 (7.21)          3;0  14.2344 (0.66)         10           1
test_fetch_diagnostics[httpx-pyrefly]     114.3010 (2.49)     118.0325 (2.54)     115.3196 (2.50)     1.1948 (7.46)     114.8530 (2.49)     1.1663 (8.62)          2;1   8.6716 (0.40)         10           1
test_fetch_diagnostics[httpx-pyright]     224.9341 (4.89)     228.4704 (4.91)     226.4147 (4.90)     1.0548 (6.59)     226.3045 (4.90)     1.0174 (7.52)          3;1   4.4167 (0.20)         10           1
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

------------------------------------------------------------------------------------------------ benchmark 'numpy': 4 tests -----------------------------------------------------------------------------------------------
Name (time in ms)                                 Min                    Max                   Mean             StdDev                 Median                 IQR            Outliers     OPS            Rounds  Iterations
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_fetch_diagnostics[numpy-ty]             311.7393 (1.0)         322.1757 (1.0)         314.2056 (1.0)       3.1423 (2.19)        313.1096 (1.0)        1.5182 (1.64)          1;2  3.1826 (1.0)          10           1
test_fetch_diagnostics[numpy-pyrefly]        562.9346 (1.81)        568.0607 (1.76)        564.3641 (1.80)      1.4365 (1.0)         564.1055 (1.80)       0.9281 (1.0)           1;1  1.7719 (0.56)         10           1
test_fetch_diagnostics[numpy-pyright]      1,182.4547 (3.79)      1,212.2849 (3.76)      1,199.6223 (3.82)      9.0291 (6.29)      1,198.6239 (3.83)      12.4973 (13.47)         3;0  0.8336 (0.26)         10           1
test_fetch_diagnostics[numpy-zuban]       36,078.9349 (115.73)   36,423.6785 (113.06)   36,193.5729 (115.19)   98.8916 (68.84)    36,198.7695 (115.61)   119.7505 (129.02)        2;1  0.0276 (0.01)         10           1
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

----------------------------------------------------------------------------------------- benchmark 'fastapi': 4 tests ----------------------------------------------------------------------------------------
Name (time in ms)                                Min                 Max                Mean            StdDev              Median               IQR            Outliers      OPS            Rounds  Iterations
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_fetch_diagnostics[fastapi-ty]           97.0200 (1.0)      101.2856 (1.0)       98.3016 (1.0)      1.2017 (2.06)      97.9454 (1.0)      1.1347 (1.86)          2;1  10.1728 (1.0)          10           1
test_fetch_diagnostics[fastapi-zuban]       171.4969 (1.77)     177.0828 (1.75)     173.4509 (1.76)     1.8097 (3.10)     173.0481 (1.77)     2.5310 (4.14)          3;0   5.7653 (0.57)         10           1
test_fetch_diagnostics[fastapi-pyrefly]     199.6927 (2.06)     201.7180 (1.99)     200.3882 (2.04)     0.5838 (1.0)      200.3402 (2.05)     0.6110 (1.0)           2;1   4.9903 (0.49)         10           1
test_fetch_diagnostics[fastapi-pyright]     457.2369 (4.71)     470.3823 (4.64)     465.9305 (4.74)     3.9981 (6.85)     466.0065 (4.76)     4.5289 (7.41)          3;1   2.1462 (0.21)         10           1
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

---------------------------------------------------------------------------------------- benchmark 'sqlalchemy': 4 tests ----------------------------------------------------------------------------------------
Name (time in ms)                                   Min                 Max                Mean            StdDev              Median               IQR            Outliers     OPS            Rounds  Iterations
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_fetch_diagnostics[sqlalchemy-ty]          212.8581 (1.0)      215.4680 (1.0)      214.1357 (1.0)      0.8579 (1.0)      214.0263 (1.0)      1.3313 (1.0)           3;0  4.6699 (1.0)          10           1
test_fetch_diagnostics[sqlalchemy-pyrefly]     250.0255 (1.17)     256.0001 (1.19)     251.9413 (1.18)     1.6665 (1.94)     251.7372 (1.18)     1.6916 (1.27)          2;1  3.9692 (0.85)         10           1
test_fetch_diagnostics[sqlalchemy-pyright]     270.1789 (1.27)     276.0185 (1.28)     272.7359 (1.27)     1.6008 (1.87)     272.7561 (1.27)     1.5684 (1.18)          2;1  3.6666 (0.79)         10           1
test_fetch_diagnostics[sqlalchemy-zuban]       383.2057 (1.80)     399.6241 (1.85)     386.9370 (1.81)     4.6166 (5.38)     385.5155 (1.80)     2.3762 (1.78)          1;1  2.5844 (0.55)         10           1
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

---------------------------------------------------------------------------------------- benchmark 'rich': 4 tests -----------------------------------------------------------------------------------------
Name (time in ms)                             Min                 Max                Mean            StdDev              Median               IQR            Outliers      OPS            Rounds  Iterations
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_fetch_diagnostics[rich-ty]           41.4694 (1.0)       41.8666 (1.0)       41.6663 (1.0)      0.1285 (1.0)       41.6513 (1.0)      0.1481 (1.0)           4;0  24.0002 (1.0)          10           1
test_fetch_diagnostics[rich-zuban]        79.5685 (1.92)      82.3503 (1.97)      80.7725 (1.94)     0.8009 (6.23)      80.6681 (1.94)     0.5338 (3.60)          3;2  12.3804 (0.52)         10           1
test_fetch_diagnostics[rich-pyrefly]      99.5237 (2.40)     115.1077 (2.75)     110.9954 (2.66)     5.6315 (43.81)    113.2185 (2.72)     1.7742 (11.98)         2;2   9.0094 (0.38)         10           1
test_fetch_diagnostics[rich-pyright]     309.8927 (7.47)     314.1458 (7.50)     311.3170 (7.47)     1.3331 (10.37)    310.9984 (7.47)     1.9001 (12.83)         3;0   3.2122 (0.13)         10           1
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

---------------------------------------------------------------------------------------- benchmark 'django': 4 tests -----------------------------------------------------------------------------------------
Name (time in ms)                               Min                 Max                Mean            StdDev              Median               IQR            Outliers      OPS            Rounds  Iterations
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_fetch_diagnostics[django-ty]           40.6335 (1.0)       41.2580 (1.0)       40.8362 (1.0)      0.1970 (1.0)       40.8098 (1.0)      0.2822 (1.0)           2;0  24.4881 (1.0)          10           1
test_fetch_diagnostics[django-zuban]        45.0162 (1.11)      47.3812 (1.15)      46.3298 (1.13)     0.7499 (3.81)      46.4050 (1.14)     0.7135 (2.53)          4;1  21.5844 (0.88)         10           1
test_fetch_diagnostics[django-pyrefly]      90.8160 (2.24)      96.1161 (2.33)      94.1640 (2.31)     2.2035 (11.19)     95.3465 (2.34)     4.3802 (15.52)         3;0  10.6198 (0.43)         10           1
test_fetch_diagnostics[django-pyright]     587.8771 (14.47)    610.7550 (14.80)    593.6576 (14.54)    8.6595 (43.96)    589.8123 (14.45)    2.7981 (9.92)          2;2   1.6845 (0.07)         10           1
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

----------------------------------------------------------------------------------------- benchmark 'sympy': 4 tests ----------------------------------------------------------------------------------------
Name (time in ms)                              Min                 Max                Mean            StdDev              Median               IQR            Outliers      OPS            Rounds  Iterations
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_fetch_diagnostics[sympy-ty]           74.5354 (1.0)       75.4191 (1.0)       74.8777 (1.0)      0.3000 (1.0)       74.7894 (1.0)      0.2066 (1.0)           4;2  13.3551 (1.0)          10           1
test_fetch_diagnostics[sympy-pyrefly]     179.4386 (2.41)     183.1834 (2.43)     180.5083 (2.41)     1.0781 (3.59)     180.2387 (2.41)     0.5938 (2.87)          1;1   5.5399 (0.41)         10           1
test_fetch_diagnostics[sympy-zuban]       260.1722 (3.49)     274.6859 (3.64)     265.9684 (3.55)     4.4955 (14.98)    264.4641 (3.54)     7.1645 (34.68)         2;0   3.7598 (0.28)         10           1
test_fetch_diagnostics[sympy-pyright]     392.3544 (5.26)     400.7913 (5.31)     396.7093 (5.30)     2.7972 (9.32)     396.7134 (5.30)     5.3469 (25.88)         4;0   2.5207 (0.19)         10           1
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

---------------------------------------------------------------------------------------- benchmark 'openai': 4 tests -----------------------------------------------------------------------------------------
Name (time in ms)                               Min                 Max                Mean            StdDev              Median               IQR            Outliers      OPS            Rounds  Iterations
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_fetch_diagnostics[openai-ty]           68.9650 (1.0)       69.2800 (1.0)       69.1050 (1.0)      0.1071 (1.0)       69.0941 (1.0)      0.1821 (1.0)           3;0  14.4707 (1.0)          10           1
test_fetch_diagnostics[openai-zuban]       139.0193 (2.02)     143.9898 (2.08)     141.1401 (2.04)     1.4470 (13.51)    140.7476 (2.04)     1.9043 (10.46)         2;0   7.0852 (0.49)         10           1
test_fetch_diagnostics[openai-pyrefly]     188.4392 (2.73)     202.4323 (2.92)     199.4188 (2.89)     5.1057 (47.66)    201.7685 (2.92)     1.2412 (6.81)          2;2   5.0146 (0.35)         10           1
test_fetch_diagnostics[openai-pyright]     513.3347 (7.44)     518.7722 (7.49)     515.7981 (7.46)     2.2311 (20.83)    515.5012 (7.46)     4.6511 (25.54)         5;0   1.9387 (0.13)         10           1
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

---------------------------------------------------------------------------------------- benchmark 'pytest': 4 tests -----------------------------------------------------------------------------------------
Name (time in ms)                               Min                 Max                Mean            StdDev              Median               IQR            Outliers      OPS            Rounds  Iterations
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_fetch_diagnostics[pytest-ty]           77.3283 (1.0)       79.4072 (1.0)       78.1006 (1.0)      0.7438 (1.0)       77.7403 (1.0)      1.0341 (1.0)           3;0  12.8040 (1.0)          10           1
test_fetch_diagnostics[pytest-zuban]       132.7784 (1.72)     135.7364 (1.71)     134.2270 (1.72)     1.0887 (1.46)     134.4337 (1.73)     1.9573 (1.89)          5;0   7.4501 (0.58)         10           1
test_fetch_diagnostics[pytest-pyrefly]     183.1395 (2.37)     186.5047 (2.35)     185.1065 (2.37)     1.0400 (1.40)     185.1994 (2.38)     1.2209 (1.18)          4;0   5.4023 (0.42)         10           1
test_fetch_diagnostics[pytest-pyright]     289.3343 (3.74)     291.7467 (3.67)     290.7208 (3.72)     0.7864 (1.06)     290.6446 (3.74)     1.2309 (1.19)          3;0   3.4397 (0.27)         10           1
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
```
