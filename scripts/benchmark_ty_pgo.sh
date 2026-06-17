#!/usr/bin/env bash
set -euo pipefail

ECOSYSTEM_ANALYZER_COMMIT="${ECOSYSTEM_ANALYZER_COMMIT:-7e3a45ca84ad4a30ba90cb27af0b568f37608e84}"
RUFF_DIR="${RUFF_DIR:-ruff}"
EXCLUDE_NEWER="${EXCLUDE_NEWER:-$(git -C "${RUFF_DIR}" show --no-ext-diff --format=%cI --no-patch HEAD)}"
TY_MAX_PARALLELISM="${TY_MAX_PARALLELISM:-8}"
BENCHMARK_DIR="${BENCHMARK_DIR:-${RUFF_DIR}/target/ty-pgo-benchmark}"
case "${RUFF_DIR}" in
  /*) ruff_dir="${RUFF_DIR}" ;;
  *) ruff_dir="$(pwd)/${RUFF_DIR}" ;;
esac
case "${BENCHMARK_DIR}" in
  /*) benchmark_dir="${BENCHMARK_DIR}" ;;
  *) benchmark_dir="$(pwd)/${BENCHMARK_DIR}" ;;
esac
RELEASE_TARGET_DIR="${benchmark_dir}/release"
PGO_TARGET_DIR="${benchmark_dir}/pgo"
RELEASE_TY="${RELEASE_TARGET_DIR}/release/ty"
PGO_TY="${PGO_TARGET_DIR}/release/ty"
ECOSYSTEM_DIR="${benchmark_dir}/ecosystem"
ECOSYSTEM_CONFIG_DIR="${ECOSYSTEM_DIR}/config"
ECOSYSTEM_CACHE_DIR="${ECOSYSTEM_DIR}/cache"

echo "Building release ty"
(
  cd "${ruff_dir}"
  CARGO_TARGET_DIR="${RELEASE_TARGET_DIR}" cargo build --locked --package ty --release
)

RUFF_DIR="${ruff_dir}" \
PGO_TARGET_DIR="${PGO_TARGET_DIR}" \
PGO_OUTPUT="${PGO_TY}" \
EXCLUDE_NEWER="${EXCLUDE_NEWER}" \
ECOSYSTEM_ANALYZER_COMMIT="${ECOSYSTEM_ANALYZER_COMMIT}" \
scripts/build_ty_pgo.sh

echo "Comparing release and PGO release on the ecosystem analyzer corpus"
mkdir -p "${ECOSYSTEM_CONFIG_DIR}/ty"
cp "${ruff_dir}/.github/ty-ecosystem.toml" "${ECOSYSTEM_CONFIG_DIR}/ty/ty.toml"
(
  cd "${ruff_dir}"
  TY_MAX_PARALLELISM="${TY_MAX_PARALLELISM}" UV_EXCLUDE_NEWER="${EXCLUDE_NEWER}" XDG_CACHE_HOME="${ECOSYSTEM_CACHE_DIR}" XDG_CONFIG_HOME="${ECOSYSTEM_CONFIG_DIR}" uvx \
    --from "git+https://github.com/astral-sh/ecosystem-analyzer@${ECOSYSTEM_ANALYZER_COMMIT}" \
    ecosystem-analyzer \
    --flaky-runs 1 \
    diff \
    --old HEAD \
    --new HEAD \
    --ty-binary-old "${RELEASE_TY}" \
    --ty-binary-new "${PGO_TY}" \
    --output-old "${ECOSYSTEM_DIR}/release.json" \
    --output-new "${ECOSYSTEM_DIR}/pgo.json"
)

uvx \
  --from "git+https://github.com/astral-sh/ecosystem-analyzer@${ECOSYSTEM_ANALYZER_COMMIT}" \
  ecosystem-analyzer \
  generate-timing-diff \
  "${ECOSYSTEM_DIR}/release.json" \
  "${ECOSYSTEM_DIR}/pgo.json" \
  --old-name release \
  --new-name pgo-release \
  --output-html "${ECOSYSTEM_DIR}/timing.html"

echo "Ecosystem timing report: ${ECOSYSTEM_DIR}/timing.html"
