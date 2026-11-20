# Valores de referencia de la edición (VID-0003 v04, aprobada por Ale el 2026-11-20)

Los números que hacen que la edición salga pulida. Están en `videos/VID-0003/hyperframes/edicion/` (`index.html`, `preparar.py`, `mezcla.py`); aquí se explican para no tener que adivinarlos. Si cambias uno en la base, cámbialo aquí.

## Lienzo y zonas seguras (1080×1920)

| Zona | Uso |
|---|---|
| 0–160 px arriba | Barra de la app («Siguiendo / Para ti»): nada importante |
| ≥ 168 px | Primera línea útil: promesa (178), acento final (168) |
| Cabeza | Tercio superior (≈ 240–950 px con el recorte 1,6×) |
| 1190 px | Subtítulos a cámara (en caja, sobre la camiseta) |
| 1000–1400 px | Tarjeta `over` en el pecho (400×400, x 340) |
| 1420 / 1440 px | Subtítulos con tarjeta / en la demo |
| > 1540 px y 120 px de la derecha | Descripción y botones de TikTok y Reels: nada importante |

## Marca y tipografía

- Paleta: `#0B0B0D` (tinta), `#1E2937`, `#0D213F` (navy), `#F5F6F8` (blanco roto), `#B7C0CC` (secundario). Solo **Plus Jakarta Sans** (Medium 500, Bold 700, ExtraBold 800). MiMiniApp (violeta, lima) solo dentro del celular.
- Subtítulos: ExtraBold 66 px, mayúsculas, caja navy con la palabra activa invertida (blanco roto, texto tinta), palabras siguientes en `#B7C0CC`. Grupos de 2–4 palabras, que caben en 980 px (escala automática), cortan siempre en «.», «?», «!». Entran en 0,16 s (expo) y salen en 0,12 s.
- Palabras protagonistas: ExtraBold 120–250 px, mayúsculas, borde de 10 px `rgba(11,11,13,.55)`, entrada con rebote (`backOut2`, 0,22–0,24 s, escala 1,5 → 1) y `GLOW` = `drop-shadow(0 0 10px rgba(245,246,248,.55)) drop-shadow(0 0 26px rgba(245,246,248,.22))`. Máximo 3–4 por vídeo.
- Promesa: ExtraBold 46 px, dos líneas, borde 8 px; una palabra clave en caja blanca («**gratis**»). De 0,4 a 3,0 s, entrada con desenfoque 8 → 0 px.
- Acento final: «Este año, *sí*.» (Bold 64 + ExtraBold 96 en caja blanca con `GLOW`), se revela de izquierda a derecha en 0,45 s y la palabra en caja cae con rebote 0,3 s después.

## Capa flotante

| Elemento | Diseño |
|---|---|
| Tarjeta / píldora | Borde 3 px `rgba(245,246,248,.92)`, fondo `rgba(11,18,38,.74)` con `backdrop-filter: blur(14px)`, radio 30 px (píldora 999 px); variante `inv` en blanco roto con texto tinta |
| Teléfono flotante | 190×330, borde 5 px blanco roto, radio 38 px, «/» de la marca y etiqueta («PLAN B», «01 /»). Posición (885, 600) |
| Entrada | 0,5 s: escala 0,78 → 1, desenfoque 14 → 0 px (expo); al aparecer en un pico, «pop» 1,25 → 1 en 0,4 s |
| Salida | Últimos 0,3 s: escala → 0,9, desenfoque → 12 px |
| Deriva | ±5–14 px y ±1,6°, con fase propia por nodo (el teléfono, quieto) |
| Flechas | Trazo 4 px, se dibujan en 0,55 s (easeOut), punta tras 0,42 s, un punto que viaja; curva por encima de la cabeza (`apex` 200–395). Máx. 3 por vídeo, sin resplandor |

## Cámara y transiciones

