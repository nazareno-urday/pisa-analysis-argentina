# Bitácora

## 13/11/2026 · Etapa 0

| Decisión | Estado |
| --- | --- |
| Diseño Plan A: PISA 2025 como fuente única para IA, contexto y rendimiento | Aprobada (el estudiante aprobó el plan A con datasets PISA) |
| Usar UNICEF Kids Online como contexto, sin cruzarlo con PISA | Aprobada como contexto; uso concreto pendiente |
| Analizar frecuencia de uso por actividad en lugar de los cuatro perfiles originales | Aprobada |
| Excluir `data/` del repositorio | Aprobada y aplicada |

### Hechos y fuentes
- Archivos y tamaños: ver `docs/fuentes_y_licencias.md`.
- Descarga del archivo de estudiantes de 2025 en tramos paralelos: con una sola conexión se medían unos 160 KB/s y en paralelo unos 1.300 KB/s. Integridad comprobada por tamaño exacto y `unzip -t` sin errores.
- Lectura de los datos: en la Etapa 0 los códigos de faltante 95 a 99 se convirtieron en NaN; desde la Etapa 2 se leen conservándolos (`user_missing=True`).
- Preguntas de IA de PISA 2025 (codebook, hoja `STU`): `ST438Q01DA` a `ST438Q04DA`, `IC170Q10DA`, `IC171Q10DA`, `AIUSESCH`.
- Cifras de Argentina: ver `notebooks/00_viabilidad_y_fuentes.ipynb`.

### Cambios de alcance
- Ninguno todavía.

## 13/11/2026 · Etapa 1

| Decisión | Estado |
| --- | --- |
| Rendimiento principal: ciencias (dominio principal elegido); matemática y lectura como complemento | Propuesta |
| Hipótesis H1 a H5 con parámetros definidos (ver README) | Propuesta |
| Hallazgos inesperados se registran como hipótesis complementarias exploratorias | Aprobada |
| Avanzar a las etapas siguientes sin esperar revisión entre una y otra | Aprobada por el estudiante |

## 13/11/2026 · Etapa 2

| Decisión | Estado |
| --- | --- |
| Leer los datos conservando los códigos de faltante | Aprobada y aplicada |
| Usar `MALE` como variable de sexo (la original no tiene datos en Argentina) | Propuesta |
| Tratar los códigos 95 o más como faltante en ESCS y en las variables de IA | Propuesta (se aplica en la Etapa 3) |

## 13/11/2026 · Etapa 3

| Decisión | Estado |
| --- | --- |
| No imputar ESCS, IA ni rendimiento | Aprobada (regla del proyecto) |
| Grupos de frecuencia de IA: nunca / a veces (2-3) / seguido (4-5) | Propuesta |
| Cuartiles de ESCS ponderados con el peso final, relativos a Argentina | Propuesta |
| Registrar el faltante de IA como hipótesis complementaria HC1 | Propuesta |

## 13/11/2026 · Etapa 4

| Decisión | Estado |
| --- | --- |
| Muestra para H2 a H5: estudiantes con ESCS y las cuatro preguntas de IA (7.191) | Propuesta |
| Controles de H4: ESCS, sexo (`MALE`) y grado | Propuesta |
| Corrección de Bonferroni informada solo para las 8 comparaciones de H3 | Propuesta |
| HC1 (no contestar IA y rendimiento) como hipótesis complementaria exploratoria | Propuesta |
| Los cuartiles de ESCS se fijan con el peso final y no se recalculan con cada réplica | Simplificación a revisar |

| HC1 sin los 526 estudiantes con pregunta no administrada (código 97) | Propuesta (corrección tras la revisión independiente) |

## 13/11/2026 · Etapa 5

| Decisión | Estado |
| --- | --- |
| Pocas variantes de sensibilidad decididas de antemano (área, medida de IA, controles, contraste estricto) | Propuesta |
| No incluir componente predictivo; el notebook 04 es de sensibilidad | Propuesta |
| Continuar con el informe final | Propuesta |

## 13/11/2026 · Etapas 6 y 7

| Decisión | Estado |
| --- | --- |
| Informe final como notebook (sin app ni modelo desplegado) | Propuesta |
| Unificar el denominador de la no respuesta: 3.091 de 10.566 (29 %) a quienes se les administró la pregunta | Propuesta |
| Declaración del uso de IA en el README | Pendiente de acordar |
| Licencia del código | Pendiente de elegir |
| H1, H2 y H3 como hipótesis principales; H4, H5 y HC1 como complementos; ideas nuevas (propósito de uso, a quién llega la IA, comparación dentro de la escuela) como posibles estudios siguientes sin probar | Aprobada por el estudiante |

## 13/11/2026 · Hipótesis exploratorias atrevidas (registradas ANTES de calcular)

Surgieron después de ver los resultados de H1 a H5, por eso son exploratorias. Se informarán todas, con el resultado que salga, y con corrección de Bonferroni para tres hipótesis (p < 0,05 / 3 = 0,0167).

| ID | Hipótesis | Parámetro | Muestra | Resultado esperado |
| --- | --- | --- | --- | --- |
| HC2 · "Para qué" | Los estudiantes de mayor ESCS usan la IA más para investigar y aprender, y los de menor ESCS más para redactar borradores | Índice de tipo de uso por estudiante = promedio de frecuencia de "investigar" y "ayudar a aprender" menos frecuencia de "redactar borradores". Diferencia del índice entre el cuartil 4 y el cuartil 1 de ESCS | 7.191 con ESCS y las 4 preguntas | Diferencia positiva |
| HC3 · "A quién llega" | La IA llega más a quienes rinden más: el uso semanal o diario en alguna actividad es mayor en el cuartil de mayor rendimiento en ciencias que en el de menor rendimiento | Diferencia en la proporción que usa IA semanal o diariamente en alguna actividad: cuartil 4 de ciencias menos cuartil 1 (los cortes se recalculan con cada valor plausible y cada peso) | 7.191 | Diferencia positiva |
| HC4 · "La misma escuela" | La brecha de uso de IA según ESCS se mantiene al comparar estudiantes de una misma escuela | Coeficiente de ESCS sobre la frecuencia promedio de IA, total y dentro de escuela (restando el promedio ponderado de cada escuela) | 7.191 | Coeficiente dentro de escuela positivo y menor al total |

Advertencias acordadas antes de calcular: son asociaciones; si el rendimiento (HC3) se relaciona con el uso de IA no se sabe cuál causa cuál; y todas valen solo para quienes contestaron las preguntas de IA.
