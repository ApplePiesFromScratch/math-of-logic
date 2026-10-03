*A Workbook*

# Numbers and Why They Work

### A First Book of Arithmetic, Where Every Rule Gets a Reason

James Pugmire


---


## Before We Start

You've been doing arithmetic since you were small. Add, subtract, multiply, divide. You know the steps. This book asks a different question: not "what are the steps," but "why do the steps work?"

Here's why that question matters. If you only know the steps, you're stuck the moment you forget one. If you know why the steps work, you can rebuild a forgotten step yourself, on the spot, because you understand what it was doing in the first place. A rule you understand is a rule you'll always have. A rule you only memorized is a rule that can slip away the moment you're nervous, like during a test.

Every rule in this book gets a reason. Not "because that's the rule," a real reason, the kind you could explain to a friend and have them actually understand it. Some of these reasons might surprise you, even for rules you've been using for years.


### How This Book Works

Every unit has a big question, an explanation with the reason spelled out, a few worked examples done slowly, a "Try It Yourself" problem with a hint, and a set of practice problems using only what that unit has covered. Answers to every practice problem are in the back, organized by unit.

Use a pencil. Do the problems on paper, not in your head. You'll understand a rule differently once you've used it yourself than you will just from reading about it.


---


*Unit 1*

## Place Value: Why Digits Change Meaning


> **Big Question:** Why does the digit 3 mean something different in 30 than it does in 300?

The number 347 isn't just the digits 3, 4, and 7 sitting next to each other. Each digit's *position* tells you what it's worth. The 7 is worth 7 (seven ones). The 4 is worth 40 (four tens). The 3 is worth 300 (three hundreds). Add those up: `300 + 40 + 7 = 347`.


> **Why does position matter?** Because we only have ten digits, 0 through 9, and we need to write numbers far bigger than 9. Position is the trick that lets ten symbols represent numbers as large as you'll ever need to write: each spot you move to the left is worth ten times more than the spot before it. That single idea, called place value, is the reason every rule in the next few units works at all.

Ten digits, and each spot worth ten times the one before it, is called **base ten**. It's the system this whole book uses, almost certainly because people have ten fingers to count on, not because ten is the only number that could have worked. Computers run on base two, using only the digits 0 and 1, with the exact same place-value idea underneath. Base ten is a choice this book makes and sticks with, not a law every number system has to follow.


*Demonstration 1*

```
347  =  3 hundreds + 4 tens + 7 ones
     =  300 + 40 + 7
     =  347
```


*Demonstration 2: a bigger number*

```
5,208  =  5 thousands + 2 hundreds + 0 tens + 8 ones
       =  5000 + 200 + 0 + 8
       =  5208

Notice the 0. It isn't decoration, it's holding the tens spot
open so the 2 stays in the hundreds spot where it belongs. Take
the 0 out and you'd have 528, a completely different number.
```


**Try It Yourself:** Break 6,024 down into thousands, hundreds, tens, and ones, and explain what job the 0 is doing. *Hint: work right to left. What's in the ones spot? Tens? Hundreds? Thousands?* Answer: 6 thousands + 0 hundreds + 2 tens + 4 ones = 6000+0+20+4 = 6024. The 0 holds the hundreds spot open so the 2 stays in the tens spot.


### Practice: Unit 1


1. Break 582 down into hundreds, tens, and ones.

2. Break 3,706 down into thousands, hundreds, tens, and ones.

3. What job is the 0 doing in the number 6,025?

4. Which is bigger, the 5 in 512 or the 5 in 125? Explain using place value, not just "512 is bigger."

---


*Unit 2*

## Addition and Subtraction: What Carrying Actually Does


> **Big Question:** When you "carry the 1" in addition, what are you actually carrying, and why does it work?

Add 38 and 47. Line them up by place value:


*Demonstration 1: 38 + 47*

```
38
 + 47
 ----

Ones column: 8 + 7 = 15. But 15 doesn't fit in one ones-spot,
it's one ten and five ones. Write the 5 in the ones spot, and
move the ten over to the tens column. That's the "carry."

Tens column: 3 + 4 + (the 1 ten you carried) = 8

   38
 + 47
 ----
   85
```


