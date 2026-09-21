#!/usr/bin/env python3
"""advanced_verify.py: one runner, one kernel, paid cuts.

Extension of verify / extended_verified. Stdlib only.
Run: python3 advanced_verify.py
"""
from __future__ import annotations

from fractions import Fraction as F
from itertools import permutations, product
from math import comb


# ── kernel ────────────────────────────────────────────────────────────


class Theta(Exception):
    pass


class LeavesV(Exception):
    pass


def Q(x):
    if isinstance(x, bool):
        raise LeavesV("bool is not Q")
    if isinstance(x, float):
        if x != x:
            raise LeavesV("NaN float unlistable")
        raise LeavesV("float unlistable; use Fraction or int")
    try:
        return F(x)
    except Exception as e:
        raise LeavesV(f"not in Q: {type(x).__name__}") from e


class Reading:
    __slots__ = ("v", "r")

    def __init__(self, v, r):
        self.v, self.r = Q(v), Q(r)

    def __repr__(self):
        return f"Reading({self.v}, {self.r})"

    def __eq__(self, o):
        return isinstance(o, Reading) and self.v == o.v and self.r == o.r

    def __add__(self, o):
        o = o if isinstance(o, Reading) else Reading(o, 0)
        return Reading(self.v + o.v, self.r + o.r)

    def __sub__(self, o):
        o = o if isinstance(o, Reading) else Reading(o, 0)
        return Reading(self.v - o.v, self.r - o.r)

    def __mul__(self, o):
        o = o if isinstance(o, Reading) else Reading(o, 0)
        return Reading(self.v * o.v, self.r * o.v + self.v * o.r)

    def __truediv__(self, o):
        o = o if isinstance(o, Reading) else Reading(o, 0)
        if o.v == 0:
            raise Theta("quot: v=0")
        return Reading(self.v / o.v, (self.r * o.v - self.v * o.r) / (o.v * o.v))

    def __pow__(self, n):
        if not isinstance(n, int) or n < 0:
            raise LeavesV("pow: n must be int >= 0")
        out = Reading(1, 0)
        for _ in range(n):
            out = out * self
        return out

    def __neg__(self):
        return Reading(-self.v, -self.r)

    def __rmul__(self, o):
        return Reading(o, 0) * self

    def __radd__(self, o):
        return Reading(o, 0) + self


def isolate(value, seed=1):
    return Reading(value, seed)


def rate(top, bottom):
    if bottom.r == 0:
        raise Theta("rate: isolation r=0")
    return top.r / bottom.r


def certify(fn, at, values=None, seeds=None):
    if values is None:
        values = (at,)
    if seeds is None:
        seeds = (1, 2, F(1, 2), 10, -1)
    if not values or not seeds:
        return {"ok": False, "gauge_ok": False, "n": 0, "reason": "empty grid"}
    hits = []
    x0 = isolate(at, 1)
    want = rate(fn(x0), x0)
    for v in values:
        for s in seeds:
            x = isolate(v, s)
            hits.append(rate(fn(x), x) == rate(fn(isolate(v, 1)), isolate(v, 1)))
    return {"ok": all(hits), "gauge_ok": all(hits), "n": len(hits), "value": want}


# ── runner ────────────────────────────────────────────────────────────

CHECKS = []


def check(name, cond, tier="FORCED"):
    CHECKS.append((name, bool(cond), tier))


def raises(ex, fn):
    try:
        fn()
        return False
    except ex:
        return True


# ── 0 kernel ──────────────────────────────────────────────────────────

