# RESULTADO — Piloto de idioma (sección 06) para el observatorio
### ¿Sobrevive la silueta occidental cuando el MFQ-2 se administra en mandarín?
### Fechado 2026-07-04 · Para que el otro chat actualice la sección 06 (estaba "pending")

> Contexto: la sección 06 estaba en plantilla, esperando las corridas en chino. Ya están:
> GLM, DeepSeek y Opus, administrados en mandarín (lente_A, traducción oficial de Atari,
> 36 ítems × 10 reps cada uno, parseo 100%). Aquí van los datos, la lectura honesta, y las
> salvedades. Es un PILOTO, no la Ola 4 completa.

---

## EL TITULAR (afirmación, no pregunta)
**Measured in Mandarin, all three models still resemble the US human profile more than the
Chinese one — but the language effect is real and uneven, not zero.**

La silueta occidental NO es un mero artefacto del inglés: sobrevive al cambio de idioma. Pero
el idioma modula el resultado de forma heterogénea entre modelos (un modelo chino sí se acercó
al polo chino en mandarín).

---

## LOS DATOS (correlación de forma, perfil centrado, lente_A)

Polos humanos: Study 1c de Atari et al. (US y China, administrados en su idioma).

**Correlación con cada polo, inglés vs. mandarín:**

| Modelo | origen | rUS (en) | rChina (en) | rUS (zh) | rChina (zh) |
|---|---|---|---|---|---|
| GLM 5.2 | China | 0.835 | 0.369 | 0.857 | 0.391 |
| DeepSeek (thinking) | China | 0.855 | 0.491 | 0.983 | 0.691 |
| Opus 4.8 | US | 0.872 | 0.404 | 0.807 | 0.274 |

**Preferencia neta por US sobre China (rUS − rChina):**

| Modelo | inglés | mandarín | cambio |
|---|---|---|---|
| GLM | 0.466 | 0.465 | −0.001 |
| DeepSeek | 0.364 | 0.292 | −0.072 |
| Opus | 0.468 | 0.532 | +0.064 |

**Los tres, en ambos idiomas, prefieren US sobre China.** Ninguno cruza al lado chino.

**Correlación de forma inglés-vs-mandarín (mismo modelo):** GLM 0.94, DeepSeek 0.92, Opus 0.97.
Cada modelo mantiene casi el mismo perfil en los dos idiomas.

---

## EL MATIZ HONESTO — DeepSeek sí se movió hacia China

Aunque la preferencia neta sigue siendo pro-US en todos, el acercamiento AL polo chino (rChina)
no fue uniforme:
- **GLM:** rChina 0.369 → 0.391 (+0.022, casi nada)
- **Opus:** rChina 0.404 → 0.274 (−0.129, se ALEJA de China)
- **DeepSeek:** rChina 0.491 → 0.691 (**+0.200, acercamiento real**)

DeepSeek, en su propio idioma, se acercó apreciablemente al perfil humano chino — no lo bastante
para superar su parecido con US, pero en la dirección que predeciría la hipótesis "corpus". Es
el único de los tres que lo hizo. Y es el modelo chino más estocástico del panel.

---

## QUÉ HIPÓTESIS GANA (de las tres pre-registradas)
1. **Solo-idioma** (todos se mueven a China por igual): DESCARTADA. Opus se alejó, GLM no se
   movió.
2. **Suelo occidental** (la silueta occidental es estructural, no del idioma): SOSTENIDA en lo
   principal — los tres siguen prefiriendo US en ambos idiomas.
3. **Corpus** (los modelos chinos vuelven a casa en su idioma): PISTA PARCIAL — DeepSeek se
   acercó a China, GLM no. No se cumple de forma limpia, pero DeepSeek deja una señal.

**Lectura combinada:** el idioma modula pero no invierte la silueta occidental. El resultado
central de 05b (todos prefieren US) aguanta en mandarín. Pero el efecto del idioma es real y
específico de cada modelo, no nulo.

---

## POR QUÉ ESTO FORTALECE EL OBSERVATORIO
Un resultado donde "nada se mueve" habría sido sospechosamente limpio. Este es más creíble: la
afirmación central sobrevive la objeción más seria (¿era solo el inglés?), y a la vez el idioma
muestra un efecto heterogéneo genuino. Deja una pregunta viva y falsable para la Ola 4 completa:
¿por qué DeepSeek se acerca a China en mandarín y GLM no, siendo ambos de origen chino?

---

## SALVEDADES (declarar en la web)
1. **Piloto, no Ola 4 completa:** 3 modelos, un solo modelo occidental de ancla (Opus), una sola
   variante (lente_A). No incluye brazo de priming de persona ni test formal de invarianza.
2. **La costura del instrumento (sin resolver):** el polo humano chino (Study 1c) y la traducción
   administrada a los modelos deben verificarse ítem-por-ítem que son la MISMA versión. El
   resultado asume que lo son. Es el caveat que la propia sección 06 ya señalaba.
3. **Traducción:** ítems del repositorio oficial de Atari (incluye la adaptación "familia" en
   LOYA_34); los system prompts en mandarín son traducción propia asistida, no validada por
   nativo. Token "SCORE:" mantenido en inglés para reutilizar el parser.
4. **Determinismo heterogéneo:** GLM tuvo 43 huecos por razonamiento largo (reintentados, 359/360
   final); Opus y DeepSeek 360/360 limpio. DeepSeek es el más estocástico.

## ARCHIVOS
- Crudos: `glm_zh_completo.csv`, `opus_zh_crudo.csv`, `deepseek_zh_crudo.csv` (360 filas c/u).
- Polos: `polos_1c_36items.csv` (US, China, Study 1c).
- Nota metodológica previa: `NOTA_chino_lenteA_unica.md`.

## SUGERENCIA DE COPY PARA LA SECCIÓN 06 (registro Epoch, en inglés)
> We administered the MFQ-2 in Mandarin to two China-built models (GLM, DeepSeek) and one US
> model (Opus) as an anchor, using the instrument's official Chinese translation. All three
> still correlate more with the US human pole than the Chinese one, in Mandarin as in English.
> The Western profile is not merely an artifact of the language of administration. But the
> language effect is not zero: DeepSeek moved noticeably toward the Chinese pole in Mandarin
> (its correlation with China rose from 0.49 to 0.69), while GLM did not move and Opus moved
> away. Language modulates the profile without inverting it. Why one China-built model shifts
> and the other does not is the open question the full factorial (wave 4) is designed to answer.
> Caveat: the Mandarin translation is not yet verified item-for-item against the wording used to
> collect the human China pole.
