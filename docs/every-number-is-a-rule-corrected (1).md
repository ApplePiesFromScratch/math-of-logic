*A Workbook, Complete Edition*

# Every Number Is A Rule

### A Full Calculus, Built From Three Moves And One Alphabet, With Nothing Imported

James Pugmire


---


## Before We Start

This book builds one machine and uses it the whole way through. The machine has an alphabet: pairs of fractions, written `(value, rate)`. It has three moves: `isolate`, which builds a pair from a starting number and a starting rate; `mix`, which combines two pairs by a rule fixed once and used everywhere; and `rate`, which reads off how fast one pair is changing compared to another. Addition and subtraction work piece by piece. Division gets derived from `mix`, not added as a fourth move.

Every number that appears in this book, from the first rate to the square root of 2 to the number `e` to an exact turn through a circle, is the *output* of running these three moves over that alphabet, a specific number of steps, checkable by hand. No number in this book is ever asserted to simply exist, ahead of the steps that produce it. When a number needs more steps than fit on a page, what you get instead is the rule itself: a finite procedure that produces the number to any precision you name, with the exact remaining gap stated, not estimated.

This edition adds three things the first edition didn't reach: a rate that has its own rate, built by nesting the machine inside itself with no new rule written; a way to find exactly when and where two moving things meet, using nothing but subtraction and division; and a second, exact construction for turning and rotation, built from whole-number pairs instead of an infinite series. All three come from the same three moves. Nothing new was adjoined to reach them.


### How This Book Works

Every unit has a big question, an explanation with the reason attached, worked examples done slowly, a "Try It Yourself" with a hint, and practice problems using only what's been covered so far. Answers are in the back, organized by unit.

Some rules in this book are forced: once you fix what came before, they can't come out any other way, and the demonstration shows why. Others are picked, because picking them is useful, and a purple box marked **A choice, not a discovery** says so and says what the choice buys. The book never claims more certainty than a rule earns, and it never calls two different constructions the same thing just because they rhyme.


---


*Unit 1*

## The Alphabet And The First Move


> **Big Question:** How do you write down a number and how fast it's changing, at the same time, without losing either one?

Everything in this book is built on one alphabet: pairs of fractions, `(value, rate)`. Nothing else gets adjoined to it, ever, unless a unit says so explicitly and names what the addition buys.

Picture a bathtub. Right now it has 8 gallons in it. The faucet is adding 2 gallons every minute. Two facts, true at the same moment: the amount right now, and how fast that amount is changing. Write both together as a pair: `(8, 2)`.


> **Why write it this way?** A number alone can't say whether it's about to grow, shrink, or sit still. "8 gallons" alone says nothing about the next minute. Keeping the two numbers glued together as one pair means the second fact is never lost.


### The First Move: isolate

The move that produces a pair from a starting value and a starting rate is called `isolate`. Everything else in this book is built by combining outputs of `isolate`.


*Demonstration 1: isolate(8, 2)*

```
isolate(8, 2)  means  "start at 8, with a rate slot of 2"

isolate(8, 2)  outputs  (8, 2)
```


*Demonstration 2: a rate of 0*

```
A puddle has 3 cups of water and nothing is being added or removed.

isolate(3, 0)  outputs  (3, 0)
```


*Demonstration 3: the shortcut*

```
isolate(5)  is short for  isolate(5, 1)  outputs  (5, 1)

Seeding something with rate 1 means: this is the thing everything
else gets compared to, so of course it moves at rate 1 relative
to itself. Unit 2 shows exactly why that's useful.
```


**Try It Yourself:** A plant is 12 centimeters tall and growing 1 centimeter per week. What does `isolate` output for this? *Hint: value first, then rate.* Answer: `isolate(12, 1)` outputs `(12, 1)`.


### Practice: Unit 1


1. A savings account has $40 in it and grows by $3 a week. What does isolate output?

2. A candle is 15 cm tall and isn't lit. What does isolate output?

3. What does `isolate(20, 4)` output, and what does each number mean?

4. A pool has 500 gallons and is draining at 10 gallons a minute. What does isolate output? (A rate can be negative.)

5. What does `isolate(7)` output, without writing the rate out? What rate does the shortcut assume?

---


*Unit 2*

## The Second Move: Reading A Rate


> **Big Question:** Given two outputs of isolate, how do you find out how fast one is changing compared to the other?

Two hoses filling two buckets. Hose A fills at 4 gallons a minute, Hose B at 2. Hose A is filling twice as fast, found by dividing the two rates: `4/2 = 2`. That's the second move, called `rate`. Given two pairs, it divides the second slot of one by the second slot of the other. It never looks at the first slot of either.


*Demonstration 1: rate(A, B)*

```
A = isolate(10, 4)  outputs  (10, 4)
B = isolate(5, 2)   outputs  (5, 2)

rate(A, B)  =  4 / 2  =  2

A is changing twice as fast as B.
```


> **Why does rate ignore the first slot?** "How much faster is A changing than B" is a question about speed, not about where each one started. A car at 60 mph is going twice as fast as a car at 30 mph, whether the fast car started the trip at mile 0 or mile 500. Only the rate slot answers a question about speed.


*Demonstration 2: comparing an output to itself*

```
x = isolate(7)  outputs  (7, 1)

rate(x, x)  =  1 / 1  =  1

Anything compared to itself outputs rate 1 when its rate slot is
not 0, no matter the value. A rate slot of 0 has nothing to land
on. Unit 6 names that refusal. The shortcut rate of 1 means this
is what everything else gets compared to, and the comparison can
land.
```


**Try It Yourself:** E = isolate(9,6), F = isolate(2,3). What does rate(E,F) output? *Hint: divide the two rate slots.* Answer: rate(E,F) = 6/3 = 2.


### Practice: Unit 2


1. P=isolate(30,8), Q=isolate(10,4). What does rate(P,Q) output?

2. M=isolate(6,9), N=isolate(1,3). What does rate(M,N) output?

3. If rate(A,B) outputs 3, what does that tell you about how A is changing compared to B?

4. What does rate(x,x) output for x=isolate(50,6), without dividing? Explain how you knew.

5. G=isolate(100,12), H=isolate(8,4). What does rate(G,H) output?

6. Explain why rate never uses the first slot of either pair.

---


*Unit 3*

## The Third Move: Mixing Two Readings


> **Big Question:** If two things are both changing, and you combine them by multiplication, how fast does the result change?

Build this one slowly, with a picture, before touching a rule.


### The Growing Rectangle

A rectangle whose width is growing and whose height is *also* growing, at the same time. What happens to its area? Sketch it: the right edge sliding out, the top edge sliding up, both at once. The area gains new space from two directions:

- A thin new strip along the right edge, as wide as the width is growing, as tall as the *current* height
- A thin new strip along the top edge, as tall as the height is growing, as wide as the *current* width

Miss either strip and you've undercounted the growth. Add exactly these two strips to the starting area, and that sum is what the rule below outputs, in full.


*[Diagram: The starting area plus the two strips. That sum is the whole output. (see the PDF for the image)]*


### The Rule

This move is called `mix`. Given two outputs of isolate, `(v1,r1)` and `(v2,r2)`, it's fixed once, here, and used everywhere in this book from here on:


*The mix rule*

```
mix( (v1,r1), (v2,r2) )  outputs  (v1*v2,  r1*v2 + v1*r2)

new value  =  v1 * v2                 (ordinary multiplication)
new rate   =  r1*v2  +  v1*r2         (the two strips, added)
```

`r1*v2` is the first strip: how fast the first number is growing, spread across the second number's current size. `v1*r2` is the second strip, the other way round. This book writes `mix(A,B)` as `A*B` from here on, since it's the only multiplication a pair ever uses.


*Demonstration 1: x = isolate(4), mix(x,x)*

```
x = isolate(4)  outputs  (4, 1)

mix(x,x):
  new value = 4*4 = 16
  new rate  = (1*4) + (4*1) = 8

mix(x,x)  outputs  (16, 8)

rate(mix(x,x), x)  outputs  8
```


*Demonstration 2: x = isolate(3), mix(x,x)*

```
x = isolate(3)  outputs  (3, 1)

mix(x,x):
  new value = 3*3 = 9
  new rate  = (1*3) + (3*1) = 6

mix(x,x)  outputs  (9, 6)

rate(mix(x,x), x)  outputs  6
```

In both demonstrations the rate that comes out, 8 and 6, is exactly double the value fed in, 4 and 3. Not a coincidence: seeded with rate 1, both strips equal the value itself, so together they output double it.


**Try It Yourself:** x = isolate(6). What does mix(x,x) output, and what does rate(mix(x,x),x) output? *Hint: new value = 6*6. new rate = (1*6)+(6*1).* Answer: mix(x,x) outputs (36,12). rate(mix(x,x),x) outputs 12.


### Practice: Unit 3

For each, isolate the value, then find what mix(x,x) and rate(mix(x,x),x) output. Show both strips before adding.


1. x = isolate(7)

2. x = isolate(8)

3. x = isolate(9)

4. x = isolate(5)

5. Predict, without arithmetic, what rate(mix(x,x),x) outputs for x=isolate(12). Then check.

6. A classmate says "why not just multiply the two rate slots instead of adding two strips?" For x=isolate(3), that would output 1*1=1. Compare to the real output from Demonstration 2, 6. What does that tell you?

---


*Unit 4*

## Bigger Powers


> **Big Question:** Unit 3 mixed two outputs of isolate. What if you need to mix three, or ten?

Nothing new. `x*x*x` is `mix(x,x)`, then mixed with `x` again, the same rule from Unit 3, applied twice.


*Demonstration 1: x = isolate(2), x*x*x*

