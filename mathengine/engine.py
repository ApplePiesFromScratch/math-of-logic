#!/usr/bin/env python3
"""Process math engine. Q is a snapshot (a, b), not a finale object."""
from __future__ import annotations


class Theta(ValueError):
    pass


def rel(a: int, b: int) -> tuple[int, int]:
    if b == 0:
        raise Theta("no isolator")
    return (a, b)


def weigh(p: tuple[int, int], q: tuple[int, int]) -> bool:
    return p[0] * q[1] == p[1] * q[0]


def radd(p, q):
    return rel(p[0] * q[1] + p[1] * q[0], p[1] * q[1])


def rsub(p, q):
    return rel(p[0] * q[1] - p[1] * q[0], p[1] * q[1])


def rmul(p, q):
    return rel(p[0] * q[0], p[1] * q[1])


def isolate(v, seed) -> tuple:
    vv = v if isinstance(v, tuple) and len(v) == 2 else rel(int(v), 1)
    ss = seed if isinstance(seed, tuple) and len(seed) == 2 else rel(int(seed), 1)
    if ss[0] == 0:
        raise Theta("seed 0")
    return (vv, ss)


def add(P, Q):
    return (radd(P[0], Q[0]), radd(P[1], Q[1]))


def mix(P, Q):
    return (rmul(P[0], Q[0]), radd(rmul(P[1], Q[0]), rmul(P[0], Q[1])))


def rate(P, G):
    return rel(P[1][0] * G[1][1], P[1][1] * G[1][0])


def parse_num(s: str, i: int):
    sign = 1
    if i < len(s) and s[i] == "-" and (i == 0 or s[i - 1] in "+-*/("):
        sign = -1
        i += 1
    j = i
    while i < len(s) and s[i].isdigit():
        i += 1
    if j == i:
        raise Theta("num")
    n = sign * int(s[j:i])
    if i < len(s) and s[i] == "/":
        i += 1
        k = i
        while i < len(s) and s[i].isdigit():
            i += 1
        if k == i:
            raise Theta("den")
        d = int(s[k:i])
        return rel(n, d), i
    return rel(n, 1), i


def parse(s: str):
    s = "".join(s.split())
    if not s:
        raise Theta("empty expr")
    i = 0

    def peek():
        return s[i] if i < len(s) else ""

    def atom():
        nonlocal i
        if peek() == "x":
            i += 1
            return "X"
        if peek() == "(":
            i += 1
            v = expr()
            if peek() != ")":
                raise Theta("paren")
            i += 1
            return v
        if peek().isdigit() or peek() == "-":
            n, i = parse_num(s, i)
            return ("N", n)
        raise Theta("atom")

    def power():
        nonlocal i
        v = atom()
        if peek() == "*" and i + 1 < len(s) and s[i + 1] == "*":
            i += 2
            n = atom()
            if not (isinstance(n, tuple) and n[0] == "N" and n[1][1] == 1 and n[1][0] >= 0):
                raise Theta("**")
            k = n[1][0]
            if k == 0:
                return ("N", rel(1, 1))
            out = v
            for _ in range(k - 1):
                out = ("*", out, v)
            return out
        return v

    def term():
        nonlocal i
        v = power()
        while peek() == "*":
            i += 1
            v = ("*", v, power())
        return v

    def expr():
        nonlocal i
        v = term()
        while peek() in ("+", "-"):
            op = peek()
            i += 1
            v = (op, v, term())
        return v

    tree = expr()
    if i != len(s):
        raise Theta("leftover " + s[i:])
    return tree


def ev(tree, x):
    if tree == "X":
        return x
    if tree[0] == "N":
        return (tree[1], rel(0, 1))
    op, a, b = tree
    ea, eb = ev(a, x), ev(b, x)
    if op == "+":
        return add(ea, eb)
    if op == "-":
        neg = (rel(-eb[0][0], eb[0][1]), rel(-eb[1][0], eb[1][1]))
        return add(ea, neg)
    if op == "*":
        return mix(ea, eb)
    raise Theta("op")


def at_point(at):
    if isinstance(at, tuple):
        return at
    if isinstance(at, int):
        return rel(at, 1)
    return parse_num(str(at).replace(" ", ""), 0)[0]


def run(expr: str, at, seeds=(1, 2, -1)):
    tree = parse(expr)
    atp = at_point(at)
    rows = []
    for s in seeds:
        x = isolate(atp, s)
        y = ev(tree, x)
        rows.append({"seed": s, "value": y[0], "rate": rate(y, x)})
    rates = [r["rate"] for r in rows]
    ok = all(weigh(rates[0], r) for r in rates)
    return {
        "expr": expr,
        "at": atp,
        "value": rows[0]["value"],
        "rate": rates[0] if ok else None,
        "gauge": ok,
        "rows": rows,
    }


def certify(expr: str, values, seeds=(1, 2, -1)):
    if not values or not seeds:
        raise Theta("empty grid")
    out = []
    for v in values:
        rec = run(expr, v, seeds)
        if not rec["gauge"]:
            raise Theta("gauge split at %s" % (v,))
        out.append(rec)
    return out


def main():
    import json
    import sys

    expr = sys.argv[1] if len(sys.argv) > 1 else "x*x"
    at = sys.argv[2] if len(sys.argv) > 2 else "3"
    rec = run(expr, at)
    print(json.dumps({"value": rec["value"], "rate": rec["rate"], "gauge": rec["gauge"]}, default=str))
    for row in rec["rows"]:
        print(" seed", row["seed"], "snapshot", row["rate"])


if __name__ == "__main__":
    main()
