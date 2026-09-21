# Map for map-making

Explored with listed V and executable G. Numbers below rerun from

```
python3 test_slots.py      # 35/35
python3 test_affect.py     # 20/20
python3 taxonomy.py
python3 slots.py && python3 slots2.py && python3 slots3.py && python3 slots4.py
python3 affect.py && python3 affect2.py
```

Do not import a derivative, a field, or an identity as furniture. Name `Vv`, `Vr`, the meets, the combinator. Scan. Keep what lands.

---

## 1. A pair is several alphabets

| slot | writes | typical leak |
|---|---|---|
| `Vv` | value meet (`*`, `&`, `min`, …) | `½×½=¼` on V3 |
| `Vr` | channel meets + combinator | `(1,1)*(1,1)→r=2` |
| `Vq` | `r/s` | host `/` on Z/5 writes `½` |
| `Vt` | jet `2rs` | bits jet `(0,1,0)*(0,1,0)=(0,0,2)` |
| `Vl` | vent `κL` | workbook `κ=2/5` leaves listed ints |

Process calc on Q runs because Q already contains every write those combinators emit. Bits do not. Q is a host, not a discovery.

---

## 2. Leibniz is two closed meets plus a `+`

On bits:

| G | `(1,1)*(1,1)` | lands |
|---|---|---|
| keep only `r·w` | `(1,1)` | CLOSE |
| keep only `v·s` | `(1,1)` | CLOSE |
| host `+` of both | `(1,2)` | LEAK ×1 |
| `xor` of both | `(1,0)` | CLOSE |
| `or` / `max` of both | `(1,1)` | CLOSE |

The leak is the combinator. Host `+` on `{0,1}` writes `2`.

Wrap-Leibniz on Z/2 is the same write as `lei_xor` at that pair: `(1,0)`. That is `2x=0` in char 2, not a rounded 2.

---

## 3. Growing a listed end does not catch host `+`

`Vv={0,1}`, `Vr={0..m-1}`, host Leibniz:

```
Lr = C(m,2) = 1,3,6,10,15,21,28
```

Always the next integer. A listed initial segment is not `+closed`.

Finite host that *does* close: wrap both slots on `Z/n`. Paid closed for `n=2,3,4,5,7`. Wrap-jet closed for `n=2,3,5`.

Wrap vs host on Z/2: **15 agree, 1 differs.** The differ is host `(1,2)` vs wrap `(1,0)`.

---

## 4. Other slots, same pattern

- Gauge `k=2` is not an op of bit-`Vr`. Isolate seed `2` into bits does not land. Isolation is the first write.
- `D:(v,r)↦(r,0)` lands iff `Vr ⊆ Vv`. Grow `Vr` to host mix and unary derivative stops landing in `Vv`.
- Host quot on bits writes `r=-1`. Combinator `−` grows `Vr` into the negatives.
- Compose stacks: seed 0 stays dead; seed 1 goes `1→2→3`.
- Dead channel `Vr={0}` + bit values is a subalgebra. Same dead channel + `{0,1,2,3}` values leaks (`2*2=4`).
- Vent closes only for trivial G (`κ=1` or one-child-all). Workbook vent is not an op of listed integer `Vl`.

---

## 5. Logic is the same engine

V2: `min` and `prod` are the same 4-row table.  
V3: `prod` writes `¼`. `min` stays. Split.

`compare_versions((0,1),(0,1,"maybe"), old_and)`: old AND still **closes** and **never emits maybe**. Collapse ≠ leak. Collapse is the silent upgrade bug.

Protocol `{off,on,fault}`: honest AND keeps fault as annihilator. Mask-fault still CLOSE and hides fault as off.

---

## 6. How to mint a calculus or a logic

1. List `Vv` and `Vr` (and `Vq`/`Vt`/`Vl` if you will write them).
2. Pick a value meet and a channel combinator from closed tables, or invent one and scan.
3. `admit(Engine, op)` → ship or name the leak.
4. If you need host `+` and a listed `Vr`, you must wrap, grow to a `+closed` host, or refuse those inputs.
5. If you add a letter, rerun. Check leak **and** collapse (new letter never emitted).
6. Stamp FORCED only for rows the runner just produced. Analogies stay STIPULATED.

`lei_xor` and `and_pair` are minted G that close on bits. They are not “the derivative.” They are maps of that frame.

---

## 7. Falsifiers

- If `lei_plus((1,1),(1,1))` lands in bit pairs, the leak claim dies.
- If wrap-Leibniz on Z/5 leaks, the finite-host claim dies.
- If `Lr` on `Vr=0..6` is not 21, the triangular claim dies.
- If isolate seed `2` into `Vr={0,1}` lands, isolation is not a write into a listed slot.
- If old AND on `{0,1,maybe}` emits `maybe`, collapse is not that G.

---

## 8. Forge: all 16 bit combinators close

`python3 forge.py`

`mix = (v*w, comb(r·w, v·s))` with `comb` any of the 16 bit tables: **16/16 CLOSE**.

Writes at `(1,1)*(1,1)` only two: `(1,0)` or `(1,1)`.
Codes 0-7 write `r=0`. Codes 8-15 write `r=1`.

Host `+` is not one of the 16. It leaves the frame.

## 9. What not to import

- “The derivative of `x²` is `2x`” without naming host vs wrap vs xor.
- “Q is the value space” without naming Q as the unpaid `+closed` host.
- “AND is min” without naming V2 (true) vs V3 (prod ≠ min).
- Unary `D` as a property of `v`.
- Infinity as the way listed `Vr` “finishes” the triangular walk.
