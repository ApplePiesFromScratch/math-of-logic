#!/usr/bin/env python3
"""Process language. A program is a list of cuts. Leak without θ is fail."""
from __future__ import annotations

from dataclasses import dataclass, field


class PFail(Exception):
    pass


@dataclass
class State:
    V: set = field(default_factory=set)
    G: str = ""
    mint: str = ""
    writes: dict = field(default_factory=dict)
    reads: dict = field(default_factory=dict)
    theta: str | None = None
    book: list = field(default_factory=list)
    maps: set = field(default_factory=lambda: {"named-G"})


def parse_val(s):
    s = s.strip()
    if s.startswith('"') and s.endswith('"'):
        return s[1:-1]
    try:
        return int(s)
    except ValueError:
        return s


class PLang:
    def __init__(self):
        self.st = State()

    def line(self, raw: str):
        raw = raw.split("#")[0].strip()
        if not raw:
            return
        parts = raw.split()
        op, args = parts[0], parts[1:]
        st = self.st
        if op == "V":
            st.V = {parse_val(a) for a in args}
        elif op == "G":
            st.G = args[0] if args else ""
        elif op == "mint":
            st.mint = " ".join(args)
        elif op == "write":
            for a in args:
                k, _, v = a.partition("=")
                st.writes[k] = parse_val(v)
        elif op == "read":
            k, _, v = args[0].partition("=")
            st.reads[k] = parse_val(v)
        elif op == "theta":
            st.theta = " ".join(args) or "refused"
        elif op == "clear":
            st.writes.clear()
            st.reads.clear()
            st.theta = None
        elif op == "post":
            self.post()
        elif op == "prune":
            # keep maps whose name appears in reads or writes keys or book last hits
            supported = set(st.writes) | set(st.reads)
            if st.theta:
                supported.add("leak")
            st.maps = {m for m in st.maps if m in supported or m == "named-G"}
        elif op == "map":
            st.maps.add(args[0])
        elif op == "need":
            # need KEY=VAL lands in last post
            self.need(args)
        else:
            raise PFail(f"unknown op {op}")

    def post(self):
        st = self.st
        if not st.G:
            raise PFail("G missing")
        if not st.V:
            raise PFail("V missing")
        if not st.mint:
            raise PFail("mint missing")
        if not st.writes and not st.theta:
            raise PFail("writes missing")
        lands = True
        for letter in st.writes.values():
            if letter not in st.V:
                lands = False
        if not lands and not st.theta:
            raise PFail(f"leak {st.writes} no theta")
        if lands and st.theta:
            raise PFail("theta on landing write")
        rec = {
            "G": st.G,
            "V": frozenset(st.V),
            "mint": st.mint,
            "writes": dict(st.writes),
            "reads": dict(st.reads),
            "theta": st.theta,
            "lands": lands,
        }
        st.book.append(rec)
        return rec

    def need(self, args):
        if not self.st.book:
            raise PFail("need on empty book")
        last = self.st.book[-1]
        for a in args:
            k, _, v = a.partition("=")
            if k == "lands":
                want = v == "1"
                if last["lands"] != want:
                    raise PFail(f"lands {last['lands']} want {want}")
            elif k == "theta":
                if bool(last["theta"]) != (v == "1"):
                    raise PFail("theta flag")
            elif k in last["writes"]:
                if last["writes"][k] != parse_val(v):
                    raise PFail(f"write {k}")
            elif k in last["reads"]:
                if last["reads"][k] != parse_val(v):
                    raise PFail(f"read {k}")
            else:
                raise PFail(f"need unknown {k}")

    def run(self, src: str):
        for i, raw in enumerate(src.splitlines(), 1):
            try:
                self.line(raw)
            except PFail as e:
                raise PFail(f"L{i}: {e}") from e
        return self.st


PROG = """
V 0 1 2 3
G isolate
mint x
write v=3 r=1
post
need lands=1

clear
V 0 1
G isolate
mint seed2
write v=1 r=2
theta r not in V
post
need lands=0 theta=1

clear
V 0 1 4 front
G merge
mint piles
write loc=front piles=1 vol=4
read school+=4
read count=1
post
need lands=1 count=1 school+=4

map two-reads
map leak
prune
"""


def main():
    p = PLang()
    p.run(PROG)
    print("posts", len(p.st.book))
    print("maps after prune", p.st.maps)
    print("ok piles reads", p.st.book[2]["reads"])

    # leak without theta must fail
    q = PLang()
    try:
        q.run("V 0 1\nG isolate\nmint z\nwrite r=2\npost\n")
        print("FAIL expected PFail")
        return 1
    except PFail as e:
        print("caught leak-no-theta", str(e).startswith("L"))

    print("PLANG PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
