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

**Deriva de cámara continua.** Un empuje casi imperceptible (100 → 103 % a lo largo del plano) solo vuelve a 100 % **en un corte real** (vuelta de un recurso, paso a la demo, empalme del corte). Si se reinicia donde no hay corte, la imagen salta un 3 % y se ve como un corte mal hecho (VID-0002 v06b, «nuevo / calma»). Los acercamientos de énfasis van aparte y siempre con curva.

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

**Bibliotecas:** el **banco de Pixabay de Ale** (AV-011) en `Documents/proyectos/referencias/banco_audios`, con nombres descriptivos. Reserva: **Sonniss #GameAudioGDC** (profesional, uso comercial sin atribución; se descarga de nuevo desde gdc.sonniss.com, la copia local se borró el 2026-11-18). Mixkit y Freesound, rechazados por Ale al oído el 2026-11-17; ZapSplat, alternativa con crédito en la descripción. Shotcraft usa por defecto Freesound y BGM *tech-house*: aquí no se adopta (AV-008 y el rechazo del 2026-11-17).

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

## 8 bis. Probado en VID-0002 v05 (2026-11-18)

Piezas y recetas que ya salieron en un render real, con la marca v2: `text-state-swap` y `icon-swap` (el que sale se desenfoca y baja; el que entra sube y se enfoca), `card-resize` (la tarjeta se ensancha hasta ser la ventana), zoom a través de un objeto, `number-wheel` (el dígito rueda) y texto detrás de la persona. Los detalles y las desviaciones del plan están en `videos/VID-0002/hyperframes/edicion/PLAN_v05.md` §14.

## 9. Lista de comprobación antes de enseñar un corte

- [ ] El fotograma 0 tiene cara o frase; nada se lee fuera de y 168–1330.
- [ ] Todo texto que se lee mide ≥ 56 px (subtítulo) o ≥ 32 px (auxiliar) en el render; nada en un término medio.
- [ ] Ninguna técnica protagoniza dos veces; ≤ 3 golpes de cámara a pantalla completa.
- [ ] Ningún tramo de más de 3 s sin cambio (`dead_stretch`) ni línea sin tiempo de lectura (`line_unread`).
- [ ] Curvas según la función, salidas más cortas que las entradas y llegadas en grupo que aceleran y descansan 0,5 s.
- [ ] 3–5 tipos de transición, cada uno con su causa.
- [ ] Cada sonido tiene causa visible, pico un fotograma después de la imagen, licencia registrada; mezcla entre −16 y −14 LUFS y ≤ −1 dBTP.
- [ ] `check` limpio, `snapshot --review` mirado (hoja de 360 px incluida), `REVIEW.md` escrito y revisión independiente hecha.
- [ ] La cara se ve ≥ 60 % del vídeo; ningún tramo a pantalla completa sin cara de más de 4 s.
- [ ] Cada corte de voz cae en un silencio medido y en final de frase.
- [ ] Ningún subtítulo se sale del ancho ni pisa la interfaz; la banda de subtítulos está libre en todos los modos.
- [ ] En la demo, ningún plano parte un campo o un botón y nada se lee por debajo de 28 px en el render.
- [ ] Hay dos másteres: sin música (para sonidos de tendencia en la app) y con música libre.

## 10. Dirección v2: dinamismo (2026-11-21)

Ale, al comparar con un reel bien editado ([REF-001](../referencias/edicion/REF-001_reel-edits/DESGLOSE.md)): «nuestra edición de textos y motion graphics es bastante plana… necesito una buena dirección de edición». Esta sección es esa dirección. Las piezas que cambian la marca (color de acento, degradados) son una **propuesta (AV-014)** hasta que Ale decida.

### 10.1 Autocrítica: VID-0003 v06 frente a REF-001

