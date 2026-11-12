# Marco de contenido de Alexander

Sistema para planificar, escribir, producir y medir vídeos verticales cortos (YouTube Shorts, TikTok, Reels, Facebook y posts de X que enlazan al vídeo) trabajando entre Alexander y Claude. Todo es texto versionado en Git más un pequeño CLI en Python que crea expedientes, registra aprobaciones y comprueba que nada se rompa.

**Versión 5.1.0** · Python 3.11+ (solo biblioteca estándar) · Windows, macOS y Linux.

## Arranque en 5 minutos

```bash
python scripts/marco.py estado                                   # qué hay y qué falta
python scripts/marco.py idea canal "Cómo grabo mis vídeos con un móvil" --problema "..." --pilar PROCESO
python scripts/marco.py semana actual --horas 5 --hipotesis "El gancho por resultado retiene más"
python scripts/marco.py video I-0001 --ensayo                    # expediente de prueba, no se publica
python scripts/marco.py validar
```

Después: Claude redacta el guion en `videos/VID-0001/GUION.md`, Ale lo revisa y dice "OK-2", se registra con `marco.py aprobar OK-2 VID-0001 --evidencia "..."`, se graba, se monta y se cierra con el OK-3. El ciclo completo está en [guias/FLUJO.md](guias/FLUJO.md).

En Windows, si `python` abre la Microsoft Store, usa `py -3 scripts/marco.py ...`.

## Mapa

```
CLAUDE.md            instrucciones para Claude (y AGENTS.md para otros agentes)
guias/               FLUJO · EDITORIAL · GUIONES · EDICION · TECNICA · SET
marca/               identidad provisional, tokens y cuentas por red
proyectos/<id>/      qué se puede demostrar de cada proyecto (miminiapp, canal…)
registro/            IDEAS.csv · DECISIONES.md · METRICAS.csv
semanas/AAAA-WNN/    SEMANA.md: lote, horas, hipótesis, OK-1, retrospectiva
videos/VID-NNNN/     GUION.md · PRODUCCION.md · CIERRE.md · MEDIOS.csv · media/ (fuera de Git)
templates/           moldes que usa el CLI
referencias/         capturas de referencia visual (solo estudio, sin licencia de uso)
scripts/             marco.py (CLI), nucleo.py, reglas.py, medios.py
pruebas/             pruebas automáticas
```

## Órdenes del CLI

| Orden | Para qué |
|---|---|
| `estado` | Tablero: ideas sin asignar, semanas, vídeos activos, siguiente paso |
| `validar` | Comprueba IDs, enlaces, tablas, aprobaciones, estados, publicaciones y métricas |
| `proyecto <id>` | Crea la ficha de un proyecto nuevo |
| `idea <proyecto> "<título>"` | Añade una idea con ID automático |
| `semana <AAAA-WNN\|actual\|siguiente>` | Crea la semana |
| `video <idea> [--semana] [--ensayo]` | Crea el expediente con ID automático y lo enlaza al lote |
| `aprobar OK-1\|OK-2\|OK-3 <objetivo> --evidencia "…"` | Registra la aprobación con su huella |
| `mover <VID> <ESTADO>` | Cambia el estado si se cumplen los requisitos |
| `huellas <VID\|semana>` | Muestra si las aprobaciones siguen vigentes |
| `medios <VID> [--comprobar] [--copia <carpeta>]` | Inventaría los medios o verifica una copia de seguridad |
| `inspeccionar <archivo>` | Metadatos del vídeo frente al perfil 1080×1920/30/H.264/SDR (necesita ffprobe) |

## Git y GitHub

- **Se versiona** todo el texto: guías, registros, guiones, producción, cierres y `MEDIOS.csv`.
- **No se versiona**: `videos/*/media/`, vídeos, audios, renders y proyectos del editor (ver `.gitignore`). Guarda los medios en un disco o nube aparte y verifica las copias con `marco.py medios VID-NNNN --copia <ruta>`.
- `.gitattributes` fija UTF-8 con saltos LF en todos los sistemas. Además, las huellas normalizan los saltos de línea, así que un editor que guarde en CRLF no invalida aprobaciones.
- **Usa un repositorio privado**: `referencias/` contiene capturas de terceros sin licencia de publicación, y el marco guarda datos de tu set y tu planificación.
- GitHub Actions ejecuta `validar` y las pruebas en Windows y Linux en cada push (`.github/workflows/validar.yml`).

Configuración local opcional, fuera de Git: `marco.local.json` con `{"ffprobe": "C:/ruta/a/ffprobe.exe"}`.

## Pruebas

```bash
python -m unittest discover -s pruebas -v
```

Historial de cambios en [CHANGELOG.md](CHANGELOG.md).