```
x = isolate(2)  outputs  (2, 1)

Step 1: mix(x,x)
  new value = 2*2 = 4
  new rate  = (1*2)+(2*1) = 4
  mix(x,x) outputs (4, 4)

Step 2: mix(mix(x,x), x), using (4,4) and (2,1)
  new value = 4*2 = 8
  new rate  = (4*2)+(4*1) = 12
  outputs (8, 12)

rate(x*x*x, x) outputs 12
```


> **Why does this work?** The mix rule from Unit 3 takes any two pairs, not just two direct outputs of isolate. mix(x,x) is itself a pair, so mixing it with x again uses the identical rule, with nothing new to check.


*Demonstration 2: x = isolate(4), x*x*x*

```
Step 1: mix(x,x) outputs (16, 8)
Step 2: mix((16,8),(4,1)): value=16*4=64, rate=(8*4)+(16*1)=48
outputs (64, 48)

rate(x*x*x, x) outputs 48
```

At `x=2` the rate output was 12, and `3*2*2=12`. At `x=4` it was 48, and `3*4*4=48`. Cubing always outputs a rate of `3` times `x` times `x`, built here from two applications of one rule, not handed down as a formula.


### Any Number Of Mixes, Not Just Three

Mix `x` with itself `n` times, for any whole number n, and a pattern holds every time: the value is `x` to the n, and the rate is `n` times `x` to the `n-1`. Not asserted, checked.


*Demonstration 3: checking the pattern up to the sixth power, x=isolate(2)*

```
power n    value (2^n)    rate output    n * 2^(n-1)
  2            4              4               4
  3            8             12              12
  4           16             32              32
  5           32             80              80
  6           64            192             192

Every row checked by actually running the mix rule n-1 times, not
by trusting the formula. The pattern holds at every power tried,
here and at other starting values.
```


> **Why does the exponent show up as a multiplier?** Each additional mix with x adds one more "copy" of x contributing a strip, and the bookkeeping from Unit 3 stacks: going from x^(n-1) to x^n multiplies the rate output by x and adds one more full copy of the value, which is exactly what turns "n-1 copies" into "n copies" one mix at a time. Unit 17 names what this pattern is called in a full course; this book builds it before naming it.


**Try It Yourself:** x=isolate(3). What does x*x*x output? *Hint: Step 1 fully, before Step 2.* Answer: Step 1: mix(x,x) outputs (9,6). Step 2: value=9*3=27, rate=(6*3)+(9*1)=27. Outputs (27,27). Check: 3*3*3=27.


### Practice: Unit 4


1. x = isolate(5). What does x*x*x output?

2. x = isolate(6). What does x*x*x output?

3. Predict the rate for x=isolate(10) using 3*x*x, then check by doing both steps.

4. Using the pattern from Demonstration 3, predict rate(x^5,x) for x=isolate(3) without running all four mixes. Then check by running them.

---


*Unit 5*

## Why The Starting Rate Doesn't Matter


> **Big Question:** Unit 1's shortcut, isolate(5), used seed rate 1. Would a different seed, even a negative one, change what later steps output?

Test it instead of assuming it.


*Demonstration 1: x = isolate(5, seed), four seeds*

```
seed 1:  x=(5,1)   x*x outputs (25,10)   rate outputs 10
seed 2:  x=(5,2)   x*x outputs (25,20)   rate outputs 10
seed 3:  x=(5,3)   x*x outputs (25,30)   rate outputs 10
seed 10: x=(5,10)  x*x outputs (25,100)  rate outputs 10

The rate slot inside x*x changes every time. rate(x*x,x)'s output
does not move. It's 10, every time.
```


> **Why doesn't the seed matter?** rate divides x*x's rate slot by x's rate slot. Whatever seed you pick lands in both the top and bottom of that division, in matching amounts, and cancels. Doubling the seed doubles both numbers being divided, and a fraction doesn't change when you double its top and bottom together.


*Demonstration 2: a negative seed*

```
x = isolate(5, -3)   outputs  (5, -3)

x*x:
  new value = 5*5 = 25
  new rate  = (-3*5)+(5*-3) = -15-15 = -30

mix(x,x) outputs (25, -30)

rate(x*x, x) outputs  -30 / -3  =  10

Same output, 10, even though every number along the way turned
negative. The two negatives cancel in the division exactly the
way two positive copies of the same seed did above.
```


> **What does a negative seed record?** Flipping the seed flips both ends of rate(x*x, x) together, and the answer stays put, as the -30 / -3 above shows. The label moved. The relation did not. A minus can also be the relation itself. Two departures, 5 and -3, give rate -5/3. Flip both labels and it is still -5/3. A bank balance is a different minus: owing and forgiving move a pile from one side to the other. Two cars driving apart are not. One pays rope out, one has the rope tied to the bumper. The rope gets longer. Nothing left the first car and arrived in the second.


**Try It Yourself:** x=isolate(4,5). What does x*x output, and rate(x*x,x)? *Hint: new value=4*4. new rate=(5*4)+(4*5).* Answer: x*x outputs (16,40). rate outputs 40/5=8, same as Unit 3 Demonstration 1's seed-1 output.


### Practice: Unit 5


1. x=isolate(3,2). What does rate(x*x,x) output? Compare to Unit 3 Demonstration 2 (seed 1).

2. x=isolate(7,4). What does rate(x*x,x) output? Compare to Unit 3 Practice Problem 1.

3. x=isolate(6,-1). What does x*x output, and rate(x*x,x)? Compare to the seed-1 output for x=isolate(6) from Unit 3's Try It Yourself.

4. Explain why the seed cancels out, using the word "divide."

---


*Unit 6*

## Chains, And When A Comparison Has Nothing To Land On


> **Big Question:** What if a quantity depends on another quantity, instead of being isolated directly?


### Multiplying By A Plain Number

First, one small piece. A plain number, like 2, is what isolate outputs with rate 0, the same as Unit 1's puddle. So multiplying by a plain number is mix, using Unit 3's rule, against an output with rate 0.


*Demonstration 1: t = isolate(2), mixed with the plain number 2*

```
t = isolate(2)  outputs  (2, 1)
2 as an output of isolate with rate 0: (2, 0)

mix(t, 2): new value=2*2=4, new rate=(1*2)+(2*0)=2
outputs (4, 2)
```

Both slots of t just get multiplied by 2, because the second strip always vanishes: the plain number's own rate is 0.


### The Chain

A machine with two rooms. Room 1 takes t and outputs u = mix(t,2). Room 2 takes u and outputs y = mix(u,u). y doesn't depend on t directly, only through u.


*Demonstration 2: t = isolate(2), through both rooms*

```
t = isolate(2)          outputs (2, 1)
u = mix(t, 2)            outputs (4, 2)
y = mix(u, u)            new value=4*4=16, new rate=(2*4)+(4*2)=16
                         outputs (16, 16)

rate(y, t) outputs 16/1 = 16

Room by room instead:
rate(y, u) outputs 16/2 = 8
rate(u, t) outputs 2/1 = 2
rate(y,u) * rate(u,t) outputs 8*2 = 16

Both paths output the same number.
```


> **Why do both paths agree?** rate(y,u) is a fraction with u's rate slot on the bottom. rate(u,t) is a fraction with u's rate slot on top. Multiplying them, u's rate cancels, the same way (8/2)*(2/1) simplifies before you multiply. Room 2 never has to know t exists; u carries everything Room 2 needs.


### When A Comparison Has Nothing To Land On

Unit 1 showed isolate can output rate 0, like an unlit candle. What happens if you try rate against one of those?


*Demonstration 3: comparing against something that isn't moving*

```
bathtub = isolate(8, 2)     outputs (8, 2)
candle  = isolate(15, 0)    outputs (15, 0)

rate(bathtub, candle)  =  2 / 0  =  theta

The machine refuses on purpose and names the refusal: theta,
isolator r=0. Not a big number, not zero, not a bare arithmetic
error inherited from the host. A refusal this book states and
means.
```


> **Why doesn't this have an output?** "How many times faster is the bathtub filling than the candle is growing" only makes sense if the candle is changing at all. It isn't. There's no rate to compare against, and no rule can manufacture one.


> **Zero apples, ten apples** If you have 0 apples and a friend has 10, your friend does not have "10 times as many" apples as you. Ten times zero is zero, not ten, and "how many times more" is a question that only makes sense when there's a nonzero amount to be a multiple of. Asking for a ratio to nothing isn't a hard question with a very large or very small answer. It's not the right shape of question to ask. rate(bathtub, candle) is the exact same situation: the candle's rate is the "0 apples," and asking how many times faster the bathtub is filling, compared to that, has nothing to be a multiple of. theta is the honest name for that, not a stand-in for "a huge number" or "basically zero."


**Try It Yourself:** Same two-room machine, t=isolate(5). What does y output, rate(y,t) directly, and rate(y,u)*rate(u,t)? *Hint: Room 1 first, u=mix(t,2)=(10,2).* Answer: u outputs (10,2). y outputs (100,40). rate(y,t) outputs 40. rate(y,u)*rate(u,t)=20*2=40.


### Practice: Unit 6

For each, use u=mix(t,2), y=mix(u,u). Find what y, rate(y,t), and rate(y,u)*rate(u,t) output, and confirm they agree.


1. t = isolate(1)

2. t = isolate(3)

3. t = isolate(4)

4. J=isolate(40,5), K=isolate(20,0). What does rate(J,K) output, and why?

5. Explain why Room 2 doesn't need to know t exists.

6. A classmate says "rate(J,K) from problem 4 must be some huge number, since K's rate is basically nothing." Using the zero-apples idea, explain what's wrong with "huge number" as the answer.

---


*Unit 7*

## Running The Machine On A Bigger Expression


> **Big Question:** Units 1 through 6 combined two outputs at a time. What happens when you chain several mixes and adds together in one expression?

