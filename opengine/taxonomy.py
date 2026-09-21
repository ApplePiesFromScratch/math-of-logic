#!/usr/bin/env python3
"""Taxonomy + evolution: same G across V. Print close/leak/split."""
from __future__ import annotations

from fractions import Fraction as F
from itertools import product

from engine import (
    AND_min,
    AND_prod,
    Engine,
    NOT,
    OR_max,
    V2,
    V3,
    V4,
    XOR,
    Z4,
    Z5,
    Z6,
    add_channels,
    leibniz,
    luk_and,
    pair_engine,
    quot_on,
    signature,
    split_report,
    trop_add,
    trop_mul,
    value_only_mix,
    wrap_add,
    wrap_mul,
)


def row(scan):
    leaks = scan["leaks"][:3]
    leak_s = "" if scan["closed"] else f"  leak={leaks}"
    props = signature(scan)
    return f"{scan['carrier']:<8} {scan['label']:<16} {'CLOSE' if scan['closed'] else 'LEAK ':<6} {props}{leak_s}"


def main():
    print("OPERATOR ENGINE — close / leak / split")
    print()

    print("== logic G on growing V ==")
    for eng in (V2, V3, V4):
        for name, op in (
            ("AND_min", AND_min),
            ("AND_prod", AND_prod),
            ("OR_max", OR_max),
            ("XOR_mod2", XOR),
            ("luk_and", luk_and),
        ):
            print(" ", row(eng.scan_binary(op, name)))
        print(" ", row(eng.scan_unary(NOT, "NOT_1minus")))
        print()

    print("== split: min vs prod ==")
    for small, big in ((V2, V3), (V3, V4)):
        r = split_report(small, big, AND_min, AND_prod, "min", "prod")
        print(
            f"  {r['small']}->{r['big']}: coincide_small={r['coincide_on_small']} "
            f"coincide_big={r['coincide_on_big']} split={r['split']} "
            f"prod_closed_big={r['b_closed_big']} leaks={r['b_leaks'][:2]}"
        )
    print()

    print("== wrap arithmetic ==")
    for n, eng in ((4, Z4), (5, Z5), (6, Z6)):
        print(" ", row(eng.scan_binary(wrap_add(n), f"+_mod{n}")))
        print(" ", row(eng.scan_binary(wrap_mul(n), f"*_mod{n}")))
    print()

    print("== quot on scalars (pole is refuse, not Inf) ==")
    for eng in (V2, V3, Z5):
        s = eng.scan_binary(quot_on(0), "quot")
        print(" ", row(s))
    print()

    print("== tropical on {0,1,2,3} ==")
    T = Engine("T4", (0, 1, 2, 3))
    print(" ", row(T.scan_binary(trop_add, "trop+")))
    print(" ", row(T.scan_binary(trop_mul, "trop*")))
    tmul = T.scan_binary(trop_mul, "trop*")
    print("   trop* closed", tmul["closed"], "leaks", tmul["leaks"][:4])
    print()

    print("== pair mix on tiny scalar V ==")
    P2 = pair_engine((0, 1), "pairs-V2")
    P3sc = pair_engine((0, 1), "pairs-V2")  # keep small; V3 scalars explode 9 pairs
    for name, op in (("leibniz", leibniz), ("value_only", value_only_mix), ("add_chan", add_channels)):
        print(" ", row(P2.scan_binary(op, name)))
    print()

    print("== protocol-shaped V: states {off, on, fault} ==")
    OFF, ON, FAULT = "off", "on", "fault"
    S = Engine("proto3", (OFF, ON, FAULT))

    def and_ok(a, b):
        # both must be on
        if FAULT in (a, b):
            return FAULT
        if a == ON and b == ON:
            return ON
        return OFF

    def and_ignore_fault(a, b):
        # bug: fault treated as off, then AND with on yields off — hides fault
        aa = OFF if a == FAULT else a
        bb = OFF if b == FAULT else b
        return ON if aa == ON and bb == ON else OFF

    def join(a, b):
        if FAULT in (a, b):
            return FAULT
        if ON in (a, b):
            return ON
        return OFF

    for name, op in (("and_ok", and_ok), ("and_mask_fault", and_ignore_fault), ("join", join)):
        print(" ", row(S.scan_binary(op, name)))
    print("  mask_fault hides FAULT:", and_ignore_fault(FAULT, ON) == OFF)
    print()

    print("== money cents: V = whole cents; 1/2-cent G leaks ==")
    cents = Engine("cents0-4", (0, 1, 2, 3, 4))

    def split_half(a, b):
        return (a + b) / 2

    print(" ", row(cents.scan_binary(split_half, "avg")))
    print(" ", row(cents.scan_binary(lambda a, b: (a + b) // 2, "avg_floor")))
    print()

    print("== permission bits grow to maybe ==")
    # deny=0 allow=1 maybe=1/2
    def allow_min(a, b):
        return min(a, b)

    print("  V2 allow-AND", signature(V2.scan_binary(allow_min, "min")))
    print("  V3 allow-AND", signature(V3.scan_binary(allow_min, "min")))
    print("  V3 product-AND", "CLOSE" if V3.scan_binary(AND_prod, "p")["closed"] else "LEAK")
    print()

    print("== evolution table: AND-shaped ==")
    print(f"  {'V':<8} {'min':<8} {'prod':<8} {'luk':<8} {'xor':<8}")
    for eng in (V2, V3, V4):
        cells = []
        for op in (AND_min, AND_prod, luk_and, XOR):
            cells.append("CLOSE" if eng.scan_binary(op, "x")["closed"] else "LEAK")
        print(f"  {eng.name:<8} " + " ".join(f"{c:<8}" for c in cells))

    print()
    print("Use: if you add a value to V, rerun scan_binary. LEAK means")
    print("the G is not an operation of that system. Grow V or change G.")


if __name__ == "__main__":
    main()
