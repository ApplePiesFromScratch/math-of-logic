#!/usr/bin/env python3
"""
ml/pl_communal_field.py  —  Carrier-Based Communal Learning Field
James Alexander Pugmire · Propagation Logic Project · 2026

Multi-agent field where gradient classification is emergent.

No agent is declared parasitic. Classification — SYMBIOTIC, NEUTRAL, PARASITIC —
emerges from each agent's gradient history relative to available field gradients.

Gradient classification:
  contribution = how much agent reduces field MSE vs consensus
  demand       = DRAS load the agent places on the field
  ratio        = contribution / demand  (exponential moving average over time)

  SYMBIOTIC:  ratio persistently above field mean  — finding patterns others miss
  NEUTRAL:    ratio ≈ field mean                   — learning similar patterns
  PARASITIC:  ratio persistently below field mean  — taking more than giving

Classification drives:
  - Immune threshold (per-agent, dynamic)
  - Genetic weight at child spawning
  - Energy redistribution on death

Death-birth cycle:
  When an agent is isolated:
    1. Its cumulative load is partially recovered as field energy (Landauer dissipation)
    2. Surviving agents' weights are averaged, weighted by coherence × gradient class
    3. When energy pool exceeds spawn threshold, a child agent is born
    4. Child inherits consensus genetics + noise scaled by recovered energy
    5. Child starts at L=0 — the seed state

Usage:
    python ml/pl_communal_field.py
"""

from __future__ import annotations
import math
import numpy as np
from dataclasses import dataclass, field
from enum import Enum, auto
from typing import Dict, List, Optional, Tuple

kB       = 1.380649e-23
LANDAUER = kB * 300.0 * math.log(2)
SEP      = "═" * 80
SUB      = "─" * 80


# ══════════════════════════════════════════════════════════════════════════════
# GRADIENT CLASSIFICATION
# ══════════════════════════════════════════════════════════════════════════════

class GradientClass(Enum):
    SYMBIOTIC = "SYMBIOTIC"
    NEUTRAL   = "NEUTRAL"
    PARASITIC = "PARASITIC"

    def marker(self) -> str:
        return {"SYMBIOTIC": "↑", "NEUTRAL": "·", "PARASITIC": "↓"}[self.value]

    def immune_multiplier(self) -> float:
        """Symbiotic agents get more leeway; parasitic agents hit threshold sooner."""
        return {"SYMBIOTIC": 1.6, "NEUTRAL": 1.0, "PARASITIC": 0.6}[self.value]

    def genetic_weight(self) -> float:
        """How much this class contributes to child genetics."""
        return {"SYMBIOTIC": 1.5, "NEUTRAL": 1.0, "PARASITIC": 0.4}[self.value]


@dataclass
class GradientProfile:
    """
    An agent's gradient history relative to available field gradients.

    ema     : exponential moving average of (contribution/demand) / field_mean_ratio
    klass   : current classification
    history : list of (epoch, class, ema) for tracking lineage
    """
    ema:     float         = 0.5
    klass:   GradientClass = GradientClass.NEUTRAL
    history: List          = field(default_factory=list)
    _alpha:  float         = 0.15   # EMA decay

    def update(self, contribution: float, demand: float,
               field_mean_ratio: float, epoch: int):
        ratio    = contribution / (demand + 1e-8)
        relative = ratio / (field_mean_ratio + 1e-8)
        self.ema = self._alpha * relative + (1.0 - self._alpha) * self.ema

        prev = self.klass
        if self.ema > 1.25:
            self.klass = GradientClass.SYMBIOTIC
        elif self.ema < 0.75:
            self.klass = GradientClass.PARASITIC
        else:
            self.klass = GradientClass.NEUTRAL

        if self.klass != prev or epoch % 10 == 0:
            self.history.append((epoch, self.klass.value, round(self.ema, 3)))


# ══════════════════════════════════════════════════════════════════════════════
# AGENT LAYER
# ══════════════════════════════════════════════════════════════════════════════

