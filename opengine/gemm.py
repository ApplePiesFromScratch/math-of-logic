#!/usr/bin/env python3
"""Tiny GEMM: exact Q vs float leftover, associativity, tile isolate."""
from __future__ import annotations

from fractions import Fraction as F
from itertools import product


def gemm(A, B):
    n = len(A)
    C = [[0 for _ in range(n)] for _ in range(n)]
    for i, j, k in product(range(n), repeat=3):
        C[i][j] += A[i][k] * B[k][j]
    return C


def main():
    Aq = [[F(1, 3), F(1, 3)], [F(1, 3), F(2, 3)]]
    Bq = [[F(3, 1), F(0)], [F(0), F(3, 1)]]
    Cq = gemm(Aq, Bq)
    print("Q GEMM", Cq)

    Af = [[1 / 3, 1 / 3], [1 / 3, 2 / 3]]
    Bf = [[3.0, 0.0], [0.0, 3.0]]
    Cf = gemm(Af, Bf)
    print("float GEMM", Cf)
    print("leftover C00", Cf[0][0] - float(Cq[0][0]))

    # associativity: (e e) e vs e (e e) on 2x2 of 0.1
    e = [[0.1, 0.1], [0.1, 0.1]]
    ee = gemm(e, e)
    left = gemm(ee, e)
    right = gemm(e, ee)
    print("(ee)e", left)
    print("e(ee)", right)
    print("assoc leftover", left[0][0] - right[0][0])

    eq = [[F(1, 10), F(1, 10)], [F(1, 10), F(1, 10)]]
    eeq = gemm(eq, eq)
    print("Q (ee)e00", gemm(eeq, eq)[0][0], "Q e(ee)00", gemm(eq, eeq)[0][0])

    # wrap GEMM on Z/256 one entry
    print("byte MAC 200*2+100", (200 * 2 + 100) & 255, "host", 200 * 2 + 100)

    # tile: 2x2 as one isolate vs four 1x1
    print("tiles 1x1 count", 4, "tiles 2x2 count", 1)


if __name__ == "__main__":
    main()
