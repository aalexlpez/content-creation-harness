# Dirección de edición

Cómo se decide el montaje desde el guion: texto en pantalla, música y efectos, color, movimiento y portada. Los valores concretos son **candidatos de prueba**. La identidad v2 (AV-006) está aprobada «por ahora»; la firma sonora sigue pendiente ([IDENTIDAD](../marca/IDENTIDAD.md)).

## Qué entrega Claude con cada guion

Una **propuesta principal** que se pueda seguir en CapCut. Una variante solo si cambia una decisión importante (por ejemplo, música o voz sola). Los tiempos son aproximados hasta tener material.

| Dónde | Qué queda escrito |
|---|---|
| GUION → Brief | Ritmo, música o silencio, jerarquía de texto, color y perfil visual |
| GUION → Escenas | Tiempo y palabra o acción que dispara el cambio, plano o corte, texto exacto, estilo, posición, duración, sonido y toma |
| PRODUCCION → Montaje | Lo que se hizo de verdad: tomas, tiempos, recursos, mezcla, valores de color y cambios frente al guion |
| CIERRE → QC | Revisión del MP4 final en el móvil y derechos de cada recurso |

## Principios

- **La demo manda.** Que se vea la interfaz y se entienda la voz es más importante que cualquier efecto.
- **Un foco por plano.** Un acento de color o de movimiento por plano, como mucho dos.
- **Cada efecto tiene una función:** orientar, señalar un cambio o confirmar un resultado. Si no la tiene, fuera.
- **Corte directo** cuando el cambio de plano ya cuenta la idea.
- **Nada tapa** la cara, los controles de la demo ni la interfaz de la red (márgenes superior e inferior y columna derecha de botones). Compruébalo en el móvil.

## Texto en pantalla

| Nivel | Uso | Pauta v2 |
|---|---|---|
| Subtítulo | Transcribe la voz | Plus Jakarta Sans Bold, mayúsculas, una línea y posición estable. La palabra que suena se invierte (caja blanco roto con texto negro). Revisa eñes, tildes y cifras en el celular |
| Rótulo | Añade información: nombre, paso, cifra | Plus Jakarta Sans Bold sobre un bloque azul marino con el símbolo «/». Dirige la mirada a la demo |
| Acento | Gancho, resultado o remate | Una frase corta; la palabra clave en Plus Jakarta Sans ExtraBold dentro de una caja blanco roto. Separado de subtítulos, cara e interfaz |

La identidad v2 no tiene color de acento: el énfasis se logra por inversión de contraste, peso o tamaño. Colores, símbolo y kit: [IDENTIDAD](../marca/IDENTIDAD.md). La tipografía es Plus Jakarta Sans (AV-007, licencia OFL): los archivos están en `marca/fuentes/plus-jakarta-sans/`. Anota en Derechos la fuente y de dónde salió el archivo. En CapCut hay que instalarla en el sistema y comprobar que la reconoce.

## Música y efectos

- Por defecto, **cama instrumental discreta o voz sola**, según la pieza. Indica cuándo entra, dónde baja bajo la voz y cuándo se funde.
- **Efectos sonoros** solo en acciones concretas: tocar, aparecer o confirmar un resultado, o cambiar de sección. Nunca de relleno.
- **Sonidos reales, nunca sintetizados por código** (AV-008): grabados por Ale con el DJI (papel, toque, golpe seco) o de bibliotecas con licencia CC0 (por ejemplo, Freesound), siempre escuchados antes de usarlos y con su fila en Derechos. Las animaciones se entregan sin audio y el sonido va en su propia pista.
- **Bibliotecas:** primero las profesionales gratuitas con licencia comercial sin atribución (Mixkit, Pixabay Sound Effects; la licencia se comprueba en la página al descargar). Freesound solo para algo concreto y escuchado entero: los micro-sonidos de interfaz sueltos sonaron «horribles» en el ensayo del 2026-11-17. Un mismo «pop» para todo lo que aparece da coherencia; no todo evento necesita sonido.
- Silencio intencional es una opción válida.
- **Derechos por destino:** que una pista esté en el catálogo de CapCut o TikTok no significa que se pueda usar en YouTube o Instagram. Registra cada pista y efecto en CIERRE → Derechos con su licencia y las redes que cubre.

