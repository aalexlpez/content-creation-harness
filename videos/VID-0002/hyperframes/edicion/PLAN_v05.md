# VID-0002 · Plan de edición v05 (más profesional)

Plan del 2026-11-18, a petición de Ale: «mantener la voz mejorada y armar un plan más profesional: mejores animaciones, mejores textos y todo lo que hemos comentado». **Es un plan:** Ale lo aprobó el 2026-11-18 («Sí, apruebo» a los puntos 1 a 4 de la §11) y se ejecutó: ver [§14, estado y desviaciones](#14-estado-y-desviaciones-v05-entregada).

Parte de la v04 (`media/trabajo/edicion_v04.mp4`, 55,48 s, hecha en la otra computadora) y de su [REVIEW](REVIEW.md). Sigue [MOTION](../../../../guias/MOTION.md) (AV-010) y [E-01](../../../../guias/EDICION.md#edición-continua). El plan anterior (v01) queda en [PLAN.md](PLAN.md).

**Lo que no verifiqué:** la v04 no está en esta computadora (solo su código y su REVIEW), así que no la vi renderizada, y la voz mejorada la medí pero no la escuché. Los diagnósticos salen del REVIEW, de lo que Ale comentó («zooms muy sencillos», «trozos que ni se leen») y del código.

## 1. Qué se mantiene y qué cambia

**Se mantiene** (Ale lo aprobó o funciona):
- La voz mejorada por Ale: `media/trabajo/audio_mejora/ensayo_2_voz_original-mejorada-v2.wav` (WAV 16 bits, 48 kHz, 63,2509 s, desfase 0 ms frente a la original, −21,7 LUFS, sin ruido en las pausas).
- Los cortes `KEEP` en silencios medidos (`cortes.py`): 5 tramos, 55,48 s.
- Los tres modos (cámara, escenario y demo en ventana con la cara abajo), la banda de subtítulos (y 862 / y 1190) y los tres golpes fuertes como máximo.
- El banco de sonidos de Pixabay (AV-011), con cada efecto en su tramo audible.

**Cambia:**
1. Los textos pasan de «un subtítulo uniforme» a **tres niveles** (§4).
2. Los cortes dejan de verse como saltos: **encuadres alternos y cortes con causa** (§5).
3. Las transiciones suben de «barrido y fundido» a **cinco tipos, cada uno con causa en pantalla** (§6).
4. La demo se rediseña con **planos de inserto** y lectura garantizada (§8).
5. La mezcla usa la voz mejorada y **baja la música cuando hablas** (§9).
6. Hay una **medición automática** del render antes de enseñarlo (§10).

## 2. Qué significa «profesional» aquí (criterios medibles)

| # | Criterio | Medida |
|---|---|---|
| 1 | Algo cambia a menudo | Un evento visible cada 0,5–1,5 s en escenario y cada 1–3 s a cámara; ningún tramo de > 3 s sin cambio |
| 2 | Jerarquía de texto | Subtítulo ≥ 56 px, palabra protagonista de 60 a 90 % del ancho, texto auxiliar ≥ 32 px, nada de 28 a 56 px que «casi» se lee |
| 3 | Cada corte tiene causa | Los 4 empalmes de `KEEP` caen en silencio medido y llevan un cambio de encuadre o una transición que los tape |
| 4 | Cada transición tiene causa | 5 tipos; ninguna que no salga de algo ya en pantalla |
| 5 | La cara sostiene | Visible ≥ 60 % del vídeo; pantalla completa sin cara ≤ 4 s seguidos (en este plan, ≤ 2 s) |
| 6 | Un protagonista por plano | Ninguna técnica protagoniza dos veces; ≤ 3 golpes de cámara |
| 7 | El sonido ayuda | Voz −14 LUFS en la mezcla, música ≈ −18 dB que baja 4 dB al hablar, pico ≤ −1 dBTP, cada efecto con causa visible |

## 3. Presupuesto de tiempo por tramo (tiempos del corte v04)

| Tramo | Tiempo | Modo | Cara visible | Presupuesto |
|---|---|---|---|---|
| T1 · Gancho | 0,0–4,6 s | Cámara | 100 % | Hoja, palabra protagonista y color, sin escenario |
| T2 · El problema | 4,6–12,8 s | Escenario | ≈ 55 % (abajo) | Gráfico ≤ 3 s sin cambio |
| T3 · La solución | 12,8–21,7 s | Cámara y escenario | ≈ 70 % | Escenario ≤ 6 s seguidos |
| T4 · La demo | 21,7–36,5 s | Escenario con ventana | ≈ 50 % + 2 insertos | Insertos a pantalla completa ≤ 2 s cada uno |
| T5 · El resultado | 36,5–40,9 s | Pantalla completa breve y escenario | ≈ 40 % | Sello + calendario + pantalla de bloqueo |
| T6 · La serie | 40,9–50,3 s | Escenario | ≈ 55 % | Un icono protagonista de ≥ 300 px por vez |
| T7 · Cierre | 50,3–55,5 s | Cámara | 100 % | Acento final, llamada a la acción y una cola de 0,8 s |

**Cola final:** la voz acaba en 55,39 s y el vídeo en 55,48 s. Las reglas piden que la última línea se sostenga ≥ 2 s. Se añaden **0,8 s** de imagen final (último fotograma) con la música que se apaga, y el vídeo mide 56,3 s. Es decisión de Ale (§11).

## 4. Textos: tres niveles

| Nivel | Qué es | Tamaño | Cuándo |
|---|---|---|---|
| 1 · Subtítulo base | La banda actual, palabra activa invertida | ≥ 66 px, encogido si no cabe en 980 px | Siempre |
| 2 · **Palabra protagonista** | Una palabra o frase corta que ocupa el cuadro | 60–90 % del ancho (≈ 650–970 px) | **Máximo 7 en todo el vídeo**, una por idea |
| 3 · Orientación | Cabecera con título de tramo y **contador «1 / 5»** (como Erik Taveras) | ≥ 32 px | Escenario |

**Las siete palabras protagonistas** (tiempos del corte v04):

| # | t (s) | Texto | Tratamiento | Receta |
|---|---|---|---|---|
| 1 | 1,28 | ABANDONASTE | **Detrás de la persona**, 1,2 s, con el bajón de color | `caption-parallax-layers` del catálogo, con `remove-background` |
| 2 | 3,26 | CALMA | Entra de golpe y se va con «todavía no» | `caption-kinetic-slam` |
| 3 | 12,31 | SIN GANAS | Dentro de la tarjeta del jueves, ≥ 900 px de ancho | `text-state-swap` («?» → SIN GANAS) |
| 4 | 14,59 | Plan B | **Ocupa el cuadro**, se encoge a su sitio y el resto de la frase se completa | `lead-word-zoom-assemble` (shotcraft) |
| 5 | 17,24 | GRATIS | Un precio con «$» que se tacha y se vuelve GRATIS | `text-state-swap` + `number-pop-in` |
| 6 | 29,60 | NO TUVE TIEMPO | Primer inserto de la demo (§8) | la propia interfaz, a pantalla completa |
| 7 | 53,26 | «Este febrero, **no.**» | Acento con «no.» invertido (2.º golpe de 3) | `brand-frame-snap` |

**Reglas de tipografía** (marca v2, AV-007):
- **Solo Plus Jakarta Sans.** El sistema de dos fuentes de `caption-editorial-emphasis` no se usa: el contraste sale de tamaño y peso (Medium frente a ExtraBold).
- Sin neón, brillo, degradados ni sombras difusas.
- La palabra activa del subtítulo base cambia de peso (500 → 800) además de invertirse, como `caption-weight-shift`.
- **El texto no refuerza un dato inventado.** El calendario deja de decir «MITAD DE ENERO» y dice **«MEDIADOS DE ENERO»**: C1 (la mitad) es un claim X y la regrabación dirá «la mayoría» o «mucha gente».

## 5. Cortes

- **Los 4 empalmes de `KEEP`** (en 32,60, 48,00, 50,34 y 53,85 s del corte v04) llevan cada uno un **cambio de encuadre del 100 % al 112 %** (o a la inversa), con corte seco de 4 fotogramas. Los encuadres alternan en cada frase a cámara: así el salto parece intencional y no un error.
- **Corte de voz en J:** en los cambios de modo, el gráfico entra **0,15–0,25 s antes** de la palabra que lo nombra (el espectador lo anticipa), nunca después.
- **Respiraciones:** como la voz mejorada tiene silencio digital absoluto, cada empalme conserva el crossfade de 12–15 ms de `cortes.py` y se escucha con la música debajo. Si un empalme suena seco, se prueba con 40 ms de «aire» tomado de otra pausa de la voz de Ale, nunca sintetizado (AV-008).
- **Un cambio de plano por frase**, no uno por ráfaga: en cámara, 100 % → 112 % → 100 % siguiendo el énfasis de la voz.

## 6. Transiciones: cinco tipos, cada uno con causa

| # | t (s) | Tipo | Cómo se hace | Causa en pantalla |
|---|---|---|---|---|
| 1 | 4,56 | **Zoom a través** de un objeto | La hoja de calendario del gancho crece hasta llenar el cuadro y su cara «ENERO» es el calendario del escenario | La hoja ya está en pantalla |
| 2 | 8,23 | **Cortina de la barra «/»** (la que ya tenemos) | La barra cruza en diagonal y el contenido cambia detrás | La barra es la marca |
| 3 | 21,7 | **El objeto se vuelve el mundo** | La tarjeta «Plan B» se ensancha (`card-resize`) y se convierte en la ventana de la app | La tarjeta ya está en el escenario |
| 4 | 40,97 | **Llevar al otro lado** | La frase del plan viaja del calendario a la pantalla de bloqueo, y esta se encoge hasta la tarjeta «01» de la serie | La frase y la pantalla ya están |
| 5 | 12,79 y 50,3 | **Cambio de fondo con desenfoque** | El escenario sube con un desenfoque de 8 px que se resuelve en 0,13 s | Cambio de modo |

**Cortes de empalme** (los 4 de §5): oscurecer ≈ 40 % durante 3 fotogramas antes del corte.

**Ya no se usan:** el deslizamiento simple del escenario (se sustituye por el desenfoque de #5) y los fundidos entre tramos.

## 7. Lista de eventos v05 (tiempos del corte v04)

Modo **C** = cámara · **E** = escenario · **I** = inserto a pantalla completa (≤ 2 s). Sonidos del banco `banco_audios`. En cada fila, «protagonista» es el elemento que lleva el plano.

| t (s) | Palabra | Modo | Evento | Receta | Sonido |
|---|---|---|---|---|---|
| **T1 · Gancho** | | | | | |
| 0,00 | — | C | Fotograma 0: cara + hoja ENERO + música | MG-01 | música entra |
| 0,32 | febrero | C | La hoja gira a FEBRERO | `page-turn-transitions` | `page-turn` |
| 1,28 | abandonaste | C | **ABANDONASTE detrás de ti** + bajón de color (golpe 1) | parallax + grade | `cinematic-impact-boom` −14 dB |
| 3,26 | Calma | C | **CALMA** y encuadre al 112 % | kinetic-slam | pop grave |
| 3,82 | Todavía no | C | Vuelve ENERO, vuelve el color | MG-01 | `page-flip` |
| **T2 · El problema** | | | | | |
| 4,56 | Pero | C→E | **Zoom a través** de la hoja al calendario del escenario; cabecera «1 / 4 · EL PROBLEMA» | transición #1 | `whoosh_largo_misterioso` (tramo 0,47–1,71) |
| 5,18 | mediados | E | Días 1–14 marcados cada vez más rápido (acelerado, R2) | `list-reveal` | `pencil_scribble_short` ×6 en escalera |
| 6,41 | ya la… | E | Las marcas se detienen; etiqueta «MEDIADOS DE ENERO» | `marker-underline-title` | `scribble-pencil` |
| 7,05 | tirado la toalla | E | Las marcas caen y se apagan | caída escalonada | `whoosh_fast-simple-chop` |
| 8,23 | Y la… | E | **Cortina «/»** a «¿Y ESE DÍA?»; cabecera «2 / 4» | transición #2 | `whoosh_esquiva` |
| 9,3 | no piensa | E | La semana se marca, menos el jueves | check | — |
| 11,29 | día | E | El jueves crece al centro con «?» | `slam-entrance-moves` suave | `pop` |
| 12,31 | ganas | E | **SIN GANAS** sobre la tarjeta | `text-state-swap` | `pop-universfield-bubble` |
| **T3 · La solución** | | | | | |
| 12,79 | Soy cerobytes | E→C | Sube el escenario con desenfoque; vuelve la cara entera | transición #5 | `whoosh_basico` |
| 14,59 | Plan B | C | **Plan B ocupa el cuadro** y se encoge a la tarjeta; sin rótulo duplicado | `lead-word-zoom-assemble` | `click-photos` |
| 15,23 | Esta es… | C→E | Baja el escenario; cabecera «3 / 4 · LA SOLUCIÓN» | transición #5 | `whoosh_esquiva` |
| 17,24 | gratis | E | «$» que se tacha y se vuelve **GRATIS** | `text-state-swap` | `pop` |
| 18,84 | planear | E | Ficha «PARA ESE DÍA» enlazada al jueves de T2 | `draw-svg-trace` | `pop-universfield-bubble` |
| 21,64 | primera | E | Contador «01 /» (`number-wheel`) | `number-wheel` | `light-switch` |
| **T4 · La demo** | | | | | |
| 21,70 | (pausa) | E | La tarjeta Plan B se ensancha hasta ser la ventana de la app | transición #3 | `whoosh_largo_misterioso` |
| 23,80 | eliges | E | Plano 1: pregunta y campo; el propósito se escribe | planos por grupo | `iphone_typing` (1,2 s) |
| 26,12 | febrero | E | Plano 2: el mes cambia y la pantalla pasa a gris | MG-06 | `page-turn` |
| 26,87 | eliges | E | Plano 3: seis tarjetas, escalonadas y aceleradas | `chip-grid-single-select-blackout` | `pop` / `pop-universfield-bubble` alternados, en escalera |
| 29,60 | no | **I** | **Inserto a pantalla completa de 1,6 s:** la tarjeta «No tuve tiempo» se presiona y negrea; la voz sigue, la cara vuelve en J | inserto | `screen-tap` |
| 31,50 | armas un plan | E | Plano 4: los dos campos del plan; entra la frase con huecos | `title-demote-to-label` | `whoosh_fast-simple-chop` |
| 32,60 | Si llego | E | Los huecos se rellenan por palabra clave | MG-06 | `phone-keyboard-typing` ×3 |
| **T5 · El resultado** | | | | | |
| 36,20 | (antes de «Con esto») | E | La frase del plan queda quieta | — | `tension-riser` que acaba en 36,54 |
| 36,54 | Con esto | **I** | **Inserto de 1,8 s:** cae el sello «Este febrero, no.» con golpe de cámara (golpe 2) | `slam-entrance-moves` | `office-stamp` (un golpe) |
| 38,54 | calendario | E | La frase pasa a evento de calendario | MG-07 | `new-notification` |
| 40,06 | fondo | E | El plan viaja a la pantalla de bloqueo | transición #4 | `message-envoye-iphone-apple` |
| **T6 · La serie** | | | | | |
| 40,97 | En esta… | E | La pantalla de bloqueo se encoge hasta la tarjeta «01»; cabecera «4 / 4 · LA SERIE» | transición #4 | `whoosh_basico` |
| 43,50 | a la semana | E | «1 POR SEMANA» y una sola tarjeta nueva, grande (≥ 300 px) | `list-reveal` | `pop` |
| 45,66 | productividad | E | **Un icono protagonista de ≥ 300 px**; el siguiente lo sustituye | `icon-swap` | `pop-universfield-bubble` |
| 46,86 | ciencia | E | Siguiente icono | `icon-swap` | `pop` |
| 49,20 | cualquier ámbito | E | La fila se aleja y se ve que sigue | `pull-back-reveal` | `whoosh_fast-simple-chop` |
| **T7 · Cierre** | | | | | |
| 50,34 | Así que | E→C | Sube el escenario | transición #5 | `whoosh_esquiva` |
| 51,58 | arma tu plan B | C | Encuadre al 112 % | — | — |
| 53,26 | febrero | C | **«Este febrero, no.»** con golpe (golpe 3) | `brand-frame-snap` | `cinematic-riser-impact` (solo el golpe) |
| 54,35 | está en mi perfil | C | Sin etiqueta de link: la dirección aún no existe (C8) | — | — |
| 55,48 | — | C | Cola de 0,8 s: último fotograma, la música se apaga | — | música en fundido |

**Recuento:** ≈ 38 eventos visuales en 55,5 s, 7 palabras protagonistas, 5 tipos de transición, 3 golpes fuertes y 2 insertos a pantalla completa.

## 8. La demo (T4): planos y lectura

Los problemas que señaló Ale en la v03 («zooms muy sencillos», «trozos que ni se lee bien la pantalla»):

| Problema | Solución |
|---|---|
| Zooms de 0,9 como máximo | Se mantiene el tope de 0,9 para no cortar campos, pero cada plano **empieza en un detalle** (≥ 1,1) y se abre a la composición: «de lo pequeño a lo grande» |
| Trozos ilegibles | Regla: **ningún texto de la interfaz por debajo de 28 px en el render** (se mide en la hoja de 1 fps). Si no llega, ese plano pasa a ser inserto |
| Mucho tiempo en la misma ventana | **Dos insertos** a pantalla completa de ≤ 2 s (el toque en «No tuve tiempo» y el sello), con la voz continuando y la cara de vuelta antes de terminar la frase (corte en J) |
| Toque con anillo | Sin anillo: presión del botón (0,97 y vuelta) y negreo, como ya hace MG-06 v04 |
| Cámara plana | Empuje claro **solo una vez por paso**, de 0,55 s, y el resto del paso en reposo |

## 9. Sonido y mezcla

- **Voz:** la voz mejorada (WAV) sustituye a la del vídeo. Está 4,4 dB más baja que la original, así que `mezcla.py` la normaliza a −14 LUFS en la mezcla final.
- **La música baja cuando hablas** (`sidechaincompress` de ffmpeg, −4 dB con ataque de 80 ms y recuperación de 400 ms). La voz limpia deja silencios digitales, y sin esta bajada la música lofi se nota más que antes.
- **Dos másteres** (AV-012, propuesta): **sin música** (voz y efectos) para añadir el sonido de tendencia dentro de cada app, y **con la música lofi** para publicar directo. Ale decide.
- **Efectos:** los del banco, con el pico un fotograma después del evento y volumen en escalera en las repeticiones. Los nuevos de este plan reutilizan los archivos existentes (`whoosh_largo_misterioso` para el zoom a través y la tarjeta que se ensancha).
- **Opcional, no necesario:** si Ale quiere sumar al banco de Pixabay un «riser corto de 1 s» y un «impacto ligero», mejorarían el sello y el «no.» final.

## 10. Medición antes de enseñar (REVIEW §4, punto 4)

Un script `revisar.py` (solo biblioteca estándar y ffmpeg) sobre el MP4 renderizado:
- loudness, pico y rango (`ebur128`);
- **tramos sin cambio visual de más de 3 s** (diferencia entre fotogramas);
- tiempo en que la cara es visible (detección por zona de la ventana de cámara);
- cada corte de voz cae en un silencio < −60 dB;
- una hoja de contacto de 1 fotograma por segundo y la de 360 px de ancho.

El resultado se escribe en `REVIEW.md` y la revisión independiente se hace **antes** de enseñar el corte, no después.

## 11. Qué necesita el sí de Ale

| # | Qué | Por qué | Recomendación |
|---|---|---|---|
| 1 | Instalar 4 piezas del catálogo con `hyperframes add`: `caption-kinetic-slam`, `caption-weight-shift`, `card-resize`, `zoom-through-transition` | Son código editable (Apache-2.0) que acelera el trabajo; yo las adapto a la marca v2 antes de usarlas | Sí |
| 2 | Descargar el modelo de `remove-background` de HyperFrames (≈ 168 MB, unos 2 fotogramas por segundo en CPU) | Para el texto detrás de la persona (ABANDONASTE y CALMA). Solo se procesan 2 tramos de ≈ 1,5 s | Sí; si no, ABANDONASTE va delante |
| 3 | Cola final de 0,8 s | Pide la regla de la última línea (≥ 2 s) | Sí |
| 4 | Un máster sin música y otro con música (AV-012) | Para canciones de tendencia en la app | Sí, pero no bloquea este plan |
| 5 | Subir HyperFrames a la 0.9.64 | Las skills ya describen funciones nuevas | No, seguir en la 0.9.42 |

## 12. Orden de trabajo (cuando Ale apruebe)

1. Registrar la voz mejorada en `cortes.py` y `mezcla.py` (apuntan hoy a un `.mp3` que no existe aquí) y regenerar `corte_v03.mp4` y `demo_v03.mp4` en esta computadora. Las fuentes de MG-06 y MG-07 v04 están en Git; sus renders se rehacen.
2. Pedir el resto de piezas (§11) y adaptarlas a la marca.
3. Componer la v05 (`index.html`) con la lista de §7 y las reglas de §4, §5 y §6. La v04 queda en `versiones/`.
4. `hyperframes check`, instantáneas, `revisar.py` y revisión P0/P1.
5. Render **sin pérdida** intermedio y render final con `--quality delivery` ([TECNICA](../../../../guias/TECNICA.md)).
6. Mezcla con la voz mejorada y la música que baja cuando hablas.
7. **Revisión de Ale en el celular**, una sola ronda de correcciones.

## 13. Lo que NO se hace

- Cambiar de editor (DaVinci Resolve) ni instalar Submagic o plugins de terceros: no aportan a este ensayo (análisis del 2026-11-18).
- Neón, glitch, flashes, grano, degradados o cualquier efecto que choque con la marca v2 (MOTION §8).
- Reemplazar la composición entera: se reescribe lo que cambia y se mantiene el sistema de `render(t)`.
- Inventar cifras en pantalla (C1) ni fijar el link (C8) mientras no exista.

## 14. Estado y desviaciones (v05 entregada)

**Entrega (2026-11-18):** `media/trabajo/edicion_v05.mp4` (con música) y `edicion_v05_sin_musica.mp4`, 56,43 s, 1080×1920, 30 fps, con la voz mejorada de Ale. Composición `index.html` (la v04 queda en `versiones/edicion_v04.html.txt`), `cortes.py`, `mezcla_v05.py` y `revisar.py`. `hyperframes check`: sin errores ni avisos (queda el de archivo largo y el de «película sin sonido», porque la composición sale muda y el sonido se mezcla aparte).

| Plan | Hecho | Nota |
|---|---|---|
| 7 palabras protagonistas | **6** | ABANDONASTE y CALMA detrás de la persona (`remove-background`, 114 fotogramas, 1,8 s por fotograma en CPU), «Plan B» que llena el cuadro, SIN GANAS, GRATIS y «Este febrero, no.». NO TUVE TIEMPO es el inserto de la demo, no una palabra aparte |
| Contador «1 / 5» en la cabecera | Hecho | 5 tramos, no 4 |
| Encuadre 100/110 % en los empalmes y por frase | Hecho | Instantáneo en los 4 empalmes; 0,3 s en el resto |
| Oscurecido de 3 fotogramas antes de cada empalme | Hecho | 40 % negro |
| Zoom a través de la hoja | Hecho | Hoja ×5,9 hasta el escenario en 0,34 s |
| Cortina «/» | Se mantiene | Solo entre «El problema» y «¿Y ese día?» |
| La tarjeta se ensancha hasta ser la ventana | Hecho | `card-resize` como técnica: tarjeta 640×300 → ventana 960×520 |
| Llevar al otro lado | Hecho | La pantalla de bloqueo se encoge hasta la tarjeta 01 |
| Cambio de fondo con desenfoque | Hecho | Desenfoque de 7 px al entrar y salir el escenario |
| 2 insertos de ≤ 2 s | Hecho | 1,5 s el más largo (medido) |
| Tarjeta protagonista de ≥ 300 px en «La serie» | **260 px** | La tarjeta mide 480×440 con un icono de 260 px; con 300 px no cabía sobre la banda de subtítulos |
| Planos de la demo que empiezan en ≥ 1,1 | **No** | Se mantiene el tope de 0,9 para no cortar campos; el «detalle» lo hacen los insertos a pantalla completa (zoom 1,0 en una pantalla de 1080 px) |
| `caption-weight-shift` | **No** | Cambiar el peso de la palabra activa mueve el ancho de la línea. Se evitó para que el subtítulo no tiemble |
| Gráficos 0,15–0,25 s antes de la palabra | **Parcial** | Los eventos nuevos (hoja, cortina, ventana) anticipan; el resto sigue en la palabra |
| Piezas del catálogo | **Como técnica** | Los 4 componentes instalados (`compositions/components/`) llevan degradados, sombras y glitch RGB genéricos, y cargan GSAP desde una CDN: no se montan. Se reescribió su técnica con la marca v2 |
| Cola de 0,8 s | **1,0 s** | Para que la última frase dure ≥ 2 s, que pide `check` |
| Color de la cara con `media-treatment` | **No** | Sin tiempo en este ensayo; sigue el filtro CSS del gancho (desaturación de 8 fotogramas) |
| Música baja 4 dB al hablar | Hecho | `sidechaincompress`, umbral 0,05, razón 3, ataque 80 ms, recuperación 400 ms |
| Dos másteres | Hecho | Mismo sonido (−14,3 LUFS, pico −1,3 dBFS) con y sin música; AV-012 sigue como propuesta |

**Medición del render** (`revisar.py`): escenario 67.6 % del vídeo · cara tapada por insertos 5.7 % (inserto continuo más largo 1.5 s) · ningún tramo del escenario sin cambio de más de 3 s · voz en los empalmes: 32.6 s → -57.2 dBFS, 48.0 s → -48.2 dBFS, 50.34 s → -63.1 dBFS, 53.85 s → -64.7 dBFS.