> **Why does carrying work?** Because of place value from Unit 1. Ten ones are worth exactly the same as one ten. When a column adds up to more than 9, you're not making a mistake, you've genuinely built enough ones to trade in for a ten. Carrying is just recording that trade in the next column over, where a ten belongs.


*Demonstration 2: subtraction, borrowing, 72 - 48*

```
72
 - 48
 ----

Ones column: can't take 8 away from 2, there aren't enough ones.
Borrow a ten from the 7 (making it 6), and turn it into 10 extra
ones, joining the 2 to make 12.

Ones: 12 - 8 = 4
Tens: 6 - 4 = 2

   72
 - 48
 ----
   24
```


> **Why does borrowing work?** The same place-value trade, in reverse. A single column isn't allowed to hold a negative count of ones by itself, so when a column doesn't have enough, you break open one ten from the tens column and turn it into 10 more ones. The total value of the number never changes, you've just repacked it differently. (Negative numbers themselves are real and useful, you'll meet them properly in Unit 5, but borrowing is a trick for keeping every single column a normal count of 0 to 9, so you never need one here.)


**Try It Yourself:** Add 156 + 278, showing every carry. *Hint: ones column first, then tens, then hundreds. Carry whenever a column passes 9.* Answer: Ones: 6+8=14, write 4 carry 1. Tens: 5+7+1=13, write 3 carry 1. Hundreds: 1+2+1=4. Answer: 434.


### Practice: Unit 2


1. 56 + 38, showing the carry.

2. 91 - 47, showing the borrow.

3. 245 + 178, showing every carry.

4. 604 - 256, showing every borrow.

5. Explain, in your own words, why a "carry" is worth 10 times more once it lands in the next column.

---


*Unit 3*

## Multiplication: Breaking A Big Problem Into Easy Pieces


> **Big Question:** Why does the multiplication algorithm you learned actually give the right answer?

Multiplication starts as repeated addition. `4 * 3` means "4, three times": `4+4+4=12`. That's a solid way to picture multiplication for whole numbers, but adding a number to itself dozens of times gets slow, so we need a faster way for bigger numbers. That faster way is built on place value again.


> Does "repeated addition" cover every multiplication you'll ever do? Not quite. "3 times 4" is easy as repeated addition: add 3 to itself 4 times. But "3 times one-half" can't literally mean adding 3 to itself half a time, that doesn't make sense as counting. Repeated addition is the right starting picture for whole numbers, the numbers this unit uses, and it's the picture this book leans on to explain the rules below. Multiplying fractions and negative numbers, later in this book, will need a different picture (scaling, instead of counting copies), built on what you learn here rather than replacing it.


*Demonstration 1: 23 * 4*

```
23 is really 20 + 3. Multiplying by 4 means multiplying BOTH
pieces by 4, then adding the results together.

20 * 4 = 80
 3 * 4 = 12
        ----
        92

23 * 4 = 92
```


> **Why does splitting the number work?** Because multiplication spreads out over addition: multiplying a sum by something is the same as multiplying each piece separately and adding the answers. `23 * 4` and `(20+3) * 4` are the exact same problem, written two ways. Splitting 23 into 20+3 just makes each piece small enough to multiply in your head.


*Demonstration 2: a bigger example, 34 * 26*

```
Split BOTH numbers by place value: 34 = 30+4, and 26 stays whole
for now.

30 * 26 = 780
 4 * 26 = 104
         ----
         884

34 * 26 = 884

Check by splitting 26 too, another way: 30*20=600, 30*6=180,
4*20=80, 4*6=24. Add all four: 600+180+80+24 = 884. Same answer,
because you're allowed to split either number, or both.
```


**Try It Yourself:** Multiply 42 * 23 by splitting 42 into 40+2. *Hint: 40*23 first, then 2*23, then add.* Answer: 40*23=920. 2*23=46. 920+46=966.


### Practice: Unit 3


1. 34 * 3, by splitting 34 into 30+4.

2. 27 * 4, by splitting 27 into 20+7.

3. 42 * 23, showing all four partial products (split both numbers).

4. Explain why splitting a number for multiplication doesn't change the answer, using the word "place value" somewhere in your explanation.

---


*Unit 4*

## Division: Undoing Multiplication


> **Big Question:** What is division actually asking?

