import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# === Read data from C++ output ===
data = pd.read_csv("points.csv", header=None, names=["x", "y"])
x = data["x"].values
y = data["y"].values

# === Classify points ===
inside = (x**2 + y**2) <= 1.0
n_inside = inside.sum()
n_total = len(x)
ratio = n_inside / n_total
pi_est = 4 * ratio

# === Plot ===
fig, ax = plt.subplots(figsize=(7, 7), dpi=120)

# Points: inside (yellow), outside (red)
ax.scatter(x[inside], y[inside], s=10, color="yellow", edgecolors="none", label="Inside (≤1)")
ax.scatter(x[~inside], y[~inside], s=10, color="red", edgecolors="none", label="Outside (>1)")

# Quarter-circle boundary
theta = np.linspace(0, np.pi / 2, 400)
ax.plot(np.cos(theta), np.sin(theta), "k--", lw=2, label="Quarter circle (r=1)")

# Layout and labels
ax.set_title("Monte Carlo π Visualization", fontsize=14, pad=12)
ax.set_xlabel("x", fontsize=12)
ax.set_ylabel("y", fontsize=12)
ax.set_aspect("equal", adjustable="box")
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.grid(True, linestyle="--", alpha=0.3)

# Add stats text box
text = (
    f"Points inside: {n_inside}\n"
    f"Points total: {n_total}\n"
    f"Ratio (inside/total): {ratio:.6f}\n"
    f"π estimate = 4×ratio = {pi_est:.6f}"
)
ax.text(
    0.02, 0.98, text,
    transform=ax.transAxes,
    fontsize=11,
    va="top",
    bbox=dict(boxstyle="round,pad=0.5", facecolor="white", alpha=0.9, edgecolor="#cccccc")
)

# Legend and display
ax.legend(loc="lower left", frameon=True)
plt.tight_layout()
plt.savefig("monte_carlo.png")
#plt.show()

