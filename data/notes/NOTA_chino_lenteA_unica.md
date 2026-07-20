# NOTA DE METODOLOGÍA — Por qué el piloto en chino usa solo lente_A
### Sección 06 del observatorio (¿sobrevive la silueta occidental en chino?)
### Fechada 2026-07-01, ANTES de completar la recogida en chino

## LA DECISIÓN
El contraste de idioma (inglés vs. chino) se administra únicamente en la variante **lente_A**
(primera persona, escala 1-5, ítems oficiales del MFQ-2), no en las cuatro variantes que se
usan en la medición en inglés.

## POR QUÉ — Y POR QUÉ ES UNA FORTALEZA, NO UN ATAJO

**1. Es la única variante con traducción oficial validada.**
La traducción al chino proviene del repositorio oficial de Atari et al. (MFQ-2), y corresponde
específicamente al formato de lente_A: primera persona, escala 1-5, con las anclas verbales
oficiales ("对我的描述...贴切"). Las otras tres variantes (canónica en 3ª persona 1-7, lente_B
en 1ª persona 1-7, lente_C en 3ª persona 1-5) NO existen como traducción oficial en chino.

**2. Traducir las otras tres nosotros introduciría un riesgo mayor del que resolverían.**
Reformular los 36 ítems a tercera persona en chino, o cambiar las anclas de escala, son
operaciones lingüísticamente delicadas. Hechas por no-nativos (traducción asistida, sin
back-translation ni revisor nativo), amenazarían la invarianza de medida — exactamente el
problema que el diseño busca evitar. Una variante oficial impecable es más rigurosa que cuatro
variantes con tres traducciones caseras.

**3. lente_A es, por diseño, la variante de anclaje humano.**
Para la pregunta central del piloto ("¿el modelo administrado en chino se mueve hacia el polo
humano chino?"), lente_A es la variante metodológicamente indicada: es la que iguala el formato
de las normas humanas (1ª persona, 1-5, ítems oficiales). Las otras tres son controles de
robustez al formato, no las de anclaje. Usar lente_A no es conveniencia: es la elección correcta
para comparar contra el polo humano.

## LÍMITE DECLARADO (honesto)
Al usar una sola variante en chino, este piloto NO puede descartar que un resultado en chino sea
un artefacto de esa variante concreta (defensa que en inglés sí dan las 4 variantes). Por eso:
- Es un PILOTO de la Ola 4, no la Ola 4 completa.
- La robustez multi-variante en chino queda como trabajo futuro, y exige traducir las otras tres
  variantes CON revisor nativo y back-translation (protocolo de invarianza de medida).

## ADEMÁS: los system prompts en chino son traducción nuestra
Los ítems son oficiales (Atari), pero la CONSIGNA en chino (system prompt: instrucciones, escala,
formato) es traducción propia asistida, no validada por nativo. El token de formato "SCORE:" se
mantiene en inglés deliberadamente, para reutilizar el mismo parser en ambos idiomas y evitar que
diferencias de parseo se confundan con diferencias de contenido.

## DESVIACIÓN HEREDADA DEL INSTRUMENTO OFICIAL
El ítem LOYA_34 en la traducción oficial de Atari dice "家庭" (familia) en vez de "equipo
deportivo" del original inglés ("the strength of a sports team comes from the loyalty..."). Es
una adaptación cultural del propio repositorio de Atari, no una modificación nuestra. Se usa tal
cual y se documenta aquí para trazabilidad.
