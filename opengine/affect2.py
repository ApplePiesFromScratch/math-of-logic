#!/usr/bin/env python3
"""Leibniz = two closed meets plus a +. Replace + with a closed +. Invent G."""
from __future__ import annotations

from itertools import product

BITS = (0, 1)
P = [(v, r) for v in BITS for r in BITS]


def closed(fn):
    for a, b in product(P, P):
        o = fn(a, b)
        if o[0] not in BITS or o[1] not in BITS:
            return False, (a, b, o)
    return True, None


def main():
    print("=== each Leibniz meet alone, then the + ===")
    def only_rw(a, b):
        (v, r), (w, s) = a, b
        return (v * w, r * w)

    def only_vs(a, b):
        (v, r), (w, s) = a, b
        return (v * w, v * s)

    def plus_chans(a, b):
        # add the two channel writes as if we already have them
        return (a[0], a[1] + b[1])

    def xor_chans(a, b):
        return (a[0], a[1] ^ b[1])

    def lei_plus(a, b):
        (v, r), (w, s) = a, b
        return (v * w, r * w + v * s)

    def lei_xor(a, b):
        (v, r), (w, s) = a, b
        return (v * w, (r * w) ^ (v * s))

    def lei_or(a, b):
        (v, r), (w, s) = a, b
        return (v * w, (r * w) | (v * s))

    def lei_max(a, b):
        (v, r), (w, s) = a, b
        return (v * w, max(r * w, v * s))

    for name, fn in [
        ("only r*w", only_rw),
        ("only v*s", only_vs),
        ("lei +", lei_plus),
        ("lei xor", lei_xor),
        ("lei or", lei_or),
        ("lei max", lei_max),
    ]:
        ok, sample = closed(fn)
        at11 = fn((1, 1), (1, 1))
        print(f"  {name:<12} {'CLOSE' if ok else 'LEAK'}  (1,1)*(1,1)={at11} {'' if ok else sample}")

    print()
    print("=== plus on channels alone ===")
    print("  +  on bits channels", closed(plus_chans)[0], "sample", closed(plus_chans)[1])
    print("  ^  on bits channels", closed(xor_chans)[0])

    print()
    print("=== change VALUE meet too ===")
    def min_val_lei_xor(a, b):
        (v, r), (w, s) = a, b
        return (min(v, w), (r * w) ^ (v * s))

    def and_val_and_chan(a, b):
        (v, r), (w, s) = a, b
        return (v & w, r & s)

    for name, fn in (("min_val xor_lei", min_val_lei_xor), ("and_and", and_val_and_chan)):
        ok, sample = closed(fn)
        print(f"  {name:<18} {'CLOSE' if ok else 'LEAK'} (1,1)*(1,1)={fn((1,1),(1,1))} (1,1)*(0,1)={fn((1,1),(0,1))}")

    print()
    print("=== dynamic: mid-stream grow Vr after a write ===")
    # start Vr=bits, compute lei_xor (stays), then switch G to lei_+ without growing Vr
    x = (1, 1)
    y = (1, 1)
    stay = (x[0] * y[0], (x[1] * y[0]) ^ (x[0] * y[1]))
    print(f"  after xor-lei: {stay} in bits? {stay[1] in BITS}")
    grown = (x[0] * y[0], x[1] * y[0] + x[0] * y[1])
    print(f"  switch G to host+ without μ: {grown} in bits? {grown[1] in BITS}")
    print(f"  switch G after μ Vr+= {2}: {grown} in (0,1,2)? {grown[1] in (0, 1, 2)}")


if __name__ == "__main__":
    main()
