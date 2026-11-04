# Raw Hyperfine results

This directory preserves the original Hyperfine 2 JSON exports for the November 4, 2026 CLI benchmark collection with native concurrency defaults. The 89 exports contain 1,202 measured runs across 18 projects and are copied byte for byte from the captured results.

Each `hyperfine/<project>/<checker>.json` contains the original command, individual measurements, exit codes, metric units, and summaries. The manifest records file hashes, sample counts, tool versions, hardware, input revisions, concurrency policy, and measurement settings. Exit codes 0 and 1 are accepted by the benchmark runner.

NumPy/Zuban exceeded the 600-second root-preflight limit. Its failure is recorded in `manifest.json`; it has no Hyperfine timing export. Peak RSS is per process on macOS and does not sum concurrent processes.

These are CLI measurements. The published language-server measurements were retained from the earlier November 3 collection.
