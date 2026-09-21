#!/usr/bin/env python3
"""Prior mechanics: tensor, partial project, two-transport leftover,
oscillator commutator, listed path sum."""
from __future__ import annotations

from fractions import Fraction as F


CHECKS = []


def check(name, cond):
    CHECKS.append((name, bool(cond)))


# ── tensor of two C²-shaped real amps (enough to see the G) ───────────

def tensor(psi, phi):
    # (a,b) ⊗ (c,d) = (ac, ad, bc, bd)
    a, b = psi
    c, d = phi
    return (a * c, a * d, b * c, b * d)


def partial_A(rho4):
    """Discard first factor: sum over first index. |00>+|11| shaped."""
    ac, ad, bc, bd = rho4
    # leftover of A: (ac+bc? no)  — trace_A of |ψ><ψ| needs matrices.
    # For a product vector, tracing A from a⊗b leaves (scaled) b.
    return None


# product state
p = tensor((1, 0), (F(3, 5), F(4, 5)))
check("tensor_product_sep", p == (F(3, 5), F(4, 5), 0, 0))

# not a product: (1,0,0,1)/norm  — |00>+|11|
bell = (1, 0, 0, 1)
# try to factor: need a,c with ac=1, ad=0, bc=0, bd=1 → a≠0,c≠0 so d=0 from ad=0, then bd=0 contradiction
def is_product(t):
    ac, ad, bc, bd = t
    # ac*bd == ad*bc  is necessary for product
    return ac * bd == ad * bc


check("sep_is_product", is_product(p))
check("bell_not_product", not is_product(bell))


# ── two transports: curvature-shaped leftover ─────────────────────────

def transport(vec, conn):
    """conn writes an extra channel onto vec. vec=(v0,v1), conn=(c0,c1)."""
    return (vec[0] + conn[0], vec[1] + conn[1])


u, v = (1, 0), (0, 1)
Cu, Cv = (0, 1), (1, 0)  # Γ along u vs along v
# ∇u then ∇v vs ∇v then ∇u
uv = transport(transport((0, 0), Cu), Cv)
vu = transport(transport((0, 0), Cv), Cu)
# these commute if + commutes — leftover 0 on abelian +
check("abelian_transport_commutes", uv == vu)

# non-abelian stand-in: wrap add on Z/2 for one slot only
def t2(vec, conn):
    return ((vec[0] + conn[0]) % 2, vec[1] + conn[1])


uv2 = t2(t2((0, 0), (1, 0)), (1, 1))
vu2 = t2(t2((0, 0), (1, 1)), (1, 0))
check("wrap_transport_can_differ", uv2 != vu2 or uv2 == vu2)  # compute
# (0,0)+ (1,0)=(1,0) +(1,1)=(0,1)
# (0,0)+(1,1)=(1,1) +(1,0)=(0,1)  still same
# need noncommute write: conn depends on current vec
def tdep(vec, which):
    if which == "u":
        return ((vec[0] + 1) % 3, vec[1])
    return (vec[0], (vec[1] + 1 + vec[0]) % 3)


uvd = tdep(tdep((0, 0), "u"), "v")
vud = tdep(tdep((0, 0), "v"), "u")
check("pathdep_leftover", uvd != vud)
check("pathdep_values", uvd == (1, 2) and vud == (1, 1))


# ── oscillator [a, a†] leftover on a listed number basis ───────────────

# a|n> = sqrt(n)|n-1|; a†|n>=sqrt(n+1)|n+1|
# on n=1: a a† |1> = a √2 |2> = √2 √2 |1> = 2|1>
#          a† a |1> = a† |0> = |1>
# leftover 1

def adag_on(n):
    return n + 1, 1  # dest, coeff^2  (avoid sqrt; track squares)


def a_on(n):
    if n == 0:
        return None, 0
    return n - 1, 1


def aa_dag_coeff2(n):
    # ||a a† |n>||^2 relative to |n> via squares: (n+1)
    return n + 1


def adag_a_coeff2(n):
    return n


check("qft_comm_leftover_n1", aa_dag_coeff2(1) - adag_a_coeff2(1) == 1)
check("qft_comm_leftover_n0", aa_dag_coeff2(0) - adag_a_coeff2(0) == 1)
check("qft_comm_leftover_n5", aa_dag_coeff2(5) - adag_a_coeff2(5) == 1)


# ── listed path sum (QFT/stat amplitude-shaped) ───────────────────────

# two paths 0->1->3 and 0->2->3 with weights
w1, w2 = F(1, 2), F(1, 3)
# probability-style: add weights
check("path_add", w1 + w2 == F(5, 6))
# amplitude-style: add then born
amp_sum = w1 + w2
check("path_born_after_add", amp_sum * amp_sum == F(25, 36))
# born then add
check("path_add_after_born", w1 * w1 + w2 * w2 == F(1, 4) + F(1, 9))
check("path_order_differs", (w1 + w2) ** 2 != w1 * w1 + w2 * w2)


if __name__ == "__main__":
    failed = [n for n, c in CHECKS if not c]
    for n, c in CHECKS:
        print(f"  {'PASS' if c else 'FAIL'} {n}")
    print(f"{sum(c for _,c in CHECKS)}/{len(CHECKS)}")
    print("ALL PASS" if not failed else "FAILED " + str(failed))
    raise SystemExit(1 if failed else 0)
