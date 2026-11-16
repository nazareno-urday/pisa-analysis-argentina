"""Genera las tablas LaTeX del artículo y un control de coherencia de cifras.

Lee exclusivamente las tablas versionadas en `reports/tables/` (salidas de los
notebooks 02 a 05). No accede a microdatos ni calcula estimaciones nuevas: solo
da formato, comprueba la coherencia interna (IC y p a partir de estimación y
error estándar) y deriva cocientes aritméticos que el texto cita.

Uso:  python paper/tablas.py
Salidas: paper/tablas/*.tex y paper/verificacion_cifras.txt
"""
from math import erfc, sqrt
from pathlib import Path

import pandas as pd
from scipy import stats

RAIZ = Path(__file__).resolve().parent.parent
TABLAS = RAIZ / "reports" / "tables"
AQUI = Path(__file__).resolve().parent
SALIDA = AQUI / "tablas"
SALIDA.mkdir(exist_ok=True)

t03 = pd.read_csv(TABLAS / "03_resultados_hipotesis.csv")
t04 = pd.read_csv(TABLAS / "04_sensibilidad.csv")
t05 = pd.read_csv(TABLAS / "05_hipotesis_exploratorias.csv")
informe = []


def anotar(*partes):
    linea = " ".join(str(p) for p in partes)
    informe.append(linea)


def num(x, d):
    s = f"{x:.{d}f}".replace(".", "{,}")
    return s.replace("-", "$-$")


def entero(n):
    return f"{int(n):,}".replace(",", ".")


def ptex(p):
    if p < 0.0001:
        return "$<$0{,}0001"
    return num(p, 4)


def buscar(tabla, hipotesis, empieza):
    sel = tabla[(tabla["hipotesis"] == hipotesis) & tabla["parametro"].str.startswith(empieza)]
    if len(sel) != 1:
        raise ValueError(f"Se esperaba 1 fila para {hipotesis!r} / {empieza!r}; hay {len(sel)}")
    return sel.iloc[0]


def renglon(etiqueta, f, d, factor=1.0, marca=""):
    est, ee = f["estimacion"] * factor, f["error_estandar"] * factor
    inf, sup = f["ic95_inferior"] * factor, f["ic95_superior"] * factor
    return (f"{etiqueta} & {entero(f['n'])} & {num(est, d)} & {num(ee, d)} & "
            f"[{num(inf, d)}; {num(sup, d)}] & {ptex(f['p'])}{marca} \\\\")


def escribir(nombre, lineas):
    (SALIDA / f"{nombre}.tex").write_text("\n".join(lineas) + "\n", encoding="utf-8")
    print("tabla:", nombre)


ACT = [("Investigar un tema", "Investigar un tema nuevo"), ("Ayudar a aprender", "Ayudar a aprender"),
       ("Resumir un texto", "Resumir un texto"), ("Redactar borradores", "Redactar borradores")]

# ---- Tabla H1 y H2 ----------------------------------------------------------
L = [r"\multicolumn{6}{@{}l}{\textit{H1. ESCS y rendimiento}} \\"]
for area in ["Ciencias", "Matemática", "Lectura"]:
    L.append(renglon(rf"\quad Pendiente de ESCS, {area.lower()}",
                     buscar(t03, "H1", "Pendiente de ESCS en " + area), 1))
L.append(renglon(r"\quad Ciencias, $Q_4-Q_1$ de ESCS (puntos)", buscar(t03, "H1", "Ciencias: cuartil 4"), 1))
L.append(r"\addlinespace")
L.append(r"\multicolumn{6}{@{}l}{\textit{H2. Uso de IA según ESCS ($Q_4-Q_1$)}} \\")
L.append(renglon(r"\quad Frecuencia media de IA (escala 1--5)", buscar(t03, "H2", "Promedio de frecuencia"), 2))
for clave, nombre in ACT:
    L.append(renglon(rf"\quad Uso frecuente, {nombre.lower()} (p.p.)",
                     buscar(t03, "H2", clave + ": diferencia"), 1, factor=100))
escribir("tab_h1_h2", L)

# ---- Tabla H3 ---------------------------------------------------------------
UMBRAL_H3 = 0.05 / 8
L = []
for contraste, titulo in [("seguido", "Uso frecuente (4--5) menos nunca (1)"),
                          ("a_veces", "Uso ocasional (2--3) menos nunca (1)")]:
    L.append(rf"\multicolumn{{6}}{{@{{}}l}}{{\textit{{{titulo}}}}} \\")
    for clave, nombre in ACT:
        f = buscar(t03, "H3", f"{clave}: {contraste} menos nunca")
        L.append(renglon(rf"\quad {nombre}", f, 1, marca=r"$^{\ast}$" if f["p"] < UMBRAL_H3 else ""))
    L.append(r"\addlinespace")