`12 / 4` is asking: "what number, multiplied by 4, gives 12?" Division and multiplication are opposites, the same way addition and subtraction are opposites. If `3 * 4 = 12`, then `12 / 4 = 3` and `12 / 3 = 4`, for free, no new fact required.


> **Why does thinking of division this way help?** Because it turns a division problem into a multiplication problem you might already know. If someone asks you `56 / 8`, you can ask yourself instead: "8 times what gives 56?" and search your times tables for the answer, rather than treating division as a totally separate skill from multiplication.


*Demonstration 1: 84 / 4*

```
Split 84 by place value: 80 + 4.

80 / 4 = 20      (since 4*20=80)
 4 / 4 = 1       (since 4*1=4)
        ----
        21

84 / 4 = 21.  Check: 21 * 4 = 84. Correct.
```


*Demonstration 2: 156 / 12*

```
What times 12 gets close to 156, without going over?
12 * 10 = 120.  156 - 120 = 36 left over.
What times 12 gets close to 36?
12 * 3 = 36.  Nothing left over.

10 + 3 = 13

156 / 12 = 13.  Check: 13 * 12 = 156. Correct.
```


### When Division Doesn't Come Out Even

Every division so far has landed exactly on a whole number, with nothing left over at the end. That's not always true, and pretending it is would be hiding something real. Numbers don't always split into equal groups perfectly.


*Demonstration 3: 17 / 5, where something is left over*

```
What times 5 gets close to 17, without going over?
5 * 3 = 15.  17 - 15 = 2 left over.
5 * 4 = 20.  That's too much, 20 is bigger than 17.

So 5 goes into 17 three whole times, with 2 left over that
can't be split into another full group of 5.

17 / 5 = 3 remainder 2

Check: 5 * 3 = 15, and 15 + 2 (the leftover) = 17. Correct.
```


> **Why keep the remainder instead of ignoring it?** The 2 left over is real. It didn't disappear, and it isn't a mistake, it's an honest part of the answer: 17 things really do split into 3 full groups of 5 with 2 things left outside any group. Writing "17/5=3" alone and dropping the 2 would be quietly throwing away a true fact about the number 17. Naming the leftover, instead of pretending it isn't there, is a habit worth keeping well beyond this one problem.


**Try It Yourself:** Find 96 / 8, by asking "8 times what gives 96?" Break it into pieces if that helps. *Hint: 8*10=80. 96-80=16. 8 times what gives 16?* Answer: 8*10=80, remainder 16. 8*2=16. So 10+2=12. 96/8=12. Check: 12*8=96.


### Practice: Unit 4


1. 96 / 8, checked by multiplying back.

2. 144 / 12, checked by multiplying back.

3. 108 / 9, checked by multiplying back.

4. 23 / 6. This one has a remainder; find it and check your answer the way Demonstration 3 did.

5. Explain, in one sentence, why checking a division answer means multiplying, not dividing again.

---


*Unit 5*

## Negative Numbers


> **Big Question:** Why does a negative number times a negative number come out positive? That rule feels like it shouldn't be true.

Before the strange rule, the easy part. A negative number is a direction, not a strange kind of stuff. Minus forty dollars is forty dollars owed, not forty anti-dollars sitting in a box. Drawing this as a number line, positives to the right and negatives to the left, is a picture people choose. The line is a tool. It is not a claim that numbers are points on a physical line. Adding moves you one way along that picture. Subtracting moves you the other way.

A minus can also be a relation, not a pile moving. Two cars drive apart. One pays rope out. The other has the rope tied to the bumper. The rope gets longer. Nothing left the first car and arrived in the second. Flip which way you call forward and each car's reading flips. The rope getting longer does not. Owing and forgiving still move a pile. The rope does not.


*Demonstration 1: addition and subtraction with negatives*

```
(-3) + (-5):  start at -3, move 5 more to the left.  ->  -8

(-3) + 7:  start at -3, move 7 to the right.  ->  4

5 - (-2):  subtracting a negative means moving right instead
of left (undoing the negative flips the direction).  ->  7
```


### Now, The Strange One: Negative Times Negative

Instead of just being told the rule, let's find it by following a pattern that's already true, and refusing to let it break.


*Demonstration 2: extending a pattern you already trust*

