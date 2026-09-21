# Calculus Without The Limit: How A Derivative Actually Works

Every number below runs in five lines of Python. Copy any block, paste it, check it yourself.

## One object

A calculus course usually opens with `y = f(x)`, treats `x` as something varying on its own, and defines a derivative as a limit: shrink a gap toward zero and see what's left. That's real machinery. It also asks you to accept an infinite process as meaningful before you're allowed to compute anything.

Here's a smaller starting point. A `Reading` is a value and a rate, carried as a pair:

```python
from fractions import Fraction as F

class Theta(Exception): pass

class Reading:
    def __init__(s, v, r): s.v, s.r = F(v), F(r)
    def __mul__(s, o):
        o = o if isinstance(o, Reading) else Reading(o, 0)
        return Reading(s.v*o.v, s.r*o.v + s.v*o.r)
    def __sub__(s, o):
        o = o if isinstance(o, Reading) else Reading(o, 0)
        return Reading(s.v-o.v, s.r-o.r)
    def __pow__(s, n):
        out = Reading(1, 0)
        for _ in range(n): out = out*s
        return out
    def __truediv__(s, o):
        o = o if isinstance(o, Reading) else Reading(o, 0)
        if o.v == 0: raise Theta("quot: v=0")
        return Reading(s.v/o.v, (s.r*o.v - s.v*o.r)/(o.v*o.v))

def isolate(v, r=1): return Reading(v, r)
def rate(top, bottom): return top.r / bottom.r
```

This one class runs every example below. Nothing gets added partway through.

`isolate(v)` seeds a value with rate 1, meaning this is the thing everything else gets compared to. `rate` divides one channel by another. No limit appears in either line.

```python
>>> x = isolate(3)
>>> rate(x*x, x)
Fraction(6, 1)
```

Same answer as `d/dx[x^2]=2x=6` at `x=3`, reached by seeding a number and multiplying it by itself.

## The seed doesn't matter, checked seven ways

A natural worry: the seed you picked, 1, seems arbitrary. Change it and see.

```python
>>> for k in (1, 2, F(1,2), 10, F(1,3), -1, F(7,9)):
...     x = isolate(3, k)
...     print(k, rate(x*x, x))
1 6
2 6
1/2 6
10 6
1/3 6
-1 6
7/9 6
```

Seven different seeds, one of them negative, one of them an unusual fraction. The raw value and raw rate both scale by whatever number you picked. The ratio between them holds still. There's no independent variable with a life of its own here, just a ratio that doesn't care what units you measured the comparison in.

## Why the product rule adds two terms

A reasonable guess: if `f` changes at 6 per unit and `g` changes at 27, shouldn't `f*g` change at `6*27`?

```python
>>> x = isolate(3)
>>> f, g = x*x, x**3
>>> rate(f*g, x)
Fraction(405, 1)
>>> rate(f,x) * rate(g,x)
Fraction(162, 1)
```

Two different numbers, both computed exactly, and only `405` matches the power rule (`5x^4=5(81)=405`). Picture `f` and `g` as a rectangle's two side lengths. When both sides grow at once, the area gains from two sources simultaneously: the first side's growth spread across the second side's current length, plus the reverse. Multiplying the rates alone throws away both contributions and multiplies two rates as if they were values. Adding the two contributions, `r1*v2 + v1*r2`, is what actually tracks the area.

## What most courses never say about that formula

That "adding the two contributions" step depends on something worth naming: both slots of a Reading live in the rational numbers here, and rational numbers are closed under addition. Add two of them, you always get another one. That closure is doing real, unpaid work in the formula above, and it stops being free the moment the numbers get smaller.

```python
>>> Vv = Vr = {0, 1}   # restrict both slots to bits

>>> def host_leibniz(v1,r1,v2,r2): return (v1*v2, r1*v2+v1*r2)
>>> host_leibniz(1,1,1,1)
(1, 2)          # 2 is not in {0,1}
```

Same formula, smaller alphabet, and it produces a number outside the alphabet. The formula depends on where its numbers are allowed to live, on top of whatever multiplication itself means.

Two other ways of combining the same pair of contributions stay inside `{0,1}`:

```python
>>> def lei_xor(v1,r1,v2,r2): return (v1*v2, (r1*v2)^(v1*r2))
>>> def lei_or(v1,r1,v2,r2): return (v1*v2, (r1*v2)|(v1*r2))
>>> lei_xor(1,1,1,1)
(1, 0)
>>> lei_or(1,1,1,1)
(1, 1)
```

Checked across all sixteen possible inputs, not just this one: both close every time. `xor` isn't a curiosity. Combining two bits with `xor` is the same computation as adding them in arithmetic mod 2, the setting mathematicians call characteristic 2, where `1+1=0` by definition. In that arithmetic, `d/dx[x^2]=2x` genuinely equals zero, not because the derivative failed, but because `2` itself is `0` there. Same rule. Different alphabet underneath it.

