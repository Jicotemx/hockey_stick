import streamlit as st
import matplotlib.pyplot as plt
from math import comb

def pascal_triangle(filas):
    """Genera el triángulo de Pascal hasta la fila indicada."""
    tri = []
    for n in range(filas):
        fila = [comb(n, k) for k in range(n+1)]
        tri.append(fila)
    return tri

def plot_hockey_stick(filas, r, longitud):
    """Dibuja el triángulo de Pascal con el palo de hockey."""
    n = r + longitud - 1  # calcular fila final del mango
    tri = pascal_triangle(filas)
    fig, ax = plt.subplots(figsize=(10,6))
    ax.axis("off")

    # Dibujar triángulo
    for i, fila in enumerate(tri):
        for j, val in enumerate(fila):
            ax.text(j - i/2, -i, str(val), ha="center", va="center", fontsize=12)

    # Mango del palo
    stick_coords = [(k, r) for k in range(r, n+1)]
    # Punta del palo
    punta_coord = (n+1, r+1) if n+1 < filas else None

    # Dibujar mango azul
    for (i,j) in stick_coords:
        ax.text(j - i/2, -i, str(tri[i][j]),
                ha="center", va="center", fontsize=12,
                color="blue", fontweight="bold")

    # Dibujar punta roja
    if punta_coord:
        pf, pc = punta_coord
        ax.text(pc - pf/2, -pf, str(tri[pf][pc]),
                ha="center", va="center", fontsize=12,
                color="red", fontweight="bold")

    # Ajustar límites
    ax.set_xlim(-filas/2 - 1, filas/2 + 1)
    ax.set_ylim(-filas - 1, 1)
    return fig

# =====================
# Interfaz Streamlit
# =====================
st.set_page_config(page_title="Identidad del palo de hockey", layout="centered")
st.title("Identidad del palo de hockey o del Calcetín de Navidad")

# Selección de número de filas
filas = st.selectbox("Número de filas del triángulo", options=list(range(5,14)), index=7)

# Selección de columna inicial (r)
r_options = list(range(0, filas-1))
r = st.selectbox("Columna donde empieza el palo (r)", options=r_options, index=3)

# Longitud del palo (limitada por filas y columna)
longitud_options = list(range(1, filas - r))
longitud = st.selectbox("Longitud del palo", options=longitud_options, index=4)

# Dibujar triángulo con palo
fig = plot_hockey_stick(filas, r, longitud)
st.pyplot(fig)
