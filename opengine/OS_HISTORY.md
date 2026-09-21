# PC languages and three families of OS

Insight cut: each era isolates more letters, hides more in a host, moves θ (toggle / asm / compile / kernel / GUI), and books a new noun (file, process, window, app).

This box paid Linux + Python + rustc + g++. Windows and Mac rows are maps of those systems, not runs on this kernel.

---

## Simplest PC

**Toggle / front panel.** V = bits in a word. G = set a switch, deposit, run. θ = halt lamp. No file noun.

**Machine code.** V = opcode bytes. G = fetch-decode-execute. θ = invalid opcode, bus error.

**BIOS / firmware interrupts.** Extra G into firmware V (disk, TTY). `INT 10h` / `INT 13h` on IBM PC: listed interrupt table. That table is a public μ of “these letters talk to hardware.”

**Assembly.** Compress of opcodes into mnemonics. Same V, nicer glyph. Syntax doing semantic work if you forget the table.

**BASIC / early interpreters.** V = lines and names. θ at run (SYNTAX ERROR). Late refuse, easy total-looking G.

**C (1970s, UNIX).** V = words, addresses, `FILE*` as a stamp. G = functions + UB-shaped writes. θ often missing at compile. Portable because UNIX listed a small syscall V (fd, fork, exec, pipe).

---

## UNIX cut (the shared ancestor)

1969+: isolate a **process** (address space + fd table).  
G: syscall.  
θ: errno.  
Noun: **file** = bytes + inode + path. Everything-is-a-file is compress: sockets and devices booked as the same letter. Useful. Lossy.

`fork` is isolate a second mint of the process. Copy-on-write later is μ of pages on write, not at fork.

This cut is still the userland grammar of Linux and of Mac (BSD layer).

---

## DOS / IBM PC

Real mode: V = 1MB-shaped addresses, segment:offset two slots booked as one pointer (error 7).  
G: DOS interrupt `21h` plus BIOS.  
θ: carry flag.  
No process isolate like UNIX. One program owns the machine. Prune = reboot.

CP/M then DOS file V: 8.3 names. Path letters listed tight.

---

## Mac family

**1984 System.** V = resource fork + heap + event queue.  
G: event loop (isolate click/key, dispatch).  
θ: bomb dialog.  
Noun: **window**, **resource**. QuickDraw is a G on pixels.

**OS X / Darwin.** Three cuts stacked:

- Mach: task/port V, message G (microkernel-shaped)
- BSD: UNIX process/fd V
- Aqua / Cocoa: object + runloop V

Same machine, three grammars. POSIX userland is the BSD cut. `launchd` is prune/ingest of services.

File resource-fork leftover mostly dropped. That was a map the terrain no longer supported.

---

## Windows family

**9x (95/98/ME).** DOS leftover + 16/32 mix. One crash can prune more than one “process.” Host not sealed.

**NT (NT/2000/XP/…/11).** Different kernel V:

- HANDLE not fd (opaque mint)
- NT object manager (named kernel objects)
- Registry as extra V (config letters outside the file noun)
- Win32 API G vs NT native G (two maps; subsystem is a cut)
- Job / token: isolate of privilege letters (uid is not the whole story)

NT did not grow from UNIX V. It listed another kernel alphabet and then wrapped a UNIX-like subsystem on top (POSIX, later WSL: a Linux-V hosted on NT). WSL is public μ of “these Linux letters land here.”

GUI: message pump ≈ Mac event loop. Same isolate-dispatch G, different names.

---

## Linux family

1991 kernel: UNIX-shaped syscall V, no Mach, no NT object manager.  
Userland is a separate cut (GNU, busybox, Android, …). “Linux” as a noun compresses kernel + a userland mint.

θ: signals, oops, panic, seccomp (listed syscall V, refuse the rest).  
cgroups / namespaces: isolate a *partial* process V (pid, mount, net). Containers are cuts, not rooms.

systemd / others: ingest and prune units. Same job as launchd.

This box: Linux 6.12, page 4096, fd 0/1/2, pid isolate. That cut is live here.

---

## Language line next to the OS line

| era | language cut | θ clock | OS it rode |
|---|---|---|---|
| 50s | FORTRAN / LISP | compile / eval | mainframe batch |
| 70s | C, Smalltalk | missing UB / live image | UNIX, Alto |
| 80s | C++, Turbo Pascal, ObjC | compile + runtime | DOS, Mac System, Win |
| 90s | Python, Java, JS, Ruby | late / VM | Win9x, NT, Linux, Mac |
| 00s | C#, Swift later | compile + GC | NT, Darwin |
| 10s | Go, Rust, TS | compile; Rust owner θ | all three families |
| now | LLM-emitted source | two mints: string vs run | all three |

VM languages add a userland kernel-shaped V (bytecode, GC heap) on top of the OS cut. Two θ clocks: VM exception, then OS fault.

Rust owner θ is the new thing: mint listed before run. C++ still wrap-or-UB. Python still intern-and-TypeError.

---

## What the three OS still disagree on

| letter | Linux | Darwin | NT |
|---|---|---|---|
| file id | fd int | fd int | HANDLE |
| process | pid + mm | pid + Mach task | PID + PEB + handles |
| config V | files + env | files + defaults | files + **registry** |
| driver cut | kernel modules | kext / dext | kernel vs user drivers |
| GUI | not in kernel | WindowServer | CSRSS / DWM |
| POSIX | native | BSD native | subsystem / WSL |

Same user hope (“run my program”). Three listed syscall alphabets. A portable language is a G that emits all three.

---

## Curiosity leftovers (what the nouns hid)

- Segment:offset and HANDLE and fd are three ways to isolate a kernel letter. The pointer glyph hid that.
- Event loop / message pump / epoll: three score-and-dispatch G on an event V.
- “App” is a compress of process + files + GUI isolate + installer μ.
- Permission: lock-G on a read (can this isolate write that path). Root/uid 0 / admin is lock off.
- Network socket booked as file on UNIX: two-reads (bytes and endpoints) under one noun. Windows SOCKET started as a different letter then converged in use.
- Mobile (iOS/Android): Darwin and Linux cuts with extra prune (no background write unless listed). The phone is not a new ontology.

---

## Build rule from this map

When you target “an OS,” name which V you emit (fd vs HANDLE, path vs registry).  
When you pick a language, name the θ clock.  
When you say portable, you owe three posts or a wrapper G.

The history is not progress toward a true container. It is thicker compressions on the same leak-relative-to-cut problem.