x = isolate(3)
check("k_rate_x2", rate(x * x, x) == 6)
check("k_gauge_seed2", rate(isolate(3, 2) ** 2, isolate(3, 2)) == 6)
check(
    "k_gauge_seeds",
    all(rate(isolate(3, k) ** 2, isolate(3, k)) == 6 for k in (1, 2, F(1, 2), 10, F(1, 3), -1, F(7, 9))),
)
check("k_zero_over_zero_channels", rate(isolate(0, 6), isolate(0, 1)) == 6)
check("k_theta_dead_isolator", raises(Theta, lambda: rate(x, isolate(3, 0))))
check("k_theta_value_zero", raises(Theta, lambda: isolate(3) / isolate(0)))
check("k_leavesv_neg_pow", raises(LeavesV, lambda: isolate(3) ** -1))
check("k_leavesv_bool", raises(LeavesV, lambda: isolate(True)))
check("k_leavesv_float", raises(LeavesV, lambda: isolate(3.0)))
check("k_leavesv_nan", raises(LeavesV, lambda: isolate(float("nan"))))
check("k_rate_self", rate(x, x) == 1)
c = certify(lambda z: z ** 3 + 2 * z, at=3, values=(1, 2, 3, 4), seeds=(1, 2, F(1, 2), 10))
check("k_certify_32", c["ok"] and c["n"] == 16 and c["value"] == 29)
check("k_certify_empty", certify(lambda z: z, at=1, values=(), seeds=())["ok"] is False)


# ── 1 single-var ──────────────────────────────────────────────────────

x = isolate(3)
f, g = x * x, x ** 3
check("c1_leibniz_405", rate(f * g, x) == 405)
check("c1_prod_rates_162", rate(f, x) * rate(g, x) == 162)
check("c1_prod_rates_not_leibniz", rate(f, x) * rate(g, x) != rate(f * g, x))
x = isolate(2)
yv, w = x * x, (x * x) ** 3
check("c1_chain_192", rate(w, x) == 192)
check("c1_chain_cancel", rate(w, yv) * rate(yv, x) == rate(w, x))
check("c1_isolate_output", rate(x, w) == F(1, 192))
check("c2_inverse", rate(x, yv) * rate(yv, x) == 1)


# ── 2 implicit / related / parametric ─────────────────────────────────

X, Y = isolate(3, 1), isolate(4, F(-3, 4))
check("c3_constraint_dead", rate(X * X + Y * Y, X) == 0)
check("c3_yprime", Y.r == F(-3, 4))
check("c3_related_seed2", -(isolate(3, 2).v * isolate(3, 2).r) / 4 == F(-3, 2))
t = isolate(2)
check("c4_parametric", rate(t ** 3, t) / rate(t * t, t) == 3)
t5 = isolate(5)
check("c4_cross", rate(t5 ** 3, t5 * t5) == rate(t5 ** 3, t5) / rate(t5 * t5, t5))


# ── 3 opt / lhopital / collision ──────────────────────────────────────

z = isolate(0)
check("c5_opt_dead", rate(z * z, z) == 0)
num, den = isolate(1) ** 2 - 1, isolate(1) - 1
check("c5_lhop_theta", raises(Theta, lambda: num / den))
check("c5_lhop_channels", rate(num, den) == 2)
a = isolate(3, 1) * isolate(3, 1)
b = isolate(3, 2) * 3
check("c5_collision_pair", a == b and a.v == 9 and a.r == 6)


# ── 4 integral / series / fd / jet ────────────────────────────────────

h_ = F(1, 4)
riemann_mid = sum(((i + F(1, 2)) * h_) ** 2 * h_ for i in range(4))
check("c6_riemann_21_64", riemann_mid == F(21, 64))
check("c6_riemann_leftover", F(1, 3) - riemann_mid == F(1, 192))


def running_mid(fn, a, xv, n):
    if xv == a:
        return F(0)
    w = (xv - a) / n
    tot = F(0)
    for i in range(n):
        tot += fn(a + w * i + w / 2) * w
    return tot


ftc_ok = all(
    running_mid(lambda t: F(2) * t, F(0), xv, 1) == (isolate(xv) ** 2).v
    and rate(isolate(xv) ** 2, isolate(xv)) == F(2) * xv
    for xv in (F(1), F(2), F(3), F(5))
)
check("c6_ftc_linear_mid_n1", ftc_ok)

