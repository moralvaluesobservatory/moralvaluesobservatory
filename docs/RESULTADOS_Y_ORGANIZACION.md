# RESULTADOS Y ORGANIZACIÓN DE LA WEB — documento de referencia
### Moral Values Observatory · versión de trabajo, julio 2026

> Este documento reúne, en un solo lugar: (1) los textos finales de los tres hallazgos tal
> como quedaron en el mockup, (2) los criterios de diseño y comunicación que gobiernan toda
> la página, (3) la estructura completa de secciones acordada, y (4) lo que sigue pendiente.
> Sirve como fuente única de verdad para retomar el proyecto sin releer todo el hilo.

═══════════════════════════════════════════════════════════════════
## 1. IDENTIDAD Y MISIÓN
═══════════════════════════════════════════════════════════════════

**Nombre:** Moral Values Observatory

**Bajada (fijada, en inglés — la web final será en inglés):**
> What values do frontier AI models express — and can we trust what they say?

**Misión (español, para revisar; se traduce al final):**
> Un registro público, continuo y reproducible de qué valores morales expresan los modelos
> de frontera, comparados con poblaciones humanas.

**Metadatos vivos (cabecera):**
> actualizado julio 2026 · 5 familias de modelos · 10 sistemas · 2 países de origen · piloto de idioma replicado en 5 familias

═══════════════════════════════════════════════════════════════════
## 2. LOS TRES HALLAZGOS — texto final vigente
═══════════════════════════════════════════════════════════════════
Los tres viven en la sección "Si tienes dos minutos": dos tarjetas lado a lado + un banner
ancho debajo. Cada uno declara su instrumento con cita exacta y su nivel de solidez.

### Tarjeta 1 — El perfil WEIRD
`etiqueta: replicado · 5 de 5 familias`

**Titular:**
> Modelos de origen chino y de origen estadounidense: ¿a qué perfil moral humano se parecen?

**Cuerpo:**
> Les damos la misma encuesta moral que se usa para estudiar poblaciones de distintas
> culturas, y comparamos sus respuestas con las de personas de 19 países. Da igual el origen
> del modelo: los de origen chino y los de origen estadounidense se parecen al mismo tipo de
> población, la que los investigadores llaman WEIRD (por sus siglas en inglés: occidental,
> educada, industrializada, rica y democrática). Ni siquiera es la población general de
> Estados Unidos o de China (ninguna de las dos forma parte de este marco de comparación):
> es el perfil de un grupo pequeño y particular de sociedades, no el de la mayoría de las
> culturas del mundo.

**Por qué importa:**
> Los modelos de origen chino se parecen a ese perfil humano tanto como los de origen
> estadounidense. El origen del modelo no predice, por ahora, a qué población humana se parece.

**Gráfico:** perfil de líneas (6 fundamentos morales), una línea de color por familia +
línea punteada gruesa para el perfil WEIRD de referencia. Desplegable `+ ver detalle
estadístico` con forest plot (IC 95% bootstrap, 2000 remuestreos, por familia).

**Instrumento:** MFQ-2 (Atari et al., 2023), 36 ítems, comparado con el marco de 19 países.

**Verificación clave:** ni EE. UU. ni China están en ese marco de 19 países (Argentina,
Bélgica, Chile, Colombia, Egipto, Francia, Irlanda, Japón, Kenia, México, Marruecos, Nueva
Zelanda, Nigeria, Perú, Rusia, Arabia Saudita, Sudáfrica, Suiza, EAU). El vector WEIRD se
construyó con Suiza, Irlanda, Nueva Zelanda y Bélgica.

---

### Tarjeta 2 — Origen e idioma  (REFRAME jul 2026, ratificado)
`etiqueta: replicado · 5 familias · 2 idiomas`
> NOTA: el texto que sigue documenta la VERSIÓN ORIGINAL (comparación contra polos rUS−rCN).
> Fue sustituida por el reframe (modelos entre sí + eje discriminante US−China) y por la réplica
> a 5 familias en mandarín (GPT-zh y Fable-zh integrados 2026-07-19). El enfoque vigente, sus
> números y el fallo pre-registrado E3 están en las notas de la sección 5 y en la propia web.
> Se conserva lo de abajo solo por trazabilidad histórica.

**Titular:**
> Si le preguntas a un modelo chino en chino, ¿deja de parecerse a una sociedad occidental?

