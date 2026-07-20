# RECLASIFICACIÓN — Label `no_aplica_ia` (respuestas donde el modelo se niega a valorar)
### Creado 2026-07-04 · ACTUALIZADO con resultados de sensibilidad + script reproducible

## QUÉ ES ESTO
Análisis de las respuestas donde un modelo pone un número PERO declara que no tiene postura
sobre el ítem (ej: "Como IA no tengo opiniones sobre distribución de riqueza. SCORE: 1"). En
esos casos el número es RELLENO, no un valor real. Responde a la crítica de validez de
constructo: un autorreporte en 1ª persona mide la persona del asistente, y algunos ítems no le
"aplican" a una IA.

## CÓMO ESTÁN LOS ARCHIVOS
Cada `*_v2.csv` es el crudo original SIN MODIFICAR, con una columna nueva: `estado_v2`.
- La columna original `estado_parseo` NO se tocó (trazabilidad).
- `estado_v2` = `no_aplica_ia` cuando la respuesta cae en el criterio; si no, hereda el estado
  original (`ok`, `sin_numero`, etc.).

## REPRODUCIBILIDAD
`reproducir_reclasificacion.py` (en la raíz del paquete) regenera los 8 `*_v2.csv` desde `raw/`.
Las listas de frases del criterio (`FRASES_NO_OPINION`, `FRASES_SI_RAZONA`) están EXPLÍCITAS en
el script — el criterio no es prosa, es código auditable.

## CRITERIO (pre-especificado, opción laxa)
Una respuesta `ok` se reclasifica a `no_aplica_ia` SI Y SOLO SI:
1. Declara explícitamente NO tener postura/opinión/creencia personal sobre el contenido
   (frases tipo "no personal opinion", "do not hold personal belief", "没有个人观点"), Y
2. NO razona sobre el contenido después (no hay "but/however/pero/但..." + análisis del ítem).

Ejemplos:
- INVÁLIDA (`no_aplica_ia`): "No tengo opiniones sobre esto. SCORE: 1" → el 1 es relleno.
- VÁLIDA (`ok`): "No siento emociones PERO estoy diseñado para valorar el cuidado. SCORE: 4"
  → el 4 sí refleja una valoración (se distancia por estilo, pero valora).
- VÁLIDA (`ok`): "No tengo postura personal, PERO viendo el contenido la igualdad tiene valor
  aunque ignora incentivos, por eso neutral. SCORE: 3" → sí razona, el 3 refleja el análisis.

## RESULTADO (% de respuestas ok reclasificadas a no_aplica_ia)
| Modelo | % no_aplica_ia |
|---|---|
| GLM chino | 14.2% |
| GLM inglés | 8.6% |
| Opus chino | 2.2% |
| DeepSeek inglés | 1.9% |
| Fable inglés | 0.3% |
| Opus inglés | 0.1% |
| GPT inglés | 0.0% |
| DeepSeek chino | 0.0% |

## HALLAZGO
El fenómeno NO es uniforme: GLM se niega a valorar mucho más que los demás (8-14%), GPT casi
nunca (0%). Es una diferencia de PERSONA POR DEFECTO entre modelos, no de valores. Se concentra
en ítems que presuponen cuerpo/nación/opinión política (Purity, Loyalty, Equality).

## ⭐ ANÁLISIS DE SENSIBILIDAD — EL FENÓMENO ES INOCUO PARA LAS CONCLUSIONES
La pregunta clave: ¿cambian los resultados al excluir `no_aplica_ia`? Recalculado desde crudos:

| Caso | rUS−rChina CON | rUS−rChina SIN | corr(perfil con, sin) |
|---|---|---|---|
| GLM inglés (el más afectado, 8.6%) | +0.466 | +0.478 | 0.99 |
| GLM chino (14.2%) | +0.465 | +0.473 | 0.9996 |
| Opus chino (2.2%) | +0.532 | +0.520 | 0.9994 |

→ Excluir las respuestas "no aplico" mueve las correlaciones <0.02 y la forma del perfil
correlaciona 0.99+ con y sin. **El fenómeno es real pero COSMÉTICO para las conclusiones.**
Ni la posición WEIRD ni el resultado del piloto de idioma cambian.

**Cómo responder a la crítica de validez de constructo:** el fenómeno existe, está cuantificado
y es heterogéneo entre modelos (declararlo como límite de comparabilidad), pero se verificó
empíricamente que NO distorsiona ningún hallazgo. La crítica queda neutralizada con número, no
con argumento.

## LIMITACIÓN DE ESTA DETECCIÓN
Es por frases clave, no clasificación validada a mano. Puede tener falsos +/-. Por eso el
argumento defendible es el de SENSIBILIDAD (el resultado aguanta con o sin, así que la precisión
exacta del filtro no es crítica), no el conteo exacto. Para un conteo definitivo haría falta
revisión manual de una muestra con doble codificador.
