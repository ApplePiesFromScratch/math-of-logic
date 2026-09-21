#!/usr/bin/env python3
"""Systems API: throw a proposed op at a listed V before you ship it."""
from __future__ import annotations

from engine import Engine, LeavesV


def admit(engine: Engine, op, arity=2, name="op") -> dict:
    """Return a ship / no-ship card."""
    scan = engine.scan_binary(op, name) if arity == 2 else engine.scan_unary(op, name)
    card = {
        "ship": scan["closed"],
        "carrier": engine.name,
        "op": name,
        "closed": scan["closed"],
        "leaks": scan["leaks"],
        "props": scan.get("props") or {},
        "fix": None,
    }
    if not scan["closed"]:
        card["fix"] = (
            "G leaves V. Either refuse those inputs (theta), "
            "change G so every write lands, or grow V in public and rescan."
        )
    return card


def outputs_of(engine: Engine, op) -> set:
    seen = set()
    for a in engine.V:
        for b in engine.V:
            try:
                seen.add(op(a, b))
            except Exception:
                pass
    return seen


def compare_versions(old_V, new_V, op, name="op") -> dict:
    """Did adding states leak, or did the new letter get collapsed?"""
    old = Engine("old", old_V)
    new = Engine("new", new_V)
    a = old.scan_binary(op, name)
    b = new.scan_binary(op, name)
    added = set(new_V) - set(old_V)
    outs = outputs_of(new, op)
    collapsed = bool(added) and added.isdisjoint(outs) and b["closed"]
    return {
        "was_closed": a["closed"],
        "now_closed": b["closed"],
        "regressed": a["closed"] and not b["closed"],
        "collapsed_new_letters": collapsed,
        "new_leaks": b["leaks"],
        "outputs": outs,
    }


# --- example: feature flag grows from bool to tri-state ---

DENY, ALLOW, MAYBE = 0, 1, "maybe"


def flag_and_v2(a, b):
    return 1 if a == 1 and b == 1 else 0


def flag_and_broken_v3(a, b):
    # treat maybe as allow
    aa = 1 if a in (1, MAYBE) else 0
    bb = 1 if b in (1, MAYBE) else 0
    return 1 if aa and bb else 0


def flag_and_v3(a, b):
    if MAYBE in (a, b):
        if a == 0 or b == 0:
            return 0
        if a == 1 and b == 1:
            return 1
        return MAYBE
    return 1 if a == 1 and b == 1 else 0


if __name__ == "__main__":
    v2 = Engine("flags2", (DENY, ALLOW))
    v3 = Engine("flags3", (DENY, ALLOW, MAYBE))
    print("v2 and", admit(v2, flag_and_v2, name="and2")["ship"])
    print("v3 broken and", admit(v3, flag_and_broken_v3, name="and_mask")["ship"],
          "writes", flag_and_broken_v3(MAYBE, ALLOW))
    print("v3 honest and", admit(v3, flag_and_v3, name="and3")["ship"],
          admit(v3, flag_and_v3, name="and3")["props"])
    print("regression", compare_versions((0, 1), (0, 1, MAYBE), flag_and_v2, "and2"))
