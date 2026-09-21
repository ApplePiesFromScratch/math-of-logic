# Piles

`python3 piles.py`

Two piles on the left, two on the right, merge in front.

```
pile-count  4 -> 1
volume      4 -> 4
grains      4000 -> 4000
locations   {left, right} -> front
school +    2+2=4
count-read of the merge = 1
```

One write: both sides occupy `front`.  
Several reads of that write.

You were not measuring volume. The 4 still arrives because school `+` is the volume/grain combinator, booked as *the* addition. The count combinator of the same merge writes **1**.

This is C1 (two combinators, one word `+`), error 3 (project a read and call it the sum), error 4 (host `+` as essence), error 9 (two reads booked as one law).

Platonist move: the 4 was in the piles.  
The 4 is the read you did not take. The write you took dropped the count.

Same pattern as:
- independence product `1/4` vs Leibniz channel `1/2`
- Born 1 vs two phases
- wrap `2=0` vs host `2`
- vacuum min vs wall min when λ flips

Merge is not broken. The noun `+` was carrying four G.
