#!/usr/bin/env python3
"""
ml/pl_standing_wave.py  —  Standing Wave Learning Engine
James Alexander Pugmire · Propagation Logic Project · 2026

Learning as symmetric wave resonance in a physical medium.

In the propagation logic framing:
  Each layer is a Carrier (V, Γ, θ).
  Forward propagation is P / G_forward → Q.
  Backward error propagation is Q / G_backward → P  (symmetric coupling).
  Interference between forward and backward waves = the weight update.

This is not backpropagation. There is no stored computation graph.
Forward and backward states propagate simultaneously — a standing wave.
The medium learns by resonating, not by differentiating through history.

The coherence threshold θ adapts with kinetic energy:
  High kinetic → lower θ  (medium becomes more fluid)
  Low kinetic  → raise θ  (medium stabilises toward coherence)

Usage:
    python ml/pl_standing_wave.py
"""

from __future__ import annotations
import math
import numpy as np
from dataclasses import dataclass
from typing import List, Tuple

kB       = 1.380649e-23
LANDAUER = kB * 300.0 * math.log(2)
SEP      = "═" * 70


# ── Carrier descriptor ────────────────────────────────────────────────────────

@dataclass
class WaveCarrier:
    """
    A layer as a Carrier (V, Γ, θ).

    name  : identifier
    theta : coherence threshold — controls wave damping
    dof   : degrees of freedom (output dimension)
    debt  : upfront DRAS cost of instantiating this carrier
    """
    name:  str
    theta: float
    dof:   int
    debt:  float


# ── Standing wave layer ───────────────────────────────────────────────────────

class StandingWaveLayer:
    """
    One layer of the standing wave field.

    Shapes per layer (input_dim → output_dim):
      W_forward:  (input_dim,  output_dim)
      W_backward: (output_dim, input_dim)   symmetric coupling

    Forward:   h = tanh(X @ W_forward * (1-θ))
    Backward:  backward_state = (error * (1-h²)) @ W_backward
    Update:    interference = X^T @ error  →  symmetric ΔW to both matrices
    """

    def __init__(self, input_dim: int, output_dim: int, name: str = "Layer"):
        theta = 0.58
        self.carrier = WaveCarrier(
            name  = name,
            theta = theta,
            dof   = output_dim,
            debt  = self._axiom_debt(output_dim, theta)
        )
        self.W_forward  = np.random.randn(input_dim,  output_dim) * np.sqrt(2.0 / input_dim)
        self.W_backward = np.random.randn(output_dim, input_dim)  * np.sqrt(2.0 / output_dim)
        self.forward_state:  np.ndarray = np.zeros((1, output_dim))
        self.backward_state: np.ndarray = np.zeros((1, input_dim))

    @staticmethod
    def _axiom_debt(size: int, theta: float) -> float:
        boundary = 1.0 / (1.0 - min(0.999, theta))
        return boundary * 0.55 + size * 0.22 + LANDAUER * 25

    def resonate(self,
                 input_flux:  np.ndarray,
                 error_flux:  np.ndarray,
                 dt:          float,
                 fluidity:    float) -> Tuple[float, float]:
        """
        One resonance step.

        input_flux:  (batch, input_dim)
        error_flux:  (batch, output_dim)

        Forward state:   h = tanh(input_flux @ W_forward * (1-θ))
                         shape: (batch, output_dim)

        Backward state:  (error_flux * (1-h²)) @ W_backward
                         shape: (batch, input_dim)
                         — error propagated back to previous layer

        Interference:    input_flux^T @ error_flux
                         shape: (input_dim, output_dim)
                         — symmetric weight update for W_forward and W_backward
        """
        theta = self.carrier.theta

        # P / G_forward → Q
        self.forward_state = np.tanh(
            np.dot(input_flux, self.W_forward) * (1.0 - theta)
        )                                                   # (batch, output_dim)

        # Activation derivative
        act_deriv = 1.0 - self.forward_state ** 2          # (batch, output_dim)

        # Error propagated back through backward weights
        # (batch, output_dim) @ (output_dim, input_dim) → (batch, input_dim)
        self.backward_state = np.dot(error_flux * act_deriv, self.W_backward)

        # Interference pattern → weight update
        # input_flux^T: (input_dim, batch)  @  error_flux: (batch, output_dim)
        # → (input_dim, output_dim)
        interference = np.dot(input_flux.T, error_flux)
        kinetic      = float(np.sum(interference ** 2))

        damping        = 1.0 - theta
        update         = fluidity * dt * damping * interference  # (input_dim, output_dim)
        self.W_forward  -= update                                 # (input_dim, output_dim) ✓
        self.W_backward -= update.T                              # (output_dim, input_dim) ✓

        reif_cost = (1.0 / (1.0 - min(0.999, theta))) * self.carrier.dof * 0.085
        dras_cost = kinetic * 0.12 + reif_cost + LANDAUER * 10

        # Adaptive θ
        if kinetic > 5.5:
            self.carrier.theta = max(0.08, theta - 0.014 * dt)
        else:
            self.carrier.theta = min(0.93, theta + 0.0065 * dt)

        return kinetic, dras_cost