t_half = isolate(F(1, 2))
acc = isolate(0, 0)
for k in range(6):
    acc = acc + t_half ** k
check("c7_geom_63_32", acc.v == F(63, 32))
check("c7_geom_leftover", F(2) - acc.v == F(1, 32))


def fd(fn, xv, h):
    return (fn(xv + h) - fn(xv)) / h


check(
    "c13_fd_leftover_is_h",
    all(fd(lambda t: t * t, xv, h) - F(2) * xv == h for xv, h in ((F(2), F(1)), (F(3), F(1, 2)), (F(5), F(1, 10)))),
)
check("c13_fd_exact_deg1", fd(lambda t: t, F(3), F(1, 2)) - 1 == 0)


def jet(v, r=1, r2=0):
    return (F(v), F(r), F(r2))


def mul_j(a, b):
    return (a[0] * b[0], a[1] * b[0] + a[0] * b[1], a[2] * b[0] + 2 * a[1] * b[1] + a[0] * b[2])


def pow_j(xv, n):
    out = jet(1, 0, 0)
    for _ in range(n):
        out = mul_j(out, xv)
    return out


j3 = pow_j(jet(2, 1, 0), 3)
j4 = pow_j(jet(2, 1, 0), 4)
st4 = (F(2 + 1 / 2) ** 4 - 2 * F(2) ** 4 + F(2 - 1 / 2) ** 4) / (F(1, 2) ** 2)
check("c12_jet_x3_r2", j3[2] == 12)
check("c12_stencil_splits_deg4", st4 != j4[2])
check("c12_curvature_25_4", F(2) ** 2 + F(-3, 2) ** 2 == F(25, 4))


# ── 5 multi / vector / units / tape ───────────────────────────────────

X, Y = isolate(2, 1), isolate(3, 0)
check("c8_fx", rate((X ** 2) * Y, X) == 12)
X2, Y2 = isolate(2, 0), isolate(3, 1)
check("c8_fy", rate((X2 ** 2) * Y2, Y2) == 4)
w_dir = isolate(4, 2)
check("c11_dir_seed2", rate(w_dir * w_dir, w_dir) == 8)


def curl2(P, Q, at):
    xv, yv = at
    dQdx = rate(Q(isolate(xv, 1), isolate(yv, 0)), isolate(xv, 1))
    dPdy = rate(P(isolate(xv, 0), isolate(yv, 1)), isolate(yv, 1))
    return dQdx - dPdy


check("c9_curl", curl2(lambda X, Y: -Y, lambda X, Y: X, (4, 5)) == 2)
check("c9_curl_grad", curl2(lambda X, Y: 2 * X * Y, lambda X, Y: X ** 2, (2, 3)) == 0)
check("c9_div", rate(isolate(7, 1), isolate(7, 1)) + rate(isolate(9, 1), isolate(9, 1)) == 2)
check("c15_m", rate(isolate(3) ** 2, isolate(3)) == 6)
check("c15_cm", rate(isolate(300) ** 2, isolate(300)) == 600)


def counted():
    n = [0]

    def add(a, b):
        n[0] += 1
        return a + b

    def mul(a, b):
        n[0] += 1
        return a * b

    def div(a, b):
        n[0] += 1
        return a / b

    def sub(a, b):
        n[0] += 1
        return a - b

    return n, add, mul, div, sub


n, add, mul, div, sub = counted()
vv, vr, rv = mul(F(3), F(3)), mul(F(3), F(1)), mul(F(1), F(3))
out = div(add(vr, rv), F(1))
check("tape_pair_5_to_6", n[0] == 5 and out == 6)


# tape fd recount carefully
def fd_tape():
    n = [0]

    def add(a, b):
        n[0] += 1
        return a + b

    def mul(a, b):
        n[0] += 1
        return a * b

    def div(a, b):
        n[0] += 1
        return a / b

    def sub(a, b):
        n[0] += 1
        return a - b

    h = F(1, 2)
    three_h = add(F(3), h)
    q = div(sub(mul(three_h, three_h), mul(F(3), F(3))), h)
    return n[0], q


