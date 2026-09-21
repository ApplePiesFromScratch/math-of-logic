# Insights :  slots, combinators, workbook cut

Paid by runners in this folder and by reading *How To Build A Novel Calculi* + `calc_verified.py`.
Rerun:

```
python3 test_slots.py       # 35/35
python3 test_affect.py      # 20/20
python3 forge.py            # 16/16 bit combinators close
python3 taxonomy.py
python3 slots.py && python3 slots2.py && python3 slots3.py && python3 slots4.py
python3 affect.py && python3 affect2.py
```

---

## A. A pair is several alphabets

`(v, r)` is not one V. Mix writes `v` with `v`, and `r` with `v` and `r`. Rate writes another scalar. Jets write a third.

| slot | what writes it | typical leak on a listed end |
|---|---|---|
| `Vv` | value meet (`*`, `&`, `min`) | `½×½=¼` on V3 |
| `Vr` | channel meets + combinator | `(1,1)*(1,1)→r=2` |
| `Vq` | `r/s` | host `/` on Z/5 writes `½` |
| `Vt` | jet term `2rs` | bits `(0,1,0)*(0,1,0)=(0,0,2)` |
| `Vl` | vent `κL` | workbook `κ=2/5` leaves listed ints |

Process calc on Q runs because Q already contains every write those combinators emit. Bits do not. Q is a stipulated host, not a discovery.

---

## B. Leibniz is two closed meets plus a `+`

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

`python3 forge.py`: all **16** bit tables as combinator of `r·w` and `v·s`, value meet `*`: **16/16 CLOSE**.
Writes at `(1,1)*(1,1)` only two: `(1,0)` or `(1,1)`. Codes 0-7 write `r=0`. Codes 8-15 write `r=1`.
Host `+` is the 17th combinator. It leaves the frame.

---

## C. Growing a listed end does not catch host `+`

`Vv={0,1}`, `Vr={0..m-1}`, host Leibniz:

```
Lr = C(m,2) = 1, 3, 6, 10, 15, 21, 28
```

Always the next integer. A listed initial segment is not `+closed`.

Finite host that closes: wrap both slots on `Z/n`. Closed for `n=2,3,4,5,7`. Wrap-jet closed for `n=2,3,5`.

Wrap vs host on Z/2: **15 agree, 1 differs.** Differ is host `(1,2)` vs wrap `(1,0)`.

Dead channel `Vr={0}` + bit values is a subalgebra. Same dead channel + `{0,1,2,3}` values leaks (`2*2=4`).

Compose stacks: seed 0 stays dead; seed 1 goes `1→2→3`.

---

## D. Other slots, same prior affect

- **Isolate** writes `(v, seed)`. Seed `2` into `Vr={0,1}` does not land. Isolation is the first write.
- **Gauge** `k=2` is not an op of bit-`Vr`. After the write lands, `top.r/bottom.r` can match. Landing is prior.
- **`D:(v,r)↦(r,0)`** lands iff `Vr ⊆ Vv`. Grow `Vr` to host mix and unary derivative stops landing in `Vv`.
- **Host quot** on bits writes `r=-1`. Combinator `−` grows `Vr` into the negatives.
- **Vent** closes only for trivial G (`κ=1` or one-child-all). Workbook vent is not an op of listed integer `Vl`.
- **`ε²` relations** on host bits all leak. On wrap Z/2 all close, and `−1≡1`.

---

## E. Logic and systems use the same engine

V2: `min` and `prod` are the same 4-row table.  
V3: `prod` writes `¼`. `min` stays. Split.

`compare_versions((0,1),(0,1,"maybe"), old_and)`: old AND still **closes** and **never emits maybe**. Collapse ≠ leak. Collapse is the silent upgrade bug.

Protocol `{off,on,fault}`: honest AND keeps fault as annihilator. Mask-fault still CLOSE and hides fault as off.

Cents: average leaks half-cents. Floor is a different G that closes.

---

## F. How to mint a calculus or a logic

