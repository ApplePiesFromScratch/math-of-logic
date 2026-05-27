# The Math of Logic

**One propagation operator. Three parameters. Every formal system.**

`P / G → Q`

A single mechanism — loaded pattern propagation under gradient constraints — generates classical logic, all major non-classical logics, differential and integral calculus, probability theory, and the De-Reification Axiom Standard (DRAS). The laws are not chosen. They are forced by carrier arithmetic.

---

## What Is a Carrier Set

Every formal system is completely specified by three parameters:

| Parameter | Symbol | What it controls |
|-----------|--------|-----------------|
| Value carrier | **V** | What values are possible: `{0,1}`, `{0,B,1}`, `[0,1]`, `ℝ` |
| Gradient family | **Γ** | Which operations are available: NOT, AND, OR, differential, ... |
| Coherence threshold | **θ** | Maximum load before incoherence |

Change one parameter. Different laws become forced automatically. The same arithmetic that forces Non-Contradiction in `{0,1}` forces the Fundamental Theorem of Calculus in `ℝ`. Not analogy — the same mechanism.

Every claim in this repository is demonstrated in running code. Run `python core/pl_unified.py` and see for yourself.

---

## Repository Structure

```
math-of-logic/
├── core/
│   ├── pl_unified.py          Reference implementation (§0–§12, all assertions)
│   └── carrier_tool.py        Interactive carrier explorer and diff tool
├── carriers/
│   └── *.json                 Carrier definitions: classical, paraconsistent,
│                              modal, fuzzy, linear, probability, calculus
├── coding-logics/             Three-book eBook series (see below)
│   ├── python/index.html
│   ├── rust/index.html
│   └── linux/index.html
├── ml/
│   ├── pl_communal_field.py   Carrier-based multi-agent learning field
│   └── pl_standing_wave.py    Standing wave learning engine
├── millennium/
│   └── millennium_engine.py   Seven Millennium Prize Problems as
│                              carrier boundary constraint questions
├── demos/
│   └── *.py                   Worked examples: paradoxes, calculus,
│                              coastline, game theory, friendship paradox
└── docs/
    ├── PL_DRAS_Calculus_Unified_v1.pdf
    └── carrier_set_framework_v2.pdf
```

---

## The Books

### Coding Logics — A Three-Language Series

Hands-on guides to building formal logic systems from first principles. Each book is a self-contained HTML eBook requiring no installation.

| Book | File | What it shows |
|------|------|---------------|
| **Python** | `coding-logics/python/index.html` | Laws as tests, `all()` as exhaustive proof, full `Carrier` class |
| **Rust** | `coding-logics/rust/index.html` | Type system enforces carrier properties at compile time, not runtime |
| **Linux / C** | `coding-logics/linux/index.html` | Standalone guide from terminal setup to complete framework in ~200 lines of C |

The Linux edition is fully standalone — includes GCC setup, mathematical reference, and everything needed without reading anything else first.

### The Math of Logic — KDP Textbook

A secondary-school-level introduction to carrier sets, formal systems, paradoxes, and the connection between logic, calculus, and probability. Available on Amazon KDP.

Ten chapters. Graded exercises with answers. Python code examples in Chapter 9. Licensed CC BY-NC 4.0.

---

## Quick Start

```bash
git clone https://github.com/ApplePiesFromScratch/math-of-logic.git
cd math-of-logic

# Full framework demonstration
python core/pl_unified.py

# Interactive carrier explorer
python core/carrier_tool.py --learn

# Compare two formal systems
python core/carrier_tool.py --diff classical paraconsistent_lp

# Read the Python eBook
open coding-logics/python/index.html    # macOS
xdg-open coding-logics/python/index.html  # Linux
```

---

## The ML Architecture

`ml/pl_communal_field.py` implements a carrier-based multi-agent learning field with emergent gradient classification and endosymbiotic integration.

Agents are classified as SYMBIOTIC, NEUTRAL, or PARASITIC based on their contribution to the consensus gradient — no hardcoded roles. A shared gradient pool accumulates the field's collective gradient history. When an agent's pool similarity exceeds a threshold for a sustained number of epochs, it transitions from sovereign agent to **GradientOperator**: a permanent gradient component embedded in pool infrastructure.

This is the mitochondria event, emerging from four ingredients:

- Load accounting
- Gradient classification
- Pool similarity measurement
- Death-birth cycle

No additional logic. The mechanism decides.

Stable attractor observed at 300 epochs: one symbiotic sovereign agent maintaining task-relevant gradients alongside N gradient operators. The symbiotic agent resists endosymbiosis through its own usefulness — higher contribution means more distinctive gradient means lower pool similarity means further from integration. Symbiosis and endosymbiosis are in natural tension.

---

## The Millennium Engine

`millennium/millennium_engine.py` encodes all seven Millennium Prize Problems as `BoundaryProblem` instances — constraint questions on carrier boundary conditions rather than statements to be proved by traditional proof methods.

```python
python millennium/millennium_engine.py
```

---

## Companion Repository

[propagation-logic](https://github.com/ApplePiesFromScratch/propagation-logic) — the core `pl/` Python package, full carrier JSON library, DRAS calculus, and additional demonstrations.

---

## License

Code: [MIT License](LICENSE)

Books and written material: [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/) — free to share, adapt, and use for non-commercial educational purposes with attribution.

---

*Formal systems are not discovered. They are engineered.*
