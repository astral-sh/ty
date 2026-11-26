# Benchmarks

All benchmarks were computed on macOS (Apple M3 Max 16, 128 GB) with the following tool versions:

- [Pyrefly](https://pypi.org/project/pyrefly/) 1.4.0
- [Pyright](https://www.npmjs.com/package/pyright) 1.1.414
- [mypy](https://pypi.org/project/mypy/) 2.4.0
- [ty](https://pypi.org/project/ty/) 0.0.111
- [Zuban](https://pypi.org/project/zuban/) 0.10.2

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
  Time (mean ± σ):      54.2 ms ±   2.3 ms    [User: 374.0 ms, System: 27.2 ms]
  Range (min … max):    49.7 ms …  59.7 ms    40 runs
  Memory (peak RSS):  130.1 MiB

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
    2.35 ± 0.10 times faster than Pyrefly
    2.65 ± 0.12 times faster than Zuban
   16.99 ± 0.73 times faster than mypy
   30.68 ± 1.32 times faster than Pyright

-------------------------------------------------------------------------------

discord.py
----------

Benchmark 1: ty
  Time (mean ± σ):     104.9 ms ±   5.2 ms    [User: 998.7 ms, System: 64.8 ms]
  Range (min … max):    97.9 ms … 115.3 ms    23 runs
  Memory (peak RSS):  214.2 MiB

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
    1.65 ± 0.09 times faster than Pyrefly
    3.40 ± 0.17 times faster than Zuban
   19.89 ± 0.99 times faster than mypy
   38.01 ± 1.88 times faster than Pyright

-------------------------------------------------------------------------------

homeassistant
-------------

Benchmark 1: ty
  Time (mean ± σ):      1.754 s ±  0.011 s    [User: 21.957 s, System: 3.515 s]
  Range (min … max):    1.736 s …  1.774 s    10 runs
  Memory (peak RSS):  3,474 MiB

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
    1.31 ± 0.02 times faster than Pyrefly
    4.25 ± 0.04 times faster than Zuban
   29.66 ± 0.32 times faster than mypy
   72.36 ± 4.12 times faster than Pyright

-------------------------------------------------------------------------------

isort
-----

Benchmark 1: ty
  Time (mean ± σ):      55.2 ms ±   1.4 ms    [User: 172.3 ms, System: 15.2 ms]
  Range (min … max):    52.7 ms …  57.8 ms    39 runs
  Memory (peak RSS):   84.9 MiB

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
  ty ran
    1.20 ± 0.04 times faster than Zuban
    1.91 ± 0.06 times faster than Pyrefly
    8.24 ± 0.21 times faster than mypy
   29.53 ± 0.75 times faster than Pyright

-------------------------------------------------------------------------------

jinja
-----

Benchmark 1: ty
  Time (mean ± σ):      44.4 ms ±   1.4 ms    [User: 216.2 ms, System: 16.5 ms]
  Range (min … max):    42.3 ms …  46.8 ms    43 runs
  Memory (peak RSS):   95.2 MiB

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
    1.90 ± 0.07 times faster than Zuban
    2.35 ± 0.08 times faster than Pyrefly
   12.37 ± 0.43 times faster than mypy
   26.54 ± 0.83 times faster than Pyright

-------------------------------------------------------------------------------

pandas
------

Benchmark 1: ty
  Time (mean ± σ):     309.4 ms ±  19.6 ms    [User: 3473.8 ms, System: 192.4 ms]
  Range (min … max):   289.0 ms … 344.2 ms    10 runs
  Memory (peak RSS):  588.7 MiB

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
    2.87 ± 0.20 times faster than Pyrefly
    4.55 ± 0.29 times faster than Zuban
   33.83 ± 2.15 times faster than mypy
   51.03 ± 3.26 times faster than Pyright

-------------------------------------------------------------------------------

pandas-stubs
------------

Benchmark 1: ty
  Time (mean ± σ):      64.2 ms ±   3.3 ms    [User: 311.8 ms, System: 39.8 ms]
  Range (min … max):    56.9 ms …  70.3 ms    34 runs
  Memory (peak RSS):  153.0 MiB

  Warning: Ignoring non-zero exit code.

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
    3.05 ± 0.16 times faster than Pyrefly
    4.22 ± 0.22 times faster than Zuban
   33.80 ± 1.76 times faster than Pyright
   74.19 ± 3.91 times faster than mypy

-------------------------------------------------------------------------------

prefect
-------

Benchmark 1: ty
  Time (mean ± σ):      92.4 ms ±   4.6 ms    [User: 561.8 ms, System: 44.4 ms]
  Range (min … max):    84.3 ms … 104.9 ms    26 runs
  Memory (peak RSS):  223.2 MiB

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
    2.94 ± 0.18 times faster than Pyrefly
   10.26 ± 0.51 times faster than Zuban
   30.55 ± 1.52 times faster than Pyright
   77.80 ± 3.96 times faster than mypy

-------------------------------------------------------------------------------

pytorch
-------

Benchmark 1: ty
  Time (mean ± σ):      1.017 s ±  0.022 s    [User: 12.921 s, System: 0.948 s]
  Range (min … max):    0.988 s …  1.048 s    10 runs
  Memory (peak RSS):  1,586 MiB

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
  ty ran
    1.19 ± 0.03 times faster than Pyrefly
    3.41 ± 0.07 times faster than Zuban
   24.96 ± 0.53 times faster than mypy
   72.79 ± 2.14 times faster than Pyright

-------------------------------------------------------------------------------

httpx
-----

Benchmark 1: ty
  Time (mean ± σ):      52.5 ms ±   1.6 ms    [User: 177.5 ms, System: 17.7 ms]
  Range (min … max):    50.0 ms …  56.1 ms    40 runs
  Memory (peak RSS):   98.7 MiB

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
    1.99 ± 0.07 times faster than Zuban
    2.24 ± 0.08 times faster than Pyrefly
   17.16 ± 0.56 times faster than mypy
   18.08 ± 0.60 times faster than Pyright

-------------------------------------------------------------------------------

numpy
-----

Benchmark 1: ty
  Time (mean ± σ):     165.4 ms ±   8.1 ms    [User: 919.5 ms, System: 67.7 ms]
  Range (min … max):   151.0 ms … 178.3 ms    14 runs
  Memory (peak RSS):  264.6 MiB

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
     3.52 ±  0.25 times faster than Pyrefly
   128.25 ±  6.33 times faster than Pyright
   489.12 ± 24.34 times faster than mypy

-------------------------------------------------------------------------------

fastapi
-------

Benchmark 1: ty
  Time (mean ± σ):      68.1 ms ±   3.6 ms    [User: 307.8 ms, System: 27.6 ms]
  Range (min … max):    62.6 ms …  75.5 ms    30 runs
  Memory (peak RSS):  139.2 MiB

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
    2.81 ± 0.15 times faster than Zuban
    4.37 ± 0.24 times faster than Pyrefly
   28.69 ± 1.53 times faster than mypy
   32.56 ± 1.72 times faster than Pyright

-------------------------------------------------------------------------------

sqlalchemy
----------

Benchmark 1: ty
  Time (mean ± σ):     241.9 ms ±  12.3 ms    [User: 2656.2 ms, System: 133.7 ms]
  Range (min … max):   225.0 ms … 268.0 ms    11 runs
  Memory (peak RSS):  394.5 MiB

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
  ty ran
    1.26 ± 0.07 times faster than Pyrefly
    2.73 ± 0.14 times faster than Zuban
   16.26 ± 0.84 times faster than mypy
   40.51 ± 2.08 times faster than Pyright

-------------------------------------------------------------------------------

rich
----

Benchmark 1: ty
  Time (mean ± σ):      53.6 ms ±   3.0 ms    [User: 326.6 ms, System: 28.1 ms]
  Range (min … max):    49.4 ms …  60.7 ms    37 runs
  Memory (peak RSS):  120.3 MiB

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
    2.29 ± 0.14 times faster than Pyrefly
    2.43 ± 0.14 times faster than Zuban
   22.56 ± 1.28 times faster than mypy
   46.86 ± 2.60 times faster than Pyright

-------------------------------------------------------------------------------

django
------

Benchmark 1: ty
  Time (mean ± σ):     198.1 ms ±   5.8 ms    [User: 1933.8 ms, System: 556.0 ms]
  Range (min … max):   190.5 ms … 206.7 ms    13 runs
  Memory (peak RSS):  308.2 MiB

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
    1.31 ± 0.04 times faster than Pyrefly
    2.58 ± 0.08 times faster than Zuban
   12.35 ± 0.38 times faster than mypy
   34.98 ± 1.06 times faster than Pyright

-------------------------------------------------------------------------------

sympy
-----

Benchmark 1: ty
  Time (mean ± σ):     503.2 ms ±  15.8 ms    [User: 6362.0 ms, System: 490.0 ms]
  Range (min … max):   492.0 ms … 545.5 ms    10 runs
  Memory (peak RSS):  705.5 MiB

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
  ty ran
    1.05 ± 0.03 times faster than Pyrefly
    2.44 ± 0.08 times faster than Zuban
   13.21 ± 0.42 times faster than mypy
   59.71 ± 1.91 times faster than Pyright

-------------------------------------------------------------------------------

openai
------

Benchmark 1: ty
  Time (mean ± σ):     216.5 ms ±  14.5 ms    [User: 1808.9 ms, System: 421.8 ms]
  Range (min … max):   190.1 ms … 233.5 ms    13 runs
  Memory (peak RSS):  322.6 MiB

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
    2.14 ± 0.15 times faster than Pyrefly
    3.98 ± 0.27 times faster than Zuban
   31.27 ± 2.10 times faster than mypy
   37.74 ± 2.55 times faster than Pyright

-------------------------------------------------------------------------------

pytest
------

Benchmark 1: ty
  Time (mean ± σ):     137.0 ms ±  10.8 ms    [User: 1107.1 ms, System: 77.0 ms]
  Range (min … max):   110.3 ms … 152.5 ms    18 runs
  Memory (peak RSS):  246.7 MiB

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
    1.66 ± 0.21 times faster than Pyrefly
    4.31 ± 0.34 times faster than Zuban
   17.38 ± 1.38 times faster than mypy
   33.39 ± 2.63 times faster than Pyright
```

## LSP

### Incremental edit

Zuban's server crashed on the incremental edits in discord.py, NumPy, and PyTorch.

```shell
---------------------------------------------------------------------------------------- benchmark 'black': 4 tests ----------------------------------------------------------------------------------------
Name (time in ms)                             Min                 Max                Mean            StdDev              Median               IQR            Outliers      OPS            Rounds  Iterations
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_incremental_edit[black-ty]           11.7008 (1.0)       12.0411 (1.0)       11.8426 (1.0)      0.1212 (1.0)       11.8383 (1.0)      0.2087 (1.0)           3;0  84.4410 (1.0)          10           1
test_incremental_edit[black-zuban]        18.8832 (1.61)      20.8855 (1.73)      19.3794 (1.64)     0.6267 (5.17)      19.2328 (1.62)     0.5062 (2.43)          2;1  51.6012 (0.61)         10           1
test_incremental_edit[black-pyrefly]      86.7763 (7.42)      97.2985 (8.08)      91.4009 (7.72)     3.0032 (24.78)     91.2891 (7.71)     4.0361 (19.34)         2;0  10.9408 (0.13)         10           1
test_incremental_edit[black-pyright]     540.2310 (46.17)    562.2411 (46.69)    549.4405 (46.40)    6.7233 (55.47)    548.0737 (46.30)    8.5098 (40.77)         4;0   1.8200 (0.02)         10           1
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

----------------------------------------------------------------------------------------- benchmark 'discord.py': 3 tests -----------------------------------------------------------------------------------------
Name (time in ms)                                  Min                 Max                Mean             StdDev              Median                IQR            Outliers      OPS            Rounds  Iterations
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_incremental_edit[discord.py-ty]           17.3911 (1.0)       17.8356 (1.0)       17.5317 (1.0)       0.1440 (1.0)       17.5023 (1.0)       0.0940 (1.0)           2;2  57.0394 (1.0)          10           1
test_incremental_edit[discord.py-pyrefly]      72.6280 (4.18)      82.8766 (4.65)      76.5269 (4.37)      3.7789 (26.24)     74.9435 (4.28)      7.2071 (76.67)         4;0  13.0673 (0.23)         10           1
test_incremental_edit[discord.py-pyright]     488.6511 (28.10)    541.3492 (30.35)    517.2384 (29.50)    16.5382 (114.84)   512.2913 (29.27)    22.0510 (234.59)        3;0   1.9333 (0.03)         10           1
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

---------------------------------------------------------------------------------------- benchmark 'homeassistant': 4 tests ----------------------------------------------------------------------------------------
Name (time in ms)                                     Min                 Max                Mean            StdDev              Median               IQR            Outliers      OPS            Rounds  Iterations
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_incremental_edit[homeassistant-ty]           19.3251 (1.0)       20.8628 (1.0)       19.9883 (1.0)      0.5866 (1.63)      19.7453 (1.0)      0.8398 (2.14)          4;0  50.0293 (1.0)          10           1
test_incremental_edit[homeassistant-pyrefly]      55.8462 (2.89)      85.5288 (4.10)      75.6855 (3.79)     8.0570 (22.42)     76.3312 (3.87)     4.9400 (12.58)         3;1  13.2126 (0.26)         10           1
test_incremental_edit[homeassistant-zuban]        56.2561 (2.91)      57.5430 (2.76)      57.0332 (2.85)     0.3593 (1.0)       57.0851 (2.89)     0.3927 (1.0)           2;0  17.5336 (0.35)         10           1
test_incremental_edit[homeassistant-pyright]     564.8898 (29.23)    580.5012 (27.82)    574.4756 (28.74)    4.9935 (13.90)    573.7045 (29.06)    6.9113 (17.60)         3;0   1.7407 (0.03)         10           1
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

----------------------------------------------------------------------------------------- benchmark 'isort': 4 tests ----------------------------------------------------------------------------------------
Name (time in ms)                             Min                 Max                Mean            StdDev              Median               IQR            Outliers       OPS            Rounds  Iterations
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_incremental_edit[isort-zuban]         5.6747 (1.0)        5.9072 (1.0)        5.7474 (1.0)      0.0701 (1.0)        5.7302 (1.0)      0.0773 (1.0)           2;1  173.9902 (1.0)          10           1
test_incremental_edit[isort-ty]           14.1993 (2.50)      14.6320 (2.48)      14.4289 (2.51)     0.1243 (1.77)      14.4506 (2.52)     0.1311 (1.70)          3;0   69.3052 (0.40)         10           1
test_incremental_edit[isort-pyrefly]      42.7818 (7.54)      57.5799 (9.75)      52.8906 (9.20)     4.5220 (64.55)     54.9351 (9.59)     5.5654 (71.97)         2;0   18.9070 (0.11)         10           1
test_incremental_edit[isort-pyright]     419.7210 (73.96)    429.1457 (72.65)    425.1017 (73.96)    2.9371 (41.93)    424.9466 (74.16)    4.3485 (56.23)         3;0    2.3524 (0.01)         10           1
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

------------------------------------------------------------------------------------------ benchmark 'jinja': 4 tests -----------------------------------------------------------------------------------------
Name (time in ms)                             Min                 Max                Mean             StdDev              Median                IQR            Outliers       OPS            Rounds  Iterations
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_incremental_edit[jinja-ty]            8.1691 (1.0)        9.9423 (1.0)        8.5999 (1.0)       0.5804 (4.33)       8.3540 (1.0)       0.1274 (1.0)           2;2  116.2808 (1.0)          10           1
test_incremental_edit[jinja-zuban]        19.9754 (2.45)      20.4125 (2.05)      20.1366 (2.34)      0.1340 (1.0)       20.1239 (2.41)      0.1803 (1.42)          3;0   49.6609 (0.43)         10           1
test_incremental_edit[jinja-pyrefly]      53.2751 (6.52)      67.2008 (6.76)      60.3027 (7.01)      4.5815 (34.19)     59.1167 (7.08)      5.8406 (45.85)         4;0   16.5830 (0.14)         10           1
test_incremental_edit[jinja-pyright]     476.3300 (58.31)    530.7210 (53.38)    503.8855 (58.59)    14.1706 (105.75)   505.3668 (60.49)    11.4062 (89.55)         2;2    1.9846 (0.02)         10           1
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

---------------------------------------------------------------------------------------- benchmark 'pandas': 4 tests -----------------------------------------------------------------------------------------
Name (time in ms)                              Min                 Max                Mean             StdDev              Median               IQR            Outliers      OPS            Rounds  Iterations
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_incremental_edit[pandas-ty]           33.0467 (1.0)       37.0218 (1.0)       33.8937 (1.0)       1.3004 (1.0)       33.3077 (1.0)      0.5401 (1.0)           2;2  29.5040 (1.0)          10           1
test_incremental_edit[pandas-pyrefly]     243.4753 (7.37)     256.9783 (6.94)     248.6074 (7.33)      4.2473 (3.27)     247.6178 (7.43)     6.6526 (12.32)         2;0   4.0224 (0.14)         10           1
test_incremental_edit[pandas-zuban]       251.8713 (7.62)     259.0576 (7.00)     254.0977 (7.50)      2.2326 (1.72)     253.3567 (7.61)     2.0706 (3.83)          2;1   3.9355 (0.13)         10           1
test_incremental_edit[pandas-pyright]     662.6549 (20.05)    701.7632 (18.96)    691.2085 (20.39)    11.6618 (8.97)     695.5558 (20.88)    8.8209 (16.33)         1;1   1.4467 (0.05)         10           1
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

------------------------------------------------------------------------------------------ benchmark 'prefect': 4 tests -----------------------------------------------------------------------------------------
Name (time in ms)                               Min                 Max                Mean             StdDev              Median                IQR            Outliers       OPS            Rounds  Iterations
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_incremental_edit[prefect-ty]            6.3473 (1.0)        6.7999 (1.0)        6.5576 (1.0)       0.1332 (1.0)        6.5651 (1.0)       0.1475 (1.0)           3;0  152.4941 (1.0)          10           1
test_incremental_edit[prefect-pyrefly]      51.3062 (8.08)      61.9334 (9.11)      56.2614 (8.58)      3.5354 (26.54)     57.8409 (8.81)      5.8660 (39.77)         4;0   17.7742 (0.12)         10           1
test_incremental_edit[prefect-zuban]       131.5461 (20.72)    132.8311 (19.53)    132.0289 (20.13)     0.4032 (3.03)     131.9307 (20.10)     0.4938 (3.35)          3;0    7.5741 (0.05)         10           1
test_incremental_edit[prefect-pyright]     660.4608 (104.05)   695.6145 (102.30)   680.8583 (103.83)   10.4803 (78.69)    682.6589 (103.98)   14.5401 (98.58)         3;0    1.4687 (0.01)         10           1
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

----------------------------------------------------------------------------------------- benchmark 'pytorch': 3 tests ----------------------------------------------------------------------------------------
Name (time in ms)                               Min                 Max                Mean            StdDev              Median               IQR            Outliers       OPS            Rounds  Iterations
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_incremental_edit[pytorch-ty]            3.1977 (1.0)        3.8554 (1.0)        3.3437 (1.0)      0.2066 (1.0)        3.2589 (1.0)      0.2242 (1.0)           1;1  299.0732 (1.0)          10           1
test_incremental_edit[pytorch-pyrefly]      20.1780 (6.31)      25.2127 (6.54)      22.7988 (6.82)     1.8837 (9.12)      23.4518 (7.20)     3.4646 (15.45)         4;0   43.8619 (0.15)         10           1
test_incremental_edit[pytorch-pyright]     411.6034 (128.72)   420.5795 (109.09)   416.2569 (124.49)   2.2362 (10.82)    416.0866 (127.68)   1.0938 (4.88)          2;2    2.4024 (0.01)         10           1
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

------------------------------------------------------------------------------------------ benchmark 'httpx': 4 tests -----------------------------------------------------------------------------------------
Name (time in ms)                             Min                 Max                Mean             StdDev              Median                IQR            Outliers       OPS            Rounds  Iterations
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_incremental_edit[httpx-ty]            5.1564 (1.0)        5.4738 (1.0)        5.2916 (1.0)       0.0859 (1.0)        5.2870 (1.0)       0.0644 (1.0)           2;1  188.9802 (1.0)          10           1
test_incremental_edit[httpx-zuban]         9.5517 (1.85)      11.7660 (2.15)       9.9430 (1.88)      0.6486 (7.55)       9.7386 (1.84)      0.1877 (2.92)          1;1  100.5729 (0.53)         10           1
test_incremental_edit[httpx-pyrefly]      47.6866 (9.25)      57.0288 (10.42)     51.7039 (9.77)      2.8466 (33.12)     52.0920 (9.85)      3.3798 (52.50)         3;0   19.3409 (0.10)         10           1
test_incremental_edit[httpx-pyright]     414.3220 (80.35)    441.5353 (80.66)    426.5495 (80.61)    10.4990 (122.15)   426.0099 (80.58)    20.2930 (315.23)        5;0    2.3444 (0.01)         10           1
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------------- benchmark 'numpy': 3 tests --------------------------------------------------------------------------------------------
Name (time in ms)                               Min                   Max                  Mean             StdDev                Median               IQR            Outliers      OPS            Rounds  Iterations
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_incremental_edit[numpy-ty]             16.7287 (1.0)         21.9342 (1.0)         18.2722 (1.0)       1.5490 (1.0)         17.9568 (1.0)      2.0782 (1.0)           1;0  54.7279 (1.0)          10           1
test_incremental_edit[numpy-pyrefly]       330.8268 (19.78)      350.2634 (15.97)      343.7851 (18.81)     6.4024 (4.13)       346.1157 (19.27)    7.2750 (3.50)          3;0   2.9088 (0.05)         10           1
test_incremental_edit[numpy-pyright]     1,171.7334 (70.04)    1,205.3624 (54.95)    1,188.2385 (65.03)    10.2539 (6.62)     1,189.4224 (66.24)    9.2393 (4.45)          3;0   0.8416 (0.02)         10           1
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

----------------------------------------------------------------------------------------- benchmark 'fastapi': 4 tests ----------------------------------------------------------------------------------------
Name (time in ms)                               Min                 Max                Mean            StdDev              Median               IQR            Outliers       OPS            Rounds  Iterations
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_incremental_edit[fastapi-ty]            5.8450 (1.0)        6.8365 (1.0)        6.0621 (1.0)      0.3194 (2.49)       5.9327 (1.0)      0.1147 (1.0)           2;2  164.9589 (1.0)          10           1
test_incremental_edit[fastapi-zuban]         8.3563 (1.43)       8.7793 (1.28)       8.5171 (1.40)     0.1283 (1.0)        8.4884 (1.43)     0.1784 (1.56)          2;0  117.4108 (0.71)         10           1
test_incremental_edit[fastapi-pyrefly]      58.2667 (9.97)      69.4830 (10.16)     65.8294 (10.86)    3.4123 (26.60)     67.0105 (11.30)    4.0596 (35.39)         2;0   15.1908 (0.09)         10           1
test_incremental_edit[fastapi-pyright]     604.3037 (103.39)   621.4753 (90.90)    614.2073 (101.32)   5.5771 (43.48)    614.2024 (103.53)   8.3417 (72.72)         3;0    1.6281 (0.01)         10           1
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

---------------------------------------------------------------------------------------- benchmark 'sqlalchemy': 4 tests -----------------------------------------------------------------------------------------
Name (time in ms)                                  Min                 Max                Mean            StdDev              Median               IQR            Outliers       OPS            Rounds  Iterations
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_incremental_edit[sqlalchemy-ty]            8.9743 (1.0)       10.6465 (1.0)        9.2287 (1.0)      0.5041 (1.0)        9.0631 (1.0)      0.1438 (1.0)           1;1  108.3576 (1.0)          10           1
test_incremental_edit[sqlalchemy-pyrefly]      56.7484 (6.32)      84.5526 (7.94)      76.4313 (8.28)     7.9762 (15.82)     76.2125 (8.41)     7.9097 (54.99)         2;1   13.0836 (0.12)         10           1
test_incremental_edit[sqlalchemy-zuban]       198.5378 (22.12)    201.8470 (18.96)    199.5849 (21.63)    0.9838 (1.95)     199.1490 (21.97)    1.1792 (8.20)          2;0    5.0104 (0.05)         10           1
test_incremental_edit[sqlalchemy-pyright]     632.0858 (70.43)    647.3986 (60.81)    639.0595 (69.25)    5.6518 (11.21)    640.6409 (70.69)    9.4287 (65.55)         5;0    1.5648 (0.01)         10           1
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

----------------------------------------------------------------------------------------- benchmark 'rich': 4 tests -----------------------------------------------------------------------------------------
Name (time in ms)                            Min                 Max                Mean            StdDev              Median                IQR            Outliers       OPS            Rounds  Iterations
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_incremental_edit[rich-ty]            4.5387 (1.0)        4.7556 (1.0)        4.6566 (1.0)      0.0678 (1.0)        4.6644 (1.0)       0.0890 (1.0)           4;0  214.7505 (1.0)          10           1
test_incremental_edit[rich-zuban]        12.7459 (2.81)      14.8288 (3.12)      13.1219 (2.82)     0.6140 (9.06)      12.9070 (2.77)      0.2442 (2.74)          1;1   76.2082 (0.35)         10           1
test_incremental_edit[rich-pyrefly]      20.0278 (4.41)      41.4377 (8.71)      31.1428 (6.69)     7.2154 (106.44)    34.0170 (7.29)     12.2488 (137.56)        4;0   32.1102 (0.15)         10           1
test_incremental_edit[rich-pyright]     433.5527 (95.52)    446.9955 (93.99)    440.7714 (94.66)    4.4355 (65.43)    442.3849 (94.84)     6.2345 (70.02)         3;0    2.2687 (0.01)         10           1
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

----------------------------------------------------------------------------------------- benchmark 'django': 4 tests ------------------------------------------------------------------------------------------
Name (time in ms)                              Min                 Max                Mean             StdDev              Median                IQR            Outliers       OPS            Rounds  Iterations
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_incremental_edit[django-zuban]         1.7699 (1.0)        1.9427 (1.0)        1.8348 (1.0)       0.0613 (1.0)        1.8271 (1.0)       0.1039 (1.0)           4;0  545.0284 (1.0)          10           1
test_incremental_edit[django-ty]            3.0908 (1.75)       3.5843 (1.85)       3.3114 (1.80)      0.1269 (2.07)       3.3166 (1.82)      0.1283 (1.24)          2;1  301.9905 (0.55)         10           1
test_incremental_edit[django-pyrefly]      21.2110 (11.98)     29.9794 (15.43)     25.4880 (13.89)     3.1539 (51.45)     26.3823 (14.44)     5.5899 (53.81)         4;0   39.2342 (0.07)         10           1
test_incremental_edit[django-pyright]     330.7418 (186.87)   381.0605 (196.15)   354.0818 (192.98)   21.3677 (348.54)   341.3754 (186.84)   39.9063 (384.17)        5;0    2.8242 (0.01)         10           1
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

----------------------------------------------------------------------------------------- benchmark 'sympy': 4 tests -----------------------------------------------------------------------------------------
Name (time in ms)                             Min                 Max                Mean            StdDev              Median                IQR            Outliers       OPS            Rounds  Iterations
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_incremental_edit[sympy-ty]            2.8324 (1.0)        3.2685 (1.0)        3.0064 (1.0)      0.1084 (1.0)        2.9891 (1.0)       0.0503 (1.0)           2;2  332.6223 (1.0)          10           1
test_incremental_edit[sympy-pyrefly]      28.2025 (9.96)      38.2077 (11.69)     33.0703 (11.00)    3.0461 (28.11)     32.1000 (10.74)     4.1055 (81.57)         3;0   30.2386 (0.09)         10           1
test_incremental_edit[sympy-zuban]        62.8081 (22.18)     67.0972 (20.53)     63.7676 (21.21)    1.3140 (12.13)     63.3715 (21.20)     0.7175 (14.25)         1;2   15.6819 (0.05)         10           1
test_incremental_edit[sympy-pyright]     465.8610 (164.48)   487.8697 (149.26)   479.7846 (159.59)   7.3209 (67.56)    478.8293 (160.19)   10.6199 (210.99)        3;0    2.0843 (0.01)         10           1
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

---------------------------------------------------------------------------------------- benchmark 'openai': 4 tests -----------------------------------------------------------------------------------------
Name (time in ms)                              Min                 Max                Mean            StdDev              Median               IQR            Outliers       OPS            Rounds  Iterations
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_incremental_edit[openai-zuban]         3.4460 (1.0)        3.6128 (1.0)        3.5186 (1.0)      0.0547 (1.0)        3.5069 (1.0)      0.0987 (1.12)          4;0  284.2066 (1.0)          10           1
test_incremental_edit[openai-ty]            3.5869 (1.04)       3.8648 (1.07)       3.7531 (1.07)     0.0933 (1.71)       3.7760 (1.08)     0.0880 (1.0)           4;1  266.4461 (0.94)         10           1
test_incremental_edit[openai-pyrefly]      70.9413 (20.59)     87.7718 (24.30)     82.7103 (23.51)    5.0859 (93.06)     83.1189 (23.70)    5.0480 (57.36)         1;1   12.0904 (0.04)         10           1
test_incremental_edit[openai-pyright]     457.0089 (132.62)   489.3018 (135.44)   478.7871 (136.07)   8.6623 (158.50)   481.2125 (137.22)   7.4462 (84.62)         2;1    2.0886 (0.01)         10           1
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

---------------------------------------------------------------------------------------- benchmark 'pytest': 4 tests -----------------------------------------------------------------------------------------
Name (time in ms)                              Min                 Max                Mean            StdDev              Median               IQR            Outliers       OPS            Rounds  Iterations
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_incremental_edit[pytest-ty]            6.6120 (1.0)        6.8202 (1.0)        6.7149 (1.0)      0.0613 (1.0)        6.7173 (1.0)      0.0950 (1.0)           3;0  148.9225 (1.0)          10           1
test_incremental_edit[pytest-zuban]        26.0735 (3.94)      26.7175 (3.92)      26.3351 (3.92)     0.1758 (2.87)      26.3459 (3.92)     0.2007 (2.11)          2;1   37.9721 (0.25)         10           1
test_incremental_edit[pytest-pyrefly]      55.3168 (8.37)      62.2285 (9.12)      58.5314 (8.72)     2.2135 (36.11)     58.4364 (8.70)     2.6986 (28.42)         3;0   17.0848 (0.11)         10           1
test_incremental_edit[pytest-pyright]     458.6860 (69.37)    490.4299 (71.91)    481.3327 (71.68)    8.7184 (142.24)   483.3412 (71.95)    6.7729 (71.32)         2;1    2.0776 (0.01)         10           1
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
```

### Fetch diagnostics

```shell
----------------------------------------------------------------------------------------- benchmark 'black': 4 tests ----------------------------------------------------------------------------------------
Name (time in ms)                              Min                 Max                Mean            StdDev              Median               IQR            Outliers      OPS            Rounds  Iterations
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_fetch_diagnostics[black-ty]           49.4920 (1.0)       50.4230 (1.0)       49.8069 (1.0)      0.2583 (1.0)       49.7654 (1.0)      0.1577 (1.0)           2;1  20.0776 (1.0)          10           1
test_fetch_diagnostics[black-zuban]        68.9572 (1.39)      73.7763 (1.46)      71.2262 (1.43)     1.4690 (5.69)      71.0236 (1.43)     2.1367 (13.55)         2;0  14.0398 (0.70)         10           1
test_fetch_diagnostics[black-pyrefly]     179.8352 (3.63)     181.0037 (3.59)     180.5095 (3.62)     0.4111 (1.59)     180.5079 (3.63)     0.6513 (4.13)          4;0   5.5399 (0.28)         10           1
test_fetch_diagnostics[black-pyright]     299.9607 (6.06)     302.2230 (5.99)     300.9091 (6.04)     0.6684 (2.59)     300.8832 (6.05)     0.6293 (3.99)          3;0   3.3233 (0.17)         10           1
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

----------------------------------------------------------------------------------------- benchmark 'discord.py': 4 tests ------------------------------------------------------------------------------------------
Name (time in ms)                                   Min                 Max                Mean             StdDev              Median                IQR            Outliers      OPS            Rounds  Iterations
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_fetch_diagnostics[discord.py-ty]           74.3813 (1.0)       81.0293 (1.0)       75.6013 (1.0)       2.0413 (8.10)      74.8164 (1.0)       0.9725 (5.01)          1;1  13.2273 (1.0)          10           1
test_fetch_diagnostics[discord.py-zuban]       177.4120 (2.39)     184.2058 (2.27)     180.0302 (2.38)      2.0807 (8.26)     179.8533 (2.40)      1.9461 (10.03)         3;1   5.5546 (0.42)         10           1
test_fetch_diagnostics[discord.py-pyrefly]     187.9900 (2.53)     188.8244 (2.33)     188.3708 (2.49)      0.2520 (1.0)      188.3499 (2.52)      0.1941 (1.0)           4;2   5.3087 (0.40)         10           1
test_fetch_diagnostics[discord.py-pyright]     621.1201 (8.35)     663.5259 (8.19)     630.2578 (8.34)     12.6775 (50.30)    626.5515 (8.37)     11.5769 (59.64)         1;1   1.5867 (0.12)         10           1
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

---------------------------------------------------------------------------------------------- benchmark 'homeassistant': 4 tests ---------------------------------------------------------------------------------------------
Name (time in ms)                                        Min                   Max                  Mean             StdDev                Median                IQR            Outliers      OPS            Rounds  Iterations
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_fetch_diagnostics[homeassistant-ty]             76.2636 (1.0)         77.1052 (1.0)         76.5899 (1.0)       0.2533 (1.0)         76.4984 (1.0)       0.3550 (1.0)           3;0  13.0566 (1.0)          10           1
test_fetch_diagnostics[homeassistant-zuban]         214.2382 (2.81)       219.2897 (2.84)       217.0925 (2.83)      1.7237 (6.81)       217.0206 (2.84)      2.0827 (5.87)          4;0   4.6063 (0.35)         10           1
test_fetch_diagnostics[homeassistant-pyrefly]       236.2060 (3.10)       239.4906 (3.11)       237.6687 (3.10)      1.0456 (4.13)       237.4407 (3.10)      1.0302 (2.90)          3;0   4.2075 (0.32)         10           1
test_fetch_diagnostics[homeassistant-pyright]     1,890.3885 (24.79)    1,924.0052 (24.95)    1,905.1369 (24.87)    10.7615 (42.49)    1,903.1950 (24.88)    14.3797 (40.50)         4;0   0.5249 (0.04)         10           1
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

----------------------------------------------------------------------------------------- benchmark 'isort': 4 tests -----------------------------------------------------------------------------------------
Name (time in ms)                              Min                 Max                Mean            StdDev              Median                IQR            Outliers      OPS            Rounds  Iterations
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_fetch_diagnostics[isort-ty]           38.4037 (1.0)       41.3622 (1.0)       38.9828 (1.0)      0.8802 (1.0)       38.6996 (1.0)       0.2372 (1.0)           1;2  25.6524 (1.0)          10           1
test_fetch_diagnostics[isort-zuban]        39.6183 (1.03)      44.7363 (1.08)      41.2833 (1.06)     1.4294 (1.62)      40.9556 (1.06)      1.3667 (5.76)          2;1  24.2229 (0.94)         10           1
test_fetch_diagnostics[isort-pyrefly]     126.7168 (3.30)     140.7936 (3.40)     134.1324 (3.44)     5.9800 (6.79)     134.6929 (3.48)     11.4701 (48.35)         4;0   7.4553 (0.29)         10           1
test_fetch_diagnostics[isort-pyright]     355.6153 (9.26)     360.0408 (8.70)     358.0638 (9.19)     1.4327 (1.63)     358.1251 (9.25)      2.5620 (10.80)         4;0   2.7928 (0.11)         10           1
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

----------------------------------------------------------------------------------------- benchmark 'jinja': 4 tests ----------------------------------------------------------------------------------------
Name (time in ms)                              Min                 Max                Mean            StdDev              Median               IQR            Outliers      OPS            Rounds  Iterations
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_fetch_diagnostics[jinja-ty]           40.7119 (1.0)       48.6519 (1.0)       43.4449 (1.0)      2.7165 (7.26)      43.3241 (1.0)      4.7827 (7.21)          2;0  23.0177 (1.0)          10           1
test_fetch_diagnostics[jinja-zuban]        85.7727 (2.11)      88.3310 (1.82)      86.9519 (2.00)     0.7278 (1.95)      87.0239 (2.01)     0.7648 (1.15)          2;0  11.5006 (0.50)         10           1
test_fetch_diagnostics[jinja-pyrefly]     125.6743 (3.09)     126.7780 (2.61)     126.3703 (2.91)     0.3741 (1.0)      126.4106 (2.92)     0.6636 (1.0)           4;0   7.9133 (0.34)         10           1
test_fetch_diagnostics[jinja-pyright]     353.2582 (8.68)     361.2105 (7.42)     356.3589 (8.20)     2.3240 (6.21)     355.8286 (8.21)     3.4593 (5.21)          2;0   2.8062 (0.12)         10           1
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

---------------------------------------------------------------------------------------- benchmark 'pandas': 4 tests ----------------------------------------------------------------------------------------
Name (time in ms)                               Min                 Max                Mean            StdDev              Median               IQR            Outliers     OPS            Rounds  Iterations
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_fetch_diagnostics[pandas-ty]          276.5726 (1.0)      280.3591 (1.0)      277.6055 (1.0)      1.0802 (1.0)      277.2327 (1.0)      0.6577 (1.0)           1;1  3.6022 (1.0)          10           1
test_fetch_diagnostics[pandas-pyrefly]     539.1561 (1.95)     562.5021 (2.01)     543.9112 (1.96)     6.9893 (6.47)     541.4131 (1.95)     2.4565 (3.74)          1;2  1.8385 (0.51)         10           1
test_fetch_diagnostics[pandas-pyright]     629.9906 (2.28)     647.6225 (2.31)     639.1170 (2.30)     5.6742 (5.25)     640.4880 (2.31)     9.5839 (14.57)         4;0  1.5647 (0.43)         10           1
test_fetch_diagnostics[pandas-zuban]       666.4379 (2.41)     680.6972 (2.43)     673.7827 (2.43)     4.4995 (4.17)     673.4846 (2.43)     6.0168 (9.15)          3;0  1.4842 (0.41)         10           1
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------------- benchmark 'prefect': 4 tests ---------------------------------------------------------------------------------------------
Name (time in ms)                                  Min                   Max                  Mean             StdDev                Median                IQR            Outliers     OPS            Rounds  Iterations
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_fetch_diagnostics[prefect-ty]            131.3135 (1.0)        133.0055 (1.0)        131.9597 (1.0)       0.4547 (1.0)        131.8158 (1.0)       0.4297 (1.0)           2;1  7.5781 (1.0)          10           1
test_fetch_diagnostics[prefect-pyrefly]       332.9010 (2.54)       467.9147 (3.52)       452.5213 (3.43)     42.0522 (92.49)      465.0061 (3.53)      2.8783 (6.70)          1;1  2.2098 (0.29)         10           1
test_fetch_diagnostics[prefect-zuban]         859.7134 (6.55)       865.6050 (6.51)       863.4421 (6.54)      2.2602 (4.97)       864.5682 (6.56)      3.9808 (9.26)          3;0  1.1582 (0.15)         10           1
test_fetch_diagnostics[prefect-pyright]     1,102.1569 (8.39)     1,130.7971 (8.50)     1,113.3106 (8.44)     10.0063 (22.01)    1,112.3842 (8.44)     16.5983 (38.62)         5;0  0.8982 (0.12)         10           1
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

---------------------------------------------------------------------------------------------- benchmark 'pytorch': 4 tests ---------------------------------------------------------------------------------------------
Name (time in ms)                                  Min                   Max                  Mean             StdDev                Median                IQR            Outliers      OPS            Rounds  Iterations
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_fetch_diagnostics[pytorch-ty]             53.8913 (1.0)         54.3844 (1.0)         54.0913 (1.0)       0.1660 (1.0)         54.0435 (1.0)       0.1451 (1.0)           3;2  18.4872 (1.0)          10           1
test_fetch_diagnostics[pytorch-pyrefly]       116.7863 (2.17)       145.4521 (2.67)       128.6864 (2.38)     14.0053 (84.36)      118.9156 (2.20)     27.4318 (189.08)        4;0   7.7708 (0.42)         10           1
test_fetch_diagnostics[pytorch-pyright]       702.6213 (13.04)      709.5476 (13.05)      705.4807 (13.04)     2.5295 (15.24)      704.5238 (13.04)     4.3440 (29.94)         3;0   1.4175 (0.08)         10           1
test_fetch_diagnostics[pytorch-zuban]       1,825.0715 (33.87)    1,860.6000 (34.21)    1,835.6793 (33.94)     9.9072 (59.67)    1,835.3201 (33.96)     8.8780 (61.19)         2;1   0.5448 (0.03)         10           1
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

----------------------------------------------------------------------------------------- benchmark 'httpx': 4 tests ----------------------------------------------------------------------------------------
Name (time in ms)                              Min                 Max                Mean            StdDev              Median               IQR            Outliers      OPS            Rounds  Iterations
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_fetch_diagnostics[httpx-ty]           36.1249 (1.0)       39.4876 (1.0)       36.6000 (1.0)      1.0205 (1.49)      36.2839 (1.0)      0.1715 (1.0)           1;1  27.3224 (1.0)          10           1
test_fetch_diagnostics[httpx-zuban]        69.2425 (1.92)      71.2874 (1.81)      70.2522 (1.92)     0.6870 (1.0)       70.2971 (1.94)     0.9758 (5.69)          3;0  14.2344 (0.52)         10           1
test_fetch_diagnostics[httpx-pyrefly]     114.3010 (3.16)     118.0325 (2.99)     115.3196 (3.15)     1.1948 (1.74)     114.8530 (3.17)     1.1663 (6.80)          2;1   8.6716 (0.32)         10           1
test_fetch_diagnostics[httpx-pyright]     224.9341 (6.23)     228.4704 (5.79)     226.4147 (6.19)     1.0548 (1.54)     226.3045 (6.24)     1.0174 (5.93)          3;1   4.4167 (0.16)         10           1
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

------------------------------------------------------------------------------------------------ benchmark 'numpy': 4 tests -----------------------------------------------------------------------------------------------
Name (time in ms)                                 Min                    Max                   Mean             StdDev                 Median                 IQR            Outliers     OPS            Rounds  Iterations
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_fetch_diagnostics[numpy-ty]             147.3199 (1.0)         151.9226 (1.0)         148.7672 (1.0)       1.3765 (1.0)         148.5472 (1.0)        1.3406 (1.44)          3;1  6.7219 (1.0)          10           1
test_fetch_diagnostics[numpy-pyrefly]        562.9346 (3.82)        568.0607 (3.74)        564.3641 (3.79)      1.4365 (1.04)        564.1055 (3.80)       0.9281 (1.0)           1;1  1.7719 (0.26)         10           1
test_fetch_diagnostics[numpy-pyright]      1,182.4547 (8.03)      1,212.2849 (7.98)      1,199.6223 (8.06)      9.0291 (6.56)      1,198.6239 (8.07)      12.4973 (13.47)         3;0  0.8336 (0.12)         10           1
test_fetch_diagnostics[numpy-zuban]       36,078.9349 (244.90)   36,423.6785 (239.75)   36,193.5729 (243.29)   98.8916 (71.84)    36,198.7695 (243.69)   119.7505 (129.02)        2;1  0.0276 (0.00)         10           1
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

----------------------------------------------------------------------------------------- benchmark 'fastapi': 4 tests ----------------------------------------------------------------------------------------
Name (time in ms)                                Min                 Max                Mean            StdDev              Median               IQR            Outliers      OPS            Rounds  Iterations
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_fetch_diagnostics[fastapi-ty]           78.4674 (1.0)       79.0430 (1.0)       78.7343 (1.0)      0.2186 (1.0)       78.6909 (1.0)      0.3844 (1.0)           3;0  12.7010 (1.0)          10           1
test_fetch_diagnostics[fastapi-zuban]       171.4969 (2.19)     177.0828 (2.24)     173.4509 (2.20)     1.8097 (8.28)     173.0481 (2.20)     2.5310 (6.58)          3;0   5.7653 (0.45)         10           1
test_fetch_diagnostics[fastapi-pyrefly]     199.6927 (2.54)     201.7180 (2.55)     200.3882 (2.55)     0.5838 (2.67)     200.3402 (2.55)     0.6110 (1.59)          2;1   4.9903 (0.39)         10           1
test_fetch_diagnostics[fastapi-pyright]     457.2369 (5.83)     470.3823 (5.95)     465.9305 (5.92)     3.9981 (18.29)    466.0065 (5.92)     4.5289 (11.78)         3;1   2.1462 (0.17)         10           1
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

---------------------------------------------------------------------------------------- benchmark 'sqlalchemy': 4 tests ----------------------------------------------------------------------------------------
Name (time in ms)                                   Min                 Max                Mean            StdDev              Median               IQR            Outliers     OPS            Rounds  Iterations
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_fetch_diagnostics[sqlalchemy-ty]          168.7246 (1.0)      179.8790 (1.0)      170.6716 (1.0)      3.4183 (2.14)     169.0453 (1.0)      2.1220 (1.35)          1;1  5.8592 (1.0)          10           1
test_fetch_diagnostics[sqlalchemy-pyrefly]     250.0255 (1.48)     256.0001 (1.42)     251.9413 (1.48)     1.6665 (1.04)     251.7372 (1.49)     1.6916 (1.08)          2;1  3.9692 (0.68)         10           1
test_fetch_diagnostics[sqlalchemy-pyright]     270.1789 (1.60)     276.0185 (1.53)     272.7359 (1.60)     1.6008 (1.0)      272.7561 (1.61)     1.5684 (1.0)           2;1  3.6666 (0.63)         10           1
test_fetch_diagnostics[sqlalchemy-zuban]       383.2057 (2.27)     399.6241 (2.22)     386.9370 (2.27)     4.6166 (2.88)     385.5155 (2.28)     2.3762 (1.52)          1;1  2.5844 (0.44)         10           1
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

---------------------------------------------------------------------------------------- benchmark 'rich': 4 tests -----------------------------------------------------------------------------------------
Name (time in ms)                             Min                 Max                Mean            StdDev              Median               IQR            Outliers      OPS            Rounds  Iterations
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_fetch_diagnostics[rich-ty]           33.3572 (1.0)       34.1940 (1.0)       33.5839 (1.0)      0.2380 (1.0)       33.5366 (1.0)      0.1747 (1.0)           1;1  29.7762 (1.0)          10           1
test_fetch_diagnostics[rich-zuban]        79.5685 (2.39)      82.3503 (2.41)      80.7725 (2.41)     0.8009 (3.37)      80.6681 (2.41)     0.5338 (3.06)          3;2  12.3804 (0.42)         10           1
test_fetch_diagnostics[rich-pyrefly]      99.5237 (2.98)     115.1077 (3.37)     110.9954 (3.31)     5.6315 (23.66)    113.2185 (3.38)     1.7742 (10.16)         2;2   9.0094 (0.30)         10           1
test_fetch_diagnostics[rich-pyright]     309.8927 (9.29)     314.1458 (9.19)     311.3170 (9.27)     1.3331 (5.60)     310.9984 (9.27)     1.9001 (10.88)         3;0   3.2122 (0.11)         10           1
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

---------------------------------------------------------------------------------------- benchmark 'django': 4 tests -----------------------------------------------------------------------------------------
Name (time in ms)                               Min                 Max                Mean            StdDev              Median               IQR            Outliers      OPS            Rounds  Iterations
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_fetch_diagnostics[django-ty]           19.9797 (1.0)       20.3007 (1.0)       20.1106 (1.0)      0.1120 (1.0)       20.0809 (1.0)      0.1710 (1.0)           4;0  49.7251 (1.0)          10           1
test_fetch_diagnostics[django-zuban]        45.0162 (2.25)      47.3812 (2.33)      46.3298 (2.30)     0.7499 (6.69)      46.4050 (2.31)     0.7135 (4.17)          4;1  21.5844 (0.43)         10           1
test_fetch_diagnostics[django-pyrefly]      90.8160 (4.55)      96.1161 (4.73)      94.1640 (4.68)     2.2035 (19.67)     95.3465 (4.75)     4.3802 (25.62)         3;0  10.6198 (0.21)         10           1
test_fetch_diagnostics[django-pyright]     587.8771 (29.42)    610.7550 (30.09)    593.6576 (29.52)    8.6595 (77.29)    589.8123 (29.37)    2.7981 (16.37)         2;2   1.6845 (0.03)         10           1
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

----------------------------------------------------------------------------------------- benchmark 'sympy': 4 tests ----------------------------------------------------------------------------------------
Name (time in ms)                              Min                 Max                Mean            StdDev              Median               IQR            Outliers      OPS            Rounds  Iterations
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_fetch_diagnostics[sympy-ty]           57.8503 (1.0)       58.8916 (1.0)       58.2277 (1.0)      0.3413 (1.0)       58.0762 (1.0)      0.4730 (1.0)           3;0  17.1740 (1.0)          10           1
test_fetch_diagnostics[sympy-pyrefly]     179.4386 (3.10)     183.1834 (3.11)     180.5083 (3.10)     1.0781 (3.16)     180.2387 (3.10)     0.5938 (1.26)          1;1   5.5399 (0.32)         10           1
test_fetch_diagnostics[sympy-zuban]       260.1722 (4.50)     274.6859 (4.66)     265.9684 (4.57)     4.4955 (13.17)    264.4641 (4.55)     7.1645 (15.15)         2;0   3.7598 (0.22)         10           1
test_fetch_diagnostics[sympy-pyright]     392.3544 (6.78)     400.7913 (6.81)     396.7093 (6.81)     2.7972 (8.20)     396.7134 (6.83)     5.3469 (11.30)         4;0   2.5207 (0.15)         10           1
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

---------------------------------------------------------------------------------------- benchmark 'openai': 4 tests -----------------------------------------------------------------------------------------
Name (time in ms)                               Min                 Max                Mean            StdDev              Median               IQR            Outliers      OPS            Rounds  Iterations
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_fetch_diagnostics[openai-ty]           54.5550 (1.0)       55.7155 (1.0)       54.8135 (1.0)      0.3378 (1.0)       54.7322 (1.0)      0.1835 (1.0)           1;1  18.2437 (1.0)          10           1
test_fetch_diagnostics[openai-zuban]       139.0193 (2.55)     143.9898 (2.58)     141.1401 (2.57)     1.4470 (4.28)     140.7476 (2.57)     1.9043 (10.38)         2;0   7.0852 (0.39)         10           1
test_fetch_diagnostics[openai-pyrefly]     188.4392 (3.45)     202.4323 (3.63)     199.4188 (3.64)     5.1057 (15.12)    201.7685 (3.69)     1.2412 (6.76)          2;2   5.0146 (0.27)         10           1
test_fetch_diagnostics[openai-pyright]     513.3347 (9.41)     518.7722 (9.31)     515.7981 (9.41)     2.2311 (6.61)     515.5012 (9.42)     4.6511 (25.35)         5;0   1.9387 (0.11)         10           1
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

---------------------------------------------------------------------------------------- benchmark 'pytest': 4 tests -----------------------------------------------------------------------------------------
Name (time in ms)                               Min                 Max                Mean            StdDev              Median               IQR            Outliers      OPS            Rounds  Iterations
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_fetch_diagnostics[pytest-ty]           61.8758 (1.0)       62.9621 (1.0)       62.3104 (1.0)      0.3293 (1.0)       62.2094 (1.0)      0.4553 (1.0)           3;0  16.0487 (1.0)          10           1
test_fetch_diagnostics[pytest-zuban]       132.7784 (2.15)     135.7364 (2.16)     134.2270 (2.15)     1.0887 (3.31)     134.4337 (2.16)     1.9573 (4.30)          5;0   7.4501 (0.46)         10           1
test_fetch_diagnostics[pytest-pyrefly]     183.1395 (2.96)     186.5047 (2.96)     185.1065 (2.97)     1.0400 (3.16)     185.1994 (2.98)     1.2209 (2.68)          4;0   5.4023 (0.34)         10           1
test_fetch_diagnostics[pytest-pyright]     289.3343 (4.68)     291.7467 (4.63)     290.7208 (4.67)     0.7864 (2.39)     290.6446 (4.67)     1.2309 (2.70)          3;0   3.4397 (0.21)         10           1
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
```
