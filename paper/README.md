# Informe final

**Más brecha que efecto. Nivel socioeconómico, uso de chatbots de inteligencia artificial y rendimiento escolar en Argentina: evidencia asociativa con diseño muestral complejo a partir de PISA 2025**

Autores: Nazareno Urday Quiroga, Juan Ignacio Cordero y Matias Sanchez.

| Archivo | Contenido |
| --- | --- |
| `informe_final.tex` | Informe final (10 páginas): el problema, datos y método, resultados, discusión y conclusión |
| `informe_final.pdf` | Versión compilada |
| `referencias.bib` | Bibliografía (8 entradas) |
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
latexmk -pdf informe_final.tex
```

Los dos programas de Python necesitan `pandas`, `matplotlib` y `scipy` (este último solo para el control de cifras). No necesitan los microdatos de PISA: leen las tablas ya versionadas.

## De dónde sale cada cifra

- Todas las estimaciones provienen de las salidas ejecutadas de los notebooks 00 a 05 y de `reports/tables/`. 
- Los cuadros del artículo se generan por programa, no a mano. `tablas.py` se detiene con error si un intervalo o un estadístico z no coincide con la estimación y el error estándar guardados (dentro del redondeo).
- **El análisis no se volvió a ejecutar para el informe**: los microdatos no están en el repositorio. La comprobación anterior detecta errores de transcripción, no errores de cálculo.
- La lectura de multiplicidad y de la referencia t (sección de robustez) y los cocientes derivados (porcentajes de reducción, cota de HC4) son aritmética sobre las estimaciones ya publicadas, no estimaciones nuevas.

## A revisar antes de enviar

1. Confirmar el factor de Fay (0,5) en el informe técnico de PISA 2025 cuando esté disponible.
2. Confirmar los términos de uso y la atribución exigida por la OCDE (figuran como no verificados en `docs/fuentes_y_licencias.md`).
3. Referencias: no se hizo un contraste automático con OpenAlex ni Crossref. Los metadatos de `bastani2025`, `judkins1990` y `mislevy1992` se confirmaron por búsqueda web; `sirin2005`, `hargittai2002`, `rubin1987` y `oecd2009manual` están citadas de memoria; `oecd2025db` sale de la documentación del proyecto. Ninguna se leyó en texto completo: revisar DOI, páginas y lo que el texto les atribuye.
