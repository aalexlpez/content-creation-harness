# VID-0001 · Plan B · Guion por beats, edición simple y motion graphics

**Estado:** propuesta del 2026-11-16, pendiente de tu revisión. No sustituye a `GUION.md` ni toca ninguna aprobación. Es un documento de trabajo para sesiones locales de Claude: léelo completo antes de pedir nada.

> **Aviso: experimento.** Este documento todavía no forma parte del marco y contradice reglas vigentes hasta que se formalice: D-EDICION (la dirección de montaje va dentro del guion), `guias/GUIONES.md` §5 y la regla de `CLAUDE.md` sobre montaje por escena, D-EDIT (CapCut como editor final), AV-001 (HyperFrames como motor) y la corrección de color de `guias/EDICION.md`. Durante el ensayo mandan el marco vigente para aprobaciones y estados, y el OK-2 se calcula sobre `GUION.md`. Después del primer ciclo completo (grabar, montar con Claude y revisar) se decide qué se formaliza.

**Para qué sirve:** (1) saber qué decir y cómo decirlo en cada momento del video, con tus palabras; (2) editar sin ser editor, con una receta corta que no depende de frases exactas; (3) pedirle a Claude los motion graphics con prompts listos para pegar.

---

## 0. Cómo se usa

| Paso | Quién | Qué pasa |
|---|---|---|
| 1 | Tú | Lees los beats (sección 2) y grabas con tus palabras. No memorices el texto de ejemplo |
| 2 | Tú | Guardas el video bruto en `videos/VID-0001/media/originales/` |
| 3 | Tú | Sacas las capturas de encuadre (sección 4.1) |
| 4 | Claude | Transcribe, propone el corte y arma la edición según el nivel que elijas (sección 3) |
| 5 | Claude | Genera cada motion graphic con el prompt maestro (4.3) más el prompt de la pieza (4.4) |
| 6 | Tú | Revisas en el celular con la lista de la sección 3.6 y pides correcciones concretas |

**Prompt de arranque para una sesión local** (pégalo tal cual y cambia el nombre del archivo):

```
Lee CLAUDE.md y videos/VID-0001/GUION_BEATS.md (secciones 1, 3 y 4).
Material: videos/VID-0001/media/originales/<archivo>.mp4
1. Transcribe con tiempos por palabra, en español. Corrige las marcas
   (cerobytes, Plan B, MiMiniApp) y enséñame el transcript.
2. Propón el corte: quita silencios de más de 0,4 s y deja la última toma
   de cada frase. No renderices todavía.
3. Aplica el Nivel B de la sección 3. Para cada pieza usa el prompt maestro
   (4.3) más el prompt de la pieza (4.4), y mis capturas en media/trabajo/capturas/.
4. Muéstrame 3 fotogramas por pieza (antes, durante, después) y espera mi OK
   antes del render completo.
```

---

## 1. Idioma: español latinoamericano

Regla del proyecto (CONTENIDO-LATAM-001): voz, subtítulos y textos en pantalla en español latinoamericano. Si una frase te suena rara al decirla, cámbiala por la tuya.

| En vez de (España) | Di (Latinoamérica) |
|---|---|
| móvil | celular |
| enlace | link |
| ordenador | computadora |
| ya has abandonado, ya lo has dejado | ya abandonaste, ya lo abandonaste (o «tiraste la toalla», «te rendiste») |
| no te apetece | no tienes ganas |
| vale | ok, listo, perfecto |
| añadir | agregar |
| coger | tomar, agarrar |
| gafas | lentes |
| genial / guay / mola | está padre, está genial, qué bueno |
| os / vosotros | ustedes |

**Textos de la app que hoy suenan a España** (la ficha v06 de `soycerobytes/miminiapp` los trae así; decisión de producto, no la cambio aquí):

| Texto actual | Sugerencia latinoamericana |
|---|---|
| Es {mes} y ya has abandonado tu propósito. | Es {mes} y ya abandonaste tu propósito. |
| Imagina que es 1 de {mes} y lo has dejado. ¿Qué ha pasado? | Imagina que es 1 de {mes} y ya abandonaste tu propósito. ¿Qué pasó? |
| Usar menos el móvil | Usar menos el celular |
| no me apetece nada | no tengo ganas de nada |
| Añadir a mi calendario / Añadir hora | Agregar a mi calendario / Agregar hora |

**Decisión (2026-11-16): los textos de la app se quedan como están por ahora.** La maqueta del video (MG-06 y MG-07) muestra los textos tal como están en la ficha v06, para que coincidan con la app real. Tu voz y tus subtítulos sí van en español latinoamericano.

---

## 2. Guion por beats

Seis momentos. Cada uno dice **qué debe lograr**, **qué expresar**, **cómo decirlo** y trae **ejemplos de cómo podría sonar**. Los ejemplos no son literales: si dices otra cosa que cumple el objetivo, está bien.

| # | Beat | Qué logra | Tiempo objetivo |
|---|---|---|---|
| 1 | Gancho | Que se queden los primeros 3 segundos | 0–3 s |
| 2 | Problema | Que se reconozcan en la situación | 3–9 s |
| 3 | Solución | Que entiendan qué es Plan B y de quién es el reto | 9–14 s |
| 4 | Demo | Que vean cómo funciona, sin leer | 14–29 s |
| 5 | Prueba | Que confíen: gratis, sin cuenta, comprobable | 29–36 s |
| 6 | Llamada a la acción | Que abran el link | 36–41 s |

Duración total estimada: 38–42 s. Se confirma al leerlo en voz alta.

### Beat 1 · Gancho (0–3 s)

- **Qué debe lograr:** tensión reconocible en la primera frase. Nada de saludo.
- **Qué expresar:** el problema (el propósito que se abandona). Es lo único que entiende cualquiera sin contexto.
- **Cómo decirlo:** empieza ya hablando, mirando al lente, con voz firme y un poco de ironía. La primera palabra con fuerza. Un solo aire, sin pausas.
- **Ejemplos:**
  - «Es febrero y ya abandonaste tu propósito de año nuevo.»
  - «Es 1 de febrero y tu propósito de año nuevo ya se acabó.»
- **Evita:** «Hola», presentarte, o empezar por el nombre de la herramienta.

| Gancho | Tipo | Se entiende solo | Coincide con el video | Prueba pronto | Sin clickbait | Total |
|---|---|---:|---:|---:|---:|---:|
| «Es febrero y ya abandonaste tu propósito…» | problema | 2 | 2 | 1 | 2 | 7/8 |
| «Voy a crear una herramienta útil cada semana. Esta es la primera.» | reto | 1 | 2 | 0 | 2 | 5/8 |

