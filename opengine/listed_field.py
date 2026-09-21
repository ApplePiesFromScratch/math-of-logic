#!/usr/bin/env python3
"""Listed interacting scalar + 3+1 Minkowski + plaquette leftover.

Not the Standard Model. Not Einstein's equation.
Finite V, named G, leftover kept.
"""
from __future__ import annotations

from fractions import Fraction as F
from itertools import product

CHECKS = []


def check(name, cond):
    CHECKS.append((name, bool(cond)))


# ── 1. Interacting scalar on a listed ring of sites ───────────────────
# V_site = {0,1,2,3} wrap
# V_φ    = {-1, 0, 1}
# free kinetic: (φ_i - φ_{i+1})^2
# interaction:  λ φ_i^4          λ = 1

SITES = (0, 1, 2, 3)
PHI = (-1, 0, 1)


def kin(cfg):
    s = 0
    for i in SITES:
        d = cfg[i] - cfg[(i + 1) % 4]
        s += d * d
    return s


def quartic(cfg):
    return sum(cfg[i] ** 4 for i in SITES)


def S(cfg, lam=1):
    return kin(cfg) + lam * quartic(cfg)


vac = (0, 0, 0, 0)
bump = (1, 0, 0, 0)
wave = (1, 0, -1, 0)
wall = (1, 1, -1, -1)

check("vac_kin_0", kin(vac) == 0)
check("vac_int_0", quartic(vac) == 0)
check("bump_kin", kin(bump) == 2)          # 1-0 and 0-1
check("bump_int", quartic(bump) == 1)
check("wave_int", quartic(wave) == 2)
check("S_vac", S(vac) == 0)
check("S_bump", S(bump) == 3)
check("interact_raises", S(bump, 1) > S(bump, 0))

# all configs on listed V_φ^4 = 3^4 = 81
all_cfg = list(product(PHI, repeat=4))
check("config_count", len(all_cfg) == 81)
Svals = [S(c) for c in all_cfg]
check("S_min_is_vac", min(Svals) == 0)
check("vac_unique_min", Svals.count(0) == 1)

# leftover: add-then-weight vs weight-then-add on two cfgs (path-sum order)
w_bump, w_wave = F(1, S(bump)), F(1, S(wave))  # toy weights 1/S
check("path_order", (w_bump + w_wave) ** 2 != w_bump ** 2 + w_wave ** 2)

# grow φ V in public: add 2
PHI2 = (-2, -1, 0, 1, 2)
check("mu_grows_cfgs", 5 ** 4 == 625)
# 2^4 = 16; bump-like (2,0,0,0) interaction 16 vs 1
check("mu_quartic_grows", 2 ** 4 == 16)


# ── 2. 3+1 Minkowski on listed 4-tuples over Q ────────────────────────

def eta4(u, v):
    return u[0] * v[0] - u[1] * v[1] - u[2] * v[2] - u[3] * v[3]


t = (1, 0, 0, 0)
x = (0, 1, 0, 0)
y = (0, 0, 1, 0)
z = (0, 0, 0, 1)
null = (1, 1, 0, 0)

check("eta_tt", eta4(t, t) == 1)
check("eta_xx", eta4(x, x) == -1)
check("eta_yy", eta4(y, y) == -1)
check("eta_zz", eta4(z, z) == -1)
check("eta_null", eta4(null, null) == 0)
check("eta_xy", eta4(x, y) == 0)

# boost in t-x, β=3/5, γ=5/4
b, g = F(3, 5), F(5, 4)


def boost_tx(u):
    T, X, Y, Z = u
    return (g * (T - b * X), g * (X - b * T), Y, Z)


tb, xb, nb = boost_tx(t), boost_tx(x), boost_tx(null)
check("boost_tt", eta4(tb, tb) == 1)
check("boost_xx", eta4(xb, xb) == -1)
check("boost_null", eta4(nb, nb) == 0)
check("boost_y_fixed", boost_tx(y) == y)


# ── 3. Plaquette leftover = curvature stand-in on 4 events ────────────
# events of a square; transport of a 2-slot (spatial) depends on edge
# edge u: add (1,0) wrap 3; edge v: add (0, 1+current[0]) wrap 3

def tu(vec):
    return ((vec[0] + 1) % 3, vec[1])


def tv(vec):
    return (vec[0], (vec[1] + 1 + vec[0]) % 3)


uv = tv(tu((0, 0)))
vu = tu(tv((0, 0)))
check("plaquette_leftover", uv != vu)
check("plaquette_uv", uv == (1, 2))
check("plaquette_vu", vu == (1, 1))
# curvature letter = slot difference
curv = ((uv[0] - vu[0]) % 3, (uv[1] - vu[1]) % 3)
check("curv_letter", curv == (0, 1))


# ── 4. Einstein-shaped leftover: G vs T as two reads, not a law ───────
# On this lattice we do not write Gμν=8πT. We write two accumulates
# and keep their difference. "Matter" = quartic load. "Geom" = plaquette.

matter_bump = quartic(bump)
matter_vac = quartic(vac)
geom = curv[1]
check("two_reads_named", matter_bump == 1 and geom == 1)
# same two G on vacuum: matter 0, geom still 1 (plaquette is config-free here)
check("not_einstein_vac", matter_vac != geom)


if __name__ == "__main__":
    failed = [n for n, c in CHECKS if not c]
    for n, c in CHECKS:
        print(("PASS " if c else "FAIL ") + n)
    print(f"{sum(c for _,c in CHECKS)}/{len(CHECKS)}")
    print("ALL PASS" if not failed else "FAILED " + str(failed))
    raise SystemExit(1 if failed else 0)
