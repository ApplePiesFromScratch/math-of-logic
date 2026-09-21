#!/usr/bin/env python3
"""Test suite for typed slots: Vv, Vr, Vq, Vt, Vl."""
from __future__ import annotations

from fractions import Fraction as F
from itertools import product

CHECKS = []


def check(name, cond):
    CHECKS.append((name, bool(cond)))


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
        raise ZeroDivisionError
    return (F(v) / F(w), (F(r) * F(w) - F(v) * F(s)) / (F(w) * F(w)))


def jet_mul(a, b):
    v, r, t = a
    w, s, u = b
    return (v * w, r * w + v * s, t * w + 2 * r * s + v * u)


def wrap_jet(n):
    def m(a, b):
        v, r, t = a
        w, s, u = b
        return (
            (v * w) % n,
            (r * w + v * s) % n,
            (t * w + 2 * r * s + v * u) % n,
        )

    return m


def closed_lei(Vv, Vr):
    for a, b in product(((v, r) for v in Vv for r in Vr), repeat=2):
        o = host_lei(a, b)
        if o[0] not in Vv or o[1] not in Vr:
            return False
    return True


def n_leaks_r(Vv, Vr):
    n = 0
    for a, b in product(((v, r) for v in Vv for r in Vr), repeat=2):
        o = host_lei(a, b)
        if o[0] in Vv and o[1] not in Vr:
            n += 1
    return n


# bits host leibniz
check("bits_lei_leaks_once", not closed_lei((0, 1), (0, 1)))
check("bits_lei_the_leak", host_lei((1, 1), (1, 1)) == (1, 2))
check("bits_dead_chan_closed", closed_lei((0, 1), (0,)))
check("zero_values_closed", closed_lei((0,), (0, 1, 2)))

# triangular Lr
for m in range(2, 8):
    Lr = n_leaks_r((0, 1), tuple(range(m)))
    check(f"triangular_m{m}", Lr == m * (m - 1) // 2)

# wrap leibniz closed
for n in (2, 3, 4, 5, 7):
    V = tuple(range(n))
    wl = wrap_lei(n)
    ok = all(
        wl(a, b)[0] in V and wl(a, b)[1] in V
        for a, b in product(((v, r) for v in V for r in V), repeat=2)
    )
    check(f"wrap_lei_Z{n}", ok)

# wrap vs host: Z/2 differs on exactly one pair
n = 2
V = range(2)
wl = wrap_lei(2)
differ = [
    (a, b)
    for a, b in product(((v, r) for v in V for r in V), repeat=2)
    if host_lei(a, b) != wl(a, b)
]
check("z2_host_wrap_differ_1", len(differ) == 1)
check("z2_the_fold", host_lei((1, 1), (1, 1)) == (1, 2) and wl((1, 1), (1, 1)) == (1, 0))

# gauge
check("gauge_k1_bits", all((v, r * 1)[1] in (0, 1) for v in (0, 1) for r in (0, 1)))
check("gauge_k2_bits_leaks", (1, 1 * 2)[1] not in (0, 1))

# D lands iff Vr subset Vv
check("D_bits_bits", all(r in (0, 1) for r in (0, 1)))
check("D_bits_Z3_strands", 2 not in (0, 1))
check("D_Z3_bits_lands", all(r in (0, 1, 2) for r in (0, 1)))

# host quot writes minus on bits
check("quot_bits_writes_minus", host_quot((1, 0), (1, 1)) == (F(1), F(-1)))

# wrap quot lands when inverse exists
def wrap_inv(w, n):
    for k in range(n):
        if (w * k) % n == 1:
            return k
    return None


check("z5_all_nonzero_invert", all(wrap_inv(s, 5) is not None for s in range(1, 5)))
check("z4_2_no_inv", wrap_inv(2, 4) is None)

# jet
check("jet_bits_leaks", jet_mul((0, 1, 0), (0, 1, 0)) == (0, 0, 2))
for n in (2, 3, 5):
    V = range(n)
    wj = wrap_jet(n)
    js = [(v, r, t) for v in V for r in V for t in V]
    ok = all(all(x in V for x in wj(a, b)) for a, b in product(js, js))
    check(f"wrap_jet_Z{n}", ok)

# compose stacks
check("compose_seed0_stays", host_lei(host_lei((1, 0), (1, 0)), (1, 0)) == (1, 0))
check("compose_seed1_stacks", host_lei(host_lei((1, 1), (1, 1)), (1, 1)) == (1, 3))

# Vq host division
qs = {F(r, s) for r in range(5) for s in range(1, 5)}
check("z5_host_rate_grows_Q", F(1, 2) in qs and F(1, 2) not in range(5))

# vent
Vl = tuple(range(13))
check("vent_keep_all", all((1 * L) in Vl for L in Vl))
check("vent_workbook_leaks", (F(2, 5) * 1) not in Vl)

# min/max chan close on bits (no add)
def max_chan(a, b):
    (v, r), (w, s) = a, b
    return (v * w, max(r, s))


bits_p = [(v, r) for v in (0, 1) for r in (0, 1)]
check(
    "max_chan_bits_closed",
    all(max_chan(a, b)[0] in (0, 1) and max_chan(a, b)[1] in (0, 1) for a, b in product(bits_p, bits_p)),
)


if __name__ == "__main__":
    failed = [n for n, c in CHECKS if not c]
    for n, c in CHECKS:
        print(f"  {'PASS' if c else 'FAIL'} {n}")
    print(f"{sum(c for _, c in CHECKS)}/{len(CHECKS)}")
    print("ALL PASS" if not failed else "FAILED " + str(failed))
    raise SystemExit(1 if failed else 0)
