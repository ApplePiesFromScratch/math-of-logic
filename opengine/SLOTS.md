# Three alphabets

A pair is not one V. Mix writes `v` with `v`, and `r` with `v` and `r`.
Rate writes a third scalar. Load is a fourth.

```
python3 slots.py
python3 slots2.py
python3 slots3.py
```

## What closed

| host | Leibniz | note |
|---|---|---|
| Vv=Vr=`{0}` | CLOSE | dead |
| Vv=`{0,1}` Vr=`{0}` | CLOSE | constants |
| Vv=Vr=`{0,1}` host +/* | LEAK ×1 | `(1,1)*(1,1)=(1,2)` |
| Vv bits, Vr=`0..m-1` | LEAK ×C(m,2) | `r+s` walks off the end |
| Vv=Vr=`Z/n` **wrap** +/* | CLOSE | finite host |
| value_only / min_chan / max_chan on bits×bits | CLOSE | they do not add channels |

On bits×bits the only mixes that close are the ones that **do not add** `r` and `s`.
Leibniz adds. That is why dual numbers over bits fail and dual numbers over `Z/n` run.

## Leak sources (host arithmetic)

```
bits/bits   leak_v=0   leak_r=1     both=0
bits/Z4     leak_v=0   leak_r=6     both=0
Z4/bits     leak_v=4   leak_r=17    both=12
tri/tri     leak_v=5   leak_r=17    both=4
```

Two independent walks off the map: `v*w ∉ Vv` and `r*w+v*s ∉ Vr`.
Growing only `Vr` never catches host-Leibniz if `1 ∈ Vv`:
`Lr = C(m,2)` for `Vr={0..m-1}`. Triangular. Next integer always appears.

## Gauge and D

Gauge `(v,r)↦(v,rk)` is a map on bit-`Vr` only for `k∈{0,1}`.
Seed `2` is not an operation of bit channels.

Unary `D:(v,r)↦(r,0)` lands iff `Vr ⊆ Vv`.
Grow `Vr` to host the mix, and `D` stops being a map into the value slot.
That is the collapse: the slope is not a value until you pay a μ `Vr → Vv`.

## Rate writes `Vq`

Host division on `Vr=Z/5` produces `{1/2,1/3,1/4,...}` :  a fourth alphabet.
Modular inverse on prime `n` keeps `Vq = Z/n` (nonzero s). Composite `n` has `NO_INV` (Z/4: 2 cases, Z/6: 10).

`rate` is not `Vr → Vr`. It is `Vr × Vr_live → Vq`.

## Load

Vent with `κ=2/5`, 3 children leaks on every listed integer `Vl`.
Closes only for trivial G: keep-all (`κ=1`) or one-child-all (`κ=0,n=1`).
The workbook vent is a G that **requires** `Vl` to contain the rationals it writes, or it is not an operation of that `Vl`.

## Systems read

Adding a feature flag is growing `Vv`.
Adding a derivative slot is growing `Vr`.
Reporting a slope as a number is growing `Vq` or collapsing `Vr` into `Vv`.
Shipping “the same AND” after the grow is either LEAK or collapse (new letter never emitted).

Wrap-Leibniz is the honest finite calc: both slots use the same tick.
Host-Leibniz on a listed cut always grows `Vr` if `1` is a value.
Process calc on Q works because Q is already the wrap-that-never-closed.
Q is not free. It is the unpaid +closed/+closed host.

## Second dive

Wrap vs host on Z/2: 15 agree, 1 differs. Host writes `(1,2)`, wrap folds to `(1,0)`.
Host quot on bits writes `r=-1`: `(1,0)/(1,1)=(1,-1)`.
Jet on bits: `(0,1,0)*(0,1,0)=(0,0,2)`. Wrap-jet closes on Z/2,3,5.
Compose stacks: seed 0 stays; seed 1 goes `1→2→3`.
Dead-channel + bit values is a subalgebra.

```
python3 test_slots.py
# 35/35 ALL PASS
```
