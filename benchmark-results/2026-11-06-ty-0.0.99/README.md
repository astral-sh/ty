# ty 0.0.99 benchmark evidence

This directory preserves original Hyperfine 2 and pytest-benchmark exports for the ty 0.0.99 refresh, retained checker results, and prior ty 0.0.96 comparison data. Measurement dates, commands, versions, machine, source guide, public project inputs, and SHA-256 checksums are in `manifest.json`.

CLI measurements use native checker concurrency, three warmups, and at least ten measured runs. LSP measurements retain sixteen pool threads, two warmups, and ten measured rounds. The 133 active LSP timing objects correspond to 136 intended outcomes; three retained Zuban incremental failures are recorded in `lsp/current-testcases.json`.

Peak RSS is peak process RSS on macOS and does not sum concurrent processes. Private environment/source maps and full private reports are excluded. The manifest hashes raw exports, inputs, and protocol files; it excludes itself and this README so formatting either cannot invalidate original raw checksums.
