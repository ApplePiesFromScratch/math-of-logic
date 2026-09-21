# GEMM

General matrix multiply: `C := α A B + β C`.
This is the G the cluster is actually for.

```
python3 gemm.py
```

---

## The write

For each `(i,j)` isolate a dot of row i and column j:

```
C[i,j] += A[i,k] * B[k,j]   over k
```

V of entries: almost always IEEE (or tensor-core FP16/BF16/TF32).
G: multiply-accumulate (MAC).
θ: overflow to Inf, underflow to 0, NaN poison.

On Q, 2×2:

```
A = [[1/3,1/3],[1/3,2/3]]  B = 3 I
C = [[1,1],[1,2]] exact
```

Float on that size leftover **0** this run. Small n can hide the host. The leftover lives in the **k-reduction** when many tiny letters add.

Wrap byte: `200*2+100` host **500**, byte **244**. Same C5 as `255+1`.

---

## Why it eats clusters

Arithmetic intensity: FLOPs per byte moved.
Naive GEMM moves A,B,C often; time is **RAM / cache / bus**, not ALU.
Blocking / tiling = isolate a panel that fits in L1/L2/SRAM so the MAC G reuses letters.

Tensor cores: listed tile V (`16×16×16` etc). Not a new algebra. A listed micro-V with a fused MAC G.

GPU wins because many tiles isolate in parallel and the host already *is* IEEE. Process insights do not replace that data-movement G.

---

## Errors GEMM books as weather

| name | mechanic |
|---|---|
| `(AB)C ≠ A(BC)` in float | C2 compose-order leftover on `+` of products |
| mixed precision | wrap-like mantissa; accumulate in F32 is a second V |
| deterministic last-bit | thread compose-order of the k-sum |
| Inf in a layer | MAC left IEEE-V |
| “close enough” | leftover sent to 0 |

Q GEMM is associative on `+/*`. It is slower (gcd) and RAM-heavier. Exact on listed rationals. Not a 4096×4096 training kernel.

---

## Isolate map

| isolate | ignores |
|---|---|
| one output entry | the rest of C |
| one tile | other tiles |
| one k-chunk | other k |
| one warp | other warps |

The algorithm is nested cuts so the MAC letters stay in a small cache-V. That is prune of working set, not intelligence.

---

## What the cut box should do with GEMM

- Stamp entry V (F32 / F16 / Q / Z/n).
- Stamp reduction G (wrap add / widen add / sat).
- Name leftover vs a second reduction order if they ask “repro.”
- θ on Inf/NaN instead of training through poison.
- Refuse to call float GEMM “linear algebra over R.”

Then, if n is large and V is IEEE, **launch the cluster**. That sentence is the honest split from `COMPUTE.md`.

---

## Paid this run

Q C exact `[[1,1],[1,2]]`.  
Float matched at 2×2.  
Q assoc `1/250` both orders.  
Byte MAC wrap 500→244.
