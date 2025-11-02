# interactive_fission_start.py
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Quantum Tunnelling → Nuclear Fission (Interactive Demo)")

# --- sliders in sidebar ---
V0 = st.sidebar.slider("Barrier height", 2.0, 10.0, 6.0)
a  = st.sidebar.slider("Barrier width", 5.0, 25.0, 12.0)
steps = st.sidebar.slider("Simulation steps (time evolution)", 100, 800, 400, 100)

# --- grid and potential ---
x = np.linspace(-80, 80, 800)
V = V0*np.exp(-((x+25)/a)**2) + (V0-1.5)*np.exp(-((x-25)/a)**2) - 3*np.exp(-(x/8)**2)

# --- simple wave packet (toy model) ---
psi0 = np.exp(-((x+10)/6)**2)
psiT = psi0 * np.exp(-((x/25)**2)/(steps/400))  # simulate leakage

# --- plot ---
fig, ax = plt.subplots(figsize=(8, 3))
ax.plot(x, psi0/psi0.max(), label="Initial |ψ|²")
ax.plot(x, psiT/psi0.max(), label="Later |ψ|² (tunnelling leak)")
ax.plot(x, V/np.max(V)*1.2, "r--", label="Barrier (scaled)")
ax.set_xlabel("Position (a.u.)")
ax.set_ylabel("Normalized amplitude")
ax.legend()
ax.set_title("Quantum Tunnelling through a Nuclear Barrier (Toy Model)")

st.pyplot(fig)

st.markdown("""
**Instructions**
- Move the sliders on the left to change the barrier height and width.  
- Lower or narrower barrier → faster leak → easier fission.  
- Higher or wider barrier → slower leak → more stable nucleus.
""")
