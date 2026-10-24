
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

algorithms = ["Q-Learning", "SARSA", "Expected SARSA"]

seed_123 = [52.2, 57.6, 87.6]
seed_2026 = [45.8, 53.2, 82.8]

x = np.arange(len(algorithms))
width = 0.35

fig, ax = plt.subplots(figsize=(9, 5))

bars1 = ax.bar(
    x - width / 2, seed_123, width,
    label="Seed 123"
)

bars2 = ax.bar(
    x + width / 2, seed_2026, width,
    label="Seed 2026"
)

ax.set_ylabel("Zero-Torque Action Usage (%)")
ax.set_title("Learned Policy Behavior")
ax.set_xticks(x)
ax.set_xticklabels(algorithms)
ax.set_ylim(0, 105)
ax.legend()
ax.grid(axis="y", alpha=0.2)

ax.bar_label(bars1, fmt="%.1f%%", padding=3)
ax.bar_label(bars2, fmt="%.1f%%", padding=3)

plt.tight_layout()

output = Path("results/figures")
output.mkdir(parents=True, exist_ok=True)

plt.savefig(
    output / "04_zero_torque_usage.png",
    dpi=250,
    bbox_inches="tight"
)

plt.show()
