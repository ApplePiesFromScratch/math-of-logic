# mathoflogic

Cut and ledger. Three knobs. One operator.

```
V       listed values
G       listed maps
theta   listed refusal / budget

P / G -> Q
```

Stdlib. No install. Nouns are labels. There is no grounding slot.
`=` is a scale. `A=A` is a weigh.

## First command

```
PYTHONPATH=. python3 -c "from pl import isolate, rate; x=isolate(3); print(rate(x*x, x))"
```

Prints `6`. V is `int` or `Fraction`. `float` and `bool` leave V.

```
python verify.py
```

## What this is

Not a math library of theorems. A tool that refuses silent growth of V
and refuses to call a finite cut a proof.

`pl.PROCESS` is the kernel: isolate, rate, certify, Runtime, ledger, mu.
Workshops (origin, modal, process-calc labs, mechanism, studio) are
presentations of the same loop.

## Run

```
python verify.py
PYTHONPATH=. python -m studio.eq
PYTHONPATH=. python -m studio.proofcut
PYTHONPATH=. python -m studio.logic
PYTHONPATH=. python -m mechanism.verify
python origin/tests/run.py
PYTHONPATH=modal python -m modal.verify
PYTHONPATH=process-calc python -m pcalc.lessons
python carriersets/tools/atlas.py
python carriersets/library_verify.py
python pl/PROCESS.py
```

`from pl import isolate, rate, certify, Runtime` is the package.
`python -m pl.forge` is not in this tree.

## Tree

```
pl/              kernel
mechanism/       seed traveler
origin/          two routes, walls, gate
modal/           generated frames
process-calc/    labs, same Reading
studio/          steps, eq, proofcut, logic census
carriersets/     catalog + atlas
docs/            maps, not a second kernel
```

## Honest scope

- Origin composite is CONDITIONAL: host `+` is Wall 0.
- `verify.py` atlas section runs process-carriers live.
  `library_verify.py` runs the inherited catalog when present.
- Logic Bin(V3) and assoc count are computed in studio/logic.py.
- Mechanism does not describe stars or Navier-Stokes.

Replica, receipt, ledger line. Or it did not happen.
