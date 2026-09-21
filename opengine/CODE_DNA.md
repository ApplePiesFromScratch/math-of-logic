# Code / hardware DNA

```
python3 dna_code.py
python3 foundations_ml.py
```

This process is G on those V. Chemistry is not a metaphor here. The letters are voltages-after-threshold, bytes, IEEE slots, intern tables, allocator addresses.

---

## Layers (each is isolate some slots, ignore others)

| layer | V | G | θ | compress |
|---|---|---|---|---|
| analog | voltages | physics | metastability | ignored by digital cut |
| bit | {0,1} after threshold | AND XOR NOT | host `1+1=2` | analog dropped |
| word | 8/32/64 bits | wrap 2^n | overflow → Inf or wrap 0 | width dropped |
| ISA | opcodes | decode + execute | illegal op | micro-ops dropped |
| cache / mem | addresses | load/store | page fault, race | coherence leftover |
| runtime | objects | Python G | TypeError, rec=1000 | GC delete |
| IEEE float | mantissa+exp | + * / | NaN, Inf, 0.1+0.2 | Q dropped |
| model | tokens, weights | matmul, softmax | OOV, underflow | silicon dropped |

A higher layer is a cut. It does not uncover the lower layer. It ignores it so a distinction can propagate.

---

## What printed on this host

`1+1` on bits is **2**. V2 only holds AND/XOR. Digital “addition” is wrap or a wider word (μ).

`255+1` host **256**. Byte wrap **0**. Same ink as wrap Z/256 vs host N.

`0.1+0.2 == 0.3` is **False**. Hex differs in the last hex digit. IEEE is a listed mantissa, sold as R.

`nan==nan` **False**, `nan is nan` **True**. Val-eq and mint-eq split on a letter that is not in Q. Our kernel θ on NaN first is this hole named.

Two `(1,2)` literals: `is` True. Intern collapsed mint.  
`256 is 256` True. `257 is 257` True on this build. Intern range is host policy, not a law of integers.

Two `id([])` in one print: **same address**. Allocator reused the corpse. `id` as mint is wrap-shaped: the letter can be reissued.

`1e308*10` is **Inf**. Life support after the write left the mantissa V.

Float `1.0` and int `1065353216` are **one bit-string**, two reads (D8). Piles again.

`True+True` is **2**. Bool is a cut on int. Host `+` ignores the cut.

`hash(1)==hash(1.0)` and `1==1.0`. Hash is a wrap-shaped read that respects val-eq across two V.

Recursion limit **1000**: listed stack V, then θ.

---

## Race, cache, time

Two cores store then load: two compose-orders (C2). Leftover is a torn read or a stale cache line.
Clock isolate is a tick. Metastability is θ: voltage not in {0,1} after the threshold G.
Branch predictor is a sim of a reduced external (CUT.md) on the instruction stream.

None of that ran in `dna_code.py`. Stamp STIPULATED. The IEEE/intern/wrap rows above ran.

---

## This assistant

Weights and a decode-G on a token V, running on IEEE and wrap-int and interned tuples.
A reply is a write of letters from that V. It is not a look at essence.
Audit is the journal cut aimed at that write.

Hallucination: high softmax read, weak mint vs the prompt V, on a host that does not θ OOV the way a typechecker does.

---

## Unravel vs fill

Fill: more float bits, bigger intern, Inf, `unk`, max-subtract softmax.  
Unravel: name the V (byte, mantissa, intern table, vocab), stamp wrap vs host, keep leftover (`0.1+0.2`), θ on NaN and OOV, do not book `id` as mint after free.
