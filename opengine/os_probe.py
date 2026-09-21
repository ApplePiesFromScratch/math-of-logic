#!/usr/bin/env python3
"""OS + runtime letters we can read here."""
from __future__ import annotations

import os
import sys


def main():
    print("pid", os.getpid(), "ppid", os.getppid())
    print("page", os.sysconf("SC_PAGESIZE") if hasattr(os, "sysconf") else "?")
    print("cwd", os.getcwd())
    print("fd stdin/out/err", sys.stdin.fileno(), sys.stdout.fileno(), sys.stderr.fileno())
    print("uid", os.getuid(), "euid", os.geteuid())
    print("path sep", os.sep, "path V is strings + this letter")
    try:
        print("nproc", os.cpu_count())
    except Exception as e:
        print(e)
    st = open("/proc/self/status").read()
    for key in ("VmRSS:", "Threads:", "Cpus_allowed:"):
        for line in st.splitlines():
            if line.startswith(key):
                print(line)
    print("open files /proc/self/fd", len(os.listdir("/proc/self/fd")))


if __name__ == "__main__":
    main()
