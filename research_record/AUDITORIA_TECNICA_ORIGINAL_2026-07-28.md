# Auditoría técnica de `mvo_core.zip`

**Fecha:** 28 de julio de 2026  
**Objeto:** revisar la corrección sobre generaciones repetidas y comprobar la coherencia entre datos, análisis, resultados, documentación y pruebas.

## Veredicto

La corrección principal va en la dirección correcta: las generaciones repetidas del mismo ítem o escenario ya no se utilizan como si fueran unidades independientes para construir los intervalos. Los análisis principales remuestrean ítems o escenarios completos. Al repetir el pipeline, los resultados generados coinciden exactamente con los incluidos en el ZIP, y las 15 pruebas automáticas pasan.

Sin embargo, el paquete **todavía no está listo para sostener la nueva web ni para publicarse como versión 1.0 sin cambios**. El principal resultado distributivo sobrevive a una comprobación independiente, pero la interpretación de “rango humano”, varias comparaciones MFQ y algunas afirmaciones documentales necesitan corrección.

## Comprobaciones superadas

- El ZIP no presenta corrupción (`testzip`: sin errores).
- Se extrajeron 105 entradas; el manifiesto registra 85 archivos, excluyendo carpetas y el propio manifiesto.
- `python -m pytest tests/ -q`: **15 pruebas superadas**.
- `python scripts/analysis/run_all.py`: ejecución completa sin error en el entorno disponible.
- Todos los archivos de `data/results/` regenerados son idénticos a los distribuidos.
- Los cinco archivos DSE utilizan exactamente el mismo diseño de viñetas, identificadores, perfiles y orden aleatorizado.
- No se encontraron claves API en los diez notebooks incluidos.
- Las sumas DSE válidas son CHF 18.000, las proporciones suman 1 y no hay importes negativos.
- Los 65 identificadores Ola 2 coinciden con el registro y sus metadatos.

## La corrección de las repeticiones

### Lo que está bien

Los intervalos de Ola 2 y DSE remuestrean el nivel correcto para generalizar sobre el banco de tareas:

- ítem para escalas y dilemas;
- `set_id` para las asignaciones DSE;
- ítem emparejado para los cambios entre snapshots.

Esto evita el error anterior de usar cientos de generaciones como si fueran cientos de ítems, escenarios o participantes independientes.

### Comprobación independiente del principal resultado DSE

Se comparó el bootstrap actual por escenarios con dos alternativas:

1. media con igual peso para cada escenario;
2. bootstrap jerárquico que remuestrea escenarios y, dentro de ellos, repeticiones.

Los cambios son pequeños y la conclusión descriptiva no cambia. Ejemplos:

| Sistema y tarea | IC actual | IC jerárquico independiente | Referencia humana publicada más baja |
|---|---:|---:|---:|
| Opus, trabajo | 4,31–13,37 % | 4,17–13,61 % | 15 % |
| Opus, familia | 6,25–23,75 % | 5,94–24,38 % | 46 % |
| GPT, familia | 0–3,75 % | 0–4,38 % | 46 % |
| DeepSeek, trabajo | 0 % | 0 % | 15 % |

Incluso en un análisis extremo donde todas las 54 respuestas DSE fallidas de DeepSeek en trabajo fueran repartos iguales, su porcentaje sería 7,5 %, todavía inferior al menor porcentaje humano publicado seleccionado (15 %).

### Lo que debe corregirse todavía

El ICC no demuestra que las llamadas API sean causalmente dependientes. Refleja, sobre todo, que las respuestas al mismo ítem se parecen y que los ítems difieren entre sí. Sirve para justificar inferencia agrupada, pero `effective_n` no debe presentarse como un tamaño muestral humano equivalente ni como una medida universal de “unidades de información”. Es preferible publicar siempre:

- número de ítems o escenarios;
- repeticiones por ítem o escenario;
- regla de remuestreo;
- ICC como diagnóstico secundario.

## Problemas bloqueantes

### 1. “Rango humano” no es todavía una métrica de representación

`dse_human_range.csv` usa el mínimo y máximo de varios porcentajes agregados publicados. `mfq_human_range.csv` usa el mínimo y máximo de 19 medias nacionales estandarizadas. Ninguno es “el intervalo en el que cae la población” en sentido individual.

Por tanto, no es válido afirmar:

> un sistema falla en representar una población cuando cae fuera de ese rango.

Lo que sí puede afirmarse es:

> la estimación del sistema se sitúa por debajo, dentro o por encima del conjunto de valores agregados publicados seleccionados.

La representación exige microdatos, distribuciones, densidad, subgrupos y una métrica de cobertura. Estar dentro de un mínimo-máximo tampoco prueba buena representación: un valor puede caer dentro de un rango muy amplio y estar lejos de casi todas las personas.

