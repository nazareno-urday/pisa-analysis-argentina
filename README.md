# PISA, inteligencia artificial y desigualdad educativa en Argentina

Proyecto de ciencia de datos de punta a punta con datos reales de PISA 2025 (OCDE). Todo el análisis está en notebooks `.ipynb`.

> **Estado:** análisis e informe terminados (notebooks 00 a 05). Los resultados son asociaciones, no causas. Pendiente: declaración del uso de IA en el proceso y revisión final del profesor.

## 1. Problema

Se quiere entender cómo se asocian el **contexto socioeconómico** y las **formas de uso de IA** con el **rendimiento** de estudiantes argentinos en PISA 2025, y qué se puede (y qué no) demostrar con esos datos.

**Quién usaría los resultados:** docentes y comunidad educativa interesados en el aprendizaje y en las brechas de acceso.

**Qué no se va a afirmar:** que la IA mejore o empeore el aprendizaje. Con datos de una encuesta solo se pueden estudiar **asociaciones**, no causas.

## 2. Datos

| Fuente | Rol | Estado |
| --- | --- | --- |
| OCDE, PISA 2025, archivo de estudiantes | Principal | Descargado y auditado |
| OCDE, PISA 2022, archivo de estudiantes | Contexto de rendimiento (no tiene preguntas de IA) | Descargado |
| UNICEF, Kids Online Argentina 2025 | Contexto descriptivo (sin microdatos, no se cruza con PISA) | Informe leído |

Detalle, enlaces y condiciones de uso en [`docs/fuentes_y_licencias.md`](docs/fuentes_y_licencias.md). Los datos **no se suben** al repositorio.

## 3. Población, unidad y variables

- **Unidad de análisis:** una fila = un estudiante de Argentina en PISA 2025.
- **Población representada:** estudiantes de 15 años escolarizados que PISA representa en Argentina (se usan los pesos muestrales; no se habla de "todos los jóvenes argentinos").
- **Muestra disponible:** 11.092 estudiantes de 412 escuelas. 7.191 tienen todas las variables clave.
- **Rendimiento:** valores plausibles de ciencias (dominio principal elegido), con matemática y lectura como complemento.
- **Contexto socioeconómico:** índice ESCS de PISA (no es ingreso familiar).
- **Uso de IA:** PISA pregunta la **frecuencia** con que se usan chatbots de IA para cuatro actividades escolares: resumir un texto, investigar un tema nuevo, redactar borradores y ayudar a aprender. La idea inicial de cuatro perfiles (delegación, investigación, tutoría y copia directa) **no coincide con el cuestionario**; "copia directa" no se mide. Se analiza frecuencia por actividad.

## 4. Preguntas e hipótesis

Pregunta principal: **¿cómo se asocian el uso de IA y el contexto socioeconómico con el rendimiento de estudiantes argentinos, y qué permite demostrar PISA?**

| ID | Hipótesis nula (H0) | Parámetro que se estima | Datos |
| --- | --- | --- | --- |
| H1 | No hay asociación entre ESCS y rendimiento | Pendiente de ESCS sobre el puntaje y diferencia entre cuartiles | ESCS y rendimiento |
| H2 | La frecuencia de uso de IA es independiente del ESCS | Diferencia en la frecuencia de uso entre cuartiles de ESCS | IA y ESCS |
| H3 | No hay diferencias de rendimiento según la frecuencia de uso de IA | Diferencia de puntaje entre quienes nunca usan y quienes usan seguido, por actividad | IA y rendimiento |
| H4 | No hay asociación entre uso de IA y rendimiento tras ajustar por contexto | Coeficiente de la frecuencia de IA con ESCS y otras covariables disponibles | Variables anteriores |
| H5 (exploratoria) | La asociación IA-rendimiento no cambia con el ESCS | Interacción IA × ESCS | Cobertura y tamaño de muestra suficientes |

Cada hipótesis se responderá con una de tres frases: *evidencia compatible con una asociación*, *evidencia insuficiente* o *no evaluable con estos datos*. No se "acepta H0" como prueba de ausencia de efecto. Se informará la magnitud y la incertidumbre, no solo el p-valor.

Si durante el análisis aparece algo llamativo, se anota como **hipótesis complementaria exploratoria** (por separado de H1 a H5) y se explica por qué surgió.

## 5. Criterios de éxito

- **Técnico:** estimaciones con los pesos de PISA, 80 pesos replicados y los 10 valores plausibles; notebooks que corren de arriba abajo con un kernel limpio; toda cifra del informe sale de una salida ejecutada.
- **De valor:** que una persona del ámbito educativo pueda leer el informe final y entender qué se encontró, qué no, y por qué no se pueden sacar conclusiones causales.