class AgentLayer:
    def __init__(self, input_dim: int, output_dim: int):
        self.W     = np.random.randn(input_dim, output_dim) * np.sqrt(2.0 / input_dim)
        self.theta = 0.55

    def propagate(self, X: np.ndarray) -> np.ndarray:
        return np.tanh(np.dot(X, self.W) * (1.0 - self.theta))

    def dras_cost(self, delta: np.ndarray) -> float:
        return float(np.mean(delta ** 2)) * 0.1


# ══════════════════════════════════════════════════════════════════════════════
# SOVEREIGN AGENT
# ══════════════════════════════════════════════════════════════════════════════

class SovereignAgent:
    """
    A sovereign carrier with emergent gradient classification.
    No agent is declared parasitic — classification emerges from dynamics.
    """

    def __init__(self, layer_sizes: List[int], agent_id: int, generation: int = 0):
        self.agent_id        = agent_id
        self.generation      = generation
        self.name            = f"Agent_{agent_id}g{generation}"
        self.layers          = [AgentLayer(layer_sizes[i], layer_sizes[i+1])
                                 for i in range(len(layer_sizes) - 1)]
        self.profile         = GradientProfile()
        self.cumulative_load = 0.0
        self.coherence       = 1.0
        self.isolated        = False
        self._inputs:  List  = []
        # Per-epoch metrics (set by field)
        self.last_contribution = 0.0
        self.last_demand       = 0.0

    def forward(self, X: np.ndarray) -> np.ndarray:
        if self.isolated:
            return np.zeros((X.shape[0], self.layers[-1].W.shape[1]))
        self._inputs = []
        state = X
        for layer in self.layers:
            self._inputs.append(state)
            state = layer.propagate(state)
        return state

    def update(self, error: np.ndarray, fluidity: float = 0.05) -> float:
        if self.isolated:
            return 0.0
        step_load     = 0.0
        current_error = error
        for i, layer in enumerate(reversed(self.layers)):
            idx         = len(self.layers) - 1 - i
            inp         = self._inputs[idx]
            step_load  += layer.dras_cost(current_error)
            flux        = np.clip(np.dot(inp.T, current_error) / inp.shape[0], -1.0, 1.0)
            layer.W    -= fluidity * (1.0 - layer.theta) * flux
            current_error = np.dot(current_error, layer.W.T) * 0.8
        self.cumulative_load += step_load
        self.coherence        = max(0.0, 1.0 - self.cumulative_load / 60.0)
        self.last_demand      = step_load
        return step_load

    def effective_threshold(self, base: float) -> float:
        return base * self.profile.klass.immune_multiplier()


# ══════════════════════════════════════════════════════════════════════════════
# COMMUNAL FIELD WITH DEATH-BIRTH CYCLE
# ══════════════════════════════════════════════════════════════════════════════

