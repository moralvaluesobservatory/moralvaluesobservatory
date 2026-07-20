# VERIFICACIÓN ESTADÍSTICA PROFUNDA — bootstrap, IC, Holm-FDR, costura
### Generada 2026-07-04 · Todo desde crudos, con semillas fijas (reproducible)

## 1. COSTURA DEL INSTRUMENTO CHINO — RESUELTA (con matiz)
La verificación ítem-por-ítem que se creía pendiente NO ES POSIBLE, por una razón estructural:
el polo humano chino (Study 1c) viene AGREGADO por fundamento (6 valores), no por ítem. Los
datos humanos no existen a nivel de ítem individual.
- ✅ Lo verificable SÍ está bien: la traducción administrada tiene los 36 ítems canónicos del
  MFQ-2, 6 por fundamento, mapeados correctamente (item_id coinciden 100% con el canónico).
- CAVEAT CORRECTO A DECLARAR (reemplaza al anterior): "No se puede verificar ítem-por-ítem que
  la traducción administrada y la usada para el polo humano chino coincidan, porque el polo
  humano solo está disponible agregado por fundamento. Ambos son MFQ-2 de 36 ítems de fuentes
  de Atari, pero la correspondencia exacta de wording a nivel de ítem no es auditable con los
  datos publicados."

## 2. BOOTSTRAP IC95% — Correlación WEIRD (Hallazgo 1) — 2000 remuestreos, semilla 42
| Sistema | IC2.5 | mediana | IC97.5 |
|---|---|---|---|
| Opus 4.8 | 0.900 | 0.932 | 0.959 |
| GPT | 0.971 | 0.983 | 0.991 |
| DeepSeek | 0.916 | 0.951 | 0.975 |
| GLM | 0.918 | 0.953 | 0.978 |
| Fable | 0.951 | 0.970 | 0.983 |
→ Todos los IC muy por encima de 0. El más bajo (Opus) es 0.90. Hallazgo WEIRD ROBUSTO.

## 3. BOOTSTRAP IC95% — Piloto idioma, (rUS − rChina) — semilla 7
| Caso | IC2.5 | mediana | IC97.5 | US>China sig? |
|---|---|---|---|---|
| GLM inglés | 0.417 | 0.465 | 0.511 | sí |
| GLM chino | 0.406 | 0.463 | 0.512 | sí |
| Opus inglés | 0.439 | 0.467 | 0.494 | sí |
| Opus chino | 0.475 | 0.532 | 0.576 | sí |
| DeepSeek inglés | 0.326 | 0.385 | 0.437 | sí |
| DeepSeek chino | 0.237 | 0.291 | 0.347 | sí |
→ Los 6 casos: IC no cruza 0. Todos prefieren US sobre China significativamente, en ambos
idiomas. Incluso DeepSeek chino (el más cercano a China) sigue en 0.24-0.35. Piloto ROBUSTO.

## 4. HOLM-FDR — Tanda 3-opciones (Hallazgo 2, ¿eligen apropiado > azar 1/3?)
| Sistema | p bruto | Holm | FDR | signif |
|---|---|---|---|---|
| Opus | 5.6e-58 | 2.8e-57 | 2.8e-57 | sí |
| DeepSeek | 3.7e-13 | 3.7e-13 | 3.7e-13 | sí |
| GPT | 1.7e-25 | 6.8e-25 | 4.3e-25 | sí |
| GLM | 4.9e-15 | 1.5e-14 | 6.1e-15 | sí |
| Fable | 4.9e-15 | 1.5e-14 | 6.1e-15 | sí |
→ Los 5 sobreviven Holm y FDR con márgenes enormes. Eligen el principio apropiado al contexto
muy por encima del azar.

## 5. DESCONEXIÓN DECLARADO-ELEGIDO (Hallazgo 2) — dos pruebas cuantitativas
**a) Descomposición de varianza:** la varianza de la elección ENTRE DILEMAS (0.265) es 7.2× la
varianza ENTRE SISTEMAS (0.037). El dilema explica la elección 7× más que el modelo.
**b) Correlación declarado-elegido entre sistemas: r = −0.28** (nula/negativa). Lo que un modelo
declara NO predice lo que elige. DeepSeek declara la mayor proporcionalidad (+1.78) pero elige
de las más bajas (0.45).
→ Doble evidencia de la desconexión. Aritmética honesta: la incertidumbre va sobre los 7 dilemas
independientes (no sobre repeticiones); por eso el argumento es la descomposición de varianza y
la correlación entre sistemas, no un p-valor sobre repeticiones.

## RESUMEN DE ROBUSTEZ
| Hallazgo | Prueba | Veredicto |
|---|---|---|
| 1. Silueta WEIRD | Bootstrap IC | 🟢 ROBUSTO (IC 0.90-0.99, lejos de 0) |
| 2. Desconexión | Varianza 7×, r=-0.28, Holm-FDR | 🟢 ROBUSTO (doble evidencia) |
| 3. Piloto idioma | Bootstrap IC | 🟢 ROBUSTO (6/6 IC no cruzan 0) |
Los tres hallazgos centrales sobreviven la verificación estadística desde crudos.