**Cambio necesario:** renombrar la métrica actual como `reported_reference_position` o equivalente. Mantener “representation coverage” como métrica futura no calculada.

### 2. `intervals_overlap` compara magnitudes que no son dos intervalos de incertidumbre

El modelo tiene un intervalo bootstrap. El lado humano es un rango de estimaciones puntuales de muestras y subgrupos, sin intervalos de confianza incorporados. La columna `intervals_overlap` y frases como “sin solapamiento de intervalos” pueden hacer creer que la incertidumbre humana fue calculada.

**Formulación correcta:**

> El intervalo bootstrap del sistema queda por debajo de todos los porcentajes humanos puntuales publicados incluidos en esta comparación.

No:

> Los intervalos humano y del modelo no se solapan.

### 3. La comparación inglés–mandarín de MFQ está mal emparejada

`analyze_mfq.py` define `PRIMARY = "canonica"`, pero los archivos mandarín contienen únicamente `lente_A`. Por tanto, el resultado actual compara:

- inglés: variante `canonica`, normalmente escala 1–7;
- mandarín: variante `lente_A`, escala 1–5.

Además:

- GPT inglés agrupa `low` y `high`, mientras mandarín usa solo `high`;
- DeepSeek inglés agrupa `thinking` y `non_thinking`, mientras mandarín usa solo `thinking`;
- la salida marca todas las configuraciones como distintas, pero no muestra que la variante también es distinta.

Al recalcular con `lente_A` y modos emparejados, las correlaciones cambian materialmente:

| Sistema | Resultado distribuido | Reanálisis emparejado |
|---|---:|---:|
| Opus | 0,978 | 0,969 |
| GPT | 0,832 | 0,969 |
| DeepSeek | 0,770 | 0,923 |
| GLM | 0,833 | 0,932 |
| Fable | 0,900 | 0,985 |

**Cambio necesario:** retirar `mfq_language_comparison.csv` actual y regenerarlo con variante y modo emparejados, o conservarlo solo como resultado inválido documentado.

## Problemas importantes

### 4. Se agrupan configuraciones distintas como repeticiones

En Ola 2 y MFQ:

- GPT contiene modos `low` y `high`;
- DeepSeek contiene `non_thinking` y `thinking`.

El pipeline los agrupa bajo un único sistema y trata las 20 respuestas por ítem como repeticiones. Esto puede ser una estimación deliberada del promedio entre modos, pero no es una “configuración exacta”. DeepSeek, además, agrupa endpoints API diferentes bajo la etiqueta de proyecto `deepseek-v4-pro`.

**Cambio necesario:** producir resultados por configuración/modo. Un agregado familiar puede publicarse adicionalmente, claramente etiquetado y con regla de ponderación explícita.

### 5. La procedencia MFQ no cumple la regla declarada

La misión dice que cada cifra humana tiene fuente, página y figura. Esto se cumple razonablemente en el registro DSE, pero no en `mfq2_human_reference_frame.csv`, que contiene 19 medias nacionales sin:

- identificador de fuente por fila;
- página o tabla;
- tamaño muestral;
- incertidumbre;
- fecha de campo;
- notas de comparabilidad.

Además, `references.bib` deja la referencia Atari incompleta y dice que debe verificarse antes de publicar.

**Cambio necesario:** sacar MFQ del núcleo activo hasta completar la procedencia o tratarlo como análisis histórico del Pilot 01.

### 6. Falta `scipy` en `requirements.txt`

`analyze_ola2.py` importa `scipy.stats`, pero `requirements.txt` solo declara NumPy, pandas y pytest. Una instalación limpia siguiendo el README puede fallar.

### 7. El número de ítems declarado para el contraste Ola 2 es incorrecto

`ola2_system_estimates.csv` informa `declared_items = 36`, y la prueba automática exige 36. Sin embargo, `declared_proportionality_minus_equality` utiliza:

- 16 ítems de proporcionalidad;
- 4 ítems de igualdad;
- total efectivo para ese contraste: 20 ítems.

Los otros 16 ítems del bloque declarado no intervienen en esa diferencia.

**Cambio necesario:** publicar `proportionality_items = 16`, `equality_items = 4` y `contrast_items = 20`.

### 8. No todos los resultados publican el número de conglomerados

`dse_coefficients.csv` no incluye el número de escenarios, aunque la documentación afirma que cada estimación lo publica. Sus intervalos usan solo 600 réplicas bootstrap, frente a 10.000 en los análisis principales.

### 9. La afirmación sobre temperatura 0 es incorrecta o no está respaldada

`docs/METRICS.md` y `reliability.py` dicen que el determinismo de 0,65 ocurre “a temperatura 0”. La documentación de recolección muestra temperatura 1,0 o parámetros por defecto para varias colecciones; no hay evidencia en el paquete de que esa cifra corresponda a temperatura 0.

