# Ideas originales para la serie de 2027

**Fecha:** 2026-11-12 · **Autor:** Claude, a petición de Ale · **Estado:** propuesta. Continúa la [investigación de mercado](INVESTIGACION_MINIAPPS_2026-11.md); decide Ale.

## El encargo

- Una serie con **una miniapp nueva por semana**. Empieza con una de productividad, sigue con una de entretenimiento y luego se alternan.
- **El primer vídeo sale el viernes 1 de enero de 2027.**
- Para **cualquier país**: sin datos ni costumbres de una sola nacionalidad. En español e inglés desde el principio (PROD-03).
- **Gancho conceptual:** sin suscripción, sin cuenta, sin datos personales y gratis.
- **Originales**, no versiones de juegos o apps que ya existen.

## 1. El concepto como gancho, sin prometer de más

Lo que se puede afirmar y demostrar en cámara (claim P):

> **«Gratis. Sin cuenta. Sin suscripción. Lo que escribes no sale de tu móvil.»**

- **Demostración en todos los vídeos:** se abre la miniapp, se activa el **modo avión** y sigue funcionando. Es una prueba visual, no una promesa.
- **No decir** «gratis para siempre» ni «cero datos» (EDITORIAL y dossier). El hosting registra visitas como cualquier web. Lo que es verdad es que *lo que escribe la persona* no se envía.
- **Para que siga siendo verdad:**
  - Sin analítica de terceros en la página.
  - Fuentes alojadas en la propia web, no en Google Fonts: cargarlas de fuera ya es una petición a otro servidor.
  - Sin scripts externos.

  Esto cierra la decisión pendiente ADR-MMA-012 (analítica) a favor de no medir en el cliente. Si hace falta medir, que sean solo los recuentos agregados del propio hosting, *por comprobar qué ofrece Cloudflare*.
