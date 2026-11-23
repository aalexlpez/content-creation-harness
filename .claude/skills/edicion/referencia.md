# Valores de referencia de la edición (VID-0003 v04 aprobada el 2026-11-20; texto y color de la v07, dirección v2 aprobada el 2026-11-21)

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

- Paleta: `#0B0B0D` (tinta), `#1E2937`, `#0D213F` (navy), `#F5F6F8` (blanco roto), `#B7C0CC` (secundario) **+ degradado «Señal» (AV-014)**: `--sen` `#F5F6F8` → `#7DB4FF` → `#2E6BFF`, `--sen-suave` `#FFFFFF` → `#CFE1FF` → `#7DB4FF` (escenarios, bordes, barra), `--sen-caja` `#5E9BFF` → `#2E6BFF` (cajas con texto blanco roto), `--sen-brillo` (con una franja blanca que cruza). Siempre a **119°** (perpendicular a la barra «/»). Solo **Plus Jakarta Sans** (Medium 500, Bold 700, ExtraBold 800). MiMiniApp y Plan B (violeta, lima) **solo dentro del celular**.
- **Sombra sutil en todo texto sobre imagen** (AV-014): `--sombra` = `drop-shadow(0 2px 3px rgba(4,10,28,.45)) drop-shadow(0 8px 18px rgba(4,10,28,.32))`; en tarjetas, `box-shadow: 0 6px 14px rgba(4,10,28,.35)`.
- **Texto en tres niveles** ([MOTION §10.2](../../../guias/MOTION.md)):
  - *Frase* (nivel 1): Bold 50 px, **minúsculas**, borde 4 px `rgba(11,11,13,.45)` + `--sombra`; palabra a palabra (sube 14 px y aparece en 0,32 s, `expo`), sale subiendo 18 px en 0,18 s. A cámara y = 1035 (por encima de la estampa de la camiseta), con tarjeta en el pecho 1430, en la demo 1440 **en caja navy** (`#line.boxed`). Grupos de 2–4 palabras, que cortan siempre en «.», «?», «!». Se apaga donde hay un tratamiento grande (`QUIET`).
  - *Clave* (nivel 2): ExtraBold 128–170 px en `--sen`, a y = 1105, **fuera de la línea de la frase**; una por frase como mucho, con la entrada de su significado (vocabulario §10.3 y laboratorio §10.9).
  - *Escenario* (nivel 3): ExtraBold 250–330 px en `--sen-suave`, a y = 330–350, **detrás de la persona** (matte `assets/persona_*.webm`); letras que se juntan (interletraje 0,9 → −0,04 em en 0,6 s) y salen dispersándose. VID-0003: «ENERO» y «ESTE AÑO».
- Tratamientos de VID-0003 v07 (código en `index.html`, uno por bloque): A cascada 3D («TODOS LOS AÑOS», `rotateX` −100° → 0, 35 ms entre letras) · B impacto + brillo («METAS», 260 % → 100 % en 0,2 s, golpe de cámara 4,5 %) · C escenario · D máscara con estela + barrido diagonal a 29° («hice una APP», caja `--sen-caja`) · Máquina («GANAS», 1 letra / 2 fotogramas, cursor) · Barrido («PLANEO») · E corte en dos + barra («POR ESO HICE») · F nace de las manos (`REV`) con brillo · G trazo que se rellena («GRATIS», SVG, contorno 0,4 s + relleno a 29°) · H la barra «/» que corta («ENERO») · I golpe con eco («¿Y TÚ?», 1,8 → 1 y tres contornos) · J CTA como componente (tarjeta con borde `--sen-suave`, botón `--sen` que se pulsa en «perfil»). **Sin resplandor** (AV-013 sigue sin decidir): el relieve lo da `--sombra`.
- Promesa: ExtraBold 46 px, dos líneas, `--sombra`; «**gratis**» en caja `--sen-caja`. Entra con un barrido de izquierda a derecha (0,45 s) a los 0,3 s y sale subiendo y desenfocándose cuando entra el primer escenario (≈ 2 s).
- Acento final: «Este año, *sí*.» (Bold 64 + ExtraBold 96 en caja `--sen-caja`, con `--sombra`), se revela de izquierda a derecha en 0,45 s y la palabra en caja cae con rebote 0,3 s después.

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
| Música | **6 dB bajo la voz** (LUFS integrados); baja ≈ 3 dB al hablar (`sidechaincompress` umbral 0,05, ratio 2,5, ataque 80 ms, release 400 ms): queda **≈ 9 dB bajo la voz** mientras hablas; sin bajada extra en la demo; +2 dB en los picos sin voz y en la cola. (Hasta la v05 iba 13 dB bajo la voz y −2 dB en la demo: en el celular no se oía.) |
| Master | −14 LUFS integrados, limitador a 0,84 (pico ≤ −1,4 dBFS), AAC 256 kb/s 48 kHz; dos másteres (con y sin música) |
| Efectos | Recortados a su tramo audible, pico 1 fotograma después del evento, fundido de salida 40 ms. Los **continuos** (tecleo) se colocan **por su inicio** y duran toda la acción. **Cada efecto tiene algo que se ve en ese momento** |