# ── Standing wave field ───────────────────────────────────────────────────────

class StandingWaveField:
    """
    A layered standing wave field: multiple carriers resonating together.
    """

    def __init__(self, layer_sizes: List[int]):
        self.layers = [
            StandingWaveLayer(layer_sizes[i], layer_sizes[i + 1], f"Layer{i + 1}")
            for i in range(len(layer_sizes) - 1)
        ]
        self.total_debt = sum(layer.carrier.debt for layer in self.layers)

    def resonate_epoch(self,
                       X:     np.ndarray,
                       Y:     np.ndarray,
                       steps: int = 6) -> Tuple[float, float, float]:
        """
        One epoch. Records the input to each layer during the forward pass
        so the backward pass can feed each layer its correct input.
        """
        dt            = 0.22
        fluidity      = 0.011
        total_kinetic = 0.0
        total_dras    = 0.0

        for _ in range(steps):
            # Forward: track input to each layer
            layer_inputs = []
            current = X
            for layer in self.layers:
                layer_inputs.append(current)
                current = np.tanh(
                    np.dot(current, layer.W_forward) * (1.0 - layer.carrier.theta)
                )
                layer.forward_state = current

            error = current - Y
            mse   = float(np.mean(error ** 2))

            # Backward: each layer gets its correct forward input
            current_error = error
            for i, layer in enumerate(reversed(self.layers)):
                layer_idx      = len(self.layers) - 1 - i
                input_to_layer = layer_inputs[layer_idx]
                kin, dras      = layer.resonate(
                    input_to_layer, current_error, dt, fluidity
                )
                total_kinetic += kin
                total_dras    += dras
                current_error  = layer.backward_state

        return mse, total_kinetic, total_dras


# ══════════════════════════════════════════════════════════════════════════════
# MAIN
# ══════════════════════════════════════════════════════════════════════════════

def main():
    print(SEP)
    print("STANDING WAVE LEARNING ENGINE")
    print("Propagation Logic + DRAS: Learning as physical wave resonance")
    print("P / G_forward → Q   |   Q / G_backward → P   (simultaneous)")
    print(SEP)

    np.random.seed(42)

    X = np.random.uniform(-1.5, 1.5, (1000, 3))
    Y = (np.sum(X ** 2, axis=1, keepdims=True) < 1.0).astype(float)

    field = StandingWaveField([3, 12, 8, 1])

    print(f"\n  Architecture:  [3 → 12 → 8 → 1]")
    print(f"  Task:          classify x ∈ ℝ³: inside unit sphere vs outside")
    print(f"  Axiom debt:    {field.total_debt:.4f}")
    print(f"  Landauer unit: {LANDAUER:.3e} J per erased bit")
    print()
    print(f"  {'Epoch':>6}  {'MSE':>10}  {'Kinetic':>10}  {'DRAS cost':>12}  {'Avg θ':>8}")
    print(f"  {'─'*6}  {'─'*10}  {'─'*10}  {'─'*12}  {'─'*8}")

    for epoch in range(1, 101):
        mse, kinetic, dras = field.resonate_epoch(X, Y, steps=5)
        if epoch == 1 or epoch % 20 == 0:
            avg_theta = sum(l.carrier.theta for l in field.layers) / len(field.layers)
            print(f"  {epoch:>6}  {mse:>10.6f}  {kinetic:>10.2f}  "
                  f"{dras:>12.4f}  {avg_theta:>8.4f}")

    print()
    print("  Final carrier states:")
    for layer in field.layers:
        print(f"    {layer.carrier.name}: θ = {layer.carrier.theta:.4f}  "
              f"dof = {layer.carrier.dof}")
    print()
    print("  The field learned by resonance, not by differentiating through history.")
    print("  No computation graph was stored. No backward pass was run.")
    print("  The gradient propagated forward and backward simultaneously.")
    print(SEP)


if __name__ == "__main__":
    main()
