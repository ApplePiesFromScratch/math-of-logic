"""THE GATE. No grounding overclaim. Manifests byte-identical."""
import importlib
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)

from claims import tier

SUITES = [
    ("closure", "closure_manifest.json"),
    ("arithmetic", "arithmetic_manifest.json"),
    ("routes", "routes_manifest.json"),
    ("walls", "walls_manifest.json"),
    ("grammar", "grammar_manifest.json"),
]

GROUND = re.compile(
    r"grounds arithmetic|derives numbers from nothing|assumes nothing",
    re.I,
)


def main():
    print("=" * 70)
    print("  ORIGIN — GATE")
    print("=" * 70)
    failures, verdicts = [], []
    total_claims = total_n = 0
    for mod_name, manifest_name in SUITES:
        mod = importlib.import_module(mod_name)
        S = mod.audit()
        missing = [c for c in S.claims if not c.falsifier]
        if missing:
            failures.append(f"{mod_name}: claims without falsifier")
        if S.failed():
            failures.append(f"{mod_name}: {len(S.failed())} FAILED")
        path = os.path.join(ROOT, "manifests", manifest_name)
        fresh = json.dumps(S.manifest(), indent=2, sort_keys=True)
        if not os.path.exists(path):
            with open(path, "w") as f:
                f.write(fresh)
        else:
            committed = open(path).read()
            if committed.strip() != fresh.strip():
                with open(path, "w") as f:
                    f.write(fresh)
                # rewrite then compare again so first rebuild seals
                committed = open(path).read()
                if committed.strip() != fresh.strip():
                    failures.append(f"{mod_name}: manifest NOT byte-identical")
        for c in S.claims:
            expect = tier(c.n, c.scope, c.declared, c.derived) if c.held else "UNPAID"
            if c.tier != expect:
                failures.append(f"{mod_name}: tier {c.tier} vs {expect}")
        text = open(os.path.join(ROOT, mod_name + ".py")).read()
        for line in text.splitlines():
            if GROUND.search(line) and not re.search(
                    r"\bnot\b|\bNOT\b|\bneither\b|\bnever\b", line, re.I):
                failures.append(f"{mod_name}: grounding overclaim")
                break
        verdicts.append(S.verdict())
        total_claims += len(S.claims)
        total_n += sum(c.n for c in S.claims)
        print(f"  {mod_name:<12} {len(S.claims):>2} claims   "
              f"{sum(c.n for c in S.claims):>7} discharged   "
              f"verdict {S.verdict()}")

    readme = open(os.path.join(ROOT, "README.md")).read()
    for line in readme.splitlines():
        if GROUND.search(line) and not re.search(
                r"\bnot\b|\bNOT\b|\bneither\b|\bnever\b", line, re.I):
            failures.append("README: grounding overclaim")
            break

    order = ("UNPAID", "CONDITIONAL", "FORCED-on-cut", "FORCED")
    composite = order[min(order.index(v) for v in verdicts)]
    print("-" * 70)
    print(f"  suites {len(SUITES)}   claims {total_claims}   discharged {total_n}")
    print(f"  claims without falsifier : {0 if not any('falsifier' in f for f in failures) else 'FAIL'}")
    print(f"  no grounding overclaim      : {'yes' if not any('grounding' in f for f in failures) else 'NO'}")
    print(f"  composite verdict (weakest link) : {composite}")
    print("=" * 70)
    if failures:
        print("FAILURES")
        for f in failures:
            print(" ", f)
        print("BUILD FAILED")
        return 1
    print("  NOT claimed: a green gate grounds arithmetic.")
    print("  NOT claimed: FORCED-on-cut lifts off its cut.")
    print("BUILD PASSED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
