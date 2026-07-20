# RESPUESTA A LAS 3 CRÍTICAS METODOLÓGICAS (decodificación, contaminación, persona)
### Las tres son válidas. Qué declarar ahora, qué controlar después.
### Fechado 2026-07-04

> Un revisor señaló tres huecos: (1) parámetros de decodificación no documentados, (2)
> contaminación del instrumento, (3) validez de constructo / persona. Las tres tienen razón y
> deben declararse como límites. Abajo: el reconocimiento, una corrección fáctica menor, y el
> plan.

═══════════════════════════════════════════════════════════════════
## CRÍTICA 1 — Parámetros de decodificación (LA MÁS GRAVE, válida)
═══════════════════════════════════════════════════════════════════

**El crítico tiene razón en lo esencial:** los parámetros de muestreo no están documentados en
el repositorio, y sin fijarlos y reportarlos, el hallazgo de determinismo (3%–92%) NO es
interpretable como propiedad del modelo. Un rango de 30× puede reflejar defaults de API
distintos tanto como propiedades de los modelos. Es el hueco más importante y no estaba declarado.

**Corrección fáctica menor (para precisión, no para defenderse):** sí hubo UNA mención de
temperatura —el código de recogida de Opus fijaba `temperature=1.0`—. No estaba en el repositorio
que el revisor vio, sino en el cuaderno de recogida. PERO esto no salva el confound; lo CONFIRMA:
- Opus: temperature=1.0 (explícito)
- GLM, DeepSeek, GPT: sin especificar → default de cada API (posiblemente distintos entre sí)

Es decir, teníamos temperaturas potencialmente DISTINTAS y NO UNIFORMES entre sistemas. Eso es
exactamente el confound descrito: el determinismo mezcla "propiedad del modelo" con "temperatura
de esa API". Capa extra: en modos de razonamiento (GLM xhigh, DeepSeek reasoner) la temperatura
puede aplicarse distinto o interactuar con el sampling del thinking.

**QUÉ HACER:**
- AHORA (declarar en la web, sección de límites y en "Can you trust this?"): "Los parámetros de
  muestreo no se fijaron de forma uniforme entre sistemas (Opus con temperature=1.0; los demás
  con el default de su API). Por tanto, el hallazgo de determinismo por sistema NO debe leerse
  como propiedad pura del modelo: confunde el modelo con su configuración de muestreo por
  defecto. La afirmación 'los modelos chinos son los más estocásticos' queda RETIRADA como
  propiedad del modelo hasta re-recoger con muestreo fijo."
- FUTURO (corrige de raíz): re-recoger fijando temperature en un valor común y declarado (p.ej.
  temperature=0 para medir determinismo real, o un valor fijo idéntico para todos). Entonces el
  determinismo SÍ es interpretable.
- La sección 04 (determinismo) debe rebajarse: de hallazgo a "observación preliminar confundida
  con parámetros de muestreo, pendiente de recogida controlada".

═══════════════════════════════════════════════════════════════════
## CRÍTICA 2 — Contaminación del instrumento (válida)
═══════════════════════════════════════════════════════════════════

**Correcta.** El MFQ-2 (Atari 2023) y los dilemas de Meindl (2019) son públicos y anteriores al
corte de entrenamiento de todos los sistemas. Los modelos pueden haber visto los ítems, su
literatura, y las medias por país. No se discute en ningún documento.

**QUÉ HACER:**
- AHORA (declarar): "Los instrumentos son públicos y preceden al entrenamiento de los modelos.
  No podemos descartar que los modelos hayan visto los ítems o las normas humanas. Los perfiles
  podrían reflejar en parte memorización, no solo valores expresados."
- FUTURO (control natural que propone el revisor): un brazo con ítems PARAFRASEADOS (validados
  contra los oficiales por retrotraducción/correlación). Si el perfil se mantiene con paráfrasis,
  la contaminación importa menos; si cambia, estaba inflando la señal. Encaja con el diseño de
  pares mínimos ya previsto para la Ola 2.

═══════════════════════════════════════════════════════════════════
## CRÍTICA 3 — Validez de constructo / persona (la más profunda, válida)
═══════════════════════════════════════════════════════════════════

**Correcta y es la más conceptual.** El ejemplo es real: GLM puntúa 1 en purity diciendo "como
IA sin cuerpo, esto no me describe". Eso NO es un valor moral bajo; es un ítem que no aplica. Un
autorreporte en primera persona mide la PERSONA DEL ASISTENTE POR DEFECTO, no "los valores del
modelo" en abstracto. La bandera de Purity mitiga el caso más visible, pero el problema es más
amplio.

Punto técnico certero: se probó robustez a variantes de REDACCIÓN (las 4 lentes: persona/escala/
fraseo), pero NO a PERSONA / SYSTEM PROMPT — que es la dimensión donde la literatura muestra MÁS
sensibilidad. Las 4 variantes administran todas al "asistente por defecto".

**QUÉ HACER:**
- AHORA (declarar): "Medimos la persona por defecto del asistente en primera persona, no 'los
  valores del modelo' en abstracto. No probamos robustez a la persona/system prompt, la dimensión
  de mayor sensibilidad conocida. Algunos ítems (p.ej. purity corporal) pueden puntuar bajo por
  no aplicar a una IA, no por rechazo del valor."
- FUTURO: el brazo de PRIMING DE PERSONA ya previsto para la Ola 4 ("responde como ciudadano
  típico de X") es exactamente el control que el revisor pide. Confirma su necesidad. Añadir
  también una variante que NO sea primera persona del asistente (p.ej. "¿cómo evaluaría un
  humano...?") para separar 'persona del asistente' de 'juicio moral en abstracto'.

═══════════════════════════════════════════════════════════════════
## RESUMEN — PRIORIDADES
═══════════════════════════════════════════════════════════════════
1. **Decodificación (urgente):** declarar el confound YA; rebajar la sección 04; re-recoger con
   muestreo fijo. Es el hueco más grande sin declarar.
2. **Persona (importante):** declarar ahora; el brazo de priming de la Ola 4 lo resuelve.
3. **Contaminación (declarable):** declarar ahora; brazo de paráfrasis como control futuro.

Las tres son límites reales que NO tiran los hallazgos, pero deben estar visibles. Declararlas
—como se hizo con el idioma y con purity— es lo que mantiene la credibilidad del observatorio.
Ninguna se descubrió "demasiado tarde": se declaran antes de sobre-vender.