### Música: cómo elegirla y sincronizarla

**De dónde (sin derechos de terceros):**
- **Pixabay Music** (Pixabay Content License, uso comercial sin atribución; el banco de Ale, AV-011). En la página de cada pista hay que mirar si el autor la registró en Content ID: si lo dice, YouTube puede reclamarla aunque la licencia lo permita. Se prefieren las que no lo dicen, y se guarda el enlace en CIERRE → Derechos.
- **Lo que no se usa:** canciones comerciales mezcladas en el archivo (solo dentro de la app de cada red, AV-012); la biblioteca de CapCut o TikTok fuera de su red; pistas «libres» de YouTube sin leer sus condiciones para otras redes.

**Qué buscar** (el brief de música va en el guion):

| Tramo del vídeo | Energía | Qué pedir a la pista |
|---|---|---|
| Gancho | Tensión baja | Intro mínima (un pulso, sin batería completa) o silencio |
| Problema | Pulso | Batería suave que empieza |
| Solución y demo | Subida y groove | La parte principal de la pista, con ritmo claro |
| Resultado | Pico | Un «drop» o subida que cae en el momento del resultado |
| Cierre | Corte | La música se corta 0,3–0,5 s antes de la frase final y vuelve, o acaba, con el golpe |

- **Tempo:** 90–115 BPM para vídeos hablados; más rápido tapa la voz.
- **Estructura:** pistas con partes claras (intro, subida, caída) de 1–3 min. Un bucle de 30 s no se puede editar por tramos.
- **Búsquedas en Pixabay** (filtrar por Música, duración 1–3 min): «upbeat tech», «modern vlog beat», «motivational beat», «minimal electronic», «future bass uplifting», «lofi hip hop upbeat». Se escuchan 4–6 candidatas **montadas en el vídeo**, nunca sueltas.

**Sincronía con el montaje:**
1. `npx hyperframes@0.9.42 beats <pista>` marca los tiempos de cada golpe de la música.
2. Se elige el **inicio de la pista** para que un tiempo fuerte caiga en el cambio más importante (por ejemplo, la entrada de la demo).
3. Se **editan compases** (quitar o repetir 1–2 compases) en los cambios de tramo, tapados por una transición, para que el pico caiga en el resultado.
4. Las transiciones y los elementos que aparecen se mueven al tiempo fuerte más cercano (±0,12 s como máximo). **La voz no se mueve:** las palabras clave siguen mandando.
5. Como mucho 3–4 puntos de sincronía claros por vídeo; más se nota mecánico.

## Planos de recurso (B-roll)

> **El vídeo empieza con la primera palabra.** Nada de apertura en frío sin voz ni texto (una imagen del resultado con música antes de hablar): Ale la probó en VID-0002 v06 y no se entendía («no hay contexto»). Si se quiere enseñar el resultado al principio, va **debajo de la voz**, como recurso de la primera frase. En una serie con la cara del creador, el primer plano es **la cara hablando**; si la primera frase lleva recurso, va como tarjeta pequeña en el pecho (sin tapar la boca), no a pantalla completa (VID-0002 v06d).

Un plano de recurso es 1–3 s de imagen real que ilustra lo que se dice mientras la voz sigue. Es lo que más hace que un vídeo parezca editado por un profesional.

- **Cuándo:** en frases que describen una situación (el problema, lo que pasa «ese día», el resultado en un celular real). Nunca en la frase que presenta al creador ni en la llamada a la acción.
- **Cuántos y cuánto:** 3–6 por vídeo. Un recurso que **cuenta** algo dura **≈ 1,6–2 s** (4–5 golpes de la música) y cubre la frase entera que ilustra: con 1,2 s no da tiempo a relacionar imagen y frase (Ale, VID-0002 v06, 2026-11-19). Solo una **lista** («productividad, ciencia, minijuegos») va más rápida, ≈ 1,2 s por elemento. Hasta 3 s si es la app real. La cara vuelve al terminar la frase o justo antes (corte en J/L).
- **Horizontales en 1080:** no se amplían a 9:16 (quedan borrosos): van como tarjeta cuadrada sobre su propia imagen desenfocada.
- **Primero propios:** objetos, manos, el celular y la pantalla real de la app se graban en la misma sesión (lista «Recursos que grabar» del guion, `/rodaje`). Se ven más auténticos y no tienen licencia que revisar.
- **Stock solo si no se puede grabar.** Pexels (Pexels License), Pixabay Videos (Pixabay Content License) o Mixkit (Mixkit Stock Video Free License): uso comercial sin atribución, según sus páginas; la licencia se comprueba al descargar y se apunta en Derechos. Mejor planos **sin caras reconocibles** (manos, objetos, espacios): las licencias no permiten dar a entender que una persona respalda algo.
- **Tratamiento:** mismo grado de color que la toma de cámara, recortado a 9:16 sin deformar y, si hace falta, un empuje lento (100 → 106 %).

