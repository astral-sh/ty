#!/usr/bin/env bash
set -euo pipefail

ECOSYSTEM_ANALYZER_COMMIT="${ECOSYSTEM_ANALYZER_COMMIT:-7e3a45ca84ad4a30ba90cb27af0b568f37608e84}"
RUFF_DIR="${RUFF_DIR:-ruff}"
EXCLUDE_NEWER="${EXCLUDE_NEWER:-$(git -C "${RUFF_DIR}" show --no-ext-diff --format=%cI --no-patch HEAD)}"
PGO_TARGET_DIR="${PGO_TARGET_DIR:-${RUFF_DIR}/target/ty-pgo}"
PGO_OUTPUT="${PGO_OUTPUT:-}"
PGO_TRAIN_ONLY="${PGO_TRAIN_ONLY:-0}"
TY_MAX_PARALLELISM="${TY_MAX_PARALLELISM:-8}"
CARGO_INCREMENTAL="${CARGO_INCREMENTAL:-0}"

case "$(uname -s)" in
  Darwin | Linux) ;;
  *)
    echo "scripts/build_ty_pgo.sh only supports host-native Darwin and Linux builds." >&2
    exit 1
  ;;
esac

PGO_OUTPUT="${PGO_OUTPUT:-${PGO_TARGET_DIR}/release/ty}"

find_llvm_profdata() {
  if [[ -n "${LLVM_PROFDATA:-}" ]]; then
    echo "${LLVM_PROFDATA}"
    return
  fi

  if command -v llvm-profdata >/dev/null 2>&1; then
    command -v llvm-profdata
    return
  fi

  local rustc_host
  rustc_host="$(rustc -vV | sed -n 's/^host: //p')"
  local rustc_llvm_profdata
  rustc_llvm_profdata="$(rustc --print sysroot)/lib/rustlib/${rustc_host}/bin/llvm-profdata"
  if [[ -x "${rustc_llvm_profdata}" ]]; then
    echo "${rustc_llvm_profdata}"
    return
  fi

  echo "llvm-profdata was not found. Install llvm-tools-preview or set LLVM_PROFDATA." >&2
  exit 1
}

append_rustflags() {
  local pgo_rustflags="$1"
  if [[ -n "${RUSTFLAGS:-}" ]]; then
    echo "${RUSTFLAGS} ${pgo_rustflags}"
  else
    echo "${pgo_rustflags}"
  fi
}

case "${RUFF_DIR}" in
  /*) ruff_dir="${RUFF_DIR}" ;;
  *) ruff_dir="$(pwd)/${RUFF_DIR}" ;;
esac
case "${PGO_TARGET_DIR}" in
  /*) pgo_target_dir="${PGO_TARGET_DIR}" ;;
  *) pgo_target_dir="$(pwd)/${PGO_TARGET_DIR}" ;;
esac
case "${PGO_OUTPUT}" in
  /*) pgo_output="${PGO_OUTPUT}" ;;
  *) pgo_output="$(pwd)/${PGO_OUTPUT}" ;;
esac

llvm_profdata="$(find_llvm_profdata)"
instrumented_target_dir="${pgo_target_dir}/instrumented"
profile_dir="${pgo_target_dir}/profiles"
merged_profile="${pgo_target_dir}/ty.profdata"
diagnostics="${pgo_target_dir}/ecosystem-diagnostics.json"
config_dir="${pgo_target_dir}/config"
cache_dir="${pgo_target_dir}/cache"

rm -rf "${profile_dir}"
mkdir -p "${profile_dir}" "${config_dir}/ty"
cp "${ruff_dir}/.github/ty-ecosystem.toml" "${config_dir}/ty/ty.toml"

echo "Building and training instrumented ty with the ecosystem analyzer corpus"
(
  cd "${ruff_dir}"
  RUSTFLAGS="$(append_rustflags "-Cprofile-generate=${profile_dir} -Cllvm-args=-vp-counters-per-site=16")" \
  CARGO_INCREMENTAL="${CARGO_INCREMENTAL}" \
  TY_MAX_PARALLELISM="${TY_MAX_PARALLELISM}" \
  UV_EXCLUDE_NEWER="${EXCLUDE_NEWER}" \
  XDG_CACHE_HOME="${cache_dir}" \
  XDG_CONFIG_HOME="${config_dir}" \
  uvx \
    --from "git+https://github.com/astral-sh/ecosystem-analyzer@${ECOSYSTEM_ANALYZER_COMMIT}" \
    ecosystem-analyzer \
    --repository . \
    --target "${instrumented_target_dir}" \
    analyze \
    --commit HEAD \
    --profile release \
    --output "${diagnostics}"
)

"${llvm_profdata}" merge --output="${merged_profile}" "${profile_dir}"
echo "PGO profile: ${merged_profile}"

if [[ "${PGO_TRAIN_ONLY}" == "1" ]]; then
  exit 0
fi

echo "Building PGO ty"
(
  cd "${ruff_dir}"
  RUSTFLAGS="$(append_rustflags "-Cprofile-use=${merged_profile} -Cllvm-args=-pgo-warn-missing-function")" \
  CARGO_INCREMENTAL="${CARGO_INCREMENTAL}" \
  CARGO_TARGET_DIR="${pgo_target_dir}" \
  cargo build --locked --package ty --release
)

test -x "${pgo_output}"
echo "PGO ty binary: ${pgo_output}"
