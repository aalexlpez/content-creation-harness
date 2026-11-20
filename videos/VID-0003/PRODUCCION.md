# VID-0003 · Producción

Rodaje, ingesta, animación y montaje. Referencias: [TECNICA](../../guias/TECNICA.md) · [SET](../../guias/SET.md).

## Control

- Estado: EN_PRODUCCION
- Bloqueo: NINGUNO
- Siguiente_paso: Ale revisa la edición v04 (media/trabajo/edicion_v04.mp4). Es un ensayo: no se publica ni necesita OK-3. Después, estandarizar la edición (EDICION → Hacia un estándar estable)
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

- 2026-11-20 · Edición v04 (autocrítica aplicada, a petición de Ale): `media/trabajo/edicion_v04.mp4` y `edicion_v04_sin_musica.mp4`. Arranque con acercamiento (1,12 → 1,0 en 0,45 s); subtítulos siempre en caja dentro de la zona segura (1190 a cámara, 1420 con tarjeta, 1440 en la demo); promesa y acento por debajo de la barra superior de las apps; cierre «Este año, sí.»; la demo con 4 toques con sonido en vez de 10

- 2026-11-20 · Edición v03: `media/trabajo/edicion_v03.mp4` y `edicion_v03_sin_musica.mp4`. Sin filtro, a petición de Ale: la toma y los recursos con su color original (solo recorte y escala) y sin viñeta. Medido: pared (107,102,130) frente a (106,101,128) en el original

- 2026-11-20 · Edición v02 (correcciones de Ale): `media/trabajo/edicion_v02.mp4` y `edicion_v02_sin_musica.mp4`. «Plan B» nace del gesto de las manos (se revela desde el centro siguiendo la apertura de las manos, medida fotograma a fotograma) y ya no se solapa con MINIAPP 01; color «natural» en vez del look B (Ale lo vio demasiado notorio en este set); la música sube 4 dB cuando aparece el plan

- 2026-11-20 · Edición v01: `media/trabajo/edicion_v01.mp4` (con música) y `edicion_v01_sin_musica.mp4` (29,72 s, 1080×1920, −14,3 LUFS, pico −1,4 dBFS). Toma 4K recortada a 1,6× con look B, voz mejorada de Ale alineada (+25 ms) y el audio de la cámara en silencio, 8 cortes en silencios medidos, R01/R02/R04, demo de la app real grabada al ritmo de la voz, tres picos con la música y 38 efectos. Composición en `hyperframes/edicion/`. Mezcla medida, no escuchada por Claude

- 2026-11-19 · OK-2 · v01 · 1a610d493b2d · Ale en chat, 2026-11-19: «OK-2 para VID-0003»
- 2026-11-20 · Estado → BORRADOR
- 2026-11-20 · OK-2 · v02 · 67f48ea49520 · Ale en chat, 2026-11-20: «OK-2 para VID-0003»
- 2026-11-20 · Estado → EN_PRODUCCION
