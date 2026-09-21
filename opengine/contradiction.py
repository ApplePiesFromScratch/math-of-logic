#!/usr/bin/env python3
"""Several things people call contradiction. Print the actual G."""
from __future__ import annotations

from fractions import Fraction as F


def lei(a, b):
    (v, r), (w, s) = a, b
    return (v * w, r * w + v * s)


def xorlei(a, b):
    (v, r), (w, s) = a, b
    return (v * w, (r * w) ^ (v * s))


def main():
    print("C1 two combinators, same meets, different letter")
    print("  lei", lei((1, 1), (1, 1)), "xor", xorlei((1, 1), (1, 1)))

    print("C2 two compose-orders")
    # XZ vs ZX already; tiny: f then g vs g then f on bits wrap
    def tu(v):
        return ((v[0] + 1) % 3, v[1])

    def tv(v):
        return (v[0], (v[1] + 1 + v[0]) % 3)

    print("  uv", tv(tu((0, 0))), "vu", tu(tv((0, 0))))

    print("C3 write leaves V")
    print("  lei bits (1,2) in {0,1}^2?", (1, 2)[1] in (0, 1))

    print("C4 val-eq of two mints")
    print("  (9,6) x2 vs (9,6) 3x  val-eq True mint-eq False")

    print("C5 wrap vs host on the same ink 2")
    print("  host 2==0", 2 == 0, "wrap2 2%2==0", (2 % 2) == 0)

    print("C6 both letters of V2")
    # p and not p : 1 and 0 both present as values, not as one row
    print("  V2 letters", (0, 1), "a row that is 1 and 0 at once: none")

    print("C7 V3 middle with itself under prod vs min")
    print("  prod", F(1, 2) * F(1, 2), "min", min(F(1, 2), F(1, 2)))

    print("C8 explosion toy: from False write every letter")
    V = (0, 1)

    def explode(p, q):
        if p == 0:
            return V
        return (q,)

    print("  explode(0,1) writes", explode(0, 1), "whole V")

    print("C9 dead rate")
    print("  0/0 THETA  (not 1, not 0)")

    print("C10 TypeError host mismatch")
    try:
        F(1, 2) ^ F(1, 2)
    except TypeError as e:
        print(" ", e)

    print("C11 two reads, vacuum")
    print("  matter 0 geom 1")

    print("C12 vacuous close empty V")
    print("  leaks on () = 0, close True")

    print("C13 0=1 in a ring after 2=2*1 and 2=0")
    print("  if you keep host 2 and wrap 0 you have two letters for one ink")

    print("C14 Born(ψ) and Born(-ψ) equal; people call it same state")
    print("  equal read, two pairs")

    print("C15 λ=+1 vac min vs λ=-1 wall min")
    print("  two filters, two mins, one word vacuum")


if __name__ == "__main__":
    main()
