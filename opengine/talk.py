#!/usr/bin/env python3
"""Tiny poster. Listed vocab. Train on labeled cuts. Talk in strings.

Stability = a label that keeps landing under the current bag.
Unsupported labels drop.
"""
from __future__ import annotations

VOCAB = (
    "pile", "count", "volume", "four", "one", "merge",
    "leak", "two", "bits", "seed", "rate", "self", "i",
    "theta", "leftover", "plus", "train", "test",
)
LABELS = ("two-reads", "leak", "I", "rate", "leftover")


def bag(text):
    w = text.lower().replace(",", " ").split()
    return {t: w.count(t) for t in VOCAB}


def score(weights, b):
    out = {}
    for lab in LABELS:
        s = 0.0
        for t in VOCAB:
            s += weights[lab][t] * b[t]
        out[lab] = s
    return out


def step(weights, b, target, eta=0.3):
    """One listed-label hinge-ish step. target is a set of labels that should win."""
    sc = score(weights, b)
    for lab in LABELS:
        y = 1.0 if lab in target else 0.0
        pred = 1.0 if sc[lab] > 0.5 else 0.0
        err = y - pred
        if err == 0:
            continue
        for t in VOCAB:
            weights[lab][t] += eta * err * b[t]


def stable(sc, thresh=0.5):
    return [lab for lab, v in sc.items() if v >= thresh]


TRAIN = [
    ("two piles merge count one volume four", {"two-reads"}),
    ("volume four plus school", {"two-reads"}),
    ("leak r two on bits theta", {"leak"}),
    ("seed two not in bits theta leak", {"leak"}),
    ("i self thinking primitive", {"I"}),
    ("self letter booked as i", {"I"}),
    ("rate six over one", {"rate"}),
    ("leftover two paths compose", {"leftover"}),
    ("train leftover test leftover", {"leftover"}),
]


def talk(weights, line):
    b = bag(line)
    sc = score(weights, b)
    hits = stable(sc)
    dropped = [lab for lab in LABELS if lab not in hits]
    return hits, dropped, sc


def main():
    weights = {lab: {t: 0.0 for t in VOCAB} for lab in LABELS}
    print("TRAIN")
    for epoch in range(8):
        for text, tgt in TRAIN:
            step(weights, bag(text), tgt)
    # show a couple weights
    print("  leftover.leftover", weights["leftover"]["leftover"])
    print("  I.self", weights["I"]["self"], "I.i", weights["I"]["i"])

    print("TALK")
    lines = [
        "two piles merge in front count one volume four",
        "seed two leak on bits theta",
        "i think self is primitive",
        "what is the rate",
        "compose two leftover paths",
        "hello weather banana",  # unsupported
        "i leftover leak",       # several
    ]
    for line in lines:
        hits, dropped, sc = talk(weights, line)
        pretty = {k: round(v, 2) for k, v in sc.items() if v}
        print(f"  > {line}")
        print(f"    hits {hits}  dropped {dropped}")
        print(f"    scores {pretty}")


if __name__ == "__main__":
    main()
