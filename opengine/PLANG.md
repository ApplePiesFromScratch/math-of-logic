# Process language

```
python3 plang.py
# PLANG PASS
```

Verbs: `V` `G` `mint` `write` `read` `theta` `post` `need` `map` `prune` `clear`.

A `post` must name G, V, mint, writes. Leak without `theta` is `PFail`. `theta` on a landing write is `PFail`. `need` checks the last post.

```
V 0 1 2 3
G isolate
mint x
write v=3 r=1
post
need lands=1
```

Piles post kept `school+=4` and `count=1`. Seed 2 on `{0,1}` posted only with theta. Bare leak did not post.

After `map two-reads` / `map leak` / `prune` on the piles cut, maps left: `{named-G}`. Unsupported maps dropped. `named-G` still survives (method `A=A`).
