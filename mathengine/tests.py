#!/usr/bin/env python3
from engine import Theta, certify, isolate, mix, rate, rel, run, weigh


def main():
    r = run("x*x", 3)
    assert r["gauge"] and weigh(r["rate"], rel(6, 1)), r
    assert weigh(r["value"], rel(9, 1)), r
    r = run("x*x+2*x", 3)
    assert weigh(r["rate"], rel(8, 1)) and weigh(r["value"], rel(15, 1)), r
    r = run("x**3", "2/3")
    assert r["gauge"] and weigh(r["rate"], rel(4, 3)), r
    assert weigh(r["value"], rel(8, 27)), r
    rows = certify("x*x", (2, 3, -1), (1, 2, -1))
    assert weigh(rows[1]["rate"], rel(6, 1))
    x = isolate(3, 2)
    assert weigh(rate(mix(x, x), x), rel(6, 1))
    try:
        isolate(3, 0)
        raise SystemExit("missed seed 0")
    except Theta:
        pass
    try:
        run("", 1)
        raise SystemExit("missed empty")
    except Theta:
        pass
    print("TESTS PASS")


if __name__ == "__main__":
    main()
