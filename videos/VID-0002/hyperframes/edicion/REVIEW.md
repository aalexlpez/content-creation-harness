# VID-0002 · Revisión de la edición v01

Revisión del 2026-11-18 de `media/trabajo/edicion_v01.mp4` (63,25 s, 1080×1920, H.264, AAC). Formato de [MOTION §7](../../../../guias/MOTION.md#7-proceso-de-una-capa-de-motion): `t=… · dónde · problema → cambio · qué se queda`, con prioridad **P0** (rompe la lectura), **P1** (debilita) o **P2** (pulido).

**Cómo se revisó:** hoja de contacto a 1 fotograma por segundo de los 63 s, cuatro fotogramas medidos a resolución completa (6, 19, 30 y 45 s), loudness con `ebur128` y detección de cortes. No se pudo correr `hyperframes check` sobre la composición: su copia de trabajo (`assets/corte.mp4`) quedó en la otra computadora. Las medidas en píxeles son aproximadas, tomadas del fotograma renderizado.

**Comparación:** el reel de Erik Taveras analizado el 2026-11-17 ([referencias/MOTION.md](../../../../referencias/MOTION.md)), el estándar [MOTION](../../../../guias/MOTION.md) (AV-010) y el método [E-01](../../../../guias/EDICION.md#edición-continua). Las pautas de «otros creadores» de la sección 3 son patrones generales del formato, no un análisis de vídeos concretos: aquí solo se estudió a fondo el reel de Erik.

## 1. Lo que funciona (se queda)

- **El fotograma 0 cumple:** cara y hoja «ENERO» ya en pantalla.
- **El gancho a cámara (0–4 s):** subtítulos con palabra invertida, la hoja que gira y la desaturación. Claro y con ritmo.
- **El escenario del problema (5–12 s):** el calendario que se marca y se para a mitad de mes, y el día «JUEVES ? / SIN GANAS». Ilustra la idea, no repite la voz. Es lo más cercano al nivel de Erik.
- **El sonido:** −14,2 LUFS integrados, LRA 3,0 LU, pico −4,1 dBFS. Dentro de la norma (−16 a −14 LUFS, ≤ −1 dBTP), y Ale lo aprobó al oído.
- **Cierre (57–63 s):** acento «Este febrero, *no*.» y la etiqueta del link sin tapar la cara.

## 2. Hallazgos por prioridad

### P0 · rompen la lectura

1. `t=22,7–41,9 · demo a pantalla completa · tu cara desaparece 19 s seguidos (30 % del vídeo) y el único cambio es la interfaz → partir la demo en 3 golpes de ≤ 4 s (escribir · elegir obstáculo · resultado) intercalados con escenario, o meter la demo DENTRO del escenario (arriba) con tu cara abajo · se queda: la maqueta y sus textos`. Erik nunca deja de mostrar la cara más de unos segundos: es lo que sostiene la retención en un vídeo hablado.
2. `t=29–31 · demo, paso 2 · los subtítulos («NO TUVE TIEMPO») caen encima de las tarjetas de obstáculo y se mezclan con ellas → en modo P, banda de subtítulos propia con fondo (franja marino) fuera de la interfaz, o subir la interfaz para liberar la banda · se queda: el negreo de las tarjetas`.
3. `t=29,6 · toque en «No tuve tiempo» · anillo de clic, prohibido en MOTION §4 («anillos de clic») → toque como presión del botón (escala 0,97 y vuelta) sin anillo · se queda: el negreo`.

### P1 · debilitan

4. `t=17–22 · escenario «LA SOLUCIÓN» · la tarjeta «Plan B» queda casi quieta 6 s; solo entran dos fichas pequeñas («GRATIS», «PARA ESE DÍA») → un evento por frase: «gratis» tacha un precio, «planear ese día» enlaza con el día «SIN GANAS» del tramo anterior, «la primera de una serie» abre el contador · se queda: la tarjeta`. Está al borde del `dead_stretch` (> 3 s sin cambio) y lejos del ritmo de Erik (un cambio cada 0,5–1,5 s).
5. `t=42–56 · escenario «LA SERIE» · 14 s con la misma fila de tarjetas e iconos de ~60 px que se van llenando → menos tiempo (es una digresión del guion, ver §4) y gráficos más grandes: un icono protagonista a ≥ 300 px por categoría, que sustituye al anterior · se queda: la idea de la fila «01 · 02 · 03»`.
6. `t=5–8 · calendario de enero · los números de los días miden ~20 px: ni se leen (< 28 px) ni son claramente textura → quitarlos (solo casillas) o subirlos a ≥ 32 px · se queda: las marcas`. Regla de los «dos estados» (MOTION §3).
7. `t=5–56 · subtítulos del escenario · ~50 px de altura efectiva, por debajo del mínimo de 56 px (MOTION §3) → subir el cuerpo ~15 % (o usar una versión condensada de la marca si existe) · se queda: la palabra invertida`. Los de Erik ocupan más ancho con menos palabras.
8. `t=0–63 · cabecera «/ PLAN B · MINIAPP 01» · ~20 px, solo legible en pantalla grande → ≥ 32 px o quitarla y dejar solo el título del tramo · se queda: el título del tramo`.
9. `t=13–16 · rótulo MG-02 · aparece arriba a la izquierda (y ≈ 280) y no abajo como en el kit; pequeño y lejos de la cara → posición del kit (y 1230–1400) o integrarlo en el escenario siguiente · se queda: el texto`.

### P2 · pulido

10. `t=23–41 · demo · el teclado y la interfaz son legibles, pero la cámara virtual apenas se mueve → si la demo se queda a pantalla completa, un empuje claro por paso (máx. 1,1×) y una sola vez (MOTION §4)`.
11. `t=57–62 · etiqueta «EL LINK, EN MI PERFIL» · el link aún no existe (claim C8) → en el vídeo real, solo con la dirección publicada`.
12. `t=0–63 · sonido · 44 efectos más música · revisar en el celular que la música (−18 dB) no compita con la voz en los tramos rápidos; si molesta, bajarla 3 dB o quitarla en la demo`.

## 3. Comparación con los referentes

| Aspecto | Erik Taveras | Patrones del formato (YouTube Shorts, Reels y TikTok educativos) | VID-0002 v01 |
|---|---|---|---|
| Cara en pantalla | Siempre (mitad inferior en el escenario) | La cara sostiene la retención en vídeos hablados | Ausente 19 s seguidos en la demo |
| Ritmo de cambios | Uno cada 0,5–1,5 s | Algo cambia cada 1–3 s | Bien en el gancho y el problema; lento en «La solución» y «La serie» |
| Tamaño de gráficos | Iconos grandes, pocos por pantalla | Un protagonista por plano | Iconos de ~60 px, varios por pantalla en «La serie» |
| Subtítulos | Grandes y condensados, 2–4 palabras, palabra clave destacada | Grandes, alto contraste, nunca encima de la interfaz | Buenos en estilo, algo pequeños; chocan con la interfaz en la demo |
| Orientación | «1 de 5», título de tramo | Capítulos o contadores en vídeos con lista | Títulos de tramo, sin contador de progreso |
| Producto | Capturas reales, breves | Demo real y breve, con zoom al detalle | Maqueta larga (19 s) |
| Duración | 96 s con 5 bloques claros | Los cortos con una sola idea rinden mejor por debajo de 45–60 s | 63 s con 7 tramos: la serie añade 14 s fuera de la idea central |

## 4. Qué cambiar en el proceso

Los problemas de arriba no son de ejecución, sino de decisiones que llegaron tarde. Cambios propuestos al proceso (MOTION §7 y E-01):

1. **Presupuesto de tiempo por tramo antes de animar.** En `PLAN.md`, cada tramo lleva una duración máxima: escenario ≤ 6 s seguidos, pantalla completa ≤ 4 s seguidos, cara visible ≥ 60 % del vídeo. Se comprueba sobre la lista de eventos, antes de escribir código.
2. **Regla «cara siempre»:** en E-01, la pantalla completa (modo P) es una excepción de ≤ 4 s. Por defecto, la demo va en el escenario, arriba, con la cara abajo.
3. **Una sola idea y una duración objetivo de 40–45 s** decididas en el guion. Las digresiones (la serie, en este vídeo) van a otro vídeo o se quedan en una frase con un solo gráfico.
4. **Medición automática en el render, no en el código.** Script con ffmpeg y la biblioteca estándar que, sobre el MP4, mida altura de texto, tramos sin cambio (> 3 s), tiempo con cara visible y loudness, y escriba el resultado en este `REVIEW.md`. Hoy dependemos de `hyperframes check`, que necesita el proyecto completo y no ve el resultado final.
5. **Banda de subtítulos reservada en cada modo:** cámara, escenario y pantalla completa tienen una franja fija para subtítulos que ningún gráfico ni interfaz puede ocupar.
6. **Revisión independiente obligatoria** (MOTION §7, paso 7) con la hoja de 1 fps y este formato antes de enseñar el corte. Esta revisión la hizo Claude después de entregar: tiene que ir antes.
7. **Referencia visual concreta por tramo:** para cada tramo, una captura de referencia (Erik u otro creador) guardada en `referencias/` y citada en `PLAN.md`, para que el tamaño y la densidad se comparen antes de animar.

## 5. Siguiente paso recomendado

Aplicar los P0 y los P1 4–7 en la regrabación (el vídeo final irá en otro expediente) y convertir los puntos 1–5 de la sección 4 en reglas de [MOTION](../../../../guias/MOTION.md) y [EDICION](../../../../guias/EDICION.md) si Ale los aprueba.

## 6. Resultado de los arreglos (v02 de la composición, 2026-11-18)

Entrega: `media/trabajo/edicion_v03.mp4` (49,66 s, voz mejorada de Ale, 39 efectos + música, −14,4 LUFS, pico −3,7 dBFS). Composición v02 en `index.html`; la v01 queda en `versiones/edicion_v01.html.txt`.

| # | Hallazgo | Hecho |
|---|---|---|
| 1–2 | Cara ausente 19 s en la demo | La demo va en una ventana del escenario (960×520, escala 0,889) que sigue el paso activo; la cara se ve en todo el vídeo |
| 3 | Subtítulos sobre la interfaz | Banda fija: y ≈ 862 en el escenario (la ventana acaba en 850) y y ≈ 1190 a cámara |
| 4 | Anillo de toque | Quitados punto y anillo en MG-06 (v04); queda la presión del botón y el negreo |
| 5 | «La solución» quieta | Precio «$» tachado → GRATIS → PARA ESE DÍA → 01 |
| 6–7 | «La serie» larga, 63 s | Recortes de voz: «Aquí simplemente», «¿Como cuál?», «para productividad… necesite» y «Y me dices qué tal» → 49,66 s. «La serie» queda en 4 s con «1 POR SEMANA» |
| 8 | Subtítulos pequeños | 58 → 66 px de cuerpo |
| 9 | Cabecera derecha | 24 → 32 px |
| 10 | Números del calendario | Quitados; días de la semana a 28 px |
| 11 | Rótulo «Plan B» duplicado | Quitado (la tarjeta del escenario lo dice 2 s después); también el rótulo «Arma tu plan B», que chocaba con el acento final |
| 12 | Cámara en la demo | El paneo de la ventana hace de cámara |
| 13 | Golpes fuertes | Siguen 3: bajón del gancho, sello y «no.» |
| 14 | Compresión de la voz | 3:1 desde −20 dB → 2:1 desde −18 dB |
| 15 | Música en la demo | −3 dB durante la demo |
| 16 | Demasiados efectos | 63 → 39 |
| 17 | Etiqueta del link | Quitada hasta que la dirección exista (C8) |
| 18 | C1 | Pendiente de la regrabación (no se puede arreglar en edición) |

`hyperframes check`: sin errores; queda un aviso menor (el subtítulo «8» dura 0,26 s) y el solape intencional de las dos caras de la hoja de calendario.

## 7. Correcciones de Ale sobre la v03 (composición v03, 2026-11-18)

Ale, sobre la v03: el corte tras «semana» era brusco («te pasaste de recorte») y los zooms de la demo «muy sencillos… hay trozos que ni se lee bien la pantalla». Entrega: `media/trabajo/edicion_v04.mp4` (55,48 s, 43 efectos + música, −14,4 LUFS, pico −4,3 dBFS). Composición v02 guardada en `versiones/edicion_v02.html.txt`.

| Problema | Causa | Arreglo |
|---|---|---|
| Corte brusco tras «semana» | El corte caía a −23 dB, en plena voz y a mitad de frase («a la semana *para…*»); Parakeet daba tiempos adelantados en esa zona | Los cortes se miden sobre la voz (ventanas de 10 ms) y caen en silencios < −60 dB y en finales de frase (`cortes.py`). «La serie» vuelve hasta «…cualquier ámbito.» (solo se quita el «eh»); «Aquí simplemente» se queda porque no tiene pausa donde cortar |
| Demo mal encuadrada | La ventana desplazaba una franja fija (zoom 0,889) por la maqueta y partía campos y botones | Planos por grupo de interfaz medidos sobre la maqueta (centro y zoom por momento, `FRAMES`), con acercamientos y alejamientos de 0,55 s; la ventana cambia de ancho con el zoom (sin franjas) y aparece cuando la maqueta terminó su entrada |
| Subtítulo que se salía del ancho | Con 66 px, «MINIAPLICACIÓN A LA SEMANA» no cabía | Cada grupo se encoge si su ancho estimado pasa de 980 px |

**Regla nueva para el proceso:** un corte de voz solo se acepta si cae en un silencio medido y no parte una frase que sigue. Se comprueba con la medida, no con los tiempos de la transcripción.
