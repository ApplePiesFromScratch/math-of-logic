#!/usr/bin/env python3
"""
ml/pl_communal_field.py  —  Carrier-Based Communal Learning Field
James Alexander Pugmire · Propagation Logic Project · 2026

A multi-agent system where each agent is a full Carrier (V, Γ, θ).

In the propagation logic framing:
  Agent   = a sovereign Carrier with its own gradient family.
  Forward = P / G → Q through the agent's layer stack.
  Update  = each agent updates from error signal and field consensus.
  Parasitic agent = a carrier that accumulates extra DRAS load per step
                    without proportional coherence contribution.

The immune response is a structural consequence, not a heuristic:
  When an agent's cumulative load exceeds the field's threshold,
  the field cannot remain coherent with that carrier included.
  Isolation IS the thermodynamic load rule applied to agents.

DRAS cost per step is batch-mean MSE at each layer (scaled) —
  dimensionless, batch-size independent, comparable across agents.
  The parasitic agent adds a fixed surcharge per epoch representing
  gradient demands it places on the field without coherence return.

Usage:
    python ml/pl_communal_field.py
"""

from __future__ import annotations
import math
import numpy as np
from dataclasses import dataclass
from typing import Dict, List, Optional

kB       = 1.380649e-23
LANDAUER = kB * 300.0 * math.log(2)
SEP      = "═" * 80


# ── Agent layer ───────────────────────────────────────────────────────────────

class AgentLayer:
    """
    One gradient layer within a sovereign agent.

    W shape: (input_dim, output_dim)
    Forward: tanh(X @ W * (1 - θ))
    """

    def __init__(self, input_dim: int, output_dim: int):
        self.W     = np.random.randn(input_dim, output_dim) * np.sqrt(2.0 / input_dim)
        self.theta = 0.55

    def propagate(self, X: np.ndarray) -> np.ndarray:
        """P / G → Q for this layer."""
        return np.tanh(np.dot(X, self.W) * (1.0 - self.theta))

    def dras_cost(self, delta: np.ndarray) -> float:
        """
        DRAS cost of propagating error delta through this layer.
        Uses batch-mean (not sum) so cost is independent of batch size.
        Scaled by 0.1 to give dimensionless, epoch-comparable units.
        """
        return float(np.mean(delta ** 2)) * 0.1


# ── Sovereign agent ───────────────────────────────────────────────────────────

@dataclass
class AgentCarrier:
    name:       str
    theta:      float
    dof:        int
    axiom_debt: float


