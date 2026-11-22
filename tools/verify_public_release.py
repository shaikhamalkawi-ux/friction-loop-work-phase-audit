#!/usr/bin/env python3
"""Validate pinned SHA-256 digests, ZIP structure/CRCs, and key derived-ledger row counts.

This is a derived-only repository packaging check, NOT a replay of provider measurements.
"""
from __future__ import annotations

import csv
import hashlib
import io
from pathlib import Path
import zipfile

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {
    "imperial_56H2B_code_and_ledgers_20261122.zip": (
        35, "imperial/results/SD16_Imperial27_Exhaustive75_AllScores.csv", 48600,
        "c65a3c4fb3a05ff6a6701a484e4df75aefaa18b4e10eaf2646639948392eba57"
    ),
    "eucentre_sd21_56H2B_code_and_ledgers_20261122.zip": (
        22, "eucentre/sd21/RESULTS/P2_EUCENTRE_EXHAUSTIVE_PHASE_SCORES.csv", 60750,
        "da4ffc51834ac9270f0eaa2be770985e810d247e9524ce2ea03ae1290b9a1ef9"
    ),
    "eucentre_r5_56H2B_code_and_ledgers_20261122.zip": (
        15, "eucentre/r5/R5_PAIRED_Q32_ALL_SCORES.csv", 12150,
        "47351e92b247f38abcf614d9237ce5bd47f8695a824529440c915fb48822f396"
    ),
    "eucentre_r6_56H2B_code_and_ledgers_20261122.zip": (
        17, "eucentre/r6/results/R6_FACT_48K_ERRORS.csv", 48600,
        "03bccf4b3ac0e5b336e7af68d410bcd4d95e951495a37c763865e8ca344fccfe"
    ),
}


def run() -> None:
    for filename, (expected_files, ledger, expected_rows, expected_sha256) in EXPECTED.items():
        path = ROOT / "releases" / filename
        if not path.is_file():
            raise FileNotFoundError(path)
        with path.open("rb") as source:
            actual_sha256 = hashlib.file_digest(source, "sha256").hexdigest()
        if actual_sha256 != expected_sha256:
            raise AssertionError(
                f"{filename}: SHA-256 mismatch: expected {expected_sha256}, got {actual_sha256}"
            )
        with zipfile.ZipFile(path) as bundle:
            names = bundle.namelist()
            if len(names) != expected_files or len(set(names)) != expected_files:
                raise AssertionError(f"{filename}: file-count or duplicate-path error")
            if bundle.testzip() is not None:
                raise AssertionError(f"{filename}: ZIP CRC check failed")
            for name in names:
                parts = Path(name).parts
                if name.startswith("/") or ".." in parts or "\\" in name:
                    raise AssertionError(f"{filename}: unsafe archive path {name}")
                low = name.lower()
                if low.startswith("manuscript/") or low.endswith((".mat", ".tdms")):
                    raise AssertionError(f"{filename}: non-release source {name}")
                if low.endswith("felt_testdata.zip"):
                    raise AssertionError(f"{filename}: third-party original ZIP {name}")
            with bundle.open(ledger) as stream:
                reader = csv.reader(io.TextIOWrapper(stream, encoding="utf-8", newline=""))
                next(reader)
                observed_rows = sum(1 for _ in reader)
            if observed_rows != expected_rows:
                raise AssertionError(
                    f"{filename}: expected {expected_rows} derived rows, got {observed_rows}"
                )
        print(f"PASS {filename}: SHA-256 OK, {expected_files} files, ZIP CRC OK, {expected_rows} derived rows")
    print("PUBLIC ARCHIVE INTEGRITY PASS (derived-only; no original-source replay)")


if __name__ == "__main__":
    run()
