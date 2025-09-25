import streamlit as st
import matplotlib.pyplot as plt
from math import comb

def pascal_triangle(filas):
    tri = []
    for n in range(filas):
        fila = [comb(n, k) for k in range(n+1)]
        tri.append(fila)
    return tri

def plot_hockey_stick(filas, r, longitud):
    n = r + longitud - 1  # calcular fila final del mango
    tri = pascal_triangle(filas)
    fig, ax = plt.subplots(figsize=(12,8))
    ax.axis("off")

    # Dibujar triángulo
    for i, fila in enumerate(tri):
        for j, val in enumerate(fila):
            ax.text(j - i/2, -i, str(val), ha="center", va="center", fontsize=12)

    # Mango
    stick_coords = [(k, r) for k in range(r, n+1)]
    # Punta
    punta_coord = (n+1, r+1) if n+1 < filas else None

    # Dibujar mango azul
    for (i,j) in stick_coords:
        ax.text(j - i/2, -i, str(tri[i][j]), ha="center", va="center",
                fontsize=12, color="blue", fontweight="bold")

    # Dibujar punta roja
    if punta_coord:
        pf, pc = punta_coord
        ax.text(pc - pf/2, -pf, str(tri[pf][pc]), ha="center", va="center",
                fontsize=12, color="red", fontweight="bold")

    # Mostrar suma
    suma = sum(tri[i][r] for i in range(r, n+1))
    punta_valor = tri[punta_coord[0]][punta_coord[1]] if punta_coord else "fuera"
    #ax.set_title(f"Suma del palo = {suma}, Punta = {punta_valor}", fontsize=14)

    # Ajustar límites
    ax.set_xlim(-filas/2 - 1, filas/2 + 1)
    ax.set_ylim(-filas - 1, 1)
    return fig

# =====================
# Interfaz Streamlit
# =====================
st.set_page_config(page_title="Teorema del Hockey-Stick", layout="wide")
st.title("Identidad del palo de hockey o del Calcetín de Navidad")

# Lista de filas del triángulo
filas = st.selectbox("Número de filas del triángulo", options=list(range(5,21)), index=7)

# Columna inicial del palo (r)
r_options = list(range(0, filas-1))
r = st.selectbox("Columna donde empieza el palo (r)", options=r_options, index=3)

# Longitud del palo
longitud_options = list(range(1, filas - r))
longitud = st.selectbox("Longitud del palo", options=longitud_options, index=4)

# Dibujar figura
fig = plot_hockey_stick(filas, r, longitud)
st.pyplot(fig)