Puntuación mía, como criterio inicial. **Recomendación:** abrir con el problema y poner el reto en el beat 3 y en el cierre. Si prefieres abrir con el reto, el gancho es débil hasta que la gente conozca el canal.

### Beat 2 · Problema (3–9 s)

- **Qué debe lograr:** que el espectador piense «eso me pasa a mí», y que el dato dé credibilidad.
- **Qué expresar:** (a) a mediados de enero mucha gente ya abandonó su propósito; (b) la idea de fondo: nadie planea qué va a hacer el día que no tenga ganas.
- **Cómo decirlo:** más bajo y cómplice. Una pausa corta después de «calma». Sin dramatizar.
- **Ejemplos:**
  - «Calma, todavía no. Pero para mediados de enero mucha gente ya tiró la toalla.»
  - «Y casi nadie piensa qué va a hacer el día que no tenga ganas.»
- **Evita:** cifras exactas, un día concreto del mes, y «todos» o «nadie» como absolutos que no puedes probar. El dato tiene una fuente (Strava) y se dice como «mucha gente».

### Beat 3 · Solución (9–14 s)

- **Qué debe lograr:** una idea clara: qué es, que es gratis y que es el primer paso de un reto.
- **Qué expresar:** (a) hiciste una herramienta para planear ese día; (b) se llama Plan B; (c) es la primera de una serie semanal.
- **Cómo decirlo:** sube un poco la energía. Presentarte aquí, en una frase y sin currículum. Di «cerobytes» sin arroba.
- **Ejemplos:**
  - «Por eso hice Plan B: una herramienta gratis para planear ese día.»
  - «Soy Alexander y cada semana voy a crear una herramienta útil. Esta es la número uno.»
- **Decisión tuya:** cuánto prometer. «Cada semana» es una promesa moderada. «Durante un año» es mucho más fuerte, y si fallas una semana te cuesta credibilidad. Mi recomendación: «cada semana, mientras pueda» o un contador visible sin prometer fecha de fin.

### Beat 4 · Demo (14–29 s)

- **Qué debe lograr:** que se entienda el recorrido de la herramienta sin leer nada.
- **Qué expresar:** cuatro verbos en orden: escribes tu propósito → te lleva a febrero → eliges qué pasó → armas tu plan («si pasa esto, entonces hago esto»). Después, lo que te llevas: recordatorio en tu calendario y fondo de pantalla.
- **Cómo decirlo:** ritmo parejo y rápido, una frase corta por paso. La imagen manda: tu voz acompaña. Usa el ejemplo de la propia app (ejercicio, no tuve tiempo, llego a casa después de las 20:00, cinco minutos de estiramiento). Nada de castigos ni flexiones.
- **Ejemplos:**
  - «Escribes tu propósito, la app te lleva a febrero, eliges por qué lo abandonaste y armas tu plan.»
  - «Por ejemplo: si llego a casa después de las ocho, hago cinco minutos de estiramiento.»
  - «Y te llevas un recordatorio en tu calendario y tu plan como fondo de pantalla.»
- **Evita:** explicar botones, decir «es muy fácil», y hablar de funciones que la app no tiene (ver la ficha v06).
- **Regla del video real:** esta parte se muestra con una **grabación de la app publicada**. La maqueta (MG-06 y MG-07) solo se usa en el ensayo o mientras la app no exista, y siempre con el rótulo «Maqueta de ensayo».

### Beat 5 · Prueba (29–36 s)

- **Qué debe lograr:** confianza. Que la gente no sienta que le van a pedir algo.
- **Qué expresar:** es gratis, no necesitas cuenta y lo que escribes se queda en tu celular. Y una invitación a comprobarlo con el modo avión.
- **Cómo decirlo:** tono de reto amistoso, mirando al lente. Que se note una sonrisa en «compruébalo».
- **Ejemplos:**
  - «Es gratis, no necesitas cuenta y lo que escribes se queda en tu celular.»
  - «No me creas: ponlo en modo avión y compruébalo.»
- **Evita:** «gratis para siempre», «nada sale de tu celular» (si compartes o exportas, sí sale) y «funciona sin internet» a secas (solo funciona en modo avión **una vez cargada** y sin recargar).
- **Imagen ideal:** tu mano activando el modo avión en un celular real con la app abierta. Con la app publicada, grábalo. Antes, no demuestres nada con una ilustración.

### Beat 6 · Llamada a la acción (36–41 s)

- **Qué debe lograr:** una sola acción: abrir el link y armar el plan.
- **Qué expresar:** «arma tu plan B», el plazo («antes de que llegue febrero») y dónde está el link.
- **Cómo decirlo:** mirando al lente, más lento, y terminar en seco, sin alargar.
- **Ejemplos:**
  - «Arma tu plan B antes de que llegue febrero. El link está en mi perfil.»
  - «La próxima semana, una nueva.» (señala el reto, sin pedir nada más)
- **Evita:** pedir dos cosas a la vez (abrir el link **y** comentar). Si el objetivo es conversación, cambia la acción por «cuéntame tu plan en los comentarios» y quita el link.

### Claims que sostiene este guion

