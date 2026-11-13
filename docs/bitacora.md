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
