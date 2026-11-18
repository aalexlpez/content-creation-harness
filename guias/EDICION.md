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

## Color

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
| 1 | Ale | Corta y limpia el bruto en CapCut: toma por frase y silencios fuera. Exporta solo **Video**, sin marcar la casilla Audio (que crea un `.aac` aparte), en 1080P, H.264, mp4 y 30 fps, sin música ni subtítulos | `media/originales/<nombre>.mp4` |
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

## Portada

Cada vídeo lleva su propia portada: título corto, un único foco (cara **o** producto) y, si hay serie, una marca de serie. Comprueba en cada red si se puede subir una portada propia antes de prometerla en el plan.

## Referencias visuales

En [referencias/LEER.md](../referencias/LEER.md). Sirven para estudiar la técnica. No se copian imágenes, tipografías, logos ni identidades.
