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

def plot_hockey_stick(filas, r, n):
    """
    Dibuja el triángulo de Pascal con el palo de hockey.
    - filas: número de filas del triángulo
    - r: columna donde empieza el palo
    - n: fila final del mango (inclusive)
    """
    tri = pascal_triangle(filas)
    fig, ax = plt.subplots(figsize=(12,8))
    ax.axis("off")

    # Dibujar todo el triángulo
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

    # Mostrar igualdad numérica
    suma = sum(tri[i][r] for i in range(r, n+1))
    punta_valor = tri[punta_coord[0]][punta_coord[1]] if punta_coord else "fuera"
    # ax.set_title(f"Suma del palo = {suma}, Punta = {punta_valor}", fontsize=14)

    # Ajustar límites para que siempre se vea todo
    ax.set_xlim(-filas/2 - 1, filas/2 + 1)
    ax.set_ylim(-filas - 1, 1)
    return fig

# =====================
# Interfaz Streamlit
# =====================
st.set_page_config(page_title="Teorema del Hockey-Stick", layout="wide")
st.title("Teorema del Hockey-Stick en el Triángulo de Pascal")

# Controles interactivos
filas = st.slider("Número de filas del triángulo", min_value=5, max_value=20, value=12)
r = st.slider("Columna donde empieza el palo (r)", min_value=0, max_value=filas-2, value=3)
n = st.slider("Longitud de palo", min_value=2, max_value=filas-r-2, value=4)
n=r+n-2
# Dibujar figura
fig = plot_hockey_stick(filas, r, n)
st.pyplot(fig)