escribir("tab_h3", L[:-1])

# ---- Tabla H4 y H5 ----------------------------------------------------------
L = [r"\multicolumn{6}{@{}l}{\textit{H4. Coeficiente de la frecuencia de IA sobre ciencias}} \\"]
L.append(renglon(r"\quad Frecuencia media, sin ajustar", buscar(t03, "H4", "Coeficiente de la frecuencia de IA (promedio 1 a 5), sin"), 2))
L.append(renglon(r"\quad Frecuencia media + ESCS$^{\dagger}$", buscar(t04, "C. Controles", "Solo ESCS"), 2))
L.append(renglon(r"\quad Frecuencia media + ESCS, sexo y grado", buscar(t03, "H4", "Coeficiente de la frecuencia de IA (promedio 1 a 5), ajust"), 2))
for clave, nombre in ACT:
    L.append(renglon(rf"\quad {nombre}, ajustado", buscar(t03, "H4", clave + ": coeficiente ajustado"), 2))
L.append(r"\addlinespace")
L.append(r"\multicolumn{6}{@{}l}{\textit{H5 (exploratoria). Modelo con interacción}} \\")
L.append(renglon(r"\quad Interacción frecuencia de IA $\times$ ESCS", buscar(t03, "H5", "Interacci"), 2))
L.append(renglon(r"\quad Frecuencia de IA (en el ESCS medio)", buscar(t03, "H5", "Coeficiente de IA con ESCS"), 2))
escribir("tab_h4_h5", L)

# ---- Tabla HC ---------------------------------------------------------------
UMBRAL_HC = 0.05 / 3
L = [r"\multicolumn{6}{@{}l}{\textit{HC1. Ciencias: respondió los cuatro ítems de IA menos no respondió}} \\"]
L.append(renglon(r"\quad Sin ajustar (puntos)", buscar(t03, "HC1", "Ciencias: contestó IA menos no contestó (puntos), sin"), 1))
L.append(renglon(r"\quad Ajustado por ESCS (puntos)", buscar(t03, "HC1", "Ciencias: contestó IA menos no contestó (puntos), ajust"), 1))
L.append(r"\addlinespace")
L.append(r"\multicolumn{6}{@{}l}{\textit{HC2--HC4. Exploratorias registradas antes del cálculo}} \\")


def m(f):
    return r"$^{\ast}$" if f["p"] < UMBRAL_HC else ""


f = buscar(t05, "HC2", "Índice de tipo de uso"); L.append(renglon(r"\quad HC2. Índice $T$, $Q_4-Q_1$ de ESCS", f, 3, marca=m(f)))
f = buscar(t05, "HC3", "Proporción que usa IA"); L.append(renglon(r"\quad HC3. Uso frecuente, $Q_4-Q_1$ de ciencias (p.p.)", f, 1, factor=100, marca=m(f)))
f = buscar(t05, "HC3", "Frecuencia promedio"); L.append(renglon(r"\quad HC3. Frecuencia media, $Q_4-Q_1$ de ciencias", f, 3, marca=m(f)))
f = buscar(t05, "HC4", "ESCS sobre frecuencia de IA, total"); L.append(renglon(r"\quad HC4. Pendiente ESCS $\to$ IA, total", f, 3, marca=m(f)))
f = buscar(t05, "HC4", "ESCS sobre frecuencia de IA, dentro"); L.append(renglon(r"\quad HC4. Pendiente ESCS $\to$ IA, intraescuela", f, 3, marca=m(f)))
escribir("tab_hc", L)

# ---- Tabla de sensibilidad --------------------------------------------------
L = [r"\multicolumn{6}{@{}l}{\textit{A. Área evaluada (modelo ajustado, frecuencia media de IA)}} \\"]
for a, e in [("Ciencias", "Ciencias (referencia)"), ("Matemática", "Matemática"), ("Lectura", "Lectura")]:
    L.append(renglon(rf"\quad {e}", buscar(t04, "A. Área", a), 2))
L += [r"\addlinespace", r"\multicolumn{6}{@{}l}{\textit{B. Medida de uso de IA (modelo ajustado, ciencias)}} \\"]
for a, e in [("Índice AIUSESCH", "Índice AIUSESCH (por unidad del índice)"),
             ("Promedio de las preguntas", "Media de ítems contestados (con parciales)"),
             ("Usa IA alguna vez", "Usa IA alguna vez (sí/no)"),
             ("Usa IA semanal", "Usa IA semanal o diariamente (sí/no)")]:
    L.append(renglon(rf"\quad {e}", buscar(t04, "B. Medida de IA", a), 2))
L += [r"\addlinespace", r"\multicolumn{6}{@{}l}{\textit{D. Contraste estricto, sin ajustar: todos los días (5) menos nunca (1)}} \\"]
for clave, nombre in ACT:
    L.append(renglon(rf"\quad {nombre}", buscar(t04, "D. Contraste estricto", clave), 1))
