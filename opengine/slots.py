#!/usr/bin/env python3
"""Three alphabets: V_value, V_channel, V_load.

A pair (v, r) is not one V. Mix writes r using v and r.
Score when that write lands.
"""
from __future__ import annotations

from fractions import Fraction as F
from itertools import product


def pairs(Vv, Vr):
    return [(v, r) for v in Vv for r in Vr]


def in_pair(p, Vv, Vr):
    v, r = p
    return v in Vv and r in Vr


def scan_mix(name, mix, Vv, Vr):
    leaks = []
    n = 0
    for a, b in product(pairs(Vv, Vr), repeat=2):
        n += 1
        out = mix(*a) if False else mix(a, b)
        if not in_pair(out, Vv, Vr):
            leaks.append((a, b, out))
    return {
        "name": name,
        "Vv": Vv,
        "Vr": Vr,
        "n": n,
        "closed": not leaks,
        "n_leaks": len(leaks),
        "leaks": leaks[:6],
    }


def leibniz(a, b):
    (v, r), (w, s) = a, b
    return (v * w, r * w + v * s)


def value_only(a, b):
    (v, r), (w, s) = a, b
    return (v * w, 0)


def add_chan(a, b):
    (v, r), (w, s) = a, b
    return (v * w, r + s)


def max_chan(a, b):
    (v, r), (w, s) = a, b
    return (v * w, max(r, s))


def min_chan(a, b):
    (v, r), (w, s) = a, b
    return (v * w, min(r, s))


def trop_chan(a, b):
    (v, r), (w, s) = a, b
    return (min(v, w), r + s)


def gauge(p, k):
    v, r = p
    return (v, r * k)


def unary_D(p):
    v, r = p
    return (r, 0)


def rate_ok(p, q):
    _, r = p
    _, s = q
    if s == 0:
        return "THETA"
    return r / s


BITS = (0, 1)
TRI = (0, F(1, 2), 1)
Z3 = (0, 1, 2)
Z4 = (0, 1, 2, 3)
Z = tuple(range(-3, 4))
Qsmall = (0, 1, -1, 2, F(1, 2), F(3, 2), 3)


def report(title, rows):
    print(title)
    for r in rows:
        flag = "CLOSE" if r["closed"] else f"LEAK x{r['n_leaks']}"
        sample = ""
        if r["leaks"]:
            a, b, o = r["leaks"][0]
            sample = f"  e.g. {a}*{b}->{o}"
        print(f"  {r['name']:<12} Vv={len(r['Vv'])} Vr={len(r['Vr'])} n={r['n']:<5} {flag}{sample}")


def main():
    mixes = [
        ("leibniz", leibniz),
        ("value_only", value_only),
        ("add_chan", add_chan),
        ("max_chan", max_chan),
        ("min_chan", min_chan),
    ]

    print("=== same alphabet for v and r ===")
    rows = []
    for V in (BITS, TRI, Z3, Z4, Z):
        for name, mix in mixes:
            rows.append(scan_mix(name, mix, V, V))
    report("Vv = Vr", rows)

    print()
    print("=== grow only Vr (values stay bits) ===")
    rows = []
    for Vr in (BITS, Z3, Z4, Z, Qsmall):
        rows.append(scan_mix("leibniz", leibniz, BITS, Vr))
    report("Vv=bits Vr grows", rows)

    print()
    print("=== grow only Vv (channel stays bits) ===")
    rows = []
    for Vv in (BITS, Z3, Z4, Z):
        rows.append(scan_mix("leibniz", leibniz, Vv, BITS))
    report("Vr=bits Vv grows", rows)

    print()
    print("=== gauge: (v,r) -> (v, r*k), k in K ===")
    for Vr, K in ((BITS, BITS), (BITS, Z3), (Z3, Z3), (Z, Z)):
        leaks = []
        for v, r, k in product((0, 1) if Vr is BITS else Vr[:4], Vr, K):
            out = gauge((v, r), k)
            if out[1] not in Vr:
                leaks.append(((v, r), k, out))
        print(f"  Vr={Vr[:6]}... K={K[:6]}... gauge_closed={not leaks} nleak={len(leaks)} {leaks[:2]}")

    print()
    print("=== unary D: (v,r) -> (r, 0)  does it land in Vv x Vr? ===")
    for Vv, Vr in ((BITS, BITS), (BITS, Z3), (Z3, BITS), (Z3, Z3)):
        leaks = [(v, r) for v in Vv for r in Vr if r not in Vv]
        print(f"  Vv={Vv} Vr={Vr} D_lands={not leaks} stranded_r={leaks[:4]}")

    print()
    print("=== rate writes a scalar: which alphabet? ===")
    for Vr in (BITS, Z3, Z):
        bad = []
        goods = []
        for r, s in product(Vr, Vr):
            if s == 0:
                continue
            q = r / s if s else None
            # r/s may be Fraction
            if q not in Vr and q not in BITS:
                bad.append((r, s, q))
            else:
                goods.append((r, s, q))
        print(f"  Vr={Vr} rate_in_Vr_or_bits leaks={len(bad)} sample={bad[:3]}")


if __name__ == "__main__":
    main()