Nothing new. Every step is still Unit 3's mix rule or piece-by-piece addition, applied as many times as the expression has operations.


*Demonstration 1: f(x) = x*x + 3*x, at x = isolate(2)*

```
x*x    =  mix((2,1),(2,1))          outputs  (4, 4)
3*x    =  (2,1)+(2,1)+(2,1)         outputs  (6, 3)
sum    =  (4,4) + (6,3)             outputs  (10, 7)

Check by hand: x*x+3x at x=2 is 4+6=10. The rate rule, applied
twice and added once, output 7 with no extra machinery.
```


*Demonstration 2: f(x) = x*x*x + 2*x + 1, at x = isolate(2)*

```
x*x        outputs (4, 4)
x*x*x      =  mix((4,4),(2,1))     outputs  (8, 12)
2*x        outputs  (4, 2)
sum so far =  (8,12)+(4,2)         outputs  (12, 14)
+ 1        =  (12,14)+(1,0)        outputs  (13, 14)

Nothing in this calculation was written to find a rate
specifically. It was written to find a value, one mix and one
add at a time. Carrying the pair through every step made the
rate output come out exact alongside it.
```


> **Why does chaining several operations still output the exact rate?** Because mix and add were fixed in Units 3 and 6 to work on any two pairs, not only direct outputs of isolate. mix(x,x) is itself a pair, so mixing it with x again is the same rule, with no new case to write.


**Try It Yourself:** Run f(x)=x*x-x at x=isolate(3), one step at a time. *Hint: x*x first, then subtract x.* Answer: x*x outputs (9,6). Subtract x=(3,1): outputs (6,5).


### Practice: Unit 7


1. Run f(x)=x*x+x at x=isolate(4), step by step.

2. Run f(x)=x*x*x at x=isolate(1), step by step.

3. Run f(x)=x*x-x at x=isolate(5). Check the value against plain arithmetic: 5*5-5.

4. Explain why mix doesn't need a separate case for "the second multiplication in a chain" versus "the first."

5. Run f(x)=x*x*x-x at x=isolate(3).

---


*Unit 8*

## A Rate That Has Its Own Rate


> **Big Question:** Unit 3's rate slot tells you how fast a value is changing. Can that rate slot itself be changing, and if so, does the machine need a new rule to track it?

Picture a car. Its position has a rate: speed. Its speed, in turn, can have a rate too: speeding up or slowing down. Nothing about the machine built so far stops a pair's rate slot from changing. What stops it is that the machine, so far, only ever wrote a plain number into the rate slot. Add a third number, and ask whether the existing rules already know what to do with it.


### Extending A Pair To A Triple

Write a triple `(value, rate, curve)`, where `curve` means "the rate of the rate," how fast the rate slot itself is changing. Seed `x` the same way as always, except now the seed states all three: `x = (v, 1, 0)`, read as "x's own rate is 1, and that rate isn't itself changing, its curve is 0."


> **Why does x get curve 0?** x is being compared to itself. Its rate relative to itself is always 1 (Unit 2), a constant, and a constant number has no rate of its own, so the rate of that rate is 0. The same reasoning that gave isolate's rate shortcut (Unit 1) gives this one.


### Finding The Rule, Not Guessing It

The value and rate slots of a triple still follow Unit 3's mix rule exactly: `new value = v1*v2`, `new rate = r1*v2 + v1*r2`. The question is what the curve slot has to be. Answer it by asking for the rate of the rate, applying Unit 3's rule a second time, to each of the two strips separately.


*Demonstration 1: deriving the curve rule, strip by strip*

```
new rate  =  r1*v2  +  v1*r2         (Unit 3's two strips)

Find the rate of EACH strip, using the mix rule on each one:

rate of (r1*v2)  =  (rate of r1)*v2 + r1*(rate of v2)
                  =  c1*v2  +  r1*r2          [c1 is r1's own curve]

rate of (v1*r2)  =  (rate of v1)*r2 + v1*(rate of r2)
                  =  r1*r2  +  v1*c2          [c2 is r2's own curve]

Add the two results together, since the new rate was their sum:

new curve  =  c1*v2  +  r1*r2  +  r1*r2  +  v1*c2
           =  c1*v2  +  2*r1*r2  +  v1*c2

No new rule was written. This is Unit 3's rule, used twice.
```


*The extended mix rule*

```
mix( (v1,r1,c1), (v2,r2,c2) )  outputs:

  value  =  v1*v2
  rate   =  r1*v2 + v1*r2
  curve  =  c1*v2 + 2*r1*r2 + v1*c2
```


*Demonstration 2: x = isolate(3,1,0), x*x*x*

```
x = (3, 1, 0)

Step 1: mix(x,x)
  value = 3*3 = 9
  rate  = (1*3)+(3*1) = 6
  curve = (0*3)+2*(1*1)+(3*0) = 2
  outputs (9, 6, 2)

Step 2: mix((9,6,2), (3,1,0))
  value = 9*3 = 27
  rate  = (6*3)+(9*1) = 27
  curve = (2*3)+2*(6*1)+(9*0) = 6+12 = 18
  outputs (27, 27, 18)

x*x*x at x=3 outputs value 27, rate 27, curve 18.
```


> **Does this match anything you'd recognize from a calculus course?** Value 27 is 3 cubed. Rate 27 is 3 times 3 squared, the same power-rule output Unit 4 already found. Curve 18 is 6 times 3, which a course would call the second derivative of x cubed. This book built it without ever writing "second derivative," by asking the same question (does this have a rate?) one layer deeper and reusing Unit 3's rule to answer it.


**Try It Yourself:** x = isolate(2,1,0). Run x*x*x and report all three slots. *Hint: Step 1 (x*x), fully, before Step 2.* Answer: Step 1: (4, 4, 2). Step 2: value=8, rate=(4*2)+(4*1)=12, curve=(2*2)+2*(4*1)+(4*0)=4+8=12. Outputs (8, 12, 12).


### Practice: Unit 8


1. x=isolate(4,1,0). Run x*x and report all three slots.

2. x=isolate(5,1,0). Run x*x*x and report all three slots.

3. Using Demonstration 2's result at x=3 (curve 18) and your answer to Problem 2 at x=5, predict the pattern connecting curve to 6*x. Check it against both.

4. Explain, in your own words, why the curve rule needed a factor of 2 on the middle term, r1*r2, but the rate rule didn't need one on its two strips.

---


*Unit 9*

## When Two Moving Things Meet


> **Big Question:** Given two moving things, each one an output of isolate, can you find out if and when they meet, using nothing but subtraction and division?

Car A starts at position 0, moving at rate 5. Car B starts at position 10, moving at rate -3, toward A. Subtract one reading from the other, piece by piece, exactly the way Unit 6 already subtracts.


*Demonstration 1: the gap between two cars*

```
A = isolate(0, 5)     outputs (0, 5)
B = isolate(10, -3)   outputs (10, -3)

gap = B - A = (10-0, -3-5) = (10, -8)

The gap's value, 10, is how far apart they start. The gap's rate,
-8, is this naming: B minus A, with B coming toward A. A minus B
flips the rate slot. The meeting does not flip.

Two cars driving apart are a different reading. One pays rope out,
one has the rope tied to the bumper. The rope gets longer. Nothing
left the first car and arrived in the second. Closing a gap uses
distance up. The rope is the relation of the two departures.
```

The gap is itself just another pair, an output of subtraction, nothing new. Ask a new question of it: divide its rate by its own value, instead of comparing it to something else.


*Demonstration 2: when do they meet?*

```
gap = (10, -8)

grow(gap) = gap's rate / gap's value = -8 / 10 = -4/5

grow(gap) = -4/5 means the gap loses 4/5 of its remaining value
per tick, if that rate holds. Time to zero is 1 / (4/5) = 5/4.

Check directly: gap's value + t * gap's rate = 0
                10 + t*(-8) = 0
                t = 10/8 = 5/4

They meet at t = 5/4.
```


> **Why divide the gap's rate by its own value, instead of comparing it to A or B?** Comparing the gap to A or B would answer "how fast is the gap closing compared to how fast A is moving," a question about two different things. Dividing the gap's rate by its own value answers "how fast is the gap closing compared to how much gap is left," which is exactly the question "when does the gap run out." Both are legitimate rate questions; they just aren't the same question.


**Try It Yourself:** A is isolate(0,2), B is isolate(20,-2). Find the gap and when they meet. *Hint: gap = B - A, then solve gap.value + t*gap.rate = 0.* Answer: gap = (20,-4). t = 20/4 = 5. They meet at t=5.


### Two Dimensions: Closest Approach

On a flat plane, track two coordinates for each mover. The same subtraction gives a gap in each direction, and the same kind of question, now asking when the *total* squared distance is smallest, tells you not just whether two things meet, but how close they come if they don't.


*Demonstration 3: a genuine meeting*

```
A starts at (0,0), moving (1,0). B starts at (10,0), moving (-1,0).

gap in x: (10, -2)     gap in y: (0, 0)

Time of closest approach (found by the same "rate over value" idea,
applied to the combined squared distance): t = 5

Position of the gap at t=5: (10 + 5*(-2), 0) = (0, 0)

Squared distance at closest approach: 0*0 + 0*0 = 0. They meet.
```


*Demonstration 4: a near miss*

```
A starts at (0,0), moving (1,0). B starts at (5,5), moving (-1,0).

gap in x: (5, -2)     gap in y: (5, 0)

Time of closest approach: t = 5/2

Position of the gap at t=5/2: (5 + 5/2*(-2), 5) = (0, 5)

Squared distance at closest approach: 0*0 + 5*5 = 25

They never meet. The closest they get is a distance whose square
is exactly 25, known in advance, with no measurement and no
trial and error.
```