```
Start with something nobody argues about: (-4) times a
shrinking positive number.

(-4) * 3  =  -12
(-4) * 2  =  -8
(-4) * 1  =  -4
(-4) * 0  =   0

Look at the pattern in the answers: -12, -8, -4, 0. Each time
the second number drops by 1, the answer goes UP by 4.

If that pattern is real, it shouldn't stop just because we
reached 0. Keep going the same way:

(-4) * (-1)  =  0 + 4  =   4
(-4) * (-2)  =  4 + 4  =   8
(-4) * (-3)  =  8 + 4  =  12
```


> Is this a proof, or a choice? Nobody was forced to continue the pattern past zero. We chose to keep the same step, add 4 each time, instead of switching steps once the numbers turned negative. That choice wrote the plus sign. Keeping the same step is what makes negative times negative sit with the multiplication facts you already trust, rather than needing a special exception at zero. It is a choice to keep one step going.

Two different "round down" rules also split once a number is negative. Toward the more negative number, and toward zero, agree on positives and disagree on negatives. This book does not pick one of them yet. Naming which rule you mean is part of the answer.


**Try It Yourself:** Using the same pattern method, find `(-6) * (-1)`. Start from `(-6)*2`, `(-6)*1`, `(-6)*0`, and continue the pattern. *Hint: (-6)*2=-12, (-6)*1=-6, (-6)*0=0. Each step up by 6.* Answer: -12, -6, 0, then continuing up by 6: (-6)*(-1)=6.


### Practice: Unit 5


1. (-6) + 9

2. (-6) - 4

3. 8 - (-5)

4. (-7) * 4

5. (-6) * (-5), using the pattern method from this unit.

6. (-20) / 4

---


*Unit 6*

## Fractions


> **Big Question:** Why do you need a common denominator to add fractions, but not to multiply them?

A fraction is a count of equal pieces. `3/4` means "3 pieces, out of 4 equal pieces that make a whole." The bottom number (denominator) says how big each piece is. The top number (numerator) says how many of those pieces you have.


### Adding Fractions

`1/2 + 1/3` is not `2/5`. Here's why: a half and a third are pieces of *different sizes*. You can't add "2 pieces of one size" to "1 piece of a different size" and call the total a clean count of pieces, until every piece is the same size.


*Demonstration 1: 1/2 + 1/3*

```
Rewrite both fractions using the same size piece (sixths, since
both 2 and 3 divide evenly into 6):

1/2  =  3/6      (each half is really 3 sixths)
1/3  =  2/6      (each third is really 2 sixths)

Now the pieces match:  3/6 + 2/6 = 5/6
```


> **Why doesn't multiplication need matching pieces?** Multiplying fractions isn't counting pieces of the same size, it's asking "what's a part of a part?" `2/3 * 3/4` asks "what's three-quarters of two-thirds?" That question makes sense no matter what size the pieces are, so multiplication just multiplies straight across: numerators together, denominators together.


*Demonstration 2: multiplying fractions*

```
2/3 * 3/4  =  (2*3) / (3*4)  =  6/12  =  1/2

(6/12 simplifies to 1/2 by dividing top and bottom by 6)
```


### Dividing Fractions

Remember from Unit 4: dividing by a number is the same as multiplying by "1 over that number." Dividing by 4 gives the same answer as multiplying by `1/4`, because `4 * 1/4 = 1`. The exact same idea works for fractions: dividing by `1/4` gives the same answer as multiplying by `4/1` (flip it over), because `1/4 * 4/1 = 1`.


*Demonstration 3: 1/2 divided by 1/4*

```
Question: how many quarters fit inside a half?

1/2  /  1/4   =   1/2  *  4/1   =   4/2   =   2

Check by counting: two quarters make a half. Two fits.
```


**Try It Yourself:** Find `3/4 divided by 1/2` by flipping the second fraction and multiplying. *Hint: 3/4 * 2/1 = ?* Answer: 3/4 * 2/1 = 6/4 = 3/2 (or 1 and a half).


### Practice: Unit 6


1. 1/3 + 1/6 (find a common denominator first)

2. 3/5 - 1/5

3. 2/5 * 5/6, simplified

4. 3/4 divided by 1/2

5. 2/3 of 15 (this means `2/3 * 15`)

---


*Unit 7*

## Decimals


