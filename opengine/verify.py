#!/usr/bin/env python3
from engine import AND_min, AND_prod, V2, V3, V4, split_report
from systems import ALLOW, DENY, MAYBE, admit, compare_versions, flag_and_v2, flag_and_v3

ok = []


def check(name, cond):
    ok.append((name, bool(cond)))


check("v2_min_closed", V2.scan_binary(AND_min, "m")["closed"])
check("v2_prod_closed", V2.scan_binary(AND_prod, "p")["closed"])
check("v2_coincide", split_report(V2, V3, AND_min, AND_prod, "m", "p")["coincide_on_small"])
check("v3_split", split_report(V2, V3, AND_min, AND_prod, "m", "p")["split"])
check("v3_prod_leak", not V3.scan_binary(AND_prod, "p")["closed"])
check("v3_min_closed", V3.scan_binary(AND_min, "m")["closed"])
check("v4_prod_leak", not V4.scan_binary(AND_prod, "p")["closed"])
r = compare_versions((DENY, ALLOW), (DENY, ALLOW, MAYBE), flag_and_v2, "and2")
check("flag_old_and_collapses_maybe", r["collapsed_new_letters"])
check("flag_v3_honest", admit(__import__("engine").Engine("f3", (DENY, ALLOW, MAYBE)), flag_and_v3, name="and3")["ship"])

failed = [n for n, c in ok if not c]
print("\n".join(f"  {'PASS' if c else 'FAIL'} {n}" for n, c in ok))
print(f"{sum(c for _, c in ok)}/{len(ok)}")
print("ALL PASS" if not failed else "FAILED " + str(failed))
raise SystemExit(1 if failed else 0)
