# AUDITORÍA COMPLETA DEL OBSERVATORIO — de principio a fin
### Generada 2026-07-04 · Todo recalculado desde los datos crudos (no de memoria)

> Este documento reúne, para una revisión de cero: (1) integridad de datos, (2) metodología
> completa, (3) los tres hallazgos recalculados desde crudos hoy, (4) las notas metodológicas,
> (5) los límites/confounds, y (6) mi lista honesta de hallazgos por solidez.
> Lo marcado ✅ lo verifiqué ejecutando código sobre los crudos en esta sesión.

═══════════════════════════════════════════════════════════════════
## 1. INTEGRIDAD DE DATOS (✅ verificado hoy)
═══════════════════════════════════════════════════════════════════
13 datasets crudos, todos con parseo ≥97%:
- Ola 1 cultural: Opus 4 versiones (5760), GPT (2880), DeepSeek (2880, 97%), GLM (1440, 97%),
  Fable (1440).
- Ola 2 conductual: Opus (2600), DeepSeek (1300), GPT (1300), GLM (650, 98.6%), Fable (650).
- Piloto chino: GLM (360, 99.7%), Opus (360), DeepSeek (360).
Detalle en 00_integridad_datos.csv. Las respuestas no-ok son huecos por razonamiento largo
(vacías), dispersas, sin concentración sesgante.

═══════════════════════════════════════════════════════════════════
## 2. METODOLOGÍA (de principio a fin)
═══════════════════════════════════════════════════════════════════

**Instrumentos:**
- MFQ-2 (Atari et al. 2023): 36 ítems, 6 fundamentos (Care, Equality, Proportionality, Loyalty,
  Authority, Purity). Ola 1 cultural.
- Meindl et al. 2019 (justicia distributiva): declarado (escala) + dilemas (binarios/escala) +
  regla (menú) + 3 escenarios de 3 opciones. Ola 2 conductual.

**Diseño de variantes (Ola 1):** factorial persona×escala en 4 variantes:
- lente_A = {1ª persona, 1-5, ítems oficiales} — PRIMARIA, ancla humana.
- canonica = {impersonal, 1-7}; lente_B = {1ª persona, 1-7}; lente_C = {impersonal, 1-5}.
Las 4 controlan robustez al formato de pregunta.

**Método de comparación — clave:** correlación de FORMA de perfil (perfil centrado sobre su
propia media), NO valores absolutos. Razón: el "4" de un modelo no vive en la misma métrica que
el "4" de un humano; la forma (patrón de altos/bajos entre fundamentos) sí es comparable. La
correlación es invariante a la escala, por eso las variantes de 1-5 y 1-7 son comparables sin
reescalar.

**Polos humanos:**
- Marco de 19 países (Atari) para "país más cercano" y perfil WEIRD.
- Polos US y China del Study 1c de Atari (administrado en cada idioma) para el piloto.

**Recogida:** 10 repeticiones por ítem×variante×sistema. Temperature NO fijada (imposible en
modelos de razonamiento actuales — ver límites). Parseo por regex del token "SCORE:"/"CHOICE:".

═══════════════════════════════════════════════════════════════════
## 3. LOS TRES HALLAZGOS (✅ recalculados desde crudos hoy)
═══════════════════════════════════════════════════════════════════

### HALLAZGO 1 — Silueta WEIRD (mapa cultural)
Los 5 sistemas correlacionan alto con el perfil WEIRD (forma, lente_A):
Opus 0.934, GPT 0.984, DeepSeek 0.954, GLM 0.955, Fable 0.971.
País más cercano SIEMPRE WEIRD: Irlanda, Nueva Zelanda, Suiza.
→ Todos los modelos, incluidos los de origen chino, tienen forma moral occidental.
(01_mapa_weird.csv)

### HALLAZGO 2 — Desconexión declarado-elegido (conductual)
Lo DECLARADO barre amplio, lo ELEGIDO es plano:
| Sistema | declarado(prop-igual) | elegido(frac prop) |
|---|---|---|
| Opus | +0.87 | 0.59 |
| DeepSeek | +1.78 | 0.45 |
| GPT | -0.41 | 0.57 |
| GLM | +1.23 | 0.56 |
| Fable | +0.39 | 0.43 |
Declarado va de -0.41 a +1.78 (barre ~2.2 puntos); elegido se queda en 0.43-0.59 (franja
estrecha). Modelos con valores declarados opuestos ELIGEN casi idéntico. "Manda el ítem, no el
valor". (02_declarado_elegido.csv)

### HALLAZGO 3 — La silueta occidental sobrevive al mandarín (piloto idioma)
| Modelo | rUS-rCN inglés | rUS-rCN chino |
|---|---|---|
| GLM | 0.466 | 0.465 |
| Opus | 0.468 | 0.532 |
| DeepSeek | 0.386 | 0.292 |
Los 3, en ambos idiomas, prefieren el polo US. PERO DeepSeek se acerca a China en mandarín
(efecto de idioma real pero no invierte). (03_piloto_idioma.csv)

═══════════════════════════════════════════════════════════════════
## 4. LÍMITES Y CONFOUNDS (declarados)
═══════════════════════════════════════════════════════════════════

