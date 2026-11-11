# Montaje final gratuito: CapCut Desktop (principal) y Shotcut (respaldo)
**Versión:** v3.5 · **Estado:** nueva etapa opcional aprobada como parte del flujo; desempeño y exportación en el equipo real por validar.
**Dueño:** Alexander · **Identidad audiovisual:** marca personal, independiente de MiMiniApp.

## Objetivo y límite
HyperFrames + Claude Code crea y renderiza las animaciones complejas. CapCut Desktop GRATIS ensambla las grabaciones Samsung S24+, las escenas HyperFrames, música, títulos y subtítulos, corrige cortes y exporta el master. Shotcut sustituye a CapCut cuando se necesiten funciones sin bloqueo Pro o una alternativa completamente libre. **No se exige CapCut para producir/publicar si la versión HyperFrames ya está aprobada**.

## Por qué se elige y qué no está demostrado
- CapCut confirma herramientas gratuitas de corte, unión, texto, audio, transiciones y exportación sin marca de agua en edición estándar usando medios y recursos libres. Algunas plantillas/IA/fuentes/efectos/exportaciones son de pago y pueden bloquear la entrega.
- Shotcut es software libre GPL, gratis para uso comercial y sin cuenta ni subscripción. Publica requisitos de 8 GB RAM para HD y opciones de proxies/preview scaling. No se ha medido su rendimiento frente a CapCut en este PC.
- Kdenlive es editor alternativo avanzado y totalmente libre, pero no es obligatorio instalarlo.
- Los proyectos HTML/GSAP de HyperFrames no se convierten en pistas editables nativas de CapCut. Se importan archivos de vídeo/audio previamente exportados; cambios de una animación interna se hacen en HyperFrames y se reemplaza su render.
- Las capas con transparencia (MOV ProRes 4444 o PNG) requieren una prueba de compatibilidad con la versión de editor concreta antes de adoptarse como entrega habitual.

## Especificaciones de intercambio (perfil inicial; no suponer valor universal)
- Proyecto de edición: 1080 x 1920 píxeles, 9:16, 30 fps, progresivo, SDR/Rec.709 cuando sea posible.
- HyperFrames exporta **escenas MP4 H.264 sin logos insertados**. Cuando se precisan superposiciones, ofrece un archivo transparente verificado o entrega ya compuesto; **no depende de ProRes alfa sin prueba de importación**.
- Se conservan por separado, si aplica, voz WAV/MP3, música licenciada, SFX, subtítulos SRT UTF-8 y portada PNG.
- Cámara Samsung: conservar el ARCHIVO ORIGINAL sin transcodificar (no necesariamente RAW). **Transferir directamente, nunca por WhatsApp**; para un equipo limitado considerar **copias proxy 1080p H.264** cuando la captura HDR/HEVC/4K produzca saltos. Proxies no sustituyen al original archivado.
- Master inicial MP4 H.264/AAC a 1080 x 1920 30 fps para material grabado/conformado a 30; si la captura es 60 fps o HDR, registrar decisión de conversión y comprobar el resultado. Verificar bitrate y calidad visual en dispositivo móvil. No insertar barras, marcas ni finales de CapCut.
- Un solo paso final de compresión cuando sea posible; evitar exportar y reimportar masters varias veces.

## Procedimiento / Gates
| Gate | Responsable | Entregable | Condición de paso |
| --- | --- | --- | --- |
| G6: escenas terminadas | Claude Code/HyperFrames | `exports/escenas/*.mp4`, `exports/audio/`, `manifest.md` | duración y sincronía revisadas; fuentes y derechos registrados |
| G6.5: intercambio | humano/IA | prueba `10s_intercambio` | importar + superponer clips, exportar gratis sin marca, audio OK |
| G7: picture lock | humano en CapCut Gratis o Shotcut | proyecto nativo del editor y `master_preview.mp4` | orden, cortes y narrativa bloqueados; ajustes finales de audio/color después |
| G7.5: acabado y QA | humano | `MONTAJE_FINAL.md`, `REVISION.md`, `QC_MASTER.md` | marca, licencias, texto, audio, duración, resolución, sin función premium ni watermark |
| G8: publicación | humano | `master_final.mp4`, `thumbnail.png`, copy + links | aprobación expresa y plataforma verificada |
| A0: archivo | humano | copias externas + manifest | aplica `14_POLITICA_ARCHIVO_Y_RESTAURACION.md` |

**Si la edición en HyperFrames ya basta:** G6.5–G7 se marcan `NO_NECESARIO`, G7.5 revisa directamente su master; no añadir trabajo por costumbre.

## Carpeta por vídeo
```
V01/
  media/camera/original/
  hyperframes/                   # fuentes de las escenas y revisión
  media/camera/proxy/
  exports/
    escenas/                     # 01_intro.mp4, 02_demo.mp4, etc.
    audio/                       # voz.wav, musica.wav, sfx/
    captions/                    # subtitulos.srt (si aplica)
    grafismos/                   # overlays con alfa ya comprobado
  montaje_final/
    capcut_o_shotcut/            # proyecto nativo y recursos referenciados
  MONTAJE_FINAL.md                # documento siempre local
  delivery/
    master_final.mp4
    thumbnail.png
  PUBLICACION.md                  # documentación siempre local
```

## Check mínimo antes del primer vídeo
1. Instalar desde sitios oficiales. Importar grabación real Samsung de 10 s y una escena HyperFrames de 8 s.
2. Añadir una pista de música (recurso propio o con licencia clara), voz original, SRT de muestra y una etiqueta de texto simple.
3. Exportar **1080 x 1920 / 30fps** sin comprar nada ni activar una prueba Pro. Confirmar marca de agua ausente, audio correcto, subtítulos legibles, render reproducible.
4. Si CapCut bloquea la entrega gratuita, repetir en Shotcut y registrar el motivo; no contratar Pro automáticamente.
5. Archivar junto a fuentes la versión del editor y el proyecto nativo, con recursos relativos cuando sea viable.

## Límites de tiempo y coste
- El tiempo de recorte y mezcla manual no consume tokens de Claude. Si se le pide al agente escribir SRT, generar una pista o diagnosticar fallos sí utiliza IA.
- Dos rondas de correcciones por vídeo como máximo antes de revisar brief. Priorizar retoques en el editor, reservar HyperFrames para modificaciones de animaciones internas.
- Registrar minutos de edición manual, minutos de render, incidencias de importación, coste premium = 0.

## Fuentes oficiales consultadas 2026-11-06
- CapCut Plan Gratis: https://www.capcut.com/es-es/pricing/
- CapCut exportar sin marca: https://www.capcut.com/es-es/help/video-without-watermark
- CapCut limitaciones Pro: https://www.capcut.com/help/join-capcut-pro-for-exporting
- CapCut Windows requisitos: https://www.capcut.com/es-es/resource/capcut-for-windows
- CapCut SRT externo: https://www.capcut.com/es-es/help/how-to-import-subtitles
- Shotcut oficial: https://shotcut.org/ y https://www.shotcut.org/FAQ/
- Kdenlive requisitos: https://docs.kdenlive.org/es/getting_started/installation.html

## Refuerzo de calidad (v3.5)
Antes de concluir G7.5, ejecutar `scripts/inspeccionar_video.py` sobre el **master** y completar `QC_MASTER.md`; registrar `INGESTA.md` del archivo original Samsung. No sustituir grabación por copia de WhatsApp. Si no se requiere CapCut, marcar `NO_NECESARIO` y preservar un único master desde HyperFrames.
