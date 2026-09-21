#!/usr/bin/env python3
"""Play: listed rocket burns + a claim gate. No Inf Isp."""
from __future__ import annotations

from fractions import Fraction as F
from math import log


G0 = 9.80665


def dv(m0, mf, isp):
    if mf <= 0 or m0 <= mf or isp <= 0:
        raise ValueError("theta")
    return isp * G0 * log(m0 / mf)


def ln_series(x, n):
    """ln(1+u) series, x=1+u>0. Leftover vs math.log."""
    u = x - 1
    s = 0.0
    term = u
    for k in range(1, n + 1):
        s += term / k if k % 2 else -term / k
        term *= u
    return s


def main():
    print("=== two stage listed ===")
    # numbers toy-shaped, not a Starship claim
    stages = [
        dict(name="L", m0=5000, mf=1800, isp=330),
        dict(name="U", m0=1200, mf=400, isp=350),
    ]
    tot = 0.0
    for s in stages:
        d = dv(s["m0"], s["mf"], s["isp"])
        tot += d
        print(f"  {s['name']} dv={d:.1f} m/s  mass ratio {s['m0']/s['mf']:.3f}")
    print(f"  stacked dv={tot:.1f} m/s")

    print("=== ln leftover vs host log ===")
    r = 5000 / 1800
    host = log(r)
    for n in (3, 8, 20):
        # ln(r)=ln((1+u)) only if r~1; use ln(r)=ln(2.777) via host
        pass
    print("  host ln(5000/1800)", host)
    print("  3-term ln(1.2)", ln_series(1.2, 3), "host", log(1.2), "leftover", ln_series(1.2, 3) - log(1.2))

    print("=== claim gate ===")
    claims = [
        dict(text="dv 9000 with isp Inf", isp=float("inf"), m0=10, mf=1),
        dict(text="dv with mf=0", isp=330, m0=10, mf=0),
        dict(text="dv listed", isp=330, m0=5000, mf=1800),
    ]
    for c in claims:
        try:
            if c["isp"] == float("inf"):
                raise ValueError("theta Inf not in V")
            d = dv(c["m0"], c["mf"], c["isp"])
            print("  LAND", c["text"], round(d, 1))
        except (ValueError, ZeroDivisionError) as e:
            print("  THETA", c["text"], e)

    print("=== two reads: wet mass vs dv ===")
    print("  school credit: bigger stack better")
    print("  other read: dry mass leftover after burns", 400)


if __name__ == "__main__":
    main()
