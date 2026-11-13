# Estado del proyecto

**Última actualización:** 13/11/2026
**Etapa actual:** 4 (Análisis) terminada; en revisión independiente
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
- Alrededor del 30 % de los estudiantes argentinos no tiene dato en las preguntas de IA (28,3 % en las cuatro, 32,6 % en alguna); el origen se determinó en la Etapa 2: casi todo es código 99 (sin respuesta) y 97 (no administrado, 526 estudiantes), sin saltos de filtro (código 95).
- Términos de uso y atribución de la OCDE no verificados; documentación técnica de 2025 no revisada (informe técnico final previsto para 2027).
- Factor de replicación de los pesos no confirmado en documentación oficial.

## Etapa 1
- README inicial con problema, población, hipótesis H1 a H5 con su parámetro, criterios de éxito y límites.
- Aprobada por el estudiante la frecuencia por actividad en lugar de los cuatro perfiles.

## Etapa 2
- `notebooks/01_carga_y_comprension.ipynb` y `docs/diccionario_datos.csv`.
- Sin duplicados; 412 escuelas, entre 1 y 35 estudiantes por escuela.
- Preguntas de IA en Argentina (de 11.092): respondieron las cuatro 7.475, ninguna 3.141, algunas 476. Faltantes: código 99 (sin respuesta) entre 2.690 y 2.894 por pregunta; código 97 (no administrado) 526; sin código 95.
- ESCS: 1.284 estudiantes con código 97 (no administrado); 9.808 válidos.
- Sexo: `ST004D01T` viene con código 99 para todo Argentina; se usa `MALE`.

## Etapa 3
- `notebooks/02_preparacion.ipynb`; conjunto analítico en `data/processed/` (no versionado); tablas en `reports/tables/`.
- Muestras: 9.808 con ESCS; 7.475 con las 4 preguntas de IA; 7.191 con ESCS y las 4 preguntas de IA (64,8 %).
- Quienes no respondieron IA rinden menos (ciencias ponderado 355 contra 418) y tienen menor ESCS: los resultados de IA describen a quienes respondieron. Candidata a hipótesis complementaria HC1.

## Etapa 4
- `notebooks/03_exploracion_e_hipotesis.ipynb`; tabla completa en `reports/tables/03_resultados_hipotesis.csv`; figuras `03_*` en `reports/figures/`.
- Inferencia con peso final, 80 pesos replicados (divisor 20, factor de Fay 0,5 sin confirmar) y 10 valores plausibles con reglas de Rubin.
- H1: +30,6 puntos de ciencias por unidad de ESCS; H2: mayor uso frecuente de IA en el cuartil de ESCS más alto; H3: uso frecuente de IA asociado a más puntaje en investigar, ayudar a aprender y resumir; H4: +4,0 puntos por punto de frecuencia ajustado (+9,5 sin ajustar); H5: evidencia insuficiente; HC1 (complementaria): quienes no contestaron IA tienen 62,7 puntos menos de ciencias (53,8 ajustado por ESCS).
- Pendiente: validar la inferencia contra otro software y confirmar el factor de Fay.
