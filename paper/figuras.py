"""Genera las figuras del artículo a partir de las tablas versionadas.

No calcula ninguna estimación nueva: solo lee `reports/tables/*.csv` (salidas de
los notebooks 03, 04 y 05) y dibuja cada estimación con su intervalo de
confianza del 95 %. Uso:  python paper/figuras.py
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

RAIZ = Path(__file__).resolve().parent.parent
TABLAS = RAIZ / "reports" / "tables"
SALIDA = Path(__file__).resolve().parent / "figuras"
SALIDA.mkdir(exist_ok=True)

AZUL = "#1f5fa8"   # el IC 95 % excluye el cero
GRIS = "#7a7a7a"   # el IC 95 % incluye el cero
TINTA = "#222222"
TENUE = "#666666"

plt.rcParams.update({
    "font.family": "STIXGeneral",
    "mathtext.fontset": "stix",
    "font.size": 9,
    "axes.titlesize": 9.5,
    "axes.labelsize": 8.5,
    "xtick.labelsize": 8,
    "ytick.labelsize": 8.5,
    "axes.edgecolor": "#999999",
    "axes.linewidth": 0.6,
    "pdf.fonttype": 42,
})

t03 = pd.read_csv(TABLAS / "03_resultados_hipotesis.csv")
t04 = pd.read_csv(TABLAS / "04_sensibilidad.csv")
t05 = pd.read_csv(TABLAS / "05_hipotesis_exploratorias.csv")


def coma(x, d):
    return f"{x:.{d}f}".replace(".", ",").replace("-", "−")


def fila(tabla, hipotesis, empieza):
    """Devuelve (estimación, IC inferior, IC superior) de la única fila que coincide."""
    sel = tabla[(tabla["hipotesis"] == hipotesis) & tabla["parametro"].str.startswith(empieza)]
    if len(sel) != 1:
        raise ValueError(f"Se esperaba 1 fila para {hipotesis!r} / {empieza!r}; hay {len(sel)}")
    f = sel.iloc[0]
    return float(f["estimacion"]), float(f["ic95_inferior"]), float(f["ic95_superior"])


def bosque(ax, filas, titulo, xlabel, dec, factor=1.0, xlim=None, separadores=()):
    """filas: lista de (etiqueta, est, inf, sup). Punto lleno azul si el IC excluye 0; hueco gris si lo incluye."""
    n = len(filas)
    for i, (_, est, inf, sup) in enumerate(filas):
        y = n - 1 - i
        est, inf, sup = est * factor, inf * factor, sup * factor
        claro = inf > 0 or sup < 0
        color = AZUL if claro else GRIS
        ax.plot([inf, sup], [y, y], color=color, lw=1.6, solid_capstyle="round", zorder=2)
        ax.plot([est], [y], "o", ms=6, mfc=color if claro else "white", mec=color, mew=1.4, zorder=3)
        ax.annotate(coma(est, dec), (est, y), xytext=(0, 6), textcoords="offset points",
                    ha="center", va="bottom", fontsize=8, color=TINTA)
    for s in separadores:
        ax.axhline(n - s - 0.5, color="#cccccc", lw=0.6)
    ax.axvline(0, color=TINTA, lw=0.8, zorder=1)
    ax.set_yticks(range(n))
    ax.set_yticklabels([f[0] for f in filas][::-1])
    ax.set_ylim(-0.6, n - 0.25)
    if xlim:
        ax.set_xlim(*xlim)
    ax.set_title(titulo, loc="left", fontweight="bold", color=TINTA)
    ax.set_xlabel(xlabel, color=TENUE)
    ax.grid(axis="x", color="#e6e6e6", lw=0.5)
    ax.set_axisbelow(True)
    ax.tick_params(length=0)
    for lado in ("top", "right", "left"):
        ax.spines[lado].set_visible(False)


def guardar(fig, nombre):
    fig.savefig(SALIDA / f"{nombre}.pdf", bbox_inches="tight")
    plt.close(fig)
    print("figura:", nombre)


ACT = ["Investigar un tema", "Ayudar a aprender", "Resumir un texto", "Redactar borradores"]

# --- Figura 1: H1 y H2 ------------------------------------------------------
fig, ejes = plt.subplots(1, 2, figsize=(7.0, 2.5), gridspec_kw={"wspace": 0.55})
f = [(a, *fila(t03, "H1", "Pendiente de ESCS en " + a)) for a in ["Ciencias", "Matemática", "Lectura"]]
bosque(ejes[0], f, "(a) H1: pendiente de ESCS", "Puntos PISA por unidad de ESCS", 1, xlim=(-2, 40))
f = [(a, *fila(t03, "H2", a + ": diferencia en la proporción")) for a in ACT]
bosque(ejes[1], f, "(b) H2: uso frecuente, $Q_4-Q_1$ de ESCS", "Puntos porcentuales", 1, factor=100, xlim=(-1.5, 25))
guardar(fig, "fig_h1_h2")

# --- Figura 2: H3, contrastes sin ajustar -----------------------------------
fig, ejes = plt.subplots(1, 2, figsize=(7.0, 2.5), sharey=True, gridspec_kw={"wspace": 0.12})
f = [(a, *fila(t03, "H3", a + ": seguido menos nunca")) for a in ACT]
bosque(ejes[0], f, "(a) Uso frecuente menos nunca", "Puntos de ciencias", 1, xlim=(-22, 45))
f = [(a, *fila(t03, "H3", a + ": a_veces menos nunca")) for a in ACT]
bosque(ejes[1], f, "(b) Uso ocasional menos nunca", "Puntos de ciencias", 1, xlim=(-22, 45))
guardar(fig, "fig_h3")

# --- Figura 3: H4, atenuación y coeficientes por actividad ------------------
fig, ejes = plt.subplots(1, 2, figsize=(7.0, 2.5), gridspec_kw={"wspace": 0.6})
f = [("Sin controles", *fila(t04, "C. Controles", "Sin controles")),
     ("+ ESCS", *fila(t04, "C. Controles", "Solo ESCS")),
     ("+ ESCS, sexo y grado", *fila(t04, "C. Controles", "ESCS, sexo y grado"))]
bosque(ejes[0], f, "(a) Frecuencia media de IA", "Puntos de ciencias por punto de frecuencia", 1, xlim=(-1, 14.5))
f = [(a, *fila(t03, "H4", a + ": coeficiente ajustado")) for a in ACT]
bosque(ejes[1], f, "(b) Por actividad, modelo ajustado", "Puntos de ciencias por punto de frecuencia", 1, xlim=(-4.5, 9.5))
guardar(fig, "fig_h4")

# --- Figura 4: sensibilidad -------------------------------------------------
fig, ejes = plt.subplots(1, 2, figsize=(7.0, 3.1), gridspec_kw={"wspace": 0.95, "width_ratios": [1, 1]})
f = [("Ciencias (base)", *fila(t04, "A. Área", "Ciencias")),
     ("Matemática", *fila(t04, "A. Área", "Matemática")),
     ("Lectura", *fila(t04, "A. Área", "Lectura")),
     ("Índice AIUSESCH", *fila(t04, "B. Medida de IA", "Índice AIUSESCH")),
     ("Media con parciales", *fila(t04, "B. Medida de IA", "Promedio de las preguntas")),
     ("Usa alguna vez (sí/no)", *fila(t04, "B. Medida de IA", "Usa IA alguna vez")),
     ("Usa semanal o diario (sí/no)", *fila(t04, "B. Medida de IA", "Usa IA semanal"))]
bosque(ejes[0], f, "(a) Modelo ajustado: área y medida de IA", "Coeficiente (la unidad depende de la variante)", 1,
       xlim=(-9, 24))
f = [(a, *fila(t04, "D. Contraste estricto", a)) for a in ACT]
bosque(ejes[1], f, "(b) Todos los días menos nunca", "Puntos de ciencias, sin ajustar", 1, xlim=(-10, 44))
guardar(fig, "fig_sensibilidad")

# --- Figura 5: HC1, HC3 y HC4 -----------------------------------------------
fig, ejes = plt.subplots(1, 3, figsize=(7.0, 2.0), gridspec_kw={"wspace": 1.0})
f = [("Sin ajustar", *fila(t03, "HC1", "Ciencias: contestó IA menos no contestó (puntos), sin")),
     ("Ajustado por ESCS", *fila(t03, "HC1", "Ciencias: contestó IA menos no contestó (puntos), ajust"))]
bosque(ejes[0], f, "(a) HC1: contestó − no contestó", "Puntos de ciencias", 1, xlim=(-4, 85))
f = [("$Q_4-Q_1$ de ciencias", *fila(t05, "HC3", "Proporción que usa IA"))]
bosque(ejes[1], f, "(b) HC3: uso semanal o diario", "Puntos porcentuales", 1, factor=100, xlim=(-2, 27))
f = [("Total", *fila(t05, "HC4", "ESCS sobre frecuencia de IA, total")),
     ("Dentro de escuela", *fila(t05, "HC4", "ESCS sobre frecuencia de IA, dentro"))]
bosque(ejes[2], f, "(c) HC4: pendiente ESCS → IA", "Escala 1–5 por unidad de ESCS", 3, xlim=(-0.02, 0.27))
guardar(fig, "fig_exploratorias")