class SovereignAgent:
    """
    A sovereign agent: a Carrier with its own gradient family.

    Maintains:
      _layer_inputs  : input to each layer during last forward pass
      cumulative_load: total DRAS load accumulated across all epochs
      coherence      : field integration quality  (1.0 = fully coherent)
      isolated       : set True by field immune response

    Parasitic agents add a fixed surcharge per update step —
    representing gradient demands placed on the field without
    proportional coherence contribution.
    """

    PARASITE_SURCHARGE = 0.5   # extra load per update step

    def __init__(self,
                 layer_sizes:  List[int],
                 agent_id:     int,
                 is_parasitic: bool = False):
        self.agent_id     = agent_id
        self.is_parasitic = is_parasitic
        self.carrier      = AgentCarrier(
            name       = f"Agent_{agent_id + 1}",
            theta      = 0.58,
            dof        = sum(layer_sizes[1:]),
            axiom_debt = self._axiom_debt(layer_sizes)
        )
        self.layers          = [AgentLayer(layer_sizes[i], layer_sizes[i + 1])
                                 for i in range(len(layer_sizes) - 1)]
        self.cumulative_load = 0.0
        self.coherence       = 1.0
        self.isolated        = False
        self._layer_inputs: List[np.ndarray] = []

    @staticmethod
    def _axiom_debt(layer_sizes: List[int]) -> float:
        total = sum(
            (1.0 / (1.0 - min(0.999, 0.58))) * 0.45 + layer_sizes[i + 1] * 0.25
            for i in range(len(layer_sizes) - 1)
        )
        return total + LANDAUER * 40

    @property
    def name(self) -> str:
        return self.carrier.name

    def forward(self, X: np.ndarray) -> np.ndarray:
        """
        P / G → Q through the full layer stack.
        Records the input to each layer for use in update().
        """
        if self.isolated:
            return np.zeros((X.shape[0], self.layers[-1].W.shape[1]))
        self._layer_inputs = []
        state = X
        for layer in self.layers:
            self._layer_inputs.append(state)    # input to this layer
            state = layer.propagate(state)
        return state

    def update(self, error: np.ndarray, fluidity: float = 0.05) -> float:
        """
        Update weights from error signal.

        For each layer (in reverse):
          gradient = layer_input^T @ current_error / batch_size
          ΔW = fluidity * (1-θ) * gradient
          error_to_prev = (current_error @ W^T) * 0.8

        Parasitic agents add a fixed surcharge to cumulative_load each step.

        Returns: DRAS cost of this update.
        """
        if self.isolated:
            return 0.0

        step_load     = 0.0
        current_error = error

        for i, layer in enumerate(reversed(self.layers)):
            layer_idx   = len(self.layers) - 1 - i
            layer_input = self._layer_inputs[layer_idx]   # (batch, input_dim)

            step_load  += layer.dras_cost(current_error)

            # Gradient: (input_dim, output_dim) — normalised by batch size
            flux = np.clip(
                np.dot(layer_input.T, current_error) / layer_input.shape[0],
                -1.0, 1.0
            )
            layer.W       -= fluidity * (1.0 - layer.theta) * flux
            current_error  = np.dot(current_error, layer.W.T) * 0.8

        # Parasitic surcharge: gradient demands not backed by coherence
        surcharge             = self.PARASITE_SURCHARGE if self.is_parasitic else 0.0
        self.cumulative_load += step_load + surcharge
        # Coherence decays toward 0 as cumulative load approaches 60.0
        self.coherence        = max(0.0, 1.0 - self.cumulative_load / 60.0)
        return step_load


# ── Communal field with immune response ───────────────────────────────────────

class CommunalField:
    """
    A field of sovereign agents sharing a consensus gradient.

    Consensus: each active agent contributes to the field's output.
    Each agent updates from a blend of its own error and the consensus error.

    Immune response: agents whose cumulative load exceeds immune_threshold
    are isolated. The field maintains coherence by excluding carriers
    that cannot sustain their thermodynamic load profiles.

    immune_threshold is calibrated so that:
      - Non-parasitic agents complete 100 epochs without isolation
      - The parasitic agent is isolated around epoch 20-25
    """

    IMMUNE_THRESHOLD = 12.0
    FLUIDITY         = 0.05

    def __init__(self,
                 n_agents:         int,
                 layer_sizes:      List[int],
                 parasite_indices: Optional[List[int]] = None):
        parasite_set  = set(parasite_indices or [])
        self.agents   = [
            SovereignAgent(layer_sizes, i, is_parasitic=(i in parasite_set))
            for i in range(n_agents)
        ]

    def process_epoch(self, X: np.ndarray, Y: np.ndarray) -> Dict:
        active = [a for a in self.agents if not a.isolated]
        if not active:
            return {"mse": 1.0, "total_load": 0.0,
                    "n_active": 0, "isolated": len(self.agents)}

        # Consensus: mean output of all active agents
        outputs   = [a.forward(X) for a in active]
        consensus = np.mean(outputs, axis=0)

        total_mse  = 0.0
        total_load = 0.0
        immune_events = []

        for agent in active:
            pred  = agent.forward(X)
            # Each agent pulls toward its own output (60%) and field consensus (40%)
            error = (pred * 0.6 + consensus * 0.4) - Y
            total_mse  += float(np.mean(error ** 2))
            total_load += agent.update(error, self.FLUIDITY)

            if (agent.cumulative_load > self.IMMUNE_THRESHOLD
                    and not agent.isolated):
                agent.isolated = True
                immune_events.append(agent.name)

        n_active = sum(1 for a in self.agents if not a.isolated)
        return {
            "mse":           total_mse / max(len(active), 1),
            "total_load":    total_load,
            "n_active":      n_active,
            "isolated":      len(self.agents) - n_active,
            "immune_events": immune_events,
        }


