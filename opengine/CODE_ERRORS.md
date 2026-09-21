# Code bugs as the same incompatibles

Math called them contradiction. Code calls them crash, freeze, hack, Heisenbug.
Same G, different nouns.

```
python3 dna_code.py contradiction.py
# E0382 and byte wrap paid in CODE_LANGS.md
```

---

## Taxonomy (code names → our C / error #)

| code name | mechanic | era it got famous |
|---|---|---|
| **invalid opcode / halt** | C3 leave V | front panel, raw machine |
| **segfault / bus error** | C3 write not in mapped page-V | UNIX, every C |
| **null deref** | C9 dead isolator | C, C++, Java NPE |
| **uninitialized read** | mint missing (error 1 on a register) | C stack |
| **buffer overflow** | C3 + silent μ of adjacent letters | Morris 1988, every C string |
| **off-by-one** | wrap vs host on an index V | everywhere |
| **integer overflow** | C5 wrap `255+1=0` vs host 256 | crypto, size checks |
| **use after free** | C4 / intern-smash: `id` reissued (`dna_code` two `id([])`) | C heap, UAFchain |
| **double free** | two compose-orders on one mint | heap |
| **type confusion** | C10 host mismatch, late θ | C union, Python, JS |
| **dangling pointer** | mint deleted, letter kept | C++ |
| **data race** | C2 two compose-orders, leftover torn word | threads, 90s+ |
| **deadlock** | two lock-G wait on each other; no write lands | freeze not crash |
| **livelock** | writes land, progress read stays 0 | freeze-shaped |
| **TOCTOU** | two reads of one path, time between; leftover | UNIX symlink, 70s+ |
| **injection (SQL/sh)** | syntax doing semantic work (#23); two V glued | web 90s+ |
| **XSS / CSRF** | mint of origin dropped; val-eq of two principals | web |
| **path traversal** | `../` leaves the path-V you named | every file API |
| **format string** | `%s` as G on attacker letters | 90s C |
| **unchecked unwrap / unwrap None** | C9 pushed to panic | Rust, JS |
| **UB** | write left standard-V, host still emits | C++ life support |
| **Heisenbug** | leftover depends on isolate (timing seed) | debug changes V |
| **memory leak** | prune skipped; map stays after cut | freeze-adjacent OOM |
| **stack overflow** | listed rec-V then θ (Python 1000) | every call stack |
| **deadlock-free livelock / priority inversion** | lock-G + scheduler isolate | RTOS, Mars Pathfinder |
| **cache / Spectre / Meltdown** | two reads (arch V vs microarch leftover) | 2018 |
| **rowhammer** | analog voltages not in bit-V; threshold G fails | DRAM |
| **bit rot / ECC** | letter flipped; V of bits not closed under physics | disks, RAM |
| **time wrap** | Y2K, 2038: wrap on time-V | DOS, UNIX time_t |
| **float 0.1+0.2** | listed mantissa sold as R | IEEE, every language |
| **NaN poison** | val-eq fails, mint holds | IEEE |
| **GIL assumption** | one-cut booked as all-cuts | CPython threads |
| **hash collision** | wrap-shaped read; two mints one bucket | language runtimes |
| **intern / interned True** | two literals one object | Python, Java |
| **LLM slop compile** | two mints: string vs run (#29 runner as ∀) | now |

---

## History as moving θ

| era | typical fail | θ clock |
|---|---|---|
| switches / asm | wrong opcode, halt | instant hardware |
| C / UNIX | segfault, overflow, TOCTOU | kernel fault *after* the write |
| DOS / 9x | one program takes the box down | reboot prune |
| NT / Darwin / Linux | process isolate contains many faults | kill one pid |
| Java / Python / JS | exception objects | late, catchable |
| Rust | E0382 move, borrow | compile, before run |
| sanitizers / fuzz | listed extra V that names leaks | research μ |
| spectres | microarch leftover not in ISA V | “safe” ISA was the compress |
| LLM-written code | looks total, run θ | two-mint gap |

Moving θ earlier (Rust, type systems) does not remove leak. It posts refuse before the OS has to.

---

## Crash vs freeze vs hack

| outcome | mechanic |
|---|---|
| crash | θ fires (fault, panic, uncaught) |
| freeze | writes stop landing or progress-read is 0 (deadlock, livelock) |
| hack | attacker chooses the letter that leaves your V (overflow, injection) or val-eq of two principals |
| silent wrong | leftover kept as if it were the intended read (UB, 0.1+0.2, intern) |
| OOM / leak | prune never ran |

“Security” is θ + mint of principal + listed V. “Reliability” is leftover named. Same books.

---

## Hacks as posted leaks

Morris worm: overflow + sendmail/finger V did not list that write.  
Heartbleed: read length not in the buffer-V.  
Log4Shell: lookup syntax as G on attacker letters (#23).  
sudo / kernel privesc: lock-G off for a path you thought sealed.

Always: a G wrote a letter the defender’s V did not contain, and θ did not fire in time.

---

## Construction errors that fire first in code

Same top five as math, plus code-flavored 20 and 23:

1. Output as primitive: “the object,” “the file,” dangling pointer kept.
2. Host as ground: machine word as Z, IEEE as R.
3. Project as system: success bool, HTTP 200, tests green (#29).
4. Combinator as essence: `+` on bytes, `+` on paths, `+` on bools.
5. Leftover → 0: “works on my machine,” UB as “fine.”
20. Total-looking `*p`, `unwrap`, `system(s)`.
23. Format string, SQL, shell, log lookup.

---

## Doctor (same four moves)

Land: bounds-checked V, Option instead of T, owner mint (Rust).  
Leftover: two clocks, two cores, two reads (TOCTOU) stay on the page.  
Public μ: sanitizer, capability list, seccomp list.  
θ: do not deref dead, do not execute attacker letters as G.

Do not hire Inf (unbounded stack, unbounded heap) to look sealed.
