# Estándar de motion graphics

Propuesta AV-010 (2026-11-17). Reúne en reglas medibles lo que enseñan las dos fuentes de oficio que usamos: el **recetario video-shotcraft** y los **estándares y el catálogo de HyperFrames**. Va por encima de cualquier receta suelta y por debajo de la marca v2 ([IDENTIDAD](../marca/IDENTIDAD.md)) y del método de [Edición continua](EDICION.md#edición-continua) (E-01):

**Orden de precedencia:** marca v2 → E-01 → este estándar → la receta concreta. Si una receta choca con la marca (neón, glitch, degradados, resplandores), gana la marca.

Una regla puede romperse a propósito, pero hay que anotar cuál y por qué en el `PLAN.md` del vídeo.

## 1. Fuentes

| Fuente | Dónde está | Qué aporta | Licencia |
|---|---|---|---|
| **video-shotcraft** (`Vincentwei1021/video-shotcraft`, commit `8710751`, 2026-11-18) | Clon fuera del repo: `C:\Users\aalex\Documents\proyectos\referencias\video-shotcraft` (99 MB). [Galería en línea](https://vincentwei1021.github.io/video-shotcraft/) | 124 recetas de plano (`references/shots/<familia>/<carta>.md`) con tiempos, curvas, «puntos críticos» y demo; reglas de estética con casos reales (`references/aesthetic-rules.md`); diseño de sonido y revisión final independiente | Código Apache-2.0. Sus audios **no**: cada uno tiene su licencia |
| **HyperFrames**: reglas | Skills instaladas en `~/.claude/skills/hyperframes*` y `media-use` (`references/motion.md`, `types/vertical.md`, `captions.md`, `overlays.md`, `sound.md`, `review.md`) | Contrato de render, movimiento medido en sus películas oficiales, zonas seguras en vertical, subtítulos, sonido y revisión | Apache-2.0 |
| **HyperFrames**: catálogo | `npx hyperframes@0.9.42 catalog --json` (448 piezas: 125 *motion-primitive*, 52 transiciones, 16 estilos de subtítulo, 17 de cámara, 13 *lower thirds*, 13 verticales) | Bloques y componentes instalables como código editable | Apache-2.0. Instalar uno (`add`) lo aprueba Ale |

Las carpetas `.md` de shotcraft están en chino. Se citan por el nombre de la carta: con él, Claude abre la carta y su demo (`demos/<familia>/<carta>/`), que es donde están los parámetros ya afinados.

**Versión:** el marco fija HyperFrames **0.9.42** (TECNICA). La última es la 0.9.64 y las skills ya describen algunas funciones nuevas. Subir de versión lo decide Ale; hasta entonces, si una orden de una skill no existe en la 0.9.42, se anota y se sigue sin ella.

## 2. Lienzo vertical

| Zona (1080×1920) | Uso |
|---|---|
| y 0–168 | Nada que se lea (barra de estado y búsqueda de la app) |
| y 168–1330 | Todo lo que se lee y el producto. En E-01: cabecera a y ≈ 272 y subtítulos del escenario a y ≈ 868 |
| y > 1330 | Solo textura o decoración (copy, usuario y botones de la red). Nada bajo la columna de botones de la derecha |
| Seguridad | Contenido dentro del 90 % del cuadro; texto dentro del 80 % |

- El fotograma 0 es la miniatura y el gancho: una cara, el resultado o una frase ya en pantalla. Nunca negro ni un logo.
- Muchos ven sin sonido: toda la voz va subtitulada y la imagen cuenta el gancho por sí sola.

## 3. Texto

| Regla | Valor | Fuente |
|---|---|---|
| Subtítulo que se lee | Altura efectiva **≥ 56 px** (≈ 5 % del alto), medida en el fotograma renderizado y no en el `font-size` | shotcraft Q11 |
| Texto auxiliar (fuente, etiqueta, nota) | ≥ 32 px. Nada que se lea por debajo de 28 px | Q11 · HF vertical |
| Palabras por grupo de subtítulo | 2–3 si hay energía, 3–5 si es conversación. Se corta en el final de frase o en pausas ≥ 150 ms | HF captions |
| Tiempo en pantalla | ≥ 0,5 s + 0,3 s por palabra; la última frase del vídeo, ≥ 2 s; un grupo nunca menos de 0,4 s | HF motion · E-01 |
| Dos estados | O **se lee** (tamaño y contraste correctos) o es **textura** (borrosa o apagada). No hay término medio: lo que no se lee, se quita | Q11 |
| Un subtítulo no debe empezar en 0,0 s | Entra entre 0,1 y 0,3 s | HF captions |
| Cada grupo se apaga del todo al salir | Fundido de 0,12 s y `visibility: hidden` al terminar | HF captions |
| El texto, después del montaje | Se reescriben rótulos y notas mirando el corte final; ningún tramo animado de más de 3 s sin texto (salvo el cierre de marca) | shotcraft C1 |

## 4. Movimiento

**Curvas por función.** Nunca la misma curva en todo: la típica `power2.out` a 0,5 s en todos los elementos delata un vídeo generado.

| Función | Curva | Duración |
|---|---|---|
| Llegada | Salida larga (`expo.out`, `power4.out`) | 0,3–0,6 s. Llega más despacio de lo que se va |
| Salida | Acelera (`power3.in`) | 40–50 % más corta que la entrada |
| Cámara, cambio de color o paso de escenario | Suave en ambos extremos (`power2.inOut`) | 0,5–0,7 s |
| Lineal | Solo rotación, progreso o el «negreo» de una selección | — |
| Rebote | Solo en posición y escala (amortiguación 0,7–0,85). La opacidad y el color nunca rebotan | — |

**Encadenado.** El siguiente elemento arranca cuando el anterior va por el 30–50 %. Desfase entre letras: 1 fotograma; entre palabras: 60–120 ms; entre elementos de lista: 40–80 ms. Las llegadas en grupo **aceleran** (cada vez más rápidas) y terminan con 0,5 s de quietud (shotcraft R2).

**Pausas.** Lo que se quiere recordar queda quieto al menos 1 s (R1). Antes del resultado, 0,3–0,75 s de espera. Un título que ya llegó no se mueve más: el movimiento pasa al siguiente elemento.

**En la duda, más lento.** La primera versión casi siempre va rápida (R3). Una interacción simulada (escribir, tocar, elegir) va a velocidad humana: quien mira debería poder hacerla a la vez.

**Una técnica, un protagonista.** Cada técnica (caer, apilar, girar, sellar) protagoniza **una sola vez** por vídeo. Lo que repite una idea ya dicha se corta (P4). Un plano, un efecto.

**Prohibido por delatar un vídeo generado** (HF motion, shotcraft Q3–Q4):
- títulos o interfaz que respiran, flotan o laten en bucle;
- un zoom lento que avanza solo al final de un plano;
- todo entra con fundido y subida;
- anillos de clic;
- rebote en la interfaz;
- vibración de cámara en mano;
- brillos o barridos de luz en cada tarjeta (como mucho uno, en el protagonista y recortado por su borde redondeado);
- golpes de cámara a pantalla completa: **≤ 3 por vídeo** (R4).

## 5. Transiciones

- Se usan 3–5 tipos por vídeo y cada uno tiene una causa en pantalla.
- Como mucho un tercio de los cambios de tramo son cortes secos.
- Dos mundos nunca se funden entre sí.
- Se corta en el fotograma más rápido del movimiento, con la misma dirección y velocidad a los dos lados.

| Transición | Cómo | Uso en E-01 |
|---|---|---|
| Cortina de la barra «/» | La barra cruza en diagonal y el contenido cambia detrás | Cambio de tramo dentro del escenario (ya en E-01) |
| El objeto se vuelve el mundo | Una tarjeta crece hasta salir del cuadro en 0,65 s y su relleno es la escena siguiente | Del escenario a una demo a pantalla completa |
| Transformación | Un contenedor se ensancha y se convierte en el siguiente (≈ 0,2 s, desenfoque horizontal 12 → 0) | Una idea del diagrama que se vuelve la interfaz |
| Llevar al otro lado | El resultado se encoge 1 → 0,6 y aterriza dentro de la escena siguiente | La frase del plan que viaja al fondo de pantalla (MG-07) |
| Cambio de fondo | El protagonista se queda y el fondo cambia de color en ≈ 0,4 s | Gancho: enero → febrero |
| Oscurecer y cortar | La imagen saliente baja ≈ 40 % durante 3 fotogramas y luego corte seco | De la cámara a la demo |

## 6. Sonido

Encima de AV-008 (solo sonidos reales):

1. **La voz es el reloj.** El texto aparece en la palabra que lo dice. No se monta al ritmo de la música.
2. **Pocos y exactos:** cada efecto tiene una causa visible:
   - whoosh: cambio de tramo o tarjeta grande que se mueve rápido;
   - golpe: aterrizaje;
   - tic suave de tecla: texto que se escribe;
   - pop: chip o número que aparece;
   - subida y golpe: el resultado, **una vez**.

   Nada de tonos, campanas o «dings» sintéticos. Si hay un movimiento con sonido propio (tecleo, toque, sello), se usa ese sonido real, recortado a lo que dura la acción (S1, S4).
3. **Sincronía:** el pico del sonido cae **un fotograma después** de la imagen. El pico de cada archivo se mide (`npx hyperframes audio <archivo> --json`), igual que el retraso del codificador AAC (≈ 1,3 fotogramas a 48 kHz), y se compensa en una sola fórmula, no efecto por efecto (S5).
4. **Repeticiones:** se alternan dos o tres tomas del mismo sonido y el volumen baja en escalera a lo largo de la serie, para que no suene a ametralladora (S2).
5. **Una tabla de efectos:** cada efecto se declara como tiempo, archivo, recorte y ganancia, con un comentario del movimiento que lo causa (S2, como el `sonido.py` del ensayo). Si cambia el montaje, se revisa la tabla entera (S3).
6. **Niveles:**
   - los golpes, 3–6 dB por encima de la cama;
   - música bajo la voz, ≈ −18 dB;
   - mezcla entre −16 y −14 LUFS, pico real ≤ −1 dBTP.

   Se mide con `hyperframes audio` sobre el render. Se dice siempre que se midió, no que se escuchó.
7. **Prueba en contexto:** un sonido se juzga ya montado en el vídeo, nunca suelto (S1).

**Bibliotecas:** el **banco de Pixabay de Ale** (AV-011) en `Documents/proyectos/referencias/banco_audios`, con nombres descriptivos. Reserva: **Sonniss #GameAudioGDC** (profesional, uso comercial sin atribución; clon local en `Documents/proyectos/referencias/sonniss-gdc-2026`, ver `videos/VID-0002/hyperframes/edicion/SONIDOS.md`). Mixkit y Freesound, rechazados por Ale al oído el 2026-11-17; ZapSplat, alternativa con crédito en la descripción. Shotcraft usa por defecto Freesound y BGM *tech-house*: aquí no se adopta (AV-008 y el rechazo del 2026-11-17).

## 7. Proceso de una capa de motion

Se integra en el orden de trabajo de E-01:

1. **Lista de eventos con receta.** En el `PLAN.md` del vídeo, cada evento lleva:
   - el tiempo de la palabra;
   - qué pasa;
   - la receta: carta de shotcraft o pieza del catálogo de HyperFrames;
   - el sonido.

   Ale la revisa antes de animar. Si hay una referencia (por ejemplo, un reel), primero se desglosa fotograma a fotograma y cada técnica se marca como «se usa» o «no se usa» (shotcraft P2).
2. **Leer la receta entera y su demo** antes de escribir. Los parámetros marcados como críticos no se rebajan (shotcraft, principio 6).
3. **Construir** con el contrato de HyperFrames:
   - todo en función del tiempo;
   - nada de `Math.random()` sin semilla ni de medir el DOM;
   - sin CSS `transform` en lo que anima GSAP;
   - tratamiento de color de la toma con `media-treatment`, no con filtros CSS.
4. **Afirmar la intención:** un `index.motion.json` con lo que debe pasar, para que `check` lo verifique (`appearsBy`, `before`, `staysInFrame`, `keepsMoving`).
5. **Comprobar** con `npx hyperframes@0.9.42 check --json`. Se corrigen los errores y se sopesa cada aviso:
   - `line_unread`: una línea que no da tiempo a leer;
   - `dead_stretch`: más de 3 s sin cambios;
   - `text_below_floor`: texto por debajo del mínimo;
   - `first_frame_empty`: el fotograma 0 está vacío.
6. **Revisar como un director duro**, no como autor:
   - `snapshot --review` (escenas, cortes y hoja a 360 px de ancho);
   - `snapshot --range` alrededor del movimiento protagonista.

   Los problemas se anotan en `REVIEW.md` con el formato `t=… · dónde · problema → cambio exacto · qué se queda` y una prioridad: **P0** (rompe la lectura), **P1** (debilita) o **P2** (pulido). Se corrigen todos los P0.
7. **Revisión independiente** antes de enseñarlo: un subagente con contexto limpio recibe solo el plan, las hojas de capturas y este estándar, y devuelve P0 y P1 (shotcraft P1 y final-review).
8. **Sonido** en una segunda pasada (§6) y render.

## 8. Mapa de recetas para la serie de miniapps

Puntos de partida. La carta o la pieza se lee antes de usarla y se viste con la marca v2.

| Necesidad | video-shotcraft | Catálogo HyperFrames |
|---|---|---|
| Hoja de calendario, cambio de mes | `transition/page-turn-transitions`, `transition/card-flip-reveal` | — |
| Escribir el propósito | `typography/typewriter-moves`, `interaction/glass-pill-dictation-typing` | `notes-reveal`, `typewriter` |
| Elegir un obstáculo | `interaction/chip-grid-single-select-blackout` (ya usada en MG-06) | `touch-indicator`, `press-ripple` |
| Diagrama que crece frase a frase | `ui-entrance/draw-svg-trace`, `ui-entrance/bezier-source-converge-merge`, `ui-entrance/list-reveal` | `svg-line-draw-loader`, `separator` |
| Tachar o marcar una palabra o un día | `typography/marker-underline-title` | `hw-underline`, `vox-annotate` (sin la textura de mano si choca con la marca) |
| Sello «Este febrero, no.» | `effects/slam-entrance-moves`, `effects/impact-feedback` | — |
| Rótulo que se vuelve etiqueta | `typography/title-demote-to-label` | `text-state-swap` |
| Cámara sobre la interfaz | `camera/crash-zoom-punch` (como mucho una vez) | `cursor-zoom-follow`, `ui-focus-zoom` |
| Cambio de tramo | `transition/line-carry-transition`, `transition/wipe-transitions` | `directional-wipe`, `zoom-through-transition` |
| Línea de tiempo (enero → febrero) | `data/timeline-travel` | — |
| Cierre de marca | `outro/ui-to-brand-morph`, `effects/brand-frame-snap` | — |
| Subtítulos del escenario | `typography/type-rhythm-sync` | `caption-highlight` (la palabra activa invertida, sin rojo), `caption-weight-shift` |

**No se usan:**
- `caption-glitch-rgb`, `caption-neon-*`, `caption-particle-burst`, `chromatic-aberration-wipe`, `camera-shake`, `drift-hold` y las piezas WebGPU o de shaders: chocan con la marca v2 o con §4;
- la plantilla Ink Press y la canalización de Remotion de shotcraft: AV-001 fija HyperFrames;
- el montaje al ritmo de la música;
- el banco de trabajo (`workbench`) de shotcraft.

**Por probar:** la exportación de shotcraft a borradores de Jianying (`jianying-export/windows_draft.py`, sin verificar en Windows) podría abrir el resultado en CapCut con subtítulos y audio editables. No se prueba sin que Ale lo pida.

## 9. Lista de comprobación antes de enseñar un corte

- [ ] El fotograma 0 tiene cara o frase; nada se lee fuera de y 168–1330.
- [ ] Todo texto que se lee mide ≥ 56 px (subtítulo) o ≥ 32 px (auxiliar) en el render; nada en un término medio.
- [ ] Ninguna técnica protagoniza dos veces; ≤ 3 golpes de cámara a pantalla completa.
- [ ] Ningún tramo de más de 3 s sin cambio (`dead_stretch`) ni línea sin tiempo de lectura (`line_unread`).
- [ ] Curvas según la función, salidas más cortas que las entradas y llegadas en grupo que aceleran y descansan 0,5 s.
- [ ] 3–5 tipos de transición, cada uno con su causa.
- [ ] Cada sonido tiene causa visible, pico un fotograma después de la imagen, licencia registrada; mezcla entre −16 y −14 LUFS y ≤ −1 dBTP.
- [ ] `check` limpio, `snapshot --review` mirado (hoja de 360 px incluida), `REVIEW.md` escrito y revisión independiente hecha.