The same pattern shows up on a bigger alphabet:

```python
>>> def unwrapped(v1,r1,v2,r2): return v1*v2, r1*v2+v1*r2
>>> def wrapped(v1,r1,v2,r2):
...     v,r = v1*v2, r1*v2+v1*r2
...     return v%3, r%3

# checked across all 81 combinations on {0,1,2}:
unwrapped leaks on 28 of 81
wrapped closes on all 81
```

One explicit step, reduce the output back into the alphabet before accepting it, closes what the plain formula leaves open. It's a decision about what to do with a number that would otherwise escape.

## Two more places the same thing happens

A derivative divides two rates. That division has its own alphabet.

```python
>>> Z5 = {0,1,2,3,4}
>>> F(1,2) in Z5
False        # ordinary division of 1 by 2 leaves Z/5 entirely

>>> def modinv(a,b,n=5):
...     for x in range(n):
...         if (b*x)%n==a: return x
>>> modinv(1,2)
3            # 2*3=6=1 (mod 5), stays inside Z/5
```

Checked across every nonzero pair in `Z/5`: ordinary division leaks on 8 of 20. Division by modular inverse closes on all 20. On the rationals, division already closes wherever it's legal, which is why nobody has to think about this there.

A second derivative needs a third number, `(v, r, r2)`. That third slot leaks the same way:

```python
>>> def mul_jet(a,b):
...     return (a[0]*b[0], a[1]*b[0]+a[0]*b[1], a[2]*b[0]+2*a[1]*b[1]+a[0]*b[2])
>>> mul_jet((0,1,0),(0,1,0))
(0, 0, 2)    # third slot writes 2, via the 2rs cross term
```

Same shape as the product rule's leak, one level deeper.

## The chain rule is cancellation

```python
>>> x = isolate(2)
>>> y = x*x
>>> w = y**3
>>> rate(w, x)
Fraction(192, 1)
>>> rate(w, y) * rate(y, x)
Fraction(192, 1)
```

Both routes land on the identical number. `y`'s channel appears once in a numerator and once in a denominator across the two ratios being multiplied, and a shared factor between a numerator and a denominator cancels, the same fact about fractions you already knew before either ratio got written down.

## Reading 0/0 correctly

`(x^2-1)/(x-1)` at `x=1`. Top and bottom are both zero.

```python
>>> a = isolate(1)
>>> num, den = a*a - 1, a - 1
>>> num.v, den.v
(Fraction(0, 1), Fraction(0, 1))
>>> num / den
Theta: quot: v=0
>>> rate(num, den)
Fraction(2, 1)
```

Dividing the values has no answer, and refusing is correct. Dividing the channels, `num.r/den.r`, was never stuck. L'Hopital's rule isn't "differentiate again and hope." It's "the first operator was the wrong one to ask."

## The actual case for fewer steps

```python
>>> def counted():
...     n = [0]
...     def add(a,b): n[0]+=1; return a+b
...     def mul(a,b): n[0]+=1; return a*b
...     def div(a,b): n[0]+=1; return a/b
...     def sub(a,b): n[0]+=1; return a-b
...     return n,add,mul,div,sub

>>> n,add,mul,div,sub = counted()
>>> vv,vr,rv = mul(F(3),F(3)), mul(F(3),F(1)), mul(F(1),F(3))
>>> out = div(add(vr,rv), F(1))
>>> n[0], out
(5, Fraction(6, 1))

>>> n2,add2,mul2,div2,sub2 = counted()
>>> h = F(1,2)
>>> three_h = add2(F(3), h)
>>> q = div2(sub2(mul2(three_h,three_h), mul2(F(3),F(3))), h)
>>> n2[0], q
(5, Fraction(13, 2))
```

Five operations, three primitives, one number system, two paths. One reaches `6`. The other reaches `13/2`, which is `6+h`, not `6`. Getting from `6+h` to `6` isn't addition, subtraction, multiplication, or division. It's a limit, a sixth kind of move the first path never needed. That's the whole content of "fewer steps," counted rather than felt.

## How to build a different one

```python
def scan_closure(Vv, Vr, mix_fn):
    for v1, r1, v2, r2 in product(Vv, Vr, Vv, Vr):
        v, r = mix_fn(v1, r1, v2, r2)
        if v not in Vv or r not in Vr:
            return False
    return True
```

Pick a value space for each slot. Pick a rule for combining two Readings. Check every input. If every output lands back inside the spaces you started with, you have a working calculus on that alphabet. If one input escapes, you know exactly where, and you get to decide: wrap the output, refuse the input, or grow the alphabet to hold it.

That's the whole of it. A calculus isn't a formula handed down. It's an alphabet, a combining rule, and a check that the rule never produces something the alphabet can't hold.

---

*Full workbook, every claim checked against runnable code: link below.*
