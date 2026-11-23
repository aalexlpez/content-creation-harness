# Color

Herramientas de color de la serie. Por defecto, **sin filtro** (desde el 2026-11-20, set nuevo). El **look B** («cálido cinematográfico», elegido por Ale el 2026-11-19 para VID-0002) queda como referencia, que se aplica con ffmpeg en `videos/VID-0002/hyperframes/v06/preparar.py` (`LOOK_B` y `PIEL`). Reglas en [EDICION → Color](../../guias/EDICION.md#color) y ajustes de cámara en [SET → Configuración vigente](../../guias/SET.md#configuración-vigente-2026-11-19).

| Archivo | Qué es | Estado |
|---|---|---|
| `cine_calido_v02.cube` | LUT 3D (33³) para tomas Rec.709 del celular: levanta los medios tonos, curva en S con negros mate, sombras algo frías y luces cálidas, piel protegida (más cálida y saturada) y el resto −10 % de saturación | **En prueba.** Probado solo en una toma de oficina subexpuesta (2026-11-19); falta probarlo en el set |
| `hacer_lut.py` | Genera el `.cube` (solo biblioteca estándar): `python marca/color/hacer_lut.py marca/color/cine_calido_v02.cube` | — |

- **Uso:** CapCut (Ajustar → LUT), DaVinci Resolve, Premiere o ffmpeg (`-vf lut3d=marca/color/cine_calido_v02.cube`).
- **No se aplica encima del look B:** los dos hacen lo mismo y se suman.
- **No arregla la luz:** da color, no volumen. Con una toma oscura, primero exposición (SET).
- Si se cambia, se sube la versión del archivo (`cine_calido_v03.cube`) y se anota aquí.
