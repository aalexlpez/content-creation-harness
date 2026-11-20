# VID-0003 · Edición v01 (2026-11-20)

Edición del ensayo 3 con el estilo de VID-0002 v06f. Orden: `python preparar.py` → `npx hyperframes@0.9.42 render . -q delivery -o ../../media/trabajo/edicion_v01_imagen.mp4` → `python mezcla.py ../../media/trabajo/edicion_v01_imagen.mp4 ../../media/trabajo/edicion_v01`. La demo se graba antes, con `node demo/grabar.mjs ../../media/trabajo/demo_real/toma1` (variables `NPXNM` y `CHROME`, ver el script) y se copia a `assets/demo_real.mp4` con 0,8 s de último fotograma.

| Archivo | Qué hace |
|---|---|
| `preparar.py` | `KEEP` (cortes en silencios medidos), recorte del 4K (`CROP` 1,6×), look B y piel, voz mejorada alineada (+25 ms), recursos R01/R02/R04, música por compases (`SEG`) y `palabras.js` |
| `palabras.js` | Generado: palabras en tiempo del corte (Parakeet, con el inicio de frase corregido) y datos del corte. No se edita a mano |
| `index.html` | Composición: promesa, picos («HICE UNA APP», el plan, «¿Y TÚ?»), nodos flotantes, demo en el celular, subtítulos |
| `demo/grabar.mjs` | La app real de staging al ritmo de la voz (`ACCIONES`) |
| `mezcla.py` | Voz, 38 efectos reales y música; dos másteres a −14 LUFS |
| `beats_top-flow-happy-rock.json` | Golpes de la canción (`hyperframes beats`) |

**Medios** (fuera de Git, `videos/VID-0003/media/`): `originales/` (toma 4K y `audio-mejorada.wav`), `originales/broll/` (R01, R02, R04 y `fuentes.txt`), `trabajo/` (corte, voz, música, demo y másteres), `descartado/`.