escribir("tab_sensibilidad", L)

# ---- Tabla descriptiva de los ítems de IA (conteos sin ponderar) ------------
# Conteos copiados de las salidas ejecutadas de notebooks/00 (celda 12) y
# notebooks/01 (celda 9). Se verifican contra los totales de esas mismas salidas.
ITEMS = {
    "Resumir un texto": ([1786, 1163, 1621, 1821, 1465], 2690),
    "Investigar un tema nuevo": ([1326, 1254, 1902, 1863, 1421], 2780),
    "Redactar borradores": ([2375, 1222, 1554, 1375, 1154], 2866),
    "Ayudar a aprender": ([1176, 1030, 1427, 1972, 2047], 2894),
}
VALIDOS = {"Resumir un texto": 7856, "Investigar un tema nuevo": 7766, "Redactar borradores": 7680, "Ayudar a aprender": 7652}
L = []
for nombre, (c5, nr) in ITEMS.items():
    v = sum(c5)
    if v != VALIDOS[nombre] or v + nr + 526 + 20 != 11092:
        raise SystemExit(f"FALLA: los conteos de {nombre} no suman lo informado por los notebooks")
    pct = " & ".join(num(x / v * 100, 1) for x in c5)
    L.append(f"{nombre} & {entero(v)} & {pct} & {num((c5[3] + c5[4]) / v * 100, 1)} & {entero(nr)} \\\\")
escribir("tab_items_ia", L)

comp = pd.read_csv(TABLAS / "02_comparacion_respondieron_ia.csv")
ETI = {"PV1SCIE": ("Ciencias (PV1)", 1), "PV1MATH": ("Matemática (PV1)", 1), "PV1READ": ("Lectura (PV1)", 1),
       "ESCS": ("ESCS", 3), "MALE": ("Proporción de varones (\\texttt{MALE})", 3), "GRADE": ("Grado relativo al modal", 3)}
L = []
for _, f in comp.iterrows():
    e, d = ETI[f["variable"]]
    a, b = f["contestaron (con pesos)"], f["no contestaron (con pesos)"]
    L.append(f"{e} & {num(f['contestaron (sin pesos)'], d)} & {num(f['no contestaron (sin pesos)'], d)} & {num(a, d)} & {num(b, d)} & {num(a - b, d)} \\\\")
escribir("tab_no_respuesta", L)

# ---- Control de coherencia --------------------------------------------------
anotar("CONTROL DE COHERENCIA DE CIFRAS (generado por paper/tablas.py)")
anotar("Fuente: reports/tables/03_resultados_hipotesis.csv, 04_sensibilidad.csv, 05_hipotesis_exploratorias.csv")
anotar("")
anotar("1) IC 95 % y p recalculados desde estimación y error estándar redondeados")
peor_ic, peor_p, filas = 0.0, 0.0, 0
for nombre, tabla in [("03", t03), ("04", t04), ("05", t05)]:
    for _, f in tabla.iterrows():
        filas += 1
        e, s = f["estimacion"], f["error_estandar"]
        peor_ic = max(peor_ic, abs(e - 1.96 * s - f["ic95_inferior"]), abs(e + 1.96 * s - f["ic95_superior"]))
        z_red = abs(e / s)
        p_red = erfc(z_red / sqrt(2))
        # tolerancia: el p guardado sale de valores sin redondear
        z_guardado = stats.norm.isf(f["p"] / 2)
        # cota del error de |z| por redondear estimación y error estándar a 3 decimales
        cota = z_red * (0.0005 / abs(e) + 0.0005 / s) + 0.001
        peor_p = max(peor_p, abs(z_red - z_guardado) / cota)
anotar(f"   filas revisadas: {filas}")
anotar(f"   mayor discrepancia en límites de IC: {peor_ic:.4f} (tolerancia 0,003 por redondeo)")
anotar(f"   mayor discrepancia en |z| implícito, como fracción de la cota de redondeo: {peor_p:.2f} (debe ser <= 1)")
if peor_ic > 0.003 or peor_p > 1:
    raise SystemExit("FALLA: las tablas no son internamente coherentes")
anotar("   resultado: COHERENTE")
anotar("")