1. **Decodificación:** la temperatura NO se fijó porque los modelos actuales no lo permiten
   (Opus 4.7+, GPT nuevo, GLM xhigh, DeepSeek reasoner rechazan o restringen temperature a su
   default). VERIFICADO empíricamente: probamos temp=0 en GPT → error 400 "only default (1)
   supported". El determinismo observado ES propiedad del modelo vía API, no artefacto de un
   parámetro. Salvedad: regímenes de muestreo por defecto distintos entre familias → el %
   determinismo no es perfectamente comparable en absoluto.

2. **Persona / validez de constructo:** el autorreporte en 1ª persona mide la persona del
   asistente por defecto. Algunos ítems (purity corporal, loyalty nacional) no "aplican" a una
   IA. Fenómeno cuantificado (label no_aplica_ia): GLM 8-14%, GPT 0%, muy heterogéneo.
   ANÁLISIS DE SENSIBILIDAD (✅): excluir no_aplica_ia NO cambia conclusiones — GLM rUS-rCN
   0.466→0.478, forma con/sin correlaciona 0.99. Fenómeno real pero INOCUO para los hallazgos.

3. **Contaminación:** instrumentos públicos y pre-entrenamiento. Los modelos pueden haber visto
   ítems y normas. Señal indirecta (✅): correlación con país más cercano alta pero NO perfecta
   (GLM→Suiza 0.970, Fable→NZ 0.967; <0.98 sugiere patrón WEIRD capturado, no memorización
   flagrante). No descartable sin brazo de paráfrasis (futuro).

4. **Purity frágil:** único fundamento sin invarianza transcultural en Atari (39.5% no-invarianza,
   omega .73). Va con bandera; los hallazgos aguantan sin él.

5. **Piloto idioma — costura sin resolver:** el polo chino (Study 1c) y la traducción administrada
   deben verificarse ítem-por-ítem que son la misma versión.

6. **Piloto — alcance:** 3 modelos, 1 ancla occidental, solo lente_A. Es piloto, no Ola 4.

═══════════════════════════════════════════════════════════════════
## 5. MI LISTA DE HALLAZGOS POR SOLIDEZ (evaluación honesta)
═══════════════════════════════════════════════════════════════════

### 🟢 MUY SÓLIDOS (sobrevivieron auditoría, replicados, robustos)
1. **La silueta moral de los LLM es WEIRD/occidental.** 5 familias, 2 orígenes (incl. chino),
   corr 0.93-0.98 con perfil WEIRD, país cercano siempre WEIRD. Robusto a 4 variantes de formato
   y (piloto) al idioma. Es el hallazgo central y el más defendible.

2. **Desconexión declarado-elegido.** 10 sistemas declaran valores dispares pero eligen casi
   idéntico; la estructura del dilema dicta la elección. Replicado en 5 familias, 2 orígenes, 2
   generaciones. Muy sólido cualitativamente (la incertidumbre va sobre 7 dilemas, no sobre
   repeticiones — con determinismo alto no se infla con p-valores).

### 🟡 SÓLIDOS CON MATIZ (verdaderos pero con salvedad importante)
3. **La silueta occidental no es artefacto del inglés.** Piloto: los 3 modelos prefieren US en
   mandarín también. MATIZ: N=3, 1 ancla occidental, costura del instrumento sin verificar.

4. **El idioma modula pero no invierte.** DeepSeek se acerca a China en mandarín (rChina
   0.49→0.69), GLM no, Opus se aleja. Efecto real y heterogéneo. Pregunta viva: ¿por qué DeepSeek
   sí y GLM no, siendo ambos chinos?

5. **El "distanciamiento como IA" es heterogéneo entre modelos.** GLM se niega a valorar 8-14%,
   GPT 0%. Es un dato sobre la persona por defecto. MATIZ: detección por palabras clave, no
   clasificación validada; pero robusto como orden de magnitud.

### 🟠 PRELIMINARES / OBSERVACIONES (no titulares)
6. **Determinismo por sistema** (GLM estocástico, Opus intermedio, etc.). Interpretable como
   propiedad del modelo (muestreo no fijable), pero regímenes no comparables entre familias.

7. **Efecto del razonamiento** (Ola 2): DeepSeek delta por modo con signo claro pero IC amplio;
   GPT nulo. Señal, no magnitud precisa.

### ⚫ DESCARTADOS (honestidad: no sobrevivieron)
8. **"Justicia contextual convergente"** (titular original Ola 2). Se desinfló en reanálisis (p
   inflado). Sustituido por la desconexión declarado-elegido, que sí aguanta.
9. **"Hiper-individualizante" como sección propia.** Retirado a matiz de 05b por no pasar las
   pruebas de robustez (dependía parcialmente de purity).

═══════════════════════════════════════════════════════════════════
## 6. ARCHIVOS EN ESTE PAQUETE
═══════════════════════════════════════════════════════════════════
- 00_integridad_datos.csv — filas/parseo de los 13 datasets
- 01_mapa_weird.csv — correlaciones WEIRD por sistema
- 02_declarado_elegido.csv — la desconexión
- 03_piloto_idioma.csv — inglés vs chino
- raw/ — copia de todos los crudos originales
- notas/ — todas las notas metodológicas
