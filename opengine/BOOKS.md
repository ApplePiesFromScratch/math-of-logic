# How many entries

`python3 books.py`

School double-entry on `2+2`:

```
debit nothing     0
credit sum        4
```

Same merge with the slots named:

```
debit left loc / right loc
credit front loc
debit pile-count 4   credit pile-count 1
debit vol 4          credit vol 4
stamp G merge-to-front
stamp V_loc {left, right, front}
θ none
```

**2 lines vs 10.** The 4 survived because volume was the only credit. Count 4→1 never posted.

---

Two columns are enough for *one* read of *one* G.  
They are a compress as soon as there is a second slot, a second read, a mint, or a θ.

V / G / θ is already three columns. Isolate writes two slots. Mix reads four numbers. Rate needs both live channels. Leftover needs two G on the page.

“Continuous entry” is: do not batch. Every `S`, every `dx`, every grain, every seed gets a line. Traveler with `eta>0` already does that (`L` writes as you move). Sending leftover to 0 is closing the book early.

Need more than 2? When more than one slot or one read is in play. That is most of the machines in this folder.

Need infinitely many? Only if V is unlistable. That is host-as-ground again. Listed V ⇒ listed lines.
