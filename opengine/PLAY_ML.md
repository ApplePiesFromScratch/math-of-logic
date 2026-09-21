# Play log: decode, attention, dual fit

`python3 play_ml.py`

---

T=50 softmax is almost flat `[0.329, 0.342, 0.329]`. Argmax still returns **b**. The project does not see how close the other two letters are.

Sample `u` is another combinator. Same logits, `u=0.01` writes `a`, `u=0.9` writes `c`. Temperature and `u` are two gauges on one read.

`exp(-1e9)` sums to 0. Softmax **THETA**. Float underflow is a hole. Libraries subtract max(logits) first: life support on this leak.

Dot vs xor on bit keys, query `(1,0)`:

```
k=(1,0)  xor=0  dot=1
k=(0,1)  xor=2  dot=0
k=(1,1)  xor=1  dot=1
```

Match wins under dot. Match **loses** under xor (distance). Same Q,K, two score G, two winners. Attention-is-dot is error 4.

Dual fit of `y=wx` on `(1,2),(2,4)`:
`L(0)=20`, `dL/dw=-20`, one step `η=1/10` writes `w=2`, `L=0`.
Test point `(3,5)` at that w: leftover **1**. Train read 0, test read 1. Same G, two Ω.

Residual `x+f` vs `f` at `x=2,f=-2` writes `0` vs `-2`. The combinator can land on a letter `f` never wrote.

16 bit score tables: all close. Score-in-{0,1} is easy. Softmax after those scores is the host that leaks.

---

Fog: argmax-on-flat, xor-vs-dot winner flip, one-step exact hit is this quadratic plus this η, softmax dies on tiny logits, train-zero does not kill test leftover.
