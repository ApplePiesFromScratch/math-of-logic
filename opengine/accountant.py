#!/usr/bin/env python3
"""Journal for formal systems.

A post names G, V, mint, writes-by-slot.
If a write is not in V, θ is required. Silent credit is refused.
"""
from __future__ import annotations

from dataclasses import dataclass, field


KINDS = (
    "isolate",
    "successor",
    "meet",
    "combinator",
    "read",
    "project",
    "accumulate",
    "refuse",
    "migrate",
    "merge",
)


class BooksError(Exception):
    pass


@dataclass
class Post:
    kind: str
    G: str
    V: frozenset
    mint: str
    writes: dict          # slot -> letter
    lands: bool
    theta: str | None = None
    reads: dict = field(default_factory=dict)   # extra named reads of the same write
    leftover_of: tuple | None = None


class Journal:
    def __init__(self):
        self.lines: list[Post] = []

    def post(self, **kw):
        kind = kw.get("kind")
        G = kw.get("G")
        V = kw.get("V")
        mint = kw.get("mint")
        writes = kw.get("writes")
        if kind not in KINDS:
            raise BooksError(f"kind {kind!r}")
        if not G:
            raise BooksError("G missing")
        if V is None:
            raise BooksError("V missing")
        if not mint:
            raise BooksError("mint missing")
        if not writes:
            raise BooksError("writes missing")
        V = frozenset(V)
        lands = all(letter in V for letter in writes.values())
        theta = kw.get("theta")
        if not lands and not theta:
            raise BooksError(f"leak {writes} not in V; θ required")
        if lands and theta:
            raise BooksError("θ on a landing write")
        p = Post(
            kind=kind,
            G=G,
            V=V,
            mint=mint,
            writes=dict(writes),
            lands=lands,
            theta=theta,
            reads=dict(kw.get("reads") or {}),
            leftover_of=kw.get("leftover_of"),
        )
        self.lines.append(p)
        return p

    def leaks(self):
        return [p for p in self.lines if not p.lands]

    def by_kind(self, kind):
        return [p for p in self.lines if p.kind == kind]


CHECKS = []


def check(name, cond):
    CHECKS.append((name, bool(cond)))


def demo():
    j = Journal()

    j.post(kind="successor", G="S", V={0, 1, 2, 3}, mint="S(2)", writes={"n": 3})
    j.post(
        kind="isolate",
        G="isolate",
        V={0, 1, 2, 3},
        mint="isolate imported 3 seed1",
        writes={"v": 3, "r": 1},
    )
    try:
        j.post(
            kind="isolate",
            G="isolate",
            V={0, 1},
            mint="seed2 on bits",
            writes={"v": 1, "r": 2},
        )
        check("seed2_refused_without_theta", False)
    except BooksError:
        check("seed2_refused_without_theta", True)

    j.post(
        kind="isolate",
        G="isolate",
        V={0, 1},
        mint="seed2 on bits",
        writes={"v": 1, "r": 2},
        theta="r=2 not in Vr",
    )

    j.post(
        kind="combinator",
        G="lei+",
        V={0, 1},
        mint="(1,1)*(1,1)",
        writes={"v": 1, "r": 2},
        theta="r=2 leak",
        leftover_of=("lei+", "xor", (1, 2), (1, 0)),
    )
    j.post(
        kind="combinator",
        G="xorlei",
        V={0, 1},
        mint="(1,1)*(1,1)",
        writes={"v": 1, "r": 0},
    )

    j.post(
        kind="merge",
        G="merge-front",
        V={"left", "right", "front", 1, 2, 4},
        mint="piles",
        writes={"loc": "front", "piles": 1, "vol": 4},
        reads={"school+": 4, "count": 1},
    )

    j.post(
        kind="read",
        G="rate",
        V={6, 9, 3, 1},
        mint="xx/x at 3 seed1",
        writes={"q": 6},
        reads={"top.r": 6, "bot.r": 1},
    )

    check("n_posts", len(j.lines) == 7)
    check("leaks_2", len(j.leaks()) == 2)
    check("xor_lands", j.lines[4].lands)
    check("pile_two_reads", j.lines[5].reads["school+"] == 4 and j.lines[5].reads["count"] == 1)
    check("lei_has_leftover", j.lines[3].leftover_of[3] == (1, 0))

    try:
        Journal().post(kind="read", G="rate", V={6}, mint="x", writes={})
        check("empty_writes_refused", False)
    except BooksError:
        check("empty_writes_refused", True)

    try:
        Journal().post(kind="read", G="", V={1}, mint="x", writes={"q": 1})
        check("empty_G_refused", False)
    except BooksError:
        check("empty_G_refused", True)

    return j


if __name__ == "__main__":
    demo()
    failed = [n for n, c in CHECKS if not c]
    for n, c in CHECKS:
        print(("PASS " if c else "FAIL ") + n)
    print(f"{sum(c for _,c in CHECKS)}/{len(CHECKS)}")
    print("ALL PASS" if not failed else "FAILED " + str(failed))
    raise SystemExit(1 if failed else 0)
