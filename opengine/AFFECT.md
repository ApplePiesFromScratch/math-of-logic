# Prior affects

The leak is not “Leibniz is big.” Leibniz is two closed writes added.

```
python3 affect.py
python3 affect2.py
python3 test_affect.py   # 20/20
```

## The stack, smallest first

1. **Isolate** writes `(v, seed)`. Seed `2` into `Vr={0,1}` already does not land. The second slot exists before any mix.
2. **Value meet** :  usually `v*w`. On bits this closes.
3. **Two channel meets** :  `r·w` and `v·s`. **Each closes on bits.** `(1,1)*(1,1)` stays `(1,1)` if you keep only one.
4. **Combinator of those two writes.** Host `+` is the leak: `1+1=2`. `xor` / `or` / `max` close.
5. Optional **ε² term** (`0`, `ε`, `1`, `−1`). On host bits every one leaks. On wrap Z/2 every one closes, and `−1 ≡ 1`.
6. **Characteristic** is which combinator `+` is. Wrap-Leibniz at `(1,1)` is `(1,0)` because `2=0`. That is `d(x²)=0` in char 2, not a rounding error.

## Invented G inside the bit frame

`lei_xor`: `(v,r)*(w,s) = (v*w, (r*w) xor (v*s))`  
CLOSED. `(1,1)*(1,1)=(1,0)`. Same write as wrap-Leibniz on this pair.

`and_pair`: `(v∧w, r∧s)` CLOSED. Not a derivative. Same pair type, different G.

## Invalid G inside the same frame

Host `+` on bit pairs: one leak, the original `(1,2)`.

Switch G mid-stream without μ: xor-lei stays; host+ writes `2` and leaves `Vr`. After μ `Vr += {2}` that write lands and you have a different system.

## What generated the earlier effects

| later effect | prior affect |
|---|---|
| triangular `Lr=C(m,2)` | `+` on a listed initial segment |
| wrap vs host differ-by-1 on Z/2 | `+` vs fold of the same two meets |
| `D` strands when `Vr` grows | isolate wrote a letter `Vv` does not have |
| quot writes `−1` | combinator `−` on bits |
| jet writes `2` | third meet `2rs` is another `+` |
| compose `1→2→3` | `+` applied twice |
| Q-pairs “just work” | Q already closed under the combinator |

The frame is: **slot write + meet + combinator + listed alphabet.**  
Change any one, rescan. That is the dynamic map.
