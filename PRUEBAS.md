# Evidencia y estado de P0 · 4.0.0-rc.1

Fecha 8 de noviembre de 2026. Windows y Python 3.12.14. Los ensayos de estructura se ejecutaron con material inventado en copias separadas. Los casos con nombre, permiso o URL ficticios carecen de efecto sobre archivos, cuentas y decisiones reales.

| Bloque | Resultado |
|---|---|
| P0.1 | Verificado. 64 archivos originales coinciden con la copia sellada. El manifiesto v3.5 enumera 63 y el sello añade el propio manifiesto. La matriz contiene 64 filas, con origen, acción, destino, copia y hash |
| P0.2 | Verificado con fixtures. Una semana con MiMiniApp y tutorial Git, alta y reprogramación, tres Markdown por vídeo y controles OK-1/2/3. Picture lock, marca, salida pública y autorización de retirada tienen evidencias separadas |
| P0.3 | Verificado con fixtures. Ocho pruebas automatizadas, incluidas altas, reintentos, controles de release/operación y condiciones adversas. Además, el inspector ejecutó ffprobe real sobre MP4 generados |
| P0.4 | Preparación e inspección sintética completadas. Prueba audiovisual real pendiente. CapCut 9.7.1.4203 y sus binarios de medios se localizaron. No se abrió el editor. HyperFrames y Shotcut no se localizaron en las rutas revisadas |
| P0.5 | Lógica verificada con dos rutas independientes ficticias en un mismo volumen de pruebas. Pendientes independencia física, traslado de medios autorizados y reapertura de un proyecto de editor desde otro soporte. No se retiró ningún original real |

## Casos de la auditoría

| Caso | Evidencia ejecutada | Alcance pendiente |
|---|---|---|
| T01 · A01/A02 | Alta semana vacía, reintento protegido, alta posterior de vídeo y rechazo de 2027-W53 | — |
| T02 · A02 | Plantilla ausente rechazada antes de crear expediente. Restaurar plantilla ficticia permite reintento sin restos. Marcadores de ID sustituidos | — |
| A03 | Dos proyectos con el mismo canal. Se bloquea doble asignación y reprogramar conserva el ID y GUION | — |
| A04 | Guion aprobado y huella reproducida en otro proceso. Claim X y nueva versión invalidan aprobación anterior | Handoff a editor con material real |
| A05 | Dossier manual con escena con voz guía y escena silenciosa. Enlace inexistente falla | Render, seek, escucha e importación de HyperFrames |
| A06 | Protocolo, dossier y SRT listos. MP4 compatible y control de metadatos verificados con material sintético | Samsung/DJI, editor gratuito, sincronía, reapertura, marca de agua y visionado móvil |
| A07 | Cambio de timing rompe picture lock. Bytes sustituidos rompen OK-3. Tras nueva revisión, salida histórica y bytes previos se conservan | — |
| A08 | Destinos ficticios independientes, uno fallido. Bloqueo sin permiso separado y ante un acto duplicado | Registro de un post real pertenece al alcance posterior autorizado |
| A09 | Dos redes, ventanas +48 h y +7 d, cero frente a dato ausente y unidades registradas | Datos de plataforma pertenecen al alcance posterior |
| T03/T04 · A10 | Rechazo de origen como destino, duplicación de etiqueta sobre ruta, fuente cambiada, hash alterado, copia caducada, recurso fuera de alcance y retirada antes de tiempo | Comprobar soportes físicos independientes |
| T05 · A11 | Retirada solo de bytes sintéticos. Validación con copia desconectada, enlace a medio archivado y consulta de proyecto, guion, publicación y métricas | — |
| T05 · A12 | Recuperación parcial a ruta nueva, hash comprobado y tres documentos intactos. La versión archivada anterior sigue recuperable tras inventariar otra | Reapertura de editor nativo y relink real |
| A13 | Proceso nuevo identifica huella y el validador rechaza que se use sobre versión posterior | Probar cambio de conversación o proveedor con expediente autorizado |
| T06 · A14 | Manifiesto vacío rechazado, release no confunde una alta legítima con paquete original, documento faltante detectado. Estado vivo y archivo offline validados por separado | — |
| T07 · A14 | Se preserva el generador histórico fuera del flujo P0. La operación rechaza token inválido, decisión incompleta, TEMP para salida pública y QC cambiado tras OK-3 | Generar estilo desde marca autorizada pertenece a P1 |
| T08 · A15 | Ruta de dependencia no disponible y controles reales de pista ausente, silencio permitido y color no SDR | Restricción Pro, importación SRT y comprobación perceptual de voz/SDR |

## Inspección sintética reproducida

FFmpeg y ffprobe existentes, versión 1.0.0-401a53202a de la instalación de CapCut. Clips de un segundo, generados con fuentes lavfi de color o tono. Se usó H.264 Media Foundation porque la compilación local no incluye libx264. El tono acredita una pista compatible, no voz ni sincronía humana.

| Entrada | Resultado del inspector |
|---|---|
| H.264, 1080×1920, 30 CFR, 30 cuadros, BT.709, AAC-LC 48 kHz mono | 0 · CONFORME metadatos. QC humano SIN_MEDIR |
| MPEG-4, 320×240, 25 fps, sin audio con pista requerida | 2 · FALLA orientación, códec, FPS, cadencia y audio. Color SIN_MEDIR |
| H.264 SDR sin pista y modo silencio | 0 · CONFORME |
| Mismo H.264 silencioso con pista requerida | 2 · FALLA audio |
| H.264 con etiquetas BT.2020/PQ contra el perfil SDR | 2 · FALLA color. Solo prueba etiquetas, no conversión HDR |
| ffprobe no disponible en PATH | 3 · SIN_MEDIR, pide ruta explícita |

## Repetir

- En una extracción limpia, `python -B scripts/validar_paquete.py release` y `python -B scripts/validar_paquete.py operacion`.
- `python -B pruebas/test_p0.py` clona la candidata en una carpeta temporal propia y ensaya datos ficticios. En Windows puedes definir MARCO_TEST_TMP como ruta de pruebas con permiso de escritura. Ejecuta la suite sobre la candidata sin contenido real.
- Prueba audiovisual autorizada según [PILOTO_AV](PILOTO_AV.md). Para el inspector usa `--ffprobe` con la ruta del binario confirmado si no está en PATH.
- Validación de release comprueba bytes, no juicio editorial ni autenticidad de autorizaciones humanas.

## Estado de preparación

**Candidata verificada para ensayos de estructura.** El piloto audiovisual real y el archivo físico quedan pendientes. Por ello el sistema aún no está validado para piloto completo ni producción recurrente. La candidata se entrega sin semanas o vídeos reales, con marca y cuentas pendientes. P1 y P2 están fuera del alcance ejecutado.
