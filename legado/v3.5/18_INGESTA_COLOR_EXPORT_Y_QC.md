# Guía técnica de ingestión, calidad y exportación — Samsung → HyperFrames → editor → redes
**Perfil operativo inicial:** 9:16 / 1080×1920 / 30 fps / SDR BT.709 / MP4 H.264 + AAC 48 kHz. Es una elección **interna para vídeos nuevos** por compatibilidad y recursos del PC, NO una obligación universal; grabaciones existentes pueden tener otra resolución/FPS/HDR. **No convertir ni sobrescribir un original sin comprobar sus metadatos.**

## 1. Ingesta desde Samsung S24+
1. Transferir **archivo original**, directamente por USB o transferencia de archivos sin compresión verificada. **No usar WhatsApp ni otra mensajería**, incluso en apariencia 4K: si comprime, destruye detalle. El usuario ha comprobado diferencia visible entre archivo de WhatsApp y original.
2. Guardar copia inmutable en `media/camera/original/`. No recortar, no modificar ni renombrar destructivamente. Usar un nombre de inventario con fecha/ID; conservar nombre de cámara en `INGESTA.md`.
3. Verificar duración, resolución, FPS real, FPS nominal, códec, bitrate, `color_primaries` y `color_transfer`, rotación, audio, fecha; dejar PENDIENTE cualquier dato no medido. Usar `python scripts/inspeccionar_video.py media/camera/original/xxx.mp4` (requiere ffprobe).
4. Comprobar voz y distorsión, ruido, exposición, foco y una toma completa, no solo fotograma.
5. Antes de borrar del teléfono, mantener otra copia. Comparar hash SHA-256 para transferencias críticas.

## 2. Proxies y formato del proyecto
- PC de oficina 16 GB RAM y GPU integrada: si 4K/HEVC causa problemas, crear **proxy** de previsualización 1080p SDR H.264; anotar relación con original. No reemplazarlo.
- Si CapCut/Shotcut no religa automáticamente proxy-original, la operación de sustituirlos antes del master deberá **probarse manualmente**; nunca presumir que la función existe.
- Para rodaje nuevo, grabar vertical 30 fps en SDR es una opción inicial simple. Si se usa 60 fps o HDR, registrar la decisión de conform/transformación: la guía oficial de YouTube recomienda mantener FPS de captura al publicar; un timeline mixto puede exigir conversiones justificadas.
- Si el vídeo de cámara es VFR y aparece desincronización, generar **copia de trabajo CFR** mediante transcodificación controlada, preservando original y comprobando audio.

## 3. Color
- SDR Rec.709/BT.709 es perfil inicial compatible y recomendado por YouTube para SDR. El vídeo HDR requiere conversión tonal correcta (*tone mapping*) si se entrega SDR; cambiar una etiqueta de color no equivale a convertir HDR.
- En CapCut, si hay diferencia visual, comprobar ajuste automático, color del proyecto, exportación y comparación lado a lado **del archivo exportado en el mismo reproductor**.
- Exportar una sola vez desde el montaje final siempre que sea posible. Evitar cadena de MP4 finales reimportados que recomprime y degrada.

## 4. Audio, subtítulos, música y efectos
- Fuente maestra de voz: capturar sin clipping y escuchar auriculares. Música por debajo de la voz, con fundidos/ducking; verificar que palabras y SFX no se enmascaran. Para el master, AAC-LC estéreo 48 kHz como perfil interoperable.
- No asignamos LUFS de broadcast ni un volumen máximo arbitrario como obligatorio de TikTok/Meta/YouTube. Medir si se dispone de herramienta, evitar picos digitales y cotejar volumen por oído/dispositivo.
- Subtítulos: texto fiel, puntuación y nombres técnicos correctos, contraste móvil, fuera de controles, si es posible archivo SRT fuente versionado. Verificar en móvil; no existe una única «safe zone» garantizada para todas las plataformas.
- Música/efectos/fuentes/fotos: registrar licencia, autor, URL, fecha y si cubre **TikTok + IG + FB + YouTube**. Un catálogo musical disponible dentro de una app no implica derechos cruzados para un master usado en otras.

## 5. Fotograma, master y control automático
- Video vertical sin barras; 1080x1920, H.264 progresivo, 30 fps cuando la captura/conform aprobado esté alineado; SFX/voz presentes cuando el guion lo requiere.
- YouTube recomienda MP4, H.264 High, audio AAC o compatible, 48kHz, SDR BT.709 y como referencia **8 Mbps para 1080p/30 SDR** (no bitrate mágico para todas las redes). Ajustar por complejidad, detalle y test visual.
- `python scripts/inspeccionar_video.py delivery/master_final.mp4 --master --fps 30` comprueba dimensiones, FPS, codec, pista de audio y muestra aviso si el color SDR no está etiquetado. No verifica nitidez, claridad de voz, licencias, ortografía ni safe zones: revisión manual obligatoria.
- Probar el **MP4 final exportado**, no solo la vista previa. Ver entero en móvil, inspeccionar cortes, glitches, legibilidad, voces, colores, silencio, CTA, miniatura, vídeo correcto y ausencia de marca CapCut.
- No hacer nuevo master si ya existe una versión aprobada; versionar `..._v01.mp4`, `..._v02.mp4`; registrar archivo exacto en `PUBLICACION.md`.

## 6. Sencillo diagnóstico «CapCut exportó peor»
Comparar original Samsung y export CapCut **del mismo fotograma y reproductor**. Revisar si el original que ingresó en CapCut era archivo comprimido por WhatsApp, fotos/capturas VFR, color HDR/SDR, reescalado, codificación y bitrate real. No asumir un defecto del editor si el archivo de entrada ya había perdido calidad.

## Fuentes verificadas (2026-11-06)
- https://support.google.com/youtube/answer/1722171 — Perfil de subida/bitrate/Rec.709/FPS.
- https://ads.tiktok.com/business/es/guides/video-advertising-guide — Vertical 9:16, legibilidad y zonas de interfaz, práctica publicitaria.
- https://workflow.frame.io/guide/checksums-backups — Integridad al copiar y respaldo.
- https://helpx.adobe.com/es/premiere/desktop/organize-media/ingest-proxy-workflow/ingest-and-proxy-workflow.html — Principios de proxies y conservación originales (referencia aplicable, sin afirmar que CapCut implementa ese mecanismo).
