# ty 0.0.111 benchmark evidence

This directory preserves the original raw exports from the ty 0.0.111 refresh: 18 CLI measurements and 17 LSP fixtures with diagnostic-fetching and incremental-edit samples. The manifest records commands, dates, tool versions, input checksums and an immutable link to the prior archive.

Only ty was rerun. Other checker measurements retain their original dates and are linked from the prior archive. The active LSP view contains 133 timing objects for 136 intended outcomes; three retained Zuban incremental failures have no timings. The retained NumPy/Zuban CLI timeout likewise has no timing result.

CLI measurements use native checker concurrency, three warmups and at least ten measured runs. LSP measurements retain sixteen pool threads, two warmups and ten measured rounds. Peak RSS is peak process RSS on macOS and does not sum concurrent processes.

Private environment/source maps and full collection reports are excluded. The manifest hashes raw exports, inputs and protocol files; it excludes itself and this README.
