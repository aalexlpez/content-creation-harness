# VID-0002 · Producción

Rodaje, ingesta, animación y montaje. Referencias: [TECNICA](../../guias/TECNICA.md) · [SET](../../guias/SET.md).

## Control

- Estado: BORRADOR
- Bloqueo: NINGUNO
- Siguiente_paso: Ensayo cerrado con la edición v01 (2026-11-17). Ale regrabará el vídeo final en otro expediente, con los cambios de C1 y C10 del GUION
- Perfil_visual: v2
- Perfil_tecnico: 1080x1920 · 30 fps · H.264 · SDR BT.709 · AAC 48 kHz
- Editor: PENDIENTE

## Rodaje

| toma | escena | qué grabar | cámara o pantalla | hecha |
|---|---|---|---|---|
| T1-B1 | S01 | Beat 1 · Gancho, seco a cámara, 2–3 tomas | Cámara A (S24+ trasera 1×), plano medio corto | no |
| T1-B2 | S02 | Beat 2 · Problema, más bajo, pausa tras «Calma», 2–3 tomas | Cámara A | no |
| T1-B3 | S03 | Beat 3 · Solución, algo más de energía, 2–3 tomas | Cámara A | no |
| T1-B4 | S04–S05 | Beat 4 · Demo y resultado, una frase por paso (va sobre la maqueta: basta la voz), 2–3 tomas | Cámara A | no |
| T1-B5 | S06 | Beat 5 · Prueba, tono de reto y sonrisa en «compruébalo», 2–3 tomas | Cámara A | no |
| T1-B6 | S07 | Beat 6 · CTA, mismo encuadre que S01, más lento, 2–3 tomas | Cámara A | no |

- Fecha:
- Set (luz, posición, reflector):
- Cámara (móvil, resolución, fps, HDR, blancos):
- Audio (DJI, modo, prueba escuchada):
- Observaciones:

## Ingesta

| archivo | escena | resolución · fps · color | audio | notas |
|---|---|---|---|---|
| originales/ensayo_2.mp4 | S01–S07 | 1080×1920 · 30 fps CFR (1897 cuadros) · H.264 BT.709 progresivo | AAC 44,1 kHz estéreo · −17,3 LUFS, pico −2,6 dBFS | Corte limpio de Ale en CapCut gratis, 63,25 s, sin marca de agua ni subtítulos (revisado en 0,5, 31 y 62,8 s). El audio pasa a WAV 48 kHz en trabajo/. El .AAC suelto, en descartado/ |

Originales intactos en `media/originales/`. Comprobación: `python scripts/marco.py inspeccionar <archivo> --perfil ingesta`.

## Animación

- Herramienta y versión: HyperFrames 0.9.42 por `npx` (un proyecto por pieza en `hyperframes/MG-0N/`, GSAP 3.12.5 y Plus Jakarta Sans locales)
- Escenas animadas y entrega (MP4 por escena, WAV, SRT): MG-01_v02 (hoja de calendario, capa transparente, 1080×1920, 30 fps, 6,4 s): `.mov` ProRes 4444 con alfa (`yuva444p12le`) y `.webm` VP9 con alfa, en `media/trabajo/`, más `MG-01_v02_vista-previa.mp4` sobre fondo neutro. Sin audio. Marcas: giro a FEBRERO en 0,9 s y vuelta a ENERO en 4,4 s (se ajustan a la voz). La v02 sustituye a la v01 (giro 3D sobre la bisagra, oscurecido al girar y asentado, según la receta split-flap de video-shotcraft); la fuente de la v01 queda en `hyperframes/MG-01/versiones/`. MG-02_v01 (rótulo «Plan B · para tu propósito» / «HERRAMIENTA N.º 1», capa transparente, 2,9 s): caja del rótulo inferior ajustado del kit (x 69, y 1230–1400) a 700 px de ancho, barra «/» que entra primero, barrido diagonal de entrada y salida, título por máscara; `.mov` ProRes 4444 y `.webm` con alfa más vista previa. Marca: el rótulo arranca en 0,0 s, en «Plan B», y se queda 2,5 s. MG-06_v01 (maqueta de Plan B, pasos 1 a 3, 15,4 s) y MG-07_v01 (sello, calendario de 4 semanas con 20 apariciones y fondo de bloqueo, 5,8 s): pantalla completa, MP4 H.264 1080×1920 30 fps BT.709, rótulo «MAQUETA DE ENSAYO», textos y movimiento de la ficha v06 de `soycerobytes/miminiapp` (Plan B aún no está construida), más `MG-06-07_v01_vista-previa.mp4`. Sus anclas internas salen del SRT de YouTube (tomas de 6:43 y 7:05 del bruto) y se recalculan con la toma elegida. **v02 (sustituye a la v01, cuya fuente queda en `hyperframes/MG-0N/versiones/`):** interfaz a pantalla completa y legible (×2,6), entrada como tarjeta que se expande, cámara que sigue cada interacción, teclado español con la tecla de cada letra y cursor dentro del texto, «blackout» al elegir obstáculo, sello con golpe de cámara y la frase como elemento compartido que viaja del resultado a la pantalla de bloqueo. Técnicas de los bloques notes-reveal y cursor-zoom-follow de HyperFrames y de recetas de video-shotcraft (Apache-2.0). `MG-06_v02.mp4` (15,4 s), `MG-07_v02.mp4` (5,8 s) y `MG-06-07_v02_vista-previa.mp4`. Falta probar que CapCut importa la transparencia de MG-01 y MG-02
- Prueba de seek (inicio, medio, final): MG-01 v02 en 12 instantes (entrada, giro de ida, FEBRERO, vuelta, ENERO asentado, vacío en 6,35 s) MG-02 v01 en 8 instantes (barra, barrido, título, sostenido, salida, vacío en 2,85 s), MG-06 v01 en 10 (escritura, mes, gris, obstáculos, toque, paso 3) y MG-07 v01 en 11 (sello, calendario, bloqueo, salida), con `snapshot`; alfa verificado con ffprobe y compuesto sobre fondo de prueba
- Sonido de la hoja (candidatos CC0 de Freesound, sin descargar): 749880 «Page turned» (0,68 s), 842183 «Page Turn Free» (0,56 s), 459657 «Calendar flip» (16,8 s, varios giros) y 856497 «Turning page (heavy paper)» (3,2 s). Pendiente de que Ale escuche y elija. Toque (MG-06): 332713 «Tap» (0,1 s), 496456 «Tap_Tablet» (3,9 s), 704862 «Finger Tapping Phone» (12,6 s). Sello (MG-07): 470710 «traditional stamp» (1,6 s), 683031 «Thump» (0,7 s), 514486 «Office stamp» (4,5 s), 461888 «stamp, rubber, plastic» (15,6 s). Todos CC0, sin descargar

