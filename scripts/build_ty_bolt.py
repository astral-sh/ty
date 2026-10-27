"""Optimize the Linux x86-64 ty executable and wheel with LLVM BOLT."""

from __future__ import annotations

import argparse
import base64
import csv
import hashlib
import io
import os
import subprocess
import tempfile
import zipfile
from pathlib import Path

from build_ty_pgo import (
    CORPUS_PROJECTS,
    EXCLUDED_ENVIRONMENT_VARIABLES,
    find_llvm_tool,
    rustc_host,
    training_command,
)


def replace_wheel_executable(wheel: Path, binary: Path) -> None:
    with tempfile.TemporaryDirectory(dir=wheel.parent) as directory:
        staged = Path(directory) / wheel.name
        with zipfile.ZipFile(wheel) as src, zipfile.ZipFile(staged, "w") as dst:
            (script,) = (n for n in src.namelist() if n.endswith(".data/scripts/ty"))
            (record,) = (n for n in src.namelist() if n.endswith(".dist-info/RECORD"))
            payload = binary.read_bytes()
            digest = base64.urlsafe_b64encode(hashlib.sha256(payload).digest()).rstrip(
                b"="
            )
            rows = list(csv.reader(io.StringIO(src.read(record).decode())))
            (script_row,) = (row for row in rows if row[0] == script)
            script_row[1:] = [f"sha256={digest.decode()}", str(len(payload))]
            updated = io.StringIO(newline="")
            csv.writer(updated, lineterminator="\n").writerows(rows)
            replacements = {script: payload, record: updated.getvalue().encode()}
            for entry in src.infolist():
                data = (
                    replacements[entry.filename]
                    if entry.filename in replacements
                    else src.read(entry)
                )
                dst.writestr(entry, data)
        staged.replace(wheel)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--llvm-dir", required=True, type=Path)
    parser.add_argument("--pgo-dir", required=True, type=Path)
    parser.add_argument("--binary", required=True, type=Path)
    parser.add_argument("--wheel", required=True, type=Path)
    args = parser.parse_args()
    binary = args.binary.resolve()
    bolt = args.llvm_dir / "bin/llvm-bolt"
    pgo = args.pgo_dir.resolve()
    environment = {
        k: v for k, v in os.environ.items() if k not in EXCLUDED_ENVIRONMENT_VARIABLES
    }

    with tempfile.TemporaryDirectory(dir=binary.parent) as directory:
        work = Path(directory)
        instrumented = work / "ty-instrumented"
        data = work / "ty.fdata"
        subprocess.run(
            [
                bolt,
                binary,
                "--instrument",
                "--thread-count=3",
                f"--instrumentation-file={data}",
                f"--runtime-instrumentation-lib={args.llvm_dir / 'lib/libbolt_rt_instr.a'}",
                "-o",
                instrumented,
            ],
            check=True,
        )
        profiles = []
        for project in CORPUS_PROJECTS:
            checkout = pgo / "corpus" / project.name
            python = pgo / "environments" / project.name / "bin/python"
            print(f"Profiling ty on {project.name}", flush=True)
            subprocess.run(
                training_command(instrumented, project, checkout, python),
                cwd=checkout,
                env=environment,
                check=True,
            )
            profiles.append(data.rename(work / f"{project.name}.fdata"))
        with data.open("wb") as stream:
            subprocess.run(
                [args.llvm_dir / "bin/merge-fdata", "-q", *profiles],
                stdout=stream,
                check=True,
            )

        optimized = work / "ty-optimized"

        def rewrite(*split_options: str) -> str:
            result = subprocess.run(
                [
                    bolt,
                    binary,
                    f"--data={data}",
                    "--reorder-blocks=ext-tsp",
                    "--reorder-functions=cdsort",
                    *split_options,
                    "--jump-tables=move",
                    "--icf=all",
                    "--align-functions=1",
                    "--align-functions-max-bytes=0",
                    "--align-blocks=false",
                    "--use-old-text",
                    "--no-huge-pages",
                    "--hugify=false",
                    "--thread-count=3",
                    "-o",
                    optimized,
                ],
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
            )
            print(result.stdout, flush=True)
            result.check_returncode()
            return result.stdout

        log = rewrite(
            "--split-functions", "--split-all-cold", "--split-strategy=cdsplit"
        )
        if "--use-old-text failed. The original .text too small" in log:
            print(
                "Retrying without function splitting to fit the original .text.",
                flush=True,
            )
            log = rewrite("--split-functions=false")
        # BOLT appends a second copy of the code if it outgrows the original text segment.
        if "using original .text for new code" not in log:
            print(
                "Keeping the compiler PGO layout because BOLT did not reuse the original .text.",
                flush=True,
            )
            optimized = binary

        stripped = work / "ty"
        # GNU strip can move BOLT's unwind sections out of their load segment.
        strip = find_llvm_tool("llvm-strip", rustc_host())
        subprocess.run([strip, "--strip-all", "-o", stripped, optimized], check=True)
        subprocess.run([stripped, "--version"], check=True)
        replace_wheel_executable(args.wheel, stripped)
        stripped.replace(binary)


if __name__ == "__main__":
    main()