class CommunalField:
    """
    Field of sovereign agents with:
      - Emergent gradient classification (SYMBIOTIC / NEUTRAL / PARASITIC)
      - Dynamic immune threshold per agent based on gradient class
      - Death-birth cycle: dead agent's load → energy pool → child agent
      - Genetic inheritance: coherence × gradient-class weighted consensus weights
      - Child noise: scaled by recovered energy (more energy = more exploration)
    """

    BASE_THRESHOLD = 12.0
    RECOVERY_RATE  = 0.70    # fraction of dead agent's load recovered
    MUTATION_BASE  = 0.02    # base weight noise for child
    SPAWN_THRESHOLD = 4.0    # energy pool needed to spawn

    def __init__(self, n_agents: int, layer_sizes: List[int]):
        self.layer_sizes = layer_sizes
        self.agents      = [SovereignAgent(layer_sizes, i) for i in range(n_agents)]
        self.energy_pool = 0.0
        self._next_id    = n_agents
        self.births:  List[dict] = []
        self.deaths:  List[dict] = []

    # ── Gradient classification ────────────────────────────────────────────

    def _classify_all(self, epoch: int):
        """Update all agents' gradient profiles relative to field mean ratio."""
        active = [a for a in self.agents if not a.isolated]
        if len(active) < 2:
            return

        ratios = [a.last_contribution / (a.last_demand + 1e-8) for a in active]
        field_mean = sum(ratios) / len(ratios)

        for agent in active:
            agent.profile.update(
                agent.last_contribution,
                agent.last_demand,
                field_mean,
                epoch
            )

    # ── Death and harvest ──────────────────────────────────────────────────

    def _harvest(self, dead: SovereignAgent) -> float:
        recovered = dead.cumulative_load * self.RECOVERY_RATE
        self.energy_pool += recovered
        self.deaths.append({
            "agent":     dead.name,
            "class":     dead.profile.klass.value,
            "load":      dead.cumulative_load,
            "recovered": recovered,
        })
        return recovered

    # ── Genetics and spawning ──────────────────────────────────────────────

    def _genetics(self, survivors: List[SovereignAgent]) -> List[np.ndarray]:
        """
        Coherence × gradient-class weighted average of survivor weight matrices.
        Symbiotic agents contribute more to child genetics.
        Parasitic agents contribute less (their history carries less useful gradient).
        """
        raw = [a.coherence * a.profile.klass.genetic_weight() for a in survivors]
        total = sum(raw) + 1e-8
        weights = [r / total for r in raw]

        return [
            sum(w * a.layers[i].W for w, a in zip(weights, survivors))
            for i in range(len(survivors[0].layers))
        ]

    def _spawn(self, survivors: List[SovereignAgent], epoch: int) -> SovereignAgent:
        """
        Spawn child from field genetics.
        Noise scaled by energy pool — more energy → more exploration.
        Child starts at L=0 (seed state).
        """
        genetics     = self._genetics(survivors)
        noise_scale  = self.MUTATION_BASE * (self.energy_pool / self.BASE_THRESHOLD)
        generation   = max(a.generation for a in survivors) + 1

        child = SovereignAgent(self.layer_sizes, self._next_id, generation)
        self._next_id += 1

        for i, layer in enumerate(child.layers):
            layer.W = genetics[i] + np.random.randn(*genetics[i].shape) * noise_scale

        # Energy consumed by birth (Landauer cost of new distinction structure)
        consumed          = self.energy_pool * 0.70
        self.energy_pool -= consumed

        self.agents.append(child)
        parent_names = [a.name for a in survivors]
        self.births.append({
            "child":         child.name,
            "generation":    generation,
            "epoch":         epoch,
            "parents":       parent_names,
            "energy_used":   consumed,
            "noise_scale":   noise_scale,
        })
        return child

    # ── Main epoch ────────────────────────────────────────────────────────

    def process_epoch(self, X: np.ndarray, Y: np.ndarray,
                      epoch: int = 0) -> Dict:
        active = [a for a in self.agents if not a.isolated]
        if not active:
            return {"mse": 1.0, "n_active": 0, "events": []}

        # Forward + consensus
        preds     = [a.forward(X) for a in active]
        consensus = np.mean(preds, axis=0)
        consensus_mse = float(np.mean((consensus - Y) ** 2))

        events    = []
        total_mse = 0.0

        for agent in active:
            pred      = agent.forward(X)
            agent_mse = float(np.mean((pred - Y) ** 2))
            total_mse += agent_mse

            # Contribution: how much better than consensus (0-clipped)
            agent.last_contribution = max(0.0, consensus_mse - agent_mse)

            # Blended error signal
            error = (pred * 0.6 + consensus * 0.4) - Y
            agent.update(error, fluidity=0.05)

            # Dynamic immune threshold based on gradient class
            if agent.cumulative_load > agent.effective_threshold(self.BASE_THRESHOLD):
                agent.isolated = True
                recovered = self._harvest(agent)
                events.append(f"DEATH  {agent.name} [{agent.profile.klass.value}] "
                              f"load={agent.cumulative_load:.2f} "
                              f"→ recovered {recovered:.2f} to pool")

        # Classify all agents relative to field gradient distribution
        self._classify_all(epoch)

        # Spawn child if energy pool is sufficient
        survivors = [a for a in self.agents if not a.isolated]
        if self.energy_pool >= self.SPAWN_THRESHOLD and len(survivors) >= 1:
            child = self._spawn(survivors, epoch)
            events.append(f"BIRTH  {child.name} gen={child.generation} "
                          f"noise={self.births[-1]['noise_scale']:.4f} "
                          f"pool→{self.energy_pool:.2f}")

        n_active = sum(1 for a in self.agents if not a.isolated)
        return {
            "mse":      total_mse / max(len(active), 1),
            "n_active": n_active,
            "n_total":  len(self.agents),
            "pool":     self.energy_pool,
            "events":   events,
        }


