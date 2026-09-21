# Fake constants, smoothness cost, distinction mechanics

```
python3 drag.py
python3 foundations.py
python3 affect.py
```

---

## 1. Relations sold as constants

| sold as constant | actually depends on | paid counterexample |
|---|---|---|
| `2` in `d(x²)=2x` | combinator and characteristic | wrap Z/2 → `(1,0)`, `2=0` |
| seed `1` as *the* unit | listed `Vr` | any `k∈Vr` gauges to 6 on Q-host `x²` at 3 |
| `3=3` | tick / wrap / mint | tick 3 reads `5` as `1`; wrap Z/2 reads `2` as `0` |
| `+` commutative and free | history of iterate-`S` | Peano `3+2` costs 2 S; import costs 0 |
| product rule *is* mix | which combinator | 16 bit combinators close; host `+` leaks |
| slope is a property of `v` | whether `r` is still attached | `π_v(9,6)=9` has no 6 |
| Q is “the” numbers | `Vv` vs `Vr` vs `Vq` | host `/` on Z/5 writes `½` not in Z/5 |
| smoothness / C∞ | every write lands | `Vr={0..m-1}` host `+` leaks `C(m,2)` |
| `A=A` | whether mint is kept | `(9,6)` from `x²` and from `3x` |
| dead `0` | dead channel vs empty V vs wrap-0 | wrap folds live `2` into dead `0` |
| leftover→0 | listed grid | Riemann leftover `1/192` at n=4 |
| `e`, `π` | series process | six-term geom leftover `1/32` |

None of these are “wrong on Q.” They are **context-locked** and sold without the lock.

---

## 2. Cost of smoothness, zero friction, zero drag

**Smoothness** here means: every small write still lands in V.

On a listed `Vr={0..m-1}`, host `+` does not land. Leaks `C(m,2)`.
The environment that makes host Leibniz look smooth is **Q (or Z) already `+closed`**. That closure is stipulated. It is not produced by the pair type.

Cost of that environment:

- You do not get to see `2` appear as a new letter. It was pre-loaded into `Vr`.
- You do not get a refuse when seed `7` is used. `7∈Q`.
- You do not see char. `2` never becomes `0`.
- Jets can write `2rs` forever. `Vt=Q` already has the `2`.

**Zero drag** (`L=0`): traveler speed `v=C/(C+L)=1`. Distance 50 costs **50** ticks.

```
L=0   ticks_to_50=50
L=1   100
L=2   150
L=8   450     # 9× the smooth path
L=12  650
```

**Friction-free math** is `L=0` plus `eta=0` (history does not write). Move without loading.

When history writes (`L += eta * dx`):

```
eta=0    ticks=50     L_end=0
eta=0.1  ticks=175    L_end=5.0
eta=0.5  ticks=674    L_end=25
eta=1.0  ticks=1298   L_end=50
```

Same goal. Same C. The extra ticks *are* the drag bill. Q-calculus bills `eta=0` for numerals, mix, and gauge. Peano bills `eta=1` per `S`.

**Zero-friction mix:** `__mul__` on Readings pays 0 S and 0 channel-alphabet growth because Q already holds the output. Bits bill 1 leak. Wrap bills a fold (`2→0`), which is a deleted distinction, not free smoothness.

---

## 3. Mechanism of distinction

Relative to a loaded history `L` and available gradients (what V still accepts).

### Establish

| move | what appears | cost |
|---|---|---|
| `S` | next numeral | 1 tick |
| `isolate(v,seed)` | pair `(v,seed)` | 1 isolate + unpaid numeral unless Peano-first; seed must be in `Vr` |
| mint name | origin string / generator | 1 label; 0 if you only store the pair |
| host `/` | letter of `Vq` | growth of `Vq` or refuse |

No available slot → write does not establish. Seed `2` into bits: no distinction `2`, only a leak.

### Hold

Keep the letter in play and the channel live.

- Hold `r≠0` or rate θ-refuses (dead isolator).
- Hold mint or val-eq deletes the generator.
- Hold `L` under θ or traveler decoheres (θ=12 at tick 167 in the workbook run).
- Hold both slots of the pair or projection deletes the ratio.

Holding is not free. Dead seed is a held “not moving.” Wrap-0 is not a held dead; it is a folded live `2`.

### Manipulate

| move | what happens to the distinction | cost |
|---|---|---|
| host `+` of two channel meets | may write a **new** letter (`2`) | leak if letter not in `Vr` |
| xor / wrap | may **identify** two letters (`2~0`) | fold, not growth |
| gauge `k` | rescale channel | `k` must be in `Vr` |
| rate | write `Vq` | `/` |
| mix then compose | stack (`1→2→3`) | each `+` |

Available gradient = which combinators still land. Bits have 16 combinators that land and one host `+` that does not. Q has host `+` as an available gradient because Q was pre-loaded.

### Delete

| move | what disappears |
|---|---|
| `π_v`, `π_r` | the other slot; rate unreadable |
| seed `0` | live channel; pair becomes constant |
| val-eq | mint / generator |
| wrap fold | host `2` as distinct from `0` |
| θ refuse | the write; distinction never enters V |
| vent / drop L | load letter; may leak `Vl` |
| `A=A` free | cost of re-weighing |

Delete is a G. Wrap-delete and project-delete and val-eq-delete are three different remainders.

---

## 4. History and available gradients

History = what has already been written (numeral ticks, `L`, mint, which letters of `Vr` exist).

Available gradient = which G still land on current V.

Self-similarity (same mix, same slope 6) holds while the seed stays in `Vr` and combinator stays host `+` on Q. Change char, listed `Vr`, or combinator, and the “constant 2” moves.

Reconfiguration: when a write will not land, you wrap (delete), grow V (establish new letter, pay μ), or refuse (θ). Smooth-math environments pick “grow V in silence” every time. That is `eta=0` plus an infinite pre-load.

---

## 5. One line

A constant in these machines is a relation whose context was frozen and whose establishment ticks were zeroed. Smoothness is V already closed under the combinator you want. Drag is history writing `L` (or S, or `Vr`) as you move. Distinction is establish / hold / manipulate / delete against that history and those gradients :  four G, four prices, not four properties of an object.