## Demo de la app real

Cuando la miniapp existe (aunque sea en staging), la demo se graba de la app de verdad, no de una maqueta (VID-0002 v06e, 2026-11-19).

- **Cómo:** `videos/VID-0002/hyperframes/v06/demo/grabar.mjs`. Usa el `puppeteer-core` y el Chrome que ya trae `npx hyperframes@0.9.42` (no se instala nada). Simula un iPhone de 393×852 pt a 1080×2342 px y graba **fotograma a fotograma**, ralentizando las animaciones de la app para que en el vídeo vayan a su velocidad real.
- **Al ritmo de la voz:** cada toque y cada tecleo van en `ACCIONES`, en el tiempo del corte (tn), para que la app haga cada cosa cuando la voz la dice. No hay que acelerar ni cortar la grabación.
- **Lo que se aprendió:** con `setViewport(deviceScaleFactor)` chrome-headless-shell captura a 393 px: la escala se fuerza al lanzar Chrome (`--force-device-scale-factor`). El tiempo virtual de CDP cuelga Chrome al cambiar de paso. Los toques se hacen desde la página (`click()` y el setter nativo con evento «input»), con un toque real al principio para que no salgan recuadros de foco. El `scrollIntoView` de la app se anula y los desplazamientos los hace la grabación.
- **Fecha:** si la app cambia según el mes («1 de febrero»), se fija la fecha en la que se publicará el vídeo, sin parar el reloj. Se anota en el plan: es lo que la app hace de verdad ese mes.
- **Nada sale del navegador:** no se pulsan Google Calendar, descargar ni compartir.
- **En el vídeo:** dentro de un celular de proporción real (19,5:9), con encuadres que siguen la voz (dos o tres a todo el ancho) y un sonido de toque por cada toque real. Sin dedos ni anillos simulados.

## Color

> **Aviso (2026-11-20, VID-0003):** en el set con la luz nueva Ale vio el look B demasiado notorio (pared violeta, piel naranja, negros aplastados, piel suavizada). VID-0003 usa un color «natural» (`videos/VID-0003/hyperframes/edicion/preparar.py`: `LOOK` y `PIEL`): curva muy suave, piel un poco más cálida, pared menos violeta y limpieza de ruido en vez de suavizar la piel. **Regla:** el color se mide en la toma (pared, piel, negros) y se corrige hacia lo natural; el look de la serie es un punto de partida, no un filtro fijo. Después Ale pidió **quitar el filtro** del todo (v03): la versión vigente de VID-0003 va con el color de la cámara, sin corrección ni viñeta. Con la luz del set bien puesta, la toma ya no necesita look.
>
> **Look de la serie (2026-11-19, VID-0002 v06f):** look B «cálido cinematográfico», elegido por Ale entre tres. Receta en `videos/VID-0002/hyperframes/v06/preparar.py` (`LOOK_B` y `PIEL`): se aplica con ffmpeg al corte antes de componer (no con filtros CSS), con suavizado de piel que respeta bordes solo en la toma de cámara y la misma curva y temperatura en los recursos.

El color se aplica a la **toma de cámara**. La captura de pantalla conserva su color original. Orden: exposición y balance de blancos primero, después contraste y saturación. Revisa la piel, los blancos y las luces del set comparando el mismo fotograma con el original. Si el original es HDR, primero conviértelo a SDR ([TECNICA](TECNICA.md)).

Rangos de partida tomados de capturas de referencia de los ajustes manuales de CapCut (escala por confirmar en tu versión; «≈» = valor parcialmente tapado en la captura):

