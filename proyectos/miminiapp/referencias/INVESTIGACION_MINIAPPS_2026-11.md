# Miniapps con potencial viral: análisis de mercado

**Fecha:** 2026-11-12 · **Autor:** Claude, a petición de Ale · **Estado:** investigación para elegir la primera miniapp (PROD-14). No es una decisión.

**Límite técnico de partida:** web estática y `localStorage`, sin cuentas, sin backend y sin API de terceros (PROD-04 a PROD-07 del [dossier](MiMiniApp_Inicio_Proyecto_Harness_IA_v1.2.md)).

**Sobre las cifras:** casi todas son estimaciones de terceros (Semrush, Ahrefs) o datos que dan los propios creadores a la prensa. Sirven para ver órdenes de magnitud, no para citarlas en un vídeo sin su fuente. Si alguna sale en un guion, va a Claims como tipo E con enlace y fecha.

## 1. Casos que funcionaron y por qué

| Caso | Qué es | Señal de éxito (fuente) | ¿Cabe en estático? | Mecanismo |
|---|---|---|---|---|
| Wordle (2021) | Una palabra al día, seis intentos | Pasó de 90 jugadores el 1 de noviembre a 300.000 a mediados de enero; el NYT lo compró por una cifra «de siete cifras bajas» ([NBC](https://www.nbcnewyork.com/news/business/money-report/the-new-york-times-is-buying-wordle-the-game-that-exploded-in-popularity-this-month/)) | Sí | Resultado compartible sin spoiler (la cuadrícula de colores) y cita diaria |
| ismy.blue (2024) | Etiquetas tonos como azul o verde y ves dónde está tu frontera | Más de 1,5 millones de visitas en un mes ([IFLScience](https://www.iflscience.com/is-my-blue-your-blue-simple-test-of-blueness-and-greenness-goes-viral-75817)) | Sí la prueba; la comparación con otros necesita datos reunidos | Discusión entre personas: «¿tu azul es mi azul?» |
| The Password Game (2023) | Reglas de contraseña cada vez más absurdas | Más de un millón de visitas tras el lanzamiento; más de diez millones de partidas ([Wikipedia](https://en.wikipedia.org/wiki/The_Password_Game)) | Sí | Sátira de una molestia que todos conocen y que escala |
| Draw a Perfect Circle (neal.fun) | Dibuja un círculo a mano y te puntúa de 0 a 100 % | Muy difundido en TikTok; la puntuación se comparte ([Mental Floss](https://www.mentalfloss.com/fun/games/this-online-tool-proves-that-drawing-a-perfect-circle-is-harder-than-it-looks)) | Sí | Reto de 5 segundos, número claro y ganas de repetir |
| Dialed.gg | Recordar un color y recrearlo con deslizadores | Difusión por clips de streamers en TikTok; cifras solo de la propia web ([dialedgg.com](https://dialedgg.com/)) | Sí | Reto de percepción; el fallo es gracioso de ver |
| Receiptify (2020) | Tus canciones más escuchadas como ticket de compra | Más de un millón de usos en sus primeros meses ([STUDIO for Creative Inquiry](https://studioforcreativeinquiry.org/?p=15552)) | **No**: necesita la API de Spotify con inicio de sesión | Estética reconocible (ticket) con datos tuyos |
| Instafest (2022) | Cartel de festival con tus artistas | Más de 5 millones de carteles en pocos días, según una sola fuente ([RouteNote](https://routenote.com/blog/instafest/)) | **No**: misma dependencia de Spotify | Tarjeta de identidad lista para stories |
| Brat generator (2024) | Texto con la estética de la portada de un álbum | Miles de parodias del cuadro verde ([meme.com](https://meme.com/memes/brat-summer)) | Sí | Plantilla visual que cada uno rellena con su chiste |
| neal.fun | Colección de juguetes web de un solo autor | Vive de la publicidad; más de 30 proyectos ([Wikipedia](https://en.wikipedia.org/wiki/Neal_Agarwal)) | Sí, la mayoría | Una idea por página y una visualización que cambia la perspectiva |
| Human Benchmark | Test de reflejos y memoria | Unos 2–3 millones de visitas al mes; «reaction time test», unas 190.000 búsquedas mensuales (estimaciones de [Semrush](https://www.semrush.com/website/humanbenchmark.com/overview/)) | Sí, sin ranking global | Demanda de búsqueda estable, no solo moda |
| Calculadoras (calculator.net) | Utilidades de cálculo | Unos 27 millones de visitas en junio de 2025 (estimación de [Ahrefs](https://ahrefs.com/top/calculator.net)) | Sí | Tráfico de búsqueda; poco gancho en redes por sí solas |

## 2. Patrones que se repiten

1. **Un resultado personal y comparable.** Un número, un porcentaje o una tarjeta que dice algo de ti: Wordle, el círculo, el azul, Receiptify. Es lo que la gente comparte.
2. **Un reto que se entiende en un segundo.** Sin instrucciones: «dibuja un círculo», «¿azul o verde?». Funciona igual en un vídeo vertical que en la web.
3. **El fallo es parte del entretenimiento.** Ver a alguien sacar un 61 % o equivocarse de color engancha más que el acierto. Para nuestros vídeos, la reacción de Ale a cámara *es* la demostración.
4. **Una estética reconocible.** Ticket, cartel o cuadrícula de colores: el resultado se identifica en el feed sin leer nada.
5. **Una molestia compartida, convertida en juego.** Contraseñas, suscripciones, reuniones.
6. **Una visualización que cambia la perspectiva** (neal.fun, «Your Life in Weeks» de Wait But Why): el dato ya existía, la forma de verlo es lo nuevo.

**Lo que no cabe en estático y conviene evitar al principio:** rankings mundiales o «comparación con el resto» con datos reales (necesitan servidor), todo lo que use cuentas de Spotify u otras plataformas, multijugador y cualquier cosa con IA en un servidor.

**Lo que sí cabe:** puntuación y racha en `localStorage`, tarjeta de resultado generada con `canvas` para descargar o compartir, texto compartible estilo Wordle y enlaces que llevan la configuración en la URL (`#…`), que no llega a ningún servidor.

**No copiamos.** Los patrones son de todos, pero los juegos concretos (Wordle, el círculo perfecto, Dialed, The Password Game) no se recrean. Cada miniapp necesita una pregunta propia.

## 3. Candidatas

Puntuación de 0 a 2 en cinco criterios (10 en total):

- **Gancho:** se entiende en 1–3 s sin contexto.
- **Compartible:** da un resultado personal en tarjeta, número o enlace.
- **Viable:** cabe en estático con `localStorage` y en unas 6 h, incluidos ES/EN y pruebas. La primera, además, arrastra la plataforma.
- **Vuelve:** utilidad o ganas de repetir después del vídeo.
- **Verdad:** no depende de datos dudosos ni copia un juego existente.

| # | Miniapp (nombre provisional) | Qué hace | Gancho para el vídeo | Patrón | G | C | V | Vu | Ve | Total |
|---|---|---|---|---|---|---|---|---|---|---|
| N1 | **¿Cuánto dura tu minuto?** | Pulsas empezar, la pantalla se oculta y paras cuando crees que ha pasado un minuto. Te dice cuánto ha durado de verdad | «Mi minuto dura 47 segundos. ¿Y el tuyo?» | 1, 2, 3 | 2 | 2 | 2 | 1 | 2 | **9** |
| N2 | **Tus 10.000 días** | Con tu fecha de nacimiento, te dice cuántos días llevas vivo, qué día cumpliste o cumplirás 10.000, 15.000 o 20.000, y lo pone en una tarjeta | «Hay un día en el que cumples 10.000 días. El mío es…» | 1, 6 | 2 | 2 | 2 | 1 | 2 | **9** |
| N3 | **El ticket de tus suscripciones** | Suscripciones y sueldo por hora en un ticket: total al año y horas de trabajo que cuesta. Evoluciona la idea anterior con la estética del patrón 4 | «Mi ticket de suscripciones: 31 h de trabajo al año» (número de ejemplo) | 1, 4, 5 | 2 | 2 | 2 | 1 | 2 | **9** |
| N4 | **Amigo invisible sin registro** | Metes los nombres y las exclusiones (parejas), y sale un enlace por persona que solo revela a quién le toca. Nada pasa por un servidor: el reparto va en el `#` del enlace | «Amigo invisible en 30 segundos, sin apps ni correos» | 5 | 2 | 2 | 1 | 2 | 2 | **9** |
| N5 | Ruleta justa de tareas (lista anterior) | Reparte tareas de casa sin repetir persona y recuerda el historial | «¿Quién friega hoy?» | 3, 5 | 2 | 1 | 1 | 2 | 2 | **8** |
| N6 | **Dibuja tu país de memoria** | Dibujas el contorno de España (o del país que elijas) y se superpone al real con un porcentaje de acierto. Contornos de [Natural Earth](https://www.naturalearthdata.com/), de dominio público | «Nadie dibuja bien Galicia» | 1, 2, 3 | 2 | 2 | 1 | 1 | 2 | **8** |
| N7 | **¿Cuántos veranos te quedan?** | Tu vida en semanas, veranos o Navidades según la esperanza de vida del INE, con las que ya has vivido marcadas | «Me quedan unos 50 veranos. Así se ven» | 1, 6 | 2 | 2 | 2 | 1 | 1 | **8** |
| N8 | ¿Cuánto cuesta esta reunión? (lista anterior) | Contador en euros que sube en directo | El contador subiendo mientras alguien habla | 5 | 2 | 1 | 2 | 1 | 2 | **8** |
| N9 | **Lo que valía tu dinero** | 100 € de un año pasado en euros de hoy, con la serie del IPC del INE | «Con 100 € de 2010 hoy compras…» | 6 | 2 | 1 | 1 | 2 | 1 | **7** |
| N10 | Test de reflejos | Pulsa al cambiar de color; mejor marca guardada en el dispositivo | «¿Eres más rápido que yo?» | 2 | 1 | 2 | 2 | 1 | 1 | **7** |

Notas por candidata:

- **N1 · minuto.** La más pequeña de construir: un temporizador, una tarjeta y nada que pueda fallar en los datos. Ideal para estrenar la plataforma. El vídeo se hace solo: Ale prueba a cámara y falla, y no se inventa nada porque el resultado es el que salga.
- **N2 · 10.000 días.** Emocional sin ser triste y con una fecha que se celebra. Hay que cuidar el cálculo (bisiestos y zona horaria) y dejar claro que la fecha no sale del móvil.
- **N3 · ticket de suscripciones.** Es la idea favorita de la lista anterior con una forma más compartible. No muestra precios de servicios reales: los pone quien la usa.
- **N4 · amigo invisible.** Tiene **ventana de calendario**: sirve hasta mediados de diciembre. Si la primera miniapp tiene que estrenar también la web, llegar a tiempo es arriesgado. Funciona mejor como segunda, si la plataforma está lista a finales de noviembre. Cada uso reparte el enlace a varias personas, así que se difunde sola.
- **N6 · país de memoria.** Muy visual y con humor, pero comparar formas lleva más trabajo. Se puede hacer como segunda o tercera.
- **N7 · veranos.** Se apoya en una estadística pública: es un claim E con fuente y año, y hay que presentarla como promedio, no como predicción. El tono hay que cuidarlo.
- **N9 · dinero.** Útil y muy de España, pero la versión en inglés necesita otra serie de precios. El bilingüismo le pesa.
- **N10 · reflejos.** La demanda está demostrada, pero hay cientos de copias. Sin un giro propio no aporta nada.

## 4. Recomendación

1. **Primera miniapp: N1 «¿Cuánto dura tu minuto?»** Es la que menos se puede romper, la que mejor deja montar la plataforma (rutas ES/EN, pruebas, staging) sin pelear con la lógica y la que tiene el vídeo más claro. Sirve también para el ensayo del marco.
2. **Segunda, con fecha: N4 «Amigo invisible sin registro»**, solo si la web está publicada hacia el 1 de diciembre. Si no, se guarda para el año que viene y entra N3 o N2.
3. **Reserva:** N3, N2 y N6, en este orden.

Pendiente de Ale: elegir la primera (cierra PROD-14) y decir si N4 entra en el calendario de diciembre.
