# QM, GR, probability :  same stack, three presentations

```
python3 machines.py
python3 complex.py
python3 drag.py
python3 foundations.py
```

Not three worlds. Three ways to freeze a context and sell the freeze as furniture.

---

## Shared mechanics (already paid)

| move | here | sold in QM | sold in GR | sold in probability |
|---|---|---|---|---|
| isolate | write `(v,seed)` | prepare / choose a basis / cut | pick coordinates | condition on a sample |
| pair you must not split | `(9,6)` | entangled / amplitude before Born | event + tangent | joint vs margin |
| project | `π_v` kills slope | Born / partial trace / phase | 3+1 split, tetrad | marginalize |
| combinator `+` vs xor | leak vs fold | commutator leftover | connection vs coordinate | inclusion vs exclusive |
| square-rule `i²=-1` | value-slot write | Schrödinger `i`, spinors | (almost never; Lorentz is split-ish) | characteristic function uses `i` |
| dead isolator | `r=0` | null measurement / forbidden | horizon / singular chart | `P(B)=0` |
| gauge | seed rescale, ratio holds | global phase, unitaries on rays | diffeomorphism / coord change | reparameterize |
| leftover | stencil−jet `1/2` | anomaly / ordering | curvature | bias / remainder of CLT on a finite n |
| unpaid smoothness | Q already `+closed` | Hilbert complete | C∞ manifold | continuum of outcomes |
| val-eq vs mint | `(9,6)` two generators | same state, two preps | same metric, two charts | i.i.d. trials |
| load `L` | traveler drag | decoherence / environment | stress-energy | sample size / prior inertia |
| θ | refuse write | no-go / selection rule | geodesic incompleteness | undefined conditional |

---

## Probability

**Conditional is rate.**

```
P(even ∧ gt3) / P(gt3) = (1/3) / (1/2) = 2/3
P(* | empty) → THETA     # dead isolator
```

`P(A|B)` is not a property of A. It is `rate(joint, margin)`. Same function as `rate(top,bottom)`.

**Independence is product-of-rates, not Leibniz.**  
`P(HH)=1/4` is Option B from the workbook (162, not 405). Leibniz would add channel meets. Confusing those two G is the same student mistake as Ch.3, sold as “events don’t interfere.” When they do (QM amplitudes), you needed the other combinator all along.

**i.i.d. is val-eq across trials.** Mint-eq is false: two flips are two generators. Treating them as `A=A` deletes history (`eta=0`). Exchangeability is a stipulated identifications-G.

**0 and 1** are annihilator / identity of the min-AND lattice on `[0,1]`, not mystical certainties. On V3, product AND leaks `¼`. Kolmogorov on `[0,1]⊂R` pre-loads the host so product lands. That is smoothness cost.

**Limit theorems** send leftover → 0. Finite-n leftover is the honest object (same as Riemann `1/192`).

---

## Quantum

**Amplitude is a complex pair.** `i` is the square-rule that writes `-bd` into the value slot. Not a substance. Schrödinger’s `i` is “the generator of rotation uses the complex mix,” i.e. the leftover of `u*u` lands in the other slot so the flow stays on the circle (`|ψ|` held). Dual numbers would write the leftover into the channel (dissipation-shaped). Different G, different remainders.

**Born is projection.**

```
(3/5, 4/5)  born=1
(-3/5,-4/5) born=1     # phase deleted
```

You cannot recover the pair from `1`. Same as `π_v(9,6)=9`. Measurement-as-Born is a delete-G plus a write into `Vq` (probabilities). The textbook then treats that `Vq` letter as the state.

**Ray / global phase:** gauge. Ratio-like reads that ignore a U(1) seed. Lands only if that seed is in the listed symmetry V.

**Entanglement:** a pair (or more) whose projections do not reconstruct the joint. The unsplittable pair, not a spooky fluid. `π_A` and `π_B` each lose the mint of the joint.

