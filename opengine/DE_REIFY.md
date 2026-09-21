# Prior mechanics :  ghosts off

```
python3 recover.py   # 29/29
python3 prior.py     # 14/14
python3 complex.py
python3 foundations.py
```

A model is a stack of writes. The named objects are leftovers of those writes, sold as rooms.

---

## 0. The only prior relations you need

1. **List a V** :  which letters may appear.
2. **Isolate** :  write a second slot (seed / chart / prep / condition).
3. **Meet** :  one slot of one pair against one slot of another.
4. **Combinator** :  `+` / xor / wrap / complex-square / split-square. Two combinators of the same meets leave a remainder.
5. **Read** :  rate, bilinear `η`, Born, inner product. Always at least two slots.
6. **Project / fold / val-eq** :  delete a slot, identify letters, drop mint.
7. **Accumulate** on a listed grid :  sum, path sum, Riemann.
8. **Refuse (θ)** :  dead isolator, empty given, pole, horizon-shaped.

Everything below is those eight, renamed.

---

## 1. Statistics :  ghosts and priors

| ghost | sold as | prior G |
|---|---|---|
| Probability of an event | a property the event has | a read `μ` on a listed subset of Ω |
| Conditional probability | a different kind of probability | `rate(joint, margin)`; `μ(B)=0` is θ |
| Independence | events don’t talk | product of two reads (workbook Option B / 162) |
| Random variable | a thing that fluctuates | a map `Ω → Vv` |
| Expectation | the true mean | accumulate `x μ` on listed Ω |
| i.i.d. | nature repeats | val-eq across trials; mint deleted |
| Likelihood | evidence-stuff | a family of μ’s indexed by a hypothesis letter |
| Prior / posterior | beliefs | two μ’s related by Bayes = chain of rates |
| “Almost sure” | certainty | leftover mass named 0 by fiat on an unlistable V |
| Continuum of outcomes | the real sample space | unpaid smoothness so every Borel write lands |

De-reify: keep Ω listed, μ a map into a listed `[0,1]`-shaped V, conditional as rate, independence as an explicit product-G (not Leibniz). When you need interference, switch combinator; do not invent a new substance called “amplitude” first.

---

## 2. QM :  ghosts and priors

| ghost | sold as | prior G |
|---|---|---|
| State / wavefunction | a thing the system is | an isolated pair (or list of pairs) waiting for a read |
| Hilbert space | the arena | linear G on a listed (or unpaid-complete) V of pairs |
| `i` | imaginary substance | square-rule: second slot writes first slot with minus |
| Superposition | being two places | host `+` on that V |
| Phase | a mystery angle | letter in the second slot; Born deletes it |
| Born probability | nature rolls dice | `π`: pair → `a²+b²` |
| Ray | physical state | gauge: drop global seed |
| Operator / observable | a property | a G `V→V` |
| Eigenvalue | the value of the property | a letter fixed by that G |
| Commutator | uncertainty stuff | leftover of two compose-orders |
| Entanglement | spooky link | tensor write whose projections do not factor (`ac·bd ≠ ad·bc`) |
| Measurement / collapse | physical jump | delete + re-isolate |
| ħ | a constant of nature | units/gauge letter (number moves with `Vr`) |

Paid:

```
tensor (1,0)⊗(3/5,4/5) = (3/5, 4/5, 0, 0)   product
bell (1,0,0,1)                               not product
XZ|0> ≠ ZX|0>
Born(ψ)=Born(-ψ)=Born(iψ)
i*i = (-1,0)
```

De-reify: start with isolate + complex mix + linear G + a project-read. Do not start with “a state in Hilbert space.” Tensor first; call it entangled only after `is_product` fails. Collapse is not a force.

---

## 3. GR :  ghosts and priors

