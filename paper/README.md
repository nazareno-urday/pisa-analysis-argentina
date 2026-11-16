# Artículo científico

**Más brecha que efecto. Nivel socioeconómico, uso de chatbots de inteligencia artificial y rendimiento escolar en Argentina: evidencia asociativa con diseño muestral complejo a partir de PISA 2025**

Autor: Nazareno Urday Quiroga.

| Archivo | Contenido |
| --- | --- |
| `main.tex` | Manuscrito completo (resumen, abstract, 8 secciones, declaraciones, 4 apéndices) |
| `main.pdf` | Versión compilada |
| `referencias.bib` | Bibliografía (biblatex, estilo autor-año) |
| `tablas.py` | Genera `tablas/*.tex` desde `reports/tables/*.csv` y el control `verificacion_cifras.txt` |
| `figuras.py` | Genera `figuras/*.pdf` desde `reports/tables/*.csv` |
| `verificacion_cifras.txt` | Coherencia interna de las 46 estimaciones y cocientes derivados que cita el texto |

## Compilar

Requiere TeX Live (con `biblatex`, `mathpazo`, `tikz`, `booktabs`, `threeparttable`, `hyphenat`) y `latexmk`.

```bash
cd paper
```

```bash
python tablas.py
```

```bash
python figuras.py
```

```bash
latexmk -pdf main.tex
```

Los dos programas de Python necesitan `pandas`, `matplotlib` y `scipy` (este último solo para el apéndice B). No necesitan los microdatos de PISA: leen las tablas ya versionadas.

## De dónde sale cada cifra

- Todas las estimaciones provienen de las salidas ejecutadas de los notebooks 00 a 05 y de `reports/tables/`. El apéndice C del artículo indica el notebook y el archivo de cada resultado.
- Los cuadros del artículo se generan por programa, no a mano. `tablas.py` se detiene con error si un intervalo o un estadístico z no coincide con la estimación y el error estándar guardados (dentro del redondeo).
- **El análisis no se volvió a ejecutar al escribir el artículo**: los microdatos no están en el repositorio y el servidor de la OCDE no fue accesible desde el entorno de redacción. La comprobación anterior detecta errores de transcripción, no errores de cálculo.
- El apéndice B (multiplicidad y referencia t) y los cocientes derivados (porcentajes de reducción, cota de HC4) son aritmética sobre las estimaciones ya publicadas; se presentan separados de los resultados originales.

## Pendientes del autor antes de enviar

Marcados en rojo en el PDF (`\pendiente{...}` en `main.tex`):

1. Afiliación y contacto, si corresponde (no se incluyó ninguno).
2. Financiamiento y conflictos de interés.
3. Declaración sobre uso de herramientas de IA en el desarrollo del análisis, según la política de la revista.

Otros puntos a resolver:

4. Confirmar los términos de uso y la atribución exigida por la OCDE para PISA 2025 (figuran como no verificados en `docs/fuentes_y_licencias.md`).
5. Confirmar el factor de Fay (0,5) en el informe técnico de PISA 2025 cuando esté disponible.
6. El resumen tiene unas 350 palabras; muchas revistas piden 250 o menos.
7. Elegir revista y adaptar formato, extensión y estilo de citas.

## Verificación de referencias

El contraste automático con OpenAlex y Crossref no fue posible (bloqueados por el proxy del entorno). El estado de cada entrada es:

| Estado | Entradas |
| --- | --- |
| Metadatos (autores, revista, volumen, páginas, DOI) confirmados por búsqueda web el 16/11/2026, sin abrir el texto completo | `bastani2025`, `deng2025`, `jerrim2017`, `judkins1990`, `avvisati2020`, `vandeursen2019`, `groves2006`, `rustrao1996`, `greenland2016`, `mislevy1992`, `mislevy1991`, `oecd2024tech` |
| Existencia confirmada por búsqueda web; año de publicación inferido, a confirmar en la página de la OCDE | `oecd2026vol1` |
| Citadas de memoria, sin contraste en esta sesión (obras clásicas; revisar DOI y páginas) | `rubin1987`, `wolter2007`, `lumley2010`, `sirin2005`, `kasneci2023`, `hargittai2002`, `wasserstein2016`, `dunn1961`, `mundlak1978`, `oecd2009manual`, `harris2020`, `hunter2007`, `mckinney2010` |
| Tomadas de la documentación del proyecto (`docs/fuentes_y_licencias.md`); título exacto y año a confirmar | `oecd2025db`, `oecd2022db`, `unicef2025` |

Ninguna referencia fue leída en texto completo durante la redacción. Las afirmaciones del artículo sobre el contenido de cada trabajo se limitan a su resultado general y deben revisarse contra la fuente antes de enviar.

No se hizo una búsqueda sistemática de antecedentes ni de análisis previos de las preguntas de IA de PISA 2025; el artículo no afirma novedad.
