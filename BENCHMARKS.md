# Benchmarks

All benchmarks were computed on macOS (Apple M3 Max 16, 128 GB) with the following tool versions:

- [Pyrefly](https://pypi.org/project/pyrefly/) 1.4.0
- [Pyright](https://www.npmjs.com/package/pyright) 1.1.414
- [mypy](https://pypi.org/project/mypy/) 2.4.0
- [ty](https://pypi.org/project/ty/) 0.0.108
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
  Time (mean ± σ):      62.5 ms ±   2.7 ms    [User: 432.2 ms, System: 30.4 ms]
  Range (min … max):    57.2 ms …  70.9 ms    34 runs
  Memory (peak RSS):  133.8 MiB

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
    2.04 ± 0.09 times faster than Pyrefly
    2.30 ± 0.10 times faster than Zuban
   14.75 ± 0.64 times faster than mypy
   26.63 ± 1.15 times faster than Pyright

-------------------------------------------------------------------------------

discord.py
----------

Benchmark 1: ty
  Time (mean ± σ):     126.8 ms ±   7.3 ms    [User: 1202.7 ms, System: 68.2 ms]
  Range (min … max):   109.0 ms … 142.9 ms    19 runs
  Memory (peak RSS):  220.7 MiB

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
    1.37 ± 0.09 times faster than Pyrefly
    2.81 ± 0.16 times faster than Zuban
   16.45 ± 0.95 times faster than mypy
   31.45 ± 1.81 times faster than Pyright

-------------------------------------------------------------------------------

homeassistant
-------------

Benchmark 1: ty
  Time (mean ± σ):      2.099 s ±  0.100 s    [User: 25.313 s, System: 4.196 s]
  Range (min … max):    2.003 s …  2.321 s    10 runs
  Memory (peak RSS):  3,476 MiB

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
    1.10 ± 0.05 times faster than Pyrefly
    3.55 ± 0.17 times faster than Zuban
   24.79 ± 1.20 times faster than mypy
   60.49 ± 4.48 times faster than Pyright

-------------------------------------------------------------------------------

isort
-----

Benchmark 1: ty
  Time (mean ± σ):      62.7 ms ±   1.4 ms    [User: 198.6 ms, System: 16.1 ms]
  Range (min … max):    60.5 ms …  65.8 ms    34 runs
  Memory (peak RSS):   86.1 MiB

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
    1.05 ± 0.03 times faster than Zuban
    1.68 ± 0.05 times faster than Pyrefly
    7.25 ± 0.17 times faster than mypy
   26.00 ± 0.63 times faster than Pyright

-------------------------------------------------------------------------------

jinja
-----

Benchmark 1: ty
  Time (mean ± σ):      52.1 ms ±   1.4 ms    [User: 250.8 ms, System: 17.3 ms]
  Range (min … max):    49.6 ms …  56.2 ms    38 runs
  Memory (peak RSS):   98.9 MiB

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
    1.62 ± 0.05 times faster than Zuban
    2.00 ± 0.06 times faster than Pyrefly
   10.53 ± 0.33 times faster than mypy
   22.60 ± 0.61 times faster than Pyright

-------------------------------------------------------------------------------

pandas
------

Benchmark 1: ty
  Time (mean ± σ):     371.5 ms ±  26.4 ms    [User: 4101.0 ms, System: 213.4 ms]
  Range (min … max):   342.0 ms … 412.2 ms    10 runs
  Memory (peak RSS):  581.9 MiB

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
    2.39 ± 0.19 times faster than Pyrefly
    3.79 ± 0.27 times faster than Zuban
   28.18 ± 2.00 times faster than mypy
   42.50 ± 3.03 times faster than Pyright

-------------------------------------------------------------------------------

pandas-stubs
------------

Benchmark 1: ty
  Time (mean ± σ):      72.8 ms ±   4.2 ms    [User: 342.3 ms, System: 40.5 ms]
  Range (min … max):    65.6 ms …  80.7 ms    32 runs
  Memory (peak RSS):  154.4 MiB

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
    2.69 ± 0.16 times faster than Pyrefly
    3.72 ± 0.22 times faster than Zuban
   29.80 ± 1.72 times faster than Pyright
   65.42 ± 3.81 times faster than mypy

-------------------------------------------------------------------------------

prefect
-------

Benchmark 1: ty
  Time (mean ± σ):     103.5 ms ±   5.5 ms    [User: 642.2 ms, System: 48.0 ms]
  Range (min … max):    95.9 ms … 117.2 ms    21 runs
  Memory (peak RSS):  224.4 MiB

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
    2.62 ± 0.17 times faster than Pyrefly
    9.16 ± 0.49 times faster than Zuban
   27.28 ± 1.46 times faster than Pyright
   69.48 ± 3.79 times faster than mypy

-------------------------------------------------------------------------------

pytorch
-------

Benchmark 1: ty
  Time (mean ± σ):      1.235 s ±  0.055 s    [User: 15.349 s, System: 1.120 s]
  Range (min … max):    1.175 s …  1.332 s    10 runs
  Memory (peak RSS):  1,590 MiB

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
    1.02 ± 0.05 times faster than ty
    2.87 ± 0.04 times faster than Zuban
   21.05 ± 0.26 times faster than mypy
   61.41 ± 1.46 times faster than Pyright

-------------------------------------------------------------------------------

httpx
-----

Benchmark 1: ty
  Time (mean ± σ):      59.6 ms ±   1.7 ms    [User: 206.0 ms, System: 18.1 ms]
  Range (min … max):    56.6 ms …  63.1 ms    35 runs
  Memory (peak RSS):  102.8 MiB

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
    1.76 ± 0.05 times faster than Zuban
    1.98 ± 0.07 times faster than Pyrefly
   15.12 ± 0.46 times faster than mypy
   15.93 ± 0.49 times faster than Pyright

-------------------------------------------------------------------------------

numpy
-----

Benchmark 1: ty
  Time (mean ± σ):     170.0 ms ±   6.9 ms    [User: 989.3 ms, System: 71.7 ms]
  Range (min … max):   159.3 ms … 185.2 ms    15 runs
  Memory (peak RSS):  258.7 MiB

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
     3.42 ±  0.22 times faster than Pyrefly
   124.83 ±  5.07 times faster than Pyright
   476.08 ± 19.61 times faster than mypy

-------------------------------------------------------------------------------

fastapi
-------

Benchmark 1: ty
  Time (mean ± σ):      75.8 ms ±   4.6 ms    [User: 347.7 ms, System: 27.1 ms]
  Range (min … max):    69.6 ms …  85.9 ms    31 runs
  Memory (peak RSS):  142.2 MiB

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
    2.52 ± 0.15 times faster than Zuban
    3.92 ± 0.24 times faster than Pyrefly
   25.77 ± 1.57 times faster than mypy
   29.24 ± 1.76 times faster than Pyright

-------------------------------------------------------------------------------

sqlalchemy
----------

Benchmark 1: ty
  Time (mean ± σ):     295.4 ms ±  16.4 ms    [User: 3113.2 ms, System: 138.8 ms]
  Range (min … max):   272.3 ms … 327.2 ms    10 runs
  Memory (peak RSS):  411.1 MiB

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
    1.03 ± 0.06 times faster than Pyrefly
    2.24 ± 0.12 times faster than Zuban
   13.31 ± 0.75 times faster than mypy
   33.17 ± 1.86 times faster than Pyright

-------------------------------------------------------------------------------

rich
----

Benchmark 1: ty
  Time (mean ± σ):      59.7 ms ±   3.6 ms    [User: 368.8 ms, System: 30.2 ms]
  Range (min … max):    52.7 ms …  67.2 ms    33 runs
  Memory (peak RSS):  121.7 MiB

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
    2.06 ± 0.14 times faster than Pyrefly
    2.18 ± 0.14 times faster than Zuban
   20.26 ± 1.25 times faster than mypy
   42.08 ± 2.56 times faster than Pyright

-------------------------------------------------------------------------------

django
------

Benchmark 1: ty
  Time (mean ± σ):     236.7 ms ±  17.9 ms    [User: 2212.9 ms, System: 622.8 ms]
  Range (min … max):   221.9 ms … 280.3 ms    10 runs
  Memory (peak RSS):  319.7 MiB

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
    1.10 ± 0.08 times faster than Pyrefly
    2.16 ± 0.17 times faster than Zuban
   10.33 ± 0.79 times faster than mypy
   29.28 ± 2.22 times faster than Pyright

-------------------------------------------------------------------------------

sympy
-----

Benchmark 1: ty
  Time (mean ± σ):     635.2 ms ±  11.8 ms    [User: 7430.2 ms, System: 583.4 ms]
  Range (min … max):   619.2 ms … 658.6 ms    10 runs
  Memory (peak RSS):  717.7 MiB

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
    1.21 ± 0.03 times faster than ty
    2.33 ± 0.03 times faster than Zuban
   12.61 ± 0.15 times faster than mypy
   57.02 ± 0.72 times faster than Pyright

-------------------------------------------------------------------------------

openai
------

Benchmark 1: ty
  Time (mean ± σ):     259.8 ms ±  20.1 ms    [User: 2131.0 ms, System: 476.3 ms]
  Range (min … max):   225.0 ms … 285.3 ms    12 runs
  Memory (peak RSS):  335.0 MiB

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
    1.79 ± 0.15 times faster than Pyrefly
    3.31 ± 0.26 times faster than Zuban
   26.06 ± 2.02 times faster than mypy
   31.44 ± 2.44 times faster than Pyright

-------------------------------------------------------------------------------

pytest
------

Benchmark 1: ty
  Time (mean ± σ):     165.4 ms ±  12.6 ms    [User: 1298.9 ms, System: 79.0 ms]
  Range (min … max):   141.7 ms … 186.1 ms    18 runs
  Memory (peak RSS):  249.5 MiB

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
    1.37 ± 0.17 times faster than Pyrefly
    3.57 ± 0.27 times faster than Zuban
   14.39 ± 1.11 times faster than mypy
   27.66 ± 2.11 times faster than Pyright
```

## LSP

### Incremental edit

Zuban's server crashed on the incremental edits in discord.py, NumPy, and PyTorch.

```shell
---------------------------------------------------------------------------------------- benchmark 'black': 4 tests ----------------------------------------------------------------------------------------
Name (time in ms)                             Min                 Max                Mean            StdDev              Median               IQR            Outliers      OPS            Rounds  Iterations
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_incremental_edit[black-ty]           14.2012 (1.0)       15.8957 (1.0)       14.7891 (1.0)      0.4404 (1.0)       14.6921 (1.0)      0.2497 (1.0)           2;2  67.6172 (1.0)          10           1
test_incremental_edit[black-zuban]        18.8832 (1.33)      20.8855 (1.31)      19.3794 (1.31)     0.6267 (1.42)      19.2328 (1.31)     0.5062 (2.03)          2;1  51.6012 (0.76)         10           1
test_incremental_edit[black-pyrefly]      86.7763 (6.11)      97.2985 (6.12)      91.4009 (6.18)     3.0032 (6.82)      91.2891 (6.21)     4.0361 (16.16)         2;0  10.9408 (0.16)         10           1
test_incremental_edit[black-pyright]     540.2310 (38.04)    562.2411 (35.37)    549.4405 (37.15)    6.7233 (15.27)    548.0737 (37.30)    8.5098 (34.08)         4;0   1.8200 (0.03)         10           1
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

----------------------------------------------------------------------------------------- benchmark 'discord.py': 3 tests -----------------------------------------------------------------------------------------
Name (time in ms)                                  Min                 Max                Mean             StdDev              Median                IQR            Outliers      OPS            Rounds  Iterations
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_incremental_edit[discord.py-ty]           23.4332 (1.0)       28.1313 (1.0)       24.7526 (1.0)       1.3417 (1.0)       24.4432 (1.0)       0.5507 (1.0)           1;2  40.3998 (1.0)          10           1
test_incremental_edit[discord.py-pyrefly]      72.6280 (3.10)      82.8766 (2.95)      76.5269 (3.09)      3.7789 (2.82)      74.9435 (3.07)      7.2071 (13.09)         4;0  13.0673 (0.32)         10           1
test_incremental_edit[discord.py-pyright]     488.6511 (20.85)    541.3492 (19.24)    517.2384 (20.90)    16.5382 (12.33)    512.2913 (20.96)    22.0510 (40.04)         3;0   1.9333 (0.05)         10           1
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

---------------------------------------------------------------------------------------- benchmark 'homeassistant': 4 tests ----------------------------------------------------------------------------------------
Name (time in ms)                                     Min                 Max                Mean            StdDev              Median               IQR            Outliers      OPS            Rounds  Iterations
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_incremental_edit[homeassistant-ty]           27.0943 (1.0)       28.0577 (1.0)       27.5364 (1.0)      0.2931 (1.0)       27.5273 (1.0)      0.4699 (1.20)          3;0  36.3156 (1.0)          10           1
test_incremental_edit[homeassistant-pyrefly]      55.8462 (2.06)      85.5288 (3.05)      75.6855 (2.75)     8.0570 (27.48)     76.3312 (2.77)     4.9400 (12.58)         3;1  13.2126 (0.36)         10           1
test_incremental_edit[homeassistant-zuban]        56.2561 (2.08)      57.5430 (2.05)      57.0332 (2.07)     0.3593 (1.23)      57.0851 (2.07)     0.3927 (1.0)           2;0  17.5336 (0.48)         10           1
test_incremental_edit[homeassistant-pyright]     564.8898 (20.85)    580.5012 (20.69)    574.4756 (20.86)    4.9935 (17.03)    573.7045 (20.84)    6.9113 (17.60)         3;0   1.7407 (0.05)         10           1
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

----------------------------------------------------------------------------------------- benchmark 'isort': 4 tests ----------------------------------------------------------------------------------------
Name (time in ms)                             Min                 Max                Mean            StdDev              Median               IQR            Outliers       OPS            Rounds  Iterations
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_incremental_edit[isort-zuban]         5.6747 (1.0)        5.9072 (1.0)        5.7474 (1.0)      0.0701 (1.0)        5.7302 (1.0)      0.0773 (1.0)           2;1  173.9902 (1.0)          10           1
test_incremental_edit[isort-ty]           20.1878 (3.56)      21.3272 (3.61)      20.9220 (3.64)     0.3366 (4.81)      21.0118 (3.67)     0.4201 (5.43)          2;0   47.7966 (0.27)         10           1
test_incremental_edit[isort-pyrefly]      42.7818 (7.54)      57.5799 (9.75)      52.8906 (9.20)     4.5220 (64.55)     54.9351 (9.59)     5.5654 (71.97)         2;0   18.9070 (0.11)         10           1
test_incremental_edit[isort-pyright]     419.7210 (73.96)    429.1457 (72.65)    425.1017 (73.96)    2.9371 (41.93)    424.9466 (74.16)    4.3485 (56.23)         3;0    2.3524 (0.01)         10           1
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

----------------------------------------------------------------------------------------- benchmark 'jinja': 4 tests -----------------------------------------------------------------------------------------
Name (time in ms)                             Min                 Max                Mean             StdDev              Median                IQR            Outliers      OPS            Rounds  Iterations
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_incremental_edit[jinja-ty]           11.7900 (1.0)       13.7590 (1.0)       12.3526 (1.0)       0.5212 (3.89)      12.2479 (1.0)       0.1973 (1.09)          2;2  80.9545 (1.0)          10           1
test_incremental_edit[jinja-zuban]        19.9754 (1.69)      20.4125 (1.48)      20.1366 (1.63)      0.1340 (1.0)       20.1239 (1.64)      0.1803 (1.0)           3;0  49.6609 (0.61)         10           1
test_incremental_edit[jinja-pyrefly]      53.2751 (4.52)      67.2008 (4.88)      60.3027 (4.88)      4.5815 (34.19)     59.1167 (4.83)      5.8406 (32.40)         4;0  16.5830 (0.20)         10           1
test_incremental_edit[jinja-pyright]     476.3300 (40.40)    530.7210 (38.57)    503.8855 (40.79)    14.1706 (105.75)   505.3668 (41.26)    11.4062 (63.28)         2;2   1.9846 (0.02)         10           1
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

---------------------------------------------------------------------------------------- benchmark 'pandas': 4 tests -----------------------------------------------------------------------------------------
Name (time in ms)                              Min                 Max                Mean             StdDev              Median               IQR            Outliers      OPS            Rounds  Iterations
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_incremental_edit[pandas-ty]           48.2998 (1.0)       51.3248 (1.0)       49.8587 (1.0)       1.1924 (1.0)       50.1217 (1.0)      2.3663 (1.14)          5;0  20.0567 (1.0)          10           1
test_incremental_edit[pandas-pyrefly]     243.4753 (5.04)     256.9783 (5.01)     248.6074 (4.99)      4.2473 (3.56)     247.6178 (4.94)     6.6526 (3.21)          2;0   4.0224 (0.20)         10           1
test_incremental_edit[pandas-zuban]       251.8713 (5.21)     259.0576 (5.05)     254.0977 (5.10)      2.2326 (1.87)     253.3567 (5.05)     2.0706 (1.0)           2;1   3.9355 (0.20)         10           1
test_incremental_edit[pandas-pyright]     662.6549 (13.72)    701.7632 (13.67)    691.2085 (13.86)    11.6618 (9.78)     695.5558 (13.88)    8.8209 (4.26)          1;1   1.4467 (0.07)         10           1
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

------------------------------------------------------------------------------------------ benchmark 'prefect': 4 tests -----------------------------------------------------------------------------------------
Name (time in ms)                               Min                 Max                Mean             StdDev              Median                IQR            Outliers       OPS            Rounds  Iterations
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_incremental_edit[prefect-ty]            7.7652 (1.0)        8.3372 (1.0)        7.9939 (1.0)       0.1783 (1.0)        7.9367 (1.0)       0.2481 (1.0)           3;0  125.0950 (1.0)          10           1
test_incremental_edit[prefect-pyrefly]      51.3062 (6.61)      61.9334 (7.43)      56.2614 (7.04)      3.5354 (19.82)     57.8409 (7.29)      5.8660 (23.64)         4;0   17.7742 (0.14)         10           1
test_incremental_edit[prefect-zuban]       131.5461 (16.94)    132.8311 (15.93)    132.0289 (16.52)     0.4032 (2.26)     131.9307 (16.62)     0.4938 (1.99)          3;0    7.5741 (0.06)         10           1
test_incremental_edit[prefect-pyright]     660.4608 (85.05)    695.6145 (83.43)    680.8583 (85.17)    10.4803 (58.77)    682.6589 (86.01)    14.5401 (58.60)         3;0    1.4687 (0.01)         10           1
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

----------------------------------------------------------------------------------------- benchmark 'pytorch': 3 tests ----------------------------------------------------------------------------------------
Name (time in ms)                               Min                 Max                Mean            StdDev              Median               IQR            Outliers       OPS            Rounds  Iterations
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_incremental_edit[pytorch-ty]            3.7468 (1.0)        4.9578 (1.0)        4.0814 (1.0)      0.3563 (1.0)        3.9728 (1.0)      0.3189 (1.0)           1;1  245.0115 (1.0)          10           1
test_incremental_edit[pytorch-pyrefly]      20.1780 (5.39)      25.2127 (5.09)      22.7988 (5.59)     1.8837 (5.29)      23.4518 (5.90)     3.4646 (10.86)         4;0   43.8619 (0.18)         10           1
test_incremental_edit[pytorch-pyright]     411.6034 (109.85)   420.5795 (84.83)    416.2569 (101.99)   2.2362 (6.28)     416.0866 (104.73)   1.0938 (3.43)          2;2    2.4024 (0.01)         10           1
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

------------------------------------------------------------------------------------------ benchmark 'httpx': 4 tests -----------------------------------------------------------------------------------------
Name (time in ms)                             Min                 Max                Mean             StdDev              Median                IQR            Outliers       OPS            Rounds  Iterations
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_incremental_edit[httpx-ty]            7.9867 (1.0)        9.8584 (1.0)        8.5427 (1.0)       0.5679 (1.0)        8.4037 (1.0)       0.5983 (3.19)          1;1  117.0592 (1.0)          10           1
test_incremental_edit[httpx-zuban]         9.5517 (1.20)      11.7660 (1.19)       9.9430 (1.16)      0.6486 (1.14)       9.7386 (1.16)      0.1877 (1.0)           1;1  100.5729 (0.86)         10           1
test_incremental_edit[httpx-pyrefly]      47.6866 (5.97)      57.0288 (5.78)      51.7039 (6.05)      2.8466 (5.01)      52.0920 (6.20)      3.3798 (18.01)         3;0   19.3409 (0.17)         10           1
test_incremental_edit[httpx-pyright]     414.3220 (51.88)    441.5353 (44.79)    426.5495 (49.93)    10.4990 (18.49)    426.0099 (50.69)    20.2930 (108.11)        5;0    2.3444 (0.02)         10           1
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------------- benchmark 'numpy': 3 tests --------------------------------------------------------------------------------------------
Name (time in ms)                               Min                   Max                  Mean             StdDev                Median               IQR            Outliers      OPS            Rounds  Iterations
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_incremental_edit[numpy-ty]             19.4522 (1.0)         21.7454 (1.0)         20.0771 (1.0)       0.7126 (1.0)         19.8050 (1.0)      0.7391 (1.0)           1;1  49.8079 (1.0)          10           1
test_incremental_edit[numpy-pyrefly]       330.8268 (17.01)      350.2634 (16.11)      343.7851 (17.12)     6.4024 (8.99)       346.1157 (17.48)    7.2750 (9.84)          3;0   2.9088 (0.06)         10           1
test_incremental_edit[numpy-pyright]     1,171.7334 (60.24)    1,205.3624 (55.43)    1,188.2385 (59.18)    10.2539 (14.39)    1,189.4224 (60.06)    9.2393 (12.50)         3;0   0.8416 (0.02)         10           1
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

----------------------------------------------------------------------------------------- benchmark 'fastapi': 4 tests ----------------------------------------------------------------------------------------
Name (time in ms)                               Min                 Max                Mean            StdDev              Median               IQR            Outliers       OPS            Rounds  Iterations
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_incremental_edit[fastapi-ty]            7.3285 (1.0)        8.0183 (1.0)        7.6094 (1.0)      0.2079 (1.62)       7.6191 (1.0)      0.2937 (1.65)          2;0  131.4160 (1.0)          10           1
test_incremental_edit[fastapi-zuban]         8.3563 (1.14)       8.7793 (1.09)       8.5171 (1.12)     0.1283 (1.0)        8.4884 (1.11)     0.1784 (1.0)           2;0  117.4108 (0.89)         10           1
test_incremental_edit[fastapi-pyrefly]      58.2667 (7.95)      69.4830 (8.67)      65.8294 (8.65)     3.4123 (26.60)     67.0105 (8.80)     4.0596 (22.76)         2;0   15.1908 (0.12)         10           1
test_incremental_edit[fastapi-pyright]     604.3037 (82.46)    621.4753 (77.51)    614.2073 (80.72)    5.5771 (43.48)    614.2024 (80.61)    8.3417 (46.76)         3;0    1.6281 (0.01)         10           1
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

---------------------------------------------------------------------------------------- benchmark 'sqlalchemy': 4 tests ----------------------------------------------------------------------------------------
Name (time in ms)                                  Min                 Max                Mean            StdDev              Median               IQR            Outliers      OPS            Rounds  Iterations
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_incremental_edit[sqlalchemy-ty]           12.9194 (1.0)       16.9897 (1.0)       13.6793 (1.0)      1.2165 (1.24)      13.2267 (1.0)      0.6256 (1.0)           1;1  73.1032 (1.0)          10           1
test_incremental_edit[sqlalchemy-pyrefly]      56.7484 (4.39)      84.5526 (4.98)      76.4313 (5.59)     7.9762 (8.11)      76.2125 (5.76)     7.9097 (12.64)         2;1  13.0836 (0.18)         10           1
test_incremental_edit[sqlalchemy-zuban]       198.5378 (15.37)    201.8470 (11.88)    199.5849 (14.59)    0.9838 (1.0)      199.1490 (15.06)    1.1792 (1.88)          2;0   5.0104 (0.07)         10           1
test_incremental_edit[sqlalchemy-pyright]     632.0858 (48.93)    647.3986 (38.11)    639.0595 (46.72)    5.6518 (5.74)     640.6409 (48.44)    9.4287 (15.07)         5;0   1.5648 (0.02)         10           1
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

----------------------------------------------------------------------------------------- benchmark 'rich': 4 tests -----------------------------------------------------------------------------------------
Name (time in ms)                            Min                 Max                Mean            StdDev              Median                IQR            Outliers       OPS            Rounds  Iterations
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_incremental_edit[rich-ty]            5.5556 (1.0)        6.3839 (1.0)        5.8543 (1.0)      0.2377 (1.0)        5.8605 (1.0)       0.2525 (1.03)          3;1  170.8132 (1.0)          10           1
test_incremental_edit[rich-zuban]        12.7459 (2.29)      14.8288 (2.32)      13.1219 (2.24)     0.6140 (2.58)      12.9070 (2.20)      0.2442 (1.0)           1;1   76.2082 (0.45)         10           1
test_incremental_edit[rich-pyrefly]      20.0278 (3.60)      41.4377 (6.49)      31.1428 (5.32)     7.2154 (30.35)     34.0170 (5.80)     12.2488 (50.16)         4;0   32.1102 (0.19)         10           1
test_incremental_edit[rich-pyright]     433.5527 (78.04)    446.9955 (70.02)    440.7714 (75.29)    4.4355 (18.66)    442.3849 (75.49)     6.2345 (25.53)         3;0    2.2687 (0.01)         10           1
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

----------------------------------------------------------------------------------------- benchmark 'django': 4 tests ------------------------------------------------------------------------------------------
Name (time in ms)                              Min                 Max                Mean             StdDev              Median                IQR            Outliers       OPS            Rounds  Iterations
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_incremental_edit[django-zuban]         1.7699 (1.0)        1.9427 (1.0)        1.8348 (1.0)       0.0613 (1.0)        1.8271 (1.0)       0.1039 (1.29)          4;0  545.0284 (1.0)          10           1
test_incremental_edit[django-ty]            3.7757 (2.13)       3.9780 (2.05)       3.8547 (2.10)      0.0659 (1.07)       3.8349 (2.10)      0.0808 (1.0)           3;0  259.4238 (0.48)         10           1
test_incremental_edit[django-pyrefly]      21.2110 (11.98)     29.9794 (15.43)     25.4880 (13.89)     3.1539 (51.45)     26.3823 (14.44)     5.5899 (69.19)         4;0   39.2342 (0.07)         10           1
test_incremental_edit[django-pyright]     330.7418 (186.87)   381.0605 (196.15)   354.0818 (192.98)   21.3677 (348.54)   341.3754 (186.84)   39.9063 (493.94)        5;0    2.8242 (0.01)         10           1
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

----------------------------------------------------------------------------------------- benchmark 'sympy': 4 tests -----------------------------------------------------------------------------------------
Name (time in ms)                             Min                 Max                Mean            StdDev              Median                IQR            Outliers       OPS            Rounds  Iterations
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_incremental_edit[sympy-ty]            3.4788 (1.0)        3.8779 (1.0)        3.6264 (1.0)      0.1231 (1.0)        3.6030 (1.0)       0.1003 (1.0)           3;2  275.7550 (1.0)          10           1
test_incremental_edit[sympy-pyrefly]      28.2025 (8.11)      38.2077 (9.85)      33.0703 (9.12)     3.0461 (24.74)     32.1000 (8.91)      4.1055 (40.92)         3;0   30.2386 (0.11)         10           1
test_incremental_edit[sympy-zuban]        62.8081 (18.05)     67.0972 (17.30)     63.7676 (17.58)    1.3140 (10.67)     63.3715 (17.59)     0.7175 (7.15)          1;2   15.6819 (0.06)         10           1
test_incremental_edit[sympy-pyright]     465.8610 (133.91)   487.8697 (125.81)   479.7846 (132.30)   7.3209 (59.46)    478.8293 (132.90)   10.6199 (105.85)        3;0    2.0843 (0.01)         10           1
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

---------------------------------------------------------------------------------------- benchmark 'openai': 4 tests -----------------------------------------------------------------------------------------
Name (time in ms)                              Min                 Max                Mean            StdDev              Median               IQR            Outliers       OPS            Rounds  Iterations
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_incremental_edit[openai-zuban]         3.4460 (1.0)        3.6128 (1.0)        3.5186 (1.0)      0.0547 (1.0)        3.5069 (1.0)      0.0987 (1.0)           4;0  284.2066 (1.0)          10           1
test_incremental_edit[openai-ty]            4.2651 (1.24)       4.7099 (1.30)       4.4452 (1.26)     0.1547 (2.83)       4.4445 (1.27)     0.2586 (2.62)          3;0  224.9632 (0.79)         10           1
test_incremental_edit[openai-pyrefly]      70.9413 (20.59)     87.7718 (24.30)     82.7103 (23.51)    5.0859 (93.06)     83.1189 (23.70)    5.0480 (51.16)         1;1   12.0904 (0.04)         10           1
test_incremental_edit[openai-pyright]     457.0089 (132.62)   489.3018 (135.44)   478.7871 (136.07)   8.6623 (158.50)   481.2125 (137.22)   7.4462 (75.47)         2;1    2.0886 (0.01)         10           1
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

---------------------------------------------------------------------------------------- benchmark 'pytest': 4 tests -----------------------------------------------------------------------------------------
Name (time in ms)                              Min                 Max                Mean            StdDev              Median               IQR            Outliers       OPS            Rounds  Iterations
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_incremental_edit[pytest-ty]            8.8387 (1.0)       10.1693 (1.0)        9.2703 (1.0)      0.4956 (2.82)       9.0366 (1.0)      0.4686 (2.33)          2;2  107.8716 (1.0)          10           1
test_incremental_edit[pytest-zuban]        26.0735 (2.95)      26.7175 (2.63)      26.3351 (2.84)     0.1758 (1.0)       26.3459 (2.92)     0.2007 (1.0)           2;1   37.9721 (0.35)         10           1
test_incremental_edit[pytest-pyrefly]      55.3168 (6.26)      62.2285 (6.12)      58.5314 (6.31)     2.2135 (12.59)     58.4364 (6.47)     2.6986 (13.45)         3;0   17.0848 (0.16)         10           1
test_incremental_edit[pytest-pyright]     458.6860 (51.90)    490.4299 (48.23)    481.3327 (51.92)    8.7184 (49.58)    483.3412 (53.49)    6.7729 (33.74)         2;1    2.0776 (0.02)         10           1
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
```

### Fetch diagnostics

```shell
----------------------------------------------------------------------------------------- benchmark 'black': 4 tests ----------------------------------------------------------------------------------------
Name (time in ms)                              Min                 Max                Mean            StdDev              Median               IQR            Outliers      OPS            Rounds  Iterations
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_fetch_diagnostics[black-ty]           61.3446 (1.0)       64.2571 (1.0)       62.0019 (1.0)      0.9246 (2.25)      61.5498 (1.0)      1.1715 (1.86)          1;0  16.1285 (1.0)          10           1
test_fetch_diagnostics[black-zuban]        68.9572 (1.12)      73.7763 (1.15)      71.2262 (1.15)     1.4690 (3.57)      71.0236 (1.15)     2.1367 (3.40)          2;0  14.0398 (0.87)         10           1
test_fetch_diagnostics[black-pyrefly]     179.8352 (2.93)     181.0037 (2.82)     180.5095 (2.91)     0.4111 (1.0)      180.5079 (2.93)     0.6513 (1.03)          4;0   5.5399 (0.34)         10           1
test_fetch_diagnostics[black-pyright]     299.9607 (4.89)     302.2230 (4.70)     300.9091 (4.85)     0.6684 (1.63)     300.8832 (4.89)     0.6293 (1.0)           3;0   3.3233 (0.21)         10           1
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

----------------------------------------------------------------------------------------- benchmark 'discord.py': 4 tests ------------------------------------------------------------------------------------------
Name (time in ms)                                   Min                 Max                Mean             StdDev              Median                IQR            Outliers      OPS            Rounds  Iterations
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_fetch_diagnostics[discord.py-ty]           91.9899 (1.0)       96.7191 (1.0)       93.3359 (1.0)       1.2987 (5.15)      92.9172 (1.0)       0.9487 (4.89)          2;1  10.7140 (1.0)          10           1
test_fetch_diagnostics[discord.py-zuban]       177.4120 (1.93)     184.2058 (1.90)     180.0302 (1.93)      2.0807 (8.26)     179.8533 (1.94)      1.9461 (10.03)         3;1   5.5546 (0.52)         10           1
test_fetch_diagnostics[discord.py-pyrefly]     187.9900 (2.04)     188.8244 (1.95)     188.3708 (2.02)      0.2520 (1.0)      188.3499 (2.03)      0.1941 (1.0)           4;2   5.3087 (0.50)         10           1
test_fetch_diagnostics[discord.py-pyright]     621.1201 (6.75)     663.5259 (6.86)     630.2578 (6.75)     12.6775 (50.30)    626.5515 (6.74)     11.5769 (59.64)         1;1   1.5867 (0.15)         10           1
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

---------------------------------------------------------------------------------------------- benchmark 'homeassistant': 4 tests ---------------------------------------------------------------------------------------------
Name (time in ms)                                        Min                   Max                  Mean             StdDev                Median                IQR            Outliers      OPS            Rounds  Iterations
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_fetch_diagnostics[homeassistant-ty]             94.3651 (1.0)        113.4692 (1.0)         99.2496 (1.0)       5.3273 (5.09)        97.8442 (1.0)       2.9808 (2.89)          1;1  10.0756 (1.0)          10           1
test_fetch_diagnostics[homeassistant-zuban]         214.2382 (2.27)       219.2897 (1.93)       217.0925 (2.19)      1.7237 (1.65)       217.0206 (2.22)      2.0827 (2.02)          4;0   4.6063 (0.46)         10           1
test_fetch_diagnostics[homeassistant-pyrefly]       236.2060 (2.50)       239.4906 (2.11)       237.6687 (2.39)      1.0456 (1.0)        237.4407 (2.43)      1.0302 (1.0)           3;0   4.2075 (0.42)         10           1
test_fetch_diagnostics[homeassistant-pyright]     1,890.3885 (20.03)    1,924.0052 (16.96)    1,905.1369 (19.20)    10.7615 (10.29)    1,903.1950 (19.45)    14.3797 (13.96)         4;0   0.5249 (0.05)         10           1
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

----------------------------------------------------------------------------------------- benchmark 'isort': 4 tests -----------------------------------------------------------------------------------------
Name (time in ms)                              Min                 Max                Mean            StdDev              Median                IQR            Outliers      OPS            Rounds  Iterations
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_fetch_diagnostics[isort-zuban]        39.6183 (1.0)       44.7363 (1.0)       41.2833 (1.0)      1.4294 (1.14)      40.9556 (1.0)       1.3667 (1.0)           2;1  24.2229 (1.0)          10           1
test_fetch_diagnostics[isort-ty]           49.0504 (1.24)      52.8668 (1.18)      50.6651 (1.23)     1.2549 (1.0)       50.9217 (1.24)      2.2342 (1.63)          4;0  19.7375 (0.81)         10           1
test_fetch_diagnostics[isort-pyrefly]     126.7168 (3.20)     140.7936 (3.15)     134.1324 (3.25)     5.9800 (4.77)     134.6929 (3.29)     11.4701 (8.39)          4;0   7.4553 (0.31)         10           1
test_fetch_diagnostics[isort-pyright]     355.6153 (8.98)     360.0408 (8.05)     358.0638 (8.67)     1.4327 (1.14)     358.1251 (8.74)      2.5620 (1.87)          4;0   2.7928 (0.12)         10           1
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

----------------------------------------------------------------------------------------- benchmark 'jinja': 4 tests ----------------------------------------------------------------------------------------
Name (time in ms)                              Min                 Max                Mean            StdDev              Median               IQR            Outliers      OPS            Rounds  Iterations
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_fetch_diagnostics[jinja-ty]           49.2497 (1.0)       53.0704 (1.0)       50.4838 (1.0)      1.3901 (3.72)      49.9364 (1.0)      2.3340 (3.52)          2;0  19.8083 (1.0)          10           1
test_fetch_diagnostics[jinja-zuban]        85.7727 (1.74)      88.3310 (1.66)      86.9519 (1.72)     0.7278 (1.95)      87.0239 (1.74)     0.7648 (1.15)          2;0  11.5006 (0.58)         10           1
test_fetch_diagnostics[jinja-pyrefly]     125.6743 (2.55)     126.7780 (2.39)     126.3703 (2.50)     0.3741 (1.0)      126.4106 (2.53)     0.6636 (1.0)           4;0   7.9133 (0.40)         10           1
test_fetch_diagnostics[jinja-pyright]     353.2582 (7.17)     361.2105 (6.81)     356.3589 (7.06)     2.3240 (6.21)     355.8286 (7.13)     3.4593 (5.21)          2;0   2.8062 (0.14)         10           1
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

---------------------------------------------------------------------------------------- benchmark 'pandas': 4 tests -----------------------------------------------------------------------------------------
Name (time in ms)                               Min                 Max                Mean            StdDev              Median                IQR            Outliers     OPS            Rounds  Iterations
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_fetch_diagnostics[pandas-ty]          351.8684 (1.0)      365.9209 (1.0)      356.7117 (1.0)      5.5499 (1.23)     354.0003 (1.0)      10.3039 (4.19)          3;0  2.8034 (1.0)          10           1
test_fetch_diagnostics[pandas-pyrefly]     539.1561 (1.53)     562.5021 (1.54)     543.9112 (1.52)     6.9893 (1.55)     541.4131 (1.53)      2.4565 (1.0)           1;2  1.8385 (0.66)         10           1
test_fetch_diagnostics[pandas-pyright]     629.9906 (1.79)     647.6225 (1.77)     639.1170 (1.79)     5.6742 (1.26)     640.4880 (1.81)      9.5839 (3.90)          4;0  1.5647 (0.56)         10           1
test_fetch_diagnostics[pandas-zuban]       666.4379 (1.89)     680.6972 (1.86)     673.7827 (1.89)     4.4995 (1.0)      673.4846 (1.90)      6.0168 (2.45)          3;0  1.4842 (0.53)         10           1
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------------- benchmark 'prefect': 4 tests ---------------------------------------------------------------------------------------------
Name (time in ms)                                  Min                   Max                  Mean             StdDev                Median                IQR            Outliers     OPS            Rounds  Iterations
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_fetch_diagnostics[prefect-ty]            157.0433 (1.0)        159.3191 (1.0)        157.9034 (1.0)       0.6149 (1.0)        157.8847 (1.0)       0.6349 (1.0)           2;1  6.3330 (1.0)          10           1
test_fetch_diagnostics[prefect-pyrefly]       332.9010 (2.12)       467.9147 (2.94)       452.5213 (2.87)     42.0522 (68.39)      465.0061 (2.95)      2.8783 (4.53)          1;1  2.2098 (0.35)         10           1
test_fetch_diagnostics[prefect-zuban]         859.7134 (5.47)       865.6050 (5.43)       863.4421 (5.47)      2.2602 (3.68)       864.5682 (5.48)      3.9808 (6.27)          3;0  1.1582 (0.18)         10           1
test_fetch_diagnostics[prefect-pyright]     1,102.1569 (7.02)     1,130.7971 (7.10)     1,113.3106 (7.05)     10.0063 (16.27)    1,112.3842 (7.05)     16.5983 (26.14)         5;0  0.8982 (0.14)         10           1
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

---------------------------------------------------------------------------------------------- benchmark 'pytorch': 4 tests ---------------------------------------------------------------------------------------------
Name (time in ms)                                  Min                   Max                  Mean             StdDev                Median                IQR            Outliers      OPS            Rounds  Iterations
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_fetch_diagnostics[pytorch-ty]             67.1467 (1.0)         69.4841 (1.0)         68.2710 (1.0)       0.8116 (1.0)         68.3885 (1.0)       1.6100 (1.0)           5;0  14.6475 (1.0)          10           1
test_fetch_diagnostics[pytorch-pyrefly]       116.7863 (1.74)       145.4521 (2.09)       128.6864 (1.88)     14.0053 (17.26)      118.9156 (1.74)     27.4318 (17.04)         4;0   7.7708 (0.53)         10           1
test_fetch_diagnostics[pytorch-pyright]       702.6213 (10.46)      709.5476 (10.21)      705.4807 (10.33)     2.5295 (3.12)       704.5238 (10.30)     4.3440 (2.70)          3;0   1.4175 (0.10)         10           1
test_fetch_diagnostics[pytorch-zuban]       1,825.0715 (27.18)    1,860.6000 (26.78)    1,835.6793 (26.89)     9.9072 (12.21)    1,835.3201 (26.84)     8.8780 (5.51)          2;1   0.5448 (0.04)         10           1
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

----------------------------------------------------------------------------------------- benchmark 'httpx': 4 tests ----------------------------------------------------------------------------------------
Name (time in ms)                              Min                 Max                Mean            StdDev              Median               IQR            Outliers      OPS            Rounds  Iterations
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_fetch_diagnostics[httpx-ty]           43.9061 (1.0)       44.6345 (1.0)       44.2958 (1.0)      0.2083 (1.0)       44.3242 (1.0)      0.2969 (1.0)           2;0  22.5755 (1.0)          10           1
test_fetch_diagnostics[httpx-zuban]        69.2425 (1.58)      71.2874 (1.60)      70.2522 (1.59)     0.6870 (3.30)      70.2971 (1.59)     0.9758 (3.29)          3;0  14.2344 (0.63)         10           1
test_fetch_diagnostics[httpx-pyrefly]     114.3010 (2.60)     118.0325 (2.64)     115.3196 (2.60)     1.1948 (5.74)     114.8530 (2.59)     1.1663 (3.93)          2;1   8.6716 (0.38)         10           1
test_fetch_diagnostics[httpx-pyright]     224.9341 (5.12)     228.4704 (5.12)     226.4147 (5.11)     1.0548 (5.06)     226.3045 (5.11)     1.0174 (3.43)          3;1   4.4167 (0.20)         10           1
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

------------------------------------------------------------------------------------------------ benchmark 'numpy': 4 tests -----------------------------------------------------------------------------------------------
Name (time in ms)                                 Min                    Max                   Mean             StdDev                 Median                 IQR            Outliers     OPS            Rounds  Iterations
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_fetch_diagnostics[numpy-ty]             176.7615 (1.0)         186.8349 (1.0)         180.0022 (1.0)       3.6389 (2.53)        178.5085 (1.0)        1.1902 (1.28)          2;2  5.5555 (1.0)          10           1
test_fetch_diagnostics[numpy-pyrefly]        562.9346 (3.18)        568.0607 (3.04)        564.3641 (3.14)      1.4365 (1.0)         564.1055 (3.16)       0.9281 (1.0)           1;1  1.7719 (0.32)         10           1
test_fetch_diagnostics[numpy-pyright]      1,182.4547 (6.69)      1,212.2849 (6.49)      1,199.6223 (6.66)      9.0291 (6.29)      1,198.6239 (6.71)      12.4973 (13.47)         3;0  0.8336 (0.15)         10           1
test_fetch_diagnostics[numpy-zuban]       36,078.9349 (204.11)   36,423.6785 (194.95)   36,193.5729 (201.07)   98.8916 (68.84)    36,198.7695 (202.78)   119.7505 (129.02)        2;1  0.0276 (0.00)         10           1
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

----------------------------------------------------------------------------------------- benchmark 'fastapi': 4 tests ----------------------------------------------------------------------------------------
Name (time in ms)                                Min                 Max                Mean            StdDev              Median               IQR            Outliers      OPS            Rounds  Iterations
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_fetch_diagnostics[fastapi-ty]           95.9351 (1.0)       99.0770 (1.0)       98.0754 (1.0)      1.1617 (1.99)      98.5677 (1.0)      1.5366 (2.52)          2;0  10.1962 (1.0)          10           1
test_fetch_diagnostics[fastapi-zuban]       171.4969 (1.79)     177.0828 (1.79)     173.4509 (1.77)     1.8097 (3.10)     173.0481 (1.76)     2.5310 (4.14)          3;0   5.7653 (0.57)         10           1
test_fetch_diagnostics[fastapi-pyrefly]     199.6927 (2.08)     201.7180 (2.04)     200.3882 (2.04)     0.5838 (1.0)      200.3402 (2.03)     0.6110 (1.0)           2;1   4.9903 (0.49)         10           1
test_fetch_diagnostics[fastapi-pyright]     457.2369 (4.77)     470.3823 (4.75)     465.9305 (4.75)     3.9981 (6.85)     466.0065 (4.73)     4.5289 (7.41)          3;1   2.1462 (0.21)         10           1
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

---------------------------------------------------------------------------------------- benchmark 'sqlalchemy': 4 tests ----------------------------------------------------------------------------------------
Name (time in ms)                                   Min                 Max                Mean            StdDev              Median               IQR            Outliers     OPS            Rounds  Iterations
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_fetch_diagnostics[sqlalchemy-ty]          207.4063 (1.0)      231.8568 (1.0)      213.2610 (1.0)      7.5025 (4.69)     211.4731 (1.0)      5.5045 (3.51)          1;1  4.6891 (1.0)          10           1
test_fetch_diagnostics[sqlalchemy-pyrefly]     250.0255 (1.21)     256.0001 (1.10)     251.9413 (1.18)     1.6665 (1.04)     251.7372 (1.19)     1.6916 (1.08)          2;1  3.9692 (0.85)         10           1
test_fetch_diagnostics[sqlalchemy-pyright]     270.1789 (1.30)     276.0185 (1.19)     272.7359 (1.28)     1.6008 (1.0)      272.7561 (1.29)     1.5684 (1.0)           2;1  3.6666 (0.78)         10           1
test_fetch_diagnostics[sqlalchemy-zuban]       383.2057 (1.85)     399.6241 (1.72)     386.9370 (1.81)     4.6166 (2.88)     385.5155 (1.82)     2.3762 (1.52)          1;1  2.5844 (0.55)         10           1
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

---------------------------------------------------------------------------------------- benchmark 'rich': 4 tests -----------------------------------------------------------------------------------------
Name (time in ms)                             Min                 Max                Mean            StdDev              Median               IQR            Outliers      OPS            Rounds  Iterations
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_fetch_diagnostics[rich-ty]           39.1258 (1.0)       40.5336 (1.0)       39.8489 (1.0)      0.4538 (1.0)       39.8839 (1.0)      0.7542 (1.41)          3;0  25.0948 (1.0)          10           1
test_fetch_diagnostics[rich-zuban]        79.5685 (2.03)      82.3503 (2.03)      80.7725 (2.03)     0.8009 (1.76)      80.6681 (2.02)     0.5338 (1.0)           3;2  12.3804 (0.49)         10           1
test_fetch_diagnostics[rich-pyrefly]      99.5237 (2.54)     115.1077 (2.84)     110.9954 (2.79)     5.6315 (12.41)    113.2185 (2.84)     1.7742 (3.32)          2;2   9.0094 (0.36)         10           1
test_fetch_diagnostics[rich-pyright]     309.8927 (7.92)     314.1458 (7.75)     311.3170 (7.81)     1.3331 (2.94)     310.9984 (7.80)     1.9001 (3.56)          3;0   3.2122 (0.13)         10           1
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

---------------------------------------------------------------------------------------- benchmark 'django': 4 tests -----------------------------------------------------------------------------------------
Name (time in ms)                               Min                 Max                Mean            StdDev              Median               IQR            Outliers      OPS            Rounds  Iterations
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_fetch_diagnostics[django-ty]           23.5612 (1.0)       24.2165 (1.0)       23.8021 (1.0)      0.2324 (1.0)       23.7625 (1.0)      0.3301 (1.0)           4;0  42.0131 (1.0)          10           1
test_fetch_diagnostics[django-zuban]        45.0162 (1.91)      47.3812 (1.96)      46.3298 (1.95)     0.7499 (3.23)      46.4050 (1.95)     0.7135 (2.16)          4;1  21.5844 (0.51)         10           1
test_fetch_diagnostics[django-pyrefly]      90.8160 (3.85)      96.1161 (3.97)      94.1640 (3.96)     2.2035 (9.48)      95.3465 (4.01)     4.3802 (13.27)         3;0  10.6198 (0.25)         10           1
test_fetch_diagnostics[django-pyright]     587.8771 (24.95)    610.7550 (25.22)    593.6576 (24.94)    8.6595 (37.26)    589.8123 (24.82)    2.7981 (8.48)          2;2   1.6845 (0.04)         10           1
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

----------------------------------------------------------------------------------------- benchmark 'sympy': 4 tests ----------------------------------------------------------------------------------------
Name (time in ms)                              Min                 Max                Mean            StdDev              Median               IQR            Outliers      OPS            Rounds  Iterations
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_fetch_diagnostics[sympy-ty]           71.8480 (1.0)       73.1758 (1.0)       72.2481 (1.0)      0.3895 (1.0)       72.1690 (1.0)      0.4300 (1.0)           2;1  13.8412 (1.0)          10           1
test_fetch_diagnostics[sympy-pyrefly]     179.4386 (2.50)     183.1834 (2.50)     180.5083 (2.50)     1.0781 (2.77)     180.2387 (2.50)     0.5938 (1.38)          1;1   5.5399 (0.40)         10           1
test_fetch_diagnostics[sympy-zuban]       260.1722 (3.62)     274.6859 (3.75)     265.9684 (3.68)     4.4955 (11.54)    264.4641 (3.66)     7.1645 (16.66)         2;0   3.7598 (0.27)         10           1
test_fetch_diagnostics[sympy-pyright]     392.3544 (5.46)     400.7913 (5.48)     396.7093 (5.49)     2.7972 (7.18)     396.7134 (5.50)     5.3469 (12.43)         4;0   2.5207 (0.18)         10           1
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

---------------------------------------------------------------------------------------- benchmark 'openai': 4 tests -----------------------------------------------------------------------------------------
Name (time in ms)                               Min                 Max                Mean            StdDev              Median               IQR            Outliers      OPS            Rounds  Iterations
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_fetch_diagnostics[openai-ty]           66.3099 (1.0)       70.3884 (1.0)       67.1152 (1.0)      1.2358 (1.0)       66.6806 (1.0)      1.0648 (1.0)           1;1  14.8998 (1.0)          10           1
test_fetch_diagnostics[openai-zuban]       139.0193 (2.10)     143.9898 (2.05)     141.1401 (2.10)     1.4470 (1.17)     140.7476 (2.11)     1.9043 (1.79)          2;0   7.0852 (0.48)         10           1
test_fetch_diagnostics[openai-pyrefly]     188.4392 (2.84)     202.4323 (2.88)     199.4188 (2.97)     5.1057 (4.13)     201.7685 (3.03)     1.2412 (1.17)          2;2   5.0146 (0.34)         10           1
test_fetch_diagnostics[openai-pyright]     513.3347 (7.74)     518.7722 (7.37)     515.7981 (7.69)     2.2311 (1.81)     515.5012 (7.73)     4.6511 (4.37)          5;0   1.9387 (0.13)         10           1
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

---------------------------------------------------------------------------------------- benchmark 'pytest': 4 tests -----------------------------------------------------------------------------------------
Name (time in ms)                               Min                 Max                Mean            StdDev              Median               IQR            Outliers      OPS            Rounds  Iterations
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_fetch_diagnostics[pytest-ty]           75.5960 (1.0)       79.3887 (1.0)       76.5090 (1.0)      1.0781 (1.37)      76.1527 (1.0)      0.6201 (1.0)           1;1  13.0704 (1.0)          10           1
test_fetch_diagnostics[pytest-zuban]       132.7784 (1.76)     135.7364 (1.71)     134.2270 (1.75)     1.0887 (1.38)     134.4337 (1.77)     1.9573 (3.16)          5;0   7.4501 (0.57)         10           1
test_fetch_diagnostics[pytest-pyrefly]     183.1395 (2.42)     186.5047 (2.35)     185.1065 (2.42)     1.0400 (1.32)     185.1994 (2.43)     1.2209 (1.97)          4;0   5.4023 (0.41)         10           1
test_fetch_diagnostics[pytest-pyright]     289.3343 (3.83)     291.7467 (3.67)     290.7208 (3.80)     0.7864 (1.0)      290.6446 (3.82)     1.2309 (1.99)          3;0   3.4397 (0.26)         10           1
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
```
