# Python, Rust, C++, OS

Paid on this host: CPython 3.12, rustc, g++, Linux 6.12 x86_64, page 4096, 2 CPUs.

```
python3 dna_code.py os_probe.py
rustc move.rs && g++ wrap.cpp
```

---

## Shared stack

A language is V + G + θ.
An OS is V (pages, pids, fds) + G (syscall) + θ (fault, kill).
Compile-time θ vs run-time θ is when the refuse runs, not a different ontology.

| | V | G | θ |
|---|---|---|---|
| bits | {0,1} after threshold | AND XOR | host + writes 2 |
| C++ byte | 0..255 | wrap + | host int 256 |
| C++ int | machine word | + * | UB, overflow, nullptr deref |
| Rust owned String | one owner | move | E0382 borrow after move |
| Python object | heap + type + refcount | runtime ops | TypeError, RecursionError |
| OS page | 4096-byte frames | map / fault | SIGSEGV |
| OS process | pid, fd {0,1,2}, mm | fork exec | kill, OOM |
| file path | string + `/` | open | ENOENT |

---

## C++

Write first, ask V later.

`uint8_t 255+1` → **0** (wrap). `int 255+1` → **256** (wider V). Same ink as wrap Z/256 vs host N.

`nullptr` is a letter. Deref is a write the V of valid objects does not list. C++ often does not θ at compile. That is hidden partiality sold as a total `*`.

Undefined behavior is life support plus silent μ: the write left the standard-V and the host still emits *something*. Doctor: stamp UB as θ, or listed sanitizer-V.

Templates / overloads: many G, one glyph. Error 4 if you book `+` as essence.

RAII is prune: end of cut drops the map (destructor). That is delete-what-is-unsupported, in time.

---

## Rust

Ownership is a listed mint: one live owner letter per String.

```
let t = s;  println!("{}", s);
error[E0382] borrow of moved value
```

θ at compile. The run that only moved printed `moved cut` and never used `s`.

Borrow is a second slot (like isolate seed) with a lifetime cut. Two compose-orders on the same letter (alias + mutate) is C2; rustc refuses instead of leftover-at-runtime.

`unwrap` on None is θ pushed to run (panic). Hidden partiality if you pretend Option is T.

unsafe is public μ of “I listed these alias letters.” Silent unsafe is error 8.

---

## Python

V is “objects.” Type is a stamp on the object, checked at run.

`1+"a"` TypeError: C10 host mismatch.
`True+True` is 2: bool is a cut on int, host `+` ignores the cut.
Intern: two `(1,2)` one id. Allocator can reissue `id([])`.
Recursion limit 1000: listed stack then θ.
GIL: one bytecode-cut at a time on this runtime. Two threads are two compose-orders with a lock-G. STIPULATED here (not measured this run).
`def` is ingest a map. NameError is prune: the cut does not support that letter.

Dynamic θ is late. Fast to write. Easy to book a total-looking G (error 20).

---

## Operating system (this box)

```
pid 382  ppid 376
page 4096
fd 0,1,2
uid 0
nproc 2
VmRSS 9360 kB
Threads 1
open fds 4
```

Process is an isolate: address space + fd table + page maps.
Syscall is a G from user V to kernel V. Wrong args: errno θ.
Page fault: write not in the mapped V. Kernel either μ (map a frame) or θ (SIGSEGV).
File is a noun. Prior: inode + bytes + path string. “The file” is error 1.
Scheduler: which isolate runs. Two processes, one core: compose-order leftover if they share a page without a lock-G.
Kill is prune of the process map.
Root uid 0 on this box: lock-G off. Most θ that would fire for uid≠0 do not.

---

## What we did not treat as furniture before

- Byte wrap vs host int is the same leak/wrap split as bits vs Q.
- Move error is θ, not a vibe. Paid E0382.
- UB is off-book landing.
- Intern and malloc reuse smash mint (`id`).
- Page size 4096 is listed V of frames. “Memory” is the noun.
- Path `/` is a letter in path-V.
- Bool+bool leaving {T,F} into 2 is V2 host +.
- Option/None and nullptr are dead isolators. Panic vs UB vs TypeError are three θ clocks (compile, run-safe, run-dynamic).

---

## How the three languages sit on the OS

C++: thin cut over words and addresses. Fast. Easy leak into UB.
Rust: extra mint slot (owner) and compile θ on alias+mutate.
Python: fat object V, late θ, intern/GC prune.

All three emit syscalls on the same page-V and pid-V. The language cut does not replace the OS cut. Two grammatical layers, one machine (`CUT.md`).
