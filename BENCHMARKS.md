# Benchmarks

All benchmarks were computed on macOS (Apple M3 Max 16, 128 GB) with the following tool versions:

- [Pyrefly](https://pypi.org/project/pyrefly/) 1.4.0
- [Pyright](https://www.npmjs.com/package/pyright) 1.1.414
- [mypy](https://pypi.org/project/mypy/) 2.4.0
- [ty](https://pypi.org/project/ty/) 0.0.96
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
  Time (mean ± σ):      66.9 ms ±   2.6 ms    [User: 477.5 ms, System: 27.4 ms]
  Range (min … max):    62.8 ms …  73.7 ms    35 runs
  Memory (peak RSS):  136.2 MiB

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
    1.90 ± 0.08 times faster than Pyrefly
    2.15 ± 0.09 times faster than Zuban
   13.76 ± 0.55 times faster than mypy
   24.85 ± 0.99 times faster than Pyright

-------------------------------------------------------------------------------

discord.py
----------

Benchmark 1: ty
  Time (mean ± σ):     137.7 ms ±   5.2 ms    [User: 1330.3 ms, System: 67.5 ms]
  Range (min … max):   131.8 ms … 153.8 ms    18 runs
  Memory (peak RSS):  222.9 MiB

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
    1.26 ± 0.06 times faster than Pyrefly
    2.59 ± 0.10 times faster than Zuban
   15.15 ± 0.57 times faster than mypy
   28.96 ± 1.09 times faster than Pyright

-------------------------------------------------------------------------------

homeassistant
-------------

Benchmark 1: ty
  Time (mean ± σ):      2.092 s ±  0.019 s    [User: 26.879 s, System: 3.587 s]
  Range (min … max):    2.077 s …  2.136 s    10 runs
  Memory (peak RSS):  3,497 MiB

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
    1.10 ± 0.02 times faster than Pyrefly
    3.56 ± 0.04 times faster than Zuban
   24.87 ± 0.32 times faster than mypy
   60.69 ± 3.48 times faster than Pyright

-------------------------------------------------------------------------------

isort
-----

Benchmark 1: ty
  Time (mean ± σ):      92.2 ms ±   1.7 ms    [User: 241.2 ms, System: 16.1 ms]
  Range (min … max):    89.4 ms …  95.9 ms    26 runs
  Memory (peak RSS):   90.5 MiB

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
    1.40 ± 0.04 times faster than ty
    1.60 ± 0.05 times faster than Pyrefly
    6.89 ± 0.15 times faster than mypy
   24.69 ± 0.54 times faster than Pyright

-------------------------------------------------------------------------------

jinja
-----

Benchmark 1: ty
  Time (mean ± σ):      55.2 ms ±   1.2 ms    [User: 264.8 ms, System: 16.3 ms]
  Range (min … max):    52.1 ms …  57.3 ms    38 runs
  Memory (peak RSS):   99.7 MiB

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
    1.53 ± 0.04 times faster than Zuban
    1.89 ± 0.05 times faster than Pyrefly
    9.95 ± 0.27 times faster than mypy
   21.34 ± 0.48 times faster than Pyright

-------------------------------------------------------------------------------

pandas
------

Benchmark 1: ty
  Time (mean ± σ):     404.8 ms ±  27.7 ms    [User: 4477.7 ms, System: 203.0 ms]
  Range (min … max):   359.3 ms … 450.3 ms    10 runs
  Memory (peak RSS):  590.3 MiB

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
    2.19 ± 0.17 times faster than Pyrefly
    3.48 ± 0.24 times faster than Zuban
   25.86 ± 1.77 times faster than mypy
   39.00 ± 2.68 times faster than Pyright

-------------------------------------------------------------------------------

pandas-stubs
------------

Benchmark 1: ty
  Time (mean ± σ):      84.4 ms ±   3.5 ms    [User: 422.7 ms, System: 41.7 ms]
  Range (min … max):    77.5 ms …  91.0 ms    26 runs
  Memory (peak RSS):  158.0 MiB

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
    2.32 ± 0.10 times faster than Pyrefly
    3.21 ± 0.13 times faster than Zuban
   25.69 ± 1.07 times faster than Pyright
   56.40 ± 2.39 times faster than mypy

-------------------------------------------------------------------------------

prefect
-------

Benchmark 1: ty
  Time (mean ± σ):     111.0 ms ±   6.2 ms    [User: 668.0 ms, System: 42.5 ms]
  Range (min … max):    98.1 ms … 121.8 ms    21 runs
  Memory (peak RSS):  224.2 MiB

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
    2.44 ± 0.16 times faster than Pyrefly
    8.54 ± 0.48 times faster than Zuban
   25.43 ± 1.43 times faster than Pyright
   64.76 ± 3.71 times faster than mypy

-------------------------------------------------------------------------------

pytorch
-------

Benchmark 1: ty
  Time (mean ± σ):      1.313 s ±  0.059 s    [User: 16.575 s, System: 1.073 s]
  Range (min … max):    1.263 s …  1.463 s    10 runs
  Memory (peak RSS):  1,646 MiB

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
    1.09 ± 0.05 times faster than ty
    2.87 ± 0.04 times faster than Zuban
   21.05 ± 0.26 times faster than mypy
   61.41 ± 1.46 times faster than Pyright

-------------------------------------------------------------------------------

httpx
-----

Benchmark 1: ty
  Time (mean ± σ):      66.4 ms ±   1.8 ms    [User: 225.2 ms, System: 17.7 ms]
  Range (min … max):    63.8 ms …  69.8 ms    32 runs
  Memory (peak RSS):  105.2 MiB

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
    1.58 ± 0.05 times faster than Zuban
    1.78 ± 0.06 times faster than Pyrefly
   13.58 ± 0.40 times faster than mypy
   14.31 ± 0.43 times faster than Pyright

-------------------------------------------------------------------------------

numpy
-----

Benchmark 1: ty
  Time (mean ± σ):     391.9 ms ±  15.3 ms    [User: 1503.6 ms, System: 68.9 ms]
  Range (min … max):   377.8 ms … 430.8 ms    10 runs
  Memory (peak RSS):  284.9 MiB

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
     1.48 ± 0.09 times faster than Pyrefly
    54.15 ± 2.13 times faster than Pyright
   206.51 ± 8.24 times faster than mypy

-------------------------------------------------------------------------------

fastapi
-------

Benchmark 1: ty
  Time (mean ± σ):      89.0 ms ±   2.4 ms    [User: 400.0 ms, System: 27.0 ms]
  Range (min … max):    85.1 ms …  94.7 ms    26 runs
  Memory (peak RSS):  142.8 MiB

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
    2.15 ± 0.06 times faster than Zuban
    3.34 ± 0.10 times faster than Pyrefly
   21.93 ± 0.62 times faster than mypy
   24.89 ± 0.68 times faster than Pyright

-------------------------------------------------------------------------------

sqlalchemy
----------

Benchmark 1: ty
  Time (mean ± σ):     289.8 ms ±  10.5 ms    [User: 3277.5 ms, System: 142.8 ms]
  Range (min … max):   272.9 ms … 303.3 ms    10 runs
  Memory (peak RSS):  404.2 MiB

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
    1.05 ± 0.05 times faster than Pyrefly
    2.28 ± 0.08 times faster than Zuban
   13.57 ± 0.50 times faster than mypy
   33.81 ± 1.25 times faster than Pyright

-------------------------------------------------------------------------------

rich
----

Benchmark 1: ty
  Time (mean ± σ):      63.0 ms ±   3.0 ms    [User: 401.2 ms, System: 28.9 ms]
  Range (min … max):    56.2 ms …  70.0 ms    34 runs
  Memory (peak RSS):  121.6 MiB

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
    2.07 ± 0.10 times faster than Zuban
   19.20 ± 0.94 times faster than mypy
   39.88 ± 1.89 times faster than Pyright

-------------------------------------------------------------------------------

django
------

Benchmark 1: ty
  Time (mean ± σ):     253.0 ms ±  26.2 ms    [User: 2494.0 ms, System: 632.4 ms]
  Range (min … max):   222.8 ms … 329.4 ms    12 runs
  Memory (peak RSS):  345.0 MiB

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
    1.03 ± 0.11 times faster than Pyrefly
    2.02 ± 0.21 times faster than Zuban
    9.67 ± 1.01 times faster than mypy
   27.40 ± 2.85 times faster than Pyright

-------------------------------------------------------------------------------

sympy
-----

Benchmark 1: ty
  Time (mean ± σ):     720.7 ms ±  14.5 ms    [User: 8946.1 ms, System: 557.6 ms]
  Range (min … max):   703.3 ms … 751.7 ms    10 runs
  Memory (peak RSS):  728.0 MiB

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
    1.37 ± 0.03 times faster than ty
    2.33 ± 0.03 times faster than Zuban
   12.61 ± 0.15 times faster than mypy
   57.02 ± 0.72 times faster than Pyright

-------------------------------------------------------------------------------

openai
------

Benchmark 1: ty
  Time (mean ± σ):     294.1 ms ±  12.6 ms    [User: 2452.3 ms, System: 432.2 ms]
  Range (min … max):   279.6 ms … 315.6 ms    10 runs
  Memory (peak RSS):  349.3 MiB

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
    1.58 ± 0.08 times faster than Pyrefly
    2.93 ± 0.13 times faster than Zuban
   23.02 ± 1.00 times faster than mypy
   27.78 ± 1.21 times faster than Pyright

-------------------------------------------------------------------------------

pytest
------

Benchmark 1: ty
  Time (mean ± σ):     164.8 ms ±  12.3 ms    [User: 1374.5 ms, System: 77.8 ms]
  Range (min … max):   148.0 ms … 186.9 ms    16 runs
  Memory (peak RSS):  248.0 MiB

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
    1.38 ± 0.17 times faster than Pyrefly
    3.59 ± 0.27 times faster than Zuban
   14.45 ± 1.09 times faster than mypy
   27.76 ± 2.09 times faster than Pyright
```

## LSP

### Incremental edit

Zuban's server crashed on the incremental edits in discord.py, NumPy, and PyTorch.

```shell
---------------------------------------------------------------------------------------- benchmark 'black': 4 tests ----------------------------------------------------------------------------------------
Name (time in ms)                             Min                 Max                Mean            StdDev              Median               IQR            Outliers      OPS            Rounds  Iterations
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_incremental_edit[black-ty]           15.7060 (1.0)       18.0898 (1.0)       16.1870 (1.0)      0.6904 (1.10)      16.0486 (1.0)      0.2907 (1.0)           1;1  61.7781 (1.0)          10           1
test_incremental_edit[black-zuban]        18.8832 (1.20)      20.8855 (1.15)      19.3794 (1.20)     0.6267 (1.0)       19.2328 (1.20)     0.5062 (1.74)          2;1  51.6012 (0.84)         10           1
test_incremental_edit[black-pyrefly]      86.7763 (5.53)      97.2985 (5.38)      91.4009 (5.65)     3.0032 (4.79)      91.2891 (5.69)     4.0361 (13.88)         2;0  10.9408 (0.18)         10           1
test_incremental_edit[black-pyright]     540.2310 (34.40)    562.2411 (31.08)    549.4405 (33.94)    6.7233 (10.73)    548.0737 (34.15)    8.5098 (29.27)         4;0   1.8200 (0.03)         10           1
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

----------------------------------------------------------------------------------------- benchmark 'discord.py': 3 tests -----------------------------------------------------------------------------------------
Name (time in ms)                                  Min                 Max                Mean             StdDev              Median                IQR            Outliers      OPS            Rounds  Iterations
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_incremental_edit[discord.py-ty]           25.3576 (1.0)       27.1014 (1.0)       25.7487 (1.0)       0.5227 (1.0)       25.5438 (1.0)       0.1858 (1.0)           1;2  38.8368 (1.0)          10           1
test_incremental_edit[discord.py-pyrefly]      72.6280 (2.86)      82.8766 (3.06)      76.5269 (2.97)      3.7789 (7.23)      74.9435 (2.93)      7.2071 (38.79)         4;0  13.0673 (0.34)         10           1
test_incremental_edit[discord.py-pyright]     488.6511 (19.27)    541.3492 (19.97)    517.2384 (20.09)    16.5382 (31.64)    512.2913 (20.06)    22.0510 (118.69)        3;0   1.9333 (0.05)         10           1
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

---------------------------------------------------------------------------------------- benchmark 'homeassistant': 4 tests ----------------------------------------------------------------------------------------
Name (time in ms)                                     Min                 Max                Mean            StdDev              Median               IQR            Outliers      OPS            Rounds  Iterations
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_incremental_edit[homeassistant-ty]           29.5244 (1.0)       30.3422 (1.0)       29.9610 (1.0)      0.2607 (1.0)       29.9622 (1.0)      0.3388 (1.0)           4;0  33.3768 (1.0)          10           1
test_incremental_edit[homeassistant-pyrefly]      55.8462 (1.89)      85.5288 (2.82)      75.6855 (2.53)     8.0570 (30.90)     76.3312 (2.55)     4.9400 (14.58)         3;1  13.2126 (0.40)         10           1
test_incremental_edit[homeassistant-zuban]        56.2561 (1.91)      57.5430 (1.90)      57.0332 (1.90)     0.3593 (1.38)      57.0851 (1.91)     0.3927 (1.16)          2;0  17.5336 (0.53)         10           1
test_incremental_edit[homeassistant-pyright]     564.8898 (19.13)    580.5012 (19.13)    574.4756 (19.17)    4.9935 (19.15)    573.7045 (19.15)    6.9113 (20.40)         3;0   1.7407 (0.05)         10           1
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

----------------------------------------------------------------------------------------- benchmark 'isort': 4 tests ----------------------------------------------------------------------------------------
Name (time in ms)                             Min                 Max                Mean            StdDev              Median               IQR            Outliers       OPS            Rounds  Iterations
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_incremental_edit[isort-zuban]         5.6747 (1.0)        5.9072 (1.0)        5.7474 (1.0)      0.0701 (1.0)        5.7302 (1.0)      0.0773 (1.0)           2;1  173.9902 (1.0)          10           1
test_incremental_edit[isort-ty]           21.2035 (3.74)      21.7138 (3.68)      21.4363 (3.73)     0.1578 (2.25)      21.4441 (3.74)     0.1972 (2.55)          3;0   46.6498 (0.27)         10           1
test_incremental_edit[isort-pyrefly]      42.7818 (7.54)      57.5799 (9.75)      52.8906 (9.20)     4.5220 (64.55)     54.9351 (9.59)     5.5654 (71.97)         2;0   18.9070 (0.11)         10           1
test_incremental_edit[isort-pyright]     419.7210 (73.96)    429.1457 (72.65)    425.1017 (73.96)    2.9371 (41.93)    424.9466 (74.16)    4.3485 (56.23)         3;0    2.3524 (0.01)         10           1
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

----------------------------------------------------------------------------------------- benchmark 'jinja': 4 tests -----------------------------------------------------------------------------------------
Name (time in ms)                             Min                 Max                Mean             StdDev              Median                IQR            Outliers      OPS            Rounds  Iterations
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_incremental_edit[jinja-ty]           11.8007 (1.0)       13.6445 (1.0)       12.2505 (1.0)       0.6098 (4.55)      11.9759 (1.0)       0.7002 (3.88)          2;1  81.6290 (1.0)          10           1
test_incremental_edit[jinja-zuban]        19.9754 (1.69)      20.4125 (1.50)      20.1366 (1.64)      0.1340 (1.0)       20.1239 (1.68)      0.1803 (1.0)           3;0  49.6609 (0.61)         10           1
test_incremental_edit[jinja-pyrefly]      53.2751 (4.51)      67.2008 (4.93)      60.3027 (4.92)      4.5815 (34.19)     59.1167 (4.94)      5.8406 (32.40)         4;0  16.5830 (0.20)         10           1
test_incremental_edit[jinja-pyright]     476.3300 (40.36)    530.7210 (38.90)    503.8855 (41.13)    14.1706 (105.75)   505.3668 (42.20)    11.4062 (63.28)         2;2   1.9846 (0.02)         10           1
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

---------------------------------------------------------------------------------------- benchmark 'pandas': 4 tests -----------------------------------------------------------------------------------------
Name (time in ms)                              Min                 Max                Mean             StdDev              Median               IQR            Outliers      OPS            Rounds  Iterations
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_incremental_edit[pandas-ty]           42.7908 (1.0)       49.9526 (1.0)       43.8403 (1.0)       2.1643 (1.0)       43.1829 (1.0)      0.3528 (1.0)           1;1  22.8101 (1.0)          10           1
test_incremental_edit[pandas-pyrefly]     243.4753 (5.69)     256.9783 (5.14)     248.6074 (5.67)      4.2473 (1.96)     247.6178 (5.73)     6.6526 (18.86)         2;0   4.0224 (0.18)         10           1
test_incremental_edit[pandas-zuban]       251.8713 (5.89)     259.0576 (5.19)     254.0977 (5.80)      2.2326 (1.03)     253.3567 (5.87)     2.0706 (5.87)          2;1   3.9355 (0.17)         10           1
test_incremental_edit[pandas-pyright]     662.6549 (15.49)    701.7632 (14.05)    691.2085 (15.77)    11.6618 (5.39)     695.5558 (16.11)    8.8209 (25.01)         1;1   1.4467 (0.06)         10           1
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

------------------------------------------------------------------------------------------ benchmark 'prefect': 4 tests -----------------------------------------------------------------------------------------
Name (time in ms)                               Min                 Max                Mean             StdDev              Median                IQR            Outliers       OPS            Rounds  Iterations
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_incremental_edit[prefect-ty]            7.7396 (1.0)        8.2893 (1.0)        7.9743 (1.0)       0.1873 (1.0)        7.9549 (1.0)       0.3074 (1.0)           3;0  125.4032 (1.0)          10           1
test_incremental_edit[prefect-pyrefly]      51.3062 (6.63)      61.9334 (7.47)      56.2614 (7.06)      3.5354 (18.88)     57.8409 (7.27)      5.8660 (19.08)         4;0   17.7742 (0.14)         10           1
test_incremental_edit[prefect-zuban]       131.5461 (17.00)    132.8311 (16.02)    132.0289 (16.56)     0.4032 (2.15)     131.9307 (16.58)     0.4938 (1.61)          3;0    7.5741 (0.06)         10           1
test_incremental_edit[prefect-pyright]     660.4608 (85.34)    695.6145 (83.92)    680.8583 (85.38)    10.4803 (55.97)    682.6589 (85.82)    14.5401 (47.30)         3;0    1.4687 (0.01)         10           1
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

----------------------------------------------------------------------------------------- benchmark 'pytorch': 3 tests ----------------------------------------------------------------------------------------
Name (time in ms)                               Min                 Max                Mean            StdDev              Median               IQR            Outliers       OPS            Rounds  Iterations
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_incremental_edit[pytorch-ty]            3.8246 (1.0)        4.2305 (1.0)        3.9541 (1.0)      0.1286 (1.0)        3.8931 (1.0)      0.1671 (1.0)           2;0  252.8999 (1.0)          10           1
test_incremental_edit[pytorch-pyrefly]      20.1780 (5.28)      25.2127 (5.96)      22.7988 (5.77)     1.8837 (14.64)     23.4518 (6.02)     3.4646 (20.73)         4;0   43.8619 (0.17)         10           1
test_incremental_edit[pytorch-pyright]     411.6034 (107.62)   420.5795 (99.42)    416.2569 (105.27)   2.2362 (17.38)    416.0866 (106.88)   1.0938 (6.54)          2;2    2.4024 (0.01)         10           1
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

------------------------------------------------------------------------------------------ benchmark 'httpx': 4 tests -----------------------------------------------------------------------------------------
Name (time in ms)                             Min                 Max                Mean             StdDev              Median                IQR            Outliers       OPS            Rounds  Iterations
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_incremental_edit[httpx-ty]            7.2699 (1.0)        7.7374 (1.0)        7.4799 (1.0)       0.1762 (1.0)        7.4646 (1.0)       0.3094 (1.65)          4;0  133.6924 (1.0)          10           1
test_incremental_edit[httpx-zuban]         9.5517 (1.31)      11.7660 (1.52)       9.9430 (1.33)      0.6486 (3.68)       9.7386 (1.30)      0.1877 (1.0)           1;1  100.5729 (0.75)         10           1
test_incremental_edit[httpx-pyrefly]      47.6866 (6.56)      57.0288 (7.37)      51.7039 (6.91)      2.8466 (16.15)     52.0920 (6.98)      3.3798 (18.01)         3;0   19.3409 (0.14)         10           1
test_incremental_edit[httpx-pyright]     414.3220 (56.99)    441.5353 (57.06)    426.5495 (57.03)    10.4990 (59.58)    426.0099 (57.07)    20.2930 (108.11)        5;0    2.3444 (0.02)         10           1
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------------- benchmark 'numpy': 3 tests --------------------------------------------------------------------------------------------
Name (time in ms)                               Min                   Max                  Mean             StdDev                Median               IQR            Outliers      OPS            Rounds  Iterations
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_incremental_edit[numpy-ty]             29.4276 (1.0)         30.9400 (1.0)         29.7841 (1.0)       0.4350 (1.0)         29.7153 (1.0)      0.2702 (1.0)           1;1  33.5749 (1.0)          10           1
test_incremental_edit[numpy-pyrefly]       330.8268 (11.24)      350.2634 (11.32)      343.7851 (11.54)     6.4024 (14.72)      346.1157 (11.65)    7.2750 (26.92)         3;0   2.9088 (0.09)         10           1
test_incremental_edit[numpy-pyright]     1,171.7334 (39.82)    1,205.3624 (38.96)    1,188.2385 (39.90)    10.2539 (23.57)    1,189.4224 (40.03)    9.2393 (34.19)         3;0   0.8416 (0.03)         10           1
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

----------------------------------------------------------------------------------------- benchmark 'fastapi': 4 tests ----------------------------------------------------------------------------------------
Name (time in ms)                               Min                 Max                Mean            StdDev              Median               IQR            Outliers       OPS            Rounds  Iterations
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_incremental_edit[fastapi-ty]            6.9249 (1.0)        7.6399 (1.0)        7.3272 (1.0)      0.2114 (1.65)       7.3312 (1.0)      0.2377 (1.33)          3;0  136.4773 (1.0)          10           1
test_incremental_edit[fastapi-zuban]         8.3563 (1.21)       8.7793 (1.15)       8.5171 (1.16)     0.1283 (1.0)        8.4884 (1.16)     0.1784 (1.0)           2;0  117.4108 (0.86)         10           1
test_incremental_edit[fastapi-pyrefly]      58.2667 (8.41)      69.4830 (9.09)      65.8294 (8.98)     3.4123 (26.60)     67.0105 (9.14)     4.0596 (22.76)         2;0   15.1908 (0.11)         10           1
test_incremental_edit[fastapi-pyright]     604.3037 (87.27)    621.4753 (81.35)    614.2073 (83.83)    5.5771 (43.48)    614.2024 (83.78)    8.3417 (46.76)         3;0    1.6281 (0.01)         10           1
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

---------------------------------------------------------------------------------------- benchmark 'sqlalchemy': 4 tests ----------------------------------------------------------------------------------------
Name (time in ms)                                  Min                 Max                Mean            StdDev              Median               IQR            Outliers      OPS            Rounds  Iterations
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_incremental_edit[sqlalchemy-ty]           11.3707 (1.0)       12.0433 (1.0)       11.6455 (1.0)      0.2271 (1.0)       11.6070 (1.0)      0.1715 (1.0)           3;2  85.8698 (1.0)          10           1
test_incremental_edit[sqlalchemy-pyrefly]      56.7484 (4.99)      84.5526 (7.02)      76.4313 (6.56)     7.9762 (35.13)     76.2125 (6.57)     7.9097 (46.11)         2;1  13.0836 (0.15)         10           1
test_incremental_edit[sqlalchemy-zuban]       198.5378 (17.46)    201.8470 (16.76)    199.5849 (17.14)    0.9838 (4.33)     199.1490 (17.16)    1.1792 (6.87)          2;0   5.0104 (0.06)         10           1
test_incremental_edit[sqlalchemy-pyright]     632.0858 (55.59)    647.3986 (53.76)    639.0595 (54.88)    5.6518 (24.89)    640.6409 (55.19)    9.4287 (54.96)         5;0   1.5648 (0.02)         10           1
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

----------------------------------------------------------------------------------------- benchmark 'rich': 4 tests -----------------------------------------------------------------------------------------
Name (time in ms)                            Min                 Max                Mean            StdDev              Median                IQR            Outliers       OPS            Rounds  Iterations
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_incremental_edit[rich-ty]            5.6515 (1.0)        6.0750 (1.0)        5.9198 (1.0)      0.1533 (1.0)        5.9963 (1.0)       0.2132 (1.0)           3;0  168.9252 (1.0)          10           1
test_incremental_edit[rich-zuban]        12.7459 (2.26)      14.8288 (2.44)      13.1219 (2.22)     0.6140 (4.00)      12.9070 (2.15)      0.2442 (1.15)          1;1   76.2082 (0.45)         10           1
test_incremental_edit[rich-pyrefly]      20.0278 (3.54)      41.4377 (6.82)      31.1428 (5.26)     7.2154 (47.05)     34.0170 (5.67)     12.2488 (57.46)         4;0   32.1102 (0.19)         10           1
test_incremental_edit[rich-pyright]     433.5527 (76.72)    446.9955 (73.58)    440.7714 (74.46)    4.4355 (28.93)    442.3849 (73.78)     6.2345 (29.25)         3;0    2.2687 (0.01)         10           1
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

----------------------------------------------------------------------------------------- benchmark 'django': 4 tests ------------------------------------------------------------------------------------------
Name (time in ms)                              Min                 Max                Mean             StdDev              Median                IQR            Outliers       OPS            Rounds  Iterations
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_incremental_edit[django-zuban]         1.7699 (1.0)        1.9427 (1.0)        1.8348 (1.0)       0.0613 (1.0)        1.8271 (1.0)       0.1039 (1.0)           4;0  545.0284 (1.0)          10           1
test_incremental_edit[django-ty]            3.7858 (2.14)       4.1484 (2.14)       4.0207 (2.19)      0.1021 (1.67)       4.0422 (2.21)      0.1108 (1.07)          2;1  248.7111 (0.46)         10           1
test_incremental_edit[django-pyrefly]      21.2110 (11.98)     29.9794 (15.43)     25.4880 (13.89)     3.1539 (51.45)     26.3823 (14.44)     5.5899 (53.81)         4;0   39.2342 (0.07)         10           1
test_incremental_edit[django-pyright]     330.7418 (186.87)   381.0605 (196.15)   354.0818 (192.98)   21.3677 (348.54)   341.3754 (186.84)   39.9063 (384.17)        5;0    2.8242 (0.01)         10           1
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

----------------------------------------------------------------------------------------- benchmark 'sympy': 4 tests -----------------------------------------------------------------------------------------
Name (time in ms)                             Min                 Max                Mean            StdDev              Median                IQR            Outliers       OPS            Rounds  Iterations
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_incremental_edit[sympy-ty]            3.2490 (1.0)        3.5340 (1.0)        3.3801 (1.0)      0.1064 (1.0)        3.3666 (1.0)       0.1848 (1.0)           5;0  295.8470 (1.0)          10           1
test_incremental_edit[sympy-pyrefly]      28.2025 (8.68)      38.2077 (10.81)     33.0703 (9.78)     3.0461 (28.63)     32.1000 (9.53)      4.1055 (22.21)         3;0   30.2386 (0.10)         10           1
test_incremental_edit[sympy-zuban]        62.8081 (19.33)     67.0972 (18.99)     63.7676 (18.87)    1.3140 (12.35)     63.3715 (18.82)     0.7175 (3.88)          1;2   15.6819 (0.05)         10           1
test_incremental_edit[sympy-pyright]     465.8610 (143.38)   487.8697 (138.05)   479.7846 (141.94)   7.3209 (68.82)    478.8293 (142.23)   10.6199 (57.46)         3;0    2.0843 (0.01)         10           1
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

---------------------------------------------------------------------------------------- benchmark 'openai': 4 tests -----------------------------------------------------------------------------------------
Name (time in ms)                              Min                 Max                Mean            StdDev              Median               IQR            Outliers       OPS            Rounds  Iterations
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_incremental_edit[openai-zuban]         3.4460 (1.0)        3.6128 (1.0)        3.5186 (1.0)      0.0547 (1.0)        3.5069 (1.0)      0.0987 (1.0)           4;0  284.2066 (1.0)          10           1
test_incremental_edit[openai-ty]            3.9247 (1.14)       4.4592 (1.23)       4.1137 (1.17)     0.1438 (2.63)       4.1115 (1.17)     0.1087 (1.10)          2;1  243.0899 (0.86)         10           1
test_incremental_edit[openai-pyrefly]      70.9413 (20.59)     87.7718 (24.30)     82.7103 (23.51)    5.0859 (93.06)     83.1189 (23.70)    5.0480 (51.16)         1;1   12.0904 (0.04)         10           1
test_incremental_edit[openai-pyright]     457.0089 (132.62)   489.3018 (135.44)   478.7871 (136.07)   8.6623 (158.50)   481.2125 (137.22)   7.4462 (75.47)         2;1    2.0886 (0.01)         10           1
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

---------------------------------------------------------------------------------------- benchmark 'pytest': 4 tests -----------------------------------------------------------------------------------------
Name (time in ms)                              Min                 Max                Mean            StdDev              Median               IQR            Outliers       OPS            Rounds  Iterations
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_incremental_edit[pytest-ty]            8.7586 (1.0)        9.3595 (1.0)        9.0144 (1.0)      0.1665 (1.0)        8.9937 (1.0)      0.1641 (1.0)           2;1  110.9332 (1.0)          10           1
test_incremental_edit[pytest-zuban]        26.0735 (2.98)      26.7175 (2.85)      26.3351 (2.92)     0.1758 (1.06)      26.3459 (2.93)     0.2007 (1.22)          2;1   37.9721 (0.34)         10           1
test_incremental_edit[pytest-pyrefly]      55.3168 (6.32)      62.2285 (6.65)      58.5314 (6.49)     2.2135 (13.29)     58.4364 (6.50)     2.6986 (16.45)         3;0   17.0848 (0.15)         10           1
test_incremental_edit[pytest-pyright]     458.6860 (52.37)    490.4299 (52.40)    481.3327 (53.40)    8.7184 (52.36)    483.3412 (53.74)    6.7729 (41.28)         2;1    2.0776 (0.02)         10           1
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
```

### Fetch diagnostics

```shell
----------------------------------------------------------------------------------------- benchmark 'black': 4 tests ----------------------------------------------------------------------------------------
Name (time in ms)                              Min                 Max                Mean            StdDev              Median               IQR            Outliers      OPS            Rounds  Iterations
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_fetch_diagnostics[black-ty]           67.6102 (1.0)       67.9940 (1.0)       67.8406 (1.0)      0.1106 (1.0)       67.8308 (1.0)      0.1467 (1.0)           3;0  14.7404 (1.0)          10           1
test_fetch_diagnostics[black-zuban]        68.9572 (1.02)      73.7763 (1.09)      71.2262 (1.05)     1.4690 (13.28)     71.0236 (1.05)     2.1367 (14.56)         2;0  14.0398 (0.95)         10           1
test_fetch_diagnostics[black-pyrefly]     179.8352 (2.66)     181.0037 (2.66)     180.5095 (2.66)     0.4111 (3.72)     180.5079 (2.66)     0.6513 (4.44)          4;0   5.5399 (0.38)         10           1
test_fetch_diagnostics[black-pyright]     299.9607 (4.44)     302.2230 (4.44)     300.9091 (4.44)     0.6684 (6.04)     300.8832 (4.44)     0.6293 (4.29)          3;0   3.3233 (0.23)         10           1
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

----------------------------------------------------------------------------------------- benchmark 'discord.py': 4 tests -----------------------------------------------------------------------------------------
Name (time in ms)                                   Min                 Max                Mean             StdDev              Median                IQR            Outliers     OPS            Rounds  Iterations
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_fetch_diagnostics[discord.py-ty]          104.1270 (1.0)      105.6242 (1.0)      104.7038 (1.0)       0.4102 (1.63)     104.6941 (1.0)       0.4468 (2.30)          2;1  9.5508 (1.0)          10           1
test_fetch_diagnostics[discord.py-zuban]       177.4120 (1.70)     184.2058 (1.74)     180.0302 (1.72)      2.0807 (8.26)     179.8533 (1.72)      1.9461 (10.03)         3;1  5.5546 (0.58)         10           1
test_fetch_diagnostics[discord.py-pyrefly]     187.9900 (1.81)     188.8244 (1.79)     188.3708 (1.80)      0.2520 (1.0)      188.3499 (1.80)      0.1941 (1.0)           4;2  5.3087 (0.56)         10           1
test_fetch_diagnostics[discord.py-pyright]     621.1201 (5.97)     663.5259 (6.28)     630.2578 (6.02)     12.6775 (50.30)    626.5515 (5.98)     11.5769 (59.64)         1;1  1.5867 (0.17)         10           1
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------------- benchmark 'homeassistant': 4 tests ---------------------------------------------------------------------------------------------
Name (time in ms)                                        Min                   Max                  Mean             StdDev                Median                IQR            Outliers     OPS            Rounds  Iterations
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_fetch_diagnostics[homeassistant-ty]            100.7611 (1.0)        105.6920 (1.0)        101.5776 (1.0)       1.4821 (1.42)       101.0498 (1.0)       0.4627 (1.0)           1;1  9.8447 (1.0)          10           1
test_fetch_diagnostics[homeassistant-zuban]         214.2382 (2.13)       219.2897 (2.07)       217.0925 (2.14)      1.7237 (1.65)       217.0206 (2.15)      2.0827 (4.50)          4;0  4.6063 (0.47)         10           1
test_fetch_diagnostics[homeassistant-pyrefly]       236.2060 (2.34)       239.4906 (2.27)       237.6687 (2.34)      1.0456 (1.0)        237.4407 (2.35)      1.0302 (2.23)          3;0  4.2075 (0.43)         10           1
test_fetch_diagnostics[homeassistant-pyright]     1,890.3885 (18.76)    1,924.0052 (18.20)    1,905.1369 (18.76)    10.7615 (10.29)    1,903.1950 (18.83)    14.3797 (31.07)         4;0  0.5249 (0.05)         10           1
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

----------------------------------------------------------------------------------------- benchmark 'isort': 4 tests -----------------------------------------------------------------------------------------
Name (time in ms)                              Min                 Max                Mean            StdDev              Median                IQR            Outliers      OPS            Rounds  Iterations
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_fetch_diagnostics[isort-zuban]        39.6183 (1.0)       44.7363 (1.0)       41.2833 (1.0)      1.4294 (3.34)      40.9556 (1.0)       1.3667 (5.44)          2;1  24.2229 (1.0)          10           1
test_fetch_diagnostics[isort-ty]           49.7201 (1.25)      51.3446 (1.15)      50.2694 (1.22)     0.4280 (1.0)       50.2065 (1.23)      0.2513 (1.0)           2;1  19.8928 (0.82)         10           1
test_fetch_diagnostics[isort-pyrefly]     126.7168 (3.20)     140.7936 (3.15)     134.1324 (3.25)     5.9800 (13.97)    134.6929 (3.29)     11.4701 (45.64)         4;0   7.4553 (0.31)         10           1
test_fetch_diagnostics[isort-pyright]     355.6153 (8.98)     360.0408 (8.05)     358.0638 (8.67)     1.4327 (3.35)     358.1251 (8.74)      2.5620 (10.20)         4;0   2.7928 (0.12)         10           1
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

----------------------------------------------------------------------------------------- benchmark 'jinja': 4 tests ----------------------------------------------------------------------------------------
Name (time in ms)                              Min                 Max                Mean            StdDev              Median               IQR            Outliers      OPS            Rounds  Iterations
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_fetch_diagnostics[jinja-ty]           51.3826 (1.0)       51.7350 (1.0)       51.5128 (1.0)      0.1209 (1.0)       51.4767 (1.0)      0.2154 (1.0)           3;0  19.4126 (1.0)          10           1
test_fetch_diagnostics[jinja-zuban]        85.7727 (1.67)      88.3310 (1.71)      86.9519 (1.69)     0.7278 (6.02)      87.0239 (1.69)     0.7648 (3.55)          2;0  11.5006 (0.59)         10           1
test_fetch_diagnostics[jinja-pyrefly]     125.6743 (2.45)     126.7780 (2.45)     126.3703 (2.45)     0.3741 (3.09)     126.4106 (2.46)     0.6636 (3.08)          4;0   7.9133 (0.41)         10           1
test_fetch_diagnostics[jinja-pyright]     353.2582 (6.88)     361.2105 (6.98)     356.3589 (6.92)     2.3240 (19.22)    355.8286 (6.91)     3.4593 (16.06)         2;0   2.8062 (0.14)         10           1
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

---------------------------------------------------------------------------------------- benchmark 'pandas': 4 tests ----------------------------------------------------------------------------------------
Name (time in ms)                               Min                 Max                Mean            StdDev              Median               IQR            Outliers     OPS            Rounds  Iterations
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_fetch_diagnostics[pandas-ty]          369.3500 (1.0)      378.3583 (1.0)      371.4269 (1.0)      2.5523 (1.0)      370.7300 (1.0)      0.6945 (1.0)           1;2  2.6923 (1.0)          10           1
test_fetch_diagnostics[pandas-pyrefly]     539.1561 (1.46)     562.5021 (1.49)     543.9112 (1.46)     6.9893 (2.74)     541.4131 (1.46)     2.4565 (3.54)          1;2  1.8385 (0.68)         10           1
test_fetch_diagnostics[pandas-pyright]     629.9906 (1.71)     647.6225 (1.71)     639.1170 (1.72)     5.6742 (2.22)     640.4880 (1.73)     9.5839 (13.80)         4;0  1.5647 (0.58)         10           1
test_fetch_diagnostics[pandas-zuban]       666.4379 (1.80)     680.6972 (1.80)     673.7827 (1.81)     4.4995 (1.76)     673.4846 (1.82)     6.0168 (8.66)          3;0  1.4842 (0.55)         10           1
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------------- benchmark 'prefect': 4 tests ---------------------------------------------------------------------------------------------
Name (time in ms)                                  Min                   Max                  Mean             StdDev                Median                IQR            Outliers     OPS            Rounds  Iterations
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_fetch_diagnostics[prefect-ty]            175.9255 (1.0)        177.0483 (1.0)        176.4931 (1.0)       0.3420 (1.0)        176.4672 (1.0)       0.5711 (1.0)           2;0  5.6659 (1.0)          10           1
test_fetch_diagnostics[prefect-pyrefly]       332.9010 (1.89)       467.9147 (2.64)       452.5213 (2.56)     42.0522 (122.97)     465.0061 (2.64)      2.8783 (5.04)          1;1  2.2098 (0.39)         10           1
test_fetch_diagnostics[prefect-zuban]         859.7134 (4.89)       865.6050 (4.89)       863.4421 (4.89)      2.2602 (6.61)       864.5682 (4.90)      3.9808 (6.97)          3;0  1.1582 (0.20)         10           1
test_fetch_diagnostics[prefect-pyright]     1,102.1569 (6.26)     1,130.7971 (6.39)     1,113.3106 (6.31)     10.0063 (29.26)    1,112.3842 (6.30)     16.5983 (29.06)         5;0  0.8982 (0.16)         10           1
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

---------------------------------------------------------------------------------------------- benchmark 'pytorch': 4 tests ---------------------------------------------------------------------------------------------
Name (time in ms)                                  Min                   Max                  Mean             StdDev                Median                IQR            Outliers      OPS            Rounds  Iterations
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_fetch_diagnostics[pytorch-ty]             71.3789 (1.0)         72.1315 (1.0)         71.6974 (1.0)       0.2211 (1.0)         71.7121 (1.0)       0.2155 (1.0)           3;1  13.9475 (1.0)          10           1
test_fetch_diagnostics[pytorch-pyrefly]       116.7863 (1.64)       145.4521 (2.02)       128.6864 (1.79)     14.0053 (63.36)      118.9156 (1.66)     27.4318 (127.29)        4;0   7.7708 (0.56)         10           1
test_fetch_diagnostics[pytorch-pyright]       702.6213 (9.84)       709.5476 (9.84)       705.4807 (9.84)      2.5295 (11.44)      704.5238 (9.82)      4.3440 (20.16)         3;0   1.4175 (0.10)         10           1
test_fetch_diagnostics[pytorch-zuban]       1,825.0715 (25.57)    1,860.6000 (25.79)    1,835.6793 (25.60)     9.9072 (44.82)    1,835.3201 (25.59)     8.8780 (41.20)         2;1   0.5448 (0.04)         10           1
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

----------------------------------------------------------------------------------------- benchmark 'httpx': 4 tests ----------------------------------------------------------------------------------------
Name (time in ms)                              Min                 Max                Mean            StdDev              Median               IQR            Outliers      OPS            Rounds  Iterations
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_fetch_diagnostics[httpx-ty]           46.3343 (1.0)       46.6930 (1.0)       46.4535 (1.0)      0.1079 (1.0)       46.4308 (1.0)      0.1212 (1.0)           2;1  21.5269 (1.0)          10           1
test_fetch_diagnostics[httpx-zuban]        69.2425 (1.49)      71.2874 (1.53)      70.2522 (1.51)     0.6870 (6.36)      70.2971 (1.51)     0.9758 (8.05)          3;0  14.2344 (0.66)         10           1
test_fetch_diagnostics[httpx-pyrefly]     114.3010 (2.47)     118.0325 (2.53)     115.3196 (2.48)     1.1948 (11.07)    114.8530 (2.47)     1.1663 (9.62)          2;1   8.6716 (0.40)         10           1
test_fetch_diagnostics[httpx-pyright]     224.9341 (4.85)     228.4704 (4.89)     226.4147 (4.87)     1.0548 (9.77)     226.3045 (4.87)     1.0174 (8.39)          3;1   4.4167 (0.21)         10           1
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

------------------------------------------------------------------------------------------------ benchmark 'numpy': 4 tests -----------------------------------------------------------------------------------------------
Name (time in ms)                                 Min                    Max                   Mean             StdDev                 Median                 IQR            Outliers     OPS            Rounds  Iterations
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_fetch_diagnostics[numpy-ty]             307.2674 (1.0)         311.5868 (1.0)         308.3130 (1.0)       1.2980 (1.0)         307.7579 (1.0)        1.2570 (1.35)          1;1  3.2435 (1.0)          10           1
test_fetch_diagnostics[numpy-pyrefly]        562.9346 (1.83)        568.0607 (1.82)        564.3641 (1.83)      1.4365 (1.11)        564.1055 (1.83)       0.9281 (1.0)           1;1  1.7719 (0.55)         10           1
test_fetch_diagnostics[numpy-pyright]      1,182.4547 (3.85)      1,212.2849 (3.89)      1,199.6223 (3.89)      9.0291 (6.96)      1,198.6239 (3.89)      12.4973 (13.47)         3;0  0.8336 (0.26)         10           1
test_fetch_diagnostics[numpy-zuban]       36,078.9349 (117.42)   36,423.6785 (116.90)   36,193.5729 (117.39)   98.8916 (76.19)    36,198.7695 (117.62)   119.7505 (129.02)        2;1  0.0276 (0.01)         10           1
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

---------------------------------------------------------------------------------------- benchmark 'fastapi': 4 tests ----------------------------------------------------------------------------------------
Name (time in ms)                                Min                 Max                Mean            StdDev              Median               IQR            Outliers     OPS            Rounds  Iterations
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_fetch_diagnostics[fastapi-ty]           99.9857 (1.0)      110.5458 (1.0)      102.0239 (1.0)      3.3295 (5.70)     100.6824 (1.0)      0.9932 (1.63)          1;2  9.8016 (1.0)          10           1
test_fetch_diagnostics[fastapi-zuban]       171.4969 (1.72)     177.0828 (1.60)     173.4509 (1.70)     1.8097 (3.10)     173.0481 (1.72)     2.5310 (4.14)          3;0  5.7653 (0.59)         10           1
test_fetch_diagnostics[fastapi-pyrefly]     199.6927 (2.00)     201.7180 (1.82)     200.3882 (1.96)     0.5838 (1.0)      200.3402 (1.99)     0.6110 (1.0)           2;1  4.9903 (0.51)         10           1
test_fetch_diagnostics[fastapi-pyright]     457.2369 (4.57)     470.3823 (4.26)     465.9305 (4.57)     3.9981 (6.85)     466.0065 (4.63)     4.5289 (7.41)          3;1  2.1462 (0.22)         10           1
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

---------------------------------------------------------------------------------------- benchmark 'sqlalchemy': 4 tests ----------------------------------------------------------------------------------------
Name (time in ms)                                   Min                 Max                Mean            StdDev              Median               IQR            Outliers     OPS            Rounds  Iterations
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_fetch_diagnostics[sqlalchemy-ty]          215.3330 (1.0)      217.2247 (1.0)      216.2931 (1.0)      0.5781 (1.0)      216.3475 (1.0)      0.6100 (1.0)           3;0  4.6234 (1.0)          10           1
test_fetch_diagnostics[sqlalchemy-pyrefly]     250.0255 (1.16)     256.0001 (1.18)     251.9413 (1.16)     1.6665 (2.88)     251.7372 (1.16)     1.6916 (2.77)          2;1  3.9692 (0.86)         10           1
test_fetch_diagnostics[sqlalchemy-pyright]     270.1789 (1.25)     276.0185 (1.27)     272.7359 (1.26)     1.6008 (2.77)     272.7561 (1.26)     1.5684 (2.57)          2;1  3.6666 (0.79)         10           1
test_fetch_diagnostics[sqlalchemy-zuban]       383.2057 (1.78)     399.6241 (1.84)     386.9370 (1.79)     4.6166 (7.99)     385.5155 (1.78)     2.3762 (3.90)          1;1  2.5844 (0.56)         10           1
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

---------------------------------------------------------------------------------------- benchmark 'rich': 4 tests -----------------------------------------------------------------------------------------
Name (time in ms)                             Min                 Max                Mean            StdDev              Median               IQR            Outliers      OPS            Rounds  Iterations
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_fetch_diagnostics[rich-ty]           42.8379 (1.0)       44.2461 (1.0)       43.0884 (1.0)      0.4288 (1.0)       42.9530 (1.0)      0.2049 (1.0)           1;1  23.2081 (1.0)          10           1
test_fetch_diagnostics[rich-zuban]        79.5685 (1.86)      82.3503 (1.86)      80.7725 (1.87)     0.8009 (1.87)      80.6681 (1.88)     0.5338 (2.61)          3;2  12.3804 (0.53)         10           1
test_fetch_diagnostics[rich-pyrefly]      99.5237 (2.32)     115.1077 (2.60)     110.9954 (2.58)     5.6315 (13.13)    113.2185 (2.64)     1.7742 (8.66)          2;2   9.0094 (0.39)         10           1
test_fetch_diagnostics[rich-pyright]     309.8927 (7.23)     314.1458 (7.10)     311.3170 (7.23)     1.3331 (3.11)     310.9984 (7.24)     1.9001 (9.27)          3;0   3.2122 (0.14)         10           1
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

---------------------------------------------------------------------------------------- benchmark 'django': 4 tests -----------------------------------------------------------------------------------------
Name (time in ms)                               Min                 Max                Mean            StdDev              Median               IQR            Outliers      OPS            Rounds  Iterations
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_fetch_diagnostics[django-ty]           40.9135 (1.0)       41.1840 (1.0)       41.0596 (1.0)      0.0780 (1.0)       41.0696 (1.0)      0.1090 (1.0)           2;0  24.3549 (1.0)          10           1
test_fetch_diagnostics[django-zuban]        45.0162 (1.10)      47.3812 (1.15)      46.3298 (1.13)     0.7499 (9.61)      46.4050 (1.13)     0.7135 (6.54)          4;1  21.5844 (0.89)         10           1
test_fetch_diagnostics[django-pyrefly]      90.8160 (2.22)      96.1161 (2.33)      94.1640 (2.29)     2.2035 (28.24)     95.3465 (2.32)     4.3802 (40.17)         3;0  10.6198 (0.44)         10           1
test_fetch_diagnostics[django-pyright]     587.8771 (14.37)    610.7550 (14.83)    593.6576 (14.46)    8.6595 (111.00)   589.8123 (14.36)    2.7981 (25.66)         2;2   1.6845 (0.07)         10           1
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

----------------------------------------------------------------------------------------- benchmark 'sympy': 4 tests ----------------------------------------------------------------------------------------
Name (time in ms)                              Min                 Max                Mean            StdDev              Median               IQR            Outliers      OPS            Rounds  Iterations
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_fetch_diagnostics[sympy-ty]           75.1789 (1.0)       75.5107 (1.0)       75.3566 (1.0)      0.1023 (1.0)       75.3472 (1.0)      0.1130 (1.0)           3;0  13.2702 (1.0)          10           1
test_fetch_diagnostics[sympy-pyrefly]     179.4386 (2.39)     183.1834 (2.43)     180.5083 (2.40)     1.0781 (10.54)    180.2387 (2.39)     0.5938 (5.26)          1;1   5.5399 (0.42)         10           1
test_fetch_diagnostics[sympy-zuban]       260.1722 (3.46)     274.6859 (3.64)     265.9684 (3.53)     4.4955 (43.93)    264.4641 (3.51)     7.1645 (63.43)         2;0   3.7598 (0.28)         10           1
test_fetch_diagnostics[sympy-pyright]     392.3544 (5.22)     400.7913 (5.31)     396.7093 (5.26)     2.7972 (27.33)    396.7134 (5.27)     5.3469 (47.34)         4;0   2.5207 (0.19)         10           1
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

---------------------------------------------------------------------------------------- benchmark 'openai': 4 tests -----------------------------------------------------------------------------------------
Name (time in ms)                               Min                 Max                Mean            StdDev              Median               IQR            Outliers      OPS            Rounds  Iterations
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_fetch_diagnostics[openai-ty]           70.1926 (1.0)       71.4647 (1.0)       70.5637 (1.0)      0.3530 (1.0)       70.4515 (1.0)      0.2744 (1.0)           2;1  14.1716 (1.0)          10           1
test_fetch_diagnostics[openai-zuban]       139.0193 (1.98)     143.9898 (2.01)     141.1401 (2.00)     1.4470 (4.10)     140.7476 (2.00)     1.9043 (6.94)          2;0   7.0852 (0.50)         10           1
test_fetch_diagnostics[openai-pyrefly]     188.4392 (2.68)     202.4323 (2.83)     199.4188 (2.83)     5.1057 (14.46)    201.7685 (2.86)     1.2412 (4.52)          2;2   5.0146 (0.35)         10           1
test_fetch_diagnostics[openai-pyright]     513.3347 (7.31)     518.7722 (7.26)     515.7981 (7.31)     2.2311 (6.32)     515.5012 (7.32)     4.6511 (16.95)         5;0   1.9387 (0.14)         10           1
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

---------------------------------------------------------------------------------------- benchmark 'pytest': 4 tests -----------------------------------------------------------------------------------------
Name (time in ms)                               Min                 Max                Mean            StdDev              Median               IQR            Outliers      OPS            Rounds  Iterations
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_fetch_diagnostics[pytest-ty]           78.7732 (1.0)       79.4850 (1.0)       79.0138 (1.0)      0.2058 (1.0)       78.9445 (1.0)      0.2460 (1.0)           2;0  12.6560 (1.0)          10           1
test_fetch_diagnostics[pytest-zuban]       132.7784 (1.69)     135.7364 (1.71)     134.2270 (1.70)     1.0887 (5.29)     134.4337 (1.70)     1.9573 (7.96)          5;0   7.4501 (0.59)         10           1
test_fetch_diagnostics[pytest-pyrefly]     183.1395 (2.32)     186.5047 (2.35)     185.1065 (2.34)     1.0400 (5.05)     185.1994 (2.35)     1.2209 (4.96)          4;0   5.4023 (0.43)         10           1
test_fetch_diagnostics[pytest-pyright]     289.3343 (3.67)     291.7467 (3.67)     290.7208 (3.68)     0.7864 (3.82)     290.6446 (3.68)     1.2309 (5.00)          3;0   3.4397 (0.27)         10           1
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
```
