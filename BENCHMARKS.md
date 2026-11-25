# Benchmarks

All benchmarks were computed on macOS (Apple M3 Max 16, 128 GB) with the following tool versions:

- [Pyrefly](https://pypi.org/project/pyrefly/) 1.4.0
- [Pyright](https://www.npmjs.com/package/pyright) 1.1.414
- [mypy](https://pypi.org/project/mypy/) 2.4.0
- [ty](https://pypi.org/project/ty/) 0.0.110
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
  Time (mean ± σ):      56.2 ms ±   1.9 ms    [User: 397.5 ms, System: 27.8 ms]
  Range (min … max):    52.4 ms …  60.6 ms    38 runs
  Memory (peak RSS):  130.8 MiB

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
    2.26 ± 0.08 times faster than Pyrefly
    2.56 ± 0.10 times faster than Zuban
   16.38 ± 0.58 times faster than mypy
   29.59 ± 1.05 times faster than Pyright

-------------------------------------------------------------------------------

discord.py
----------

Benchmark 1: ty
  Time (mean ± σ):     111.3 ms ±   5.3 ms    [User: 1051.5 ms, System: 62.0 ms]
  Range (min … max):   103.4 ms … 122.7 ms    22 runs
  Memory (peak RSS):  214.6 MiB

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
    1.56 ± 0.08 times faster than Pyrefly
    3.20 ± 0.16 times faster than Zuban
   18.75 ± 0.90 times faster than mypy
   35.83 ± 1.70 times faster than Pyright

-------------------------------------------------------------------------------

homeassistant
-------------

Benchmark 1: ty
  Time (mean ± σ):      1.872 s ±  0.019 s    [User: 23.476 s, System: 3.538 s]
  Range (min … max):    1.848 s …  1.905 s    10 runs
  Memory (peak RSS):  3,448 MiB

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
    1.23 ± 0.02 times faster than Pyrefly
    3.98 ± 0.05 times faster than Zuban
   27.80 ± 0.37 times faster than mypy
   67.82 ± 3.90 times faster than Pyright

-------------------------------------------------------------------------------

isort
-----

Benchmark 1: ty
  Time (mean ± σ):      57.9 ms ±   1.8 ms    [User: 183.7 ms, System: 15.4 ms]
  Range (min … max):    55.4 ms …  63.2 ms    37 runs
  Memory (peak RSS):   86.0 MiB

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
    1.14 ± 0.04 times faster than Zuban
    1.82 ± 0.07 times faster than Pyrefly
    7.85 ± 0.25 times faster than mypy
   28.14 ± 0.90 times faster than Pyright

-------------------------------------------------------------------------------

jinja
-----

Benchmark 1: ty
  Time (mean ± σ):      46.2 ms ±   1.0 ms    [User: 230.3 ms, System: 16.6 ms]
  Range (min … max):    43.8 ms …  48.7 ms    42 runs
  Memory (peak RSS):   95.8 MiB

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
    1.82 ± 0.05 times faster than Zuban
    2.25 ± 0.06 times faster than Pyrefly
   11.88 ± 0.33 times faster than mypy
   25.49 ± 0.59 times faster than Pyright

-------------------------------------------------------------------------------

pandas
------

Benchmark 1: ty
  Time (mean ± σ):     336.8 ms ±  26.8 ms    [User: 3765.0 ms, System: 204.8 ms]
  Range (min … max):   304.6 ms … 391.3 ms    10 runs
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
    2.64 ± 0.23 times faster than Pyrefly
    4.18 ± 0.33 times faster than Zuban
   31.09 ± 2.48 times faster than mypy
   46.89 ± 3.74 times faster than Pyright

-------------------------------------------------------------------------------

pandas-stubs
------------

Benchmark 1: ty
  Time (mean ± σ):      68.5 ms ±   4.1 ms    [User: 329.3 ms, System: 41.3 ms]
  Range (min … max):    58.6 ms …  74.6 ms    36 runs
  Memory (peak RSS):  154.0 MiB

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
    2.86 ± 0.17 times faster than Pyrefly
    3.96 ± 0.24 times faster than Zuban
   31.69 ± 1.90 times faster than Pyright
   69.56 ± 4.20 times faster than mypy

-------------------------------------------------------------------------------

prefect
-------

Benchmark 1: ty
  Time (mean ± σ):      98.7 ms ±   4.2 ms    [User: 597.3 ms, System: 46.0 ms]
  Range (min … max):    93.3 ms … 110.8 ms    24 runs
  Memory (peak RSS):  223.4 MiB

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
    2.75 ± 0.15 times faster than Pyrefly
    9.60 ± 0.41 times faster than Zuban
   28.60 ± 1.22 times faster than Pyright
   72.83 ± 3.21 times faster than mypy

-------------------------------------------------------------------------------

pytorch
-------

Benchmark 1: ty
  Time (mean ± σ):      1.125 s ±  0.038 s    [User: 14.004 s, System: 1.052 s]
  Range (min … max):    1.077 s …  1.176 s    10 runs
  Memory (peak RSS):  1,578 MiB

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
    1.07 ± 0.04 times faster than Pyrefly
    3.08 ± 0.11 times faster than Zuban
   22.56 ± 0.77 times faster than mypy
   65.81 ± 2.61 times faster than Pyright

-------------------------------------------------------------------------------

httpx
-----

Benchmark 1: ty
  Time (mean ± σ):      56.3 ms ±   1.5 ms    [User: 191.4 ms, System: 18.0 ms]
  Range (min … max):    53.8 ms …  59.2 ms    38 runs
  Memory (peak RSS):   99.3 MiB

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
    1.86 ± 0.06 times faster than Zuban
    2.09 ± 0.07 times faster than Pyrefly
   16.02 ± 0.46 times faster than mypy
   16.87 ± 0.50 times faster than Pyright

-------------------------------------------------------------------------------

numpy
-----

Benchmark 1: ty
  Time (mean ± σ):     168.4 ms ±   8.6 ms    [User: 951.4 ms, System: 69.9 ms]
  Range (min … max):   157.8 ms … 182.1 ms    15 runs
  Memory (peak RSS):  264.3 MiB

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
     3.45 ±  0.25 times faster than Pyrefly
   125.96 ±  6.43 times faster than Pyright
   480.41 ± 24.72 times faster than mypy

-------------------------------------------------------------------------------

fastapi
-------

Benchmark 1: ty
  Time (mean ± σ):      70.4 ms ±   2.7 ms    [User: 326.1 ms, System: 27.5 ms]
  Range (min … max):    66.1 ms …  76.4 ms    32 runs
  Memory (peak RSS):  139.7 MiB

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
    2.72 ± 0.11 times faster than Zuban
    4.22 ± 0.17 times faster than Pyrefly
   27.75 ± 1.10 times faster than mypy
   31.48 ± 1.23 times faster than Pyright

-------------------------------------------------------------------------------

sqlalchemy
----------

Benchmark 1: ty
  Time (mean ± σ):     247.3 ms ±  13.9 ms    [User: 2823.9 ms, System: 138.3 ms]
  Range (min … max):   229.6 ms … 283.4 ms    11 runs
  Memory (peak RSS):  392.4 MiB

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
    1.23 ± 0.07 times faster than Pyrefly
    2.67 ± 0.15 times faster than Zuban
   15.90 ± 0.90 times faster than mypy
   39.63 ± 2.24 times faster than Pyright

-------------------------------------------------------------------------------

rich
----

Benchmark 1: ty
  Time (mean ± σ):      55.8 ms ±   2.9 ms    [User: 351.4 ms, System: 29.7 ms]
  Range (min … max):    48.0 ms …  60.9 ms    38 runs
  Memory (peak RSS):  121.8 MiB

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
    2.20 ± 0.13 times faster than Pyrefly
    2.33 ± 0.13 times faster than Zuban
   21.66 ± 1.14 times faster than mypy
   44.99 ± 2.32 times faster than Pyright

-------------------------------------------------------------------------------

django
------

Benchmark 1: ty
  Time (mean ± σ):     213.4 ms ±   6.5 ms    [User: 2083.7 ms, System: 564.1 ms]
  Range (min … max):   202.4 ms … 227.0 ms    12 runs
  Memory (peak RSS):  308.0 MiB

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
    1.22 ± 0.04 times faster than Pyrefly
    2.39 ± 0.08 times faster than Zuban
   11.46 ± 0.36 times faster than mypy
   32.47 ± 1.01 times faster than Pyright

-------------------------------------------------------------------------------

sympy
-----

Benchmark 1: ty
  Time (mean ± σ):     629.0 ms ± 110.9 ms    [User: 6544.2 ms, System: 606.8 ms]
  Range (min … max):   527.7 ms … 822.2 ms    10 runs
  Memory (peak RSS):  703.6 MiB

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
    1.19 ± 0.21 times faster than ty
    2.33 ± 0.03 times faster than Zuban
   12.61 ± 0.15 times faster than mypy
   57.02 ± 0.72 times faster than Pyright

-------------------------------------------------------------------------------

openai
------

Benchmark 1: ty
  Time (mean ± σ):     237.0 ms ±  19.8 ms    [User: 1999.4 ms, System: 447.3 ms]
  Range (min … max):   217.1 ms … 287.4 ms    12 runs
  Memory (peak RSS):  329.9 MiB

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
    1.96 ± 0.17 times faster than Pyrefly
    3.63 ± 0.31 times faster than Zuban
   28.56 ± 2.39 times faster than mypy
   34.47 ± 2.89 times faster than Pyright

-------------------------------------------------------------------------------

pytest
------

Benchmark 1: ty
  Time (mean ± σ):     154.7 ms ±  13.9 ms    [User: 1203.9 ms, System: 80.3 ms]
  Range (min … max):   124.8 ms … 169.8 ms    16 runs
  Memory (peak RSS):  245.9 MiB

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
    1.47 ± 0.19 times faster than Pyrefly
    3.82 ± 0.34 times faster than Zuban
   15.39 ± 1.39 times faster than mypy
   29.56 ± 2.66 times faster than Pyright
```

## LSP

### Incremental edit

Zuban's server crashed on the incremental edits in discord.py, NumPy, and PyTorch.

```shell
---------------------------------------------------------------------------------------- benchmark 'black': 4 tests ----------------------------------------------------------------------------------------
Name (time in ms)                             Min                 Max                Mean            StdDev              Median               IQR            Outliers      OPS            Rounds  Iterations
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_incremental_edit[black-ty]           12.3932 (1.0)       12.8353 (1.0)       12.5927 (1.0)      0.1482 (1.0)       12.5999 (1.0)      0.2329 (1.0)           4;0  79.4109 (1.0)          10           1
test_incremental_edit[black-zuban]        18.8832 (1.52)      20.8855 (1.63)      19.3794 (1.54)     0.6267 (4.23)      19.2328 (1.53)     0.5062 (2.17)          2;1  51.6012 (0.65)         10           1
test_incremental_edit[black-pyrefly]      86.7763 (7.00)      97.2985 (7.58)      91.4009 (7.26)     3.0032 (20.27)     91.2891 (7.25)     4.0361 (17.33)         2;0  10.9408 (0.14)         10           1
test_incremental_edit[black-pyright]     540.2310 (43.59)    562.2411 (43.80)    549.4405 (43.63)    6.7233 (45.37)    548.0737 (43.50)    8.5098 (36.54)         4;0   1.8200 (0.02)         10           1
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

----------------------------------------------------------------------------------------- benchmark 'discord.py': 3 tests -----------------------------------------------------------------------------------------
Name (time in ms)                                  Min                 Max                Mean             StdDev              Median                IQR            Outliers      OPS            Rounds  Iterations
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_incremental_edit[discord.py-ty]           18.8740 (1.0)       24.6758 (1.0)       20.0876 (1.0)       2.1832 (1.0)       19.0685 (1.0)       0.6511 (1.0)           2;2  49.7820 (1.0)          10           1
test_incremental_edit[discord.py-pyrefly]      72.6280 (3.85)      82.8766 (3.36)      76.5269 (3.81)      3.7789 (1.73)      74.9435 (3.93)      7.2071 (11.07)         4;0  13.0673 (0.26)         10           1
test_incremental_edit[discord.py-pyright]     488.6511 (25.89)    541.3492 (21.94)    517.2384 (25.75)    16.5382 (7.58)     512.2913 (26.87)    22.0510 (33.87)         3;0   1.9333 (0.04)         10           1
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

---------------------------------------------------------------------------------------- benchmark 'homeassistant': 4 tests ----------------------------------------------------------------------------------------
Name (time in ms)                                     Min                 Max                Mean            StdDev              Median               IQR            Outliers      OPS            Rounds  Iterations
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_incremental_edit[homeassistant-ty]           22.0430 (1.0)       25.6657 (1.0)       22.6308 (1.0)      1.0774 (3.00)      22.3201 (1.0)      0.2474 (1.0)           1;1  44.1876 (1.0)          10           1
test_incremental_edit[homeassistant-pyrefly]      55.8462 (2.53)      85.5288 (3.33)      75.6855 (3.34)     8.0570 (22.42)     76.3312 (3.42)     4.9400 (19.97)         3;1  13.2126 (0.30)         10           1
test_incremental_edit[homeassistant-zuban]        56.2561 (2.55)      57.5430 (2.24)      57.0332 (2.52)     0.3593 (1.0)       57.0851 (2.56)     0.3927 (1.59)          2;0  17.5336 (0.40)         10           1
test_incremental_edit[homeassistant-pyright]     564.8898 (25.63)    580.5012 (22.62)    574.4756 (25.38)    4.9935 (13.90)    573.7045 (25.70)    6.9113 (27.93)         3;0   1.7407 (0.04)         10           1
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

----------------------------------------------------------------------------------------- benchmark 'isort': 4 tests ----------------------------------------------------------------------------------------
Name (time in ms)                             Min                 Max                Mean            StdDev              Median               IQR            Outliers       OPS            Rounds  Iterations
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_incremental_edit[isort-zuban]         5.6747 (1.0)        5.9072 (1.0)        5.7474 (1.0)      0.0701 (1.0)        5.7302 (1.0)      0.0773 (1.0)           2;1  173.9902 (1.0)          10           1
test_incremental_edit[isort-ty]           17.3874 (3.06)      17.7855 (3.01)      17.5375 (3.05)     0.1275 (1.82)      17.5074 (3.06)     0.1806 (2.34)          4;0   57.0207 (0.33)         10           1
test_incremental_edit[isort-pyrefly]      42.7818 (7.54)      57.5799 (9.75)      52.8906 (9.20)     4.5220 (64.55)     54.9351 (9.59)     5.5654 (71.97)         2;0   18.9070 (0.11)         10           1
test_incremental_edit[isort-pyright]     419.7210 (73.96)    429.1457 (72.65)    425.1017 (73.96)    2.9371 (41.93)    424.9466 (74.16)    4.3485 (56.23)         3;0    2.3524 (0.01)         10           1
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

------------------------------------------------------------------------------------------ benchmark 'jinja': 4 tests -----------------------------------------------------------------------------------------
Name (time in ms)                             Min                 Max                Mean             StdDev              Median                IQR            Outliers       OPS            Rounds  Iterations
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_incremental_edit[jinja-ty]            9.1586 (1.0)       10.2422 (1.0)        9.3816 (1.0)       0.3424 (2.56)       9.2578 (1.0)       0.0847 (1.0)           2;2  106.5919 (1.0)          10           1
test_incremental_edit[jinja-zuban]        19.9754 (2.18)      20.4125 (1.99)      20.1366 (2.15)      0.1340 (1.0)       20.1239 (2.17)      0.1803 (2.13)          3;0   49.6609 (0.47)         10           1
test_incremental_edit[jinja-pyrefly]      53.2751 (5.82)      67.2008 (6.56)      60.3027 (6.43)      4.5815 (34.19)     59.1167 (6.39)      5.8406 (68.98)         4;0   16.5830 (0.16)         10           1
test_incremental_edit[jinja-pyright]     476.3300 (52.01)    530.7210 (51.82)    503.8855 (53.71)    14.1706 (105.75)   505.3668 (54.59)    11.4062 (134.72)        2;2    1.9846 (0.02)         10           1
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

---------------------------------------------------------------------------------------- benchmark 'pandas': 4 tests -----------------------------------------------------------------------------------------
Name (time in ms)                              Min                 Max                Mean             StdDev              Median               IQR            Outliers      OPS            Rounds  Iterations
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_incremental_edit[pandas-ty]           34.9681 (1.0)       36.9436 (1.0)       35.4396 (1.0)       0.5832 (1.0)       35.2583 (1.0)      0.3973 (1.0)           1;1  28.2170 (1.0)          10           1
test_incremental_edit[pandas-pyrefly]     243.4753 (6.96)     256.9783 (6.96)     248.6074 (7.01)      4.2473 (7.28)     247.6178 (7.02)     6.6526 (16.74)         2;0   4.0224 (0.14)         10           1
test_incremental_edit[pandas-zuban]       251.8713 (7.20)     259.0576 (7.01)     254.0977 (7.17)      2.2326 (3.83)     253.3567 (7.19)     2.0706 (5.21)          2;1   3.9355 (0.14)         10           1
test_incremental_edit[pandas-pyright]     662.6549 (18.95)    701.7632 (19.00)    691.2085 (19.50)    11.6618 (20.00)    695.5558 (19.73)    8.8209 (22.20)         1;1   1.4467 (0.05)         10           1
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

------------------------------------------------------------------------------------------ benchmark 'prefect': 4 tests -----------------------------------------------------------------------------------------
Name (time in ms)                               Min                 Max                Mean             StdDev              Median                IQR            Outliers       OPS            Rounds  Iterations
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_incremental_edit[prefect-ty]            6.8997 (1.0)        7.1183 (1.0)        7.0151 (1.0)       0.0738 (1.0)        7.0045 (1.0)       0.1042 (1.0)           3;0  142.5487 (1.0)          10           1
test_incremental_edit[prefect-pyrefly]      51.3062 (7.44)      61.9334 (8.70)      56.2614 (8.02)      3.5354 (47.88)     57.8409 (8.26)      5.8660 (56.29)         4;0   17.7742 (0.12)         10           1
test_incremental_edit[prefect-zuban]       131.5461 (19.07)    132.8311 (18.66)    132.0289 (18.82)     0.4032 (5.46)     131.9307 (18.84)     0.4938 (4.74)          3;0    7.5741 (0.05)         10           1
test_incremental_edit[prefect-pyright]     660.4608 (95.72)    695.6145 (97.72)    680.8583 (97.06)    10.4803 (141.94)   682.6589 (97.46)    14.5401 (139.53)        3;0    1.4687 (0.01)         10           1
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

----------------------------------------------------------------------------------------- benchmark 'pytorch': 3 tests ----------------------------------------------------------------------------------------
Name (time in ms)                               Min                 Max                Mean            StdDev              Median               IQR            Outliers       OPS            Rounds  Iterations
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_incremental_edit[pytorch-ty]            3.3809 (1.0)        3.8737 (1.0)        3.5010 (1.0)      0.1415 (1.0)        3.4548 (1.0)      0.0805 (1.0)           1;1  285.6306 (1.0)          10           1
test_incremental_edit[pytorch-pyrefly]      20.1780 (5.97)      25.2127 (6.51)      22.7988 (6.51)     1.8837 (13.31)     23.4518 (6.79)     3.4646 (43.06)         4;0   43.8619 (0.15)         10           1
test_incremental_edit[pytorch-pyright]     411.6034 (121.74)   420.5795 (108.57)   416.2569 (118.90)   2.2362 (15.80)    416.0866 (120.44)   1.0938 (13.59)         2;2    2.4024 (0.01)         10           1
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

------------------------------------------------------------------------------------------ benchmark 'httpx': 4 tests -----------------------------------------------------------------------------------------
Name (time in ms)                             Min                 Max                Mean             StdDev              Median                IQR            Outliers       OPS            Rounds  Iterations
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_incremental_edit[httpx-ty]            6.7227 (1.0)        7.1053 (1.0)        6.8640 (1.0)       0.1125 (1.0)        6.8557 (1.0)       0.1466 (1.0)           3;0  145.6880 (1.0)          10           1
test_incremental_edit[httpx-zuban]         9.5517 (1.42)      11.7660 (1.66)       9.9430 (1.45)      0.6486 (5.77)       9.7386 (1.42)      0.1877 (1.28)          1;1  100.5729 (0.69)         10           1
test_incremental_edit[httpx-pyrefly]      47.6866 (7.09)      57.0288 (8.03)      51.7039 (7.53)      2.8466 (25.30)     52.0920 (7.60)      3.3798 (23.05)         3;0   19.3409 (0.13)         10           1
test_incremental_edit[httpx-pyright]     414.3220 (61.63)    441.5353 (62.14)    426.5495 (62.14)    10.4990 (93.33)    426.0099 (62.14)    20.2930 (138.40)        5;0    2.3444 (0.02)         10           1
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------------- benchmark 'numpy': 3 tests --------------------------------------------------------------------------------------------
Name (time in ms)                               Min                   Max                  Mean             StdDev                Median               IQR            Outliers      OPS            Rounds  Iterations
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_incremental_edit[numpy-ty]             17.7037 (1.0)         20.2315 (1.0)         18.0769 (1.0)       0.7671 (1.0)         17.8214 (1.0)      0.2546 (1.0)           1;1  55.3193 (1.0)          10           1
test_incremental_edit[numpy-pyrefly]       330.8268 (18.69)      350.2634 (17.31)      343.7851 (19.02)     6.4024 (8.35)       346.1157 (19.42)    7.2750 (28.58)         3;0   2.9088 (0.05)         10           1
test_incremental_edit[numpy-pyright]     1,171.7334 (66.19)    1,205.3624 (59.58)    1,188.2385 (65.73)    10.2539 (13.37)    1,189.4224 (66.74)    9.2393 (36.29)         3;0   0.8416 (0.02)         10           1
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

----------------------------------------------------------------------------------------- benchmark 'fastapi': 4 tests ----------------------------------------------------------------------------------------
Name (time in ms)                               Min                 Max                Mean            StdDev              Median               IQR            Outliers       OPS            Rounds  Iterations
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_incremental_edit[fastapi-ty]            6.5237 (1.0)        7.0582 (1.0)        6.7083 (1.0)      0.1551 (1.21)       6.6963 (1.0)      0.1643 (1.0)           3;1  149.0690 (1.0)          10           1
test_incremental_edit[fastapi-zuban]         8.3563 (1.28)       8.7793 (1.24)       8.5171 (1.27)     0.1283 (1.0)        8.4884 (1.27)     0.1784 (1.09)          2;0  117.4108 (0.79)         10           1
test_incremental_edit[fastapi-pyrefly]      58.2667 (8.93)      69.4830 (9.84)      65.8294 (9.81)     3.4123 (26.60)     67.0105 (10.01)    4.0596 (24.70)         2;0   15.1908 (0.10)         10           1
test_incremental_edit[fastapi-pyright]     604.3037 (92.63)    621.4753 (88.05)    614.2073 (91.56)    5.5771 (43.48)    614.2024 (91.72)    8.3417 (50.76)         3;0    1.6281 (0.01)         10           1
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

---------------------------------------------------------------------------------------- benchmark 'sqlalchemy': 4 tests -----------------------------------------------------------------------------------------
Name (time in ms)                                  Min                 Max                Mean            StdDev              Median               IQR            Outliers       OPS            Rounds  Iterations
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_incremental_edit[sqlalchemy-ty]            9.4911 (1.0)        9.7282 (1.0)        9.6110 (1.0)      0.0787 (1.0)        9.6316 (1.0)      0.1459 (1.0)           4;0  104.0469 (1.0)          10           1
test_incremental_edit[sqlalchemy-pyrefly]      56.7484 (5.98)      84.5526 (8.69)      76.4313 (7.95)     7.9762 (101.33)    76.2125 (7.91)     7.9097 (54.22)         2;1   13.0836 (0.13)         10           1
test_incremental_edit[sqlalchemy-zuban]       198.5378 (20.92)    201.8470 (20.75)    199.5849 (20.77)    0.9838 (12.50)    199.1490 (20.68)    1.1792 (8.08)          2;0    5.0104 (0.05)         10           1
test_incremental_edit[sqlalchemy-pyright]     632.0858 (66.60)    647.3986 (66.55)    639.0595 (66.49)    5.6518 (71.80)    640.6409 (66.51)    9.4287 (64.64)         5;0    1.5648 (0.02)         10           1
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

----------------------------------------------------------------------------------------- benchmark 'rich': 4 tests -----------------------------------------------------------------------------------------
Name (time in ms)                            Min                 Max                Mean            StdDev              Median                IQR            Outliers       OPS            Rounds  Iterations
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_incremental_edit[rich-ty]            4.9403 (1.0)        5.1406 (1.0)        5.0498 (1.0)      0.0697 (1.0)        5.0382 (1.0)       0.1152 (1.0)           5;0  198.0263 (1.0)          10           1
test_incremental_edit[rich-zuban]        12.7459 (2.58)      14.8288 (2.88)      13.1219 (2.60)     0.6140 (8.81)      12.9070 (2.56)      0.2442 (2.12)          1;1   76.2082 (0.38)         10           1
test_incremental_edit[rich-pyrefly]      20.0278 (4.05)      41.4377 (8.06)      31.1428 (6.17)     7.2154 (103.55)    34.0170 (6.75)     12.2488 (106.32)        4;0   32.1102 (0.16)         10           1
test_incremental_edit[rich-pyright]     433.5527 (87.76)    446.9955 (86.95)    440.7714 (87.28)    4.4355 (63.65)    442.3849 (87.81)     6.2345 (54.12)         3;0    2.2687 (0.01)         10           1
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

----------------------------------------------------------------------------------------- benchmark 'django': 4 tests ------------------------------------------------------------------------------------------
Name (time in ms)                              Min                 Max                Mean             StdDev              Median                IQR            Outliers       OPS            Rounds  Iterations
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_incremental_edit[django-zuban]         1.7699 (1.0)        1.9427 (1.0)        1.8348 (1.0)       0.0613 (1.63)       1.8271 (1.0)       0.1039 (4.35)          4;0  545.0284 (1.0)          10           1
test_incremental_edit[django-ty]            3.3010 (1.87)       3.4511 (1.78)       3.3853 (1.85)      0.0375 (1.0)        3.3894 (1.85)      0.0239 (1.0)           2;2  295.3970 (0.54)         10           1
test_incremental_edit[django-pyrefly]      21.2110 (11.98)     29.9794 (15.43)     25.4880 (13.89)     3.1539 (84.09)     26.3823 (14.44)     5.5899 (234.12)        4;0   39.2342 (0.07)         10           1
test_incremental_edit[django-pyright]     330.7418 (186.87)   381.0605 (196.15)   354.0818 (192.98)   21.3677 (569.69)   341.3754 (186.84)   39.9063 (>1000.0)       5;0    2.8242 (0.01)         10           1
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

----------------------------------------------------------------------------------------- benchmark 'sympy': 4 tests -----------------------------------------------------------------------------------------
Name (time in ms)                             Min                 Max                Mean            StdDev              Median                IQR            Outliers       OPS            Rounds  Iterations
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_incremental_edit[sympy-ty]            3.0396 (1.0)        3.2818 (1.0)        3.1235 (1.0)      0.0776 (1.0)        3.1079 (1.0)       0.1102 (1.0)           3;0  320.1507 (1.0)          10           1
test_incremental_edit[sympy-pyrefly]      28.2025 (9.28)      38.2077 (11.64)     33.0703 (10.59)    3.0461 (39.27)     32.1000 (10.33)     4.1055 (37.27)         3;0   30.2386 (0.09)         10           1
test_incremental_edit[sympy-zuban]        62.8081 (20.66)     67.0972 (20.45)     63.7676 (20.42)    1.3140 (16.94)     63.3715 (20.39)     0.7175 (6.51)          1;2   15.6819 (0.05)         10           1
test_incremental_edit[sympy-pyright]     465.8610 (153.26)   487.8697 (148.66)   479.7846 (153.60)   7.3209 (94.37)    478.8293 (154.07)   10.6199 (96.40)         3;0    2.0843 (0.01)         10           1
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

---------------------------------------------------------------------------------------- benchmark 'openai': 4 tests -----------------------------------------------------------------------------------------
Name (time in ms)                              Min                 Max                Mean            StdDev              Median               IQR            Outliers       OPS            Rounds  Iterations
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_incremental_edit[openai-zuban]         3.4460 (1.0)        3.6128 (1.0)        3.5186 (1.0)      0.0547 (1.0)        3.5069 (1.0)      0.0987 (1.0)           4;0  284.2066 (1.0)          10           1
test_incremental_edit[openai-ty]            3.7644 (1.09)       4.1036 (1.14)       3.9680 (1.13)     0.1045 (1.91)       3.9882 (1.14)     0.1589 (1.61)          3;0  252.0137 (0.89)         10           1
test_incremental_edit[openai-pyrefly]      70.9413 (20.59)     87.7718 (24.30)     82.7103 (23.51)    5.0859 (93.06)     83.1189 (23.70)    5.0480 (51.16)         1;1   12.0904 (0.04)         10           1
test_incremental_edit[openai-pyright]     457.0089 (132.62)   489.3018 (135.44)   478.7871 (136.07)   8.6623 (158.50)   481.2125 (137.22)   7.4462 (75.47)         2;1    2.0886 (0.01)         10           1
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

---------------------------------------------------------------------------------------- benchmark 'pytest': 4 tests -----------------------------------------------------------------------------------------
Name (time in ms)                              Min                 Max                Mean            StdDev              Median               IQR            Outliers       OPS            Rounds  Iterations
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_incremental_edit[pytest-ty]            7.6362 (1.0)        9.3470 (1.0)        7.9488 (1.0)      0.5006 (2.85)       7.8129 (1.0)      0.1154 (1.0)           1;1  125.8056 (1.0)          10           1
test_incremental_edit[pytest-zuban]        26.0735 (3.41)      26.7175 (2.86)      26.3351 (3.31)     0.1758 (1.0)       26.3459 (3.37)     0.2007 (1.74)          2;1   37.9721 (0.30)         10           1
test_incremental_edit[pytest-pyrefly]      55.3168 (7.24)      62.2285 (6.66)      58.5314 (7.36)     2.2135 (12.59)     58.4364 (7.48)     2.6986 (23.38)         3;0   17.0848 (0.14)         10           1
test_incremental_edit[pytest-pyright]     458.6860 (60.07)    490.4299 (52.47)    481.3327 (60.55)    8.7184 (49.58)    483.3412 (61.86)    6.7729 (58.68)         2;1    2.0776 (0.02)         10           1
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
```

### Fetch diagnostics

```shell
----------------------------------------------------------------------------------------- benchmark 'black': 4 tests ----------------------------------------------------------------------------------------
Name (time in ms)                              Min                 Max                Mean            StdDev              Median               IQR            Outliers      OPS            Rounds  Iterations
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_fetch_diagnostics[black-ty]           53.1848 (1.0)       55.7492 (1.0)       53.6592 (1.0)      0.7535 (1.83)      53.4633 (1.0)      0.3916 (1.0)           1;1  18.6361 (1.0)          10           1
test_fetch_diagnostics[black-zuban]        68.9572 (1.30)      73.7763 (1.32)      71.2262 (1.33)     1.4690 (3.57)      71.0236 (1.33)     2.1367 (5.46)          2;0  14.0398 (0.75)         10           1
test_fetch_diagnostics[black-pyrefly]     179.8352 (3.38)     181.0037 (3.25)     180.5095 (3.36)     0.4111 (1.0)      180.5079 (3.38)     0.6513 (1.66)          4;0   5.5399 (0.30)         10           1
test_fetch_diagnostics[black-pyright]     299.9607 (5.64)     302.2230 (5.42)     300.9091 (5.61)     0.6684 (1.63)     300.8832 (5.63)     0.6293 (1.61)          3;0   3.3233 (0.18)         10           1
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

----------------------------------------------------------------------------------------- benchmark 'discord.py': 4 tests ------------------------------------------------------------------------------------------
Name (time in ms)                                   Min                 Max                Mean             StdDev              Median                IQR            Outliers      OPS            Rounds  Iterations
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_fetch_diagnostics[discord.py-ty]           80.2123 (1.0)       83.0548 (1.0)       80.8108 (1.0)       0.8653 (3.43)      80.5531 (1.0)       0.6466 (3.33)          1;1  12.3746 (1.0)          10           1
test_fetch_diagnostics[discord.py-zuban]       177.4120 (2.21)     184.2058 (2.22)     180.0302 (2.23)      2.0807 (8.26)     179.8533 (2.23)      1.9461 (10.03)         3;1   5.5546 (0.45)         10           1
test_fetch_diagnostics[discord.py-pyrefly]     187.9900 (2.34)     188.8244 (2.27)     188.3708 (2.33)      0.2520 (1.0)      188.3499 (2.34)      0.1941 (1.0)           4;2   5.3087 (0.43)         10           1
test_fetch_diagnostics[discord.py-pyright]     621.1201 (7.74)     663.5259 (7.99)     630.2578 (7.80)     12.6775 (50.30)    626.5515 (7.78)     11.5769 (59.64)         1;1   1.5867 (0.13)         10           1
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

---------------------------------------------------------------------------------------------- benchmark 'homeassistant': 4 tests ---------------------------------------------------------------------------------------------
Name (time in ms)                                        Min                   Max                  Mean             StdDev                Median                IQR            Outliers      OPS            Rounds  Iterations
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_fetch_diagnostics[homeassistant-ty]             81.0942 (1.0)         81.6612 (1.0)         81.3481 (1.0)       0.1928 (1.0)         81.3268 (1.0)       0.2609 (1.0)           3;0  12.2928 (1.0)          10           1
test_fetch_diagnostics[homeassistant-zuban]         214.2382 (2.64)       219.2897 (2.69)       217.0925 (2.67)      1.7237 (8.94)       217.0206 (2.67)      2.0827 (7.98)          4;0   4.6063 (0.37)         10           1
test_fetch_diagnostics[homeassistant-pyrefly]       236.2060 (2.91)       239.4906 (2.93)       237.6687 (2.92)      1.0456 (5.42)       237.4407 (2.92)      1.0302 (3.95)          3;0   4.2075 (0.34)         10           1
test_fetch_diagnostics[homeassistant-pyright]     1,890.3885 (23.31)    1,924.0052 (23.56)    1,905.1369 (23.42)    10.7615 (55.83)    1,903.1950 (23.40)    14.3797 (55.11)         4;0   0.5249 (0.04)         10           1
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

----------------------------------------------------------------------------------------- benchmark 'isort': 4 tests -----------------------------------------------------------------------------------------
Name (time in ms)                              Min                 Max                Mean            StdDev              Median                IQR            Outliers      OPS            Rounds  Iterations
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_fetch_diagnostics[isort-zuban]        39.6183 (1.0)       44.7363 (1.06)      41.2833 (1.0)      1.4294 (10.85)     40.9556 (1.0)       1.3667 (13.35)         2;1  24.2229 (1.0)          10           1
test_fetch_diagnostics[isort-ty]           41.5515 (1.05)      42.0646 (1.0)       41.7895 (1.01)     0.1317 (1.0)       41.7718 (1.02)      0.1024 (1.0)           2;2  23.9294 (0.99)         10           1
test_fetch_diagnostics[isort-pyrefly]     126.7168 (3.20)     140.7936 (3.35)     134.1324 (3.25)     5.9800 (45.41)    134.6929 (3.29)     11.4701 (112.04)        4;0   7.4553 (0.31)         10           1
test_fetch_diagnostics[isort-pyright]     355.6153 (8.98)     360.0408 (8.56)     358.0638 (8.67)     1.4327 (10.88)    358.1251 (8.74)      2.5620 (25.03)         4;0   2.7928 (0.12)         10           1
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

----------------------------------------------------------------------------------------- benchmark 'jinja': 4 tests ----------------------------------------------------------------------------------------
Name (time in ms)                              Min                 Max                Mean            StdDev              Median               IQR            Outliers      OPS            Rounds  Iterations
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_fetch_diagnostics[jinja-ty]           43.3489 (1.0)       43.7942 (1.0)       43.5760 (1.0)      0.1517 (1.0)       43.5660 (1.0)      0.2734 (1.0)           4;0  22.9484 (1.0)          10           1
test_fetch_diagnostics[jinja-zuban]        85.7727 (1.98)      88.3310 (2.02)      86.9519 (2.00)     0.7278 (4.80)      87.0239 (2.00)     0.7648 (2.80)          2;0  11.5006 (0.50)         10           1
test_fetch_diagnostics[jinja-pyrefly]     125.6743 (2.90)     126.7780 (2.89)     126.3703 (2.90)     0.3741 (2.47)     126.4106 (2.90)     0.6636 (2.43)          4;0   7.9133 (0.34)         10           1
test_fetch_diagnostics[jinja-pyright]     353.2582 (8.15)     361.2105 (8.25)     356.3589 (8.18)     2.3240 (15.32)    355.8286 (8.17)     3.4593 (12.65)         2;0   2.8062 (0.12)         10           1
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

---------------------------------------------------------------------------------------- benchmark 'pandas': 4 tests ----------------------------------------------------------------------------------------
Name (time in ms)                               Min                 Max                Mean            StdDev              Median               IQR            Outliers     OPS            Rounds  Iterations
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_fetch_diagnostics[pandas-ty]          298.5411 (1.0)      304.3703 (1.0)      299.9820 (1.0)      1.8750 (1.0)      299.2466 (1.0)      2.4159 (1.0)           1;0  3.3335 (1.0)          10           1
test_fetch_diagnostics[pandas-pyrefly]     539.1561 (1.81)     562.5021 (1.85)     543.9112 (1.81)     6.9893 (3.73)     541.4131 (1.81)     2.4565 (1.02)          1;2  1.8385 (0.55)         10           1
test_fetch_diagnostics[pandas-pyright]     629.9906 (2.11)     647.6225 (2.13)     639.1170 (2.13)     5.6742 (3.03)     640.4880 (2.14)     9.5839 (3.97)          4;0  1.5647 (0.47)         10           1
test_fetch_diagnostics[pandas-zuban]       666.4379 (2.23)     680.6972 (2.24)     673.7827 (2.25)     4.4995 (2.40)     673.4846 (2.25)     6.0168 (2.49)          3;0  1.4842 (0.45)         10           1
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------------- benchmark 'prefect': 4 tests ---------------------------------------------------------------------------------------------
Name (time in ms)                                  Min                   Max                  Mean             StdDev                Median                IQR            Outliers     OPS            Rounds  Iterations
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_fetch_diagnostics[prefect-ty]            141.6225 (1.0)        145.8938 (1.0)        143.3660 (1.0)       1.5674 (1.0)        142.6658 (1.0)       3.0057 (1.04)          4;0  6.9752 (1.0)          10           1
test_fetch_diagnostics[prefect-pyrefly]       332.9010 (2.35)       467.9147 (3.21)       452.5213 (3.16)     42.0522 (26.83)      465.0061 (3.26)      2.8783 (1.0)           1;1  2.2098 (0.32)         10           1
test_fetch_diagnostics[prefect-zuban]         859.7134 (6.07)       865.6050 (5.93)       863.4421 (6.02)      2.2602 (1.44)       864.5682 (6.06)      3.9808 (1.38)          3;0  1.1582 (0.17)         10           1
test_fetch_diagnostics[prefect-pyright]     1,102.1569 (7.78)     1,130.7971 (7.75)     1,113.3106 (7.77)     10.0063 (6.38)     1,112.3842 (7.80)     16.5983 (5.77)          5;0  0.8982 (0.13)         10           1
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

---------------------------------------------------------------------------------------------- benchmark 'pytorch': 4 tests ---------------------------------------------------------------------------------------------
Name (time in ms)                                  Min                   Max                  Mean             StdDev                Median                IQR            Outliers      OPS            Rounds  Iterations
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_fetch_diagnostics[pytorch-ty]             59.0455 (1.0)         62.8995 (1.0)         59.8251 (1.0)       1.1568 (1.0)         59.4721 (1.0)       0.4351 (1.0)           1;2  16.7154 (1.0)          10           1
test_fetch_diagnostics[pytorch-pyrefly]       116.7863 (1.98)       145.4521 (2.31)       128.6864 (2.15)     14.0053 (12.11)      118.9156 (2.00)     27.4318 (63.04)         4;0   7.7708 (0.46)         10           1
test_fetch_diagnostics[pytorch-pyright]       702.6213 (11.90)      709.5476 (11.28)      705.4807 (11.79)     2.5295 (2.19)       704.5238 (11.85)     4.3440 (9.98)          3;0   1.4175 (0.08)         10           1
test_fetch_diagnostics[pytorch-zuban]       1,825.0715 (30.91)    1,860.6000 (29.58)    1,835.6793 (30.68)     9.9072 (8.56)     1,835.3201 (30.86)     8.8780 (20.40)         2;1   0.5448 (0.03)         10           1
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

----------------------------------------------------------------------------------------- benchmark 'httpx': 4 tests ----------------------------------------------------------------------------------------
Name (time in ms)                              Min                 Max                Mean            StdDev              Median               IQR            Outliers      OPS            Rounds  Iterations
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_fetch_diagnostics[httpx-ty]           39.1986 (1.0)       40.1746 (1.0)       39.6171 (1.0)      0.3942 (1.0)       39.4998 (1.0)      0.7537 (1.0)           5;0  25.2416 (1.0)          10           1
test_fetch_diagnostics[httpx-zuban]        69.2425 (1.77)      71.2874 (1.77)      70.2522 (1.77)     0.6870 (1.74)      70.2971 (1.78)     0.9758 (1.29)          3;0  14.2344 (0.56)         10           1
test_fetch_diagnostics[httpx-pyrefly]     114.3010 (2.92)     118.0325 (2.94)     115.3196 (2.91)     1.1948 (3.03)     114.8530 (2.91)     1.1663 (1.55)          2;1   8.6716 (0.34)         10           1
test_fetch_diagnostics[httpx-pyright]     224.9341 (5.74)     228.4704 (5.69)     226.4147 (5.72)     1.0548 (2.68)     226.3045 (5.73)     1.0174 (1.35)          3;1   4.4167 (0.17)         10           1
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

------------------------------------------------------------------------------------------------ benchmark 'numpy': 4 tests -----------------------------------------------------------------------------------------------
Name (time in ms)                                 Min                    Max                   Mean             StdDev                 Median                 IQR            Outliers     OPS            Rounds  Iterations
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_fetch_diagnostics[numpy-ty]             160.6400 (1.0)         182.6270 (1.0)         165.9340 (1.0)       6.3025 (4.39)        164.3488 (1.0)        3.2548 (3.51)          1;1  6.0265 (1.0)          10           1
test_fetch_diagnostics[numpy-pyrefly]        562.9346 (3.50)        568.0607 (3.11)        564.3641 (3.40)      1.4365 (1.0)         564.1055 (3.43)       0.9281 (1.0)           1;1  1.7719 (0.29)         10           1
test_fetch_diagnostics[numpy-pyright]      1,182.4547 (7.36)      1,212.2849 (6.64)      1,199.6223 (7.23)      9.0291 (6.29)      1,198.6239 (7.29)      12.4973 (13.47)         3;0  0.8336 (0.14)         10           1
test_fetch_diagnostics[numpy-zuban]       36,078.9349 (224.59)   36,423.6785 (199.44)   36,193.5729 (218.12)   98.8916 (68.84)    36,198.7695 (220.26)   119.7505 (129.02)        2;1  0.0276 (0.00)         10           1
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

----------------------------------------------------------------------------------------- benchmark 'fastapi': 4 tests ----------------------------------------------------------------------------------------
Name (time in ms)                                Min                 Max                Mean            StdDev              Median               IQR            Outliers      OPS            Rounds  Iterations
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_fetch_diagnostics[fastapi-ty]           85.1741 (1.0)       88.4667 (1.0)       86.0940 (1.0)      1.0142 (1.74)      85.8062 (1.0)      0.4641 (1.0)           2;2  11.6152 (1.0)          10           1
test_fetch_diagnostics[fastapi-zuban]       171.4969 (2.01)     177.0828 (2.00)     173.4509 (2.01)     1.8097 (3.10)     173.0481 (2.02)     2.5310 (5.45)          3;0   5.7653 (0.50)         10           1
test_fetch_diagnostics[fastapi-pyrefly]     199.6927 (2.34)     201.7180 (2.28)     200.3882 (2.33)     0.5838 (1.0)      200.3402 (2.33)     0.6110 (1.32)          2;1   4.9903 (0.43)         10           1
test_fetch_diagnostics[fastapi-pyright]     457.2369 (5.37)     470.3823 (5.32)     465.9305 (5.41)     3.9981 (6.85)     466.0065 (5.43)     4.5289 (9.76)          3;1   2.1462 (0.18)         10           1
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

---------------------------------------------------------------------------------------- benchmark 'sqlalchemy': 4 tests ----------------------------------------------------------------------------------------
Name (time in ms)                                   Min                 Max                Mean            StdDev              Median               IQR            Outliers     OPS            Rounds  Iterations
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_fetch_diagnostics[sqlalchemy-ty]          184.4423 (1.0)      189.6220 (1.0)      187.2045 (1.0)      1.4448 (1.0)      187.2169 (1.0)      2.0694 (1.32)          2;0  5.3418 (1.0)          10           1
test_fetch_diagnostics[sqlalchemy-pyrefly]     250.0255 (1.36)     256.0001 (1.35)     251.9413 (1.35)     1.6665 (1.15)     251.7372 (1.34)     1.6916 (1.08)          2;1  3.9692 (0.74)         10           1
test_fetch_diagnostics[sqlalchemy-pyright]     270.1789 (1.46)     276.0185 (1.46)     272.7359 (1.46)     1.6008 (1.11)     272.7561 (1.46)     1.5684 (1.0)           2;1  3.6666 (0.69)         10           1
test_fetch_diagnostics[sqlalchemy-zuban]       383.2057 (2.08)     399.6241 (2.11)     386.9370 (2.07)     4.6166 (3.20)     385.5155 (2.06)     2.3762 (1.52)          1;1  2.5844 (0.48)         10           1
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

---------------------------------------------------------------------------------------- benchmark 'rich': 4 tests -----------------------------------------------------------------------------------------
Name (time in ms)                             Min                 Max                Mean            StdDev              Median               IQR            Outliers      OPS            Rounds  Iterations
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_fetch_diagnostics[rich-ty]           36.1197 (1.0)       38.5802 (1.0)       36.6509 (1.0)      0.7291 (1.0)       36.3236 (1.0)      0.4692 (1.0)           1;1  27.2845 (1.0)          10           1
test_fetch_diagnostics[rich-zuban]        79.5685 (2.20)      82.3503 (2.13)      80.7725 (2.20)     0.8009 (1.10)      80.6681 (2.22)     0.5338 (1.14)          3;2  12.3804 (0.45)         10           1
test_fetch_diagnostics[rich-pyrefly]      99.5237 (2.76)     115.1077 (2.98)     110.9954 (3.03)     5.6315 (7.72)     113.2185 (3.12)     1.7742 (3.78)          2;2   9.0094 (0.33)         10           1
test_fetch_diagnostics[rich-pyright]     309.8927 (8.58)     314.1458 (8.14)     311.3170 (8.49)     1.3331 (1.83)     310.9984 (8.56)     1.9001 (4.05)          3;0   3.2122 (0.12)         10           1
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

---------------------------------------------------------------------------------------- benchmark 'django': 4 tests -----------------------------------------------------------------------------------------
Name (time in ms)                               Min                 Max                Mean            StdDev              Median               IQR            Outliers      OPS            Rounds  Iterations
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_fetch_diagnostics[django-ty]           21.7860 (1.0)       24.7737 (1.0)       22.2781 (1.0)      0.8924 (1.19)      21.9620 (1.0)      0.3634 (1.0)           1;1  44.8872 (1.0)          10           1
test_fetch_diagnostics[django-zuban]        45.0162 (2.07)      47.3812 (1.91)      46.3298 (2.08)     0.7499 (1.0)       46.4050 (2.11)     0.7135 (1.96)          4;1  21.5844 (0.48)         10           1
test_fetch_diagnostics[django-pyrefly]      90.8160 (4.17)      96.1161 (3.88)      94.1640 (4.23)     2.2035 (2.94)      95.3465 (4.34)     4.3802 (12.05)         3;0  10.6198 (0.24)         10           1
test_fetch_diagnostics[django-pyright]     587.8771 (26.98)    610.7550 (24.65)    593.6576 (26.65)    8.6595 (11.55)    589.8123 (26.86)    2.7981 (7.70)          2;2   1.6845 (0.04)         10           1
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

----------------------------------------------------------------------------------------- benchmark 'sympy': 4 tests ----------------------------------------------------------------------------------------
Name (time in ms)                              Min                 Max                Mean            StdDev              Median               IQR            Outliers      OPS            Rounds  Iterations
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_fetch_diagnostics[sympy-ty]           65.4690 (1.0)       69.7235 (1.0)       66.3799 (1.0)      1.2557 (1.16)      65.9127 (1.0)      0.6829 (1.15)          1;1  15.0648 (1.0)          10           1
test_fetch_diagnostics[sympy-pyrefly]     179.4386 (2.74)     183.1834 (2.63)     180.5083 (2.72)     1.0781 (1.0)      180.2387 (2.73)     0.5938 (1.0)           1;1   5.5399 (0.37)         10           1
test_fetch_diagnostics[sympy-zuban]       260.1722 (3.97)     274.6859 (3.94)     265.9684 (4.01)     4.4955 (4.17)     264.4641 (4.01)     7.1645 (12.07)         2;0   3.7598 (0.25)         10           1
test_fetch_diagnostics[sympy-pyright]     392.3544 (5.99)     400.7913 (5.75)     396.7093 (5.98)     2.7972 (2.59)     396.7134 (6.02)     5.3469 (9.01)          4;0   2.5207 (0.17)         10           1
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

---------------------------------------------------------------------------------------- benchmark 'openai': 4 tests -----------------------------------------------------------------------------------------
Name (time in ms)                               Min                 Max                Mean            StdDev              Median               IQR            Outliers      OPS            Rounds  Iterations
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_fetch_diagnostics[openai-ty]           58.5604 (1.0)       60.8052 (1.0)       59.6067 (1.0)      0.7767 (1.0)       59.6806 (1.0)      1.1436 (1.0)           4;0  16.7766 (1.0)          10           1
test_fetch_diagnostics[openai-zuban]       139.0193 (2.37)     143.9898 (2.37)     141.1401 (2.37)     1.4470 (1.86)     140.7476 (2.36)     1.9043 (1.67)          2;0   7.0852 (0.42)         10           1
test_fetch_diagnostics[openai-pyrefly]     188.4392 (3.22)     202.4323 (3.33)     199.4188 (3.35)     5.1057 (6.57)     201.7685 (3.38)     1.2412 (1.09)          2;2   5.0146 (0.30)         10           1
test_fetch_diagnostics[openai-pyright]     513.3347 (8.77)     518.7722 (8.53)     515.7981 (8.65)     2.2311 (2.87)     515.5012 (8.64)     4.6511 (4.07)          5;0   1.9387 (0.12)         10           1
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

---------------------------------------------------------------------------------------- benchmark 'pytest': 4 tests -----------------------------------------------------------------------------------------
Name (time in ms)                               Min                 Max                Mean            StdDev              Median               IQR            Outliers      OPS            Rounds  Iterations
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_fetch_diagnostics[pytest-ty]           67.6779 (1.0)       70.2133 (1.0)       68.7026 (1.0)      0.7623 (1.0)       68.6753 (1.0)      0.8243 (1.0)           3;0  14.5555 (1.0)          10           1
test_fetch_diagnostics[pytest-zuban]       132.7784 (1.96)     135.7364 (1.93)     134.2270 (1.95)     1.0887 (1.43)     134.4337 (1.96)     1.9573 (2.37)          5;0   7.4501 (0.51)         10           1
test_fetch_diagnostics[pytest-pyrefly]     183.1395 (2.71)     186.5047 (2.66)     185.1065 (2.69)     1.0400 (1.36)     185.1994 (2.70)     1.2209 (1.48)          4;0   5.4023 (0.37)         10           1
test_fetch_diagnostics[pytest-pyright]     289.3343 (4.28)     291.7467 (4.16)     290.7208 (4.23)     0.7864 (1.03)     290.6446 (4.23)     1.2309 (1.49)          3;0   3.4397 (0.24)         10           1
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
```