**Commutator:** two combinators of the same meets disagree. On bits, host `+` vs xor at `(1,1)`: leftover slot `2`. `[X,P]=iħ` is a named leftover of two mixes, with the complex square-rule supplying the `i`. ħ is a units/gauge letter (like m vs cm: the *number* moves, the comparison can hold).

**Hilbert completeness:** unpaid smoothness. Listed finite V (qubits, spin) do not need it. The continuum wavefunction imports Q/C as host so every write lands.

**Collapse:** delete + re-isolate. Not a physical substance changing. A cut. History `L` of the previous pair is dropped or written into the apparatus (drag).

---

## General relativity

**Metric is a comparison, not a property of a point.**  
`g(u,v)` reads two isolations together (bilinear). Same job as rate: no single vector “has” an interval. Selling `g_μν(x)` as furniture at `x` is `π` onto a chart.

**Coordinates are isolate / gauge.** Change of chart rescales components; some ratios (scalars) hold. Equivalence principle is the claim that *locally* you can choose seed so the connection write looks like zero :  gauge to inertial. That seed is not free globally (holonomy / leftover).

**Curvature is leftover.**  
Paid stand-in: stencil of `x^4` at 2, `h=1/2` is `97/2`; jet `r2=48`; leftover `1/2`. The stencil is a different G than the jet. Parallel transport around a loop is compose-then-compare; the disagreeing remainder is curvature. Not a fluid in the manifold.

**Smooth manifold:** C∞ pre-load. Every derivative order writes a new `Vt` letter that R already contains. Listed / piecewise hosts leak (triangular `Lr`, jet `2rs` on bits).

**Geodesic:** traveler with connection as the available gradient. `L` here is not thermodynamic; it is whatever the connection writes as you move. Zero connection in a chart is `L=0` *in that isolate*, not zero drag in the machine.

**Horizon / singularity:** θ. The chart’s `Vr` cannot host the next write (dead isolator for “time,” or `g` writes 0 on a live displacement). Extend V (Kruskal) or refuse. Do not hire Inf.

**Stress-energy:** load. It sources connection the way `eta` writes `L`. Treat T as a primitive blob and the write that produced it is off-book.

**Spacetime as a container:** output of the comparison-G treated as a room. Same reification as “the real line” or “the state space.”

---

## Cross-identifications that cause damage

1. **Independence (product) used where amplitudes need Leibniz/complex mix.** Classical probability. Interference is the missing meet.
2. **Born / marginal / 3+1 split** all project. Then the projection is called the system.
3. **i.i.d. / same state / same spacetime point** as val-eq. Mint gone.
4. **ħ, c, G, “1”** as eternal numerals. They are unit/gauge letters. Change `Vr` (units) and the *number* moves.
5. **Continuum limits** as smoothness instead of leftover-named finite cuts.
6. **Commutator / curvature / bias** as substances instead of two-G leftovers.

---

## What this does *not* claim

It does not replace the Einstein equation or the Born rule with `lei_xor`.  
It names which G those theories already run, which projections they sell as objects, and which hosts they pre-load.

FORCED here: conditional=rate `2/3`, empty given θ, Born phase-kill, `i*i=(-1,0)`, bit commutator leftover `2`, stencil leftover `1/2`.  
STIPULATED: “metric is rate-shaped,” “ħ is units,” “collapse is re-isolate.” Those are maps, not recoveries of the full theories.

---

## Falsifiers

- If `P(A|B)` with `P(B)=0` lands, dead-isolator≠conditional.
- If Born distinguishes `ψ` from `-ψ`, projection is not Born.
- If wrap Z/2 keeps `i²=-1` distinct from `j²=+1`, char-2 collapse died.
- If stencil always equals jet `r2`, leftover-as-curvature stand-in dies on that example.
- If a chart change moves a scalar the same way it moves `g_μν` components, gauge-invariance of the read died.
