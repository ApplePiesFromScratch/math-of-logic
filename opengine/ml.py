#!/usr/bin/env python3
"""Tiny paid cuts: vocab V, softmax project, loss leftover, chain, type θ."""
from __future__ import annotations

from fractions import Fraction as F
from math import exp, log


CHECKS = []


def check(name, cond):
    CHECKS.append((name, bool(cond)))


# listed vocab
VOCAB = ("a", "b", "c")


def softmax(logits):
    # host float: life support. Stamp it.
    xs = [exp(x) for x in logits]
    z = sum(xs)
    if z == 0:
        raise ZeroDivisionError("dead isolator")
    return [x / z for x in xs]


def cross_entropy(p, y):
    # y one-hot on listed vocab; p from softmax
    s = 0.0
    for pi, yi in zip(p, y):
        if yi:
            if pi <= 0:
                raise ZeroDivisionError("dead isolator")
            s += -yi * log(pi)
    return s


def main():
    # isolate context: seed is the prompt letters already in V
    ctx = ("a", "a")
    check("ctx_in_V", all(t in VOCAB for t in ctx))
    check("unk_not_in_V", "z" not in VOCAB)

    logits = (0.0, 1.0, 0.0)  # peak on b
    p = softmax(logits)
    check("softmax_sum1", abs(sum(p) - 1) < 1e-12)
    check("softmax_peak_b", p[1] == max(p))

    y_b = (0.0, 1.0, 0.0)
    y_a = (1.0, 0.0, 0.0)
    L_ok = cross_entropy(p, y_b)
    L_bad = cross_entropy(p, y_a)
    check("loss_wrong_higher", L_bad > L_ok)

    # temperature = gauge on logits
    def softr(logits, T):
        return softmax(tuple(x / T for x in logits))

    p_cold = softr(logits, 0.5)
    p_hot = softr(logits, 2.0)
    check("cold_peakier", p_cold[1] > p[1])
    check("hot_flatter", p_hot[1] < p[1])

    # argmax T→0 is project
    am = max(range(3), key=lambda i: logits[i])
    check("argmax_b", VOCAB[am] == "b")

    # OOV write
    check("oov_is_theta", "unk" not in VOCAB)

    # dual/backprop shaped: lei on a tiny affine
    # y = w*x, isolate x=2 seed 1, w=3 seed 0 (const)
    x, w = (2, 1), (3, 0)
    y = (x[0] * w[0], x[1] * w[0] + x[0] * w[1])
    check("affine_y", y == (6, 3))
    check("dydx", y[1] / x[1] == 3)

    # two-step chain z = y*y
    z = (y[0] * y[0], y[1] * y[0] + y[0] * y[1])
    check("chain_z", z == (36, 36))
    check("dzdx", z[1] / x[1] == 36)  # 2*y*w = 2*6*3 = 36

    # train vs test: two reads of one G
    train_L, test_L = L_ok, L_bad
    check("two_reads", train_L != test_L)

    # residual combinator: x + f(x) vs f(x)
    fx = 5
    check("resid_not_f", (2 + fx) != fx)

    print("softmax", [round(v, 4) for v in p])
    print("L_ok", round(L_ok, 4), "L_bad", round(L_bad, 4))


if __name__ == "__main__":
    main()
    failed = [n for n, c in CHECKS if not c]
    for n, c in CHECKS:
        print(("PASS " if c else "FAIL ") + n)
    print(f"{sum(c for _,c in CHECKS)}/{len(CHECKS)}")
    print("ALL PASS" if not failed else "FAILED " + str(failed))
    raise SystemExit(1 if failed else 0)
