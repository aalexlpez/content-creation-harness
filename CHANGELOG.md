# Changelog

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
