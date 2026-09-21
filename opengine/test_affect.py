#!/usr/bin/env python3
"""Prior affects that generate leak/close.  Invented G vs invalid G."""
from __future__ import annotations

from itertools import product

BITS = (0, 1)
P = [(v, r) for v in BITS for r in BITS]
CHECKS = []


def check(name, cond):
    CHECKS.append((name, bool(cond)))


def lands(fn):
    return all(fn(a, b)[0] in BITS and fn(a, b)[1] in BITS for a, b in product(P, P))


def rw(a, b):
    (v, r), (w, s) = a, b
    return (v * w, r * w)


def vs(a, b):
    (v, r), (w, s) = a, b
    return (v * w, v * s)


def lei_plus(a, b):
    (v, r), (w, s) = a, b
    return (v * w, r * w + v * s)


def lei_xor(a, b):
    (v, r), (w, s) = a, b
    return (v * w, (r * w) ^ (v * s))


def lei_or(a, b):
    (v, r), (w, s) = a, b
    return (v * w, (r * w) | (v * s))


def lei_max(a, b):
    (v, r), (w, s) = a, b
    return (v * w, max(r * w, v * s))


# each meet closed
check("meet_rw_closed", lands(rw))
check("meet_vs_closed", lands(vs))
# + of two closed writes is the leak
check("plus_is_the_leak", not lands(lei_plus))
check("the_write", lei_plus((1, 1), (1, 1)) == (1, 2))
# replace + with a closed combinator
check("lei_xor_closed", lands(lei_xor))
check("lei_or_closed", lands(lei_or))
check("lei_max_closed", lands(lei_max))
check("xor_char2", lei_xor((1, 1), (1, 1)) == (1, 0))
check("or_keeps_1", lei_or((1, 1), (1, 1)) == (1, 1))

# isolation prior
check("seed1_in_bits", 1 in BITS)
check("seed2_not_in_bits", 2 not in BITS)

# wrap fold == xor on this one pair
check("wrap_eq_xor_at_11", ((1 * 1) % 2, (1 + 1) % 2) == lei_xor((1, 1), (1, 1)))

# ε² = -1 equals ε² = 1 in char 2
check("neg1_is_1_mod2", (-1) % 2 == 1)

# invented valid G
def and_pair(a, b):
    return (a[0] & b[0], a[1] & b[1])


check("and_pair_closed", lands(and_pair))
check("and_pair_not_lei", and_pair((1, 1), (1, 1)) != lei_plus((1, 1), (1, 1)))

# invalid G: host + inside bit frame
check("host_plus_invalid_in_bits", not lands(lei_plus))

# mid-stream switch
check("switch_without_mu_leaks", lei_plus((1, 1), (1, 1))[1] not in BITS)
check("switch_after_mu_lands", lei_plus((1, 1), (1, 1))[1] in (0, 1, 2))

# dead isolate then any lei stays dead
check("dead_xor", lei_xor((1, 0), (1, 0)) == (1, 0))
check("dead_plus", lei_plus((1, 0), (1, 0)) == (1, 0))


if __name__ == "__main__":
    failed = [n for n, c in CHECKS if not c]
    for n, c in CHECKS:
        print(f"  {'PASS' if c else 'FAIL'} {n}")
    print(f"{sum(c for _, c in CHECKS)}/{len(CHECKS)}")
    print("ALL PASS" if not failed else "FAILED " + str(failed))
    raise SystemExit(1 if failed else 0)