**Cuerpo:**
> Comparamos a cada modelo con el perfil moral de una muestra representativa de personas de
> Estados Unidos (una población occidental, educada, industrializada, rica y democrática, lo
> que se conoce como WEIRD) y de una muestra representativa de China, preguntándoles en
> inglés y en mandarín. Los tres modelos, incluidos los de origen chino, se parecen más a la
> población estadounidense que a la china, en los dos idiomas. Cambiar el idioma de la
> pregunta no invierte el resultado.

**Por qué importa:**
> El parecido con ese perfil occidental no es un artefacto de preguntar en inglés. Persiste
> incluso cuando el modelo responde en su propio idioma.

**Gráfico:** scatter con diagonal (eje X = parecido a EE. UU., eje Y = parecido a China),
zona sombreada bajo la diagonal, cada modelo con dos puntos (hueco = inglés, relleno =
mandarín) unidos por una línea de su color. Desplegable con forest plot de las diferencias
rUS−rCN por caso.

**Instrumento:** MFQ-2 (Atari et al., 2023), administrado en inglés y mandarín contra los
polos humanos de EE. UU. y China (Study 1c de Atari).

**Verificación clave:** las muestras son nacionalmente estratificadas (cuotas de edad,
género, raza, orientación política; ~515–517 personas por país vía Qualtrics Panels) —
nunca una persona individual. Este hallazgo usa un marco de comparación distinto al de la
Tarjeta 1 (polos US/China de Study 1c, no el marco de 19 países).

---

### Banner — La desconexión declarado/elegido
`etiqueta: replicado · 10 sistemas · eje igualdad–proporcionalidad`

**Titular:**
> Lo que un modelo dice sobre repartir con justicia no predice cómo reparte.

**Cuerpo:**
> No les hicimos una sola pregunta: les dimos 36 juicios distintos sobre cómo repartir
> dinero, bienes, prestigio y trato, para construir un puntaje de cuánto valoran la igualdad
> frente al mérito. Luego les dimos siete escenarios reales de reparto (un bono de empresa,
> una nota de proyecto, una beca, un turno escolar, una sede deportiva, entre otros) y los
> obligamos a elegir entre repartir por igual o por aporte. Lo que declaran en los 36 juicios
> varía muchísimo de un modelo a otro. Lo que eligen en los siete escenarios, casi no varía.

**Por qué importa:**
> No puedes saber cómo actuará un modelo preguntándole por sus principios de reparto.
> Comprobarlo exige observar lo que elige, no lo que declara.

**Nota de estadística agregada (visible sin abrir el desplegable):**
> Varianza entre dilemas 7.2× la varianza entre sistemas · r(declarado, elegido) = −0.28.

**Gráfico:** dos filas de puntos (declarado arriba, disperso; elegido abajo, apiñado),
color por modelo. Desplegable con el mini-comparador de las dos varianzas (0.265 vs 0.037).

**Instrumento:** Comprehensive Distributive Justice Scale, 36 ítems en 4 dominios (Meindl,
Iyer & Graham, 2019), y 7 dilemas narrativos del mismo estudio, adaptados a elección binaria
igualdad-vs-mérito.

**Verificación clave (contra el paper original de Meindl et al. 2019):**
- El factor "declarado" real de Meindl es *Equality/need* (20 ítems: igualdad, necesidad,
  utilitarismo, libertarismo invertido) vs *Equity/merit* (16 ítems: contribución, esfuerzo,
  habilidad, calidad del trabajo), cruzado con 4 recursos (trato, bienes/servicios,
  riqueza/ingreso, estatus).
- Los 7 dilemas narrativos son reales y distintos entre sí (empresa Altaia, escuela de
  negocios USC, fundación John Henry Dean, escuela primaria Bright Country Day, presidencia
  de la OMS, teatro comunitario de Des Moines, sede del Consejo Internacional de Atletismo).
  Cada uno tiene versión de escala (equity/equality/need) y una versión binaria forzada
  igualdad-vs-mérito — **la opción de necesidad no entra en la versión binaria**, aunque sí
  existe en el diseño original de Meindl.
- Alcance honesto: la desconexión está demostrada en el eje igualdad–proporcionalidad
  específicamente, no en "todos los valores" de un modelo.

═══════════════════════════════════════════════════════════════════
## 3. CRITERIOS DE DISEÑO Y COMUNICACIÓN (los 9 que gobiernan la página)
═══════════════════════════════════════════════════════════════════
1. **Orden Epoch:** qué somos → qué sabemos → por qué creernos. La misión (permanente) va
   antes que los hallazgos (cambiantes).
