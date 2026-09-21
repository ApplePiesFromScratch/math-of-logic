#!/usr/bin/env python3
"""Deeper: composition, quotient slot, jets, wrap vs host agreement window."""
from __future__ import annotations

from fractions import Fraction as F
from itertools import product


def host_lei(a, b):
    (v, r), (w, s) = a, b
    return (v * w, r * w + v * s)


def wrap_lei(n):
    def m(a, b):
        (v, r), (w, s) = a, b
        return ((v * w) % n, (r * w + v * s) % n)

    return m


def host_quot(a, b):
    (v, r), (w, s) = a, b
    if w == 0:
        return "THETA"
    return (v / w, (r * w - v * s) / (w * w))


def wrap_quot(n):
    def inv(w):
        for k in range(n):
            if (w * k) % n == 1:
                return k
        return None

    def m(a, b):
        (v, r), (w, s) = a, b
        i = inv(w % n)
        if i is None:
            return "THETA"
        qv = (v * i) % n
        # r/w - v s / w^2
        num = (r * w - v * s) % n
        i2 = inv((w * w) % n)
        if i2 is None:
            return "THETA"
        qr = (num * i2) % n
        return (qv, qr)

    return m


def jet_mul(a, b):
    v, r, t = a
    w, s, u = b
    return (v * w, r * w + v * s, t * w + 2 * r * s + v * u)


def main():
    print("=== wrap vs host agreement window on Z/n pairs ===")
    for n in (2, 3, 4, 5, 7):
        V = range(n)
        wl = wrap_lei(n)
        agree = differ = 0
        samples = []
        for a, b in product(((v, r) for v in V for r in V), repeat=2):
            h = host_lei(a, b)
            w = wl(a, b)
            hw = (h[0] % n, h[1] % n)
            if h[0] == w[0] and h[1] == w[1]:
                agree += 1
            else:
                differ += 1
                if len(samples) < 2:
                    samples.append((a, b, h, w))
        print(f"  n={n} agree={agree} differ={differ}  differ_sample={samples[:1]}")

    print()
    print("=== host quot leak sources on bits and Z5 ===")
    for name, Vv, Vr in (("bits", (0, 1), (0, 1)), ("Z5", tuple(range(5)), tuple(range(5)))):
        theta = leak_v = leak_r = ok = 0
        sample = None
        for a, b in product(((v, r) for v in Vv for r in Vr), repeat=2):
            o = host_quot(a, b)
            if o == "THETA":
                theta += 1
                continue
            ov, or_ = o
            badv = ov not in Vv
            badr = or_ not in Vr
            if badv or badr:
                leak_v += badv
                leak_r += badr
                if sample is None:
                    sample = (a, b, o)
            else:
                ok += 1
        print(f"  {name} ok={ok} theta={theta} leak_v={leak_v} leak_r={leak_r} e.g. {sample}")

    print()
    print("=== wrap quot on Z/n ===")
    for n in (2, 3, 4, 5, 7):
        V = range(n)
        wq = wrap_quot(n)
        theta = ok = 0
        for a, b in product(((v, r) for v in V for r in V), repeat=2):
            o = wq(a, b)
            if o == "THETA":
                theta += 1
            else:
                ok += 1
                assert o[0] in V and o[1] in V
        print(f"  Z/{n} wrap-quot lands={ok} theta={theta} total={n**4}")

    print()
    print("=== jet third slot V_t on bits ===")
    bits = (0, 1)
    jets = [(v, r, t) for v in bits for r in bits for t in bits]
    leaks = []
    for a, b in product(jets, repeat=2):
        o = jet_mul(a, b)
        if any(x not in bits for x in o):
            leaks.append((a, b, o))
    print(f"  bits^3 n={len(jets)**2} leaks={len(leaks)} e.g. {leaks[0] if leaks else None}")
    # wrap jet
    def wrap_jet(n):
        def m(a, b):
            v, r, t = a
            w, s, u = b
            return ((v * w) % n, (r * w + v * s) % n, (t * w + 2 * r * s + v * u) % n)

        return m

    for n in (2, 3, 5):
        V = range(n)
        js = [(v, r, t) for v in V for r in V for t in V]
        wj = wrap_jet(n)
        bad = sum(1 for a, b in product(js, js) if any(x not in V for x in wj(a, b)))
        print(f"  wrap-jet Z/{n} closed={bad==0} n={len(js)**2}")

    print()
    print("=== compose two leibniz on bits: does leak stack? ===")
    bits = (0, 1)
    P = [(v, r) for v in bits for r in bits]
    # (x*x)*x on each seed
    for seed in bits:
        x = (1, seed) if True else None
        # use v=1 to stay in bits for value
        x = (1, seed)
        xx = host_lei(x, x)
        xxx = host_lei(xx, x)
        print(f"  seed={seed} x*x={xx} (x*x)*x={xxx}  xx_in={xx[1] in bits} xxx_in={xxx[1] in bits}")

    print()
    print("=== constants Vr={0} is a subalgebra of host leibniz ===")
    Vv = (0, 1, 2, 3)
    Vr = (0,)
    leaks = 0
    for a, b in product(((v, 0) for v in Vv), repeat=2):
        o = host_lei(a, b)
        if o[1] != 0 or o[0] not in Vv:
            leaks += 1
    print(f"  Vv=0..3 Vr={{0}} value-closed? {leaks} leaks (expect value 2*2=4 leak)")
    Vv = (0, 1)
    leaks = 0
    for a, b in product(((v, 0) for v in Vv), repeat=2):
        o = host_lei(a, b)
        if o[1] != 0 or o[0] not in Vv:
            leaks += 1
    print(f"  Vv=bits Vr={{0}} closed={leaks==0}")


if __name__ == "__main__":
    main()