| Qué | Valor |
|---|---|
| Arranque | Escala 1,12 → 1,0 en 0,45 s |
| Deriva | 100 → 103 % por plano (`easeIO`), reinicio solo en cortes reales (`SHOTS`) |
| Picos | Acercamiento instantáneo 1,10 (pico 1) y 1,18 + sacudida 9 px amortiguada (pico 3) |
| Empalmes a cámara | Cambio de escala 1,0 ↔ 1,07 y oscurecido 35 % en los 3 fotogramas previos (no en recursos, demo ni picos) |
| `transform-origin` del vídeo | 50 % 30 % (la cara no se sale al acercar) |
| B-roll `full` | Entrada 1,08 → 1 en 0,3 s + empuje 1 → 1,05 durante el plano |
| B-roll `over` | Sube 40 px y escala 0,92 → 1 en 0,3 s, giro −3° → −1,8°, borde 3 px, radio 28 px |

## Demo (celular de la app real)

- Grabación 1080×2342 a escala `K0 = 0,5` en un marco de 568×1199 (radio 74, borde 2 px `rgba(245,246,248,.32)`), centro (540, 880).
- `FRAMES = [t, centro y en la grabación, escala del texto]`: 0,5 = celular entero; 0,8–0,92 = una zona legible; 0,98–1,0 = a todo el ancho. Transición entre encuadres 0,45 s (`easeIO`). Perspectiva `rotateY −9°`, `rotateX 4°` solo cuando el celular se ve entero.
- Entrada: crece desde el teléfono flotante en 0,5 s; salida: se encoge a él en 0,4 s. La cara detrás: desenfoque 18 px y brillo 50 %.
- Golpe del pico 2: escala × 1,035 con caída exponencial.

## Sonido

| Qué | Valor |
|---|---|
| Voz | La mejorada de Ale, alineada; a −17,4 LUFS antes de mezclar; compresor suave (umbral −18 dB, ratio 2) |
| Música | 13 dB bajo la voz (LUFS integrados); baja ≈ 5 dB al hablar (`sidechaincompress` umbral 0,04, ratio 4, ataque 60 ms, release 350 ms); −2 dB en la demo; +4 dB en los picos sin voz y en la cola |
| Master | −14 LUFS integrados, limitador a 0,84 (pico ≤ −1,4 dBFS), AAC 256 kb/s 48 kHz; dos másteres (con y sin música) |
| Efectos | Recortados a su tramo audible, pico 1 fotograma después del evento, fundido de salida 40 ms |

Efectos de VID-0003 v04 (32; banco de Pixabay de Ale, carpeta `BANCO_AUDIOS`):

| Evento | Archivo (recorte) | Pico dBFS |
|---|---|---|
| Tarjeta / píldora que aparece | `pop.mp3` (0,19–0,31) o `pop-universfield-bubble.mp3` (0–0,18), alternando | −14 a −19 |
| Flecha | `pencil_scribble_short.mp3` (0–0,29) | −21 |
| Hoja de calendario | `page-turn.mp3` (0–0,55) / `page-flip.mp3` (0,64–1,77) | −17 a −20 |
| Pico 1 | `cinematic-impact-boom.mp3` (0–1,92) + `whoosh_fast-simple-chop.mp3` | −15 / −19 |
| «Plan B» protagonista | `click-photos.mp3` (0–0,84) | −16 |
| Precio tachado | `scribble-pencil.mp3` (0,3–0,75) | −18 |
| Teléfono → celular de la demo | `whoosh_largo_misterioso.mp3` (0,47–1,71) | −16 |
| Toque en la app (solo ≈ 4) | `screen-tap.mp3` (0,40–0,70) | −11 a −14 |
| Tecleo | `iphone_typing.mp3` (2,58–3,98 / 5,19–6,39) | −21 |
| Pico 2 (el plan) | `tension-riser.mp3` por su final + `office-stamp-varios-veces.mp3` (0–0,66) | −19 / −10 |
| Recordatorio | `new-notification.mp3` (0–1,38) | −17 |
| Desplazamiento / encogerse | `whoosh_basico.mp3` / `whoosh_fast-simple-chop.mp3` | −17 a −19 |
| Pico 3 | `cinematic-riser-impact.mp3` desde 0,05 s antes del pico | −10 |

## Música de la serie

`top-flow-happy-rock.mp3` (145 BPM, golpes en `beats_top-flow-happy-rock.json`): intro 0–6,7 · batería 6,7–13,3 · estribillo 13,3–24,9 · valle 26,5–39,8 · subida 39,8–53,0 · estribillo 2 53,0–64,6 · final 76,6. Tramos de VID-0003 en `preparar.py → SEG`.
