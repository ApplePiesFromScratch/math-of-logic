# AI / code / learning as the same stack

```
python3 ml.py          # 15/15
python3 accountant.py
python3 recover.py
```

A model isolates some slots (weights, context), ignores the rest, runs a sim, reads a loss. Naming did not grant essence. Float and `softmax` are stamped hosts.

---

## Prior G (what you need before “the model”)

| move | in this stack | in ML / code |
|---|---|---|
| list V | vocab, types, `{0,1}` | tokenizer alphabet, dtype, label set |
| isolate | context tokens, seed | prompt, init weights, train/test split |
| meet + combinator | matmul, residual `x+f(x)`, attention scores | same |
| read | softmax, loss, reward | μ on vocab, leftover vs one-hot |
| project | argmax, one-hot, Born-like | T→0 sample |
| accumulate | batch sum, SGD step | listed Ω of examples |
| θ | OOV, type error, /0, NaN | refuse or life support (unk, Inf) |
| leftover | train L vs test L; two optimizers | generalization gap |
| mint | this checkpoint, this seed | val-eq of two runs as “the” model |
| μ | new vocab item, LoRA rank, bigger ctx | public if you stamp it |

Autograd is dual mix (`ε²=0`). That is the Q-kernel Reading. Backprop is chain: shared channel cancels. `ml.py` affine `y=3x` at 2: pair `(6,3)`, rate 3. Then `z=y²`: `(36,36)`, rate vs x is 36.

---

## Ghosts

| ghost | booked as | prior |
|---|---|---|
| Intelligence | a property | a stack of G on a listed (or float) V |
| Representation | stuff inside | isolated slots after a compose |
| Loss landscape | a place | leftover of a step-G |
| Gradient | a force | jet / rate slot |
| Probability of a token | a property of the token | softmax read of logits |
| Hallucination | a sin | write of a letter with high read and low mint vs the prompt V |
| Emergence | magic at scale | new letter emitted that train V did not list (scan emit, error 14) |
| Alignment | a virtue | extra filter-G on outputs (Einstein-lock shaped) |
| The model | one object | mint of weights + tokenizer V + decode G |
| Code meaning | in the source | G plus a run; syntax doing semantic work if unread |
| Type | essence of a value | V stamp; θ on mismatch |
| Floating point | the reals | IEEE life support (Inf, NaN, wrap-like mantissa) |

---

## Life support in this domain

| patch | left V | doctor |
|---|---|---|
| float / mixed precision | Q | listed Q or stamp IEEE |
| softmax on raw logits | exp host | θ if overflow; listed log-sum-exp table |
| `unk` token | OOV | θ, or public μ add the letter |
| context window slide | ctx longer than V | listed window; leftover is dropped prefix |
| dropout | delete slots at random | project-G; mint the mask |
| weight decay | extra load | L on traveler |
| teacher forcing | future token isolated early | different mint than decode |
| RLHF / preference model | two reads locked by a filter | extra G, not a soul |
| temperature 0 as truth | argmax project | one decode combinator |
| “scale will fix it” | leftover → 0 at ∞ params | keep leftover vs listed compute |

`ml.py` softmax is host `exp`. Stamp that. Vocab is listed `a,b,c`. `z` is θ.

---

## Attention, residual, diffusion (mechanics only)

Attention: read of (Q,K) pairs, project onto V. Rate-shaped. Dead key is θ.

Residual: combinator `id + f`, not `f`. Same as lei vs keep-one-meet: two combinators.

Diffusion: add a noise-G then invert. Two compose-orders. Leftover if invert ≠ denoise path (C2).

GAN: two G, leftover of their reads. Locking them is an extra filter.

Mixture-of-experts: isolate a route letter, then one of several G. Collapse if the route never emits an expert.

---

## Code as a carrier

| code | V | G | θ |
|---|---|---|---|
| Python | objects + types | runtime ops | TypeError, NameError |
| Rust | ownership letters | move | use-after-move |
| types | type letters | constructors | fail to typecheck |
| tests | listed examples | runner | assert |

`1+"a"` is C10 host mismatch. A type system is V listed in advance. “It typechecks so it is true” is runner sold as ∀ (#29).

LLM-written code is a decode-G on a vocab of tokens, then a second G (the compiler) that may θ. Two mints: generated string vs passing run. Val-eq of those is the usual lie.

---

## Errors that fire first here

1. Output as primitive: “the model,” “the capability.”
2. Host as ground: R^params, float.
3. Project as system: argmax as the answer; softmax as the belief.
4. Combinator as essence: “attention is all.”
5. Leftover → 0: scale, “more data.”
6. Mint delete: two seeds, one reported number.
20. Hidden partiality: softmax /0, OOV, empty context.
26. Default hides partiality: temperature=1, seed=1.
29. Runner as ∀: train loss as generalization.

Overfit is C4/C11: train read locked to test read by silence.

---

## Where this does not recover ChatGPT

No 161-row gate runs a transformer. What landed: listed vocab, softmax-as-project, loss-as-leftover, temperature-as-gauge, OOV as θ, dual affine + chain, train vs test as two reads, residual ≠ f.

Weights-as-V, attention table, tokenizer μ: next listed labs, not Inf.
