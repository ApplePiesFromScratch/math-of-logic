#!/usr/bin/env python3
"""Two piles left, two right, merge in front. Several reads of one write."""
from __future__ import annotations


def merge(left, right):
    """One location. Volumes add. Pile-count collapses to 1."""
    return {
        "loc": "front",
        "piles": 1,
        "vol": left["vol"] + right["vol"],
        "grains": left["grains"] + right["grains"],
    }


def main():
    left = {"loc": "left", "piles": 2, "vol": 2, "grains": 2000}
    right = {"loc": "right", "piles": 2, "vol": 2, "grains": 2000}
    out = merge(left, right)
    print("in ", left, right)
    print("out", out)
    print("pile-count", left["piles"] + right["piles"], "->", out["piles"])
    print("volume    ", left["vol"] + right["vol"], "->", out["vol"])
    print("grains    ", left["grains"] + right["grains"], "->", out["grains"])
    print("locations ", {left["loc"], right["loc"]}, "->", out["loc"])
    print("school + on the count letters 2+2=", 2 + 2, "but count-read of merge is", out["piles"])


if __name__ == "__main__":
    main()
