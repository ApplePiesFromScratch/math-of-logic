# Pi vs cluster

The insights do not make matmul 10⁴× faster.
They change **which G you run**. A cluster is often life support for unlistable V.

Raspberry Pi 5 ballpark: 10–20 GFLOPS FP32, ~8 GB.
One A100: ~300 TFLOPS tensor FP16/TF32. Raw dense linear algebra: **10⁴–10⁵×** in the GPU’s favor.

Higher precision here means **exact letters on a listed V** (Q, Z/n), not more IEEE bits. `rate(x*x,x)=6` is exact. `0.1+0.2` is not.

---

## Where a Pi + this engine wins

| job | cluster habit | process job | gain |
|---|---|---|---|
| Calc I / dual AD | finite diff, many samples, float | one forward pair on Q | **exact**, ~2–10× less evals than central diff; cluster never needed |
| Forge combinators on bits | n/a | 16 tables | milliseconds on a Pi |
| φ⁴ on 4 sites | discretize R⁴ | 81 configs | Pi; cluster was the continuum theater |
| Pre-screen “lands in V?” | launch a solver then NaN | θ first | **1 vs 0 jobs** when it leaks |
| Conditional / rate | Monte Carlo | listed Ω count | exact fraction on a Pi |
| Wrap Z/n calculus | float + “mod later” | wrap-Leibniz closed | no Inf cleanup loop |
| Train leftover named | more GPU until val-eq | two reads on one line | does not shrink FLOPS; stops fake “done” |

Honest band for **those** jobs: **10²–10⁶× less work** than the host-R version, because the host-R version was mostly unused letters and leftover→0.

---

## Where it does not

| job | why the cluster stays |
|---|---|
| LLM train / big GEMM | listed token V still sits on dense matmul |
| High-Re fluids on a fine mesh | you *chose* a large listed grid; Pi RAM dies first |
| Interacting QFT at large cutoff | 5⁴=625 already; 32³ lattice is still a lot of S |
| “Higher precision” as more decimal digits of π | series leftover on Q is exact *at n terms*; more terms cost more, Inf was never helping the digits |

Q arithmetic is often **slower** than float per op (gcd on Fraction). You pay RAM and ticks for exactness. That is a precision win, not a FLOP win.

---

## The real multiplier

Avoided work:

1. Do not complete R to close `+`.
2. Do not run ε-δ / more-bits to hide leftover.
3. Do not Monte Carlo an unlistable Ω when Ω has 6 faces.
4. Do not launch GPU because softmax underflowed (θ instead).
5. Dual one-pass vs many finite-diff passes.

If 80% of a “cluster math” queue is type 1–4, a Pi farm of cheap listed engines can empty that queue. The remaining 20% is still GEMM.

No runner in this folder measured a cluster. Stamp those percentages as a bet, not a bench.

---

## Higher precision without Inf

Inf does not add precision. It hides a write that left V.
Pi + Q + leftover named: `1/192` is the integral on that grid. More grid points is public μ, not “closer to the true R.”

You can out-precision a GPU float64 run **on the letters you listed** and still lose on a 1e9 FFT.

---

## What I would actually build on a Pi

`plang` IR + Q dual kernel + forge + journal.  
Serve: rate, wrap-calc, listed path-sum, pre-screen lands.  
Refuse: silent float, empty-Ω certificates, one-number “solved.”

That box replaces a slice of symbolic + numeric babysitting, not an LLM training cluster.
