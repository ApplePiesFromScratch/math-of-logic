# Game engines and physics engines

A game engine is isolate-tick + render-read.
A physics engine is a step-G on a listed world-V plus collision θ.

```
python3 phys.py
```

```
euler  40 steps dt=0.1  E 0.50 -> 0.74  leftover +0.244
verlet 40 steps dt=0.1  E~0.48         leftover -0.023
screen wrap 7.5+2 -> 1.5  host 9.5
```

Energy is not conserved by the noun “spring.” It is leftover of the integrator G.

---

## Shared cut

| slot | engine |
|---|---|
| tick | isolate a dt (fixed or frame) |
| body | letters: x, v, m, sometimes orientation |
| step G | Euler / semi-implicit / Verlet / RK4 / constraint solver |
| collision | two-body read; θ = contact manifold / TOI |
| render | project world-V onto pixel-V |
| scene / ECS | which letters exist this cut |

Fixed dt is a listed time-V. Variable frame-dt is host time; same G, leftover depends on seed (Heisenbug / desync).

---

## Integrators (combinators of the same meets)

Forward Euler: `x+=v dt`, `v+=a dt`. Cheap. Energy leak +0.244 here.
Semi-implicit Euler: v first, then x. Still one-way leftover.
Verlet: uses two x slots (mint of previous isolate). Energy leftover smaller (−0.023 with a v reconstructed after).
RK4: more reads per tick. Smoother on listed dt; still not R.

“Stability” = letters stay in the V you care about (bounded E, no NaN). Not a law of nature.

---

## Collision

Discrete: step then test. Tunneling = write skipped the contact-V (C3).
Continuous (TOI): extra G that isolates first time-of-impact. Cost for not leaking through a thin letter.
SAT / GJK: two reads of shape letters. SAT listed axes; GJK listed simplex. Both can θ “no overlap.”
Impulse / constraint / penalty: three combinators after contact. Penalty is a spring (energy leftover again). Impulse is a wrap-shaped jump in v. Constraint solver iterates leftover toward 0 (life support if you hide the residual).

Resting contact + float = buzz. IEEE leftover booked as physics.

---

## Engines as products

| name | cut |
|---|---|
| Box2D / Chipmunk | 2D, impulse, listed shapes |
| Bullet / PhysX / Havok | 3D, broadphase isolate + narrow G |
| Unity PhysX / Havok | scene + components; dt often frame-tied unless you lock |
| Unreal Chaos | constraint-heavy; network mint of bodies |
| Godot | separate 2D/3D V |
| custom platformer | wrap screen, AABB θ, often Euler |

Networked games: two mints of the same body (server / client). Val-eq is the lie. Lockstep = same seed + same G. Rollback = prune a cut and replay.

---

## Game engine around physics

Render: project. Camera is isolate. LOD is prune of maps the cut does not support.
Audio / input / UI: more isolates on the same tick or another.
GC / heap: prune. Spike = freeze (progress-read 0).
Shader: G on GPU tile-V (GEMM-cousin).
Script (C# / GDScript / Lua): late θ. A `null` is C9.

Pong: two wrap axes, AABB θ, v flip combinator. Listed and small. That is the honest core of most “physics.”

---

## Errors treated as weather

| name | mechanic |
|---|---|
| energy gain | Euler leftover |
| tunneling | discrete step leaves contact-V |
| jitter on sleep | float leftover vs constraint residual |
| desync | two compose-orders or two dt seeds |
| explode to Inf | MAC left IEEE |
| “just use smaller dt” | leftover → 0 at unlistable time-V |

Doctor: stamp integrator, lock dt, name energy leftover, continuous G if thin letters, θ Inf, two reads (gameplay feel vs conserved E).

---

## Cut box in a game

Post per tick (or per second): G=verlet, V=world box, E leftover, contacts θ count, dt mint.
A build that cannot name leftover is the same theater as Inf Isp.
