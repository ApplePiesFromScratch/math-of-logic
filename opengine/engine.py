#!/usr/bin/env python3
"""Operator engine: is G a map V^k -> V?

Use: decide whether an operation stays legal when the value alphabet
grows (new state, new grade, new unit). That is the systems question.
"""
from __future__ import annotations

from fractions import Fraction as F
from itertools import product
from typing import Callable, Iterable


class LeavesV(Exception):
    pass


class Engine:
    def __init__(self, name: str, V: Iterable):
        self.name = name
        self.V = tuple(V)
        self.index = {v: i for i, v in enumerate(self.V)}

    def in_V(self, x) -> bool:
        return x in self.index

    def scan_unary(self, op: Callable, label: str) -> dict:
        table = {}
        leaks = []
        for a in self.V:
            try:
                out = op(a)
            except Exception as e:
                leaks.append((a, type(e).__name__))
                continue
            table[a] = out
            if not self.in_V(out):
                leaks.append((a, out))
        return {
            "kind": "unary",
            "label": label,
            "carrier": self.name,
            "closed": not leaks,
            "leaks": leaks,
            "table": table,
        }

    def scan_binary(self, op: Callable, label: str) -> dict:
        table = {}
        leaks = []
        for a, b in product(self.V, self.V):
            try:
                out = op(a, b)
            except Exception as e:
                leaks.append(((a, b), type(e).__name__))
                continue
            table[(a, b)] = out
            if not self.in_V(out):
                leaks.append(((a, b), out))
        closed = not leaks
        props = {}
        if closed:
            props = self._binary_props(op)
        return {
            "kind": "binary",
            "label": label,
            "carrier": self.name,
            "closed": closed,
            "leaks": leaks,
            "n": len(self.V) ** 2,
            "props": props,
        }

    def _binary_props(self, op: Callable) -> dict:
        V = self.V
        comm = all(op(a, b) == op(b, a) for a, b in product(V, V))
        assoc = all(op(op(a, b), c) == op(a, op(b, c)) for a, b, c in product(V, V, V))
        idem = all(op(a, a) == a for a in V)
        ids = [e for e in V if all(op(e, a) == a and op(a, e) == a for a in V)]
        anns = [z for z in V if all(op(z, a) == z and op(a, z) == z for a in V)]
        return {
            "comm": comm,
            "assoc": assoc,
            "idem": idem,
            "idents": ids,
            "annihilators": anns,
        }


def coincide_binary(V, op_a, op_b) -> bool:
    return all(op_a(a, b) == op_b(a, b) for a, b in product(V, V))


def split_report(small, big, op_a, op_b, name_a, name_b) -> dict:
    same_small = coincide_binary(small.V, op_a, op_b)
    a_big = big.scan_binary(op_a, name_a)
    b_big = big.scan_binary(op_b, name_b)
    same_big = a_big["closed"] and b_big["closed"] and coincide_binary(big.V, op_a, op_b)
    return {
        "small": small.name,
        "big": big.name,
        "coincide_on_small": same_small,
        "coincide_on_big": same_big,
        "a_closed_big": a_big["closed"],
        "b_closed_big": b_big["closed"],
        "a_leaks": a_big["leaks"][:8],
        "b_leaks": b_big["leaks"][:8],
        "split": same_small and not same_big,
    }


def signature(scan: dict) -> str:
    if not scan["closed"]:
        return "LEAK"
    p = scan.get("props") or {}
    bits = []
    if p.get("comm"):
        bits.append("comm")
    if p.get("assoc"):
        bits.append("assoc")
    if p.get("idem"):
        bits.append("idem")
    if p.get("idents"):
        bits.append(f"id={p['idents']}")
    if p.get("annihilators"):
        bits.append(f"ann={p['annihilators']}")
    return " ".join(bits) or "closed"


# ── catalogue of systems ──────────────────────────────────────────────

V2 = Engine("V2", (0, 1))
V3 = Engine("V3", (0, F(1, 2), 1))
V4 = Engine("V4", (0, F(1, 3), F(2, 3), 1))
Z4 = Engine("Z/4", (0, 1, 2, 3))
Z5 = Engine("Z/5", (0, 1, 2, 3, 4))
Z6 = Engine("Z/6", tuple(range(6)))
Bits = Engine("bits", (0, 1))


def AND_min(a, b):
    return min(a, b)


def AND_prod(a, b):
    return a * b


def OR_max(a, b):
    return max(a, b)


def XOR(a, b):
    return (a + b) % 2


def NOT(a):
    return 1 - a


def luk_and(a, b):
    return max(0, a + b - 1)


def trop_add(a, b):
    return min(a, b)


def trop_mul(a, b):
    return a + b


def wrap_add(n):
    return lambda a, b: (a + b) % n


def wrap_mul(n):
    return lambda a, b: (a * b) % n


def quot_on(V_zero=0):
    def q(a, b):
        if b == V_zero:
            raise ZeroDivisionError("pole")
        return a / b

    return q


# Leibniz mix on pair-V: pairs (v,r) with v,r in a scalar set
def pair_engine(scalars, name):
    pairs = tuple((v, r) for v in scalars for r in scalars)
    return Engine(name, pairs)


def leibniz(a, b):
    (v, r), (w, s) = a, b
    return (v * w, r * w + v * s)


def value_only_mix(a, b):
    (v, r), (w, s) = a, b
    return (v * w, 0)


def add_channels(a, b):
    (v, r), (w, s) = a, b
    return (v * w, r + s)
