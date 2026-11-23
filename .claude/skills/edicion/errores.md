# Errores que ya se cometieron (y cómo se evitan)

Cada fila es una corrección real de Ale o un fallo técnico de las sesiones del 2026-11-17 al 2026-11-20 (VID-0002 y VID-0003). Si aparece uno nuevo, se añade aquí con su regla.

## Lo que Ale corrigió

| Fallo | Regla |
|---|---|
| Corte a mitad de palabra («te pasaste de recorte») | Cortes solo dentro de silencios medidos (< −55 dB, 10 ms) |
| Zooms de la demo «muy sencillos», trozos ilegibles | Encuadres por grupo de interfaz, escala ≥ 0,8 para leer, la app real en un celular |
| Sonidos sintéticos o de Freesound «horribles» | Solo sonidos reales del banco de Pixabay de Ale (AV-008, AV-011) |
| Apertura en frío: «una foto de fondo y música alta, sin contexto» | El vídeo empieza con la voz y la cara; nada antes de la primera palabra |
| B-roll de 1,2 s: «no alcanzo a entender el contexto» | Un recurso que cuenta algo dura ≈ 1,6–2 s y cubre la frase |
| Empezar con un B-roll a pantalla completa | En una serie con cara, la primera frase con recurso va como tarjeta en el pecho |
| La tarjeta tapaba la boca | Tarjeta de 400 px desde y = 1000, comprobada en varios fotogramas |
| Flecha flotando sin su tarjeta | Las flechas terminan, como tarde, cuando se va su primera tarjeta (`showEnd`) |
| «Corte abrupto» donde no había corte (nuevo / calma) | La deriva de cámara solo se reinicia en cortes reales (`SHOTS`) |
| «Plan B» solapado con «MINIAPP 01» | Cada protagonista tiene su zona; las píldoras no comparten altura con él |
| Un gesto de manos sin aprovechar | Si Ale hace un gesto, la palabra nace del gesto (máscara medida fotograma a fotograma, `REV`) |
| Filtro «bastante notorio y fuerte» (look B en el set nuevo) | Color medido; por defecto, sin filtro ni viñeta (v03 de VID-0003) |
| Gancho «Imagina: es febrero» para el 1 de enero | El gancho tiene que funcionar el día en que se publica (GUIONES §3 bis) |
| «Propósito» cuando Ale se pone «metas» | La confesión usa las palabras de Ale |
| Guion sin la intención de cada frase | Cada guion lleva su GUION_BEATS (intención, energía, pausas, énfasis) |
| Cortes «atropellados»: 0,15–0,27 s entre frases (VID-0003 v06 de la otra sesión) | 0,30–0,50 s de respiración entre frases (§3) |
| «Cuando se abría la aplicación se hacía como una bajada de volumen» | La demo iba sobre el valle de la pista (−5 dB): tramos de energía pareja para las partes largas |
| «No tiene la música de fondo» (13 dB bajo la voz + 5 de bajada) | Música ≈ 9 dB bajo la voz mientras hablas (`MUS_DB` 6, bajada ≈ 3 dB) |
| «Suena el boom sin nada de contexto» | Cada efecto con algo que se ve; golpes de cine solo para un protagonista con imagen fuerte |
| «No suena el efecto del teclado» | Sonidos continuos por su inicio, durante toda la acción y a −15 dBFS |
| Look B «muy notorio» (otra vez, en la v06) | Sin filtro por defecto; Ale eligió además, en una comparación, una coloración muy suave (`eq` contraste 1,04, gamma 1,03): solo si la pide |
| Texto y motion «bastante planos» frente a un reel de referencia | Dirección v2 (MOTION §10): tres niveles de texto, vocabulario de entradas y salidas, auditoría de dinamismo |
| Mezclar el violeta y el lima de MiMiniApp con la marca cerobytes | Paleta Señal de cerobytes (AV-014); los colores del producto, solo dentro del celular |
| Letras «planas en imagen» | Sombra sutil de dos capas en todo texto sobre imagen (`--sombra`) |
| Animaciones que «no son tan wow» | Laboratorio de tratamientos con letra para elegir (`hyperframes/lab_texto/`) antes de pasarlos a la base |

## Lo que encontró la autocrítica de Claude

| Fallo | Regla |
|---|---|
| Subtítulos sobre el estampado rojo de la camiseta | Subtítulos siempre en caja navy |
| Subtítulos y textos bajo la interfaz de TikTok / Reels | Zona segura: ≥ 168 px arriba, ≤ 1540 px abajo, 120 px libres a la derecha |
| Dos frases en una línea de subtítulos («TENGO POR ESO HICE») | Los grupos cortan siempre en «.», «?», «!» |
| «Este febrero, no.» cuando la voz dice «no las dejo en enero» | El texto en pantalla no contradice la voz: «Este año, sí.» |
| 10 toques sonoros en 12 s de demo | ≈ 4 toques con sonido (los que cambian algo) |
| El pico 2 (sin voz) sonaba a −20 LUFS | Medir la sonoridad momentánea de cada pico; subir la música donde no hay voz |
| Primer fotograma mirando abajo | Acercamiento de arranque; y en el rodaje, mirar al lente 1 s antes de hablar |

## Fallos técnicos

| Fallo | Solución |
|---|---|
| `setViewport(deviceScaleFactor)` en chrome-headless-shell captura a 393 px | Lanzar Chrome con `--force-device-scale-factor=2.748 --window-size=393,852` y `defaultViewport: null` |
| El screencast de puppeteer graba en puntos (393 px) | Captura fotograma a fotograma con `Page.captureScreenshot` |
| El tiempo virtual de CDP cuelga Chrome al cambiar de paso | Stop motion con `Animation.setPlaybackRate` ajustado cada 30 fotogramas |
| Clics de CDP colgados o recuadros de foco en los títulos | Toques desde la página (`click()`, setter nativo + evento `input`) y un toque real al principio |
| El `scrollIntoView` suave de la app daba saltos | Se anula y los desplazamientos los hace la grabación, recalculando el destino cada fotograma |
| La app decía «1 de diciembre» en noviembre | Fecha emulada en el mes de publicación (el reloj sigue corriendo) |
| Pantalla del celular vacía al encogerse | Alargar la grabación con su último fotograma (`tpad`) |
| Comentario `//` en una función de una línea rompió el script | Comentarios al final de la línea completa; `lint` tras cada cambio |
| Vídeos creados por JS no se renderizan | Todo `<video>` con `id`, `data-start`, `data-duration` y `data-track-index` escrito en el HTML |
| `.cube`, enlaces a `videos/…` en el CHANGELOG rompían las pruebas | En el CHANGELOG, rutas como código, no como enlace |
| Tabla de 5 columnas dentro de «## Escenas» rompía el validador | Listas en viñetas dentro de las secciones con tablas fijas del GUION |
