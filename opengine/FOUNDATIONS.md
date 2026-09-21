# Foundations :  generators, isolation, unsplittable pairs

```
python3 foundations.py
```

---

## 1. What Peano is

Peano is not a bag of numbers. It is a machine:

- letter `0` (pay 0)
- op `S` (pay 1 tick, write the next letter)
- induction: a property of all letters reached from `0` by `S`

Run:

```
numeral(0) ticks=0
numeral(1) ticks=1
numeral(3) ticks=3
3+2 = S^2(3) ticks=2
3*4 via plus ticks=12     # each of 4 pluses costs 3 S
```

`+` is iterate `S`. `*` is iterate `+`. The numeral `12` is an **output**. The process that wrote it cost 12 successors.

Treat `12` as a primitive container and those 12 ticks go off-book.

---

## 2. What the calculus that uses Peano is

The Q-kernel does this:

```
isolate(3) -> Reading(3, 1)   ticks=1   origin=imported
```

The `3` is not minted. It is a letter already sitting in the host. Isolate pays **1** for attaching a channel. It pays **0** for the numeral.

Same cut, Peano first:

```
isolate_from_peano(3) -> Reading(3, 1)   ticks=4   (3 S + 1 isolate)
```

Calculus `Reading +` on imported `3` and `2`:

```
host+ ticks=2 isolates, 0 S
Peano 3+2 ticks=2 S
```

Same integer answer. Different ledger. The calculus that “uses Peano” uses the **output alphabet** of Peano and runs host `+/*` as if those ops were not iterate-`S`.

**Difference:** Peano generates letters. Calculus writes channels on letters it did not generate. Gauge then looks like induction, but the alphabet it inducts over is the **seed list** `K`, not N.

```
gauge on K=(1, 2, 1/2, -1)  all slopes=6
```

That is “for all k in listed K.” It is not Peano induction.

---

## 3. What isolation is doing

Isolation is a **write**, not a discovery.

```
isolate : Vv × Vr  →  Vv × Vr
isolate(v, seed)   =  (v, seed)
```

Prior conditions:

- `v` must already be a letter of `Vv` (imported, or minted by Peano, or wrapped).
- `seed` must already be a letter of `Vr`. Seed `2` into bit-`Vr` does not land.

What it does **not** do:

- It does not generate `v`.
- It does not prove `v` exists.
- It does not make `r` a property of `v`.

What it does:

- It attaches a comparison channel so later mix has two slots to write.
- Seed `0` writes “dead.” Seed `1` writes “this is the cut.” Other seeds write other gauges.

Price: 1 isolate tick, plus whatever you paid to mint `v` and to have `seed` in `Vr`. The Q-kernel bills only the isolate tick. That is the unpaid Peano (and the unpaid `Vr=Q`).

Unary `D:(v,r)↦(r,0)` is the reverse write: dump the channel into the value slot. It lands iff `Vr ⊆ Vv`. Isolation and `D` are not symmetric unless the two alphabets were already the same.

---

## 4. A pair that cannot be separated

`xx = (9, 6)` after `x*x` at isolate(3,1).

```
project_v(xx) = 9     lost the slope; 9 does not remember 6
project_r(xx) = 6     lost the value; 6 of what?
rate(xx, x)   = 6     needs both slots of both pairs
```

The live pair under a shared cut is the thing rate reads. Split it and you have two letters that do not reconstruct the ratio.

That is not mysticism. It is projection:

- `π_v : Vv×Vr → Vv` is a map. It is not invertible.
- `π_r : Vv×Vr → Vr` is a map. It is not invertible.
- `rate` is `Vr_top / Vr_bottom` and needs the bottoms live.

A second unsplittable: **mint vs value**.

```
(9,6) from x² seed 1
(9,6) from 3x  seed 2
eq_val  = True
eq_mint = False
```

Val-eq is `A=A` on the output pair. It identifies two generators. Mint-eq keeps the generator. If you substitute after val-eq you write seed `2` into a slot that still thinks it is seed `1` (`2=0` as slots). The pair of *pairs* `(output, generator)` is what you must not split if you still need the generator.

A third: **numeral and its tick count**. `12` without `ticks=12` is Peano output treated as primitive.

---

## 5. What makes an equivalence framework stable

`=` is a G. It is stable on a model when:

1. It is a map of the listed V (writes a letter you named: yes/no, or a tick-read).
2. It does not identify letters you still use as distinct inputs to a later G.
3. The cost of a weigh sits on the ledger (tick, wrap, mint).

Unstable patterns we already ran:

| G | what it identifies | what breaks later |
|---|---|---|
| val-eq on pairs | `x²` seed1 with `3x` seed2 | slot `2` vs `0` |
| wrap-eq on Z/2 | host `2` with `0` | host Leibniz vs wrap Leibniz |
| `all([])` | empty grid with “all seeds ok” | vacuous certificate |
| S5 `A=A` free | a world with its own box | see-blind frames |

Stable on a listed cut:

- Tick-eq: `read(a)=read(b)` at declared tick. `5` and `2` match at tick 3? No. `5` and `5` match, cost 1 weigh.
- Mint-eq: same pair and same generator.
- Gauge-eq of *rates*: many seeds, one ratio. That identifies readings, not numerals.

Peano `=` on numerals is “same iterate-count from 0.” Cost is already in the numerals if you kept the ticks. Host `3==3` after import has paid 0 for that fact.

---

## 6. Outputs treated as primitive :  process and price

| output treated as thing | process that wrote it | unpaid if primitive |
|---|---|---|
| numeral `3` | `S³(0)` | 3 ticks |
| `3+2=5` | `S²(3)` | 2 ticks |
| `3*4=12` | iterate plus | 12 S |
| Q letter `½` | host `/` or named Fraction | Vq growth |
| Reading `(3,1)` | isolate after a numeral | 1 isolate; numeral often 0 |
| slope `6` | `rate` after Leibniz mix | two meets + combinator `+` + `/` into `Vq` |
| school `2x` | project `r` after mix, forget seed | unary `D` / property-of-v |
| wrap `0` from host `2` | `% 2` | a different G, not a rounding |
| `(9,6)` as “the” pair | val-eq of two mints | mint |

Price the process: name the G, count the ticks or name the leak. If the ledger shows 0 and a letter appeared, the generator is off-book.

---

## 7. The stack, smallest first

```
0
S                         # Peano write
numeral                   # output of S-iterates
isolate                   # write a channel onto a numeral
meet r·w, meet v·s        # two closed writes on bits
combinator (+ / xor / or) # + leaks on bits; xor closes
rate = r_top / r_bot      # writes Vq
π_v or π_r                # kills the pair
val-eq                    # kills the mint
```

Calculus textbooks start at “numeral” or even at “slope.” Peano starts at `0` and `S`. Isolation sits between numeral and mix. Equivalence sits on whatever you still need to tell apart.

---

## 8. Falsifiers

- If `isolate_import(3)` bills 3 S, the unpaid-numeral claim dies.
- If `project_v(xx)` plus a rule recovers `6` without storing `r`, the pair was never needed.
- If val-eq of `(9,6)` keeps slot `2` distinct from slot `0`, mint was already in `=`.
- If gauge on `{1,2}` fails to agree on Q-host `x²` at 3, the Q-kernel is not the machine we ran.