| Dimensión | Nosotros (v06) | REF-001 | Regla nueva |
|---|---|---|---|
| Ritmo de cambios | Algo nuevo cada 1–1,7 s fuera de la demo | Igual | Se mantiene |
| Subtítulos | Un solo estilo para todo: mayúsculas, caja navy, palabra activa invertida, misma posición y entrada | Dos niveles: frase pequeña + palabra clave grande en color; a veces otro estilo para una frase | **Tres niveles de texto** (§10.2) |
| Entradas y salidas | Casi todo entra igual (escala 0,78 → 1 + desenfoque) y sale igual (se disuelve). Es lo que §4 prohíbe: «todo entra con fundido y subida» | Cada elemento entra desde un sitio y se va a otro; letras, barridos, golpes | **Vocabulario con nombre** y nunca dos iguales seguidos (§10.3) |
| Color | Monocromo (navy y blanco roto): las claves no resaltan | Un acento cálido para las claves y el degradado de cada marca en su nombre | **Acento + color del producto** (AV-014, §10.4) |
| Profundidad | Todo encima de la imagen | Palabras gigantes detrás de la persona | **Palabra escenario** detrás (matte) |
| Iconos | Dibujados por nosotros (teléfono con «/», hoja de calendario) | Iconos reales en baldosa con brillo y etiqueta | **Icono real del producto** (Plan B: `/brand/plan-b/icon.png` de la app) |
| Tarjetas | Píldoras de cristal con texto | Tarjetas que hacen algo: gráfica, interruptores, terminal, caja de comentario | **Tarjetas vivas** (§10.5) |
| CTA | Texto «El link está en mi perfil» | Componente de interfaz (píldora + caja de comentario) | El CTA es un componente |
| Lo que ya está bien | Demo con la app real, el celular que nace del teléfono flotante, «Plan B» que sale de las manos, picos con silencio y golpe | — | Se mantiene |

### 10.2 Tres niveles de texto

| Nivel | Qué es | Estilo | Cuándo |
|---|---|---|---|
| 1 · Frase | Lo que dice la voz, palabra a palabra | Plus Jakarta Sans Bold 46–52 px, minúsculas (como se habla), blanco roto con borde suave; sin caja salvo sobre fondos difíciles. Entra palabra a palabra (subida de 8 px y enfoque, 60–90 ms entre palabras) | Siempre, a y ≈ 1150–1250 |
| 2 · Clave | Una palabra por frase, la que carga el sentido | ExtraBold 96–130 px, color de acento (o el del producto si nombra el producto), **debajo** de la frase. Su entrada depende de lo que significa (§10.3) | Una por frase, como mucho |
| 3 · Escenario | Una palabra que titula el bloque | ExtraBold 260–360 px, mayúsculas, detrás de la persona (matte), acento o blanco al 40–60 %. Entra deslizándose con desenfoque, se queda 2–4 s mientras siguen las frases y sale desenfocándose cuando cambia la idea | 3–5 por vídeo, nunca en la demo |

Las palabras protagonistas de ahora («HICE UNA APP», «¿Y TÚ?») pasan a ser **claves con golpe** o **escenarios**; el resplandor (AV-013) solo si Ale lo aprueba.

### 10.3 Vocabulario de entradas y salidas

Cada elemento tiene una entrada y una salida con nombre. **Nunca el mismo par dos veces seguidas**, al menos 5 tipos distintos por vídeo, y la salida va en la dirección que pide el siguiente elemento (o lo empuja).

| Nombre | Entrada | Salida | Para qué |
|---|---|---|---|
| Subida | 20–40 px desde abajo + enfoque 10 → 0 px, `expo.out` 0,35 s | Sube y se desenfoca, `power3.in` 0,2 s | Frase (nivel 1) |
| Barrido | Máscara de izquierda a derecha, 0,3–0,45 s | Barrido hacia el otro lado | Revelar: un resultado, una lista |
| Golpe | Escala 1,6 → 1 con rebote corto (0,22 s) + sacudida de 6–9 px | Corte seco o empujón | Palabras fuertes y picos (≤ 3 por vídeo) |
| Máquina | Letra a letra con cursor (1 letra / fotograma) | Se borra hacia atrás o se desenfoca | Verbos de acción («escribes», «automatiza») |
| Letras | Cada letra sube desde abajo con 1 fotograma de desfase | Bajan en orden inverso | Nombres (Plan B, MiniApp 01) |
| Deslizar | Entra desde el lado con desenfoque de movimiento (12 px horizontal), 0,3 s | Sale por el lado contrario | Palabra escenario; pasado ← izquierda, futuro → derecha |
| Rodar | Una palabra rueda a la siguiente en su hueco (máscara vertical) | — | Cambios: «$ → GRATIS», «enero → febrero» |
| Nacer del gesto | Sale del punto donde la mano se abre o señala | Se desenfoca | Cuando Ale hace un gesto |
| Pop de icono | Escala 0 → 1,12 → 1 con desenfoque, 0,4 s; los grupos con 60–80 ms de desfase | Encoge a 0,8 y cae 20 px | Iconos y baldosas |
| Empujar | El elemento nuevo entra y desplaza al anterior | — | Encadenar ideas sin vacío |

