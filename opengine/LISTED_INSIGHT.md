# Listed field and 3+1 :  what landed without Inf

```
python3 listed_field.py   # 30/30
python3 recover.py prior.py
```

The withheld line was: interacting QFT and 3+1 Einstein need a new G or a public μ, not another Inf.

Done on listed V: an interacting scalar, a 3+1 Minkowski read, a plaquette leftover. Einstein’s equation is **not** recovered. The vacuum row is the proof: matter-read 0, geom-read 1.

---

## Interacting scalar

```
sites     {0,1,2,3} wrap
φ         {-1,0,1}
kinetic   Σ (φ_i − φ_{i+1})²
interact  λ Σ φ_i⁴          λ=1
S         kin + λ·quart
```

| cfg | kin | quart | S |
|---|---|---|---|
| `(0,0,0,0)` | 0 | 0 | 0 |
| `(1,0,0,0)` | 2 | 1 | 3 |
| `(1,0,-1,0)` | | 2 | |

81 configs (`3⁴`). Unique min S=0 is vacuum. λ=1 raises bump above free bump.

Public μ: add `φ=±2` → `5⁴=625` configs, quartic of a height-2 bump is **16** not 1. Interaction is a self-meet of the value slot. Grow V and that meet writes a new letter.

Path-sum order on `1/S` weights: `(w_b+w_w)² ≠ w_b²+w_w²`. Same leftover as Ch.3 and as QM interference. No continuum of paths.

What this is: φ⁴ on a 4-cycle.  
What this is not: renormalized interacting QFT in 3+1. Continuum, loops, and “the” finite part are the retired IV.

---

## 3+1 Minkowski

```
η(u,v) = uᵗvᵗ − uˣvˣ − uʸvʸ − uᶻvᶻ
```

```
η(t,t)=1   η(x,x)=η(y,y)=η(z,z)=-1
η(t+x,t+x)=0
boost β=3/5 γ=5/4 in t-x preserves η(t,t), η(x,x), null; y fixed
```

Four slots. One split-square combinator. Boost is gauge on two of them. No manifold. No C∞.

---

## Plaquette leftover

Transport depends on current slot:

```
u-then-v (0,0) → (1,2)
v-then-u (0,0) → (1,1)
curv letter     (0,1)
```

That letter is curvature-shaped: leftover of two compose-orders on a listed square. Not a tensor field on a spacetime.

---

## Why Einstein did not appear

Two reads:

- matter-shaped: quartic of bump = 1
- geom-shaped: curv letter = 1

On vacuum: matter = 0, geom = 1. **They are not locked.**  
`G=8πT` would be a further G that forces those two letters equal. We did not write that G. Booking the accidental `1=1` on the bump row as Einstein is error P.

Doctor options for that missing G:

1. **Don’t.** Keep two reads. Leftover is the object.
2. **Write it** as a constraint-G: only configs with `matter_read = geom_read` stay in V. Then Einstein is θ + a filter, not a fluid.
3. **μ** a new letter (coupling) that rescales one read until they match. Coupling is seed/gauge, not a constant of a room.

None of those need Inf.

---

## Insight

Interacting and 3+1 were never “too big.” They were **unlistable hosts** plus a law that identified two different reads.

- Interaction = extra self-meet (`φ⁴`) on a listed site V.
- 3+1 = four slots + split bilinear.
- Curvature = plaquette leftover.
- Einstein-shaped = optional constraint between two reads.
- QFT-shaped path = accumulate; order of born vs add is a G-choice.
- Continuum / Hilbert / C∞ / ∞ modes = life support on a leak.

Relationally simpler: sites, slots, meets, leftover. The nouns “field,” “spacetime,” “interaction,” “gravity” are filing labels for those writes.

Still not done as physics: no experiment, no 625-config scan of a coupling that holds matter=geom, no fermion combinator. Those are more listed G, or a public μ :  the same doctor moves.
