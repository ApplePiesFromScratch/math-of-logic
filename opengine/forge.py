#!/usr/bin/env python3
"""Mint closed pair-mixes on a listed frame.

Enumerates 16 binary bit combinators as the channel combiner of
the two Leibniz meets. Prints which close, and the write at (1,1)*(1,1).
"""
from __future__ import annotations

from itertools import product

BITS = (0, 1)
P = [(v, r) for v in BITS for r in BITS]


def bit_op(code):
    """code 0..15 as the truth table of (x,y) -> bit, x+2y index."""
    def op(x, y):
        return (code >> (x + 2 * y)) & 1
    return op


def mix_from(code):
    comb = bit_op(code)

    def mix(a, b):
        (v, r), (w, s) = a, b
        return (v * w, comb(r * w, v * s))

    return mix


def lands(mix):
    for a, b in product(P, P):
        o = mix(a, b)
        if o[0] not in BITS or o[1] not in BITS:
            return False
    return True


def table_name(code):
    names = {
        0: "0",
        1: "AND",          # x&y  at bits: (0,0)->0 (1,0)->1 (0,1)->0 (1,1)->1 wait
        # index x+2y: 0:(0,0) 1:(1,0) 2:(0,1) 3:(1,1)
    }
    bits = "".join(str((code >> i) & 1) for i in range(4))
    known = {
        "0000": "const0",
        "1111": "const1",
        "1000": "AND",      # 1 only at (1,1) if we used y+2x...
        "0111": "OR",
        "0110": "XOR",
        "1001": "EQ",
        "0100": "proj_y",
        "0010": "proj_x?",
        "1010": "proj_x",
        "1100": "proj_y",
        "0001": "NOR-ish",
        "1110": "NAND-ish",
    }
    # compute actual at (0,0)(1,0)(0,1)(1,1)
    op = bit_op(code)
    sig = tuple(op(x, y) for x, y in ((0, 0), (1, 0), (0, 1), (1, 1)))
    label = {
        (0, 0, 0, 0): "0",
        (1, 1, 1, 1): "1",
        (0, 0, 0, 1): "AND",
        (0, 1, 1, 1): "OR",
        (0, 1, 1, 0): "XOR",
        (1, 0, 0, 1): "EQ",
        (0, 1, 0, 1): "proj_x",
        (0, 0, 1, 1): "proj_y",
        (1, 1, 0, 0): "NOT_y",
        (1, 0, 1, 0): "NOT_x",
        (1, 1, 1, 0): "NAND",
        (1, 0, 0, 0): "NOR",
        (1, 0, 1, 1): "x→y",
        (1, 1, 0, 1): "y→x",
        (0, 1, 0, 0): "x∧¬y",
        (0, 0, 1, 0): "¬x∧y",
    }.get(sig, bits)
    return label, sig


def main():
    print("FORGE  Vv=Vr={0,1}  mix=(v*w, comb(r*w, v*s))")
    print(f"{'code':<6} {'comb':<10} {'sig':<12} {'close':<6} {'(1,1)*(1,1)'}")
    closed = []
    for code in range(16):
        mix = mix_from(code)
        name, sig = table_name(code)
        ok = lands(mix)
        write = mix((1, 1), (1, 1))
        print(f"{code:<6} {name:<10} {sig} {str(ok):<6} {write}")
        if ok:
            closed.append((code, name, write))
    print(f"closed {len(closed)}/16")
    print("minted writes at x=1 seed=1 squared:", sorted(set(w for _, _, w in closed)))


if __name__ == "__main__":
    main()
