# fusion_TE_plot.py
import numpy as np
import matplotlib
matplotlib.use("Agg")   # ensures it saves even without GUI
import matplotlib.pyplot as plt
import os

# make sure results folder exists
os.makedirs("results", exist_ok=True)

# -----------------------------
# Physical parameters (arbitrary but realistic)
# -----------------------------
V0 = 5.0e-14       # barrier height (J)
a = 1e-14          # barrier width (m)
m = 1.67e-27       # proton mass (kg)
hbar = 1.054e-34

# -----------------------------
# Energy range (Joules)
# -----------------------------
E = np.linspace(1e-15, 8e-14, 400)

# -----------------------------
# Tunnelling probability formula
# -----------------------------
# Transmission coefficient (simplified rectangular barrier)
T = np.exp(-2 * a * np.sqrt(2 * m * np.maximum(V0 - E, 0)) / hbar)

# -----------------------------
# Plot setup
# -----------------------------
plt.figure(figsize=(8, 5))
plt.plot(E * 1e14, T, color="royalblue", lw=2, label="Tunnelling Probability")
plt.title("Quantum Tunnelling Probability vs Energy\n(Nuclear Fusion Connection)")
plt.xlabel("Particle Energy (×10⁻¹⁴ Joules)")
plt.ylabel("Tunnelling Probability (T)")
plt.grid(True, linestyle="--", alpha=0.6)

# Add annotation
plt.text(4.5, 0.2,
         "Higher Energy → Higher Tunnelling\n→ Easier Nuclear Fusion",
         fontsize=10, color="firebrick", bbox=dict(facecolor='white', alpha=0.7, edgecolor='none'))

plt.legend()

# -----------------------------
# Save the plot
# -----------------------------
output_path = os.path.join("results", "fusion_TE_plot.png")
plt.tight_layout()
plt.savefig(output_path, dpi=300)
print(f"✅ Fusion tunnelling plot saved as: {output_path}")
