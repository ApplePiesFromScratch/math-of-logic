#!/usr/bin/env python3
"""Cross-wire G from different machines. Print what happens. No PASS religion."""
from __future__ import annotations

from fractions import Fraction as F
from itertools import product


def lei(a, b):
    (v, r), (w, s) = a, b
    return (v * w, r * w + v * s)


def xorlei(a, b):
    (v, r), (w, s) = a, b
    return (v * w, (r * w) ^ (v * s))


def cmul(a, b):
    (p, q), (r, s) = a, b
    return (p * r - q * s, p * s + q * r)


def born(z):
    a, b = z
    return a * a + b * b


def eta(u, v):
    return u[0] * v[0] - u[1] * v[1]


def rate(tr, br):
    if br == 0:
        return "THETA"
    return F(tr) / F(br)


def main():
    print("B1 born of a Reading (9,6)")
    print(" ", born((9, 6)))

    print("B2 eta of a Reading (9,6) with itself")
    print(" ", eta((9, 6), (9, 6)))

    print("B3 rate of eta(t,t) over eta(x,x)")
    print(" ", rate(eta((1, 0), (1, 0)), eta((0, 1), (0, 1))))

    print("B4 Leibniz then complex on (1,1),(1,1)")
    L = lei((1, 1), (1, 1))
    print("  lei", L, "then c*c", cmul(L, L))

    print("B5 complex then Leibniz on (1,1),(1,1)")
    C = cmul((1, 1), (1, 1))
    print("  c", C, "then lei*lei", lei(C, C))

    print("B6 isolate seed = value (3,3) squared lei")
    print(" ", lei((3, 3), (3, 3)), "rate", rate(18, 3))

    print("B7 two deads rate")
    print(" ", rate(0, 0))

    print("B8 Leibniz on two probabilities (1/2,1/2)")
    print(" ", lei((F(1, 2), F(1, 2)), (F(1, 2), F(1, 2))))

    print("B9 product independence vs Leibniz on same pair")
    print("  prod", F(1, 2) * F(1, 2), "lei value slot", lei((F(1, 2), 1), (F(1, 2), 1))[0])

    print("B10 wrap 1: everything folds to 0")
    print("  5%1", 5 % 1, "lei wrap1", ((1 * 1) % 1, (1 * 1 + 1 * 1) % 1))

    print("B11 swap slots of (9,6) then rate vs x=(3,1)")
    print("  swapped rate", rate(9, 1), "normal", rate(6, 1))

    print("B12 D then D on (9,6)")
    d1 = (6, 0)
    d2 = (0, 0)
    print(" ", d1, d2)

    print("B13 tensor two Readings as 4-tuple then is_product")
    ac, ad, bc, bd = 3 * 3, 3 * 1, 1 * 3, 1 * 1
    print(" ", (ac, ad, bc, bd), "product?", ac * bd == ad * bc)

    print("B14 tensor x with xx")
    t = (3 * 9, 3 * 6, 1 * 9, 1 * 6)
    print(" ", t, "product?", t[0] * t[3] == t[1] * t[2])

    print("B15 gauge k=i on (3,1) via complex scale")
    # (3,1) as 3+1ε not 3+i; pretend scale first slot only
    print("  not typed; skip object. complex scale (3,0) by i:", cmul((0, 1), (3, 0)))

    print("B16 Born after complex i*i")
    print(" ", born(cmul((0, 1), (0, 1))))

    print("B17 Born after lei (1,1)^2")
    print(" ", born(lei((1, 1), (1, 1))))

    print("B18 add-then-born vs born-then-add on Readings (3,1)+(2,0)")
    s = (5, 1)
    print("  born(sum)", born(s), "sum born", born((3, 1)) + born((2, 0)))

    print("B19 φ⁴ S with λ=-1 on listed {-1,0,1}")
    def S(cfg, lam):
        kin = sum((cfg[i] - cfg[(i + 1) % 4]) ** 2 for i in range(4))
        return kin + lam * sum(x ** 4 for x in cfg)
    print("  vac", S((0, 0, 0, 0), -1), "bump", S((1, 0, 0, 0), -1), "wall", S((1, 1, 1, 1), -1))

    print("B20 empty V scan")
    V = ()
    leaks = 0
    for a, b in product(V, V):
        leaks += 1
    print("  pairs", leaks, "all([]) close?", True)  # zero leaks

    print("B21 rate of plaquette leftover slots")
    print(" ", rate(2, 1))

    print("B22 xorlei of two Q fractions")
    try:
        print(" ", xorlei((F(1, 2), 1), (F(1, 2), 1)))
    except Exception as e:
        print(" ", type(e).__name__, e)

    print("B23 Peano ticks vs lei ticks: 3*3")
    print("  host 9, lei r=6; Peano 3*3 would be 9 S if billed")

    print("B24 η(null,null)/η(t,t)")
    print(" ", rate(eta((1, 1), (1, 1)), eta((1, 0), (1, 0))))

    print("B25 same leftover number 1 from [a,a†] and from curv letter and from quartic bump")
    print("  three 1s, three G")


if __name__ == "__main__":
    main()