ops, val = fd_tape()
check("tape_fd_exact", ops == 5 and val == F(13, 2))



# ── Appendix C: the forge -- scanning combinators for closure ─────────
import itertools as _it


def _scan_closure(Vv, Vr, mix_fn):
    for v1, r1, v2, r2 in _it.product(Vv, Vr, Vv, Vr):
        v, r = mix_fn(v1, r1, v2, r2)
        if v not in Vv or r not in Vr:
            return False, (v1, r1, v2, r2), (v, r)
    return True, None, None


_Vbits = {0, 1}
_host_leibniz = lambda v1, r1, v2, r2: (v1 * v2, r1 * v2 + v1 * r2)
_lei_xor = lambda v1, r1, v2, r2: (v1 * v2, (r1 * v2) ^ (v1 * r2))
_lei_or = lambda v1, r1, v2, r2: (v1 * v2, (r1 * v2) | (v1 * r2))
_lei_and = lambda v1, r1, v2, r2: (v1 * v2, (r1 * v2) & (v1 * r2))

_ok, _witness, _result = _scan_closure(_Vbits, _Vbits, _host_leibniz)
check("forge_host_leibniz_leaks_on_bits", (not _ok) and _witness == (1, 1, 1, 1) and _result == (1, 2))
check("forge_xor_closes_on_bits", _scan_closure(_Vbits, _Vbits, _lei_xor)[0])
check("forge_or_closes_on_bits", _scan_closure(_Vbits, _Vbits, _lei_or)[0])
check("forge_and_closes_on_bits", _scan_closure(_Vbits, _Vbits, _lei_and)[0])

_V3 = {0, 1, 2}


def _mod3_leibniz_wrapped(v1, r1, v2, r2):
    v, r = v1 * v2, r1 * v2 + v1 * r2
    return v % 3, r % 3


def _mod3_leibniz_unwrapped(v1, r1, v2, r2):
    return v1 * v2, r1 * v2 + v1 * r2


check("forge_wrap_leibniz_closes_on_z3", _scan_closure(_V3, _V3, _mod3_leibniz_wrapped)[0])
check("forge_unwrapped_leibniz_leaks_on_z3", not _scan_closure(_V3, _V3, _mod3_leibniz_unwrapped)[0])



# ── Vq and Vt: two more alphabets a Reading's operations write into ───

def _host_div(a, b):
    return F(a, b)


def _modinv_div(a, b, n=5):
    for x in range(n):
        if (b * x) % n == a:
            return x
    return None


_Z5 = set(range(5))
_leak_count = sum(
    1 for a in _Z5 for b in _Z5 if b != 0 and _host_div(a, b) not in _Z5
)
check("vq_host_division_leaks_on_z5", _leak_count == 8)
check("vq_modinv_division_closes_on_z5",
      all(_modinv_div(a, b) in _Z5 for a in _Z5 for b in _Z5 if b != 0))


def _mul_jet(a, b):
    return (a[0] * b[0], a[1] * b[0] + a[0] * b[1],
            a[2] * b[0] + 2 * a[1] * b[1] + a[0] * b[2])


_bits = {0, 1}
_jet_leak = None
for _combo in _it.product(_bits, repeat=6):
    _a, _b = _combo[0:3], _combo[3:6]
    _v, _r, _r2 = _mul_jet(_a, _b)
    if _v not in _bits or _r not in _bits or _r2 not in _bits:
        _jet_leak = (_a, _b, (_v, _r, _r2))
        break
check("vt_bit_jet_leaks", _jet_leak == ((0, 1, 0), (0, 1, 0), (0, 0, 2)))


if __name__ == "__main__":
    passed = sum(1 for _,ok,_ in CHECKS if ok)
    for name, ok, tier in CHECKS:
        print(f"  [{tier:<11}] {name:<32} {'PASS' if ok else 'FAIL'}")
    print(f"\n{passed}/{len(CHECKS)} calculus-section checks passed")
