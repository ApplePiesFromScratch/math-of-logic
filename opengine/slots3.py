#!/usr/bin/env python3
"""Pivot: wrap is the finite host. Rate needs a field or it grows Vq.
Triangular leak count. Load only closes for trivial vent."""
from __future__ import annotations

from fractions import Fraction as F
from itertools import product


def wrap_rate(r, s, n):
    if s % n == 0:
        return "THETA"
    for k in range(n):
        if (s * k) % n == r % n:
            return k
    return "NO_INV"


def main():
    print("=== triangular Lr on bits values, Vr=0..m-1 host leibniz ===")
    print("  expect Lr = C(m,2) = m(m-1)/2  (pairs r,s with r+s>=m, v=w=1)")
    for m in range(1, 9):
        Vr = range(m)
        Lr = 0
        for r, s in product(Vr, Vr):
            if r + s >= m:
                Lr += 1
        print(f"  m={m} Lr={Lr} C(m,2)={m*(m-1)//2} match={Lr==m*(m-1)//2}")

    print()
    print("=== rate on Z/n : host / vs modular inverse ===")
    for n in (2, 3, 4, 5, 6, 7):
        host_out = set()
        wrap_out = set()
        theta = noinv = 0
        for r, s in product(range(n), range(n)):
            if s == 0:
                theta += 1
                continue
            host_out.add(F(r, s))
            wr = wrap_rate(r, s, n)
            if wr == "NO_INV":
                noinv += 1
            elif wr != "THETA":
                wrap_out.add(wr)
        extra_host = [q for q in host_out if q not in range(n)]
        print(f"  Z/{n} host_|Vq|={len(host_out)} extra={extra_host[:6]}  "
              f"wrap_Vq={sorted(wrap_out)} no_inv={noinv} theta={theta}")

    print()
    print("=== load vent closed only if coefficients stay in Vl ===")
    # kappa=1 keep all: closed
    # kappa=0 n=1 dump all to one child: child=L, closed
    Vl = tuple(range(0, 13))
    for kappa, nch, label in ((1, 3, "keep_all"), (0, 1, "one_child_all"),
                              (F(1, 2), 2, "half_two"), (F(2, 5), 3, "workbook")):
        leaks = 0
        for L in Vl:
            kept = kappa * L
            child = 0 if nch == 0 else (1 - kappa) * L / nch
            if kept not in Vl or child not in Vl:
                leaks += 1
        print(f"  {label:<16} leaks={leaks}/{len(Vl)} closed={leaks==0}")

    print()
    print("=== D after wrap-leibniz: Vr=Vv=Z/n so D lands ===")
    for n in (2, 3, 5):
        V = range(n)
        bad = [(v, r) for v in V for r in V if (r % n) not in V or 0 not in V]
        print(f"  Z/{n} D always lands {not bad}")


if __name__ == "__main__":
    main()
