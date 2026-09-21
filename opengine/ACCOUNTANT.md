# Journal for formal systems

```
python3 accountant.py   # 8/8
```

A post must name **G**, **V**, **mint**, **writes-by-slot**.  
If a written letter is not in V, **θ** is required. Silent credit is `BooksError`.

---

## Columns (more than two)

| column | job |
|---|---|
| kind | isolate / successor / meet / combinator / read / project / accumulate / refuse / migrate / merge |
| G | the map |
| V | listed letters this post may write |
| mint | generator of this line |
| writes | slot → letter |
| lands | every letter ∈ V |
| θ | required on a leak |
| reads | other named reads of the same write |
| leftover_of | (G1, G2, write1, write2) when two combinators ran |

Double-entry is the school+ credit alone. This journal keeps the count-read next to it.

---

## What it refuses

- no G, no V, no mint, no writes
- leak without θ (`isolate` seed 2 into `{0,1}`)
- θ on a write that landed
- unknown kind

---

## What it booked in the demo

| mint | lands | note |
|---|---|---|
| `S(2)` → 3 on `{0,1,2,3}` | yes | Peano letter |
| isolate imported 3 seed 1 | yes | numeral still imported; mint says so |
| seed 2 on bits, no θ | refused | hidden partiality |
| seed 2 on bits, θ named | posted leak | |
| lei+ `(1,1)*(1,1)` → r=2 | leak + leftover vs xor | |
| xorlei same input → r=0 | lands | |
| piles merge | lands | reads `school+=4` and `count=1` |
| rate xx/x | lands | reads top.r and bot.r still on the line |

---

## How to post a new machine

```python
j = Journal()
j.post(
    kind="combinator",
    G="your-map",
    V={...},
    mint="who wrote this",
    writes={"slot": letter},
    theta="why" if letter not in V else None,
    reads={"other-measure": value},
)
```

If you cannot fill those fields, it is not a claim yet (taxonomy #1, #20, #23).

The journal is a stipulated meter. Booking it as reality is error 1 on this file.