| Referencia | Exposición | Contraste | Saturación | Temperatura | Sombras | Altas luces |
|---|---:|---:|---:|---:|---:|---:|
| Interiores claros | 0 a +10 | +10 a +20 | +10 a +15 | 0 a +10 | +5 a +10 | +5 a ≈+10 |
| Estudio frío | 0 a +5 | +15 a +20 | +10 a +15 | +15 a +25 | +5 a +10 | +5 |
| Estudio cálido | 0 a +5 | +15 a +20 | +10 a +15 | −10 a −15 | 0 a −5 | −5 a ≈−10 |

Las capturas se etiquetaban «Frío» y «Cálido» al revés de lo que sugiere el signo de la temperatura: comprueba el efecto real en la toma. Registra el editor, su versión y los valores aplicados en PRODUCCION → Montaje. Ayuda de CapCut: [corrección de color](https://www.capcut.com/es-es/tools/video-color-correction).

## Movimiento e interfaz

Decisión vigente (AV-002): interfaz cinematográfica por capas en vez de una grabación de pantalla plana, **cuando aporte**. Las animaciones se hacen nuevas para cada vídeo; lo que se reutiliza es el estilo y el flujo de trabajo (AV-003). Motivo de la identidad v2: la barra diagonal «/», con barridos inclinados ≈ 29° respecto a la vertical, superficies planas y sin degradados ni resplandores.

Patrones de referencia:

| Código | Patrón |
|---|---|
| F-01 | Cámara del creador + un rótulo verificable + corte motivado |
| U-01 | Móvil → tarjeta en foco → transformación a detalle → interacción → resultado |
| T-01 | Frase clave animada y sincronizada con una palabra de la voz |
| C-01 | Terminal real con zoom y resaltado. Nunca código falso |
| Q-01 | Pregunta concreta, tres opciones visuales como máximo y CTA claro |
| E-01 | Edición continua: el video alterna «a cámara» y «escenario» (gráfico arriba, cámara abajo) y la capa gráfica cambia con cada frase. Ver [Edición continua](#edición-continua) |

Técnicas que se pueden pedir por escena: tipografía cinética sincronizada, transformación de un mismo elemento (*shared element*), aparición escalonada de campos, cámara virtual o parallax, microinteracción de toque, máscara para revelar el resultado, sonido ligado al evento, corte J/L con la voz y transiciones con sentido. Cada una debe poder comprobarse en tres fotogramas: antes, durante y después.

## Edición continua

Propuesta AV-009, probada en el ensayo de edición del 2026-11-17 (`videos/VID-0001/hyperframes/ensayo-edicion/`). Nace de estudiar la técnica del creador Erik Taveras ([referencias/MOTION.md](../referencias/MOTION.md)); se copia el método, no su estilo.

**El error que corrige:** planificar unas pocas piezas sueltas (una hoja, un rótulo, una maqueta) alrededor de la cara. Se ven pequeñas, compiten con el encuadre y dejan largos tramos sin nada. El nivel profesional sale de una **capa gráfica continua**, sencilla pero constante, ligada a lo que se dice.

| Regla | Cómo se aplica |
|---|---|
| Dos modos | **A cámara** (la toma tal cual) y **escenario**: panel `#0D213F` en la mitad de arriba (y 0–1000) con el gráfico, y la toma desplazada 700 px hacia abajo para que la cara quede en la mitad inferior. Se pasa de uno a otro en 0,5 s |
| Un evento por frase | Cada sustantivo o idea con peso dispara algo: un icono, un nodo, un tachado, un interruptor. Un cambio cada 0,5–1,5 s en el escenario. Se saca de los tiempos por palabra del corte |
| Ilustrar la idea, no la interfaz | Diagramas que crecen frase a frase (propósito → febrero → obstáculo → plan). La interfaz real, solo como prueba breve |
| Composición fija | Cabecera a la izquierda (título del tramo) y «/ PLAN B · MINIAPP 01» a la derecha, a y ≈ 272 px. Orienta y hace serie |
| Subtítulos propios en el escenario | Plus Jakarta Sans ExtraBold en mayúsculas, a y ≈ 868 px, la palabra que suena invertida. Ningún grupo de subtítulo menos de 0,4 s en pantalla |
| Cambio de tramo | El escenario no sube y baja entre tramos seguidos: la barra «/» cruza en diagonal y el contenido cambia detrás de ella, como una cortina |
| Tramos a cámara | Se usan para respirar y para lo que no conviene ilustrar (por ejemplo, un castigo que la ficha del producto evita). Pueden llevar elementos ligeros junto a la cara |
| Sistema pequeño | Marca v2 sin color de acento, iconos lineales en blanco roto, la barra como conector, notas pequeñas en mayúsculas con tracking para la fuente de un dato |
| Cara siempre | La cara se ve en todo el vídeo (≥ 60 % del tiempo a pantalla, entera o abajo en el escenario). La pantalla completa sin cara es una excepción de ≤ 4 s. Presupuesto por tramo en el `PLAN.md` antes de animar: escenario ≤ 6 s seguidos con el mismo gráfico quieto |
| La demo, en una ventana | La interfaz va en una ventana del escenario (y 330–850) con la cara abajo. La cámara trabaja por **planos de grupo de interfaz** (pregunta y campo, tarjetas, campos del plan, resultado…), medidos sobre la maqueta, con acercamientos y alejamientos de 0,5–0,6 s y zoom ≤ 0,9. Ningún plano parte un campo o un botón. La ventana cambia de ancho con el zoom para que no queden franjas |
| Banda de subtítulos | Fija en cada modo (y ≈ 862 en el escenario, y ≈ 1190 a cámara) y nunca ocupada por gráficos ni interfaz. Si un grupo no cabe en 980 px, se encoge (estimación por caracteres, sin medir el DOM) |
| Cortes de voz | Solo en un **silencio medido** (< −60 dB en ventanas de 10 ms) y en final de frase. Nunca a mitad de una frase que sigue, aunque la transcripción diga que ahí acaba una palabra: sus tiempos fallan. Script de referencia: `videos/VID-0002/hyperframes/edicion/cortes.py` |
| Una idea, 40–55 s | La duración se decide en el guion. Las digresiones se quedan en una frase con un gráfico o van a otro vídeo |

**Estándar:** cada evento de la capa sigue [MOTION](MOTION.md) (tamaños, curvas, transiciones, sonido, recetas de video-shotcraft y del catálogo de HyperFrames, y la revisión).

**Orden de trabajo:** primero el corte (en silencios medidos), después la capa. Antes de enseñar el corte, una revisión con la hoja de 1 fotograma por segundo y el formato de `REVIEW.md` (no después de entregar). Los tiempos por palabra de la versión cortada son la base; con el bruto solo se puede planificar. Es el flujo que salió bien en VID-0002 el 2026-11-17 («ha quedado muchísimo mejor»). El ejemplo completo está en `videos/VID-0002/hyperframes/edicion/` (`PLAN.md`, `index.html`, `mezcla.py`).

| paso | quién | qué | sale |
|---|---|---|---|
| 1 | Ale | Corta y limpia el bruto en CapCut: toma por frase y silencios fuera. Exporta solo **Video**, sin marcar la casilla Audio (que crea un `.aac` aparte), H.264, mp4 y 30 fps, sin música ni subtítulos, **en 4K si CapCut lo permite** (si no, 1080P y Ale deja el bruto 4K en `media/originales/`: Claude reconstruye el corte en 4K alineando el audio de cada tramo con el bruto) | `media/originales/<nombre>.mp4` |
| 2 | Claude | Ingesta: `inspeccionar --perfil ingesta`, `medios`, revisar marca de agua y subtítulos en tres fotogramas. Copia de trabajo H.264 con un fotograma clave por segundo y audio a WAV 48 kHz | `hyperframes/<pieza>/assets/corte.mp4`, `media/trabajo/corte.wav` |
| 3 | Claude | Tiempos por palabra con Parakeet **frase a frase**, cortando en las pausas, y texto corregido a mano ([TECNICA](TECNICA.md#cómo-se-trabaja-aprendido-el-2026-11-17)) | `media/trabajo/corte_palabras.json` |
| 4 | Claude | Si lo dicho no coincide con el guion: voz literal y claims nuevos en el GUION y subida de `Version` (el OK-2 se pide sobre lo grabado) | `GUION.md` vN |
| 5 | Claude → Ale | **Lista de eventos**: tiempo, palabra, modo (C, E o P), evento, receta de [MOTION §8](MOTION.md#8-mapa-de-recetas-para-la-serie-de-miniapps) y sonido del banco. Ale la aprueba antes de animar | `PLAN.md` §3 |
| 6 | Claude | Composición: un solo `index.html` con `render(t)`. Las maquetas ya hechas se re-anclan con un mapa de tiempos (`WARP`) y entran como video a pantalla completa | `index.html` |
| 7 | Claude | `check`, capturas en ~30 instantes y revisión P0/P1 ([MOTION §7](MOTION.md#7-proceso-de-una-capa-de-motion)); se corrige y se vuelve a capturar | `media/trabajo/capturas*/` |
| 8 | Claude | Render sin sonido añadido | `media/trabajo/edicion_vNN_sin_sfx.mp4` |
| 9 | Claude | Mezcla con `mezcla.py`: tabla de efectos (evento, archivo, recorte, pico objetivo, nota), pico 1 fotograma después del evento, música en todo el vídeo 18 dB bajo la voz, −14 LUFS | `media/trabajo/edicion_vNN.mp4` + `_mezcla.json` |
| 10 | Ale | Lo ve y lo escucha entero en el celular; una ronda de correcciones | PRODUCCION → Correcciones |

**Lo que funcionó en VID-0002 (2026-11-17):**
- **Modos:** tres (cámara, escenario y pantalla completa), con la maqueta a pantalla completa para que se lea.
- **Subtítulos:**
  - un solo bloque que se desliza entre y 862 (escenario) e y 1190 (cámara), en vez de dos bloques que parpadean al cambiar de modo;
  - sobre interfaz clara, cada palabra va en caja marina.
- **Ritmo:**
  - un evento por idea con peso (unos 45 en 63 s);
  - tres golpes fuertes por vídeo, como máximo;
  - pops, clics y lápiz alternados y con volumen en escalera.
- **Banco de sonidos:** el que armó Ale en Pixabay (AV-011), con cada efecto recortado a su tramo audible.

### Textos, cortes y transiciones que subieron el nivel (v05 de VID-0002, 2026-11-18)

| Qué | Regla probada |
|---|---|
| Tres niveles de texto | Subtítulo base (66 px), **palabra protagonista** (60–90 % del ancho, máximo 7 por vídeo, una por idea) y cabecera con contador «n / total». En VID-0002 salieron 6 |
| Texto detrás de la persona | Solo en 1–2 palabras de ≈ 1,5 s a cámara (`remove-background`, [TECNICA](TECNICA.md)). El texto queda entre la toma y el recorte, y al menos un tercio de la palabra debe verse |
| Empalmes de voz | Cada empalme de `KEEP` lleva un cambio de encuadre (100 % ↔ 110 %, instantáneo) y un oscurecido del 40 % durante 3 fotogramas justo antes. El salto se lee como intencional |
| Transiciones con causa | Cinco tipos por vídeo, todos salen de algo ya en pantalla: **zoom a través** de un objeto, **cortina «/»**, **la tarjeta que se ensancha** hasta ser la ventana, **llevar al otro lado** (el elemento se encoge hasta su sitio en la escena siguiente) y **cambio de fondo con desenfoque** |
| Demo | En una ventana del escenario con la cara abajo, más **dos insertos a pantalla completa de ≤ 2 s** (el toque y el resultado) donde la interfaz se ve a su tamaño real. Sin anillo de toque |
| Una serie de cosas | Una tarjeta protagonista que cambia de contenido (`icon-swap`: sale con desenfoque, entra enfocándose) en vez de una fila de iconos pequeños |
| Última línea | ≥ 2 s en pantalla: una cola de 1 s con el último fotograma (`tpad`) y las últimas palabras en un solo grupo |
| Mezcla | Música que **baja 4 dB cuando hablas** (`sidechaincompress`) y dos másteres, con y sin música (AV-012, propuesta) |
| Revisión | `revisar.py` mide el MP4 (loudness, cara tapada, tramos del escenario sin cambio, voz en los empalmes) y genera la hoja de 1 fotograma por segundo y la de 360 px |

### Estilo flotante (ensayo 3 de VID-0002, 2026-11-18; propuesta AV-013)

Alternativa a E-01 cuando la pantalla dividida no aporta: la **cara a pantalla completa** todo el vídeo y la división solo para la **demo** de la app. Los gráficos flotan sobre la cara:
- **Nodos** (icono, tarjeta de cristal oscuro o etiqueta) en los márgenes y por encima de la cabeza, nunca sobre la cara. A cámara la cabeza ocupa de y 500 a 1040: la zona libre es y 170–480, las columnas x < 370 y x > 790, y el pecho de y 1040 a 1140.
- **Entrada y salida desenfocadas** (14 → 0 px), **deriva leve** (±5–14 px y ±1,6°, con fase propia) y **profundidad** (los lejanos, más pequeños, tenues y con 2 px de desenfoque).
- **Flechas** que se dibujan con un punto de luz que viaja; las que cruzan el cuadro **dan la vuelta por encima de la cabeza**, nunca por el mentón.
- **Un hilo conductor:** un elemento que reaparece (en VID-0002, el teléfono flotante, que se ensancha hasta ser la ventana de la demo y vuelve a encogerse).
- **Resplandor** en blanco roto: es excepción a AV-007 (sin resplandores) y solo se usa tras la decisión de Ale.

## Hacia un estándar estable

**Meta:** que un vídeo nuevo se edite con los mismos pasos, archivos y scripts, cambiando solo el contenido (palabras, eventos, recursos y música). **Se da por estable** cuando dos vídeos seguidos salen sin tocar los scripts ni las reglas.

> **Estado (2026-11-20):** el proceso está escrito en la skill **`/edicion`** (`.claude/skills/edicion/`: pasos, valores de referencia, errores ya corregidos y lista de revisión) y la base canónica es `videos/VID-0003/hyperframes/edicion/` (v04, aprobada por Ale): un vídeo nuevo copia esa carpeta y cambia solo los datos. Motivo: una edición hecha en otra computadora solo con las guías salió poco pulida (transiciones, volúmenes, tarjetas, efectos), porque los valores finos vivían en el código de una sesión.

| Pieza | Hoy (VID-0002) | Estable |
|---|---|---|
| Corte | `cortes.py` con `KEEP` medido a mano por vídeo | El mismo script; `KEEP` en un archivo de datos del vídeo y la medida de silencios automática |
| Eventos | Tablas en `PLAN*.md` y tiempos en segundos escritos en `index.html` | **Un `eventos.csv` por vídeo** anclado a palabras (no a segundos), del que leen la composición y la mezcla. Si cambia el corte, nada se mueve a mano |
| Componentes | Hoja, tarjeta, flecha, celular, subtítulo, ventana y sello reescritos en cada composición | **Librería de la marca** (`marca/motion/`) reutilizable; cada vídeo solo la combina |
| Estilo | E-01 (escenario) y flotante (AV-013) en prueba | Un estilo elegido por Ale, con variantes por tipo de vídeo |
| Mezcla | Tres scripts (`mezcla.py`, `mezcla_v05.py`, `mezcla_flotante.py`) | Uno, que lee los sonidos de `eventos.csv`, edita la música por tramos y saca los dos másteres |
| Recursos | No había | B-roll propio en el guion y en `/rodaje`; stock solo si falta |
| Música | Un lofi en bucle bajo la voz | Brief de música en el guion, pista con estructura y sincronía en 3–4 puntos |
| Revisión | `revisar.py`, capturas y revisión de Claude | Lo mismo, más la escucha de Ale en el celular como puerta antes de pulir |
| Orden | Varios scripts y pasos manuales | **Hecho en parte:** skill `/edicion` con el orden y los valores; `preparar.py` → `render` → `mezcla.py` en VID-0003. Pendiente: `editar.py` que lo encadene |

**Orden para llegar:** (1) cerrar el estilo y la música con VID-0002 v06; (2) extraer los componentes y el `eventos.csv` de la v06; (3) unificar la mezcla y crear `editar.py`; (4) editar el siguiente vídeo con el estándar y anotar lo que haya que tocar; (5) si el segundo sale sin tocar nada, se declara estable.

## Portada

Cada vídeo lleva su propia portada: título corto, un único foco (cara **o** producto) y, si hay serie, una marca de serie. Comprueba en cada red si se puede subir una portada propia antes de prometerla en el plan.

## Referencias visuales

En [referencias/LEER.md](../referencias/LEER.md). Sirven para estudiar la técnica. No se copian imágenes, tipografías, logos ni identidades.
