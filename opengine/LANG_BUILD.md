# Build a coding language without the usual errors

Not “use Rust and hope.” List the errors, then make each one unpostable or visible.

```
python3 plang.py accountant.py dna_code.py
```

---

## Target

A programmer writes cuts. The compiler posts them. If a write leaves V and has no θ, the program does not exist.

Errors we refuse to ship as total-looking G: C3 leak, C9 dead, C2 race leftover, C5 wrap-as-host, C10 sort clash, #20 hidden partiality, #23 syntax-as-G, #1 dangling primitive, #29 tests-green as ∀.

---

## 1. Every value has a listed V

Types are V stamps, not essences.

- `Byte` is `{0..255}`. `+` on Byte is wrap or it is `Option<Byte>` or it is θ. The glyph `+` names which G in the source (`plus_wrap` / `plus_widen` / `plus_sat`). Error 4 blocked at the glyph.
- `Int` is a listed width or a bigint V. No silent C++ `int`.
- `Ptr` is not `T`. It is `Option<Owned<T>>` or `Borrowed<T, 'cut>`. Dead isolator is a letter (`None`), not `nullptr` you star.

---

## 2. Partial maps show the hole

No `*` that looks total. No `unwrap` without a cut.

```
open : Path -> Option<File> | Err
div  : (Q, Q) -> Q | Theta   # second 0
index: (Arr T, Nat) -> T | Theta
```

The `| Theta` is in the type. Hidden partiality (#20) is a type error.

`plang` already: `post` without `theta` on a leak is `PFail`.

---

## 3. Mint is in the type

Ownership is a mint slot.

- Move drops the old letter (Rust E0382). Use-after-free cannot post.
- Borrow is isolate of a second slot with a cut name (`'a`). Two mut borrows of one mint: compile θ (C2 refused early).
- `id` / addresses are not mint. Allocator reuse is wrap; the language does not expose raw `id` as identity.

---

## 4. Two compose-orders are visible

Shared mutable letters require a lock-G in the type (`Mutex`, channel, actor isolate).
Missing lock is not UB. It is “this program did not post.”

TOCTOU: two reads of a path must be one G (`open_atom`) or leftover is a value the caller names.

---

## 5. Syntax cannot become G

No format string as executable. No `system(s)` on attacker letters. No SQL glued from strings.

Quoted data stays in data-V. Code letters live in code-V. Crossing is an explicit `eval` with a listed V of allowed G. Default is θ.

Injection (#23) becomes a type error: `Query` is not `String`.

---

## 6. Host ops stay stamped

IEEE is `F32`, not `Real`. `0.1+0.2 == 0.3` is false and sayable.
NaN: `F32` is `Num | NaN`. `==` on NaN is the letter `off`, not a bool you forget.
Bool is not Int. `True+True` does not post.

Intern is not `=`. `==` is val-eq. `is` if it exists is mint-eq and does not reuse freed ids.

---

## 7. Effects are a second V

`fn f(x: T) -> U` that also writes the disk is a lie.

```
fn f(x: T) -> U / {Net, Fs}
```

Or capability letters passed in. A function without `Fs` cannot open. Path traversal leaves the granted path-V: θ.

---

## 8. Prune and cuts

End of a cut drops borrows (RAII). Maps that the current module does not support are not in scope (no ambient god object).
`I` / global mutable singleton is opt-in and named.

---

## 9. Tests are not ∀

A test is a listed Ω. Green means those rows landed. The type `tested[Ω]` is not `true`.
Fuzz / property: extra listed generators. Still not R.

---

## 10. OS letters named

`Fd` vs `Handle` vs path. Portable code is a G that emits the target V or it is `#ifdef` as public μ.
Page, pid, errno are not “memory” and “process” essences.

---

## What to steal, what to still stamp

| steal | from | still stamp |
|---|---|---|
| owner mint + compile θ | Rust | wrap vs widen `+` |
| Option / Result | ML, Rust | no `unwrap` in the prelude |
| GC prune | Python, Java | intern and `id` |
| capabilities | Midori, Newspeak, WASM | ambient OS |
| effects | Koka, Frank | hidden IO |
| small syscall V | UNIX | “everything is a file” |

Do not steal: C total `*`, C++ UB as platform, Python `+` on bool, JS `==` coerce (val-eq across V).

---

## Smallest compiler path

1. Keep `plang` verbs as the IR: `V G mint write read theta post`.
2. Surface language elaborates into that IR.
3. `post` is the typechecker. Fail = no artifact.
4. Backend emits C / LLVM / WASM only from landed posts.
5. Runtime θ (OOM, kill) stays listed; do not pretend compile θ is the only clock.

---

## What this does not remove

Physics leftover (rowhammer, spectre) sits under the bit-V. You can list “must fence” as G. You cannot close analog into digital by a type.

Unbounded heap is still Inf if you allow it. List a cap or admit the μ.

A language without common errors is a language that cannot post them quietly. The errors can still be written as explicit θ or explicit wrap. That is the point.