| ghost | sold as | prior G |
|---|---|---|
| Spacetime | a 4-room | the output of a comparison-G, treated as a container |
| Point / event | a location | an isolate index |
| Metric | property of the point | bilinear read of two isolations |
| Interval / ds² | a length that exists | that read, evaluated |
| Coordinates | names on the room | seed / chart; gauge |
| Tangent vector | an arrow at a point | a slot attached to an isolate |
| Connection / Γ | geometry stuff | a write that depends on current slot and direction |
| Parallel transport | sliding an arrow | compose those writes along a listed path |
| Curvature | a field in the room | leftover of two transport-orders |
| Torsion | another field | leftover of transport-of-sum vs sum-of-transports |
| Geodesic | a straight worldline | traveler whose connection-write is 0 in that isolate |
| Horizon | a place | θ: this chart’s V cannot host the next write |
| Energy-momentum | stuff that gravitates | load that sources the connection-write |
| Equivalence principle | physics insight | local gauge to `L=0` in one isolate |

Paid:

```
η(t,t)=1  η(x,x)=-1  η(null,null)=0
euclid(null,null)=2                      leftover vs η
boost β=3/5 preserves η
path-dep transport (0,0): u-then-v=(1,2) v-then-u=(1,1)
abelian + transports commute
```

De-reify: two isolations and a bilinear combinator (split-square for Lorentz, plus-square for Euclid). Connection is a *path-dependent write*. Curvature is the leftover when you swap order. Do not put a tensor in the manifold; keep the two paths.

---

## 4. QFT :  ghosts and priors

QFT is QM’s stack **copied along a listed index** (mode / site / path), plus accumulate.

| ghost | sold as | prior G |
|---|---|---|
| Field | a value at every point | a family of isolations indexed by a listed site |
| Quantum field | operator-valued | that family, each site a G not a numeral |
| Vacuum | empty space | all oscillators at n=0 (dead seed on the number slot) |
| Particle | an excitation | `n → n+1` write (`a†`) |
| [a, a†]=1 | canonical structure | leftover `aa†−a†a = 1` on every listed n |
| Mode | a momentum existence | isolate a Fourier letter |
| Lagrangian | the true action | a combinator you accumulate along a path |
| Path integral | sum over histories | listed path-sum; **order of born vs add is a G-choice** |
| Virtual particle | a ghost in a diagram | an internal edge of the path-sum, projected out of Vq |
| Renormalization | subtracting infinity | leftover named on a listed cutoff; grow V in public |
| Vacuum energy | a density of space | accumulate `½` per listed mode; unlistable modes → unpaid ∞ |

Paid:

```
aa† coeff² − a†a coeff² = 1     for n=0,1,5
(w1+w2)² ≠ w1²+w2²             add-then-born ≠ born-then-add
```

That last line is Ch.3 again (405 vs 162) and also “interference vs classical mixture.” QFT’s path story is: pick which combinator you accumulate, on a listed path set. Continuum of paths is smoothness.

De-reify: oscillator leftover + listed index + accumulate. Do not start with “a field on spacetime.” Spacetime was already a ghost from §3.

---

## 5. What is *prior* to all four

Same stack as Peano → isolate → meet → combinator → read → project.

```
S / isolate          establish a letter or a slot
meet + combinator    write the next letter (or leak, or fold)
read                 rate / η / Born / μ
project / val-eq     delete
accumulate           listed sum
θ                    refuse
L / ticks            history of those writes
```

Peano prices numerals. Calculus imports them and writes channels. Probability reads a listed set. QM writes a complex second slot and projects. GR reads two isolations and keeps transport-order leftover. QFT copies the oscillator along an index and accumulates.

No extra ontology is required to *replicate the calculi*. Extra ontology appears when an output (state, spacetime, field, probability) is filed as the thing the relations belong to.

---

## 6. How to run without ghosts

1. Name V (Ω, C², 1+1 pairs, n=0,1,2,…, listed sites).
2. Name G (rate, complex mul, η, transport, a/a†, add-then-born).
3. Name θ (empty given, dead n under `a`, chart pole).
4. Keep mint when two generators write the same pair.
5. When you add a letter (i, continuum, ∞ modes), say you grew V.
6. Leftover of two G keeps its name as leftover, not as a fluid.

If a sentence cannot declare those, it is still a ghost.
