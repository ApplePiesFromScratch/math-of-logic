#!/usr/bin/env python3
"""Euler vs Verlet on a spring. Energy leftover is the engine."""
from __future__ import annotations


def energy(x, v, k=1.0, m=1.0):
    return 0.5 * m * v * v + 0.5 * k * x * x


def euler(x, v, dt, k=1.0, m=1.0):
    a = -k * x / m
    return x + v * dt, v + a * dt


def verlet(x, x_prev, dt, k=1.0, m=1.0):
    a = -k * x / m
    x_new = 2 * x - x_prev + a * dt * dt
    return x_new, x


def main():
    dt = 0.1
    steps = 40
    x, v = 1.0, 0.0
    e0 = energy(x, v)
    for _ in range(steps):
        x, v = euler(x, v, dt)
    print("euler E0", e0, "E", energy(x, v), "leftover", energy(x, v) - e0)

    x, xp = 1.0, 1.0  # v0=0 => x_prev=x
    for _ in range(steps):
        x, xp = verlet(x, xp, dt)
    v_approx = (x - xp) / dt
    print("verlet E0", e0, "E~", energy(x, v_approx), "leftover~", energy(x, v_approx) - e0)

    # wrap "screen" 0..8
    p = 7.5
    vel = 2.0
    p2 = (p + vel) % 8
    print("screen wrap", p, "+", vel, "->", p2, "host", p + vel)


if __name__ == "__main__":
    main()
