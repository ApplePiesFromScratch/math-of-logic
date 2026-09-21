#!/usr/bin/env python3
"""Adjoin a letter with a square-rule. Complex / dual / split / idempotent."""
from __future__ import annotations

from itertools import product

BITS = (0, 1)
Z5 = tuple(range(5))


def mul(rel):
    """(a,b)*(c,d) = (ac + rel_v(b,d), ad+bc + rel_r(b,d))
    rel returns (write_to_value, write_to_channel) from b*d.
    """
    def m(p, q):
        a, b = p
        c, d = q
        ev, er = rel(b, d)
        return (a * c + ev, a * d + b * c + er)
    return m


def rel_dual(b, d):
    return (0, 0)           # ε² = 0


def rel_complex(b, d):
    return (-b * d, 0)      # i² = -1  → value slot


def rel_split(b, d):
    return (b * d, 0)       # j² = +1


def rel_idemp(b, d):
    return (0, b * d)       # ε² = ε   → channel slot


def rel_zero_and_chan(b, d):
    return (0, b * d)       # same idemp


def scan(name, rel, V):
    m = mul(rel)
    leaks = []
    for p, q in product(((x, y) for x in V for y in V), repeat=2):
        o = m(p, q)
        if o[0] not in V or o[1] not in V:
            leaks.append((p, q, o))
    one = m((0, 1), (0, 1))  # i*i or ε*ε
    return name, not leaks, len(leaks), one, leaks[:1]


def wrap_mul(rel, n):
    def m(p, q):
        a, b = p
        c, d = q
        ev, er = rel(b, d)
        return ((a * c + ev) % n, (a * d + b * c + er) % n)
    return m


def main():
    print("=== i*i under four square-rules (host +/*) ===")
    for Vname, V in (("bits", BITS), ("Z5", Z5), ("pm3", tuple(range(-3, 4)))):
        print(f"  -- V={Vname} --")
        for name, rel in (("dual ε²=0", rel_dual), ("complex i²=-1", rel_complex),
                          ("split j²=+1", rel_split), ("idemp ε²=ε", rel_idemp)):
            n, ok, nleak, one, sample = scan(name, rel, V)
            print(f"     {name:<16} closed={ok} leaks={nleak}  unit*unit={one} {sample}")

    print()
    print("=== wrap Z/n : all four close; i*i folded ===")
    for n in (2, 3, 5):
        print(f"  Z/{n}")
        for name, rel in (("dual", rel_dual), ("complex", rel_complex),
                          ("split", rel_split), ("idemp", rel_idemp)):
            m = wrap_mul(rel, n)
            one = m((0, 1), (0, 1))
            print(f"     {name:<10} i*i = {one}")

    print()
    print("=== project 'real' : drop second slot ===")
    m = mul(rel_complex)
    z = m((2, 3), (1, 4))  # (2+3i)(1+4i) = 2-12 + (8+3)i = (-10, 11)
    print(f"  (2,3)*(1,4) = {z}")
    print(f"  π_real = {z[0]}  lost imag {z[1]}")
    print(f"  π_imag = {z[1]}  lost real {z[0]}")

    print()
    print("=== 'real' as pairs with second slot dead ===")
    m = mul(rel_complex)
    a, b = (5, 0), (3, 0)
    print(f"  (5,0)*(3,0) = {m(a,b)}  stays on imag=0")
    print(f"  (5,0)*(0,1) = {m((5,0),(0,1))}  5i")

    print()
    print("=== same pair type, dual vs complex at (1,1)*(1,1) ===")
    print(f"  dual    {mul(rel_dual)((1,1),(1,1))}")
    print(f"  complex {mul(rel_complex)((1,1),(1,1))}")
    print(f"  split   {mul(rel_split)((1,1),(1,1))}")
    print("  dual writes channel 2; complex writes value 0 and channel 2")
    print("  (1+1ε)² = 1+2ε; (1+i)² = 1+2i+i² = 0+2i")


if __name__ == "__main__":
    main()