# ══════════════════════════════════════════════════════════════════════════════
# MAIN
# ══════════════════════════════════════════════════════════════════════════════

def main():
    print(SEP)
    print("CARRIER-BASED COMMUNAL LEARNING FIELD")
    print("Emergent gradient classification: SYMBIOTIC · NEUTRAL · PARASITIC")
    print("Classification from loaded history relative to available field gradients")
    print(SEP)

    np.random.seed(42)
    X = np.random.uniform(-1.5, 1.5, (800, 3))
    Y = (np.sin(X[:, [0]]) + X[:, [1]] * X[:, [2]] > 0.0).astype(float)

    field = CommunalField(n_agents=5, layer_sizes=[3, 10, 6, 1])

    print(f"\n  5 agents | all start NEUTRAL | classification emerges from dynamics")
    print(f"  Base immune threshold: {CommunalField.BASE_THRESHOLD}")
    print(f"  Symbiotic threshold:   {CommunalField.BASE_THRESHOLD * 1.6:.1f}  (more leeway)")
    print(f"  Parasitic threshold:   {CommunalField.BASE_THRESHOLD * 0.6:.1f}  (less leeway)")
    print(f"  Recovery rate:         {CommunalField.RECOVERY_RATE*100:.0f}%  of dead agent's load")
    print(f"  Spawn threshold:       {CommunalField.SPAWN_THRESHOLD}")
    print()

    hdr = f"  {'Ep':>4}  {'MSE':>7}  {'Pool':>5}  {'N':>3}"
    hdr += "  " + "  ".join(f"{'A'+str(i):<12}" for i in range(5))
    print(hdr)
    print("  " + "─" * 100)

    for epoch in range(1, 121):
        result = field.process_epoch(X, Y, epoch)

        for ev in result["events"]:
            print(f"\n  ⚡ {ev}\n")

        if epoch == 1 or epoch % 10 == 0 or result["events"]:
            active = [a for a in field.agents if not a.isolated]
            row = f"  {epoch:>4}  {result['mse']:>7.4f}  {result['pool']:>5.2f}  {result['n_active']:>3}"
            # Show first 5 original agents
            for i in range(5):
                agents_with_id = [a for a in field.agents if a.agent_id == i]
                if agents_with_id:
                    a = agents_with_id[0]
                    if a.isolated:
                        row += f"  {'✗':<12}"
                    else:
                        marker = a.profile.klass.marker()
                        row += f"  {marker}{a.profile.klass.value[:3]} {a.profile.ema:.2f}  "
                else:
                    row += f"  {'—':<12}"
            print(row)

    print()
    print(SEP)
    print("FINAL FIELD STATE")
    print(SUB)
    for a in field.agents:
        status  = "ISOLATED" if a.isolated else "ACTIVE  "
        marker  = "⚠ " if a.isolated else "✓ "
        history = [f"{h[1][:3]}@{h[0]}" for h in a.profile.history[-3:]]
        print(f"  {marker}{a.name:<18} load={a.cumulative_load:>6.2f}  "
              f"coh={a.coherence:.3f}  [{a.profile.klass.value:<9}]  "
              f"ema={a.profile.ema:.3f}  {status}")
        if history:
            print(f"    gradient history: {' → '.join(history)}")

    print()
    print(f"  Energy pool:  {field.energy_pool:.2f}")
    print(f"  Total births: {len(field.births)}")
    print(f"  Total deaths: {len(field.deaths)}")

    if field.births:
        print()
        print("  Birth lineage:")
        for b in field.births:
            print(f"    {b['child']} (gen {b['generation']}) at epoch {b['epoch']}")
            print(f"      parents: {', '.join(b['parents'])}")
            print(f"      noise scale: {b['noise_scale']:.4f}  energy used: {b['energy_used']:.2f}")

    print(SUB)
    print("  Classification was not declared. It emerged from gradient history.")
    print("  The field maintained coherence through the thermodynamic load rule.")
    print("  Every distinction has a cost. Every death seeds the next generation.")
    print(SEP)


if __name__ == "__main__":
    main()