# ══════════════════════════════════════════════════════════════════════════════
# MAIN
# ══════════════════════════════════════════════════════════════════════════════

def main():
    print(SEP)
    print("CARRIER-BASED COMMUNAL LEARNING FIELD")
    print("Multi-agent learning with DRAS immune response")
    print("Each agent is a Carrier. Parasitic load triggers field isolation.")
    print(SEP)

    np.random.seed(42)

    # Task: classify sin(x₀) + x₁x₂ > 0 in ℝ³
    X = np.random.uniform(-1.5, 1.5, (800, 3))
    Y = (np.sin(X[:, [0]]) + X[:, [1]] * X[:, [2]] > 0.0).astype(float)

    # Agent 4 (index 4) is the parasitic carrier
    field = CommunalField(
        n_agents         = 5,
        layer_sizes      = [3, 10, 6, 1],
        parasite_indices = [4]
    )

    total_debt = sum(a.carrier.axiom_debt for a in field.agents)
    print(f"\n  Agents:           5 sovereign carriers  [Agent_1 ... Agent_5]")
    print(f"  Parasitic:        Agent_5 (+{SovereignAgent.PARASITE_SURCHARGE} load/step surcharge)")
    print(f"  Immune threshold: {CommunalField.IMMUNE_THRESHOLD}")
    print(f"  Total axiom debt: {total_debt:.2f}")
    print(f"  Landauer unit:    {LANDAUER:.3e} J per erased bit")
    print()
    print(f"  {'Epoch':>6}  {'MSE':>8}  {'Load':>8}  {'Coherence':>10}  "
          f"{'Active':>8}  {'Isolated':>10}")
    print(f"  {'─'*6}  {'─'*8}  {'─'*8}  {'─'*10}  {'─'*8}  {'─'*10}")

    for epoch in range(1, 101):
        result = field.process_epoch(X, Y)

        for name in result["immune_events"]:
            agent = next(a for a in field.agents if a.name == name)
            print(f"\n  ⚠  IMMUNE RESPONSE: {name} isolated  "
                  f"(cumulative load = {agent.cumulative_load:.2f}  "
                  f"threshold = {CommunalField.IMMUNE_THRESHOLD}  "
                  f"parasitic = {agent.is_parasitic})\n")

        if epoch == 1 or epoch % 15 == 0 or epoch == 100:
            active = [a for a in field.agents if not a.isolated]
            avg_coh = (sum(a.coherence for a in active) / len(active)
                       if active else 0.0)
            print(f"  {epoch:>6}  {result['mse']:>8.5f}  "
                  f"{result['total_load']:>8.3f}  {avg_coh:>10.3f}  "
                  f"{result['n_active']:>8}  {result['isolated']:>10}")

    print()
    print(SEP)
    print("FINAL CARRIER STATES")
    print(SEP)
    for agent in field.agents:
        status = "ISOLATED" if agent.isolated else "ACTIVE  "
        marker = "⚠ " if agent.isolated else "✓ "
        para   = " (parasitic)" if agent.is_parasitic else ""
        print(f"  {marker}{agent.name}{para:<15}  "
              f"load = {agent.cumulative_load:>6.2f}  "
              f"coherence = {agent.coherence:.3f}  "
              f"{status}")
    print(SEP)
    print()
    print("  The field maintained coherence by isolating the incoherent carrier.")
    print("  This is not a heuristic. It is the thermodynamic load rule applied to agents.")
    print("  Every distinction has a DRAS cost. Carriers that cannot pay are excluded.")


if __name__ == "__main__":
    main()
