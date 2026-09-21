# Cut and ledger

A claim names **V** (listed letters), **G** (maps), **θ** (refuse).
A rate is two live channels: `P.r / G.r`.
A name isolates some slots and ignores others so a distinction can travel.

```
python3 verify_all.py
```

8 gates. 161 paid rows if this page is current.

---

## Use

1. List `Vv` and `Vr` (add `Vq` / `Vt` if you write them).
2. Pick a meet and a combinator, or run `forge.py`.
3. Isolate writes a seed. Seed must sit in `Vr`. No default seed if you want partiality visible.
4. Rate needs both slots of both pairs.
5. Write leaves V: wrap, grow V on the page, change combinator, or θ.
6. `=` is tick, wrap, val, or mint. Pick one.
7. Leftover stays on the page.
8. Post to `accountant.py`: G, V, mint, writes-by-slot. Leak without θ is `BooksError`.

---

## Paid numbers

| claim | value | runner |
|---|---|---|
| bit host Leibniz leaks | `(1,1)*(1,1)=(1,2)` | test_slots 35/35 |
| wrap-Leibniz Z/2,3,4,5,7 | closed | test_slots |
| wrap vs host Z/2 | 15 agree, 1 differs | test_slots |
| triangular leak `Vr=0..m-1` host `+` | C(m,2) = 1,3,6,10,15,21,28 | test_slots |
| bit combinators of `r·w` and `v·s` | 16/16 closed | forge.py |
| seed 2 into bit-`Vr` | does not land | test_affect 20/20 |
| Peano `numeral(3)` | 3 ticks | foundations.py |
| `isolate_import(3)` | 1 tick | foundations.py |
| `isolate_from_peano(3)` | 4 ticks | foundations.py |
| traveler L=0 vs L=8 to 50 | 50 vs 450 ticks | drag.py |
| `i*i` host | `(-1,0)` | complex / recover 29/29 |
| wrap Z/2 complex `i*i` | `(1,0)` equals split | complex.py |
| `P(even given gt3)` | 2/3 | recover.py |
| `P(* given empty)` | θ | recover.py |
| Bayes `P(fair given 6)` | 1/4 | recover.py |
| `XZ|0>` vs `ZX|0>` | not equal | recover.py |
| Born phase-kill | Born(ψ)=Born(-ψ)=Born(iψ)=1 | recover.py |
| η 3+1 | 1,-1,-1,-1; null 0 | listed_field 30/30 |
| boost β=3/5 γ=5/4 | η holds | listed_field |
| plaquette u-then-v vs v-then-u | (1,2) vs (1,1) | listed_field |
| φ⁴, 4 sites, φ in {-1,0,1} | 81 configs; unique S=0 | listed_field |
| vacuum matter vs geom | 0 ≠ 1 | listed_field |
| [a,a†] leftover | 1 at n=0,1,5 | prior 14/14 |
| add-then-born vs born-then-add | 25/36 ≠ 13/36 | prior.py |
| Bell (1,0,0,1) factors | no | prior.py |
| pile merge count vs volume | 4→1 vs 2+2=4 | piles.py |
| journal leak without θ | BooksError | accountant 8/8 |
| lei then complex vs complex then lei | (-3,4) vs (0,0) | break.py |

---

## Maps

| file | payload |
|---|---|
| [CUT.md](CUT.md) | naming isolates slots; apparatus and journal are two cuts |
| [COMPRESS.md](COMPRESS.md) | noun = lossy compress; P/C/N = bad books |
| [BOOKS.md](BOOKS.md) | 2-line school + vs 10-line merge |
| [ACCOUNTANT.md](ACCOUNTANT.md) | journal rules |
| [PILES.md](PILES.md) | 2+2 as merge; count 1, volume 4 |
| [CONTRADICTION.md](CONTRADICTION.md) | C1–C15 incompatibles under one word |
| [ERROR_TAXONOMY.md](ERROR_TAXONOMY.md) | 30 construction errors |
| [SELF_AUDIT.md](SELF_AUDIT.md) | this stack; unravel vs fill |
| [ACCOUNTING.md](ACCOUNTING.md) | P primitive, C conflate V/G, N nest |
| [DEBUG_MATH.md](DEBUG_MATH.md) | debug math as those postings |
| [LIFESUPPORT.md](LIFESUPPORT.md) | patches after G left V |
| [FOUNDATIONS.md](FOUNDATIONS.md) | Peano vs isolate; unsplittable pair |
| [DRAG.md](DRAG.md) | fake constants; four distinction G |
| [COMPLEX.md](COMPLEX.md) | dual / complex / split / idempotent |
| [INSIGHTS.md](INSIGHTS.md) | slots, 16 combinators, workbook cut |
| [MACHINES.md](MACHINES.md) | QM GR stats as one stack |
| [RECOVER.md](RECOVER.md) | finite Ω, C², 1+1 η |
| [DE_REIFY.md](DE_REIFY.md) | ghosts vs prior G |
| [SCIENCE_MAP.md](SCIENCE_MAP.md) | science models as eight writes |
| [LISTED_INSIGHT.md](LISTED_INSIGHT.md) | listed φ⁴, 3+1, plaquette |
| [BREAK_LOG.md](BREAK_LOG.md) | cross-wired G |
| [MAP.md](MAP.md) [SLOTS.md](SLOTS.md) [AFFECT.md](AFFECT.md) | earlier slot maps |

---

## Construction errors that fire first

1. Output booked as primitive.
2. Host booked as ground.
3. Project, then call the projection the system.
4. One combinator sold as essence.
5. Leftover sent to 0.

Full list: [ERROR_TAXONOMY.md](ERROR_TAXONOMY.md). This kernel still carries default seed 1, one `Q()` for two slots, host Leibniz hardcoded, `rate` as a Fraction, mint as a string ([SELF_AUDIT.md](SELF_AUDIT.md)).

---

## Falsifiers

- `lei_plus((1,1),(1,1))` lands in bit pairs: leak claim dies.
- wrap-Leibniz on Z/5 leaks: finite-host claim dies.
- `Lr` on `Vr=0..6` is not 21: triangular claim dies.
- `isolate_import(3)` bills 3 S: unpaid-numeral claim dies.
- vacuum quartic equals plaquette letter: `not_einstein_vac` dies.
- Born distinguishes ψ from -ψ: projection-as-Born dies.
- `P(A given B)` with `P(B)=0` lands: dead-isolator claim dies.
- pile merge posts count 4: count-read claim dies.
- seed 2 into bits posts without θ: journal claim dies.

If `verify_all.py` is not green, this page is stale.

---

## Runners without a gate line

```
python3 foundations.py
python3 drag.py
python3 complex.py
python3 piles.py
python3 books.py
python3 contradiction.py
python3 break.py
python3 machines.py
```

They print. They do not fail the 161-row gate.