Curvas y tiempos: los de §4 (llegadas más lentas que salidas, rebote solo en posición y escala).

### 10.4 Color: paleta de cerobytes con degradados (AV-014, aprobada: «Señal»)

Ale, 2026-11-21: no mezclar colores de MiMiniApp con los de cerobytes; **actualizar la paleta de cerobytes con degradados**. Los colores de un producto (violeta y lima de Plan B) siguen **solo dentro del celular**.

Reglas de la propuesta: la base no cambia (marino `#0D213F`, negro `#0B0B0D`, carbón `#1E2937`, blanco roto `#F5F6F8`); los degradados van a **119°**, la dirección perpendicular a la barra «/» (29° de la vertical); nada del degradado violeta-azul ni de los colores descartados en AV-006 (`#54E0EA`, `#AD8BFF`, `#D9F77A`); y en vídeo el texto en degradado lleva una sombra oscura suave para leerse sobre la imagen. Opciones (tablero: `videos/VID-0003/hyperframes/paleta_v21/`):

| Opción | Degradado | Carácter |
|---|---|---|
| 1 · Acero | `#FFFFFF` → `#C9D4E6` → `#7F9CC9` | Frío, extiende el marino; elegante y discreto |
| 2 · Ignición | `#FFE08A` → `#FF9F43` → `#FF5E3A` | Cálido, complementario del marino: es el que más resalta sobre la camiseta y la pared |
| 3 · Señal ✅ **elegida por Ale** (2026-11-21) | `#F5F6F8` → `#7DB4FF` → `#2E6BFF` | Azul eléctrico sin violeta. Sobre ropa oscura necesita la sombra sutil |
| 4 · Ignición + Acero | Claves en Ignición; palabras escenario, bordes de tarjetas y la barra en Acero | Un acento cálido para lo que importa y una estructura fría que es la marca de siempre |

### 10.5 Iconos, tarjetas vivas, profundidad y transiciones

- **Iconos reales:** baldosa de 140–160 px, radio 34, el icono del producto (Plan B, de la propia app) o el de la herramienta que se nombra, con una etiqueta en píldora debajo. Enmarcan la cara (izquierda / derecha, a la altura de los ojos) y se conectan con un arco y un punto que viaja (máx. 3 arcos por vídeo).
- **Tarjetas vivas:** cada tarjeta hace algo mientras está: una notificación que llega, una línea que se dibuja, un interruptor que se enciende, una lista que se marca con ✓, un precio que rueda, una caja de comentario que se escribe. Una tarjeta solo con texto se cambia por un subtítulo de nivel 2.
- **Escena de proceso:** cuando el guion cuenta un proceso que no es la demo, una interfaz inventada lo enseña paso a paso (interruptores, progreso, terminal). Nunca se presenta como si fuera la app real (CONTENIDO: nada inventado).
- **Profundidad:** la palabra escenario va detrás de la persona con el matte de `npx hyperframes@0.9.42 remove-background` (ya probado en VID-0002 v05).
- **CTA como componente:** píldora con la acción y una caja que se escribe sola («Comenta PLAN B»), en lugar de una frase suelta.
- **Transiciones:** además de §5, empujar (el nuevo desplaza al viejo), del objeto al mundo y corte en el gesto; cada palabra escenario cambia con la idea, no con la frase.

### 10.6 Piezas del catálogo de HyperFrames para empezar