anotar("2) Cocientes derivados que cita el texto (aritmética sobre estimaciones puntuales)")
sin = buscar(t04, "C. Controles", "Sin controles")["estimacion"]
escs = buscar(t04, "C. Controles", "Solo ESCS")["estimacion"]
todo = buscar(t04, "C. Controles", "ESCS, sexo y grado")["estimacion"]
anotar(f"   H4 reducción al ajustar por ESCS: {(sin - escs) / sin * 100:.1f} %")
anotar(f"   H4 reducción al ajustar por ESCS, sexo y grado: {(sin - todo) / sin * 100:.1f} %")
tot = buscar(t05, "HC4", "ESCS sobre frecuencia de IA, total")["estimacion"]
den = buscar(t05, "HC4", "ESCS sobre frecuencia de IA, dentro")["estimacion"]
anotar(f"   HC4 cociente intraescuela/total: {den / tot * 100:.1f} %; cota inferior de la parte entre escuelas: {(1 - den / tot) * 100:.1f} %")
brecha = buscar(t03, "H1", "Ciencias: cuartil 4")["estimacion"]
for clave, _ in ACT:
    d = buscar(t03, "H3", clave + ": seguido menos nunca")["estimacion"]
    anotar(f"   H3 {clave}: {d:.1f} puntos = {d / brecha * 100:.0f} % de la brecha Q4-Q1 de ESCS ({brecha:.1f})")
anotar(f"   H4 ajustado x 4 puntos de escala: {todo * 4:.1f} puntos = {todo * 4 / brecha * 100:.0f} % de la brecha Q4-Q1")
hc1 = buscar(t03, "HC1", "Ciencias: contestó IA menos no contestó (puntos), sin")["estimacion"]
anotar(f"   HC1 sin ajustar / brecha Q4-Q1: {hc1 / brecha * 100:.0f} %")
anotar(f"   No respuesta: 3091/10566 = {3091 / 10566 * 100:.2f} %; 3617/11092 = {3617 / 11092 * 100:.2f} %; 3141/11092 = {3141 / 11092 * 100:.2f} %")
anotar(f"   Casos completos: 7191/11092 = {7191 / 11092 * 100:.2f} %; ESCS válido 9808/11092 = {9808 / 11092 * 100:.2f} %")
anotar(f"   Usó IA alguna vez: 6608/7191 = {6608 / 7191 * 100:.1f} %; semanal o diario en alguna: 4674/7191 = {4674 / 7191 * 100:.1f} % (sin ponderar)")
anotar("")

anotar("3) Lectura adicional de multiplicidad (sobre los p ya publicados; no son estimaciones nuevas)")
h4 = t03[t03["hipotesis"] == "H4"]
anotar(f"   Familia H4 (6 estimaciones), umbral 0,05/6 = {0.05 / 6:.5f}: superan {int((h4['p'] < 0.05 / 6).sum())} de 6")
for _, f in h4.iterrows():
    anotar(f"      p = {f['p']:.2e}  {'supera' if f['p'] < 0.05 / 6 else 'no supera'}  | {f['parametro'][:70]}")
todas = pd.concat([t03, t04, t05])
k = len(todas)
anotar(f"   Todas las estimaciones informadas ({k}), umbral 0,05/{k} = {0.05 / k:.5f}: superan {int((todas['p'] < 0.05 / k).sum())}")
no = todas[(todas["p"] < 0.05) & (todas["p"] >= 0.05 / k)]
anotar("   Con p < 0,05 pero sin superar el umbral global:")
for _, f in no.iterrows():
    anotar(f"      p = {f['p']:.4f} | {f['hipotesis']} | {f['parametro'][:70]}")
anotar("")

anotar("4) Sensibilidad a la distribución de referencia: t de Student con 80 grados de libertad en lugar de normal")
cambios = 0
for _, f in todas.iterrows():
    z = abs(f["estimacion"] / f["error_estandar"])
    pt = 2 * stats.t.sf(z, 80)
    if (f["p"] < 0.05) != (pt < 0.05):
        cambios += 1
        anotar(f"      cambia a 0,05: {f['parametro'][:60]} p_normal={f['p']:.4f} p_t80={pt:.4f}")
anotar(f"   valor crítico t(80; 0,975) = {stats.t.ppf(0.975, 80):.3f}; veredictos a 0,05 que cambian: {cambios}")
for etiqueta, f, umbral in [("H4 ajustado", buscar(t03, "H4", "Coeficiente de la frecuencia de IA (promedio 1 a 5), ajust"), 0.05),
                            ("HC4 intraescuela", buscar(t05, "HC4", "ESCS sobre frecuencia de IA, dentro"), 0.05 / 3),
                            ("H3 resumir (frecuente)", buscar(t03, "H3", "Resumir un texto: seguido"), 0.05 / 8)]:
    pt = 2 * stats.t.sf(abs(f["estimacion"] / f["error_estandar"]), 80)
    anotar(f"   {etiqueta}: p_normal = {f['p']:.5f}; p_t80 = {pt:.5f}; umbral {umbral:.5f}: {'supera' if pt < umbral else 'no supera'}")

(AQUI / "verificacion_cifras.txt").write_text("\n".join(informe) + "\n", encoding="utf-8")
print("\n".join(informe))
