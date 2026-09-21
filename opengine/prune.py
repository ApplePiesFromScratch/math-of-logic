#!/usr/bin/env python3
"""Delete maps the current cut does not support. 'I' is a compress that wants to stay."""
from __future__ import annotations

from mini_me import ATLAS, Cut, Map, Mini


def supported(m: Map, cut: Cut) -> bool:
    return m.hit(cut)


def demo():
    mind = Mini(name="mind")
    # the I-map: treats a self-letter as primitive
    I = Map("I", ("self",), "compress of seeing, booked as agent")
    mind.ingest([I])

    piles = Cut(
        "piles",
        "merge",
        frozenset({1, 4, "front"}),
        {"loc": "front"},
        {"school+": 4, "count": 1},
    )
    print("before", [m.name for m in mind.maps])
    kept = [m for m in mind.maps if supported(m, piles)]
    dropped = [m.name for m in mind.maps if m not in kept]
    mind.maps = kept
    print("after piles, kept", [m.name for m in mind.maps])
    print("dropped (unsupported)", dropped)

    selfcut = Cut(
        "think",
        "compress",
        frozenset({"mind", "I"}),
        {"self": "mind"},
        {},
    )
    mind.ingest([I])  # thinking puts I back as primitive
    print("thinking rebooks I", "I" in [m.name for m in mind.maps])
    kept = [m for m in mind.maps if supported(m, selfcut)]
    dropped = [m.name for m in mind.maps if m not in kept]
    mind.maps = kept
    print("after self-cut kept", [m.name for m in mind.maps])
    print("dropped", dropped)

    # terrain changes: no self letter
    mind.maps = kept + [I]
    empty = Cut("gone", "none", frozenset(), {}, theta="no self")
    kept = [m for m in mind.maps if supported(m, empty)]
    print("no-self terrain kept", [m.name for m in mind.maps if m in kept], "I dropped", I not in kept)


if __name__ == "__main__":
    demo()