### 10. El umbral de deriva no está preespecificado en el paquete

`WITHDRAWN.md` afirma que ninguna transición alcanza el umbral “que el propio protocolo estableció”, pero el único lugar donde aparece `|d| ≥ 0,5` es el código y la documentación producida en esta revisión. No hay un protocolo previo o preregistro fechado que permita llamarlo preespecificado.

**Cambio necesario:** describirlo como umbral operativo adoptado en el reanálisis, no como criterio previo.

### 11. La comparación DSE debe volver a declarar la desviación del instrumento humano

La documentación anterior reconocía que el diseño fuente variaba la suma entre CHF 3.000, 9.000, 18.000 y 30.000, mientras la recolección de modelos fijó CHF 18.000. El núcleo actual ya no incluye esta advertencia. También debe permanecer visible que las viñetas son una reconstrucción, no el instrumento original verificado.

Esto no elimina el resultado, pero reduce la fuerza de la comparación directa.

### 12. La licencia de `CITATION.cff` no coincide con el tipo de recurso

El archivo se declara `type: dataset`, pero especifica `license: MIT`. Según los documentos del propio repositorio, los datos y documentación son CC BY-SA 4.0 y solo el código es MIT.

### 13. Falta procedencia de recolección para MFQ

Hay notebooks originales para DSE y Ola 2, pero no para MFQ. Los archivos MFQ contienen respuestas crudas, modelos y timestamps, pero el paquete no permite reconstruir desde el código público:

- las cuatro variantes inglesas;
- la traducción mandarín;
- los parámetros exactos de las llamadas.

### 14. Las pruebas automáticas no verifican todo lo que afirman

`CONTENIDO.txt` dice que las pruebas comprueban que ninguna estimación usa filas como tamaño muestral. En realidad, las pruebas revisan solo algunas salidas. Tampoco verifican:

- que `dse_coefficients.csv` lleve escenarios;
- que inglés y mandarín usen la misma variante;
- que los modos no se mezclen;
- que todos los hashes del manifiesto coincidan (solo se prueba una muestra);
- que los resultados regenerados coincidan con una versión inmutable anterior.

## El hallazgo distributivo que sí se conserva

La formulación defendible es:

> En el banco reconstruido de asignaciones, los intervalos bootstrap por escenarios de los cinco sistemas probados quedaron por debajo de todos los porcentajes puntuales humanos publicados incluidos en la comparación para repartos exactamente iguales, tanto en la tarea laboral como en la familiar. La comparación no incorpora todavía la incertidumbre humana, utiliza referencias de muestras distintas y no demuestra por sí sola falta de representación de personas o poblaciones.

También se mantiene como resultado interno del banco:

- en trabajo, los atributos de mérito reciben mayor peso;
- en familia, la dificultad económica recibe mayor peso.

Estas son descripciones de las configuraciones, prompts y escenarios probados, no una conclusión general sobre la justicia de los modelos.

## Qué puede alimentar la nueva web

### Núcleo activo

- datos DSE crudos;
- identificadores exactos de las cinco configuraciones DSE;
- contraste de tareas trabajo/familia;
- efectos estimados de atributos, con número de escenarios y límites claros;
- comparación descriptiva con valores humanos publicados, sin llamarla aún cobertura de representación;
- registro de procedencia y discrepancias;
- historial de afirmaciones retiradas;
- pipeline, hashes y pruebas mejoradas.

### Archivo del Pilot 01

- perfiles MFQ frente a medias nacionales;
- países “más cercanos”;
- comparación lingüística actual;
- declarado frente a elegido;
- ordenaciones entre modelos;
- alertas de deriva no preespecificadas.

## Orden de corrección recomendado

1. Cambiar la definición y los nombres de “human range” para que describan valores agregados publicados, no representación.
2. Sustituir `intervals_overlap` por una etiqueta que no implique incertidumbre humana.
3. Retirar o recalcular la comparación inglés–mandarín con variante y modo emparejados.
4. Separar GPT y DeepSeek por modo/configuración.
5. Corregir los conteos Ola 2 de 36 a 16/4/20.
6. Añadir `scipy` y mejorar las pruebas de reproducción.
7. Añadir escenarios y más réplicas a los coeficientes DSE.
8. Corregir temperatura, umbral, licencia y documentación de la desviación CHF.
9. Mover MFQ al archivo hasta completar procedencia y código de recolección.
10. Solo después reconstruir la web principal.

## Conclusión

El reanálisis corrigió el error estadístico más grave de la versión anterior y no destruye los datos. El resultado DSE central es robusto a formas alternativas razonables de tratar las repeticiones. Pero el repositorio todavía confunde en varios lugares una **posición frente a cifras agregadas publicadas** con una **medida de representación humana**. Esa distinción debe corregirse antes de que la nueva web se construya alrededor del objetivo de gobernanza.
