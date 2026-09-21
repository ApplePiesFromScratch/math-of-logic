# The cut box

Most powerful small thing we can actually build:
a **poster that sits in front of math and compute**, not a tiny GPU.

Budget: **$0 software** (this folder + a laptop). Optional **~$80–150** Pi 5 8GB if you want a lab brick.

---

## What it is

One process:

```
input:  G, V, writes  (or a plang snippet, or isolate/rate)
output: lands | θ | leftover | two reads | mint
no output: silent Inf, empty-Ω certificate, one-number “solved”
```

V1 contents (already almost here):

- Q dual kernel (`isolate` / `rate` / lei) exact
- wrap Z/n + forge 16
- journal (`accountant.py` / `plang.py`)
- pre-screen: does this write stay in V?
- leftover named (grid integral, train vs test, two combinators)
- prune unsupported maps

V1 does not: train an LLM, replace MATLAB, prove RH.

---

## What it changes

Today: pick a host (R, float, GPU), run, patch NaN / Inf / “almost.”

Cut box: **post first.** If it leaks, you wrap, μ in public, change G, or θ. Only then, if the host-R job is still required, you spend cluster.

That flips the queue. The 80% theater jobs never launch. The 20% GEMM still do.

Also changes teaching: rate on Q in five minutes, leftover on the page, no ε-δ as entry tax.

Also changes LLM-code: generated string is mint A; `plang`/compiler post is mint B. CI refuses val-eq.

---

## Why this and not a bigger model

A small exact poster plus θ is a new **gate**.  
A small inexact model is another decode-G on IEEE.

Gates change what is allowed to count as a result. That is how UNIX (small syscall V) and Rust (owner θ) changed practice: not by FLOPS.

---

## Hardware if you want a brick

Pi 5 8GB + SSD + a one-button “run journal.”  
Enough for Q dual, wrap, forge, listed path-sums, class-sized Ω.  
Not enough for fine-mesh CFD. Do not sell it as that.

---

## 90-day build

1. Single package: `plang` + Q kernel + journal CLI.  
2. Ten lab cards: rate x², leak on bits, piles two-reads, empty Ω θ, 0.1+0.2, E0382-shaped move, softmax underflow θ, train/test line, wrap vs host, prune I.  
3. CI hook: PR must attach a post file.  
4. Optional Pi image.

Success metric: a claim that used to ship as one number now fails CI without leftover + V + mint.

That is the change. Not a cluster in a sandwich bag.