> **Big Question:** What is a decimal, really, and how is it connected to fractions?

Unit 1 showed that moving one spot to the left multiplies a digit's value by 10. Decimals just keep going the other direction, past the ones spot: each spot to the *right* of the decimal point divides by 10 again. The first spot after the point is tenths, the next is hundredths, and so on.


> **Why does this mean a decimal is secretly a fraction?** Because "tenths" and "hundredths" are just fraction denominators wearing a different outfit. `0.3` means 3 tenths, which is the fraction `3/10`. `0.75` means 75 hundredths, which is `75/100`. Every decimal is a fraction with a denominator of 10, 100, 1000, and so on, written in a shorter form.


*Demonstration 1: adding decimals, using the fraction underneath*

```
0.3 + 0.45

As fractions: 3/10 + 45/100

Match the denominators (Unit 6): 3/10 = 30/100

30/100 + 45/100 = 75/100 = 0.75

0.3 + 0.45 = 0.75
```

This is also exactly why lining decimals up by their decimal point when you add them works: lining up the points lines up the tenths with tenths, hundredths with hundredths, the same "matching pieces" idea from Unit 6.


*Demonstration 2: multiplying decimals*

```
1.2 * 0.3

As fractions: 12/10 * 3/10 = 36/100 = 0.36

1.2 * 0.3 = 0.36

Notice: one decimal place in 1.2, one decimal place in 0.3, and
two decimal places in the answer, 0.36, because the denominators
are multiplying together too: 10*10=100.
```


**Try It Yourself:** Find 2.5 * 4 by thinking of 2.5 as the fraction 25/10. *Hint: 25/10 * 4 = 100/10 = ?* Answer: 25/10 * 4 = 100/10 = 10. So 2.5*4=10.


### Practice: Unit 7


1. 1.5 + 2.75

2. 6.4 - 2.9

3. 3.2 * 5

4. 9.6 / 1.6 (hint: turn both into fractions over 10 first: 96/10 divided by 16/10)

---


*Unit 8*

## Order of Operations


> **Big Question:** Why does everyone agree to do multiplication before addition? Couldn't we just go left to right?

Try going strictly left to right on `3 + 4 * 2`. You'd get `3+4=7`, then `7*2=14`. But if you do the multiplication first, `4*2=8`, then `3+8=11`. Same problem, two different answers. That's a real problem: math needs every person, everywhere, to get the same answer to the same written problem, or numbers stop being useful for agreeing on anything.


> **Why multiplication before addition, and not the other way around?** Multiplication is a shortcut for repeated addition (Unit 3). `4*2` is shorthand for `4+4`. If you write `3 + 4*2`, you're really writing `3 + (4+4)` in a compressed form, and doing the multiplication first is just unpacking that shorthand before you add. The agreed order isn't arbitrary, it's the order that respects what multiplication actually stands for.


*Demonstration 1: 3 + 4 * 2*

```
Multiply first: 4*2 = 8
Then add: 3 + 8 = 11

3 + 4 * 2 = 11
```

Parentheses come first, before even multiplication, because they're a direct instruction: "treat everything inside me as one already-finished number before you do anything else with it."


*Demonstration 2: (3+4) * 2, and why it's different*

```
Parentheses first: 3+4 = 7
Then multiply: 7 * 2 = 14

(3+4) * 2 = 14

Compare to Demonstration 1's answer of 11. Same three numbers,
same two operations, different answer, because the parentheses
changed which operation had to happen first.
```


**Try It Yourself:** Find `20 - 4 * 3 + 2`. *Hint: do the multiplication first, then work left to right through the addition and subtraction.* Answer: 4*3=12. Then 20-12+2 = 8+2 = 10.


### Practice: Unit 8


1. 5 + 3 * 4

2. (5 + 3) * 4

3. 18 / 3 + 2 * 5

4. 30 - 2 * (4 + 1)

5. Explain, in your own words, why parentheses are allowed to override the usual order.

---


*Closing*

## You Understand These Rules Now, Not Just Remember Them

Every rule in this book had a reason behind it, and now you know all of them: place value explains carrying and borrowing. Splitting a number by place value explains multiplication. Multiplication in reverse explains division. A pattern that refuses to break explains negative times negative. Matching piece sizes explains adding fractions, and division-as-its-reciprocal explains dividing them. Fractions in disguise explain decimals. And respecting what multiplication stands for explains the order of operations.

