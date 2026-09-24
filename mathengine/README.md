# process-math

One engine. Q is a reconfiguration snapshot `(a, b)`, not a finished rational.

```
python3 tests.py
python3 engine.py x*x 3
python3 engine.py x**3 2/3
python3 engine.py x*x+2*x 3
```

```
x*x at 3       value (9, 1)    rate (6, 1)
x*x+2*x at 3   value (15, 1)   rate (8, 1)
x**3 at 2/3    value (8, 27)   rate weighs (4, 3)
seed 2 on x*x  snapshot (12, 2)  weighs (6, 1)
```

`tests.py` prints `TESTS PASS`.

---

## What it is

- `isolate(v, seed)` — two histories
- `mix` — stipulated Leibniz on those histories
- `rate(P, G)` — weigh of the two seed-histories
- `weigh` — `ad = bc`, not object identity
- `run("x*x+2*x", 3)` — parse + gauge on seeds `1, 2, -1`
- `certify` — empty grid is θ

Allowed expr: `x`, integers, `a/b`, `+ - * **nat`, `()`.
θ: empty expr, seed 0, bad paren, leftover tokens, `**` non-nat, empty certify.

No float. No limit. No `Fraction` on the page.

---

## Not this engine

Word problems. `sin`. `sqrt`. Division by a live `x` at 0 (write a new mix + θ).
SymPy replacement. GSM8K mind.

---

## GitHub

```
git init
git add engine.py tests.py README.md LICENSE
git commit -m "process-math: snapshots not finale Q"
git remote add origin git@github.com:YOURUSER/process-math.git
git push -u origin main
```
