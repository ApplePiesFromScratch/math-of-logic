#!/usr/bin/env python3
"""Run gated scripts. Stdlib only."""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent

GATES = [
    ("test_slots.py", "35/35"),
    ("test_affect.py", "20/20"),
    ("forge.py", "16/16"),
    ("recover.py", "29/29"),
    ("prior.py", "14/14"),
    ("listed_field.py", "30/30"),
    ("verify.py", "9/9"),
    ("accountant.py", "8/8"),
    ("ml.py", "15/15"),
]


def run(name):
    p = subprocess.run(
        [sys.executable, str(ROOT / name)],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    out = (p.stdout or "") + (p.stderr or "")
    return p.returncode, out


def main():
    failed = []
    paid = 0
    for name, expect in GATES:
        code, out = run(name)
        ok = code == 0 and expect in out
        mark = "PASS" if ok else "FAIL"
        print(f"  {mark} {name:<22} want {expect}")
        if not ok:
            failed.append(name)
            print(out[-400:])
        else:
            paid += int(expect.split("/")[0])
    print(f"PAID ROWS {paid}  GATES {len(GATES) - len(failed)}/{len(GATES)}")
    print("VERIFY_ALL PASS" if not failed else "VERIFY_ALL FAIL " + str(failed))
    raise SystemExit(1 if failed else 0)


if __name__ == "__main__":
    main()