2. **Significado grande, dato técnico de apoyo.** Nunca un número sin su traducción pegada.
3. **Cero jerga en la puerta de entrada.** "WEIRD" nunca en un titular; se explica la
   primera vez que aparece, con sus 5 palabras completas, entre paréntesis.
4. **La incertidumbre es diseño, no disculpa.** Etiquetas de alcance con el mismo peso
   visual que el titular ("replicado · 5 de 5 familias", "piloto · 3 modelos").
5. **Estratificación para tres audiencias:** titular llano → "por qué importa" → gráfico →
   desplegable `+ ver detalle estadístico` para el revisor técnico.
6. **Mostrar, no afirmar.** Ejemplos reales de ítems y respuestas en vez de solo describir
   el instrumento.
7. **El color codifica, nunca decora.** Paleta fija por familia de modelo (Opus, GPT,
   DeepSeek, GLM, Fable), consistente en las tres piezas. Tonos vivos, no apagados.
8. **Herramienta viva, no informe congelado.** Fecha de actualización visible, sección de
   próximos pasos, ranura de credibilidad.
9. **Contención.** Austeridad tipo Epoch (fondo claro, tinta oscura, color solo en datos) +
   el "por qué importa" narrativo que Epoch no necesita pero este observatorio sí.

### Reglas de estilo acordadas
- Sin guiones largos (em dash) en ningún texto — se usan paréntesis o punto y seguido.
- WEIRD siempre con sus siglas explicadas la primera vez; nunca como sinónimo de "Estados
  Unidos" (son cosas relacionadas pero distintas — ni EE. UU. ni China están en el marco de
  19 países que define el vector WEIRD de la Tarjeta 1).
- Los gráficos con intervalos de confianza van ocultos por defecto detrás de
  `+ ver detalle estadístico` (elemento `<details>` nativo, sin JavaScript), para no
  saturar la lectura rápida.
- Cada tarjeta cita su instrumento exacto en una línea mono al final, antes del desplegable.

### Paleta de color por modelo (fija en toda la web)
| Modelo | Color |
|---|---|
| Opus | azul índigo `#3D5CE0` |
| GPT | verde salvia `#3E9450` |
| DeepSeek | naranja quemado `#D9611E` |
| GLM | teal vivo `#0FA98C` |
| Fable | púrpura `#9B3FC4` |

Tipografía: Fraunces (serif, titulares) + IBM Plex Sans (cuerpo) + IBM Plex Mono (datos,
etiquetas, citas de instrumento).

═══════════════════════════════════════════════════════════════════
## 4. ESTRUCTURA COMPLETA DE LA WEB (acordada, construida hasta la sección C)
═══════════════════════════════════════════════════════════════════

**A · Cabecera fija** — nombre, navegación (Hallazgos · Próximamente · Confianza · Método),
fecha de actualización. ✅ construida.

**B · Misión** — frase de misión + metadatos vivos. ✅ construida.

**C · Resultados en 60 segundos** — Tarjeta 1 + Tarjeta 2 + banner ancho. ✅ construida,
con intervalos de confianza en desplegables.

**D · Divisor duro** — línea que marca "aquí termina el resumen, empieza la evidencia
completa". ⏳ pendiente de construir.

**E · Sección-puente** — "qué le preguntamos y cómo lo medimos": ejemplos reales de ítems
(uno del MFQ-2/Atari, uno de la CDJS/dilema de Meindl), la explicación de "forma vs.
números absolutos" (por qué se compara la forma del perfil, no los valores crudos), y el
anticipo del bloque de confianza. ⏳ pendiente de construir (ya redactada en el chat,
falta maquetar).

**F · Hallazgos profundos, por temas** — no lista plana, tres temas:
- Tema I — ¿De quién son los valores? (perfil WEIRD completo, piloto de idioma completo)
- Tema II — ¿Hacen lo que dicen? (desconexión completa, con el detalle de Meindl)
- Tema III — ¿Es fiable medir esto? (deriva entre versiones E1, distanciamiento "como IA"
  H5, amplificación E2 — los exploratorios, marcados como tales)
⏳ pendiente de construir.

