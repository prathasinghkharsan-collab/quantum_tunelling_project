import numpy as np, matplotlib
matplotlib.use("Agg")  # ensures the file saves even if no window opens
import matplotlib.pyplot as plt, os

# Make sure results folder exists
os.makedirs("results", exist_ok=True)

# --- Physics constants (arbitrary realistic values) ---
V0 = 5e-14        # Barrier height (J)
a = 1e-14         # Barrier width (m)
m = 1.67e-27      # Proton mass (kg)
hbar = 1.054e-34

# --- Energy range (J) ---
E = np.linspace(1e-15, 8e-14, 400)

# --- Tunnelling probability formula (rectangular barrier) ---
T = np.exp(-2 * a * np.sqrt(2 * m * np.maximum(V0 - E, 0)) / hbar)

# --- Plot ---
plt.figure(figsize=(8,5))
plt.plot(E*1e14, T, lw=2, color="royalblue")
plt.title("Quantum Tunnelling Probability vs Energy (Fusion Relation)")
plt.xlabel("Energy ×10⁻¹⁴ J")
plt.ylabel("Tunnelling Probability")
plt.grid(True, ls="--", alpha=0.6)
plt.tight_layout()

# --- Save image ---
output_path = os.path.join("results", "fusion_TE_plot.png")
plt.savefig(output_path, dpi=200)
print("✅ Fusion tunnelling plot saved as:", output_path)