Se instalan con `npx hyperframes@0.9.42 add <nombre>` y se adaptan a la marca (fuente, colores, tiempos): `caption-editorial-emphasis` (dos niveles de texto), `mk-emphasis-type` y `caption-parallax-layers` (palabra detrás de la persona), `typewriter`, `text-stagger`, `text-state-swap` y `kinetic-type-swap` (rodar), `caption-kinetic-slam` (direcciones alternas), `badge-pop` e `icon-swap` (iconos), `macos-notification` y `notification-pileup` (tarjeta que llega), `mk-line-graph` (línea que se dibuja), `settings-toggle-flow` y `toggle-flip` (interruptores), `physical-exit` (salidas con inercia), `arc-motion-path` (algo que viaja por un arco).

### 10.7 Autocrítica constante

En cada edición, además de la revisión de la skill (`.claude/skills/edicion/revision.md`):

1. **Antes de editar:** elegir 1–2 referencias de `referencias/edicion/` y apuntar en el plan qué técnicas se toman de cada una (préstamos).
2. **Tras el primer render:** hoja de contacto lado a lado con la referencia (`snapshot --against <referencia>` si hay vídeo, o capturas) y la **auditoría de dinamismo**, 0–2 puntos cada fila:

| Criterio | 2 puntos |
|---|---|
| Jerarquía | Cada frase tiene clave (nivel 2); 3–5 palabras escenario |
| Variedad | ≥ 5 tipos de entrada; ningún par entrada/salida repetido dos veces seguidas |
| Salidas | ≥ 80 % de los elementos salen con dirección (no solo fundido) |
| Color | Claves y escenarios con la Señal (AV-014), todo texto con la sombra sutil; ningún color de producto fuera del celular |
| Profundidad | Al menos una palabra escenario detrás de la persona |
| Tarjetas vivas | ≥ 2 tarjetas que hacen algo; ninguna tarjeta solo con texto |
| Iconos | El producto aparece con su icono real al nombrarlo |
| Huecos | Fuera de la demo, nunca más de 1,5 s sin un cambio gráfico |
| Gestos | Cada gesto claro de Ale tiene su gráfico (nacer del gesto, señalar) |
| CTA | El CTA es un componente animado |

Se entrega con ≥ 16 de 20 o se dice qué falta y por qué.
3. **Cada corrección de Ale** va a `errores.md` de la skill y, si es una técnica nueva, a este vocabulario.
4. **Cada mes**, dos técnicas nuevas sacadas de referencias nuevas.

### 10.8 Muestrario (2026-11-21)

Los primeros 12,95 s de VID-0003 rehechos con este lenguaje, para decidir viéndolo: `videos/VID-0003/hyperframes/muestrario_v2/` (composición) y `media/trabajo/muestrario_v2.mp4` (con el sonido de la edición v06, que no se rediseñó). Lo que enseña:

| t (s) | Técnica |
|---|---|
| 0,3 | Promesa con Barrido; «gratis» en caja ámbar |
| 0,16–9,9 | Frases en minúsculas palabra a palabra (Subida), por encima de la estampa de la camiseta |
| 1,70 | Clave «METAS» en ámbar con Letras; sale cayendo |
| 2,18 | Escenario «ENERO» detrás de la cabeza (matte), Deslizar desde la izquierda; sale por la izquierda en «pero» |
| 4,34 | Clave «APP» en caja violeta (producto) con Golpe y sacudida; entra el icono real de Plan B con Pop |
| 5,83 | Clave «GANAS» con Máquina sobre el recurso; se borra hacia atrás |
| 7,03 | Clave «PLANEO» con Barrido; sale barriéndose |
| 9,14 | Logo con Deslizar y arco con un punto lima hasta el icono |
| 9,92 | «Plan B» nace de las manos (de la base), con la «B» en lima |
| 10,62 | Píldora violeta «MINIAPP 01» con Letras |
| 11,42 | Tarjeta viva «PRECIO»: «$» rueda a «GRATIS» |
| 12,62 | El icono crece hacia la cámara: entrada a la demo |