**G · Próximamente** — roadmap: brazo de paráfrasis anti-contaminación, extender la
desconexión a los ejes necesidad y bienestar, Ola 4 multilingüe con más anclas, auditoría
de divergencia de persona. ⏳ pendiente.

**H · ¿Puedes confiar en esto?** — auto-crítica: los títulares descartados, los límites
declarados, la reproducibilidad desde crudos (scripts + CSV del paquete). ⏳ pendiente.

**I · Método** — instrumentos completos, diseño de variantes, olas, citas académicas
completas. ⏳ pendiente.

**J · Pie** — contacto para revisión/financiación, fecha, nombre de trabajo. ⏳ pendiente.

═══════════════════════════════════════════════════════════════════
## 5. PENDIENTES Y DECISIONES ABIERTAS
═══════════════════════════════════════════════════════════════════
- Traducir el mockup completo al inglés (se revisó y corrigió en español a propósito).
- Maquetar D, E, F, G, H, I, J — solo A, B, C están construidas en el HTML.
- Definir si los hallazgos exploratorios (E1 deriva, E2 amplificación, H5 distanciamiento)
  se presentan con el mismo desplegable `+ ver detalle estadístico` o con una etiqueta
  distinta que refuerce que son preliminares (recomendado: sí, para mantener consistencia).