*[Diagram: A moving right, B moving left on a higher line. The dashed segment is the closest the two paths ever come. (see the PDF for the image)]*


> **Why is knowing the squared distance enough, without taking a square root?** "Do they come within 5 units of each other" is answered exactly by comparing 25 to 5*5, both whole numbers, no irrational step required. The square root of 25 happens to be a whole number here, but Unit 11 shows that's the exception, not the rule. Staying with the squared distance keeps the whole question inside fractions, exactly, for free.


**Try It Yourself:** A starts at (0,0) moving (1,1). B starts at (10,5) moving (-1,-1). Do they meet? Find the gap in each direction first. *Hint: gap in x = (10,-2), gap in y = (5,-2). Find t where the total squared gap is smallest, the same way Demonstration 3 and 4 did.* Answer: time of closest approach works out to t=15/4 using the same method; the squared distance at that time is not 0 (check: gap-x and gap-y don't hit 0 at the same t), so they don't meet, but you can find exactly how close they get the same way Demonstration 4 did.


### Practice: Unit 9


1. A is isolate(0,3), B is isolate(30,-7). Find the gap and when they meet.

2. A is isolate(5,1), B is isolate(5,-1). What does the gap look like right away? What does that tell you about t=0?

3. A starts at (0,0) moving (2,0). B starts at (8,6) moving (-2,0). Find the gap in each direction, the time of closest approach, and the squared distance at that time.

4. Explain, in your own words, why "closest approach" is still a well-defined, computable question even when two things never actually meet.

---


*Unit 10*

## How Far The Machine Reaches


> **Big Question:** Which functions can the machine handle exactly, and where does it stop?

Addition and multiplication of Readings are settled: stipulated directly, as in Unit 3. That leaves division, and this time the rule does not need to be picked. It can be derived: division undoes multiplication, so whatever the quotient is, multiplying it by the divisor has to rebuild the dividend.


*Demonstration 1: what the quotient has to be*

```
Call the quotient (q, s). It has to satisfy:

  (v2, r2) * (q, s)  =  (v1, r1)

Apply the mix rule to the left side:

  (v2*q,  r2*q + v2*s)  =  (v1, r1)

Match the first slots:   v2*q = v1            so  q = v1 / v2
Match the second slots:  r2*q + v2*s = r1     so  s = (r1 - r2*q) / v2
                                                  = (r1*v2 - r2*v1) / v2²

This needs v2 to be something other than 0, for the same reason
ordinary division does.
```


> **Why is this rule derived, when the mix rule was stipulated?** Only the mix rule was picked, back in Unit 3. Everything here follows from requiring that division undo it. Once multiplication is fixed, "the quotient times the divisor gives back the dividend" leaves no freedom: the two slots of the quotient are forced by that one requirement, solved directly from the mix rule already in hand.


*Demonstration 2: 1/x at x = (3,1)*

```
Dividend (1,0), divisor (3,1).

q = 1/3
s = (0*3 - 1*1) / 3² = -1/9

Result: (1/3, -1/9).

Check by multiplying back: (3,1) * (1/3,-1/9)
  = (3*1/3,  1*1/3 + 3*(-1/9))  =  (1,  1/3 - 1/3)  =  (1, 0)
```


*Demonstration 3: (x*x + 1) / (x - 1) at x = (3,1)*

```
numerator:    x*x + 1  =  (9,6) + (1,0)  =  (10, 6)
denominator:  x - 1    =  (3,1) - (1,0)  =  (2, 1)

q = 10/2 = 5
s = (6*2 - 10*1) / 2² = 2/4 = 1/2

Result: (5, 1/2).
```

Combine `+`, `-`, `*`, `/` as many times as you like, starting from `x` and constants, and the machine reports an exact value and an exact rate, at every point where the divisor's value isn't 0.


*Demonstration 4: the edge, where the divisor's value is 0*

```
1/x at x = (0,1) means (1,0) divided by (0,1). q = 1/0. No answer.
The machine refuses: theta. Nothing can be adjusted to fix this,
because ordinary division by 0 has no answer either.
```

Outside that reach sit three kinds of question, each different, and the next three units take them one at a time. What number squares to 2 (Unit 11). What function's rate always equals its own value (Unit 12). What function's rate always equals a partner function's value, and vice versa (Unit 13). None of the three needs anything you don't already have.


**Try It Yourself:** Divide (6,4) by (2,0). *Hint: q = v1/v2, then s = (r1*v2 - r2*v1)/v2², with r2 = 0.* Answer: (3, 2). Check: (2,0)*(3,2) = (6, 0*3+2*2) = (6,4).


### Practice: Unit 10


1. Divide (10,5) by (5,0).

2. Find the Reading for `1/x` at `x=(2,1)`.

3. Find the Reading for `x/(x+1)` at `x=(1,1)`.

4. Find the Reading for `1/(x*x)` at `x=(2,1)`.

5. What does the machine do with `1/x` at `x=(0,1)`, and why?

6. For each, say whether the machine reaches it at x=(3,1): (a) x*x*x+2; (b) 1/(x-3); (c) (x+1)/(x-2).

---


*Unit 11*

## A Number That Isn't A Fraction


> **Big Question:** What do you do when the answer to a question is a number that is not a fraction?

A square with sides of length 1 has a diagonal `d` with `d * d = 2` (Geometry book, Unit 5). Is there a fraction whose square is 2?


*Demonstration 1: no fraction squares to 2*

```
Suppose a/b is a fraction in lowest terms with (a/b)² = 2.

1. Then a² = 2*b², so a² is even, so a is even (odd*odd is
   odd). Write a = 2c.
2. Then 4c² = 2*b², so b² = 2*c², so b is even too.

Now a and b are both even, so a/b was not in lowest terms.
Contradiction. No such fraction exists.
```

That proof is finite and it settles the question: no fraction, none at all, squares to exactly 2. It does not say the question has no answer. It says the answer isn't a fraction. Here are two rules that answer it, staying in fractions at every single step.


*Demonstration 2: closing in by halving*

```
Start knowing 1*1=1 is too small and 2*2=4 is too big. Check the
midpoint; if its square is too small, it becomes the new low end;
if too big, it becomes the new high end. Either way the gap halves.
Every number here is an exact fraction, nothing rounded.

step  low     high    gap    midpoint checked
0     1       2       1
1     1       3/2     1/2    3/2 squared = 9/4, too big, new high
2     5/4     3/2     1/4    5/4 squared = 25/16, too small, new low
3     11/8    3/2     1/8    11/8 squared = 121/64, too small, new low
4     11/8    23/16   1/16   23/16 squared = 529/256, too big, new high

Ask for any gap you want, however small, and this rule tells you
exactly how many steps close it, then runs that many steps.
Halving ten times takes the gap under 1/1000.
```


*Demonstration 3: a faster rule, closing in by averaging*

```
Start at x=1. Each step, replace x with the average of x and 2/x.
Still exact fractions, nothing rounded, at every step.

x0 = 1
x1 = (1 + 2/1) / 2             = 3/2
x2 = (3/2 + 2/(3/2)) / 2       = (3/2 + 4/3) / 2     = 17/12
x3 = (17/12 + 2/(17/12)) / 2   = (17/12 + 24/17) / 2 = 577/408
x4 = (577/408 + 2/(577/408)) / 2                     = 665857/470832

Square the last one directly: (665857/470832)^2 = 443365544449/221682772224
2, written over that same bottom, is 443365544448/221682772224

The two numerators differ by exactly 1. The gap between x4 squared
and 2 is 1/221682772224, a named fraction, after only four
steps. Halving needs about forty steps to close a gap that small.
```


> **Why does averaging close the gap so much faster?** Halving always cuts the gap in half, no matter how close you already are. Averaging's gap shrinks roughly by squaring each time: Demonstration 3's gaps were about 1/4, then 1/144, then 1/166464, each one roughly the square of the one before. Both rules stay in exact fractions and both come with a provable bound. They're different rules, is all, and this book keeps both because seeing two different rules reach the same kind of answer is part of the point: nothing about the square root of 2 is tied to one particular construction.

Either rule *is* the square root of 2, in every sense that matters for computing with it. Name a precision, a rule hands you a fraction within it, and a proof that says how good it is. Nothing about either rule ever finishes, and nothing about it needs to. You call it as many times as your problem needs and stop.


> **Isn't a rule less real than a number?** No more than `1/3` is less real than "1 divided by 3, in progress." `1/3` was already a rule: given how many digits you want, it produces them, forever, on demand, one at a time. The square root of 2 works the same way. It never gets a special status where it "finishes existing." It gets a rule, checked, and that's the whole of what it is here.


> **A choice, not a discovery** Nothing forces you to give this rule a name and a symbol, `√2`. Doing so is a choice, made because the rule comes up often enough to be worth a short label. The label doesn't add anything the rule didn't already have.


**Try It Yourself:** Run the halving rule one more step from step 4 above (low 11/8, high 23/16). Which end moves? *Hint: check the midpoint, 45/32, squared.* Answer: midpoint = (11/8+23/16)/2 = 45/32. Squared: 2025/1024. Compare to 2 = 2048/1024: 2025 is less, so 45/32 is too small, and it becomes the new low end. New range: low 45/32, high 23/16, gap 1/32.


### Practice: Unit 11


1. Show that the square of any odd number `2k+1` is odd.

2. In Demonstration 1, where does "in lowest terms" get used?

3. Continue the halving rule two more steps past your answer to Try It Yourself, keeping every number an exact fraction.

4. Roughly how many halving steps would it take to get the gap under 1/100,000? (You don't need the exact count, just show the gap roughly halves each step and estimate.)

5. Run Demonstration 3's averaging rule one more step, from x4=665857/470832. You don't need to simplify the result, just set up the fraction: `(x4 + 2/x4) / 2`.

6. Explain, in your own words, why calling either rule "√2" doesn't change what it is.

---


*Unit 12*

## A Number Defined By How It Changes


> **Big Question:** How would you build a function whose rate always equals its own value?

Money in an account that grows continuously grows faster the more there is. The cleanest version of that pattern: a quantity `E` that starts at 1 and whose rate always equals its own value.


> **A choice, not a discovery** `E(0) = 1` and `rate(E) = E` are a definition. No rectangle picture produces this function; it is picked because the pattern (grows faster the bigger it gets) is useful.


### Building It By Fixing Shortfalls

The machine can't hold `E` directly, so build polynomials that follow the law as closely as you like, and name exactly what's missing at each stage.

- Start with `P0 = 1`. Rate 0. The law wants 1. Shortfall: 1.
- Add a piece with rate 1: `x`. Now `P1 = 1 + x` has rate 1, but the law wants `1+x`. Shortfall: `x`.
- Add a piece with rate `x`: since `x*x` has rate `2x`, half of it does the job. `P2 = 1 + x + x*x/2`. Shortfall: `x*x/2`.


*Demonstration 1: P(n) at x = 1, and the exact shortfall*

```
n    value P(n)     rate of P(n)    shortfall (value minus rate)
0    1              0               1
1    2              1               1
2    5/2            2               1/2
3    8/3            5/2             1/6
4    65/24          8/3             1/24
5    163/60         65/24           1/120
6    1957/720       163/60          1/720

Each rate equals the previous value. The shortfall is exactly
1/n! every time, provably: the next piece added is x^n/n!, and
that's exactly the shortfall this row is carrying.
```


> **Why can no single polynomial satisfy the law exactly?** The rate of a polynomial of degree n has degree n-1, one lower. A polynomial and its own rate can never be equal unless both are 0, and `E(0)=1` rules that out. So no single, finite polynomial is `E`. `E` is the rule: for any n you name, run this construction n steps, and the shortfall left behind is exactly `1/n!`, a fact proven above, not estimated.


### Precision On Demand


*Demonstration 2: naming a precision, getting a proof*

```
Ask: give me E(1) within 1/1000.

For n=6, the next term is 1/7!. Every term after that is at most
1/8 of the one before it (the denominator grows by at least 8 each
step), so the whole remaining tail is at most a shrinking-by-8
series:

  1/7! * (1 + 1/8 + 1/8^2 + ...) = 1/7! * (8/7) = 8/35280 = 1/4410

That's a closed-form fraction, not an estimate. Compare it to
1/1000 directly: 1/4410 < 1/1000 exactly when 1000 < 4410, true.

So P(6), value 1957/720, answers the request: E(1) is within
1/1000 of 1957/720, proven by a finite calculation entirely in
fractions, no further steps needed.
```

Nothing above required infinitely many steps to run. Every check was a finite sum, or a finite comparison. The rule `E` is fully specified by "compute P(n) for any n I ask, and the shortfall is exactly 1/n!." That sentence is the whole content of what `E` is. `E(1)`, the number people write as `e`, is the name for that rule at `x=1`, nothing more added.


**Try It Yourself:** Find the value, rate, and shortfall of `P3 = 1 + x + x*x/2 + x*x*x/6` at `x = 2`. *Hint: the four pieces at x=2 are 1, 2, 2, 4/3. The rate is P2 at 2.* Answer: value = 1+2+2+4/3 = 19/3. Rate = 1+2+2 = 5. Shortfall = 19/3 - 5 = 4/3, which is 2³/3!.


### Practice: Unit 12


1. Find the value, rate, and shortfall of `P4` at `x = 1/2`.

2. Check at `x = 2` that the rate of `P2` equals the value of `P1`.

3. Explain in your own words why the degree of a polynomial's rate stops it from ever satisfying `rate(E)=E`.

4. What is the shortfall of `P7` at `x = 1`?

5. What does the law say the rate of `E` is at `x = 0`?

---


*Unit 13*

## Two Rates That Feed Each Other


> **Big Question:** What if the rate of one quantity is the value of another, and vice versa?


> **A choice, not a discovery** `S(0)=0`, `C(0)=1`, `rate(S)=C`, `rate(C)=-S`. Four lines, picked as a definition. Whether the functions they define match the sine and cosine measured from triangles is a separate claim, checked against measurement, not proven here.


### Building Them By Matching Rates

Same method as Unit 12. The rate of `x` is 1. The rate of `x*x*x/6` is `x*x/2`. Build two series, term by term, so each one's rate lands on the other's value at the previous stage.


*Demonstration 1: truncated S and C at x = 1*

```
S3 = x - x^3/6                    at 1:  value 5/6,      rate 1/2
C2 = 1 - x^2/2                    at 1:  value 1/2,      rate -1
rate of S3 = 1/2, which is the value of C2.

S5 = x - x^3/6 + x^5/120          at 1:  value 101/120,  rate 13/24
C4 = 1 - x^2/2 + x^4/24           at 1:  value 13/24,    rate -5/6
rate of S5 = 13/24, the value of C4.
rate of C4 = -5/6, which is minus the value of S3.
```

Each one is a finite polynomial. Ask for more accuracy, add more terms; the next term is a specific, computable fraction, exactly like Unit 12's shortfall. Nothing here waits on an infinite process to finish. `S` and `C` are the rule "build the next term this way," the same way `E` was a rule in Unit 12.


### What The Rate Laws Alone Can Show

At any point, if `S` has value `s` and `C` has value `c`, then `S` reads `(s, c)` and `C` reads `(c, -s)`, straight from the definition.


*Demonstration 2: the rate of S*S + C*C*

```
Suppose S reads (3/5, 4/5) and C reads (4/5, -3/5).

S*S = (9/25,   24/25)
C*C = (16/25, -24/25)
S*S + C*C = (1, 0)

Do it with letters instead of numbers: S reads (s,c), C reads
(c,-s).
S*S = (s^2,  2sc)
C*C = (c^2, -2sc)
S*S + C*C = (s^2+c^2, 0)

The rate is exactly 0, for every s and c, not just this pair. Pure
algebra: two terms that are exact negatives of each other, added.
```


> **Does rate 0 mean S*S + C*C stays 1 forever?** That would need a separate argument connecting "rate 0 at a point" to "same value at another point," and this book doesn't build that argument, because it isn't needed for anything else here. What Demonstration 2 shows is smaller and fully finite: at whatever point you check, `S*S+C*C` has rate exactly 0. That's a fact about the rate, proven by algebra, not a claim about every point at once. Unit 14 builds a second, completely different construction where a version of this identity holds exactly, everywhere, for a different reason.


**Try It Yourself:** Find S3 and C2 at `x = 2`. Does the rate of S3 equal the value of C2? Answer: S3 at 2 is 2 - 8/6 = 2/3, rate -1. C2 at 2 is 1 - 2 = -1. Yes, both -1.


### Practice: Unit 13


1. Check that C2's rate at x=1 equals minus the value of S1=x at x=1.

2. Let S read (3/5,4/5) and C read (4/5,-3/5). Find the Reading for S*C.

3. Let S read (5/13,12/13) and C read (12/13,-5/13). Find the Reading for S*S+C*C.

4. Redo Demonstration 2 with letters s, c, but for S*C instead of S*S+C*C. What's its rate, in terms of s and c?

5. Why is "S3 approximates the true sine function" a different kind of sentence than "S3's rate at 1 is exactly 1/2"?

---


*Unit 14*

## A Second Way To Turn, Exactly


> **Big Question:** Unit 13 built two rates that feed each other and showed S*S+C*C has rate 0, without ever proving the value itself stays exactly 1. Is there a construction where it does, provably, with no series at all?

Yes, and it's built from nothing but a pair of whole numbers. This is not Unit 13's S and C under a different name. It's a different construction entirely, picked for a different reason, and this unit is careful to keep the two apart.


### A Pair Of Whole Numbers, Turned Into A Pair That Squares To 1

Take two whole numbers, written `(P : Q)`, called a **heading**. Build two fractions from them:


*The heading rule*

```
heading(P, Q)  outputs  (c, s)  where

  c  =  (Q*Q - P*P) / (P*P + Q*Q)
  s  =  2*P*Q / (P*P + Q*Q)
```


*Demonstration 1: heading(1, 2)*

```
P=1, Q=2.  P*P+Q*Q = 1+4 = 5

c = (4-1)/5 = 3/5
s = 2*1*2/5 = 4/5

heading(1,2) outputs (3/5, 4/5)

Check: c*c + s*s = 9/25 + 16/25 = 25/25 = 1

Exactly 1. Not approximately. The 3-4-5 triangle is sitting
inside this computation: 3, 4, and 5 are exactly the numbers that
came out.
```


*Demonstration 2: two more headings, same check*

```
heading(1,3): c=4/5, s=3/5.  c*c+s*s = 16/25+9/25 = 1
heading(2,3): c=5/13, s=12/13.  c*c+s*s = 25/169+144/169 = 1

Every whole-number pair (P,Q) produces a (c,s) with c*c+s*s
exactly 1, checked here on three pairs, provably true for every
pair by the same algebra each time: expand (Q*Q-P*P)^2 and
(2*P*Q)^2, add them, and the sum is always (P*P+Q*Q)^2 exactly,
which divided by (P*P+Q*Q)^2 is 1.
```


> **Why does this hold exactly, with no series and no limit?** Unit 13's S and C are built by adding up infinitely many shrinking pieces, and only a finite number of them are ever actually added, so S*S+C*C landing on exactly 1 would need infinitely many pieces to finish, which never happens. A heading never adds up pieces at all. It's two fractions built directly from P and Q by one formula, and checking c*c+s*s=1 is a single finite algebra fact, true the same way for every pair, not approached.


### Combining Two Headings

Two headings combine by a rule that mixes P's and Q's the way Unit 3 mixes values and rates:


*Demonstration 3: combining heading(1,2) and heading(1,1)*

```
Combine rule:  P' = P1*Q2 + P2*Q1,   Q' = Q1*Q2 - P1*P2

(1,2) combined with (1,1):
  P' = 1*1 + 1*2 = 3
  Q' = 2*1 - 1*1 = 1

Combined heading: (3, 1). heading(3,1) outputs:
  c = (1-9)/10 = -4/5,  s = 2*3*1/10 = 3/5

Compare to combining the two (c,s) pairs directly:
  heading(1,2) = (3/5, 4/5).  heading(1,1) = (0, 1).
  c1*c2 - s1*s2 = 3/5*0 - 4/5*1 = -4/5
  s1*c2 + c1*s2 = 4/5*0 + 3/5*1 = 3/5

Both routes output the same pair, (-4/5, 3/5).
```


### A Turn Rate, Built The Same Way As Unit 3's Rate

Seed P the way Unit 1 seeds a value, with its own rate attached, and ask how fast the heading turns.


*Demonstration 4: turn rate, and it adds under combining*

```
turn rate of (P,Q), P moving at rate 1, Q fixed:
  turn = 2*(Q*1 - P*0) / (P*P+Q*Q) = 2*Q / (P*P+Q*Q)

heading(1,2): turn = 2*2/5 = 4/5
heading(1,1): turn = 2*1/2 = 1

Combine the two headings (Demonstration 3 gave (3,1)). Under the
same seeding, the combined turn rate works out to 4/5 + 1 = 9/5,
checked directly from the combined (P,Q)=(3,1) and its own rates,
not assumed.
```


> **Is this the same thing as sine and cosine?** No, and saying so plainly matters more here than almost anywhere else in this book. Unit 13's S and C are built from an infinite series and connect, through calculus most books don't build from scratch, to an actual angle measured in degrees or radians. A heading is built from a pair of whole numbers and never mentions an angle at all. Both produce a pair with c*c+s*s=1. Both compose by matching algebra. That's a shared pattern, not a shared identity, and this book has been careful all the way through not to confuse the two. A heading cannot currently answer "what is the cosine of 30 degrees," because connecting P and Q to a specific angle is a question this construction was never built to answer.


> **A choice, not a discovery** The formula for heading(P,Q) is one specific way to turn a whole-number pair into a pair that squares to 1. It was picked because it matches how a 3-4-5 triangle and its relatives are already built from whole numbers, not because it's the only possible choice.


**Try It Yourself:** Find heading(2,1) and check c*c+s*s. *Hint: P=2, Q=1, so P*P+Q*Q=5.* Answer: c=(1-4)/5=-3/5, s=2*2*1/5=4/5. Check: 9/25+16/25=1.


### Practice: Unit 14


1. Find heading(3,4) and check c*c+s*s.

2. Find heading(1,4) and check c*c+s*s.

3. Combine heading(1,2) with heading(2,1) using the P',Q' rule. Find the resulting (c,s) both ways, directly from the combined (P,Q) and by combining the two (c,s) pairs with the c1c2-s1s2 formula, and check they match.

4. Find the turn rate of heading(1,4) with P moving at rate 1.

5. Explain, in your own words, why "both satisfy c*c+s*s=1" is not a strong enough reason to call a heading and Unit 13's (S,C) the same construction.

---


*Unit 15*

## Precision On Demand


> **Big Question:** Units 11 to 13 kept saying "ask for a precision, the rule hands you a fraction within it." What exactly is that move, in general?

Here it is, stripped down. A **rule**, in this sense, is a finite procedure: you give it a positive fraction (how close you need to be), it gives back a whole number (how many steps to run), and running that many steps produces a fraction, with a proof that the fraction is that close. Every step of every part of that is finite. You never run the procedure forever. You run it once, for the precision you actually asked for, and it stops.


*Demonstration 1: the rule for 1/n, made explicit*

```
Request: get 1/n within 1/500 of 0.

Solve 1/n < 1/500 directly: n > 500. So n = 501 works.
Check directly, no decimal needed: 1/501 < 1/500 exactly when
500 < 501, true.

One division settled it. No infinite process ran.
```


*Demonstration 2: the rule for the sums of halves*

```
1, 3/2, 7/4, 15/8, ...   each term is the last plus the next half.

The gap between the n-th term and 2 is exactly 1/2^n, a fact you
can check by induction: gap(0) = 2-1 = 1 = 1/2^0, and each step
covers exactly half of what's left. Request gap under 1/100:
2^n > 100 first happens at n=7 (2^7=128). Run 7 steps, done.
```


*Demonstration 3: the rule for a hole in a fraction*

```
f(x) = (x*x-1)/(x-1) refuses at x=1 (0/0). But away from 1,
algebra simplifies it: x*x-1 = (x-1)*(x+1), so f(x) = x+1 for
every x other than 1.

Feed the rule x = 1 + 1/n:
f(1+1/n) = (1+1/n) + 1 = 2 + 1/n

Request f within 1/50 of 2: need 1/n < 1/50, so n=51 works.
This is algebra, not a limiting process: f genuinely equals x+1
at every point besides x=1, checked directly.
```


> **Where mathematicians usually say "limit," what's actually there?** A rule, exactly like the three above: give it a tolerance, it gives back a stage, checked by a finite calculation. Historically that whole package got a name, "limit," and got talked about as if something was being approached, a target sitting out there waiting. Nothing needs to sit anywhere. The rule is complete in itself: callable, finite per call, and proven correct per call. That's the entire mathematical content. This book will keep saying "rule, requested precision, proven bound" instead of "approaches," because that phrasing doesn't invite the question "approaches what completed thing?" when there's no completed thing in the account at all.


**Try It Yourself:** For the rule `3/n`, find a stage that gets it within 1/100 of 0. *Hint: solve 3/n < 1/100 directly.* Answer: n > 300, so n=301 works. Check directly, no decimal needed: 3/301 < 1/100 exactly when 3*100 < 301*1, and 300 < 301 is true.


### Practice: Unit 15


1. For `5/n`, find a stage within 1/1000 of 0.

2. For the sums of halves, find the first stage with gap under 1/1000.

3. For `f(x)=(x*x-1)/(x-1)` at `x=1+1/n`, find a stage within 1/20 of 2.

4. Unit 11's halving rule for the square root of 2: after 10 steps the gap is 1/1024. How many more steps, roughly, to get the gap under 1/100,000?

5. Explain, in your own words, why a rule that runs finitely for every request you actually make doesn't need to run forever to be complete.

---


*Unit 16*

## "Algebraic" And "Transcendental" Are Rule Labels


> **Big Question:** The square root of 2 gets called "algebraic." The number e gets called "transcendental." What does that difference actually say?

A number is called **algebraic** if it is a root of some polynomial with whole-number coefficients: something like `x*x - 2` (root: the square root of 2) or `2x + 1` (root: -1/2). A number is called **transcendental** if it is not a root of any such polynomial. Every fraction is algebraic. The square root of 2 is algebraic. It is a theorem that `e` is not the root of any whole-number polynomial. That proof is longer than this book has room for; it is stated here, not derived.


> **What does "algebraic" or "transcendental" actually tell you about a number?** Which rule reaches it, and nothing else. "Algebraic" means: reachable by the rule "find a root of a whole-number polynomial." "Transcendental" means: not reachable by that particular rule. It does not mean harder to compute, less precise, less real, or further away. Unit 11 reached the square root of 2 with a halving rule and an averaging rule. Unit 12 reached e with a shortfall rule. All of these rules are finite per step. All come with a proven precision bound on request. No number here is more "arrived at" than another. The words "algebraic" and "transcendental" sort numbers by which generating rule was used to name the sorting question, the way "even" and "odd" sort whole numbers by which rule (divide by 2 cleanly, or not) answers a specific question. Nobody thinks odd numbers are less real than even ones.


*Demonstration 1: the square root of 2 is a root, directly*

```
The halving rule from Unit 11 never mentions a polynomial. But its
target satisfies x*x = 2, which rearranges to x*x - 2 = 0: exactly
the polynomial x*x-2, evaluated at that x, hits 0. That's what
makes the square root of 2 algebraic: a short polynomial names it.
```


*Demonstration 2: not every number gets named this way*

```
Try the same move on e. Is there a whole-number polynomial
a_n*x^n + ... + a_1*x + a_0 with e as a root? The theorem says
no, for any such polynomial, however long. e still has a rule (Unit
12's shortfall construction). It just isn't the root-of-a-polynomial
rule. That's the entire difference.
```


> **Is this a fact about what numbers ultimately are?** No. "Transcendental" sounds like it's announcing something deep about a number's nature, sitting beyond ordinary numbers in some special realm. It isn't. It's a checkable fact about one specific, narrow question: does a whole-number polynomial hit this number exactly? For e, the answer is no, proven. That's the whole claim. Treating "transcendental" as a kind of thing a number IS, rather than a fact about which rule reaches it, turns a checkable classification into an unchecked story about hidden depths. This book keeps the checkable version only.


**Try It Yourself:** Which polynomial, with whole-number coefficients, has 3/4 as a root? *Hint: start from 4x = 3.* Answer: `4x - 3`. Check: `4*(3/4) - 3 = 0`.


### Practice: Unit 16


1. Find a whole-number polynomial with -2/5 as a root.

2. Find a whole-number polynomial with the square root of 3 as a root.

3. Every fraction p/q is algebraic. Give the general polynomial that proves it.

4. Sine and cosine, built in Unit 13 the same way e was built in Unit 12, are also transcendental (a theorem, not proven here). Does that change anything about how you compute S3 or C2 at a point?

5. Explain, in your own words, the difference between "e is transcendental" and "e is less real than the square root of 2."

---


*Unit 17*

## What This Machine Never Needed


> **Big Question:** Look back across Units 1 to 16. What was actually required to reach every number and every construction in this book?

Fractions, and the three moves from Unit 1 through 3. That's the full list. Here is everything this book built, and what it took.


*Demonstration 1: every construction in this book, and its rule*

```
number/function                             rule                                            per-step arithmetic
------------------------------------------- ----------------------------------------------- ------------------
rate of x*x*x+2x+1                          mix and add on Readings (Unit 7)                fractions, finite
rate of the rate of x^3                     the same mix rule, one layer deeper (Unit 8)    fractions, finite
when two movers meet                        subtract, then divide rate by value (Unit 9)    fractions, finite
1/x, (x+1)/(x-2)                            derived quotient (Unit 10)                      fractions, finite
sqrt(2)                                     halving, or averaging (Unit 11)                 fractions, finite
e = E(1)                                    shortfall construction (Unit 12)                fractions, finite
sin(1), cos(1)                              coupled shortfall construction (Unit 13)        fractions, finite
an exact turn, c*c+s*s=1                    whole-number pair (Unit 14)                     fractions, finite
"a rule gets within any distance you name"  naming a stage for a named tolerance (Unit 15)  fractions, finite

Every row: fractions in, fractions out, a finite number of
arithmetic steps, and (where relevant) a finite proof of how
close the answer is. Nothing on this list required a number that
isn't a fraction to exist ahead of time. Nothing required treating
"all the numbers there could ever be" as a single object to reason
about. Every claim was: run this many steps, get this fraction,
here is the proof it's close enough.
```


> **So what was the limit for, in other treatments of this material?** In most courses, "the real numbers" get declared first, as a completed collection that already contains every possible decimal, and then a limit is defined as a way of picking out one member of that collection using a sequence. That's a choice some mathematicians made, for their own reasons: it lets certain existence theorems get stated cleanly, at the cost of talking about a completed infinite collection before doing any arithmetic with it. This book made a different choice: build the rule first, prove its precision bound, and never declare a completed collection that the rule is reaching into. Every number this book named came with its rule attached, in full, with nothing left over that the rule doesn't already supply.


> **A choice, not a discovery** Declaring a completed set called "the real numbers" is a choice other treatments make. This book doesn't make it, because nothing in this book needed it. That doesn't mean the choice is wrong for other purposes; existence theorems and some parts of later mathematics do lean on it. It means the choice was never a prerequisite for anything built here.


**Try It Yourself:** Which unit in this book used a number that wasn't a fraction, at any single step of any calculation? Answer: none. Every intermediate value in every demonstration in Units 1 through 16 was a fraction. The rules reach past what fractions can exactly represent (sqrt(2), e, sine, cosine) without any step along the way leaving fractions.


### Practice: Unit 17


1. For each, name the unit and the rule that reaches it: (a) the rate of x*x*x at x=5; (b) the square root of 2 within 1/500; (c) e within 1/100; (d) an exact turn with c*c+s*s=1.

2. A friend says "e isn't really a number until you take the limit." Using this unit, write two sentences responding to that.

3. Why does building the rule first, instead of declaring a completed set of numbers first, avoid ever having to say "all the real numbers" as a single object?

---


*Unit 18*

## What This Book Claims, And What It Doesn't


> **Big Question:** What kinds of statements has this book been making, and which kinds can no calculation support?

Statements come in three kinds.

- **Kind 1: checked by calculation or proof.** "At x=3 the rate of x*x is 6." "No fraction squares to 2." "e is transcendental." "heading(1,2) satisfies c*c+s*s=1." Anyone can check these, by running the rule or the argument.
- **Kind 2: claims about the world, through a model.** "A dropped ball falls about 4.9*t*t meters in t seconds, ignoring air." Checked by measurement, and can be wrong.
- **Kind 3: claims about what everything ultimately is.** "Numbers exist whether or not anyone thinks about them." "Transcendental numbers belong to a deeper layer of reality than algebraic ones." "A heading is secretly the real meaning of sine and cosine." No calculation and no measurement can test these.

This book makes claims of kinds 1 and 2 only.


> **Where a kind 3 claim likes to hide inside this material** "Transcendental" is a real, checkable, kind 1 fact about a number: which rule reaches it (Unit 16). The word invites a kind 3 reading anyway, because it sounds like it's describing a deeper category of existence rather than a narrow fact about polynomials. It isn't. Reading it as ontology is exactly the mistake this unit exists to name: a kind 1 fact, dressed in language that suggests a kind 3 claim, smuggled past the reader because the two sentences sound similar. "Not the root of a whole-number polynomial" is checkable. "Belongs to a higher order of number" is not, and this book never says it, whatever "transcendental" sounds like it's implying.


> **Where a kind 3 claim likes to hide inside "the same," too** Unit 14 built headings specifically to avoid a different version of this mistake: two constructions that satisfy the same algebraic identity, c*c+s*s=1, are not thereby the same construction. "They satisfy the same equation" is a kind 1 fact, checkable. "They are the same thing" is a much larger claim that the shared equation alone does not support, and this book never makes it. The same caution applies to "the real numbers" (Unit 17): some treatments present them as a completed totality that existed before anyone started computing. Read as a claim about what fundamentally exists, that is also a kind 3 claim, and this book doesn't make it.


### No Method Is Free Of Assumptions

Every calculation in this book rests on assumptions: that whole-number and fraction arithmetic is consistent, and that checking a finite proof by hand is reliable. No check can show that a method has no assumptions at all, so a book claiming none would be claiming more than it can support. What a book can do is state its assumptions where they appear, which is what the purple boxes were for throughout.


**Try It Yourself:** Which kind is this statement: "e is not the root of any whole-number polynomial"? Answer: kind 1. It is a theorem, a checkable argument, even though this book didn't reproduce it in full.


### Practice: Unit 18

For each statement, say which kind it is, and say what would count as checking it (or say that nothing could).


1. At x=4, the rate of x*x is 8.

2. There is no fraction whose square is 2.

3. A dropped ball falls about 4.9*t*t meters in t seconds, ignoring air.

4. Transcendental numbers are more real than algebraic numbers.

5. e is transcendental.

6. The real numbers exist as a completed totality, prior to any rule that reaches into them.

7. Given a requested precision, the halving rule for the square root of 2 reaches it within that many steps.

8. A heading is what sine and cosine really are, underneath the series.

---


*Closing*

## What You Can Say Now

For every function built from a starting Reading with adding, subtracting, multiplying, and dividing, the machine gives an exact value and an exact rate by finite arithmetic, at every point where no division by a zero value occurs. The mix rule is the whole output, two strips added to a starting area, nothing approximated and nothing set aside. The same rule, applied one layer deeper with no new axiom, gives a rate that has its own rate. The same subtraction already in the book, paired with a single division, tells you exactly when and where two moving things meet, or exactly how close they come if they don't.

When a question's answer isn't a fraction, the answer is a rule: a finite procedure that, given any precision you name, hands back a fraction and a proof of how close it is. The square root of 2, e, sine, and cosine were each built this way, by different but structurally similar constructions, none of them needing anything beyond fraction arithmetic at every single step. A heading, built from nothing but a pair of whole numbers, gives a fifth construction that needs no series at all, and satisfies its own version of the same circular identity exactly, for a completely different reason, never claimed to be the same thing as the series it resembles. "Algebraic" and "transcendental" name which construction reaches a number, not what kind of thing it is. Nothing in this book declared a completed totality of numbers, because nothing in this book needed one, and nothing in this book treated a number as existing ahead of the steps that produced it.

The book claimed nothing about what numbers ultimately are. It said what its three moves produce, where each choice was made, and what each choice buys.


### What This Book Does Not Cover

Integrals, the way a rate turns back into a quantity. The proofs that a rate law has a solution and only one, used in Units 12 and 13 without being proven unique. The proof that S and C from Unit 13 match the sine and cosine measured on triangles. Connecting a heading's (P:Q) to an actual angle in degrees or radians. What happens with more than two dimensions. A longer companion, *How To Build A Novel Calculi*, treats the machine itself, and how to build a different one on a different alphabet.


---


*Answer Key*

## Check Your Work


### Unit 1


**1.** isolate(40,3) outputs (40,3).

**2.** isolate(15,0) outputs (15,0).

**3.** isolate(20,4) outputs (20,4): 20 is the value now, 4 is how fast it's changing.

**4.** isolate(500,-10) outputs (500,-10).

**5.** isolate(7) is short for isolate(7,1), and outputs (7,1). It assumes rate 1.

### Unit 2


**1.** rate(P,Q) outputs 8/4=2.

**2.** rate(M,N) outputs 9/3=3.

**3.** A is changing three times as fast as B.

**4.** rate(x,x) outputs 1. The rate slot is 6, so the comparison lands, and a reading compared to itself is changing exactly as fast as itself.

**5.** rate(G,H) outputs 12/4=3.

**6.** Because "how fast" is a question about speed, not where each Reading started; only the rate slot answers that.

### Unit 3


**1.** x=7: strips 7 and 7, sum 14. mix(x,x) outputs (49,14). rate outputs 14.

**2.** x=8: strips 8,8, sum 16. Outputs (64,16). rate outputs 16.

**3.** x=9: strips 9,9, sum 18. Outputs (81,18). rate outputs 18.

**4.** x=5: strips 5,5, sum 10. Outputs (25,10). rate outputs 10.

**5.** Prediction: 2*12=24. Check: strips 12,12, sum 24. Outputs (144,24). rate outputs 24.

**6.** Shortcut outputs 1*1=1. Real output is 6. Different: the shortcut throws away information the two strips keep.

### Unit 4


**1.** x=5: Step1 outputs (25,10). Step2: value=125, rate=(10*5)+(25*1)=75. Outputs (125,75).

**2.** x=6: Step1 outputs (36,12). Step2: value=216, rate=(12*6)+(36*1)=108. Outputs (216,108).

**3.** Prediction 3*10*10=300. Step1 outputs (100,20). Step2: value=1000, rate=300. Matches.

**4.** Prediction: 5*3^4=405. Running four mixes from x=isolate(3) confirms rate(x^5,x)=405.

### Unit 5


**1.** x=isolate(3,2): x*x outputs (9,12). rate outputs 12/2=6. Matches Unit 3's seed-1 output.

**2.** x=isolate(7,4): x*x outputs (49,56). rate outputs 56/4=14. Matches Unit 3 Practice Problem 1.

**3.** x=isolate(6,-1): x*x outputs (36,-12). rate outputs -12/-1=12. Matches the seed-1 output of 12 for x=isolate(6).

**4.** Whatever seed you pick multiplies into both top and bottom of the rate division, in matching amounts, so it cancels out.

### Unit 6


**1.** t=1: u outputs (2,2). y outputs (4,8). rate(y,t) outputs 8. rate(y,u)*rate(u,t)=(8/2)*(2/1)=8. Matches.

**2.** t=3: u outputs (6,2). y outputs (36,24). rate(y,t) outputs 24. (24/2)*(2/1)=24. Matches.

**3.** t=4: u outputs (8,2). y outputs (64,32). rate(y,t) outputs 32. (32/2)*(2/1)=32. Matches.

**4.** rate(J,K) is 5/0, theta. K isn't changing, so there's nothing to compare J's rate against, the same way there's no "how many times more" when the amount you're comparing to is zero.

**5.** u already carries everything about t that Room 2 needs; Room 2 never has to reach back and ask t anything directly.

**6.** "Huge number" still treats the question as having a well-shaped answer that's just large. It doesn't. K's rate isn't "basically nothing," it's exactly 0, and a ratio to exactly 0 isn't a big number, it's not a number at all.

### Unit 7


**1.** x*x=(16,8). Add x=(4,1): (20,9).

**2.** x*x=(1,2). x*x*x = (1,2)*(1,1) = (1,3).

**3.** x*x=(25,10). Subtract x=(5,1): (20,9). Plain check: 5*5-5=20, matches.

**4.** The mix rule takes any two Readings and returns a Reading, so its output can always be fed back in as an input to the same rule.

**5.** x*x*x=(27,27). Subtract x=(3,1): (24,26).

### Unit 8


**1.** x=isolate(4,1,0): x*x outputs (16,8,2).

**2.** x=isolate(5,1,0): x*x*x outputs (125,75,30).

**3.** Pattern: curve = 6*x. At x=3, 6*3=18, matches Demonstration 2. At x=5, 6*5=30, matches Problem 2.

**4.** The curve's middle term, r1*r2, comes from two different paths (rate of the first strip, and rate of the second strip) that both produce the same product r1*r2, so they add together. The rate rule's two strips, r1*v2 and v1*r2, are different products from the start, so there's nothing to double.

### Unit 9


**1.** gap = (30,-10). Meet when 30+t*(-10)=0, so t=3.

**2.** gap = (0,-2). The gap's value is already 0 at the start: they begin at the same position.

**3.** gap-x=(8,-4), gap-y=(6,0). Time of closest approach: t=2. Squared distance at that time: 36.

**4.** The same subtract-then-divide method finds the exact time the combined squared distance is smallest, whether or not that smallest value happens to be 0; "closest" is a well-defined minimum either way, not something that only makes sense for an actual meeting.

### Unit 10


**1.** q=2, s=(5*5-0*10)/25=1. Result: (2,1).

**2.** q=1/2, s=(0*2-1*1)/4=-1/4. Reading (1/2,-1/4).

**3.** numerator (1,1), denominator (2,1). q=1/2, s=(1*2-1*1)/4=1/4. Reading (1/2,1/4).

**4.** x*x=(4,4). q=1/4, s=(0*4-1*4)/16=-1/4. Reading (1/4,-1/4).

**5.** The divisor's value is 0, so the machine refuses: theta, the same reason ordinary division by 0 has no answer.

**6.** (a) yes, built from + and *. (b) no, divisor's value is 0 at x=3. (c) yes: numerator (4,1), divisor (1,1), q=4, s=(1*1-1*4)/1=-3, Reading (4,-3).

### Unit 11


**1.** (2k+1)² = 4k²+4k+1 = 2(2k²+2k)+1, one more than even, so odd.

**2.** It supplies the contradiction: the argument shows a and b are both even, but lowest terms means they share no factor of 2.

**3.** Step 6: midpoint of 45/32 and 23/16 is 91/64. Squared: 8281/4096, versus 2=8192/4096, too big, new high. Range (45/32, 91/64), gap 1/64. Step 7: midpoint of 45/32 and 91/64 is 181/128. Squared: 32761/16384, versus 2=32768/16384, too small, new low. Range (181/128, 91/64), gap 1/128.

**4.** The gap halves each step, starting at 1. After k steps the gap is 1/2^k. Need 1/2^k under 1/100,000: 2^17=131,072 clears it, so about 17 steps.

**5.** (665857/470832 + 2/(665857/470832)) / 2. No need to simplify the fraction inside.

**6.** The label is just a short name for the rule. Calling it √2 doesn't add any information either rule didn't already contain; you could run the whole book without ever writing the symbol.

### Unit 12


**1.** Value: 1+1/2+1/8+1/48+1/384=211/128. Rate: P3 at 1/2=1+1/2+1/8+1/48=79/48. Shortfall: 1/384.

**2.** P2 at 2 has rate 1+2=3. P1 at 2 is 1+2=3. Equal.

**3.** A degree-n polynomial's rate has degree n-1, one lower, so a polynomial can never equal its own rate unless both are 0. E(0)=1 rules that out, so only the ongoing construction, not any single polynomial, satisfies the law.

**4.** 1/7! = 1/5040.

**5.** The law says rate(E)=E, and E(0)=1, so the rate at 0 is 1.

### Unit 13


**1.** C2's rate at 1 is -x=-1. S1=x at 1 is 1, minus that is -1. Match.

**2.** S*C = (12/25, 7/25).

**3.** S*S+C*C = (1, 0).

**4.** S*C reads (sc, c*c-s*s). The rate is c²-s².

**5.** "Approximates" compares S3 to something else assumed to exist separately. "S3's rate at 1 is exactly 1/2" is a fact about S3 alone, checked by arithmetic, with nothing else assumed.

### Unit 14


**1.** heading(3,4): c=(16-9)/25=7/25, s=2*3*4/25=24/25. Check: 49/625+576/625=625/625=1.

**2.** heading(1,4): c=(16-1)/17=15/17, s=2*1*4/17=8/17. Check: 225/289+64/289=1.

**3.** Combined P,Q = (1*1+2*2, 2*1-1*2) = (5,0). heading(5,0)=(-1,0). Direct combine: c1c2-s1s2 and s1c2+c1s2 using heading(1,2)=(3/5,4/5) and heading(2,1)=(-3/5,4/5) both give (-1,0). Match.

**4.** turn = 2*4/17 = 8/17.

**5.** Satisfying the same equation only shows both pairs sit somewhere on the same algebraic curve; it says nothing about how each pair was built, and a heading (whole-number pair, no series, no angle) and Unit 13's (S,C) (infinite series, connects to measured angles) are built by genuinely different processes.

### Unit 15


**1.** 5/n < 1/1000 needs n > 5000, so n=5001 works.

**2.** 2^n > 1000 first happens at n=10 (2^10=1024), so stage 10.

**3.** 1/n < 1/20 needs n > 20, so n=21 works.

**4.** From 2^10=1024, need 2^n > 100,000; 2^17=131,072 is the first past it, so about 7 more steps.

**5.** Every actual request names one specific precision, and the rule only ever has to answer that one request in finitely many steps; there's no request that would force it to run forever.

### Unit 16


**1.** 5x + 2, since 5*(-2/5)+2=0.

**2.** x*x - 3.

**3.** qx - p, since q*(p/q) - p = 0.

**4.** No. Computing S3 or C2 at any point is exactly the same finite arithmetic either way; being transcendental doesn't change a single step of it.

**5.** "Transcendental" is a checked, narrow fact: e isn't a root of any whole-number polynomial. "Less real" claims something about existence that no calculation tests; it isn't something the transcendence proof says or implies.

### Unit 17


**1.** (a) Unit 7, mix on Readings. (b) Unit 11, the halving or averaging rule. (c) Unit 12, the shortfall construction. (d) Unit 14, the heading rule on a whole-number pair.

**2.** Answers vary. For example: e is fully specified by the rule in Unit 12, which produces a proven-accurate fraction for any precision requested; nothing about that description waits on a limit being taken first.

**3.** Because every claim only ever refers to one specific rule and one specific requested precision at a time; nothing in the reasoning requires gathering every possible number into one object before starting.

### Unit 18


**1.** Kind 1. Check: (4,1)*(4,1) = (16,8).

**2.** Kind 1. Checked by the proof in Unit 11.

**3.** Kind 2. Checked by dropping balls and timing them; fails once air resistance matters.

**4.** Kind 3. No calculation tests "more real."

**5.** Kind 1. A theorem, a checkable argument.

**6.** Kind 3. No calculation or proof in this book tests a claim about what exists prior to any rule.

**7.** Kind 1. Unit 11 proves the bound directly, by the halving construction.

**8.** Kind 3, as written. "Both satisfy c*c+s*s=1" is kind 1 and checkable; "is what they really are, underneath" claims an identity between two different constructions that no shared equation can establish.

---
