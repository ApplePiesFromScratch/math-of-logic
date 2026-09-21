#!/usr/bin/env python3
"""Play: decode combinators, attention scores, dual net, two-point fit."""
from __future__ import annotations

from fractions import Fraction as F
from itertools import product
from math import exp, log


VOCAB = ("a", "b", "c")


def softmax(logits):
    xs = [exp(x) for x in logits]
    z = sum(xs)
    if z == 0:
        raise ZeroDivisionError("dead")
    return [x / z for x in xs]


def sample_argmax(p):
    return max(range(len(p)), key=lambda i: p[i])


def sample_rand(p, u):
    # listed u in [0,1); scan cdf
    acc = 0.0
    for i, pi in enumerate(p):
        acc += pi
        if u < acc:
            return i
    return len(p) - 1


# dual pair
def dadd(a, b):
    return (a[0] + b[0], a[1] + b[1])


def dmul(a, b):
    return (a[0] * b[0], a[1] * b[0] + a[0] * b[1])


def dscale(k, a):
    return (k * a[0], k * a[1])


def attn_dot(q, k):
    return sum(qi * ki for qi, ki in zip(q, k))


def attn_l1(q, k):
    return -sum(abs(qi - ki) for qi, ki in zip(q, k))


def attn_max(q, k):
    return max(qi * ki for qi, ki in zip(q, k))


def attn_xor_bit(q, k):
    # bits only
    return sum((qi ^ ki) for qi, ki in zip(q, k))


def main():
    print("=== P1 decode T and u ===")
    logits = (0.0, 2.0, 0.0)
    for T in (0.25, 1.0, 4.0, 50.0):
        p = softmax(tuple(x / T for x in logits))
        print(f"  T={T:<5} p={[round(x,4) for x in p]} argmax={VOCAB[sample_argmax(p)]}")
    p = softmax(logits)
    for u in (0.01, 0.3, 0.5, 0.9):
        print(f"  u={u} token={VOCAB[sample_rand(p, u)]}")

    print("=== P2 empty / oov / dead softmax ===")
    print("  empty ctx letters", ())
    print("  oov z in V", "z" in VOCAB)
    try:
        softmax((-1e9, -1e9, -1e9))
        print("  tiny logits landed", True)
    except Exception as e:
        print("  tiny logits", type(e).__name__)
    # all -inf shaped
    try:
        xs = [exp(-1e9)] * 3
        print("  exp(-1e9) sum", sum(xs))
    except Exception as e:
        print(e)

    print("=== P3 attention 2 keys, 3 score G ===")
    q = (1.0, 0.0)
    keys = [(1.0, 0.0), (0.0, 1.0)]
    for name, fn in (("dot", attn_dot), ("l1", attn_l1), ("max", attn_max)):
        scores = [fn(q, k) for k in keys]
        print(f"  {name:4} scores={scores}")

    print("=== P4 bit keys xor vs host + ===")
    qb = (1, 0)
    keysb = [(1, 0), (0, 1), (1, 1)]
    for k in keysb:
        print(f"  q={qb} k={k} xor={attn_xor_bit(qb,k)} dot={attn_dot(qb,k)}")

    print("=== P5 dual linear fit two points ===")
    # y = w x + b ; points (1,2), (2,4)  true w=2 b=0
    def pred(w, b, x):
        return dadd(dmul(w, x), b)

    def loss_pair(w, b):
        # listed two points; leftover vs labels 2 and 4
        y1 = pred(w, b, (1, 0))  # x const for value; need x seed for dw
        # isolate x as (val, 0) and w as (val, 1) to get dL/dw
        return y1

    w, b = (0, 1), (0, 0)  # isolate w
    # L = (wx+b - y)^2 at x=1 y=2 and x=2 y=4, w value 0
    def L_at(wv, bv):
        e1 = wv * 1 + bv - 2
        e2 = wv * 2 + bv - 4
        return e1 * e1 + e2 * e2

    print("  L(w=0,b=0)", L_at(0, 0))
    print("  L(w=2,b=0)", L_at(2, 0))
    print("  L(w=1,b=1)", L_at(1, 1))
    # dual L wrt w at (0,0): isolate w
    # e1 = w-2, e2=2w-4; L=(w-2)^2+(2w-4)^2
    # at w=0: L=4+16=20
    # dL/dw = 2(w-2)+2(2w-4)*2 = 2w-4+8w-16=10w-20; at 0 = -20
    w = (0, 1)
    e1 = dadd(w, (-2, 0))
    e2 = dadd(dmul((2, 0), w), (-4, 0))
    L = dadd(dmul(e1, e1), dmul(e2, e2))
    print("  dual L at w=0", L, "rate dL/dw", L[1] / w[1])

    print("=== P6 one step vs true ===")
    eta = F(1, 10)
    w1 = 0 - float(eta) * (L[1] / w[1])
    print("  w after one step", w1, "L", L_at(w1, 0))

    print("=== P7 residual vs plain on listed ===")
    x = 2
    for f in (0, 3, -2):
        print(f"  x={x} f={f} plain={f} resid={x+f}")

    print("=== P8 forge: 2-key bit score tables close? ===")
    # score in {0,1}, two keys, softmax skipped; pick combinator of bits
    closed = 0
    for code in range(16):
        leak = False
        for q, k in product((0, 1), repeat=2):
            bit = (code >> (q + 2 * k)) & 1
            if bit not in (0, 1):
                leak = True
        closed += not leak
    print("  16 bit score maps closed", closed)

    print("=== P9 train read vs test read after one step ===")
    print("  train L at w=0", L_at(0, 0), "at w=2", L_at(2, 0))
    print("  if test is the same two points, leftover 0; if test is (3,5) L(w=2)", (2*3+0-5)**2)


if __name__ == "__main__":
    main()