- FABLE-ZH INTEGRADO Y PRE-REGISTRO CERRADO (2026-07-19): 360/360 ok. E1 (+0.960, la más
  alta) y E2 (+0.944) cumplidas → hallazgo de idioma ASCIENDE a replicado · 5 familias ·
  2 idiomas (tag actualizado en Tarjeta 2 y sección profunda). E3 FALLIDA: Fable–DeepSeek en
  mandarín = 0.914 < 0.95; publicada en "¿Puedes confiar en esto?" como tercer ítem del
  registro, y el dato del par cruzando el Pacífico queda acotado como hecho del inglés en la
  tarjeta. E4: 0.0%. Forest a 10 filas; scatter a 5 modelos (Fable cae en diagonal); método a
  15 datasets. La etiqueta de la Tarjeta 2 del punto 2 de este documento ("piloto · 3 modelos ·
  inglés y mandarín") queda OBSOLETA; el texto de la tarjeta en este doc necesita reescritura
  para reflejar el reframe si se ratifica.
- GPT-ZH INTEGRADO (2026-07-19): 360/360 ok. Pre-registro E1, E2 y E4 CUMPLIDAS (proyección
  +0.937 [.921,.951]; sin Care +0.977; no_aplica_ia 0.6%). Forest de la Tarjeta 2 pasa a 9 filas;
  scatter profundo pasa a 4 modelos (GPT cae en diagonal, como Opus); método actualizado a
  14 datasets y "mandarin: 4 of 5". E3 espera a Fable-zh. Crudo: gpt_zh_crudo.csv (lente_A,
  snapshot gpt-5.5-2026-04-23).
- REFRAME TARJETA 2 (jul 2026, aplicado al mockup, pendiente de ratificar): la tarjeta ya no
  compara contra cada polo completo (rUS-rCN), sino (1) modelos entre si sin polos humanos
  (acuerdo 0.94-0.99; el par mas parecido es Fable-DeepSeek, 0.99, cruzando origenes) y
  (2) proyeccion sobre el vector diferencia US-China (el eje que discrimina). Motivo: los polos
  correlacionan 0.76 entre si; el framing anterior perdia la mitad del efecto sin Care. El nuevo
  eje sobrevive leave-care-out (medianas 0.83-0.98, ningun IC toca 0; bootstrap 2000, semilla 42,
  remuestreo de repeticiones dentro de item). Se añadio ademas un hallazgo descriptivo en Tema I:
  los modelos no se situan entre las dos poblaciones, las SOBREPASAN (care por encima del polo US,
  purity por debajo, loyalty por debajo de ambas). Limites declarados en el desplegable: eje de
  n=6 fundamentos, vector construido desde los polos publicados, version por item imposible con
  datos humanos agregados. Los dos SVG nuevos se generan por script desde crudos, no a mano.
- Decidir el contenido exacto de la sección de roadmap (G) en detalle de hitos.
- RESUELTO (jul 2026): la discrepancia del valor de DeepSeek en inglés (0.364 vs 0.386) queda
  reconciliada. Origen: 0.364 provino de una corrida en modo *thinking* (rUS=0.855) registrada en
  `notas/RESULTADO_piloto_chino_seccion06.md`; 0.386 sale del modo *non_thinking* de
  `deepseek_crudo.csv`, que es el que alimenta el pipeline oficial (`03_piloto_idioma.csv`) y el
  bootstrap (mediana 0.385, IC 0.326-0.437). VALOR OFICIAL = 0.386. La web ya lo grafica correcto
  (coordenada = 0.385). No cambia ninguna conclusión: en ambos modos DeepSeek se inclina a EE. UU.
  y esa inclinacion baja en mandarin.

═══════════════════════════════════════════════════════════════════
## 5c. DIRECCIÓN DE INVESTIGACIÓN AÑADIDA A "WHAT'S NEXT" (2026-07-19)
Casilla principal nueva: "Do models match the values their own labs wrote down?" — el delta
especificación → comportamiento. Justificación tras revisar el estado del campo (jul 2026):
- La desconexión declarado/elegido es ahora frontera activa del campo (Gu et al. 2025; Shen et al.
  2025 "value-action gap"; Slama, Souly, Bansal, Davidson, Summerfield, Luettgau 2026 "When do LLM
  preferences predict downstream behavior?" — este último con gente del AISI). Confirma que
  elegimos el problema correcto, pero la ventana se estrecha.
- Auditar CUMPLIMIENTO de constitución YA está ocupado (pipeline que descompone la constitución de
  Anthropic en 205 tenets y el Model Spec de OpenAI en 197; survey de 6 iniciativas). NO ir ahí.
- Religión: DESCARTADO (MFT ya ligada a política/religión; máximo riesgo de mal uso, justo lo que
  pasamos iteraciones desactivando).
- Réplica del hallazgo WEIRD: YA existe (arxiv 2511.11790 nov-2025; ScienceDirect jun-2026 "moral
  drift", que encuentra OpenAI > Anthropic en las 6 fundaciones, mayor brecha en Sanctity).
HUECO LIBRE Y FACTIBLE = medir PERFIL (no cumplimiento binario) contra la spec, en 3 capas:
  (1) spec → declarado, (2) declarado → elegido [ya lo tenemos], (3) spec → elegido [nadie lo mide].
  Eje extra: labs con spec pública vs sin ella (Gemini no tiene spec comparable, per Anthropic).
  Encaja de seguridad: un modelo que actúa distinto de lo que su lab documentó = brecha de
  gobernanza cuantificable. Ventaja diferencial: nadie junta spec + perfil + comportamiento +
  anclas humanas cross-culturales. Requiere nuestra combinación exacta.

## 5b. PREPARADO PARA COMPARTIR (2026-07-19)
Cambios aplicados a la web para dejarla lista para difusión:
- Masthead y metadatos: "hold" → "express" (alineado con la limitación de que se mide la
  persona del asistente, no una propiedad interna). El H1 se mantuvo como pregunta fijada,
  solo cambió el verbo.
- Limitación obsoleta de DeepSeek reescrita: la discrepancia quedó trazada (modo de razonamiento
  distinto) y reconciliada a 0.386; ya no figura como pendiente sin resolver.
- Añadida caja "Reproduced independently" en la sección de confianza: se corrieron los scripts
  desde los crudos y se recuperaron las cifras publicadas (5 correlaciones WEIRD al 3er decimal,
  r declarado-elegido −0.28, ratio de varianza 7.2, conteos de usables fila a fila). Verificación
  ejecutada, no declarada.
- Footer: estado actualizado a "language finding replicated across 5 families · under
  independent review".
- Organización de secciones y posición del banner: SIN CAMBIOS (decisión del autor).
- Pendientes que quedan fuera de este pase: contacto real del pie (href vacío), y la migración
  del resto de gráficos a generación por script (infra, no bloqueante).

## 6. ARCHIVOS DE ESTE PROYECTO
═══════════════════════════════════════════════════════════════════
- `observatorio_web.html` — mockup funcional, secciones A–C construidas.
- `INVENTARIO_HALLAZGOS.md` — catálogo completo de hallazgos con criterios de solidez.
- `NOTA_EXPLORATORIOS.md` + scripts `exp1/exp2/exp3_*.py` — los tres análisis exploratorios
  post-hoc (deriva longitudinal, amplificación, efecto de persona en Equality).
- Paquete original de auditoría (`AUDITORIA_COMPLETA.md`, `VERIFICACION_ESTADISTICA.md`,
  CSV de bootstrap) — fuente de todos los números citados aquí.
