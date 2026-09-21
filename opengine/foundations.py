#!/usr/bin/env python3
"""Peano as a machine. Calculus as a consumer of its output.
Isolation as a write. Pairs that die when split. Priced =."""
from __future__ import annotations

from fractions import Fraction as F


class Ledger:
    def __init__(self):
        self.ticks = 0
        self.log = []

    def pay(self, kind, n=1, note=""):
        self.ticks += n
        self.log.append((kind, n, note))


# ── Peano: 0 and S, + as iterate S ────────────────────────────────────


def S(n, led):
    led.pay("S", 1, f"{n}->")
    return n + 1  # host successor; the PAY is the point


def plus_peano(a, b, led):
    """a+b = S^b(a). Cost = b successors."""
    x = a
    for _ in range(b):
        x = S(x, led)
    return x


def times_peano(a, b, led):
    """a*b = a + a + ... (b times). Cost = b pluses, each plus costs a S."""
    x = 0
    for _ in range(b):
        x = plus_peano(x, a, led)
    return x


def numeral(k, led):
    """Build k from 0. Cost = k successors."""
    x = 0
    for _ in range(k):
        x = S(x, led)
    return x


# ── Calculus consumer: isolate imports the numeral ─────────────────────


class Reading:
    def __init__(self, v, r, origin="imported"):
        self.v, self.r, self.origin = v, r, origin

    def __repr__(self):
        return f"Reading({self.v},{self.r},{self.origin})"


def isolate_import(v, seed=1, led=None):
    """Standard kernel: v is already a letter. Pay 0 for the numeral."""
    if led:
        led.pay("isolate", 1, "import")
    return Reading(v, seed, origin="imported")


def isolate_from_peano(k, seed=1):
    """Pay Peano to mint the numeral, then write the channel."""
    led = Ledger()
    v = numeral(k, led)
    led.pay("isolate", 1, "after_peano")
    return Reading(v, seed, origin=f"peano_ticks={led.ticks}"), led


# ── Split the pair ────────────────────────────────────────────────────


def project_v(p):
    return p.v


def project_r(p):
    return p.r


def rate(top, bottom):
    if bottom.r == 0:
        raise ZeroDivisionError("dead")
    return top.r / bottom.r


# ── Equivalence ───────────────────────────────────────────────────────


def eq_val(a, b):
    return a.v == b.v and a.r == b.r


def eq_mint(a, b):
    return eq_val(a, b) and a.origin == b.origin


def main():
    print("=== Peano prices ===")
    for k in (0, 1, 3, 5):
        led = Ledger()
        n = numeral(k, led)
        print(f"  numeral({k}) = {n}  ticks={led.ticks}")

    led = Ledger()
    s = plus_peano(3, 2, led)
    print(f"  3+2 via S^2(3) = {s}  ticks={led.ticks}  (expect 2)")

    led = Ledger()
    p = times_peano(3, 4, led)
    print(f"  3*4 via plus = {p}  ticks={led.ticks}  (expect 3*4=12 S)")

    print()
    print("=== isolate import vs isolate after Peano ===")
    led = Ledger()
    a = isolate_import(3, 1, led)
    print(f"  import isolate(3) = {a}  ticks={led.ticks}  (numeral unpaid)")

    b, ledp = isolate_from_peano(3, 1)
    print(f"  peano isolate(3) = {b}  ticks={ledp.ticks}  (3 S + 1 isolate)")

    print()
    print("=== pair split: what each projection loses ===")
    x = isolate_import(3, 1)
    y = x  # same object
    # x*x host lei
    xx = Reading(x.v * x.v, x.r * x.v + x.v * x.r, origin="lei")
    print(f"  xx={xx}")
    print(f"  project_v(xx)={project_v(xx)}  lost rate 6; cannot recover slope")
    print(f"  project_r(xx)={project_r(xx)}  lost value 9; 6 of what?")
    print(f"  rate(xx,x)={rate(xx,x)}  needs BOTH slots of BOTH pairs")

    print()
    print("=== two pairs that val-eq and mint-differ ===")
    p1 = Reading(9, 6, origin="x*x seed1")
    p2 = Reading(9, 6, origin="3x seed2")
    print(f"  eq_val={eq_val(p1,p2)}  eq_mint={eq_mint(p1,p2)}")
    print("  val-eq is A=A on the output pair; mint keeps the generator")

    print()
    print("=== calculus + uses host + (Peano + unpaid) ===")
    led = Ledger()
    u = isolate_import(3, 1, led)
    w = isolate_import(2, 0, led)
    sread = Reading(u.v + w.v, u.r + w.r, origin="host+")
    print(f"  Reading add {u}+{w} = {sread}  ledger ticks={led.ticks} (2 isolates, 0 S)")
    led2 = Ledger()
    _ = plus_peano(3, 2, led2)
    print(f"  same 3+2 in Peano ticks={led2.ticks}")

    print()
    print("=== induction vs gauge ===")
    # Peano induction: property of all n from 0 via S
    # Gauge: property of all seeds in listed K
    K = (1, 2, F(1, 2), -1)
    slopes = []
    for k in K:
        x = isolate_import(3, k)
        xx = Reading(x.v * x.v, x.r * x.v + x.v * x.r)
        slopes.append(rate(xx, x))
    print(f"  gauge on K={K} slopes={slopes}  all_same={len(set(slopes))==1}")
    print("  gauge is induction-shaped on the SEED alphabet, not on N")


if __name__ == "__main__":
    main()
