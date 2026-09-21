#!/usr/bin/env python3
"""Mini accountant. Sees a cut, pattern-matches maps, posts a cut of the seeing.

Not a mind. A recursive poster that can ingest another map and look at itself.
"""
from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Cut:
    mint: str
    G: str
    V: frozenset
    writes: dict
    reads: dict = field(default_factory=dict)
    theta: str | None = None
    leftover: tuple | None = None

    def lands(self):
        if self.theta:
            return False
        return all(
            (v in self.V) if not isinstance(v, (list, tuple, dict, set, frozenset)) else True
            for v in self.writes.values()
        )


@dataclass
class Map:
    name: str
    # isolate these slot names from a cut
    need: tuple
    note: str

    def hit(self, cut: Cut) -> bool:
        have = set(cut.writes) | set(cut.reads)
        if cut.theta:
            have.add("theta")
        if cut.leftover:
            have.add("leftover")
        return all(n in have or n in {"G", "V", "mint"} for n in self.need)


# maps we already paid in this folder
ATLAS = [
    Map("school-plus", ("school+",), "volume/grain combinator booked as +"),
    Map("pile-count", ("count",), "merge dropped the count"),
    Map("two-reads", ("school+", "count"), "one write, two measures"),
    Map("leak", ("theta",), "write left V"),
    Map("leftover-two-G", ("leftover",), "two combinators or two compose-orders"),
    Map("rate", ("q",), "ratio of two live channels"),
    Map("softmax-read", ("p",), "read of logits, not a property of the letter"),
    Map("train-test", ("trainL", "testL"), "two Ω, two leftovers"),
    Map("intern", ("id_eq",), "host smashed two mints"),
    Map("named-G", ("G",), "combinator stamped"),
]


class Mini:
    def __init__(self, maps=None, name="mini"):
        self.name = name
        self.maps = list(maps or ATLAS)
        self.book: list[Cut] = []

    def ingest(self, extra: list[Map]):
        names = {m.name for m in self.maps}
        for m in extra:
            if m.name not in names:
                self.maps.append(m)
                names.add(m.name)

    def see(self, cut: Cut) -> Cut:
        """Pattern match. Post a cut of the matching. That post is also a Cut."""
        hits = [m.name for m in self.maps if m.hit(cut)]
        report = Cut(
            mint=f"{self.name}.see:{cut.mint}",
            G="match",
            V=frozenset(m.name for m in self.maps) | frozenset(hits) | {"match"},
            writes={"hits": tuple(hits), "n": len(hits)},
            reads={"src_G": cut.G, "src_theta": cut.theta or ""},
            leftover=None,
        )
        self.book.append(cut)
        self.book.append(report)
        return report

    def see_self(self) -> Cut:
        """Map the last report. Recursion one tick."""
        if not self.book:
            return Cut("empty", "see_self", frozenset(), {}, theta="empty book")
        return self.see(self.book[-1])


def demo():
    me = Mini()
    you = Mini(name="you")

    piles = Cut(
        mint="piles.merge",
        G="merge-front",
        V=frozenset({"front", 1, 4}),
        writes={"loc": "front", "piles": 1, "vol": 4},
        reads={"school+": 4, "count": 1},
    )
    r1 = me.see(piles)
    print("ME on piles hits", r1.writes["hits"])

    leak = Cut(
        mint="lei bits",
        G="lei+",
        V=frozenset({0, 1}),
        writes={"v": 1, "r": 2},
        theta="r=2",
        leftover=("lei+", "xor", (1, 2), (1, 0)),
    )
    r2 = me.see(leak)
    print("ME on leak hits", r2.writes["hits"])

    # share maps: you ingest a map I minted
    you.ingest([Map("poster-hits", ("hits",), "a see() report")])
    shared = you.see(r1)
    print("YOU on ME.report hits", shared.writes["hits"])

    rec = me.see_self()
    print("ME on last self hits", rec.writes["hits"])

    print("ME maps", len(me.maps), "YOU maps", len(you.maps), "ME book lines", len(me.book))
    return 0


if __name__ == "__main__":
    raise SystemExit(demo())