Efectos de VID-0003 v06 (31; banco de Pixabay de Ale, carpeta `BANCO_AUDIOS`):

| Evento | Archivo (recorte) | Pico dBFS |
|---|---|---|
| Tarjeta / píldora que aparece | `pop.mp3` (0,19–0,31) o `pop-universfield-bubble.mp3` (0–0,18), alternando | −14 a −19 |
| Flecha | `pencil_scribble_short.mp3` (0–0,29) | −21 |
| Hoja de calendario | `page-turn.mp3` (0–0,55) / `page-flip.mp3` (0,64–1,77) | −17 a −20 |
| Pico 1 («APP» y el teléfono) | `pop.mp3` + `whoosh_fast-simple-chop.mp3` (sin boom de cine: «sonaba sin contexto») | −14 / −19 |
| «Plan B» nace de las manos | `benkirb-shine.mp3` (0–1,2), al empezar a abrirse las manos (no un clic de cámara) | −20 |
| Precio tachado | `scribble-pencil.mp3` (0,3–0,75) | −18 |
| Teléfono → celular de la demo | `whoosh_basico.mp3` (0–0,94) mientras crece | −17 |
| Toque en la app (solo ≈ 4) | `screen-tap.mp3` (0,40–0,70) | −11 a −14 |
| Tecleo | `iphone_typing.mp3` desde 2,58 / 5,19 s, **por su inicio y durante todo el tecleo** | −15 |
| Pico 2 (el plan) | `magic-spell.mp3` (0–1,6) con el estribillo 2 (sin riser ni sello: no hay sello en imagen) | −15 |
| Recordatorio | `new-notification.mp3` (0–1,38) | −17 |
| Desplazamiento / encogerse | `whoosh_basico.mp3` / `whoosh_fast-simple-chop.mp3` | −17 a −19 |
| Pico 3 | `cinematic-riser-impact.mp3` desde 0,05 s antes del pico (el riser llena el silencio) | −12 |

## Música de la serie

`top-flow-happy-rock.mp3` (145 BPM, golpes en `beats_top-flow-happy-rock.json`): intro 0–6,7 · batería 6,7–13,3 · estribillo 13,3–24,9 · valle 26,5–39,8 · subida 39,8–53,0 · estribillo 2 53,0–64,6 · final 76,6. Tramos de VID-0003 en `preparar.py → SEG`. **Las partes largas sin cambio (la demo) van sobre tramos de energía pareja:** el valle (26,5–39,8, ≈ 5 dB más bajo) suena a «bajada de volumen» si cae al abrirse la app; en VID-0003 el estribillo sigue de 13,3 a 24,5 s bajo toda la demo. Mide la pista por tramos (`ebur128`, sonoridad a corto plazo) antes de elegir.
