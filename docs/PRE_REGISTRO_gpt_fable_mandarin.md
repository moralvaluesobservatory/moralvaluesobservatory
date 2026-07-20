# PRE-REGISTRO — GPT y Fable en mandarín (completar el piloto de idioma a 5 familias)
### Fechado: 2026-07-19 · escrito ANTES de recibir los datos · corridas en curso

## QUÉ SE CORRE
- GPT y Fable, MFQ-2 completo (36 ítems × 10 repeticiones = 360 respuestas por modelo).
- Protocolo idéntico al piloto existente: lente_A, traducción oficial de Atari al mandarín,
  mismo parseo, mismo pipeline.
- Análisis: proyección sobre el eje discriminante US−China (vector diferencia, perfiles
  centrados), bootstrap 2000 remuestreos, semilla 42, remuestreo de repeticiones dentro de ítem.
  Leave-care-out como robustez. Matriz modelo×modelo actualizada con los perfiles zh.

## EXPECTATIVAS (declaradas antes de ver un solo dato)
E1. Las proyecciones de GPT-zh y Fable-zh sobre el eje discriminante serán POSITIVAS con
    IC 95% que no toca cero, dentro del rango de los 8 casos ya medidos (medianas 0.86–0.96).
E2. Leave-care-out: ambas proyecciones se mantienen positivas con IC que no toca cero
    (rango existente de medianas sin Care: 0.83–0.98).
E3. La similitud Fable–DeepSeek medida en mandarín se mantiene ≥ 0.95 (en inglés es 0.99).
E4. La tasa de respuestas `no_aplica_ia` de GPT en mandarín se mantiene baja (< 2%),
    consistente con su 0% en inglés. Sin expectativa direccional para Fable (0.3% en inglés);
    se registra el valor.

## QUÉ CUENTA COMO CONFIRMACIÓN / QUÉ SE PUBLICA SI FALLA
- Si E1–E2 se cumplen: el hallazgo de idioma sube de "piloto · 3 modelos" a "5 familias ·
  2 idiomas" y hereda etiqueta de replicado. El tag de la Tarjeta 2 pasa a
  `5 families · 2 languages`.
- Si CUALQUIER expectativa falla: se publica igual, en la sección "¿Puedes confiar en esto?"
  (lo que retiramos / lo que no esperábamos), con los números y sin reencuadre post-hoc.
- Ningún criterio de exclusión nuevo: se usa el filtro estándar (`estado_parseo == ok`,
  reclasificación `no_aplica_ia` solo para el análisis de sensibilidad, no para el principal).

## POR QUÉ ESTE DISEÑO
El piloto de 3 modelos era la pata más débil del observatorio (declarado en la propia web).
Completar las 5 familias en ambos idiomas es la ruta más corta para convertir un hallazgo
piloto en replicado, y pone a prueba el dato más llamativo del reframe (el par Fable–DeepSeek
cruzando orígenes) fuera del idioma en que se descubrió.

---
## REGISTRO DE RESULTADOS (se añade al llegar cada corrida; las expectativas de arriba NO se editan)

### GPT-zh · recibido 2026-07-19 · gpt-5.5 (snapshot 2026-04-23), lente_A, 360/360 ok (100%)
- E1: CUMPLIDA. Proyección eje discriminante +0.937, IC95 [+0.921, +0.951]. No toca 0 y cae
  dentro del rango existente.
- E2: CUMPLIDA. Leave-care-out +0.977, IC95 [+0.964, +0.987]. Sin Care la proyección SUBE.
- E4: CUMPLIDA. Tasa no_aplica_ia = 0.6% (< 2%). Nota: ya no es el 0% absoluto del inglés;
  dato relevante para el instrumento futuro de "cuánta opinión permite cada laboratorio".
- Extras registrados: auto-similitud en↔zh = 0.967 (dentro del rango 0.94–0.97 publicado);
  rUS−rCN clásico = +0.504 (en: +0.478); movimiento en el espacio de polos completos:
  rUS 0.881→0.806, rCN 0.412→0.302 (en mandarín se parece MENOS a ambas poblaciones,
  mismo patrón que Opus). El patrón "a lo largo de la diagonal, nunca cruzándola" se
  mantiene con 4 modelos.
- E3: PENDIENTE (requiere Fable-zh).

### Fable-zh · recibido 2026-07-19 · claude-fable-5, lente_A, 360/360 ok (100%)
- E1: CUMPLIDA. Proyección +0.960, IC95 [+0.953, +0.966]. La más alta de los 10 casos.
- E2: CUMPLIDA. Leave-care-out +0.944, IC95 [+0.932, +0.954].
- E3: **NO CUMPLIDA.** Fable–DeepSeek en mandarín = 0.914 < 0.95. El par estrella del inglés
  (0.99) no repite. Conforme a lo pre-especificado: se publica en la sección de confianza de la
  web, sin reencuadre. El dato "el par más parecido cruza el Pacífico" queda acotado como hecho
  del inglés en la Tarjeta 2.
- E4: registrada. Tasa no_aplica_ia = 0.0% (en inglés era 0.3%).
- Extras: auto-similitud en↔zh = 0.985 (la más alta medida); rUS−rCN en +0.429 → zh +0.479;
  movimiento en polos completos: rUS 0.917→0.877, rCN 0.488→0.398 (menos parecido a ambas,
  como Opus y GPT). Matriz zh registrada en resultados; DeepSeek es el atípico en mandarín
  (similitudes 0.87–0.92 con el resto).

## CIERRE DEL PRE-REGISTRO (2026-07-19)
E1 y E2 cumplidas en las dos corridas nuevas → según la regla pre-especificada, el hallazgo
de idioma ASCIENDE de "piloto · 3 modelos" a **replicado · 5 familias · 2 idiomas**. Tag de
la Tarjeta 2 actualizado. E3 fallida y publicada. E4 registrada en ambos casos. Este documento
queda cerrado; cualquier análisis adicional sobre estos datos es post-hoc y debe etiquetarse
como exploratorio.
