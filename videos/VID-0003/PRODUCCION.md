# VID-0003 · Producción

Rodaje, ingesta, animación y montaje. Referencias: [TECNICA](../../guias/TECNICA.md) · [SET](../../guias/SET.md).

## Control

- Estado: EN_PRODUCCION
- Bloqueo: NINGUNO
- Siguiente_paso: Ale escucha la edición v06 (media/trabajo/edicion_v06.mp4): la base estándar con la música audible y los efectos revisados. Es un ensayo: no se publica ni necesita OK-3
- Perfil_visual: v2
- Perfil_tecnico: 1080x1920 · 30 fps · H.264 · SDR BT.709 · AAC 48 kHz
- Editor: PENDIENTE

## Rodaje

| toma | escena | qué grabar | cámara o pantalla | hecha |
|---|---|---|---|---|

- Fecha:
- Set (luz, posición, reflector):
- Cámara (móvil, resolución, fps, HDR, blancos):
- Audio (DJI, modo, prueba escuchada):
- Observaciones:

## Ingesta

| archivo | escena | resolución · fps · color | audio | notas |
|---|---|---|---|---|

Originales intactos en `media/originales/`. Comprobación: `python scripts/marco.py inspeccionar <archivo> --perfil ingesta`.

## Animación

- Herramienta y versión:
- Escenas animadas y entrega (MP4 por escena, WAV, SRT):
- Prueba de seek (inicio, medio, final):

## Montaje

- Proyecto_editor:
- Corte_actual:
- Cambios frente al guion:
- Color aplicado:
- Mezcla (voz, música, efectos):
- Subtítulos:

## Correcciones

| ronda | tiempo | defecto | cambio | verificado |
|---|---|---|---|---|

## Tiempo

| fecha | tarea | minutos |
|---|---|---|

## Historial

- 2026-11-20 · Edición v06 (correcciones de sonido de la sesión del 2026-11-19 pasadas a la base, a petición de Ale): `media/trabajo/edicion_v06.mp4` y `edicion_v06_sin_musica.mp4`, misma imagen que la v05. Música 6 dB bajo la voz con bajada de ≈ 3 dB (antes 13 + 5: no se oía), el estribillo sigue bajo toda la demo (antes el valle: «bajada de volumen» al abrir la app) y +2 dB en los picos sin voz; efectos: fuera el boom del pico 1, el clic de cámara de «Plan B», el riser + sello del plan (ahora `magic-spell`) y el whoosh «misterioso»; tecleos por su inicio, durante todo el tecleo y a −15 dBFS; impacto de «¿Y tú?» a −12. Medido: −14,2 / −14,3 LUFS, pico −4,2 dBFS; pico 2 a −11,0 LUFS momentáneos (antes −17,8). **Mezcla medida, no escuchada por Claude.**
- 2026-11-20 · Edición v05 (la base estándar `hyperframes/edicion/`, la de la v04, rehecha en la segunda computadora con `/edicion`): `media/trabajo/edicion_v05.mp4` y `edicion_v05_sin_musica.mp4` (29,72 s, 1080×1920, 30 fps; −14,3 LUFS los dos, pico −4,4 dBFS estéreo / −1,4 dBFS antes del AAC; 32 efectos). Se regeneraron aquí la transcripción (Parakeet sobre la voz alineada +25 ms: mismas palabras que la v04, tiempos ±0,08 s, y ahora «enero.» y «¿Y» bien marcados), el corte sin filtro, la voz, la música, los recursos y la demo real (390 fotogramas). Revisado: `lint` 0 errores, capturas en 18 momentos, hoja a 2 fps y sonoridad en los picos. **Mezcla medida, no escuchada por Claude.**
- 2026-11-20 · Edición v04 (autocrítica aplicada, a petición de Ale): `media/trabajo/edicion_v04.mp4` y `edicion_v04_sin_musica.mp4`. Arranque con acercamiento (1,12 → 1,0 en 0,45 s); subtítulos siempre en caja dentro de la zona segura (1190 a cámara, 1420 con tarjeta, 1440 en la demo); promesa y acento por debajo de la barra superior de las apps; cierre «Este año, sí.»; la demo con 4 toques con sonido en vez de 10

- 2026-11-20 · Edición v03: `media/trabajo/edicion_v03.mp4` y `edicion_v03_sin_musica.mp4`. Sin filtro, a petición de Ale: la toma y los recursos con su color original (solo recorte y escala) y sin viñeta. Medido: pared (107,102,130) frente a (106,101,128) en el original

- 2026-11-20 · Edición v02 (correcciones de Ale): `media/trabajo/edicion_v02.mp4` y `edicion_v02_sin_musica.mp4`. «Plan B» nace del gesto de las manos (se revela desde el centro siguiendo la apertura de las manos, medida fotograma a fotograma) y ya no se solapa con MINIAPP 01; color «natural» en vez del look B (Ale lo vio demasiado notorio en este set); la música sube 4 dB cuando aparece el plan

- 2026-11-20 · Edición v01: `media/trabajo/edicion_v01.mp4` (con música) y `edicion_v01_sin_musica.mp4` (29,72 s, 1080×1920, −14,3 LUFS, pico −1,4 dBFS). Toma 4K recortada a 1,6× con look B, voz mejorada de Ale alineada (+25 ms) y el audio de la cámara en silencio, 8 cortes en silencios medidos, R01/R02/R04, demo de la app real grabada al ritmo de la voz, tres picos con la música y 38 efectos. Composición en `hyperframes/edicion/`. Mezcla medida, no escuchada por Claude

- 2026-11-19 · OK-2 · v01 · 1a610d493b2d · Ale en chat, 2026-11-19: «OK-2 para VID-0003»
- 2026-11-20 · Estado → BORRADOR
- 2026-11-20 · OK-2 · v02 · 67f48ea49520 · Ale en chat, 2026-11-20: «OK-2 para VID-0003»
- 2026-11-20 · Estado → EN_PRODUCCION
- 2026-11-20 · Estado → EN_PRODUCCION
- 2026-11-20 · Estado → EN_PRODUCCION