## Montaje

- Proyecto_editor: HyperFrames `hyperframes/edicion/` (edición continua, AV-009); plan y pasos en `hyperframes/edicion/PLAN.md`. Carpetas `media/originales`, `trabajo`, `entregas` y `descartado` creadas el 2026-11-17. Los renders MG-0N de MEDIOS.csv no están en este equipo: se rehacen desde sus fuentes
- Corte_actual: `media/trabajo/edicion_v01.mp4` (2026-11-17, 63,25 s, 1080×1920, 30 fps, H.264, AAC 48 kHz; inspector OK). Sin sonido añadido: `edicion_v01_sin_sfx.mp4`. Composición `hyperframes/edicion/index.html` sobre `assets/corte.mp4`, con MG-06 y MG-07 v03 (re-ancladas con mapa de tiempos) a pantalla completa
- Cambios frente al guion: el corte (63,25 s) cambia la voz literal; GUION sube a v02 el 2026-11-17 (C1 pasa a X, nuevos C9 y C10). Decisiones de Ale ese día: demo a pantalla completa, música lofi de Pixabay en todo el vídeo, edición en BORRADOR
- Color aplicado: Toma tal cual de CapCut. Firma del gancho: desaturado y frío en «abandonaste» (1,28 s, 8 fotogramas) y vuelta en «todavía» (3,82 s)
- Mezcla (voz, música, efectos): `hyperframes/edicion/mezcla.py`: voz con compresión suave (-17.4 LUFS de origen), 63 efectos del banco de Pixabay recortados a su tramo audible con el pico 1 fotograma después del evento (detalle en `media/trabajo/edicion_v01_mezcla.json`), música lofi en todo el vídeo 18 dB bajo la voz; total -14.2 LUFS, pico -1.1 dBFS. Medido, no escuchado por Claude
- Subtítulos: Propios, quemados en la composición: Plus Jakarta Sans ExtraBold 58 px, 2–4 palabras, palabra activa invertida; y 862 en el escenario y 1190 a cámara; sobre la maqueta, en cajas marinas

- Edición v03 (2026-11-18): arreglos de `hyperframes/edicion/REVIEW.md` (demo en ventana del escenario con la cara siempre visible, subtítulos en banda fija, sin anillo de toque, recortes de voz a 49,66 s, textos más grandes, 39 efectos) con la voz mejorada de Ale (`media/trabajo/voz_mejorada_v2.mp3`). Entrega `media/trabajo/edicion_v03.mp4`, −14,4 LUFS, pico −3,7 dBFS
- Edición v04 (2026-11-18): correcciones de Ale sobre la v03 (cortes en silencios medidos y finales de frase con `cortes.py`, «La serie» hasta «cualquier ámbito», demo encuadrada por grupos de interfaz con zoom, subtítulos que caben en el ancho). Entrega `media/trabajo/edicion_v04.mp4`, 55,48 s, −14,4 LUFS, pico −4,3 dBFS

## Correcciones

| ronda | tiempo | defecto | cambio | verificado |
|---|---|---|---|---|

## Tiempo

| fecha | tarea | minutos |
|---|---|---|

## Historial

- 2026-11-16 · Estado → BORRADOR
