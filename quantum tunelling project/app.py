# app.py
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import os

# Set up the page
st.set_page_config(page_title="Quantum Tunnelling Project", layout="wide")

st.title("⚛️ Quantum Tunnelling in Nuclear Fission & Fusion")
st.markdown("""
Welcome to our interactive project demonstrating **Quantum Tunnelling**
and its connection to **Nuclear Fission** and **Fusion** processes for **clean energy**.

Use the sidebar to select which part of the project you’d like to explore.
""")

# Sidebar Navigation
choice = st.sidebar.radio(
    "Select Simulation:",
    ["Interactive Fission Simulation", "Fusion Tunnelling Plot", "Fission Demo Animation"]
)

# ===============================================================
# 1️⃣ INTERACTIVE FISSION SIMULATION
# ===============================================================
if choice == "Interactive Fission Simulation":
    st.header("🔹 Interactive Quantum Tunnelling → Fission Simulation")

    V0 = st.slider("Barrier height (V₀)", 2.0, 10.0, 6.0)
    a = st.slider("Barrier width (a)", 5.0, 25.0, 12.0)
    steps = st.slider("Simulation steps", 100, 800, 400, 100)

    x = np.linspace(-80, 80, 800)
    V = V0*np.exp(-((x+25)/a)**2) + (V0-1.5)*np.exp(-((x-25)/a)**2) - 3*np.exp(-(x/8)**2)

    psi0 = np.exp(-((x+10)/6)**2)
    psiT = psi0 * np.exp(-((x/25)**2)/(steps/400))

    fig, ax = plt.subplots(figsize=(8, 3))
    ax.plot(x, psi0/psi0.max(), label="Initial |ψ|²")
    ax.plot(x, psiT/psi0.max(), label="Later |ψ|² (leakage)")
    ax.plot(x, V/np.max(V)*1.2, "r--", label="Barrier (scaled)")
    ax.legend()
    ax.set_title("Quantum Tunnelling through Nuclear Barrier (Toy Fission Model)")
    st.pyplot(fig)

    st.info("""
    👉 Adjust the sliders to see how barrier **height** and **width**
    affect the probability of tunnelling (and hence nuclear fission).
    """)

# ===============================================================
# 2️⃣ FUSION TUNNELLING PROBABILITY PLOT
# ===============================================================
elif choice == "Fusion Tunnelling Plot":
    st.header("🔹 Fusion Tunnelling Probability vs Energy")

    V0 = 5e-14
    a = 1e-14
    m = 1.67e-27
    hbar = 1.054e-34
    E = np.linspace(1e-15, 8e-14, 400)

    T = np.exp(-2*a*np.sqrt(2*m*np.maximum(V0-E,0))/hbar)

    fig, ax = plt.subplots(figsize=(7,4))
    ax.plot(E*1e14, T, color='royalblue', lw=2)
    ax.set_xlabel("Particle Energy ×10⁻¹⁴ J")
    ax.set_ylabel("Tunnelling Probability (T)")
    ax.set_title("Quantum Tunnelling Probability vs Energy")
    ax.grid(True, ls="--", alpha=0.6)
    st.pyplot(fig)

    st.success("""
    ✅ As particle energy increases, tunnelling probability rises —  
    this explains **how nuclear fusion can occur** in stars and reactors.
    """)

# ===============================================================
# 3️⃣ FISSION DEMO VIDEO
# ===============================================================
elif choice == "Fission Demo Animation":
    st.header("🔹 Fission Tunnelling Animation Demo")

    result_path_mp4 = os.path.join("results", "fission_tunnelling_demo.mp4")
    result_path_gif = os.path.join("results", "fission_tunnelling_demo.gif")

    if os.path.exists(result_path_mp4):
        st.video(result_path_mp4)
        st.caption("MP4 Animation of Quantum Tunnelling → Fission Process")
    elif os.path.exists(result_path_gif):
        st.image(result_path_gif, caption="GIF Animation of Fission Tunnelling")
    else:
        st.warning("⚠️ No animation file found in results/. Please run fission_demo_small.py first.")

st.markdown("---")
st.markdown("👩‍💻 *Developed by [Your Name] and Team — Quantum Tunnelling Project, 2025*")
