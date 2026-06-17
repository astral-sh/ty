#!/usr/bin/env bash
set -euo pipefail

ECOSYSTEM_ANALYZER_COMMIT="${ECOSYSTEM_ANALYZER_COMMIT:-7e3a45ca84ad4a30ba90cb27af0b568f37608e84}"
BENCHMARK_DIR="${BENCHMARK_DIR:-ruff/target/ty-pgo-benchmark}"
RELEASE_TY="${BENCHMARK_DIR}/release/release/ty"
PGO_TY="${BENCHMARK_DIR}/pgo/release/ty"

if [[ ! -x "${RELEASE_TY}" || ! -x "${PGO_TY}" ]]; then
  echo "Build release ty and run scripts/build_ty_pgo.sh before comparing instructions." >&2
  exit 1
fi

env -u UV_EXCLUDE_NEWER UV_NO_CONFIG=1 uv run \
  --no-project \
  --python 3.14 \
  --with "git+https://github.com/astral-sh/ecosystem-analyzer@${ECOSYSTEM_ANALYZER_COMMIT}" \
  python scripts/compare_ty_pgo_instructions.py \
  --release-ty "${RELEASE_TY}" \
  --pgo-ty "${PGO_TY}" \
  "$@"