None of that was arbitrary. Every single rule followed consistently from place value and the handful of choices this book named along the way, base ten, keeping a pattern going, treating multiplication as repeated addition to start. That's what real math looks like: not a pile of separate facts to memorize, but one small set of chosen starting points, followed carefully wherever they lead.

Algebra is next, and it uses every one of these rules constantly, just with letters standing in for numbers you don't know yet. You're ready for it.


---


*Answer Key*

## Check Your Work


### Unit 1


**1.** 582 = 5 hundreds + 8 tens + 2 ones

**2.** 3,706 = 3 thousands + 7 hundreds + 0 tens + 6 ones

**3.** 6,025: the 0 sits in the hundreds spot, holding it open so the 2 stays correctly in the tens spot.

**4.** The 5 in 512 is worth 500 (five hundreds). The 5 in 125 is worth 5 (five ones). Same digit, different position, different value.

### Unit 2


**1.** 56+38=94. Ones: 6+8=14, write 4 carry 1. Tens: 5+3+1=9. Answer: 94.

**2.** 91-47=44. Ones: borrow, 11-7=4. Tens: 8-4=4. Answer: 44.

**3.** 245+178=423. Ones: 5+8=13, write 3 carry 1. Tens: 4+7+1=12, write 2 carry 1. Hundreds: 2+1+1=4. Answer: 423.

**4.** 604-256=348.

**5.** Ten of whatever you carried in the smaller column are worth exactly one of the next column over, because each column is ten times the value of the one before it.

### Unit 3


**1.** 34*3: 30*3=90, 4*3=12, sum=102.

**2.** 27*4: 20*4=80, 7*4=28, sum=108.

**3.** 42*23: 40*20=800, 40*3=120, 2*20=40, 2*3=6, sum=966.

**4.** Splitting a number by place value just rewrites it as a sum (like 34=30+4) without changing its value, and multiplication spreads out evenly over a sum, so multiplying the pieces separately and adding always gives the same answer as multiplying the whole thing at once.

### Unit 4


**1.** 96/8=12. Check: 12*8=96.

**2.** 144/12=12. Check: 12*12=144.

**3.** 108/9=12. Check: 12*9=108.

**4.** 23/6 = 3 remainder 5, since 6*3=18 and 23-18=5. Check: 6*3=18, and 18+5=23.

**5.** Because division and multiplication undo each other; multiplying your answer by the number you divided by should rebuild the original number.

### Unit 5


**1.** (-6)+9 = 3

**2.** (-6)-4 = -10

**3.** 8-(-5) = 13

**4.** (-7)*4 = -28

**5.** (-6)*(-5): pattern from (-6)*2=-12, (-6)*1=-6, (-6)*0=0, going up by 6 each step: (-6)*(-1)=6, (-6)*(-2)=12, (-6)*(-3)=18, (-6)*(-4)=24, (-6)*(-5)=30.

**6.** (-20)/4 = -5

### Unit 6


**1.** 1/3+1/6: 1/3=2/6, so 2/6+1/6=3/6=1/2.

**2.** 3/5-1/5 = 2/5

**3.** 2/5*5/6 = 10/30 = 1/3

**4.** 3/4 divided by 1/2 = 3/4*2/1 = 6/4 = 3/2

**5.** 2/3 of 15 = 2/3*15 = 30/3 = 10

### Unit 7


**1.** 1.5+2.75 = 4.25

**2.** 6.4-2.9 = 3.5

**3.** 3.2*5 = 16.0

**4.** 9.6/1.6: as fractions, 96/10 divided by 16/10 = 96/16 = 6. So 9.6/1.6=6.

### Unit 8


**1.** 5+3*4: multiply first, 3*4=12, then 5+12=17.

**2.** (5+3)*4: parentheses first, 5+3=8, then 8*4=32.

**3.** 18/3+2*5: 18/3=6, 2*5=10, 6+10=16.

**4.** 30-2*(4+1): parentheses first, 4+1=5, then 2*5=10, then 30-10=20.

**5.** Parentheses are a direct instruction to finish what's inside them first, before anything else happens, which lets you deliberately change the order when the usual order isn't what you meant.

---
