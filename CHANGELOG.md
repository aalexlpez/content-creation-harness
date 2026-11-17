# Changelog

## Sin publicar

- **Edición continua** (AV-009, propuesta): método nuevo en [EDICION](guias/EDICION.md#edición-continua), patrón E-01. Probado en un ensayo de edición sobre el corte de TikTok de VID-0001 (`videos/VID-0001/hyperframes/ensayo-edicion/`).
- **Sonidos reales** (AV-008): fuera los efectos sintetizados por código; grabados por Ale o CC0 con licencia registrada.
- **Motion graphics de VID-0002** en HyperFrames: MG-01 v02 (hoja de calendario con giro 3D), MG-02 (rótulo de presentación), ambos con alfa (ProRes 4444 y WebM), y MG-06/MG-07 v02 (maqueta de Plan B a pantalla completa con cámara, teclado y frase que viaja al fondo de bloqueo). Un proyecto por pieza en `videos/VID-0002/hyperframes/`.
- [TECNICA](guias/TECNICA.md): cómo se trabaja con HyperFrames (render por tiempo, no medir el DOM, 3D, transparencia, video de cámara, tiempos por palabra con Parakeet, catálogo).
- [referencias/MOTION.md](referencias/MOTION.md): repositorios, herramientas y el reel de referencia estudiados, con su veredicto.
- **Identidad visual v2** (AV-006): cerobytes «creative tech» (wordmark en minúsculas con barra diagonal, paleta de cuatro colores y Plus Jakarta Sans, AV-007). Sustituye al perfil TEMP y a la v1 (PR-002). El **kit vectorial v1.2** vive en `marca/kit/` (37 SVG y 53 PNG, reconstrucción no maestra: el wordmark es vectorial pero no es el diseño maestro original) y se documenta en `marca/IDENTIDAD.md`.
- **Tipografía** Plus Jakarta Sans (Google Fonts, OFL) en `marca/fuentes/plus-jakarta-sans/`, en lugar de Satoshi (AV-007). Se exportaron de nuevo los 15 PNG con texto del kit.
- Rótulo inferior 9:16 **ajustado** (`marca/kit/*/rotulo-inferior-video-9x16-ajustado.*`): desplazado 100 px sobre el kit v1.2 para no pisar la banda de subtítulos.
- **Español latinoamericano** en voz, guiones y textos en pantalla (CONTENIDO-LATAM-001).
- La ficha de Plan B del repositorio `soycerobytes/miminiapp` pasa a ser la fuente de verdad (PROD-17).
- **Experimento:** `videos/VID-0001/GUION_BEATS.md` propone un guion por momentos, edición simple y prompts de motion graphics. Contradice D-EDICION y otras reglas hasta que se formalice.

## 5.1.0 · 12 de noviembre de 2026

- **Posts en X** (DIST-X-001): X entra en el plan de publicación como `VID-NNNN-X-NN`. No lleva vídeo: en `archivo` va la publicación de TikTok o Instagram a la que enlaza. El validador y el OK-3 rechazan enlaces a archivos, a otras redes o a publicaciones fuera del plan. También rechazan un post registrado antes que su vídeo. Se aceptan métricas con la plataforma `X`.
- Cuenta de X en `marca/CUENTAS.csv`.
- **Corregido:** las pruebas dependían del estado real de `CUENTAS.csv`. Ahora parten siempre de cuentas sin verificar.

## 5.0.0 · 12 de noviembre de 2026

Marco limpio para empezar a producir, pensado para trabajar entre Alexander y Claude.

- **CLI único** `scripts/marco.py`: `estado`, `validar`, `proyecto`, `idea`, `semana`, `video`, `aprobar`, `mover`, `huellas`, `medios` e `inspeccionar`. IDs automáticos y semana `actual`/`siguiente`.
- **Aprobaciones con un comando.** OK-1, OK-2 y OK-3 guardan aprobador, fecha, evidencia y huella, y actualizan el estado. El corte fijado (*picture lock*) y la autorización por destino se integran en el OK-3.
- **Huellas robustas:** normalizan saltos de línea y espacios, y las tablas se comparan celda a celda. Un CRLF de Windows o de Git ya no invalida nada.
- **Portabilidad Git:** `.gitattributes` (UTF-8 + LF), `.gitignore` (medios fuera), `.editorconfig` y GitHub Actions en Windows y Linux.
- **Medios:** inventario `MEDIOS.csv` con SHA-256 y verificación de copias de seguridad. Sustituye al sistema de archivo con soportes físicos.
- **Guías nuevas** en `guias/`: FLUJO, EDITORIAL, GUIONES (recupera familias de guion, ganchos y voz de la v3.5), EDICION, TECNICA y SET.
- **Comandos de Claude Code** en `.claude/commands/`: ideas, semana, guion, rodaje, cierre y retro.
- Proyecto `canal` para contenido del creador mientras MiMiniApp no tenga su primera miniapp.
- **Corregido:** la semana recién creada fallaba la validación por un enlace a `videos/`; el manifiesto de release quedaba desfasado tras cada cambio.
- **Eliminado:** legado v3.5, auditoría, manifiesto de release y migración. Siguen en el historial de Git (etiqueta sugerida `v4.0.0-rc.1`).
