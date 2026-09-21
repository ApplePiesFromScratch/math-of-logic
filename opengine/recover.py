#!/usr/bin/env python3
"""Recover the calculi: finite probability, C² qubit, 1+1 metric.

FORCED = this file just computed it.
STIPULATED = the name of the theory, not extra axioms.
"""
from __future__ import annotations

from fractions import Fraction as F
from itertools import product


CHECKS = []


def check(name, cond, tier="FORCED"):
    CHECKS.append((name, bool(cond), tier))


# ── Probability on listed Ω ───────────────────────────────────────────

OMEGA = (1, 2, 3, 4, 5, 6)
UNIFORM = {w: F(1, 6) for w in OMEGA}


def P(event, mu=UNIFORM):
    return sum(mu[w] for w in event)


def cond(A, B, mu=UNIFORM):
    pb = P(B, mu)
    if pb == 0:
        raise ZeroDivisionError("dead isolator")
    return P(set(A) & set(B), mu) / pb


EVEN = {2, 4, 6}
GT3 = {4, 5, 6}
EMPTY = set()

check("prob_even", P(EVEN) == F(1, 2))
check("prob_cond", cond(EVEN, GT3) == F(2, 3))
try:
    cond(EVEN, EMPTY)
    check("prob_empty_theta", False)
except ZeroDivisionError:
    check("prob_empty_theta", True)

# Bayes: P(H|E) = P(E|H)P(H)/P(E)
# two-hypothesis mint
HYPO = ("fair", "biased")
prior = {"fair": F(1, 2), "biased": F(1, 2)}
# E = land 6; fair 1/6, biased 1/2
lik = {"fair": F(1, 6), "biased": F(1, 2)}
PE = prior["fair"] * lik["fair"] + prior["biased"] * lik["biased"]
post_fair = lik["fair"] * prior["fair"] / PE
check("prob_bayes_fair", post_fair == F(1, 4))
check("prob_bayes_PE", PE == F(1, 3))

# independence product vs joint
COIN = (0, 1)
mu2 = {(a, b): F(1, 4) for a in COIN for b in COIN}
check("prob_indep_product", mu2[(1, 1)] == F(1, 2) * F(1, 2))


# ── C² qubit ──────────────────────────────────────────────────────────

def cadd(u, v):
    return (u[0] + v[0], u[1] + v[1])


def cscale(k, u):
    # k real or complex pair
    if isinstance(k, tuple):
        return (k[0] * u[0] - k[1] * u[1], k[0] * u[1] + k[1] * u[0])
    return (k * u[0], k * u[1])


def cmul(u, v):
    return (u[0] * v[0] - u[1] * v[1], u[0] * v[1] + u[1] * v[0])


def cinner(u, v):
    # <u|v> = conj(u)·v
    return (u[0] * v[0] + u[1] * v[1], u[0] * v[1] - u[1] * v[0])


def born_amp(z):
    return z[0] * z[0] + z[1] * z[1]


def norm2(psi):
    a, b = psi[0], psi[1]
    return born_amp(a) + born_amp(b)


I = ((1, 0), (0, 0))  # 1+0i  — not used as matrix yet

# computational basis
KET0 = ((1, 0), (0, 0))  # (1+0i, 0+0i)
KET1 = ((0, 0), (1, 0))


def mat_vec(M, psi):
    # M 2x2 of complex pairs
    return (
        cadd(cmul(M[0][0], psi[0]), cmul(M[0][1], psi[1])),
        cadd(cmul(M[1][0], psi[0]), cmul(M[1][1], psi[1])),
    )


X = (((0, 0), (1, 0)), ((1, 0), (0, 0)))
Z = (((1, 0), (0, 0)), ((0, 0), (-1, 0)))
H = (
    ((F(1, 1), 0), (F(1, 1), 0)),
    ((F(1, 1), 0), (F(-1, 1), 0)),
)  # unnormalized; real Hadamard * sqrt2 later


check("qm_ii", cmul((0, 1), (0, 1)) == (-1, 0))
check("qm_X0", mat_vec(X, KET0) == KET1)
check("qm_X1", mat_vec(X, KET1) == KET0)
check("qm_Z0", mat_vec(Z, KET0) == KET0)
check("qm_Z1", mat_vec(Z, KET1) == ((0, 0), (-1, 0)))

# [X,Z] on |0>: XZ|0> = X|0> = |1>; ZX|0> = Z|1> = -|1|
XZ0 = mat_vec(X, mat_vec(Z, KET0))
ZX0 = mat_vec(Z, mat_vec(X, KET0))
check("qm_XZ0", XZ0 == KET1)
check("qm_ZX0", ZX0 == ((0, 0), (-1, 0)))
check("qm_XZ_neq_ZX", XZ0 != ZX0)

# Born + phase
plus = ((F(3, 5), 0), (F(4, 5), 0))  # real amps
check("qm_born_plus", norm2(plus) == 1)
flip = ((F(-3, 5), 0), (F(-4, 5), 0))
check("qm_born_phase", norm2(flip) == norm2(plus))

# global i phase
iphase = (cscale((0, 1), plus[0]), cscale((0, 1), plus[1]))
check("qm_born_i_phase", norm2(iphase) == norm2(plus))

# projector |0><0|
def proj0(psi):
    return (psi[0], ((0, 0), (0, 0))[0] if False else (0, 0))


check("qm_proj0_kills_ket1", proj0(KET1) == ((0, 0), (0, 0)))
check("qm_proj0_keeps_ket0", proj0(KET0) == (KET0[0], (0, 0)))


# ── 1+1 metric ────────────────────────────────────────────────────────

def eta(u, v):
    """Minkowski 1+1: u^t v^t - u^x v^x. Split-shaped."""
    return u[0] * v[0] - u[1] * v[1]


def euclid(u, v):
    return u[0] * v[0] + u[1] * v[1]


t = (1, 0)
x = (0, 1)
null = (1, 1)
check("gr_eta_tt", eta(t, t) == 1)
check("gr_eta_xx", eta(x, x) == -1)
check("gr_eta_tx", eta(t, x) == 0)
check("gr_null", eta(null, null) == 0)
check("gr_euclid_null", euclid(null, null) == 2)
check("gr_eta_not_euclid", eta(x, x) != euclid(x, x))

# boost gauge: (t,x) -> (γ(t-βx), γ(x-βt)) at β=3/5, γ=5/4  (3-4-5)
beta, gamma = F(3, 5), F(5, 4)


def boost(u):
    T, X = u
    return (gamma * (T - beta * X), gamma * (X - beta * T))


tb, xb = boost(t), boost(x)
nb = boost(null)
check("gr_boost_eta_tt", eta(tb, tb) == 1)
check("gr_boost_eta_xx", eta(xb, xb) == -1)
check("gr_boost_null", eta(nb, nb) == 0)

# leftover: euclid vs eta on same pair = 2 u^x v^x
check("gr_leftover_xx", euclid(x, x) - eta(x, x) == 2)


if __name__ == "__main__":
    failed = [(n, t) for n, c, t in CHECKS if not c]
    for n, c, t in CHECKS:
        print(f"  [{t:<11}] {n:<28} {'PASS' if c else 'FAIL'}")
    print(f"{sum(c for _,c,_ in CHECKS)}/{len(CHECKS)}")
    print("ALL PASS" if not failed else "FAILED " + str(failed))
    raise SystemExit(1 if failed else 0)
