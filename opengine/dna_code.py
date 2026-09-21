#!/usr/bin/env python3
"""Code/hardware letters this process is made of."""
from __future__ import annotations

import struct
import sys


def bits8(n):
    return format(n & 255, "08b")


def main():
    print("=== D1 V2 is voltage-shaped only after a threshold G ===")
    print("  letters", (0, 1))
    print("  AND", 1 & 1, 1 & 0)
    print("  XOR", 1 ^ 1, 1 ^ 0)
    print("  host +", 1 + 1, "leaves V2")

    print("=== D2 wrap 256 vs host int ===")
    print("  255+1 host", 255 + 1)
    print("  255+1 byte", (255 + 1) & 255)
    print("  bits", bits8(255), bits8(256))

    print("=== D3 IEEE: 0.1+0.2 ===")
    s = 0.1 + 0.2
    print("  ", s, "eq 0.3", s == 0.3)
    print("  hex", float.hex(s), float.hex(0.3))

    print("=== D4 NaN is not a letter of Q and is not eq to itself ===")
    n = float("nan")
    print("  nan==nan", n == n, "nan is nan", n is n)

    print("=== D5 intern: two mints one object ===")
    a, b = (1, 2), (1, 2)
    print("  val", a == b, "id", a is b, hex(id(a)), hex(id(b)))
    x, y = 256, 256
    u, v = 257, 257
    print("  256 is 256", x is y, "257 is 257", u is v)

    print("=== D6 pointer / id is a mint letter ===")
    print("  id(())", id(()), "id([])", id([]), "id([])", id([]))

    print("=== D7 overflow to Inf ===")
    big = 1e308 * 10
    print("  ", big, "is inf", big == float("inf"))

    print("=== D8 struct pack: same bits two reads ===")
    bits = struct.pack(">f", 1.0)
    as_int = struct.unpack(">I", bits)[0]
    print("  float 1.0 bits", hex(as_int), "as int", as_int)

    print("=== D9 recursion limit θ ===")
    print("  rec limit", sys.getrecursionlimit())

    print("=== D10 True+True host ===")
    print("  ", True + True, "bool subclass of int", issubclass(bool, int))

    print("=== D11 hash as wrap-shaped read ===")
    print("  hash(1)", hash(1), "hash(1.0)", hash(1.0), "eq", (1 == 1.0))

    print("=== D12 byteorder ===")
    print(" ", sys.byteorder, "int 1 as 2 bytes", (1).to_bytes(2, sys.byteorder))


if __name__ == "__main__":
    main()
