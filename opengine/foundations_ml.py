#!/usr/bin/env python3
"""Foundations under ML nouns: isolate, =, listed Ω, leftover, cut."""
from __future__ import annotations

from math import log


def L(w, pts):
    return sum((w * x - y) ** 2 for x, y in pts)


def main():
    print("=== F1 two examples, val-eq vs mint ===")
    e1, e2 = (1, 2), (1, 2)
    print("  val-eq", e1 == e2, "mint-eq", e1 is e2)
    print("  i.i.d. books val-eq")

    print("=== F2 ERM on listed Ω vs extra point ===")
    train = ((1, 2), (2, 4))
    test = ((3, 5),)
    print("  L(2) train", L(2, train), "L(2) test", L(2, test))
    print("  L(0) train", L(0, train), "L(0) test", L(0, test))

    print("=== F3 empty Ω ===")
    print("  L(2) empty", L(2, ()), "  all([]) shaped")

    print("=== F4 feature cut: drop x, keep y ===")
    pts = ((1, 2), (2, 4), (3, 6))
    ys = [y for _, y in pts]
    print("  ys", ys, "cannot recover w from ys alone")

    print("=== F5 two inits, one architecture ===")
    print("  mint A w0=0 L", L(0, train), "mint B w0=1 L", L(1, train))
    print("  same G, two seeds")

    print("=== F6 softmax as μ, not as P-in-the-token ===")
    p = [0.1, 0.8, 0.1]
    print("  read on V", p, "sum", sum(p))
    print("  letter b does not own 0.8; the read does")

    print("=== F7 CE leftover of two μ ===")
    y = [0, 1, 0]
    ce = -sum(yi * log(pi) for yi, pi in zip(y, p) if yi)
    print("  CE(p, onehot_b)", round(ce, 4))
    print("  CE(y,y)", 0.0)

    print("=== F8 next-token = isolate prefix, read V ===")
    V = ("a", "b", "c")
    prefix = ("a",)
    print("  prefix in V", all(t in V for t in prefix))
    print("  write is a letter of V, not a thought")

    print("=== F9 step-G iterate is Peano-shaped ===")
    w = 0.0
    for t in range(3):
        # dL/dw on train at w: 2(w-2)+2(2w-4)*2 = 10w-20
        g = 10 * w - 20
        w = w - 0.1 * g
        print(f"  tick {t+1} w={w} Ltrain={L(w, train)}")

    print("=== F10 capacity: listed w in {-1,0,1,2,3} ===")
    Ws = (-1, 0, 1, 2, 3)
    best = min(Ws, key=lambda w: L(w, train))
    print("  listed-best", best, "L", L(best, train), "missed w=2.1 L", L(2.1, train))


if __name__ == "__main__":
    main()
