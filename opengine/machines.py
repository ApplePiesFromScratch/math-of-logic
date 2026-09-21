#!/usr/bin/env python3
"""Tiny paid cuts that QM / GR / prob reuse from this stack."""
from __future__ import annotations

from fractions import Fraction as F
from itertools import product


def rate(top_r, bot_r):
    if bot_r == 0:
        raise ZeroDivisionError("dead isolator")
    return F(top_r) / F(bot_r)


def born(amp):
    # |a+bi|^2 = a^2+b^2  — drop phase, write Vq
    a, b = amp
    return a * a + b * b


def main():
    print("=== STAT: conditional is rate; P=0 is dead isolator ===")
    # die
    die = list(range(1, 7))
    P_even = F(sum(1 for d in die if d % 2 == 0), 6)
    P_gt3 = F(sum(1 for d in die if d > 3), 6)
    P_even_and_gt3 = F(sum(1 for d in die if d % 2 == 0 and d > 3), 6)
    print(f"  P(even)={P_even} P(gt3)={P_gt3} P(both)={P_even_and_gt3}")
    print(f"  P(even|gt3) = both/gt3 = {rate(P_even_and_gt3, P_gt3)}")
    try:
        rate(P_even_and_gt3, 0)
        print("  P(*|empty) landed")
    except ZeroDivisionError:
        print("  P(*|empty) THETA dead isolator")

    print()
    print("=== STAT: independence is product-of-rates, not Leibniz ===")
    # two coins P(H)=1/2
    p, q = F(1, 2), F(1, 2)
    prod = p * q
    print(f"  P(HH) if independent = product {prod}")
    print("  Leibniz would add channel meets; that is a different G")

    print()
    print("=== STAT: i.i.d. is val-eq across trials ===")
    t1, t2 = ("coin", F(1, 2)), ("coin", F(1, 2))
    print(f"  val-eq trials {t1[1]==t2[1]}  mint-eq {t1 is t2}")

    print()
    print("=== QM: Born drops the pair ===")
    psi = (F(3, 5), F(4, 5))  # 3/5 + 4/5 i, norm 1
    print(f"  amp {psi}  born={born(psi)}")
    psi2 = (F(-3, 5), F(-4, 5))  # global minus
    print(f"  phase-flip {psi2} born={born(psi2)}  π killed the sign")

    print()
    print("=== QM: i from complex square-rule, not extra substance ===")
    def c_mul(p, q):
        a, b = p
        c, d = q
        return (a * c - b * d, a * d + b * c)
    print(f"  i*i = {c_mul((0,1),(0,1))}")

    print()
    print("=== QM: commutator leftover ===")
    # on bits, host + vs xor: two mixes of same meets
    def lei(p, q):
        (v, r), (w, s) = p, q
        return (v * w, r * w + v * s)
    def xorm(p, q):
        (v, r), (w, s) = p, q
        return (v * w, (r * w) ^ (v * s))
    a = b = (1, 1)
    print(f"  host lei a*b={lei(a,b)} xor a*b={xorm(a,b)}  leftover slot {lei(a,b)[1]-xorm(a,b)[1]}")

    print()
    print("=== GR-shaped: leftover as curvature stand-in ===")
    # jet r2 vs stencil already paid in calc; reprint the split
    x, h = F(2), F(1, 2)
    f = lambda t: t ** 4
    stencil = (f(x + h) - 2 * f(x) + f(x - h)) / (h * h)
    jet_r2 = F(48)  # d2/dx2 x^4 = 12 x^2 at 2 = 48
    print(f"  stencil={stencil} jet_r2={jet_r2} leftover={stencil-jet_r2}")

    print()
    print("=== GR-shaped: metric as comparison (rate) ===")
    # ds along two isolations of same displacement
    print("  g(u,v) is a bilinear read of two isolations; not a property of a point")
    print("  coordinate change is gauge: seed rescale. Slope ratio can hold; components move")


if __name__ == "__main__":
    main()