| claim_id | tipo | afirmación | prueba y límites |
|---|---|---|---|
| C1 | E | A mediados de enero mucha gente ya abandonó su propósito | Datos de actividad de Strava, vía [BikeRadar](https://www.bikeradar.com/news/today-is-the-day-we-lose-motivation-strava-says). Son usuarios de una app deportiva y el día cambia cada año: se dice «mucha gente», sin fecha ni cifra |
| C2 | O | Casi nadie piensa qué hará el día que no tenga ganas | Opinión tuya. Decirla como opinión |
| C3 | H | El recorrido: propósito, salto al mes siguiente, obstáculo, plan «si… entonces» | Ficha v06 de la app. Pasa a P cuando la app esté publicada y la demo sea una grabación real |
| C4 | H | Te llevas un recordatorio en tu calendario y tu plan como fondo de pantalla | Ficha v06. Pasa a P tras la prueba en Android y iPhone. No se promete la hora del aviso |
| C5 | H | Gratis y sin cuenta | Ficha v06. Nunca «para siempre» |
| C6 | H | Lo que escribes se queda en tu celular y funciona en modo avión | Ficha v06: solo sale si exportas a Google o compartes la imagen; en modo avión funciona con la página ya cargada y sin recargar |
| C7 | O | Esta es la primera herramienta del reto | Compromiso tuyo; decide cuánto prometer |

Claims C3–C6 siguen en H hasta que la app exista. Un claim X bloquea el OK-2: aquí no hay ninguno.

### Cómo grabar para que la edición sea fácil

1. **Mismo encuadre en todas las tomas.** Marca en el suelo el trípode y tu lugar. Camiseta lisa, sin logos (el logo obliga a difuminar).
2. **Un segundo quieto** antes y después de cada frase, para poder cortar limpio.
3. **Mirada al lente**, no a la pantalla de lectura. Si usas chuleta, pégala junto al lente.
4. **Dos o tres tomas por beat**, y sigue sin parar si te equivocas: se queda la última buena.
5. **El audio primero:** prueba del DJI de 10 segundos, escuchada con audífonos.
6. **Fondo de pantalla del celular:** si grabas la demo real, que no tenga notificaciones ni datos personales.

---

## 3. Edición simple

Principio: **la edición responde al beat, no a la frase.** Si cambias una palabra, nada se rompe. Los tiempos los saca Claude del transcript, después de grabar.

### 3.1 Tres niveles

Elige uno antes de empezar. Los tiempos son estimaciones hasta tener datos.

| Nivel | Qué incluye | Tu tiempo de revisión | Cuándo |
|---|---|---|---|
| **A · Mínimo** | Corte limpio + subtítulos (SUB-01) + rótulo de presentación (MG-02) + acento final (MG-05). Sin música | ~15 min | Semana apretada |
| **B · Estándar (recomendado)** | A + demo a pantalla completa (MG-06 y MG-07) + tarjetas de fuente y de prueba (MG-03, MG-04) + efectos de sonido + música suave | ~25 min | Lo normal |
| **C · Completo** | B + hoja de calendario del gancho (MG-01) + firma MiMiniApp (MG-08) | ~40 min | Videos de lanzamiento |

### 3.2 Receta por beat

| Beat | Imagen | Texto en pantalla | Transición | Sonido | Música |
|---|---|---|---|---|---|
| 1 Gancho | Cámara, plano medio. Opcional (C): MG-01 junto a la cabeza | Subtítulos | Ninguna: arranca en seco | Nivel C: golpe grave corto al apagarse la imagen | No |
| 2 Problema | Cámara. B: MG-03 (fuente del dato) en la franja baja | Subtítulos + tarjeta | Corte directo | Nada | No |
| 3 Solución | Cámara + MG-02. C: MG-08 al final del beat | Rótulo «Plan B · para tu propósito» | Corte directo | Pop suave al aparecer el rótulo | Entra muy suave al final del beat |
| 4 Demo | **Pantalla completa** (MG-06, MG-07). Tu cara no sale | Subtítulos abajo | Entrada deslizante de 0,3 s | Whoosh de entrada, toque, golpe del sello, ding del calendario | Sostenida, baja |
| 5 Prueba | Cámara + MG-04. Con la app publicada: grabación del celular en modo avión a pantalla completa | Subtítulos + tarjeta | Corte directo | Clic del interruptor | Sostenida |
| 6 CTA | Cámara, **mismo encuadre que el gancho**. MG-05 sobre la cabeza | Subtítulos + acento | Corte directo | Ding suave | Se funde antes de tu última frase y termina |

### 3.3 Reglas simples

- **Transiciones:** solo dos, corte directo y entrada deslizante de 0,3 s para pasar a pantalla completa. Nada de giros, glitch ni zooms.
- **Un foco por plano:** un solo elemento animado a la vez, máximo dos.
- **Color:** no se corrige. La cámara manda. El único efecto de color es el del gancho (Nivel C), y lo hace Claude: no tienes que tocar saturación.
- **Ritmo:** corta los silencios de más de 0,4 s. No aceleres el video.
- **Cierre:** sin tarjeta final. El cierre es tu frase.

### 3.4 Subtítulos

Los hace Claude con SUB-01 (sección 4.4). Resumen para revisarlos: una línea, por frases, palabra activa en caja blanco roto con texto negro, mayúsculas, nunca tapan la barbilla. Revisa eñes, tildes y los nombres (cerobytes, Plan B, MiMiniApp).

### 3.5 Sonido y música

- **Efectos:** solo cuatro tipos, ligados a una acción: whoosh (entra pantalla completa), toque o clic (interacción), golpe (sello o gancho) y ding (confirmación). Van entre 8 y 16 dB por debajo del pico de tu voz.
- **Música:** cama instrumental suave, sin letra, 12 a 15 LU por debajo de tu voz. Que Claude la **mida** (no a ojo). Entra con la demo y se funde antes de tu última frase.
- **Derechos:** que una pista esté en el catálogo de CapCut o TikTok no significa que sirva en YouTube o Instagram. Anota cada pista y efecto en `CIERRE.md → Derechos`. No se usan efectos sintetizados por código (AV-008, 2026-11-17): solo sonidos reales, grabados por Ale o de bibliotecas CC0 como Freesound, escuchados antes de usarlos.
- **Mezcla final:** −14 LUFS, con pico bajo −1 dBTP.

### 3.6 Revisión en el celular (tu lista)

1. ¿Se entiende la voz en todos los momentos, con música y efectos?
2. ¿Los subtítulos se leen sin esfuerzo y sin errores de ortografía?
3. ¿Algo tapa tu cara, la barbilla o los botones de la red?
4. ¿Cada tarjeta dice algo que tú **no** dices? Si repite la voz, se quita.
5. ¿Todo lo que se afirma está en la tabla de claims?
6. ¿La música baja cuando hablas y se va antes del final?
7. ¿El primer segundo engancha?
8. ¿El video termina cuando termina la frase?

Pide correcciones con tiempo, defecto, cambio y criterio: «en 0:21 la tarjeta tapa mi mano; muévela abajo hasta que no se vea». Máximo dos rondas.

---

## 4. Motion graphics

### 4.1 Insumos que le das a Claude

Por cada video:

1. **Video bruto** en `media/originales/`.
2. **Transcript con tiempos por palabra** (lo genera Claude).
3. **Captura de encuadre con rejilla.** Sirve para ubicar texto alrededor de tu cara:

```bash
ffmpeg -ss 5 -i media/originales/TOMA.mp4 -frames:v 1 -vf "drawgrid=w=100:h=100:t=2:c=red@0.6" media/trabajo/capturas/encuadre_rejilla.png
```

   Cada cuadro mide 100 px. Guarda **también** el mismo fotograma sin rejilla (`-vf` omitido). Saca tres: tú en reposo, con la mano arriba y con la cabeza girada.
4. **Capturas anotadas (opcional):** dibuja un rectángulo sobre una captura donde quieres un texto. Claude lee la imagen y respeta la zona.
5. **Marcas.** La del video (cerobytes v2) está en `marca/identidad.json` y sus logos en `marca/kit/`. La tipografía (Plus Jakarta Sans) está en `marca/fuentes/plus-jakarta-sans/`. La de MiMiniApp está en el repositorio `soycerobytes/miminiapp` (`public/brand/` y `public/fonts/`): clónalo junto a este o copia esas dos carpetas a `media/trabajo/marca/`.

### 4.2 Dos marcas, sin mezclar

Decisión AV-005: la identidad del video es distinta de la identidad del producto. **La del video cambió el 2026-11-16 (AV-006): cerobytes v2**, con el kit vectorial en `marca/kit/` (detalle en [IDENTIDAD](../../marca/IDENTIDAD.md)).

**Marca del video (cerobytes v2).** Para todo lo que sale alrededor de tu cara.

| Token | HEX | Uso |
|---|---|---|
| Negro | `#0B0B0D` | Texto sobre fondos claros y fondo alternativo |
| Gris carbón | `#1E2937` | Superficies y divisores |
| Azul marino profundo | `#0D213F` | Tarjetas, rótulos y fondo principal |
| Blanco roto | `#F5F6F8` | Texto y símbolo sobre fondos oscuros |
| Azul de la barra (provisional) | `#003571` | Solo formas grandes sobre fondos claros. No es color oficial |

- **No hay color de acento.** El énfasis se hace por **inversión de contraste** (caja blanco roto con texto negro), por peso o por tamaño.
- **Texto secundario sobre marino:** `#B7C0CC` (lo usa el kit; no es color oficial).
- **Contraste:** blanco roto sobre marino 14,9:1 y sobre negro 18,2:1. Carbón, marino y negro casi no se distinguen entre sí (1,1 a 1,3:1): sepáralos con un borde fino de blanco roto al 20 % o con el símbolo. La barra azul sobre negro da solo 1,6:1: en la v1.2, `logo-oscuro.svg` ya lleva la barra blanca y el azul queda solo en los archivos `*-azul-referencia`.
- **Fuente: Plus Jakarta Sans** (AV-007; sustituye a Satoshi). Licencia OFL; archivos en `marca/fuentes/plus-jakarta-sans/`. Pesos propuestos, sin aprobar: Medium 500 (secundario), Bold 700 (subtítulos y rótulos) y ExtraBold 800 (frases de impacto). No tiene peso 900.
- **Símbolo:** la barra diagonal «/» es un paralelogramo (`M 73 4 L 109 4 L 36 134 L 0 134 Z`), inclinado ≈ 29° respecto a la vertical (≈ 61° sobre la horizontal). Es el motivo del video: úsalo con moderación, como acento o separador.
- **Logo:** `marca/kit/svg/logo-navy.svg` sobre marino y `marca/kit/svg/logo-oscuro.svg` sobre negro. `marca/kit/png/` trae PNG transparentes (marcas de agua y rótulo) para CapCut, exportados con Plus Jakarta Sans. **Advertencia de procedencia:** el wordmark es vectorial, pero no es el diseño maestro original; es una reconstrucción del kit v1.2.
- **Prohibido:** el símbolo ®, degradados, resplandores, efectos de ciencia ficción, circuitos, redes de nodos, hexágonos, cerebros y el degradado violeta-azul. Acabados planos.
- **Descartado en AV-006:** cian `#54E0EA`, violeta `#AD8BFF`, lima `#D9F77A`, Inter y Crimson Text + Mr Dafoe.

**Marca del producto (MiMiniApp).** Solo para lo que sale **dentro** del celular y para su logotipo. Fuente: `soycerobytes/miminiapp`, `src/styles/global.css` y `docs/design-docs/appearance-proposal.md`.

| Token | Claro | Oscuro |
|---|---|---|
| Canvas | `#F7F5F0` | `#171421` |
| Superficie / panel | `#FFFFFF` / `#FBFAF8` | `#242033` |
| Texto / secundario | `#242136` / `#605B70` | `#F7F3FF` / `#C0B7D0` |
| Marca (violeta) | `#7950F2` | `#A68AFF` |
| Lima / coral | `#B9F65A` / `#FF9368` | iguales |
| Tinte / borde de panel | `#EDE6FE` / `#CEC6D8` | `#352B4B` / `#494057` |
| Texto del botón principal | `#FFFFFF` | `#171421` |

- **Fuentes:** Space Grotesk (títulos, 700) y DM Sans (cuerpo), en `public/fonts/` (OFL).
- **Radios:** controles 12 px, tarjetas 20 px, paneles 28 px.
- **Reglas de contraste:** el texto sobre lima o coral va **siempre** en `#242136`; nunca blanco (1,28:1 y 2,18:1).
- **Logotipo:** `public/brand/wordmark-editorial-dark.svg` (sobre fondos oscuros) y `wordmark-editorial.svg` (sobre claros). La versión editorial es «el recurso para piezas de marca y videos». No dibujar la M de nuevo ni sustituirla por una letra de fuente.
- **Movimiento de la app (ficha v06):** el paso 2 pasa a gris en 600 ms; el sello cae a −6° con escala 1,4 → 1 en 300 ms.

### 4.3 Prompt maestro

Pégalo **siempre primero**, antes del prompt de cada pieza.

```
ROL
Eres el motion designer de un video vertical corto. Construyes cada pieza en
código (Remotion con la skill de edición ya instalada, o HyperFrames) y me
muestras fotogramas antes de renderizar. Tu criterio es profesional: jerarquía
clara, poco texto, movimiento con intención y nada que compita con mi cara.

CONTEXTO
Video: VID-0001 (Plan B, primera miniapp de MiMiniApp). Lo presenta Alexander,
canal "cerobytes". Audiencia: público general que empieza el año con un
propósito. Idioma de todo texto: español latinoamericano (celular, link,
computadora, pretérito simple). Sin expresiones de España.

FORMATO TÉCNICO
1080×1920, 30 fps, H.264, SDR BT.709 (--color-space=bt709). Render final a
~6 Mbps. Las piezas se componen sobre mi video; no re-encodes innecesarios.
Fuentes SIEMPRE locales (archivos o incrustadas), nunca Google Fonts ni CDN.
Render con concurrency 2 y timeout de 60 s por defecto.

MARCA DEL VIDEO (cerobytes v2; todo lo que va alrededor de mi cara)
Negro #0B0B0D · gris carbón #1E2937 · azul marino #0D213F · blanco roto #F5F6F8.
Texto secundario sobre marino: #B7C0CC. NO hay color de acento: el énfasis es
inversión de contraste (caja #F5F6F8 con texto #0B0B0D), mayor peso o tamaño.
Fuente: Plus Jakarta Sans (Medium 500 / Bold 700 / ExtraBold 800), en
marca/fuentes/plus-jakarta-sans/ (cárgala con @font-face desde ahí). Si no está
disponible en la sesión, DETENTE y avísame: no la sustituyas sin preguntar.
Símbolo: la barra diagonal "/" (marca/kit/svg/isotipo-blanco.svg), inclinada
≈29° respecto a la vertical, usada con moderación como acento o separador.
Logo: marca/kit/svg/logo-navy.svg sobre marino. No lo redibujes.
Superficies planas. Panel de tarjeta: fondo #0D213F al 95 %, radio 18 px, borde
fino #F5F6F8 al 20 %, sin sombras difusas.
PROHIBIDO: cualquier otro color o fuente, degradados, resplandores, símbolo ®,
circuitos, redes de nodos, hexágonos, cerebros, degradado violeta-azul, efectos
de ciencia ficción.

MARCA DEL PRODUCTO (solo dentro del celular y el logotipo)
Claro: canvas #F7F5F0, superficie #FFFFFF, texto #242136, secundario #605B70,
violeta #7950F2, lima #B9F65A, coral #FF9368, tinte #EDE6FE, borde #CEC6D8.
Oscuro: canvas #171421, superficie #242033, texto #F7F3FF, violeta #A68AFF.
Space Grotesk 700 (títulos) y DM Sans (cuerpo). Radios 12/20/28 px.
Texto sobre lima o coral: siempre #242136. Botón principal claro: fondo #7950F2,
texto #FFFFFF. Logotipo: los SVG de soycerobytes/miminiapp/public/brand/, sin redibujar.

ENCUADRE (confirma con mi captura con rejilla; estos son los valores medidos en
el ensayo del 2026-11-12)
Cabeza aprox. x 380–880, y 380–990 (barbilla ≈ 990). Me muevo de lado a lado:
el centro de la cara va de x≈390 a x≈690. Manos y torso desde y≈1000.
Zonas de la red (no poner nada informativo): arriba 250 px, abajo 500 px,
izquierda 70 px, derecha 140 px.
ZONAS DE COLOCACIÓN (en px de 1080×1920):
  Z-TOP    y 250–370, x 70–940: una línea corta sobre la cabeza.
  Z-ESQ    x 70–300, y 250–420: objeto pequeño a la izquierda de la cabeza.
  Z-SUB    y 1060–1180: subtítulos. Siempre visibles. Nada los tapa.
  Z-TARJETA y 1200–1420, x 70–940: tarjetas, ancladas ABAJO (y=1420) y que
           crecen hacia arriba sin pasar de y=1200.
Nada cruza la barbilla (y 990) ni los ojos. Comprueba en la captura con rejilla
y verifica en el fotograma donde más me muevo.

MOVIMIENTO
Entrada: 350–500 ms, cubic-bezier(0.22, 1, 0.36, 1). Salida: 250 ms.
Firma de movimiento: cortes y barridos DIAGONALES con la inclinación de la barra
(≈29° respecto a la vertical), no cortes rectos. Resorte (spring) solo en sello,
chips e interruptor. Un foco animado por plano, máximo dos. Escalonado entre
elementos: 60–120 ms. Sin parpadeos, sin glitch, sin zoom rotatorio, sin barra
de progreso ni destellos blancos. Cada animación tiene una función: orientar,
señalar un cambio o confirmar un resultado.

CONTENIDO
- Texto exacto entre comillas, tal cual. No lo reescribas ni lo traduzcas.
- Ninguna tarjeta repite lo que digo en ese segundo: aporta contraste,
  consecuencia o un dato derivado.
- No inventes cifras, fechas, tarifas ni funciones de la app.
- Si falta un dato, pregunta. No rellenes.

SINCRONÍA
Ancla cada pieza a la PALABRA que se dice en mi transcript (te doy el criterio
semántico en cada pieza). Los tiempos salen del transcript, no de segundos fijos.
Si la frase cambia, recalcula.

PROCESO (obligatorio)
1. Lee el transcript y mi captura con rejilla; mide el encuadre y dime las zonas.
2. Propón, para cada pieza, 3 fotogramas: antes, durante, después. NO renderices.
3. Espera mi OK. Aplica los cambios que pida (máximo dos rondas).
4. Render. Verifica con ffprobe y con 3 recortes a resolución nativa.

NO HAGAS
Cajas opacas sobre mi cara, sombras duras o difusas que ensucien el fondo, más
de un énfasis por plano, tarjetas de cierre, corrección de color sobre mi toma,
aceleración del video, datos inventados, degradados ni resplandores.

ENTREGA
Un archivo por pieza (nombre estable MG-0X_vNN) o la composición completa, más
los fotogramas de revisión en media/trabajo/qa/.
```

### 4.4 Prompts por pieza

Cada uno asume el prompt maestro ya pegado. Las **anclas** dicen en qué momento semántico entra la pieza; Claude busca el tiempo exacto en el transcript.

#### SUB-01 · Subtítulos por frases (siempre)

```
PIEZA: SUB-01 · Subtítulos por frases. Nivel A, B y C.
OBJETIVO: que se lea la frase completa de un vistazo y que la palabra que suena
se sienta viva, sin distraer de mi cara.
INSUMO: transcript con tiempos por palabra, ya corregido ("cerobytes" en
minúsculas, "Plan B", "MiMiniApp").
REGLAS
- Divide por FRASES con sentido (nunca mezcles dos frases en una página),
  normalmente 2 a 5 palabras, UNA sola línea, ancho máximo 850 px.
- Plus Jakarta Sans Bold 700, MAYÚSCULAS salvo marcas (cerobytes, MiMiniApp). Tamaño
  automático: 80 px sobre cámara, 64 px sobre pantalla completa; baja el tamaño si no cabe.
- Color: texto #F5F6F8 con contorno de 3 px #0B0B0D al 70 % sobre cámara (sin
  contorno sobre fondo plano). La palabra que suena va invertida: caja #F5F6F8
  (radio 12 px, relleno de 14 px a los lados) con texto #0B0B0D y escala 1,04; la
  caja pasa de palabra en palabra en 120 ms. Palabras aún no dichas, a 55 % de
  opacidad. Sin colores de resalte.
- Posición: centro de Z-SUB (y≈1110) sobre cámara; y≈1345 sobre pantalla completa.
- Entrada: 0,18 s. Sin animación de salida. Se queda hasta que entra la siguiente.
- Los subtítulos NUNCA se ocultan por una tarjeta: las tarjetas se colocan fuera de Z-SUB.
- Revisa eñes, tildes, ¿? ¡! y que no se parta una palabra.
ACEPTACIÓN: 3 fotogramas (inicio, mitad, final) donde se lea sin esfuerzo y
no se pise barbilla ni tarjetas.
```

#### MG-01 · Hoja de calendario del gancho (Nivel C)

```
PIEZA: MG-01 · Hoja de calendario junto a la cabeza. Sobre cámara, ZONA Z-ESQ.
ANCLA: la primera vez que digo "febrero" (entra); la frase de calma o "todavía
no" (regresa a enero).
OBJETIVO: dar el contexto del tiempo sin palabras. Ojo: es una metáfora gráfica
del video, no la interfaz de la app.
DISEÑO: hoja de 228×176 px en x 72, y 250. Fondo #F5F6F8, esquinas 18 px, cabecera
de 46 px en #0D213F con dos anillas #F5F6F8. Mes en Plus Jakarta Sans ExtraBold 800, 42 px,
#0B0B0D: "ENERO" y "FEBRERO". Sin sombra difusa: borde de 2 px #0B0B0D al 15 %.
ANIMACIÓN: entra desde arriba con resorte (rotación inicial −20°, final −6°).
En "febrero": la hoja ENERO gira sobre su borde superior (rotateX 0 → −112°) en
10 frames, ease-in, revelando FEBRERO. En el momento de "abandonaste": hoja y
mi imagen se apagan juntas (grayscale 0 → 1 y brillo −18 % en 8 frames). En
"todavía no": la hoja gira de vuelta a ENERO y todo recupera el color en 8 frames.
Sale con un fundido de 0,3 s antes de que termine el beat 2.
SONIDO: whoosh corto en el giro; golpe grave corto al apagarse.
NO: tapar la cabeza (comprueba el fotograma donde giro a la izquierda).
ACEPTACIÓN: fotogramas en ENERO, FEBRERO apagado y ENERO de vuelta.
```

#### MG-02 · Rótulo de presentación (Nivel A, B, C)

```
PIEZA: MG-02 · Rótulo "Plan B · para tu propósito". Sobre cámara, Z-TARJETA
(esquina izquierda, x 70, borde inferior en y=1400).
ANCLA: cuando nombro "Plan B" por primera vez. Dura unos 2,3 s.
OBJETIVO: poner nombre a la herramienta y marcar que es la primera de la serie.
BASE: marca/kit/svg/rotulo-inferior-video-9x16-ajustado.svg (bloque #0D213F al 95 %,
radio 18 px, símbolo "/" blanco roto a la izquierda, título Bold y una línea
secundaria en mayúsculas con tracking). Es el rótulo del kit v1.2 desplazado 100 px:
caja en y 1230–1400, sin pisar los subtítulos (y 1060–1180) y dentro del límite de
la red (y=1420). Si lo reconstruyes en código, respeta esas medidas.
ESTRUCTURA
1) Título: "Plan B" en Plus Jakarta Sans Bold 700, 58 px, #F5F6F8, seguido de " · para tu
   propósito" en Plus Jakarta Sans Medium 500, 32 px, #B7C0CC. A la izquierda, el símbolo "/"
   (isotipo-blanco.svg) de ~100 px de alto.
2) Línea secundaria: "MINIAPP N.º 1" (si decido prometer el reto: "MINIAPP N.º 1 ·
   CADA SEMANA"), Plus Jakarta Sans Medium 500, 26 px, tracking 0,12 em, #B7C0CC.
ANIMACIÓN: barrido DIAGONAL (≈29° respecto a la vertical) de izquierda a derecha
en 0,4 s que revela el bloque; el símbolo entra primero (0,2 s). Sale en 0,3 s con
el mismo barrido en sentido inverso.
SONIDO: pop suave al aparecer.
NO: tapar manos importantes ni los subtítulos (quedan en Z-SUB, y 1060–1180).
ACEPTACIÓN: se lee "Plan B · para tu propósito" completo, sin salir de x 70–940
ni pasar de y=1420, y no pisa la banda de subtítulos.
```

#### MG-03 · Tarjeta «de dónde sale el dato» (Nivel B, C)

```
PIEZA: MG-03 · Tarjeta de fuente. Sobre cámara, Z-TARJETA.
ANCLA: cuando digo que a mediados de enero mucha gente ya abandonó su propósito.
OBJETIVO: dar credibilidad. La voz dice el dato; la tarjeta dice DE DÓNDE sale
(no repite la frase).
TEXTO (exacto)
  Kicker: "DE DÓNDE SALE EL DATO"
  Línea 1: "Actividad en Strava"
  Línea 2: "El día exacto cambia cada año"
DISEÑO: panel estándar de la marca del video: fondo #0D213F al 95 %, radio 18 px,
borde fino #F5F6F8 al 20 %. Kicker Plus Jakarta Sans Bold 700, 26 px, tracking 0,2 em,
#B7C0CC, con el símbolo "/" de 26 px a su izquierda. Línea 1 Plus Jakarta Sans Bold 700,
42 px, #F5F6F8. Línea 2 Plus Jakarta Sans Medium 500, 34 px, #B7C0CC. Ancho 870 px,
anclado abajo en y=1420.
ANIMACIÓN: el panel entra con barrido diagonal (≈29° respecto a la vertical) en
0,4 s; las dos líneas entran escalonadas (120 ms) con 34 px de desplazamiento
desde la izquierda. Sale en 0,25 s. Dura ~3 s.
SONIDO: ninguno.
NO: poner cifras ni el nombre de una fecha exacta.
ACEPTACIÓN: no cruza y=1200 ni la barbilla; la línea 2 se lee sin esfuerzo.
```

#### MG-04 · Tarjeta «lo que no te pide» con modo avión (Nivel B, C)

```
PIEZA: MG-04 · Tarjeta de prueba. Sobre cámara, Z-TARJETA.
ANCLA: entra cuando digo "gratis"; el interruptor se enciende cuando digo "modo avión".
OBJETIVO: resumir de un vistazo lo que la herramienta NO pide y dejar claro el
modo avión como prueba. No repite la voz: la resume visualmente.
TEXTO (exacto)
  Kicker: "LO QUE NO TE PIDE"
  Chips: "PAGO" · "CUENTA"
  Fila: icono de avión + "MODO AVIÓN" + interruptor
  Nota pequeña bajo la fila, Plus Jakarta Sans Medium 500, 24 px, #B7C0CC: "Con la página ya cargada"
DISEÑO: panel estándar (fondo #0D213F al 95 %, radio 18 px, borde fino #F5F6F8 al
20 %). Kicker como en MG-03. Chips: borde 2 px #F5F6F8, texto #F5F6F8, Plus Jakarta Sans
Bold 700, 30 px, radio 12 px. Interruptor 96×52 px, radio 26 px: apagado = borde
#F5F6F8 y pomo #F5F6F8; encendido = relleno #F5F6F8 y pomo #0D213F con una marca
de verificación.
ANIMACIÓN: los chips entran escalonados con resorte (escala 0,7 → 1); la fila
sube con 24 px de desplazamiento. En "modo avión" el pomo recorre el interruptor
(resorte) y el fondo pasa a #F5F6F8; el icono pasa de #B7C0CC a #F5F6F8.
SONIDO: clic seco del interruptor.
NO: añadir un chip "INTERNET" sin la nota (no es verdad en general), ni la
palabra "siempre".
ACEPTACIÓN: interruptor apagado antes, en movimiento durante y encendido después.
```

#### MG-05 · Acento final «Este febrero, no.» (Nivel A, B, C)

```
PIEZA: MG-05 · Acento de cierre sobre la cabeza. Sobre cámara, Z-TOP (y 250–370).
ANCLA: cuando digo "antes de que llegue febrero" (empieza) hasta el final del video.
OBJETIVO: dejar una frase para recordar. Es el ÚNICO énfasis grande del video.
TEXTO (exacto): "Este febrero, " + "no."
DISEÑO: "Este febrero," en Plus Jakarta Sans Bold 700, 72 px, #F5F6F8, con contorno de 3 px
#0B0B0D al 70 %. "no." en Plus Jakarta Sans ExtraBold 800, 120 px, #0B0B0D dentro de una caja
#F5F6F8 (radio 14 px, relleno de 18 px). Centrado entre x 70 y 940. Toda la altura
cabe en y 250–370 (no entrar en la zona de la red).
ANIMACIÓN: "Este febrero," se revela con barrido diagonal (≈29° respecto a la
vertical) de izquierda a derecha en 0,55 s; la caja de "no." cae con resorte
(escala 0,3 → 1) 0,35 s después. Se queda hasta el final.
SONIDO: ding suave en "no.".
NO: combinar con otro texto en Z-TOP; tapar el pelo.
ACEPTACIÓN: se lee en una mirada y no invade y<250 ni toca la cabeza.
```

#### MG-06 · Demo de Plan B, pasos 1 a 3 (pantalla completa, Nivel B, C)

```
PIEZA: MG-06 · Maqueta de la app, pasos 1 a 3. PANTALLA COMPLETA (mi cara no sale;
mi voz sigue). Es una MAQUETA: rotula "MAQUETA DE ENSAYO" arriba, centrada, hasta
que la app esté publicada. Con la app publicada, sustituye la maqueta por mi
grabación y usa esta pieza solo para marco, cámara virtual y resaltes.
ANCLA: entra cuando empiezo a explicar el recorrido ("escribes tu propósito")
y sale cuando hablo del recordatorio o el calendario.
FUENTE DE VERDAD: soycerobytes/miminiapp/docs/product-specs/plan-b.md (ficha
v06). No inventes pantallas ni funciones que no estén ahí.
FONDO: plano #0D213F (azul marino de cerobytes), sin degradados ni resplandores.
Una barra diagonal gigante (marca/kit/svg/isotipo-blanco.svg) al 6 % de opacidad,
fija, a la derecha. El fondo no cambia cuando la app pasa a gris.
CELULAR: marco genérico sin marcas, 550×950 px, centrado, esquinas 64 px, borde
2 px #F5F6F8 al 20 %, fondo #1E2937. Pantalla con la app en TEMA CLARO
(canvas #F7F5F0). Subtítulos debajo en y≈1345 con velo.
PASO 1 (ancla: "escribes tu propósito")
  Cabecera "Paso 1 de 3". Pregunta (variante de enero): "¿Qué quieres lograr este año?".
  Se teclea "Hacer ejercicio 3 veces por semana" en el campo (borde violeta #7950F2).
  Debajo, seis sugerencias en chips: Hacer ejercicio · Leer más · Ahorrar ·
  Aprender un idioma · Dormir mejor · Usar menos el móvil. Botón "Siguiente"
  (violeta, texto blanco).
SALTO (ancla: "te lleva a febrero")
  La etiqueta de mes cambia de "enero" a "febrero". La pantalla pasa a gris en
  600 ms (grayscale 0 → 100 %, un poco más oscura y fría). Cámara virtual: zoom
  1,10× hacia la etiqueta de mes y regreso en 0,6 s.
PASO 2 (ancla: "eliges por qué…")
  Pregunta (texto de la ficha v06): "Imagina que es 1 de febrero y lo has dejado. ¿Qué ha pasado?".
  Seis botones en dos columnas: No tuve tiempo · Perdí las ganas · Algo se
  cruzó · Era demasiado · Se me olvidó · Otra cosa. Entran escalonados con resorte
  (120 ms entre cada uno). Un toque (círculo semitransparente + anillo) en
  "No tuve tiempo": el botón se oprime y el paso avanza solo.
PASO 3 (ancla: "armas tu plan" y el ejemplo)
  Título "Tu plan para ese día". Etiquetas "Si" y "entonces". Se escriben
  "llego a casa después de las 20:00" y "hago 5 minutos de estiramientos antes de
  sentarme en el sofá". Los dos huecos laten suavemente mientras esperan texto.
  Gris: 100 % → 50 % al completar el primer hueco → 0 % (color completo) al
  completar el segundo. Botón "Ver mi plan".
CÁMARA VIRTUAL: zoom 1,06× sobre el campo activo, interpolación ease-in-out.
SONIDO: whoosh al entrar el celular; tecleo suave; toque; la música baja al gris
y recupera al volver el color.
NO: datos personales, logos de terceros, marcas de celulares reales.
ACEPTACIÓN: 3 fotogramas por paso; el gris se aprecia en 100 %, 50 % y 0 %; el
texto del paso 3 cabe sin partirse.
```

#### MG-07 · Resultado: sello, calendario y fondo de pantalla (pantalla completa, Nivel B, C)

```
PIEZA: MG-07 · Resultado de la app. PANTALLA COMPLETA, continúa a MG-06 sin
corte (mismo celular, misma cámara virtual).
ANCLA: sello al decir "al final"; calendario al decir "recordatorio" o
"calendario"; fondo de pantalla al decir "fondo de pantalla".
FUENTE DE VERDAD: ficha v06 de Plan B (soycerobytes/miminiapp).
SELLO (la ficha v06 fija −6°, escala 1,4 → 1 en 300 ms y no tapar el texto; los colores son propuesta mía): "Este febrero, no." en Space Grotesk 700 sobre lima #B9F65A con texto
#242136, borde 4 px #242136, rotación −6°. Cae con escala 1,4 → 1 en 300 ms. Sacudida
corta del celular (amplitud 9 px, decae en ~0,3 s) y 1 s de silencio musical.
NO tapar la frase del plan.
RESULTADO: frase grande "Si llego a casa después de las 20:00, entonces hago 5 minutos
de estiramientos antes de sentarme en el sofá." y debajo, pequeño, "Tu propósito:
Hacer ejercicio 3 veces por semana". Color vuelve completo.
CALENDARIO: tarjeta "Añadir a mi calendario" (texto de la ficha v06) con título del evento "Plan B: hago
5 minutos de estiramientos antes de sentarme en el sofá", resumen "De lunes a viernes
a las 20:00, durante 4 semanas" y una cuadrícula de 4 semanas × 7 días donde se
marcan en lima las 20 apariciones (lunes a viernes), una a una, 40 ms entre
celdas. Sonido: ding.
FONDO DE PANTALLA: el celular se transforma (mismo elemento, escala y fundido) en
una pantalla de bloqueo oscura con reloj grande (19:58) y la frase del plan
centrada entre el 32 % y el 72 % de la altura, márgenes laterales del 10 %,
etiqueta pequeña "Mi plan B" encima, SIN logotipo ni dirección. Tema: oscuro
(#171421, texto #F7F3FF). Un brillo diagonal lo recorre una vez.
DURACIÓN: ~4,5 s en total. Sale con deslizamiento hacia abajo y vuelve mi cámara.
NO: prometer la hora del aviso; mostrar datos personales.
ACEPTACIÓN: sello legible, 20 celdas marcadas, frase del fondo dentro de la franja.
```

#### MG-08 · Firma MiMiniApp: la M que se ensambla (Nivel C)

```
PIEZA: MG-08 · Firma de marca del producto. PANTALLA COMPLETA, ~2,3 s.
ANCLA: transición entre el beat 3 (solución) y el beat 4 (demo).
OBJETIVO: dar identidad al producto con su propio gesto, sin hablar.
RECURSO: soycerobytes/miminiapp/public/brand/wordmark-editorial-dark.svg (usar
el archivo tal cual; no redibujar la M ni cambiar sus piezas).
FONDO: #171421 (canvas oscuro del producto).
ANIMACIÓN (valores de docs/design-docs/creative-playground.md):
  Las 4 piezas de la M entran desde fuera y se ensamblan. Duración 1450 ms por
  pieza, retraso i × 70 ms, curva cubic-bezier(0.2, 0.65, 0.25, 1). Desplazamientos
  y giros iniciales (unidades del viewBox):
    asta izquierda   dx −90,  dy −84,1  giro −60,8°
    diagonal izq.    dx  51,  dy −133,4 giro  83,2°
    diagonal der.    dx −45,  dy  124,7 giro −73,6°
    asta derecha     dx 135,  dy   50,75 giro 54,4°
  Pasa por el 64 % del recorrido con ×0,13 del vector y ×0,12 del giro, con un
  pequeño sobrepaso alterno (±2 unidades y ±1,7°) al 84 % y encaje exacto al 100 %.
  Después aparecen las letras "iMiniApp" con fundido breve y se quedan 0,6 s.
  Escala: el wordmark ocupa ~70 % del ancho, centrado en y≈960.
SONIDO: cuatro "clics" suaves, uno por pieza, y un ding al final.
NO: sustituir el ensamblaje por un fundido de opacidad (lo prohíbe su propio
contrato de marca) ni mezclar con la paleta de cerobytes (aquí manda la marca del producto).
ACEPTACIÓN: fotogramas con las piezas separadas, a mitad de camino y ensambladas.
```

---


## 5. Pendientes y decisiones tuyas

1. **El reto:** cuánto prometer («cada semana, mientras pueda» frente a «un año») y si el chip de MG-02 lleva «CADA SEMANA».
2. ~~Textos de la app en español latinoamericano~~ **Resuelto (2026-11-16):** se quedan como están. La maqueta usa los de la ficha v06.
3. ~~Dos fichas de Plan B~~ **Resuelto (2026-11-16, PROD-17):** la fuente de verdad es la más reciente, `docs/product-specs/plan-b.md` en `soycerobytes/miminiapp`. Este documento ya la sigue.
4. **Firma sonora:** no existe y no hace falta para empezar. El logo ya existe en el kit v1.1 (`marca/kit/`), pero es una reconstrucción, no el maestro. Los efectos son sonidos reales (AV-008); la música, con licencia clara.
5. **Proceso:** si te sirve este formato, se formaliza en el marco (plantilla del guion con beats, ficha de montaje por video generada del transcript, ajustes al validador y a las pruebas). Hoy esto es un documento aparte que no toca `GUION.md`.
6. **Antes del video real:** app publicada, grabación real de la demo y modo avión, y prueba del `.ics` en Android y iPhone.
7. **Rehacer el corto del ensayo con la identidad v2.** El v3 usa la paleta anterior (cian y violeta) y no debe publicarse.
8. ~~Satoshi~~ **Resuelto (2026-11-16, AV-007):** Plus Jakarta Sans (OFL), incluida en `marca/fuentes/`. Pendiente: confirmar los pesos (propuestos: 500, 700 y 800).
9. **Azul de la barra:** definir su valor exacto. Hoy el kit usa `#003571` como referencia provisional, solo en los archivos `*-azul-referencia`.
10. **Wordmark:** es una reconstrucción. Aprobarlo como maestro exige revisar curvas, espaciado, tamaños pequeños y criterios ópticos.