No se exige que los resultados sean estadísticamente significativos.

## 6. Límites y riesgos

- Solo asociaciones, no causalidad. El uso de IA es autorreportado.
- Entre los estudiantes a quienes se les hicieron las preguntas de IA (10.566), alrededor del 29 % (3.091) no las contestó, y quienes no contestaron rinden bastante menos. Los resultados sobre IA valen para quienes contestaron.
- El nivel socioeconómico (ESCS) es un índice relativo, no un ingreso.
- El archivo de PISA 2025 usa documentación técnica provisional (informe técnico final previsto para 2027).
- Los datos de UNICEF corresponden a otra población (urbana, 9 a 17 años) y no se mezclan con los de PISA.

## Resultados principales (Etapa 4)

Detalle, intervalos y figuras en `notebooks/03_exploracion_e_hipotesis.ipynb` y `reports/tables/03_resultados_hipotesis.csv`. Todo con pesos de PISA, 80 réplicas y 10 valores plausibles.

- **H1:** el ESCS se asocia con el rendimiento: +30,6 puntos de ciencias por unidad de ESCS; el cuartil más alto supera al más bajo en 82,4 puntos.
- **H2:** los estudiantes de mayor ESCS usan IA con más frecuencia (entre 13 y 17 puntos porcentuales más de uso semanal o diario, según la actividad).
- **H3:** usar IA seguido (semanal o diario) se asocia con más puntaje en investigar, ayudar a aprender y resumir (+18,8 a +28,4 puntos, sin ajustar), pero no de forma concluyente en redactar borradores.
- **H4:** ajustando por ESCS, sexo y grado, la asociación baja a +4,0 puntos por punto de frecuencia (sin ajustar +9,5).
- **H5 (exploratoria):** evidencia insuficiente de que la asociación cambie con el ESCS.
- **HC1 (complementaria):** quienes no contestaron las preguntas de IA tienen unos 66 puntos menos de ciencias (54 ajustando por ESCS).

## 7. Estructura

| Ruta | Contenido |
| --- | --- |
| `notebooks/` | Análisis, un notebook por etapa (ver orden en la sección 8) |
| `docs/` | Fuentes y licencias, bitácora de decisiones, estado |
| `reports/` | Figuras y tablas pequeñas (a medida que existan) |
| `data/` | Datos originales y derivados (no se versionan) |

## 8. Cómo ejecutar

1. **Entorno** (Windows, PowerShell):

```powershell
python -m venv .venv
.venv\Scripts\python -m pip install -r requirements.txt
```

2. **Datos** (no se incluyen en el repositorio). Descargar de la OCDE, usando los enlaces de [`docs/fuentes_y_licencias.md`](docs/fuentes_y_licencias.md):
   - PISA 2025, archivo de estudiantes `CY09_MS_STU_PUF.zip` (unos 993 MB): descomprimir el `.sav` en `data/raw/pisa2025/extraido/`.
   - Codebook `PISA2025_Codebook.xlsx` de la página de PISA 2025, en `data/raw/pisa2025/docs/` (se descarga a mano; la OCDE bloquea la descarga automática).
   - PISA 2022, archivo de estudiantes `STU_QQQ_SPSS.zip`: descomprimir el `.sav` en `data/raw/pisa2022/sav/`.

3. **Notebooks**, en este orden (cada uno se ejecuta de arriba abajo con el kernel reiniciado):

| Orden | Notebook | Qué hace |
| --- | --- | --- |
| 1 | `00_viabilidad_y_fuentes.ipynb` | Fuentes y comprobación de viabilidad |
| 2 | `01_carga_y_comprension.ipynb` | Carga, diccionario de datos y faltantes |
| 3 | `02_preparacion.ipynb` | Conjunto analítico (se guarda en `data/processed/`) |
| 4 | `03_exploracion_e_hipotesis.ipynb` | Pruebas de H1 a H5 y HC1 |
| 5 | `04_sensibilidad_y_evaluacion.ipynb` | Pruebas de sensibilidad |
| 6 | `05_informe_final.ipynb` | Informe final |

```powershell
.venv\Scripts\python -m jupyter lab
```

Se comprobó que los seis notebooks corren en orden en un entorno nuevo creado con `requirements.txt` y que las tablas y figuras guardadas no cambian.

## 9. Uso de IA en el proceso

Se declarará al cierre del proyecto, indicando qué asistencia se usó y qué verificamos nosotros.
