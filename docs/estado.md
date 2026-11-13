# Estado del proyecto

**Última actualización:** 13/11/2026
**Etapa actual:** 1 (Problema) terminada; en curso 2 (Comprensión)
**Etapa 0:** aprobada y publicada (push 13/11/2026)

## Hecho
- Fuentes localizadas y descargadas (ver `docs/fuentes_y_licencias.md`).
- `notebooks/00_viabilidad_y_fuentes.ipynb` ejecutado de arriba abajo.
- Verificado en el archivo de estudiantes de PISA 2025: Argentina tiene 11.092 estudiantes en 412 escuelas, con valores plausibles, ESCS, peso final, 80 pesos replicados (sin faltantes) y cuatro preguntas de frecuencia de uso de chatbots de IA.
- Casos completos en Argentina (valor plausible de matemática, ESCS, peso y las cuatro preguntas de IA): 7.191 de 11.092 (64,8 %).
- PISA 2022 (respaldo): 12.111 estudiantes de Argentina con rendimiento, ESCS y pesos; ninguna de las 1.278 variables tiene IA en su etiqueta.

## Decisiones
- **Aprobada:** Plan A con PISA 2025; PISA 2022 y UNICEF como contexto.
- **Pendiente de aprobación:** los cuatro usos originales no coinciden con el instrumento. Se analizará frecuencia de uso por actividad (resumir, investigar, redactar borradores, ayudar a aprender). "Copia directa" no se mide.

## Pendientes y riesgos
- Alrededor del 30 % de los estudiantes argentinos no tiene dato en las preguntas de IA (28,3 % en las cuatro, 32,6 % en alguna); el origen (filtro, rotación o no respuesta) no está determinado. El archivo declara los códigos 95 a 99, pero la lectura actual los convierte en faltante; en la Etapa 1 se leerá conservándolos para distinguirlos.
- Términos de uso y atribución de la OCDE no verificados; documentación técnica de 2025 no revisada (informe técnico final previsto para 2027).
- Factor de replicación de los pesos no confirmado en documentación oficial.

## Etapa 1
- README inicial con problema, población, hipótesis H1 a H5 con su parámetro, criterios de éxito y límites.
- Aprobada por el estudiante la frecuencia por actividad en lugar de los cuatro perfiles.
