# Estado del proyecto

**Última actualización:** 13/11/2026
**Etapa actual:** 7 (Cierre) casi terminada; falta la revisión final
**Etapa 0:** aprobada y publicada (push 13/11/2026)

## Hecho
- Fuentes localizadas y descargadas (ver `docs/fuentes_y_licencias.md`).
- `notebooks/00_viabilidad_y_fuentes.ipynb` ejecutado de arriba abajo.
- Verificado en el archivo de estudiantes de PISA 2025: Argentina tiene 11.092 estudiantes en 412 escuelas, con valores plausibles, ESCS, peso final, 80 pesos replicados (sin faltantes) y cuatro preguntas de frecuencia de uso de chatbots de IA.
- Casos completos en Argentina (valor plausible de matemática, ESCS, peso y las cuatro preguntas de IA): 7.191 de 11.092 (64,8 %).
- PISA 2022 (respaldo): 12.111 estudiantes de Argentina con rendimiento, ESCS y pesos; ninguna de las 1.278 variables tiene IA en su etiqueta.

## Decisiones
- **Aprobada:** Plan A con PISA 2025; PISA 2022 y UNICEF como contexto.
- **Aprobada:** los cuatro usos originales no coinciden con el instrumento. Se analiza frecuencia de uso por actividad (resumir, investigar, redactar borradores, ayudar a aprender). "Copia directa" no se mide.

## Pendientes y riesgos
- Alrededor del 30 % de los estudiantes argentinos no tiene dato en las preguntas de IA (28,3 % no contestó ninguna de las cuatro y 32,6 % no contestó las cuatro, incluyendo respuestas parciales); el origen se determinó en la Etapa 2: casi todo es código 99 (sin respuesta) y 97 (no administrado, 526 estudiantes), sin saltos de filtro (código 95).
- Términos de uso y atribución de la OCDE no verificados; documentación técnica de 2025 no revisada (informe técnico final previsto para 2027).
- Factor de replicación de los pesos no confirmado en documentación oficial.

## Etapa 1
- README inicial con problema, población, hipótesis H1 a H5 con su parámetro, criterios de éxito y límites.
- Aprobada por el estudiante la frecuencia por actividad en lugar de los cuatro perfiles.

## Etapa 2
- `notebooks/01_carga_y_comprension.ipynb` y `docs/diccionario_datos.csv`.
- Sin duplicados; 412 escuelas, entre 1 y 35 estudiantes por escuela.
- Preguntas de IA en Argentina (de 11.092): respondieron las cuatro 7.475, ninguna 3.141, algunas 476. Faltantes: código 99 (sin respuesta) entre 2.690 y 2.894 por pregunta; código 97 (no administrado) 526; código 96 (faltante del sistema) 20; sin código 95.
- ESCS: 1.284 estudiantes con código 97 (no administrado); 9.808 válidos.
- Sexo: `ST004D01T` viene con código 99 para todo Argentina; se usa `MALE`.

## Etapa 3
- `notebooks/02_preparacion.ipynb`; conjunto analítico en `data/processed/` (no versionado); tablas en `reports/tables/`.
- Muestras: 9.808 con ESCS; 7.475 con las 4 preguntas de IA; 7.191 con ESCS y las 4 preguntas de IA (64,8 %).
- Quienes no respondieron IA rinden menos (ciencias ponderado 355 contra 418) y tienen menor ESCS: los resultados de IA describen a quienes respondieron. Candidata a hipótesis complementaria HC1.

## Etapa 4
- `notebooks/03_exploracion_e_hipotesis.ipynb`; tabla completa en `reports/tables/03_resultados_hipotesis.csv`; figuras `03_*` en `reports/figures/`.
- Inferencia con peso final, 80 pesos replicados (divisor 20, factor de Fay 0,5 sin confirmar) y 10 valores plausibles con reglas de Rubin.
- H1: +30,6 puntos de ciencias por unidad de ESCS; H2: mayor uso frecuente de IA en el cuartil de ESCS más alto; H3: uso frecuente de IA asociado a más puntaje en investigar, ayudar a aprender y resumir; H4: +4,0 puntos por punto de frecuencia ajustado (+9,5 sin ajustar); H5: evidencia insuficiente; HC1 (complementaria): quienes no contestaron IA tienen 66,0 puntos menos de ciencias (53,8 ajustado por ESCS), sin contar a los 526 con pregunta no administrada.
- Validación: una implementación independiente (otro código, mismos datos) reprodujo la pendiente de ESCS, el contraste entre cuartiles, el coeficiente de IA ajustado y la diferencia de HC1 original con coincidencia dentro de 0,01. No se contrastó contra software estadístico de terceros (R `intsvy` o `Rrepest`).
- Pendiente: confirmar el factor de Fay (0,5) en la documentación técnica de PISA 2025. Los cortes de los cuartiles de ESCS son fijos entre réplicas (práctica habitual, pero no incluye su variabilidad en el error estándar).

## Etapa 5
- `notebooks/04_sensibilidad_y_evaluacion.ipynb`, `reports/tables/04_sensibilidad.csv`, `reports/figures/04_sensibilidad.png`.
- Variantes: otras áreas, otras medidas de IA, otros controles y contraste más estricto. El signo y el patrón por actividad se mantienen; el tamaño depende de los controles (+9,5 sin controles, +5,0 con ESCS, +4,0 con ESCS, sexo y grado).
- Decisión: continuar con el informe final comunicando que valen para quienes contestaron, que el tamaño es modesto y que no son causales.
- No se incluyó un componente predictivo (no fue acordado), por eso el notebook 04 es de sensibilidad y no de modelado.

## Etapa 6
- `notebooks/07_informe_final.ipynb`, revisado contra las tablas; se corrigieron denominadores (29 % de quienes recibieron la pregunta), mezcla de resultados ajustados y no ajustados y redacción para docentes.

## Etapa 7
- Reproducción: los seis notebooks corrieron en orden en un entorno nuevo creado con `requirements.txt`; las tablas y figuras versionadas no cambiaron.
- README con instalación, obtención de datos, orden de notebooks y resultados principales.
- Licencia del código: MIT.

## Hipótesis exploratorias (HC2 a HC4)
- `notebooks/05_hipotesis_exploratorias.ipynb` y `reports/tables/05_hipotesis_exploratorias.csv`; registradas en la bitácora antes de calcularlas.
- HC3: +16,6 puntos porcentuales de uso semanal o diario en el cuartil de mayor rendimiento (IC 95 %: 11,3 a 22,0). HC4: coeficiente de ESCS sobre frecuencia de IA 0,185 en total y 0,080 dentro de escuela. HC2: no concluyente (+0,08; -0,03 a 0,19).
- El informe final pasó a ser `notebooks/07_informe_final.ipynb`; hay que repetir la reproducción en un entorno limpio con los 7 notebooks.

- El informe final (`notebooks/07_informe_final.ipynb`) incluye la sección 5, con la confianza en cada hipótesis según sus p-valores, umbrales de Bonferroni, tamaño e intervalos.
