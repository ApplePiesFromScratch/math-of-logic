# Real, imaginary, complex :  the mechanics

```
python3 complex.py
```

Same pair machine as Readings. Different square-rule for the second slot.

---

## 1. The second letter

You have a slot `a` and you adjoin a letter `u` with one rule: what `u·u` writes.

| name | rule | `u*u` lands in | host `(0,1)*(0,1)` |
|---|---|---|---|
| dual `ε` | `ε²=0` | nowhere | `(0,0)` |
| complex `i` | `i²=-1` | **value** slot, minus | `(-1,0)` |
| split `j` | `j²=+1` | **value** slot, plus | `(1,0)` |
| idempotent `ε` | `ε²=ε` | **channel** slot | `(0,1)` |

Mix on pairs `(a,b)`, `(c,d)`:

```
value   = a*c  +  (square-rule applied to b*d)
channel = a*d + b*c  +  (optional leftover)
```

Leibniz / dual: square-rule writes **0** to value. Channel gets `ad+bc` only.  
Complex: square-rule writes **`-bd`** to value. Channel still `ad+bc`.

That is all “imaginary” is doing. The self-meet of the second slot is allowed to write the first slot.

School name “imaginary” is the marketing for: this letter is not in the old `Vv`, and its square is.

---

## 2. “Real”

Two different cuts, often conflated:

**Slice:** pairs with second slot dead: `(a,0)`.  
`(5,0)*(3,0)=(15,0)` stays on the slice for dual, complex, and split. That slice is a subalgebra.

**Projection:** `π_value(a,b)=a`.  
`(2,3)*(1,4)=(-10,11)`. `π_value=-10` dropped `11`. Not invertible. Same bug as `π_v` on a Reading.

“The real line” as used in calculus is usually the slice (dead second slot) **plus** an unpaid `+closed` host (Q or R). Completeness / smoothness is the same pre-load as before.

---

## 3. What closes

Host `+/*` on bits, Z/5, `{-3..3}`: **none** of the four rules close. Complex leaks immediately: `i*i=(-1,0)` and `-1` is not in bits or Z/5.

Wrap `Z/n` (both slots): all four close.

```
Z/2  complex i*i = (1,0)    because -1 ≡ 1  (complex = split)
Z/3  complex i*i = (2,0)    because -1 ≡ 2
Z/5  complex i*i = (4,0)    because -1 ≡ 4
```

Char 2 collapses `i²=-1` with `j²=+1`. You do not have complex-as-distinct-from-split until `-1≠1`.

Gaussian-like host on Z: you need `-1` already in `Vv`. That is why “reals then adjoin i” is the story :  `Vv` was grown to include the letter `i²` writes **before** the adjunction is closed.

---

## 4. Same pair, four writes at `(1,1)*(1,1)`

```
dual     (1, 2)     1+2ε
complex  (0, 2)     (1+i)² = 2i
split    (2, 2)     (1+j)² = 2+2j
```

Dual dumps the extra `2` into the **channel** (Leibniz leak on bits).  
Complex dumps `i²=-1` into the **value** (`1-1=0`) and still writes channel `2`.  
One pair type. Four G. Four remainders.

Readings in the workbook are dual numbers (`ε²=0`) on Q. Complex is the same slots with a different square-rule. The book’s Ch.20 line “grow V to include `i`” is this adjunction, not a new ontology.

---

## 5. Isolation again

`isolate` for complex is: pick `(a,b)` with `b` a letter of the second alphabet.  
`i` is `isolate` of `0` with seed-slot `1` in the *adjoined* alphabet :  `(0,1)`.  
`3` “real” is `(3,0)`.  
`3+2i` is `(3,2)`.

No mysticism. Two listed alphabets and a square-rule that may write across them.

Rate on a complex pair is a different question (Wirtinger, etc.). That would be a third read, not a third substance.

---

## 6. Outputs treated as primitive

| sold as a thing | process | unpaid if primitive |
|---|---|---|
| “the imaginary unit” | adjoin `u` with `u²=-1` | the square-rule and the growth of `Vv` to hold `-1` |
| “a complex number” | pair + that mix | same |
| “the real part” | `π_value` or dead-slice | which cut you used |
| “R ⊂ C” | dead-slice embedding | not the projection |
| “C is a field” | wrap or Q-host so `/` lands | `Vq`; Z[i] is not a field |

---

## 7. Falsifiers

- If `i*i` on bits host lands in `{0,1}²`, the `-1` growth claim dies.
- If wrap Z/2 keeps complex ≠ split, `-1≡1` died.
- If `π_value` recovers the dropped slot, the pair was never needed.
- If `(a,0)*(c,0)` leaves the dead slice under complex mix, the subalgebra claim dies.