1. List `Vv` and `Vr` (and `Vq`/`Vt`/`Vl` if you will write them).
2. Pick a value meet and a channel combinator, or invent one and scan.
3. `admit(Engine, op)` → ship or name the leak.
4. If you need host `+` and a listed `Vr`, wrap, grow to a `+closed` host, or refuse those inputs.
5. If you add a letter, rerun. Check leak **and** collapse (new letter never emitted).
6. Stamp FORCED only for rows the runner just produced.

`lei_xor` and `and_pair` are minted G that close on bits. They are not “the derivative.” They are maps of that frame.

---

## G. Falsifiers

- If `lei_plus((1,1),(1,1))` lands in bit pairs, the leak claim dies.
- If wrap-Leibniz on Z/5 leaks, the finite-host claim dies.
- If `Lr` on `Vr=0..6` is not 21, the triangular claim dies.
- If isolate seed `2` into `Vr={0,1}` lands, isolation is not a write into a listed slot.
- If old AND on `{0,1,maybe}` emits `maybe`, collapse is not that G.
- If `forge.py` reports a bit combinator leaking, the 16/16 claim dies.

---

## H. Workbook cut :  *How To Build A Novel Calculi* + `calc_verified.py`

The book is a **Q-host Leibniz machine**. Existing FORCED numbers still hold (`rate(x*x,x)=6`, `405≠162`, leftover `1/192`, chain `192`, refuse float/bool/NaN).

It does **not** need a full rewrite. It needs a named host and one load-bearing box.

### Stay

Ch.2-19 as first calculus on Q-pairs with host `+/*`. Leftovers named. Dead isolator. Tape 5 ops → 6.

### Update (short, load-bearing)

**Ch.1 / p.4 “One object carries this entire book.”**  
A Reading is two slots. The book puts both in one Q. `isolate(1, 2)` is legal in Appendix A and illegal on bit-`Vr`. Say `Vv=Vr=Q` **here**, stipulated. Seed `k` lands only if `k∈Vr`.

**Ch.2-3 mix as what multiplication “already is.”**  
`new rate = r1·v2 + v1·r2` is host Leibniz. On bits that write leaves. Sixteen other combinators close. Stamp the mix **STIPULATED**. Ch.3 already has 405 vs 162; add xor/wrap as a third column. STIPULATED is defined on p.4 and then almost unused.

**Gauge.** Invariance is after the write lands. Gauge `k=2` is not an op of bit-`Vr`.

**Jets.** Third alphabet `Vt`. Bits jet writes `2` via `2rs`. Wrap-jet closes on Z/2,3,5.

**Quot.** Host quot on bits writes `−1`. On Q the negatives were already in `Vr`.

**Ch.20 deferred list.** Add: other combinators and listed `Vr`. Host `+` on bits leaks once. Wrap-Leibniz closes. Closer to Ch.3 than Green’s theorem is.

**Title vs body.** Title promises how to *build* novel calculi. Body teaches how to *run this* calculus. Forge `16/16` is the build chapter. Not in the volume.

**`calc_verified.py`.** `Q()` is one gate for both slots. `__mul__` is hardcoded host Leibniz. `__eq__` merges mint collision `(9,6)`. Grade cannot fail a wrap/xor row it does not contain. Scratch leftover comment remains in the attached file near the unused `n2` tape block.

### Heavy or not

| piece | rewrite? |
|---|---|
| Worked Q examples, leftovers, refuse floats | no |
| Ch.1 object + Ch.3 mix + gauge wording | yes, short |
| Ch.20 + title “novel calculi” | add combinator/slot map |
| Appendix kernel | box the host; optional `lei_xor` / wrap lab |

If Ch.1 says “Q is the stipulated host for both slots, mix is host Leibniz, other mixes are other labs,” the rest stays honest. If it keeps “one object, multiplication already is the product rule,” it imports the host as terrain.

---

## I. What not to import

- “The derivative of `x²` is `2x`” without naming host vs wrap vs xor.
- “Q is the value space” without naming Q as the unpaid `+closed` host.
- “AND is min” without naming V2 (true) vs V3 (prod ≠ min).
- Unary `D` as a property of `v`.
- Infinity as the way listed `Vr` finishes the triangular walk.
- A pair type as a single carrier.