- **Límite técnico que condiciona el diseño:** Safari borra el `localStorage` de una web tras **7 días sin interacción** ([política de WebKit de 2020](https://searchengineland.com/what-safaris-7-day-cap-on-script-writeable-storage-means-for-pwa-developers-332519)). Una miniapp no puede depender de recordar algo durante meses. La solución encaja con el concepto: **lo importante se lo lleva la persona**, como imagen, archivo o evento de su propio calendario (`.ics`). Nada queda en una cuenta nuestra.

Promesa de serie propuesta para el gancho y la bio:

> «Cada viernes, una miniapp gratis. Sin cuenta, sin suscripción, y lo que escribes no sale de tu móvil.»

Esto concreta PR-001 (promesa editorial, todavía en propuesta). Si Ale la aprueba, se registra en DECISIONES.

## 2. Por qué el 1 de enero importa

- **Efecto «nuevo comienzo».** Dai, Milkman y Riis (2014) encontraron que las búsquedas de «dieta», las visitas al gimnasio y los compromisos con objetivos suben tras hitos temporales como el inicio de semana, de mes o de año ([Management Science](https://econpapers.repec.org/RePEc:inm:ormnsc:v:60:y:2014:i:10:p:2563-2582)). El 1 de enero es el hito más fuerte del año para empezar algo.
- **El abandono temprano.** Strava popularizó el «Quitter's Day» con datos de su app: la actividad cae hacia la segunda semana de enero ([BikeRadar](https://www.bikeradar.com/news/today-is-the-day-we-lose-motivation-strava-says)). La fecha concreta ha cambiado según el año y la fuente, así que en vídeo se dice «a mediados de enero», sin un día exacto.
- **Planes «si… entonces».** Las «intenciones de implementación» ayudan a cumplir objetivos. El efecto es real pero más pequeño de lo que se creía: un metaanálisis de 2024 lo rebaja mucho tras corregir sesgos ([resumen](https://www.thebehavioralscientist.com/glossary/implementation-intentions)). Se presenta como ayuda, no como garantía (claim H o E con matiz).

## 3. Lo que descarté por no ser original

He buscado cada idea antes de proponerla. Que no aparezca un producto no demuestra que no exista, pero estas sí existen y no las vamos a repetir:

| Idea | Ya existe | Ejemplo |
|---|---|---|
| Una sola tarea al día | Sí, varias apps | [1Task](https://www.producthunt.com/products/1task-one-task-a-day-that-s-all), [One Task](https://sindresorhus.com/one-task) |
| Tareas que caducan si no las haces | Sí | [Gone](https://www.producthunt.com/products/gone-2), [Do or Die](https://github.com/lkang-pdx/do-or-die) |
| Auditoría de tus 168 horas | Sí | [168 Hours a Week](https://www.producthunt.com/posts/168-hours-a-week) |
| «¿Esta reunión podía ser un correo?» | Sí | [Convo](https://www.itsconvo.com/tools/should-this-be-a-meeting) |
| ¿Cuánto dura tu minuto? (N1, lista anterior) | Es un reto conocido de cronómetro | Sale de la recomendación anterior |

## 4. Candidatas originales

Puntuación de 0 a 2 en seis criterios (12 en total):

- **Original (O):** no encontré un producto dedicado.
- **Productiva (P):** ayuda de verdad a organizarse o a cumplir algo.
- **Gancho (G):** se entiende y engancha en 1–3 s.
- **Global (Gl):** sirve en cualquier país.
- **Viable (V):** cabe en estático, sin servidor, en unas 6 h, contando el límite de Safari.
- **Enero (E):** encaja con el arranque del año.

### Productividad

| # | Miniapp (provisional) | Cómo funciona | Gancho | O | P | G | Gl | V | E | Total |
|---|---|---|---|---|---|---|---|---|---|---|
| **P1** | **Tu propósito, a prueba de febrero** | Escribes tu propósito. La app te lleva al futuro: «Es febrero y lo has dejado. ¿Por qué?». Eliges o escribes hasta tres motivos, y cada uno se convierte en un plan «si pasa esto, entonces haré aquello». Te llevas una tarjeta con tu plan y un **recordatorio en tu propio calendario** (`.ics`) para mediados de enero | «Mi propósito de 2027 ya ha fracasado. Lo he hecho a propósito» | 2 | 2 | 1 | 2 | 2 | 2 | **11** |
| P2 | Encoge tu propósito | El propósito grande se encoge en pantalla, pregunta a pregunta («¿y en dos minutos?»), hasta convertirse en un gesto diario mínimo. Sin IA: lo encoge la persona, guiada | «Leer 50 libros» se convierte en «una página después de cenar» | 1 | 2 | 2 | 2 | 2 | 2 | **11** |
| P3 | El coste de hacer dos cosas a la vez | Mismo ejercicio dos veces: primero una tarea y luego otra, después alternándolas. Mide tu propio tiempo y te enseña la diferencia | «En 30 segundos te demuestro que la multitarea te hace más lento» | 1 | 2 | 2 | 2 | 2 | 1 | **10** |
| P4 | Tu 2026 en reuniones | Importas el archivo `.ics` que exporta tu calendario y la web te hace un resumen del año (horas en reuniones, día más cargado, etc.). El archivo no sale del navegador | «Pasé X horas de 2026 en reuniones» (dato real de Ale o ninguno) | 1 | 1 | 2 | 2 | 1 | 2 | **9** |

- **P1.** No encontré una herramienta dedicada al «pre-mortem» de propósitos personales. La técnica existe en empresa (Gary Klein) y algunas guías la aplican a propósitos ([Lumosity](https://fee.lumosity.com/en/blog/a-positive-mindset-planning-for-failure-resolution-success)), pero no como app. El recordatorio `.ics` resuelve el límite de Safari y es coherente con «nada nuestro guarda tus datos».
- **P2 · ★ A Ale le gusta el concepto (2026-11-12).** Queda como candidata firme para la serie; falta decidir la fecha. Existe al menos un generador de microhábitos ([ejemplo](https://ehm-tech.pages.dev/habit/tools/tiny-habit-generator/)), así que la originalidad es parcial. Lo propio es la animación del texto encogiéndose. También podría ser un paso dentro de P1.
- **P3.** El ejercicio de multitarea en papel es conocido, así que el valor está en medirte a ti. Conviene revisar antes de construirla si hay ya versiones interactivas.
- **P4.** Existe al menos algo parecido («Meetings Wrapped»). Además, las reuniones periódicas del `.ics` (RRULE) dan trabajo.

### Entretenimiento

| # | Miniapp (provisional) | Cómo funciona | Gancho | O | P | G | Gl | V | E | Total |
|---|---|---|---|---|---|---|---|---|---|---|
| **E1** | **Predicciones selladas 2027** | Escribes tus predicciones del año. La web genera una **huella** (SHA-256 con una clave aleatoria) que puedes publicar ya. El texto y la clave te los llevas en un archivo. En diciembre los pegas y cualquiera comprueba que no los cambiaste | «Hoy publico una huella. En diciembre os demuestro que acerté» | 2 | 0 | 2 | 2 | 2 | 2 | **10** |
| E2 | Móviles en la mesa | Cada persona abre la web en su móvil y lo deja en la mesa. Si alguien lo mueve, su pantalla se pone roja y marca la hora. Gana el último | «Cena familiar: el primero que toque el móvil, friega» | 2 | 1 | 2 | 2 | 1 | 1 | **9** |
| E3 | El reto del silencio | El micrófono mide el ruido de la sala, siempre dentro del móvil. Si alguien supera el umbral, pierde el grupo | «¿Cuánto aguanta tu familia en silencio?» | 1 | 0 | 2 | 2 | 1 | 1 | **7** |

- **E1.** El método de «compromiso con huella» se conoce en foros técnicos ([LessWrong](https://www.lesswrong.com/posts/DHKaRB2dKYHYNrBGj/is-there-a-convenient-way-to-make-sealed-predictions)), pero no encontré una herramienta para el público general. Encaja con la marca: Ale usa huellas en su propio flujo de trabajo, y se puede contar en el vídeo como algo verdadero.
- **E2.** El juego de apilar móviles en la cena existe desde 2012 ([The Week](https://theweek.com/article/index/223137/how-the-phone-stack-is-civilizing-dinners-out-with-friends)), pero no encontré una app que lo arbitre con el sensor de movimiento. Lo técnico hay que probarlo en un prototipo:
  - En iPhone, el sensor exige permiso con un toque y HTTPS ([MDN](https://developer.mozilla.org/en-US/docs/Web/API/DeviceMotionEvent/requestPermission_static)).
  - La pantalla tiene que mantenerse encendida, y Safari solo lo admite desde la 16.4 ([Chrome Developers](https://developer.chrome.com/docs/capabilities/web-apis/wake-lock)).
  - Los móviles no se comunican entre sí: cada uno marca su hora y se comparan a ojo.
- **E3.** Pide micrófono, lo que choca con la sensación de «sin datos» aunque todo se procese en el móvil. Queda de reserva.

## 5. Recomendación y calendario

| Viernes | Miniapp | Tipo | Por qué en esa fecha |
|---|---|---|---|
| 1 ene 2027 | **P1 · Tu propósito, a prueba de febrero** | Productividad | El día del año con más ganas de empezar. Original, global, sin datos y con su propio «recuerdo» en el calendario |
| 8 ene | **E1 · Predicciones selladas 2027** | Entretenimiento | Aún es «principio de año». La huella se publica en redes y se vuelve a ella en diciembre: serie con final asegurado |
| 15 ene | P3 · El coste de hacer dos cosas a la vez | Productividad | Vuelta a la rutina de trabajo |
| 22 ene | E2 · Móviles en la mesa | Entretenimiento | Si el prototipo del sensor funciona en los dos móviles de Ale; si no, entra P2 |

**Producción.** Hoy es 12 de noviembre: quedan siete semanas.
- Antes del 1 de enero tienen que estar **la web en producción y P1 publicada**. Así el vídeo puede enseñar una URL real.
- Conviene llegar con **P1 y E1 terminadas y grabadas antes de Navidad**, para que las fiestas no rompan la serie en la segunda semana.
- El **ensayo del marco** se hace con P1 en diciembre (expediente `--ensayo`): sirve de prueba de grabación y montaje sin publicar.

## 6. Evaluación independiente (2026-11-12)

Ale pasó el [brief ciego](BRIEF_EVALUACION_CIEGA.md) a otra IA, sin memoria del proyecto. Las letras del brief equivalen a: A = PDF para trámites, B = Predicciones selladas (E1), C = Encoge tu propósito (P2), D = QR (H3), E = Propósito a prueba de febrero (P1).

| Idea | Mi valoración | Independiente (/100) | Coincidencia |
|---|---|---|---|
| P1 · Propósito a prueba de febrero | 11/12, para el 1 de enero | **81, 1.ª, para el 1 de enero** | Sí, en puesto y fecha. **Mi «original 2» estaba mal:** WOOP (contraste mental + planes «si… entonces») hace el núcleo gratis en ES/EN. Lo nuevo es el encuadre «ya es febrero» |
| H3 · QR | 10/12, 2.º o 3.er vídeo | **78, 2.ª**; el plano físico es lo valioso; propone el 15 de enero | Sí. Añade avisos: el QR Wi-Fi impreso expone la clave y `BarcodeDetector` no es universal |
| P2 · Encoge tu propósito | 11/12 | **74, 3.ª**, la más débil en diferenciación | Parcial. Propone cerrar con «Después de [rutina], haré [acción mínima]» y no publicarla justo después de P1 |
| PDF para trámites | Viable, con límites | **59, 4.ª**: la más útil, pero la peor para la cadencia semanal | Parcial. Recorte aceptado (ver la ficha en HERRAMIENTAS) |
| E1 · Predicciones selladas | 10/12, para el 8 de enero | **53, 5.ª, descartar** | **No.** Tenía razón en dos cosas que yo no vi: ya existen herramientas para el público general (Sealed, Globefin, según esa evaluación, sin verificar por mí) y la huella no demuestra *cuándo* se creó. Un pie de foto editable no da una fecha creíble |

**Correcciones que acepto:**
1. **El concepto es un argumento de confianza, no el gancho principal.** Los ganchos parten del problema («Es febrero y ya has abandonado tu propósito») y la privacidad cierra el vídeo como firma breve, en pocos segundos de modo avión.
2. **Promesa más exacta:** «Gratis. Sin cuenta. Sin suscripción. Tus datos se procesan en tu dispositivo. Solo salen de él cuando decides compartirlos o exportarlos.» Sustituye a la del §1, pendiente de que Ale la apruebe.
3. **P1 sin adornos:** un propósito, un obstáculo, un plan concreto, una tarjeta y un evento descargable. El texto dice «Descargar evento para tu calendario», no «te avisaremos». Se cita WOOP o el contraste mental como base (claim E), sin presentarlo como técnica nueva.
4. **E1 sale del calendario inicial.** El hueco de entretenimiento del 8 de enero queda libre.
5. **Condición para publicar cada miniapp:** una persona real resuelve el problema sin instrucciones y lo anunciado está probado en iOS Safari y Android Chrome. Si no se cumple, se recortan funciones antes que calidad.

**Dónde matizo a la evaluación:**
- Su piloto de 15–20 personas por idea (unas 100 en total) no cabe en 11–15 h semanales. Propuesta: 5–8 personas **solo para P1** antes del 1 de enero, para comprobar que completan el plan sin ayuda. El resto se mide con las publicaciones.
- Su prueba «gancho de problema frente a gancho de privacidad» encaja con el marco como **hipótesis de una semana** (EDITORIAL: una variable), no como experimento aleatorio, que no podemos hacer.

**Calendario ajustado (propuesta):**

| Viernes | Miniapp |
|---|---|
| 1 ene | P1 · Propósito a prueba de febrero |
| 8 ene | Entretenimiento: por elegir (E2 «Móviles en la mesa» u otra; hace falta investigar más) |
| 15 ene | QR de pósits |
| 22 ene | Entretenimiento: por elegir |
| 29 ene | P2 · Encoge tu propósito, con la frase «Después de…» |
| Más adelante | PDF para trámites, versión recortada |

## 7. Decisiones que tiene que tomar Ale

1. Elegir la primera miniapp: **P1**, recomendada. Cierra PROD-14.
2. Aprobar la promesa de serie («Cada viernes, una miniapp gratis…»), que concreta PR-001.
3. No usar analítica en la página (ADR-MMA-012), para que la promesa sea cierta.
4. Calendario de enero: el orden de la tabla u otro.
