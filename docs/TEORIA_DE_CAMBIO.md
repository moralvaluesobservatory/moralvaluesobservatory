# TEORÍA DE CAMBIO — Moral Values Observatory
### Documento interno · brújula, no folleto · versión julio 2026

> Propósito de este documento: decidir en qué invertir esfuerzo y, sobre todo, saber
> cuándo NO seguir. Una teoría de cambio interna sin criterios de parada es una carta de
> motivación disfrazada. Aquí cada eslabón lleva su supuesto y su señal de fractura.

---

## 0. LA FRASE HONESTA (si solo lees una línea)
No transformamos la gobernanza de la IA. Producimos evidencia y método lo bastante creíbles
como para que quien SÍ tiene poder (institutos de evaluación, reguladores) pueda hacerlo.
Somos proveedor de infraestructura de confianza, no agente transformador. Nuestra ventaja es
una ventana temporal (rigor + independencia + anclas cross-culturales), no un foso permanente.

---

## 1. EL PROBLEMA QUE DECIMOS RESOLVER
Los laboratorios publican especificaciones de comportamiento (constitución de Anthropic, Model
Spec de OpenAI) que expresan prioridades morales implícitas. Nadie mide si el PERFIL moral que
el modelo realmente exhibe coincide con el que su propia spec prescribe. Las auditorías actuales
comprueban cumplimiento binario de reglas bajo presión; ninguna mide la brecha de perfil.

Supuesto subyacente (el más peligroso de todo el documento): que esa brecha IMPORTA para la
seguridad. Si el perfil moral medido no predice comportamiento consecuente en despliegue real,
toda la cadena de abajo pierde fuerza.
→ SEÑAL DE FRACTURA: si el brazo agéntico del roadmap (probar si declarado/elegido sobrevive a
  tareas reales, no dilemas) muestra que el perfil NO predice conducta, hay que replantear el
  impacto entero, no seguir midiendo perfiles como si importaran por sí solos.

---

## 2. LA CADENA (insumos → impacto), CON SUS FRACTURAS

### Insumos (lo que YA tenemos — control alto)
Instrumento cross-cultural con anclas humanas estratificadas · desconexión declarado/elegido
replicada en 5 familias · reproducibilidad desde crudos verificada · disciplina de pre-registro
(con un fallo ya publicado) · paleta de credibilidad procedimental difícil de falsificar.

### Actividades (lo que haríamos — control alto)
Medir el delta spec→comportamiento en tres capas: (1) spec→declarado, (2) declarado→elegido [ya
lo tenemos], (3) spec→elegido [nadie lo mide]. Perfiles, no cumplimiento binario. Eje extra:
labs con spec pública vs. sin ella.

### Productos (lo tangible — control alto)
Un método auditable + mediciones públicas de la brecha, lab por lab, actualizadas en el tiempo.

  ─────────  AQUÍ TERMINA LO QUE CONTROLAMOS  ─────────

### Resultados intermedios (cambio en OTROS — control bajo)
Que evaluadores independientes, institutos (AISI) y los propios labs usen la medición como una
señal que antes no existía.
→ SUPUESTO: que a alguien le importe la brecha.
→ SEÑAL DE FRACTURA: si los labs responden "la spec es aspiración, no promesa de perfil medible"
  y nadie recoge el dato en 12-18 meses, el producto es una curiosidad, no una palanca.
→ MITIGACIÓN: enmarcarlo como diagnóstico útil PARA ellos (los labs no siempre saben qué valores
  instalaron), no como "os pillamos". El framing acusatorio mata la adopción.

### Impacto (el cambio último — control casi nulo)
Que la brecha spec→comportamiento se vuelva una dimensión estándar de rendición de cuentas: que
publicar una constitución como gesto de gobernanza conlleve que alguien verifique, con número, si
el modelo la encarna.
→ SUPUESTO: adopción por actores con poder (reguladores, institutos). No lo decidimos nosotros.
→ REALISMO: nuestro rol probable es proveer método + credibilidad; la institucionalización la
  hará otro. No es fracaso: es división del trabajo. Si la teoría de cambio dependiera de que
  NOSOTROS institucionalicemos algo, sería falsa.

---

## 3. LOS CUATRO SUPUESTOS QUE PUEDEN HUNDIRLA (ordenados por letalidad)
1. **El perfil no predice conducta.** (Ver §1.) El más letal. Lo prueba el brazo agéntico.
2. **A nadie le importa la brecha.** Salto producto→resultado. Lo prueba la recepción a 12-18 meses.
3. **La ventana se cierra antes de movernos.** Un grupo con más recursos ocupa el espacio; nuestra
   contribución marginal cae a casi cero. Lo prueba el reloj: ya hay gente del AISI (Slama et al.)
   y réplicas del hallazgo WEIRD publicadas en 2025-2026.
4. **El instrumento es demasiado lateral.** Valores/cultura no es el núcleo del AISI (bio, ciber,
   autonomía). Nuestra vía real es beca de investigación o rol de tercero independiente, NO la
   evaluación de capacidades peligrosas de frontera. Fingir lo contrario nos haría perder el tiro.

---

## 4. QUÉ TENDRÍA QUE SER CIERTO PARA SEGUIR (criterios de continuación)
Seguimos invirtiendo SI Y SOLO SI, en orden:
- [ ] El brazo agéntico muestra QUE el perfil declarado/elegido tiene ALGUNA relación con conducta
      en tareas reales (aunque sea parcial). Si es cero, paramos y replanteamos.
- [ ] El delta spec→comportamiento produce al menos UNA diferencia entre labs que no sea trivial
      ni explicable por ruido de medición.
- [ ] Aparece al menos un interlocutor externo (beca, colaboración, cita institucional) en un
      horizonte razonable. Silencio total = revisar el framing o el canal.
- [ ] Nadie con más recursos publicó exactamente esto primero. Si lo hacen, pivotar a lo que
      seguimos teniendo único (anclas cross-culturales + reproducibilidad), no competir de frente.

## 5. SEÑALES DE ALTO (cuándo parar es la decisión correcta)
- El brazo agéntico da nulo robusto → el perfil no importa → parar o reconvertir en trabajo puramente
  descriptivo/académico, sin pretensión de impacto en seguridad.
- 18 meses sin ningún recogedor del dato → el problema no era sentido por nadie salvo nosotros.
- La ventana se cierra (otro ocupa el nicho con más alcance) → aceptar rol de complemento o cerrar.
- Advertencia meta: el mayor riesgo de un proyecto con buena disciplina epistémica es enamorarse
  del método y seguir midiendo con rigor algo que ya no cambia nada. Rigor no es lo mismo que
  relevancia. Este documento existe para no confundirlos.

---

## 6. LO QUE ESTA TEORÍA DE CAMBIO NO PROMETE (para no auto-engañarnos)
- No promete que cambiemos cómo se entrenan los modelos.
- No promete que el AISI nos adopte; a lo sumo, que encajamos en una de sus puertas (beca /
  tercero independiente / accountability), no en su mandato central.
- No promete un foso. Promete usar bien una ventana.
- No promete impacto por mérito del rigor. El rigor es condición necesaria, no suficiente: sin
  un actor que recoja el dato, el rigor es un adorno privado.
