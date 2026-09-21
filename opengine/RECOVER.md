# Recovered calculi

```
python3 recover.py
# 29/29 ALL PASS
```

These are the machines those theories run on listed V. Not the Einstein equation. Not infinite-dimensional Hilbert.

---

## Probability :  listed Ω

`Ω = {1,2,3,4,5,6}`, uniform `μ(w)=1/6`.

```
P(even)              = 1/2
P(even | gt3)        = 2/3     # rate(joint, margin)
P(even | ∅)          THETA     # dead isolator
P(E) two-hyp         = 1/3
P(fair | land-6)     = 1/4     # Bayes = chain of rates
P(HH) i.i.d. coins   = 1/4     # product-of-rates
```

Recovered: measure on a listed set, conditional as rate, Bayes as chain, independence as product.  
Not recovered: continuum of outcomes, limiting frequency as leftover→0.

---

## Qubit :  C² with complex mix

`i*i = (-1,0)`.

```
X|0> = |1>     X|1> = |0>
Z|0> = |0>     Z|1> = -|1>
XZ|0> = |1>    ZX|0> = -|1>     # do not commute
Born(3/5,4/5) = Born(-3/5,-4/5) = Born(i·ψ) = 1
|0><0| kills |1>, keeps |0>
```

Recovered: complex square-rule, two Pauli maps, commutator as two compose-orders, Born as projection (phase dies), a projector as delete+keep.  
Not recovered: full operator algebra on L², measurement postulates as physics, spin-1/2 experiment.

---

## 1+1 metric :  split bilinear

```
η(t,t)=1   η(x,x)=-1   η(t,x)=0
η(t+x,t+x)=0           # null
euclid(t+x,t+x)=2      # leftover 2 on the same pair
boost β=3/5 γ=5/4 preserves η(t,t), η(x,x), null
```

`η` is the split square-rule (`j²=+1` sign) as a read of two isolations.  
Euclid is the complex-adjacent `+`. Leftover on `x` is `2`.  
Boost is gauge: components move, `η` on the boosted pair holds.

Recovered: bilinear comparison, null cone as `η=0`, Lorentz boost on 1+1 as gauge that preserves the read, leftover vs Euclid.  
Not recovered: curvature, Einstein equation, 3+1, horizons.

---

## What “recover” meant

Run the G those chapters already use, on listed V, with the same isolate / rate / project / leftover stack.

Still STIPULATED as physics: that a qubit is an electron, that η is spacetime, that μ is propensity.

FORCED as machines: the rows above.
