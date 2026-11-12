# Guía técnica

Del móvil al MP4 publicado sin perder calidad. El set (luz, cámara y micrófono) está en [SET](SET.md).

## Perfil de entrega

**1080×1920 · 9:16 · 30 fps constantes · MP4 H.264 progresivo · SDR BT.709 · AAC-LC 48 kHz.**

Es la elección interna para vídeo nuevo, por compatibilidad entre redes y por los recursos del PC. Material antiguo o con otra resolución, fps o HDR se registra y se convierte de forma controlada antes de montarlo. YouTube recomienda unos 8 Mbps para 1080p a 30 fps en SDR como referencia, no como cifra mágica ([codificación de subida](https://support.google.com/youtube/answer/1722171)).

Comprobación automática de metadatos:

```bash
python scripts/marco.py inspeccionar videos/VID-0001/media/entregas/VID-0001_v01.mp4
python scripts/marco.py inspeccionar media/originales/toma.mp4 --perfil ingesta   # solo describe
```

El inspector busca ffprobe en `--ffprobe`, en la variable `MARCO_FFPROBE`, en `marco.local.json`, en el PATH y en la carpeta de CapCut en Windows. Revisa resolución, rotación, códec, fps, cadencia, color, progresivo y audio. **No** comprueba nitidez, voz, ortografía, márgenes ni derechos: eso es el QC humano.

## Grabación

- **Cámara principal:** Galaxy S24+, lente principal 1×, vertical, 4K/30 (o 1080p/30 si el flujo va pesado). Prueba primero con **HDR de vídeo desactivado**.
- **Micro:** DJI con receptor en el móvil. Graba una prueba y **escúchala con auriculares** antes de la toma buena.
- **Parpadeo:** en España la red es de 50 Hz. Si ves bandas, prueba obturación 1/50 o 1/100.
- **Pantalla:** graba la web o la app directamente (navegador u OBS), nunca filmando el monitor salvo que sea un recurso narrativo. Usa datos de ejemplo, sin datos personales.
- **Continuidad:** rellena la ficha de set en PRODUCCION → Rodaje (posición, luz, ajustes de cámara, audio).

## Ingesta

1. Pasa el **archivo original** por USB o una transferencia sin compresión. **Nunca por WhatsApp** ni otra mensajería: recomprime y destruye detalle.
2. Guárdalo intacto en `media/originales/`. No lo recortes, no lo conviertas y no lo sobrescribas.
3. Inspecciónalo (`--perfil ingesta`) y anota en PRODUCCION → Ingesta la resolución, fps, color y audio.
4. Escucha la voz y mira una toma completa, no solo un fotograma.
5. Ejecuta `marco.py medios VID-NNNN` y haz la copia de seguridad antes de borrar nada del móvil.

**Casos especiales**

- **HDR** (HLG o PQ): hay que convertir el tono a SDR. Cambiar la etiqueta de color no es convertir. Mejor evitarlo desde la grabación.
- **VFR** (fps variable) con desincronización: crea una copia de trabajo a 30 fps constantes en `media/trabajo/` y conserva el original.
- **4K o HEVC que va lento:** crea un proxy 1080p H.264 en `media/trabajo/`. El proxy no sustituye al original en el máster. Comprueba si tu editor vuelve a enlazar el original.

## Animación (HyperFrames)

HyperFrames es el motor de animación principal (AV-001). Si falla en una prueba real, la alternativa es Remotion. Se usa solo en las escenas donde la animación aporta.

- Proyecto por vídeo en `videos/VID-NNNN/hyperframes/`. Los renders van a `media/trabajo/`.
- Entrega **MP4 por escena** (1080×1920, 30 fps, H.264), con nombres estables (`S02_v01.mp4`), más voz o audio en WAV y SRT en UTF-8 si aplica. Sin subtítulos incrustados si se van a corregir en el editor.
- Capas con transparencia (ProRes 4444 o PNG) solo si se ha probado que el editor instalado las importa.
- Prueba el **seek** en inicio, mitad y final de cada escena: debe verse el estado esperado en cada punto.
- Sin `frame.md` de marca definitiva hasta que exista una identidad aprobada. Mientras tanto, perfil TEMP.
- Documentación: [HyperFrames en GitHub](https://github.com/heygen-com/hyperframes).

**Estado:** sin instalar en el PC de Ale. La instalación necesita su autorización.

## Montaje (CapCut Desktop gratis o Shotcut)

Decisión vigente (D-EDIT): CapCut Desktop **gratis** como editor final y Shotcut como alternativa libre. Sin funciones de pago ni pruebas Pro.

1. Proyecto vertical 1080×1920 a 30 fps.
2. Importa los originales (o proxies), las escenas animadas, la voz y la música con derechos.
3. Corta siguiendo el guion. Anota en PRODUCCION → Montaje los cambios frente al guion.
4. Subtítulos: transcribe la voz e importa el SRT si hace falta. Comprueba la sincronía al principio y al final.
5. Color sobre la toma de cámara ([EDICION](EDICION.md)). La voz siempre por encima de la música.
6. Dos rondas de correcciones como máximo.
7. **Exporta una sola vez** desde los originales a `media/entregas/VID-NNNN_v01.mp4`. No reimportes y vuelvas a exportar masters.
8. Si CapCut bloquea algo por Pro, pon una marca de agua o falla el SRT, para, anota la causa y prueba en Shotcut. En Shotcut: modo vertical, V1 para la cámara y V2 para superposiciones.

Si el montaje sale completo de HyperFrames, el editor externo no hace falta: anota `Editor: NO_NECESARIO`.

Para probar la importación de subtítulos hay un SRT de muestra en [pruebas/piloto.srt](../pruebas/piloto.srt).

**Estado:** CapCut Desktop 9.7.1.4203 instalado. La exportación gratis sin marca y reabrir el proyecto están por probar: el primer vídeo ENSAYO sirve de prueba.

## QC y OK-3

Antes de pedir el OK-3, rellena CIERRE → QC. Cada campo debe quedar en `CONFORME` (o `FALLA` con el hallazgo):

| Campo | Qué se comprueba |
|---|---|
| Tecnico | `marco.py inspeccionar` sobre el máster da OK o las diferencias están justificadas |
| Imagen | Sin saltos, glitches, parpadeo ni cortes raros. Color de piel e interfaz correctos. Sin marca de agua |
| Audio | Voz clara y por encima de la música, sin saturación ni cortes, sincronía al principio y al final |
| Textos | Ortografía, tildes y eñes, tiempo de lectura, nada tapado por la interfaz de la red |
| Derechos | Cada recurso (música, efectos, fuentes, imágenes, capturas de terceros) tiene una fila en Derechos que cubre las redes del plan |
| Movil | **El MP4 exportado** visto entero en el móvil, con el brillo habitual. No vale la vista previa del editor |

Después: `marco.py aprobar OK-3 VID-NNNN --master media/entregas/VID-NNNN_v01.mp4 --evidencia "…"`.

## Diagnóstico: «CapCut exportó peor»

Compara el mismo fotograma del original y del exportado en el mismo reproductor. Antes de culpar al editor, revisa si la entrada ya venía recomprimida (WhatsApp), si era VFR o HDR, si hubo reescalado y qué bitrate real tiene el exportado.

## Publicación

- La sube Ale, red por red, con el copy y la portada del plan.
- En X no se sube el vídeo: el post con el enlace se publica después del vídeo de TikTok o Instagram al que lleva ([FLUJO → Posts en X](FLUJO.md#posts-en-x)).
- Al publicar, Ale da la URL real y Claude la añade en CIERRE → Publicaciones con la fecha. Si una red falla, anota la causa en `notas` y sigue con las demás.
- Una cuenta solo puede usarse si está `VERIFICADA` en `marca/CUENTAS.csv`.
- Divulgación: si el vídeo promociona un producto propio, revisa las normas de contenido de marca de cada red.
