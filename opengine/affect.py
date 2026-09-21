#!/usr/bin/env python3
"""Prior affects: isolation, meets, adjoined letter, characteristic."""
from __future__ import annotations

from itertools import product


BITS = (0, 1)


def pairs(Vv=BITS, Vr=BITS):
    return [(v, r) for v in Vv for r in Vr]


def scan(chan, Vv=BITS, Vr=BITS):
    leaks = []
    table = {}
    for a, b in product(pairs(Vv, Vr), repeat=2):
        (v, r), (w, s) = a, b
        ov = v * w
        or_ = chan(v, r, w, s)
        table[(a, b)] = (ov, or_)
        if ov not in Vv or or_ not in Vr:
            leaks.append((a, b, (ov, or_)))
    return not leaks, leaks, table


# channel meets: which relational writes survive
MEETS = {
    "0":           lambda v, r, w, s: 0,
    "r":           lambda v, r, w, s: r,
    "s":           lambda v, r, w, s: s,
    "r+s":         lambda v, r, w, s: r + s,
    "r*s":         lambda v, r, w, s: r * s,
    "r*w":         lambda v, r, w, s: r * w,
    "v*s":         lambda v, r, w, s: v * s,
    "r*w+v*s":     lambda v, r, w, s: r * w + v * s,       # leibniz
    "r*w-v*s":     lambda v, r, w, s: r * w - v * s,
    "max(r,s)":    lambda v, r, w, s: max(r, s),
    "min(r,s)":    lambda v, r, w, s: min(r, s),
    "r^s":         lambda v, r, w, s: r ^ s,               # xor channels
    "r&s":         lambda v, r, w, s: r & s,
    "r|s":         lambda v, r, w, s: r | s,
    "r*w+v*s+r*s": lambda v, r, w, s: r * w + v * s + r * s,  # if ε²=ε or keep ε²
}


def adjoin_mul(rel_eps2):
    """(v + rε)(w + sε) with ε² = rel_eps2(r,s) contribution to value or channel."""
    def mul(a, b):
        (v, r), (w, s) = a, b
        # vw + (rw+vs)ε + rs ε²
        e2_v, e2_r = rel_eps2(r, s)
        return (v * w + e2_v, r * w + v * s + e2_r)
    return mul


def rel_nil(r, s):
    return (0, 0)          # ε² = 0  dual


def rel_idemp(r, s):
    return (0, r * s)      # ε² = ε  channel absorbs rs


def rel_real(r, s):
    return (r * s, 0)      # ε² = 1  value absorbs rs  (split-complex if -)


def rel_neg(r, s):
    return (-r * s, 0)     # ε² = -1  complex-shaped


def main():
    print("=== every meet on bits ===")
    for name, fn in MEETS.items():
        ok, leaks, _ = scan(fn)
        sample = leaks[0] if leaks else None
        print(f"  {name:<16} {'CLOSE' if ok else 'LEAK':<6} {'' if ok else sample}")

    print()
    print("=== adjoin ε with a relation, host +/* on bits ===")
    for name, rel in (("nil ε²=0", rel_nil), ("idemp ε²=ε", rel_idemp),
                      ("ε²=1", rel_real), ("ε²=-1", rel_neg)):
        mul = adjoin_mul(rel)
        leaks = []
        for a, b in product(pairs(), repeat=2):
            o = mul(a, b)
            if o[0] not in BITS or o[1] not in BITS:
                leaks.append((a, b, o))
        print(f"  {name:<14} {'CLOSE' if not leaks else 'LEAK'} nleak={len(leaks)} e.g. {leaks[:1]}")

    print()
    print("=== same relations with WRAP +/* on Z/2 ===")
    def wrap_adjoin(rel):
        def mul(a, b):
            (v, r), (w, s) = a, b
            ev, er = rel(r, s)
            return ((v * w + ev) % 2, (r * w + v * s + er) % 2)
        return mul
    for name, rel in (("nil", rel_nil), ("idemp", rel_idemp), ("ε²=1", rel_real), ("ε²=-1", rel_neg)):
        mul = wrap_adjoin(rel)
        leaks = [1 for a, b in product(pairs(), repeat=2) if any(x not in BITS for x in mul(a, b))]
        # compare (1,1)*(1,1)
        print(f"  wrap {name:<8} closed={not leaks}  1,1 * 1,1 = {mul((1,1),(1,1))}")

    print()
    print("=== characteristic: 2x on host vs wrap ===")
    for n in (2, 3, 5, 0):
        # 0 means host Z
        xx_host = (1 * 1, 1 * 1 + 1 * 1)
        if n == 0:
            print(f"  host     x^2 at (1,1) = {xx_host}   2x={2}")
        else:
            xx_w = ((1 * 1) % n, (1 * 1 + 1 * 1) % n)
            print(f"  wrap Z/{n} x^2 at (1,1) = {xx_w}   2x%n={2 % n}")

    print()
    print("=== invalid G in wrap frame: use host + anyway ===")
    def invalid_in_wrap(a, b):
        return (a[0] * b[0], a[1] * b[0] + a[0] * b[1])  # host
    leaks = []
    for a, b in product(pairs(), repeat=2):
        o = invalid_in_wrap(a, b)
        if o[0] not in BITS or o[1] not in BITS:
            leaks.append((a, b, o))
    print(f"  host-lei inside bit-frame leaks={len(leaks)} {leaks}")

    print()
    print("=== invent a CLOSED rate-like op on bits: AND-channel + AND-value ===")
    def and_pair(a, b):
        return (a[0] & b[0], a[1] & b[1])
    def xor_pair(a, b):
        return (a[0] ^ b[0], a[1] ^ b[1])
    for name, fn in (("and_pair", and_pair), ("xor_pair", xor_pair)):
        leaks = [fn(a, b) for a, b in product(pairs(), repeat=2) if fn(a, b)[0] not in BITS or fn(a, b)[1] not in BITS]
        print(f"  {name} closed={not leaks}  (1,1)*(1,1)={fn((1,1),(1,1))}  (1,1)*(1,0)={fn((1,1),(1,0))}")

    print()
    print("=== isolation is the prior write ===")
    # isolate: Vv -> Vv x Vr   seed must be in Vr
    for seed, Vr in ((1, BITS), (2, BITS), (1, (0, 1, 2)), (2, (0, 1, 2))):
        lands = seed in Vr
        print(f"  isolate(*, seed={seed}) into Vr={Vr}  lands={lands}")


if __name__ == "__main__":
    main()
