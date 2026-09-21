#!/usr/bin/env python3
"""Same merge, 2-line book vs many-line book."""
from __future__ import annotations


def double(left_n, right_n):
    return [("debit nothing", 0), ("credit sum", left_n + right_n)]


def process_lines(left, right):
    return [
        ("debit left loc", left["loc"]),
        ("debit right loc", right["loc"]),
        ("credit front loc", "front"),
        ("debit pile-count in", left["piles"] + right["piles"]),
        ("credit pile-count out", 1),
        ("debit vol in", left["vol"] + right["vol"]),
        ("credit vol out", left["vol"] + right["vol"]),
        ("stamp G", "merge-to-front"),
        ("stamp V_loc", {"left", "right", "front"}),
        ("theta", "none"),
    ]


def main():
    left = {"loc": "left", "piles": 2, "vol": 2}
    right = {"loc": "right", "piles": 2, "vol": 2}
    print("DOUBLE (school +)")
    for row in double(2, 2):
        print(" ", row)
    print("PROCESS")
    for row in process_lines(left, right):
        print(" ", row)
    print("lines double", 2, "lines process", len(process_lines(left, right)))


if __name__ == "__main__":
    main()
