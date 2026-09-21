#!/usr/bin/env python3
"""Pivot: which slot leaks? Which finite hosts close? Rate writes a fourth alphabet."""
from __future__ import annotations

from fractions import Fraction as F
from itertools import product


def leibniz(a, b):
    (v, r), (w, s) = a, b
    return (v * w, r * w + v * s)


def classify_leaks(Vv, Vr, mix=leibniz):
    Lv = Lr = both = 0
    n = 0
    samples = {"v": [], "r": [], "both": []}
    for a, b in product(((v, r) for v in Vv for r in Vr), repeat=2):
        n += 1
        ov, or_ = mix(a, b)
        bad_v = ov not in Vv
        bad_r = or_ not in Vr
        if bad_v and bad_r:
            both += 1
            if len(samples["both"]) < 2:
                samples["both"].append((a, b, (ov, or_)))
        elif bad_v:
            Lv += 1
            if len(samples["v"]) < 2:
                samples["v"].append((a, b, (ov, or_)))
        elif bad_r:
            Lr += 1
            if len(samples["r"]) < 2:
                samples["r"].append((a, b, (ov, or_)))
    return n, Lv, Lr, both, samples


def wrap_leibniz(n):
    def mix(a, b):
        (v, r), (w, s) = a, b
        return ((v * w) % n, (r * w + v * s) % n)

    return mix


def main():
    print("=== leak source split (host +/*) ===")
    hosts = {
        "bits/bits": ((0, 1), (0, 1)),
        "bits/Z4": ((0, 1), (0, 1, 2, 3)),
        "Z4/bits": ((0, 1, 2, 3), (0, 1)),
        "Z4/Z4": ((0, 1, 2, 3), (0, 1, 2, 3)),
        "tri/tri": ((0, F(1, 2), 1), (0, F(1, 2), 1)),
        "bits/Z": ((0, 1), tuple(range(-4, 5))),
        "Z/Z": (tuple(range(-2, 3)), tuple(range(-2, 3))),
    }
    for name, (Vv, Vr) in hosts.items():
        n, Lv, Lr, both, s = classify_leaks(Vv, Vr)
        print(f"  {name:<12} n={n:<5} leak_v={Lv:<4} leak_r={Lr:<4} both={both:<4} "
              f"closed={Lv+Lr+both==0}")
        if Lr and s["r"]:
            print(f"               r-sample {s['r'][0]}")
        if Lv and s["v"]:
            print(f"               v-sample {s['v'][0]}")

    print()
    print("=== wrap BOTH slots (Z/n arithmetic on v and r) ===")
    for n in (2, 3, 4, 5):
        V = tuple(range(n))
        mix = wrap_leibniz(n)
        leaks = []
        for a, b in product(((v, r) for v in V for r in V), repeat=2):
            o = mix(a, b)
            if o[0] not in V or o[1] not in V:
                leaks.append((a, b, o))
        print(f"  Z/{n} wrap-leibniz closed={not leaks} n={n*n*n*n}")

    print()
    print("=== smallest closed hosts for HOST leibniz ===")
    # Vv={0}: product 0, channel r*0+0*s=0. Dead.
    # Vv={1}: product 1, channel r+s. Need (Vr,+) closed.
    # Vv={0,1}: product closed, channel is {0,s,r,r+s}. Need (Vr,+) closed.
    for label, Vv, Vr in [
        ("dead values {0}", (0,), (0, 1, 2)),
        ("unit values {1}, Vr bits", (1,), (0, 1)),
        ("unit values {1}, Vr Z+", (1,), tuple(range(0, 8))),
        ("bits, Vr={0} dead chan", (0, 1), (0,)),
        ("bits, Vr={0,1}", (0, 1), (0, 1)),
    ]:
        n, Lv, Lr, both, _ = classify_leaks(Vv, Vr)
        print(f"  {label:<28} closed={Lv+Lr+both==0} Lv={Lv} Lr={Lr} both={both}")

    print()
    print("=== theorem check: 1 in Vv => Vr must be +closed for leibniz ===")
    for m in (2, 3, 4, 5, 6):
        Vv = (0, 1)
        Vr = tuple(range(m))  # {0..m-1} not +closed
        n, Lv, Lr, both, _ = classify_leaks(Vv, Vr)
        print(f"  Vv=bits Vr=0..{m-1}  +closed={all((a+b) in Vr for a,b in product(Vr,Vr))} "
              f"leibniz_closed={Lv+Lr+both==0} Lr={Lr}")

    print()
    print("=== rate alphabet Vq = {r/s : s!=0} vs Vr ===")
    for name, Vr in [("bits", (0, 1)), ("Z3", (0, 1, 2)), ("Z5", tuple(range(5))),
                     ("pm3", tuple(range(-3, 4)))]:
        qs = set()
        for r, s in product(Vr, Vr):
            if s == 0:
                continue
            qs.add(r / s if not isinstance(r, int) else F(r, s))
        extra = [q for q in qs if q not in Vr]
        print(f"  Vr={name:<4} |Vq|={len(qs):<3} Vq-Vr={extra[:8]}")

    print()
    print("=== unary D then mix: collapse cost ===")
    # grow Vr so more channels exist, dump into Vv=bits via D
    Vv, Vr = (0, 1), (0, 1, 2)
    stranded = [(v, r) for v in Vv for r in Vr if r not in Vv]
    print(f"  D:(v,r)->(r,0) stranded when Vr not subset Vv: {stranded}")
    print("  so: grow Vr to host mix => D is no longer a map into Vv x Vr")

    print()
    print("=== load as third alphabet: vent L -> kappa L and (1-k)L/n ===")
    for Vl in ((0, 1, 2, 3, 4, 5, 12), (0, F(1, 2), 1), tuple(range(0, 20))):
        kappa, nch = F(2, 5), 3
        leaks = []
        for L in Vl:
            if L == 0:
                continue
            kept = kappa * L
            child = (1 - kappa) * L / nch
            if kept not in Vl or child not in Vl:
                leaks.append((L, kept, child))
        print(f"  |Vl|={len(Vl):<3} vent_closed={not leaks} sample={leaks[:2]}")


if __name__ == "__main__":
    main()
