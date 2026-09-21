#!/usr/bin/env python3
"""Constants that move. Smoothness cost. Distinction vs history."""
from __future__ import annotations

from fractions import Fraction as F


def arrival(L0, goal=50.0, C=1.0, cap=10**6):
    x = 0.0
    L = float(L0)
    t = 0
    while x < goal and t < cap:
        v = C / (C + L)  # drag
        x += v
        t += 1
    return t


def arrival_growing(eta, goal=50.0, C=1.0, cap=10**6):
    x = L = 0.0
    t = 0
    while x < goal and t < cap:
        v = C / (C + L)
        x += v
        L += eta * v
        t += 1
    return t, L


def host_lei(a, b):
    (v, r), (w, s) = a, b
    return (v * w, r * w + v * s)


def wrap_lei(n):
    def m(a, b):
        (v, r), (w, s) = a, b
        return ((v * w) % n, (r * w + v * s) % n)
    return m


def main():
    print("=== drag: L held constant vs L=0 'smooth' ===")
    for L in (0, 1, 2, 8, 12):
        print(f"  L={L:<3} ticks_to_50={arrival(L)}")
    print(f"  zero-drag L=0 is {arrival(0)} ticks; L=8 is {arrival(8)} ({arrival(8)/arrival(0)}x)")

    print()
    print("=== history grows: eta writes L as you move ===")
    for eta in (0, 0.1, 0.5, 1.0):
        t, L = arrival_growing(eta)
        print(f"  eta={eta:<4} ticks={t:<6} L_end={L:.3f}")

    print()
    print("=== '2' in 2x is not constant ===")
    print(f"  host     (1,1)*(1,1) = {host_lei((1,1),(1,1))}   2x=2")
    for n in (2, 3, 5):
        print(f"  wrap Z/{n} (1,1)*(1,1) = {wrap_lei(n)((1,1),(1,1))}   2%{n}={2%n}")

    print()
    print("=== '1' as THE seed is not the only unit that gauges ===")
    slopes = []
    for k in (1, 2, F(1, 2), -1, 7):
        x = (3, k)
        xx = host_lei(x, x)
        sl = xx[1] / x[1]
        slopes.append((k, sl))
    print(" ", slopes)

    print()
    print("=== smoothness = every write lands; listed Vr fails ===")
    for m in (2, 4, 8):
        Vr = list(range(m))
        leak = sum(1 for r in Vr for s in Vr if (r + s) not in Vr)
        print(f"  Vr=0..{m-1}  +leaks={leak}  C(m,2)={m*(m-1)//2}")

    print()
    print("=== delete a distinction ===")
    print("  wrap fold 2->0 on Z/2:", 2 % 2)
    print("  project drop r from (9,6):", 9, "  slope gone")
    print("  seed 0 dead:", host_lei((3, 0), (3, 0)))
    print("  val-eq merges two mints (9,6) and (9,6)")

    print()
    print("=== hold a distinction: keep r live and mint ===")
    live = (9, 6)
    dead = (9, 0)
    print(f"  live rate vs dead: {live[1]}/{1} vs dead isolator")
    print(f"  hold mint: origin x2 vs 3x still two letters if you keep origin")

    print()
    print("=== manipulate: gauge vs wrap vs host ===")
    print("  gauge k=2 on r=1:", (3, 1 * 2))
    print("  wrap after host leak:", (host_lei((1, 1), (1, 1))[1] % 2))
    print("  those are different remaining distinctions")


if __name__ == "__main__":
    main()