⚠ El color del muestrario (violeta y lima de Plan B, ámbar) quedó **descartado por Ale** (2026-11-21): mezclaba MiMiniApp con cerobytes. Ver §10.4 y el laboratorio (§10.9).

**Auditoría de dinamismo (§10.7)** sobre lo que cabe en 13 s: jerarquía 1 (4 claves en 12 frases; 1 escenario) · variedad 2 · salidas 2 · color 2 (con la propuesta AV-014) · profundidad 2 · tarjetas vivas 1 (solo el precio) · icono 2 · huecos 2 · gestos 1 · CTA sin evaluar (no está en el tramo): **15 de 18**. Para una edición completa faltaría: una clave en casi cada frase, 3–5 escenarios, una segunda tarjeta viva (el recordatorio de las 20:00 o el plan que se escribe) y el CTA como componente.

### 10.9 Laboratorio de texto (2026-11-21)

Ale sobre el muestrario: «quedó mejor, pero no son tan wow como el ejemplo». Diez tratamientos de texto más potentes, cada uno con su letra para elegir, sobre tres tramos de VID-0003: `videos/VID-0003/hyperframes/lab_texto/` y `media/trabajo/lab_texto.mp4` (13,7 s, con el sonido de la v06). Color: opción 4 de §10.4.

| Letra | Tratamiento | Cómo | Dónde |
|---|---|---|---|
| A | Cascada 3D | Cada letra gira desde abajo (`rotateX` −100° → 0, perspectiva 700) con 1 fotograma de desfase y rebote corto; sale girando hacia delante | «TODOS LOS AÑOS» |
| B | Impacto + brillo | Entra al 260 % y desenfocada y cae a su tamaño en 0,2 s con golpe de cámara; un brillo cruza a 29°; sale estirándose hacia arriba | «METAS» |
| C | Letras que se juntan, detrás | Palabra escenario detrás de la persona: interletraje 0,9 em → −0,04 em con desenfoque; sale dispersándose desde el centro | «ENERO» |
| D | Máscara con estela + barrido diagonal | Las palabras suben desde una línea con estela; «APP» entra con un barrido a 29° en una caja degradada | «hice una APP» |
| E | Corte en dos + barra | Mitad de arriba por la izquierda, mitad de abajo por la derecha; al encajar cruza la barra «/»; salen separándose | «POR ESO HICE» |
| F | Nace de las manos + brillo | La técnica de la base, en degradado, con un brillo cuando llega la «B» | «Plan B» |
| G | Trazo que se rellena | El contorno se dibuja y el degradado entra con un barrido a 29°; golpe leve al asentarse | «GRATIS» |
| H | La barra «/» que corta | La palabra cae, la barra de la marca la atraviesa y las dos mitades se separan | «ENERO» (antes de «¿Y tú?») |
| I | Golpe con eco | Cae de 1,8 a 1 con sacudida y tres contornos se expanden hacia fuera | «¿Y TÚ?» |
| J | CTA como componente | Tarjeta con borde degradado que sube; el botón se pulsa en «perfil» | «El link está en mi perfil» |

**Ale, 2026-11-21:** «este nuevo ejemplo está bastante bien», con la paleta Señal y una sombra sutil en todas las letras (`media/trabajo/lab_texto_senal.mp4`). Tokens y sombra en [IDENTIDAD](../marca/IDENTIDAD.md).

Lo que se elija pasa a la base (`hyperframes/edicion/`) como funciones reutilizables, con su entrada y su salida, y a `referencia.md` de la skill.

### 10.10 Aplicado en VID-0003 v07 (2026-11-21)

Ale: «Sí, edítalo». La base `videos/VID-0003/hyperframes/edicion/` pasa a la dirección v2 (es la base de `/edicion`): frases en minúsculas, claves en Señal, escenarios «ENERO» y «ESTE AÑO» detrás de la persona, los tratamientos A–J, Máquina y Barrido, sombra sutil en todo texto y los efectos de sonido rehechos para que cada uno tenga algo que se ve. Sale el recurso R01 («ENERO» detrás de la cabeza cuenta lo mismo) y la hoja de calendario del cierre (la cuenta la barra que corta «ENERO»). Entrega: `media/trabajo/edicion_v07.mp4`.
