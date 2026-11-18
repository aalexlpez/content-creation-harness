# VID-0002 · Plan de edición continua (ensayo 2)

Composición final del ensayo 2 con el método de [Edición continua](../../../../guias/EDICION.md#edición-continua) (AV-009, propuesta) y lo aprendido en el ensayo 1 (`videos/VID-0001/hyperframes/ensayo-edicion/`). Si el montaje sale entero de aquí, `Editor: NO_NECESARIO`.

Estándar: [guias/MOTION.md](../../../../guias/MOTION.md). Cada evento de la sección 3 lleva su receta (carta de video-shotcraft o pieza del catálogo) antes de animarse.

Plan de la edición más profesional (v05): [PLAN_v05.md](PLAN_v05.md).

Estado: **v01 entregada el 2026-11-17** (`media/trabajo/edicion_v01.mp4`; Ale: «ha quedado muchísimo mejor»). Antes: (`media/originales/ensayo_2.mp4`, 63,25 s, limpio en CapCut por Ale). Fuentes, GSAP y logo ya están en `fonts/`, `lib/` y `assets/`. El `index.html` se escribe después del corte, con los tiempos por palabra reales.

## 1. Qué tiene que traer Ale

- Un archivo por sesión (o por beat) en `videos/VID-0002/media/originales/`, sin renombrar ni recomprimir (nada de WhatsApp: cable, Quick Share o Drive con calidad original).
- Por beat, 2–3 tomas con un segundo quieto antes y después de cada frase. Las palabras son propias: la voz literal del GUION es guía.
- Audio del DJI dentro del mismo vídeo (comprobado al oírlo, SET §2.3).
- Cuáles son las tomas buenas, si ya lo sabe. Si no, Claude propone a partir de la transcripción.

## 2. Pasos al recibirlo

| paso | qué | comando o salida |
|---|---|---|
| 1 | Ingesta: metadatos frente al perfil y huella | `python scripts/marco.py inspeccionar videos/VID-0002/media/originales/<archivo> --perfil ingesta` · `python scripts/marco.py medios VID-0002` · fila en PRODUCCION → Ingesta |
| 2 | Copia de trabajo H.264 (si viene HEVC o VFR) y audio a WAV 48 kHz | `media/trabajo/bruto_h264.mp4`, `media/trabajo/bruto.wav` (ffmpeg) |
| 3 | Transcripción con tiempos por palabra del bruto | `npx hyperframes@0.9.42 transcribe media/trabajo/bruto.wav --engine parakeet --language es --json` → texto corregido a mano (Parakeet traduce partes) |
| 4 | **Corte**: elegir toma por beat, quitar silencios > 0,4 s y muletillas. Lista de cortes (entrada/salida en el bruto) para que Ale la apruebe | `media/trabajo/corte_v01.mp4` + tabla en este archivo |
| 5 | Si cambian las frases: actualizar la voz literal del GUION, subir `Version` a v02 y avisar de que el OK-2 se renueva | GUION.md |
| 6 | Tiempos por palabra **del corte** (se repite el paso 3 sobre el corte) | `media/trabajo/corte_v01.json` |
| 7 | Lista de eventos por frase con sus tiempos reales (sección 3 rellenada). **Ale la revisa** antes de animar | este archivo |
| 8 | Composición `index.html` sobre el corte: video con `data-has-audio`, escenario, cabecera, subtítulos propios, barrido de tramo. Reutiliza MG-01/02/06/07 como piezas dentro del escenario o a pantalla completa | `npx hyperframes@0.9.42 lint .` y `check .` |
| 9 | Revisión con capturas en el inicio, mitad y fin de cada tramo | `snapshot . --at … --no-end -o media/trabajo/capturas` |
| 10 | Render sin efectos | `render . --format mp4 --fps 30 --resolution portrait -o media/trabajo/edicion_v01.mp4` |
| 11 | Segunda pasada de sonido con el **banco de Pixabay de Ale** (`Documents/proyectos/referencias/banco_audios`): los momentos de la sección 3 y la música en todo el vídeo a −18 dB. Licencia de Pixabay → filas en CIERRE → Derechos | `sonido.py` adaptado (base: el del ensayo 1) |
| 12 | Revisión en el celular por Ale y una ronda de correcciones como máximo | PRODUCCION → Correcciones |

## 3. Lista de eventos sobre el corte (v01, pendiente de revisión de Ale)

Sale del corte `media/originales/ensayo_2.mp4` (63,25 s). Los tiempos por palabra están en `media/trabajo/corte_palabras.json`: Parakeet frase a frase, con el texto corregido a mano. En 5 frases el tiempo de cada palabra se repartió y se ajusta al componer.

- **Modos:** **C** = a cámara · **E** = escenario (panel `#0D213F` arriba, toma bajada 700 px) · **P** = pantalla completa.
- **Cabecera:** derecha fija en E: «/ PLAN B · MINIAPP 01».
- **Sonidos:** de `Documents/proyectos/referencias/banco_audios` (Pixabay), recortados a su tramo audible.
- **Música:** `watrfallkero-lofi-beat-chill` en todo el vídeo, a −18 dB bajo la voz; se corta con la última palabra.

| t (s) | palabra | modo | evento | receta (MOTION §8) | sonido |
|---|---|---|---|---|---|
| **T1 · Gancho** | | | | | |
| 0,00 | — | C | Fotograma 0: cara + hoja «ENERO» ya en pantalla (miniatura) | MG-01 v02 | entra la música |
| 0,32 | febrero | C | La hoja gira a FEBRERO | `page-turn-transitions` (MG-01) | `page-turn` |
| 1,28 | abandonaste | C | Desaturado y frío en 8 fotogramas | grade por tiempo | `cinematic-impact-boom`, bajo (−14 dB) |
| 3,26 | Calma | C | Zoom 10 % sobre la toma | punch-in en el contenedor | — |
| 3,82 | Todavía no | C | La hoja vuelve a ENERO y el color vuelve de golpe | MG-01 | `page-flip` (tramo 0,64–1,77) |
| **T2 · El problema** | | | | | |
| 4,66 | Pero | C→E | Entra el escenario; cabecera «EL PROBLEMA» | E-01 | `whoosh_basico` |
| 5,18 | mediados de enero | E | Calendario de enero; los días 1–14 se marcan uno a uno, cada vez más rápido | `list-reveal` acelerado (R2) | `pencil_scribble_short` ×6, volumen en escalera |
| 6,41 | la mitad | E | Las marcas se detienen a mitad de mes; la mitad derecha queda vacía | `marker-underline-title` | `scribble-pencil` |
| 7,05 | tirado la toalla | E | Las marcas caen y se apagan | caída escalonada | `whoosh_fast-simple-chop` |
| 8,23 | Y la mayoría | E | Cortina «/»; cabecera «¿Y ESE DÍA?» | barra en diagonal (E-01) | `whoosh_esquiva` |
| 11,29 | día | E | Un solo día se ilumina en el centro | `slam-entrance-moves` suave | `pop` |
| 12,31 | ganas | E | Aparece en el día «SIN GANAS» | `text-state-swap` | `pop-universfield-bubble` |
| **T3 · La solución** | | | | | |
| 12,79 | Soy cerobytes | E→C | Sube el escenario; vuelve la cara entera | E-01 | `whoosh_basico` |
| 14,59 | Plan B | C | Rótulo «Plan B · para tu propósito» / «HERRAMIENTA N.º 1», 2,5 s | MG-02 | `click-photos` |
| 15,23 | Esta es | C→E | Entra el escenario; tarjeta «PLAN B» al centro | `card-flip-reveal` | `whoosh_esquiva` |
| 17,24 | gratis | E | Ficha «GRATIS» | pop en escalera | `pop` |
| 18,84 | planear | E | Ficha «PARA ESE DÍA» | ídem | `pop-universfield-bubble` |
| 21,64 | primera | E | Contador «01 /» que cae junto a la tarjeta | `number-pop-in` | `light-switch` |
| **T4 · La demo** | | | | | |
| 22,70 | (pausa) | E→P | La tarjeta crece hasta llenar el cuadro y se vuelve la maqueta (con «MAQUETA DE ENSAYO») | el objeto se vuelve el mundo (MOTION §5) | `whoosh_largo_misterioso` (tramo 0,47–1,71) |
| 23,80 | eliges | P | Tecleo del propósito con el teclado español | `typewriter-moves` (MG-06) | `iphone_typing` (tramo de 1,2 s) |
| 26,12 | febrero | P | Salto a febrero; la pantalla se vuelve gris | MG-06 | `page-turn` |
| 26,87 | eliges | P | Seis tarjetas de obstáculo, escalonadas y aceleradas | `chip-grid-single-select-blackout` | `pop` / `pop-universfield-bubble` alternos, en escalera |
| 29,60 | no tuve tiempo | P | Toque en «No tuve tiempo» y negreo | ídem (1 fotograma gris) | `screen-tap` |
| 31,50 | armas un plan | P | Las demás tarjetas se van; entra la frase con huecos | `title-demote-to-label` | `whoosh_fast-simple-chop` |
| 33,60–36,64 | Si llego… estiramiento | P | Los huecos se rellenan uno por palabra clave («casa», «8», «cinco minutos», «estiramiento»); el color vuelve poco a poco | MG-06 | `phone-keyboard-typing` en 4 golpes cortos |
| **T5 · El resultado** | | | | | |
| 36,70 | (antes de «Con esto») | P | Tensión: la frase del plan se queda quieta | — | `tension-riser` (termina en 37,54) |
| 37,54 | Con esto | P | Cae el sello «Este febrero, no.» con golpe de cámara (1 de 3 golpes del vídeo) | `slam-entrance-moves` + `impact-feedback` (MG-07) | `office-stamp` (un solo golpe) |
| 39,54 | calendario | P | El plan pasa a evento de calendario | MG-07 | `new-notification` |
| 41,06 | fondo | P | El plan viaja a la pantalla de bloqueo | llevar al otro lado (MOTION §5) | `message-envoye-iphone` |
| **T6 · La serie** | | | | | |
| 41,97 | En esta | P→E | La pantalla de bloqueo se encoge y se vuelve una tarjeta «01» del escenario; cabecera «LA SERIE» | transformación (MOTION §5) | `whoosh_basico` |
| 44,65 | miniaplicación | E | Fila de tarjetas «01 · 02 · 03 …» que se construye | `list-reveal` | `pop` ×3 en escalera |
| 45,68 | semana | E | Etiqueta «1 POR SEMANA» | `text-state-swap` | `click-photos` |
| 46,66 | productividad | E | Icono + palabra en la tarjeta 02 | `icon-swap` | `pop-universfield-bubble` |
| 47,86 | ciencia | E | Icono en la 03 | ídem | `pop` |
| 49,53 | minijuegos | E | Icono en la 04 | ídem | `pop-universfield-bubble` |
| 51,06 | cualquier ámbito | E | La fila se completa con «…» y se aleja | `pull-back-reveal` | `whoosh_fast-simple-chop` |
| 54,04 | libres | E | Ficha «LIBRES» | interruptor | `switch-toggle` |
| 54,60 | gratis | E | Ficha «GRATIS» | interruptor | `light-switch` |
| 55,24 | cualquier persona | E | Icono de persona que se multiplica en tres | escalonado | `pop` ×3 suave |
| **T7 · Llamada a la acción** | | | | | |
| 56,60 | Así que | E→C | Sube el escenario | E-01 | `whoosh_esquiva` |
| 57,88 | arma tu plan B | C | Rótulo «ARMA TU PLAN B» en el tercio superior | MG-02 (variante) | `click-photos` |
| 59,56 | febrero | C | Acento «Este febrero, *no*.» con «no.» invertido (2.º golpe del vídeo) | `brand-frame-snap` | `cinematic-riser-impact` (solo el golpe) |
| 61,80 | link | C | Flecha pequeña hacia la zona del perfil | `draw-svg-trace` | `benkirb-shine` (tramo corto, −12 dB) |
| 63,16 | perfil | C | Final en seco; la música se corta con un fundido de 0,2 s | — | — |

**Recuento:** 44 momentos con sonido, más la música de fondo. Tres golpes fuertes: sello, «no.» final y el bajón del gancho.

**Sin usar:**
- `magic-spell` y `sparkle-subtle-cartoon`: suenan a dibujo animado;
- `teclado-pc`, `phone-keyboard-clicks-volumen-bajo`, `mouse-click-sfx` y `whoosh_pitch_alto`;
- `cinematic-riser-impact` completo (solo se usa su golpe).

**Subtítulos:** en E, los propios (ExtraBold, palabra activa invertida, y ≈ 868); en C y en P, la misma banda abajo, encima de y 1330.

## 4. Lista de cortes

El corte lo hizo Ale en CapCut (2026-11-17) desde el bruto de 13 min y la composición parte de él. Los pasos 2–6 de la sección 2 quedan cubiertos así:

- copia de trabajo `assets/corte.mp4` (H.264, fotograma clave cada 30 para que el seek funcione);
- audio `media/trabajo/corte.wav`;
- tiempos por palabra en `media/trabajo/corte_palabras.json`.

Decisiones de Ale (2026-11-17, «Todo lo que me recomiendas, hazlo»):

- demo a pantalla completa;
- música en todo el vídeo;
- edición en BORRADOR y OK-2 sobre el guion v02.

## 5. Lo que hay que rehacer o comprobar

- Los renders de MG-01, MG-02, MG-06 y MG-07 que lista `MEDIOS.csv` **no están en este equipo** (no existía `media/`). Se vuelven a renderizar desde `hyperframes/MG-0N/` o se integran como escenas dentro de esta composición (recomendado: una sola composición, sin depender de la transparencia en CapCut).
- Las anclas internas de MG-06/MG-07 salen del bruto antiguo: se recalculan con los tiempos del corte.
- C3–C6 se revisan contra la ficha v06 antes del OK-2.
