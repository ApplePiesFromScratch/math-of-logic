# Foundations under the ML nouns

```
python3 foundations_ml.py
python3 play_ml.py
python3 foundations.py
```

Learning is isolate weights, iterate a step-G, read leftover on a listed Ω.
Generalization is that leftover on a second Ω.
A token prob is a read of logits, not a property of the letter.

---

## What sits under the nouns

| noun | prior |
|---|---|
| Dataset | listed Ω of pairs |
| i.i.d. | val-eq of two examples (mint dropped) |
| Model | G plus isolated weights plus a decode |
| Parameter | letter of a weight-V |
| Init | isolate seed |
| Loss | leftover of pred-read vs label-read |
| Gradient | rate / dual slot of that leftover |
| SGD step | Peano-shaped `S` on the weight letter |
| Epoch | one pass accumulate on Ω |
| Probability of token t | softmax letter; t does not own it |
| Cross-entropy | leftover of two μ |
| Feature | cut: isolate some slots, ignore others |
| Generalization | train read vs test read |
| Capacity | how many w in listed V; `w=2.1` is a μ |
| Empty train set | `L=0` vacuous (error 13) |
| Intelligence | compress of the stack |

---

## What printed

Two copies of `(1,2)`: val-eq True. In this run mint-eq was also True: CPython interned the tuple. The host collapsed two mints. i.i.d. does that on purpose.

`L(2)` train 0, test point `(3,5)` leftover **1**. ERM zeroed the train read. The test read stayed.

`L` on empty Ω is **0**. Same hole as `all([])` and empty-V close.

Drop `x`, keep `y`: `[2,4,6]`. The cut cannot recover `w`. Features are isolate/ignore (CUT.md).

Two inits: `L(0)=20`, `L(1)=5`. Same G, two seeds, two mints.

Softmax `[0.1,0.8,0.1]`: `b` does not contain 0.8. The read does. Same as `P(A)` not a property of A.

CE(p, one-hot b) `0.223`. CE(y,y) `0`. Leftover of two μ.

Prefix `("a",)` in V. Next write is a letter of V.

Three SGD ticks: tick 1 writes `w=2`, L=0, then stays. Iterate-`S` on weights. This quadratic plus this η hit exact in one `S`. That is this G, not a law of learning.

Listed `w ∈ {-1,0,1,2,3}`: best is 2, L=0. `w=2.1` is not in V; L=`0.05`. Capacity is the listed V. Float 2.1 is a silent μ.

---

## Equals in play

| = | used as |
|---|---|
| val-eq of examples | i.i.d. |
| val-eq of two runs | “the” accuracy |
| wrap-eq of float | 0.050000000000000086 is 0.05 |
| mint-eq of weights | checkpoint |
| host intern | two tuples one object |

---

## Unpaid in textbook ML

True risk: accumulate on unlistable Ω (error 2, 25).
PAC “with high probability”: leftover sent toward 0.
R^d features: host as ground.
Softmax as belief: project as system.
Backprop as “the” derivative: one combinator (dual).
Scale: leftover → 0 at ∞.

Doctor: list Ω, list weight-V or stamp float, keep train and test on one journal line, stamp intern/host `=`, empty Ω is θ.
