# Plan B · Bad Day Plan

**Definición de producto · v04 (2026-11-12, revisión de CTO)**. Documento autocontenido: se puede leer sin ningún otro archivo.

Este documento dice **qué es el producto, cómo tiene que sentirse y qué calidad debe tener**. Cómo se construye lo decide quien lo desarrolle. «Ale» es Alexander, el responsable del producto: lo marcado como «decisión de Ale» no se cierra sin él.

- **Nombre:** ES **«Plan B»**, con el subtítulo *«para tu propósito»* · EN **«Bad Day Plan»**. En inglés no se usa «Plan B» porque en EE. UU. se asocia a una marca de anticonceptivo. Decidido por Ale.
- **Direcciones propuestas:** `/es/plan-b` y `/en/bad-day-plan`, una dirección estable por idioma.

**Cambios de la v04:**
1. Textos que dependen del mes y del año, en lugar de «febrero» y «2027» fijos.
2. El aviso del calendario ya no promete una hora exacta que no podemos garantizar.
3. Los avisos usan las palabras exactas de la persona, sin conjugarlas.
4. El reto deja de mostrar un nombre escrito por otros.
5. Alcance dividido en imprescindible, importante y si da tiempo.
6. Requisitos de calidad medibles.
7. Página de privacidad honesta.
8. Criterios para decidir si se lanza.

---

## 0. Contexto mínimo

- **MiMiniApp** (nombre provisional) es una web pública, gratuita, bilingüe (español e inglés) y de código abierto con una colección de **miniapps**: herramientas pequeñas, cada una con su propia dirección web y fáciles de compartir. Su creador, Alexander, publica una miniapp nueva cada semana con un vídeo vertical corto (TikTok, Reels, Shorts) en el que la enseña.
- **Esta es la primera miniapp.** Su vídeo abre la serie el **viernes 1 de enero de 2027**. Tiene que estar publicada y probada antes de Navidad para poder grabarlo.
- **Condiciones de todas las miniapps:**
  - Web estática, sin servidor propio, sin cuentas ni inicio de sesión y sin servicios de terceros por defecto. **Única excepción decidida:** una medición anónima de visitas sin cookies (§12).
  - Los datos se procesan en el navegador y solo pueden guardarse en el propio dispositivo.
  - Pensadas primero para el móvil, con una versión de escritorio igual de cuidada.
  - Español e inglés completos.
  - Cada miniapp tiene un ejemplo listo para probar y un botón para empezar de cero.
  - Comparten los componentes comunes del §5: compartir, explorar, privacidad e idioma.
  - El resultado tiene que verse bien en un vídeo vertical, sin que la web se diseñe solo para el vídeo.

---

## 1. La idea en una frase

> **Dime tu propósito, dime qué te hará dejarlo y te ayudo a tener un plan B para ese día.**

Casi todo el mundo empieza enero con un propósito. Casi nadie piensa qué hará el día en que no le apetezca o no le dé tiempo. Ese día llega, no hay plan y se abandona.

Plan B te lleva **un mes al futuro**, al momento en que ya lo has dejado, para que veas qué falló, y te trae de vuelta con un plan para ese momento exacto. En 2 minutos sales con una frase «Si pasa esto, entonces haré esto otro» y con algo que te la recuerda cuando importa: **un evento repetido en tu propio calendario** y **tu plan en la pantalla de bloqueo**.

- **Para quién:** cualquier persona con un propósito, en cualquier país.
- **Lo que no es:** una app de hábitos. No te sigue, no manda notificaciones propias, no lleva rachas. Es un ejercicio corto de una sola vez que te deja algo útil.
- **Base:** la investigación sobre planes «si… entonces» y contraste mental, que herramientas como WOOP también aplican. No es un método nuevo. Lo nuestro es la experiencia: el viaje al mes siguiente, la brevedad y el recordatorio a la hora del peligro.

## 2. La promesa

1. **Dos minutos y tres preguntas.**
2. **Un recordatorio a la hora del peligro,** desde tu calendario y no desde una app nuestra.
3. **Sin cuenta, sin correo y sin pagar.** Tus datos se procesan en tu dispositivo y solo salen cuando tú decides compartirlos o exportarlos.
4. **Te reta a comprobarlo:** *«No te fíes de nosotros: activa el modo avión y sigue.»*

---

## 3. El concepto visual: un viaje al mes siguiente y de vuelta

| Momento | Sensación | Cómo se ve |
|---|---|---|
| **Hoy** (portada y paso 1) | Ilusión | Colores vivos. Hoja de calendario con el mes actual |
| **El salto** (paso 2) | «Uy» | La hoja pasa sola al mes siguiente y todo se apaga: colores desaturados y luz fría |
| **El plan** (paso 3) | Recuperar el control | El color vuelve poco a poco mientras se escribe |
| **La vuelta** (paso 4) | Alivio | Cae un sello sobre la hoja del mes siguiente: *«Este [febrero], no.»* La pantalla vuelve al mes actual |

- **La transición de color es la firma** de la miniapp y el plano estrella del vídeo.
- **Tono:** cercano, con algo de humor y honesto. *«Febrero da miedo, lo sabemos.»* Nada de frases motivacionales vacías.
- **Movimiento:** suave y con intención. Con «reducir movimiento» activado en el móvil, solo fundidos.
- **Detalle táctil:** una vibración corta al caer el sello, solo en los móviles que lo permiten.
- **Identidad visual de MiMiniApp:** **ya está definida por Ale** y se entrega junto a este documento. Es distinta de la identidad visual de los vídeos del creador. El concepto de color de este apartado (vivo → apagado → vivo) se aplica dentro de esa identidad, sin sustituirla.

---

## 4. La experiencia, pantalla a pantalla

Los textos entre `{llaves}` cambian solos según la fecha y el idioma (ver §6).

### Portada

- Titular: **«Es {mesSiguiente} y ya has abandonado tu propósito.»** Debajo: *«Vamos a evitarlo. Tardas 2 minutos.»*
- Botones: **Empezar** y **Ver un ejemplo**.
- Al pie: *«Gratis. Sin cuenta. Lo que escribes se queda en tu móvil. Compruébalo: activa el modo avión.»*
  - Antes decía «nada sale de tu móvil», y era falso, porque la persona sí puede exportar o compartir.

### Paso 1 · ¿Qué quieres lograr?

- Un campo grande (máx. 80 caracteres). En enero la pregunta añade «este año».
- Ejemplos que se tocan: *Hacer ejercicio · Leer más · Ahorrar · Aprender un idioma · Dormir mejor · Usar menos el móvil*.

### Paso 2 · El salto

- Animación de la hoja y apagado de colores.
- Pregunta: **«Imagina que es 1 de {mesSiguiente} y lo has dejado. ¿Qué ha pasado?»**
- Seis tarjetas grandes; se toca una (lista confirmada por Ale el 2026-11-12):
  - No tuve tiempo
  - Perdí las ganas
  - Algo se cruzó
  - Era demasiado
  - Se me olvidó
  - Otra cosa (se escribe)
- Es el corazón del producto: **adivinar el obstáculo antes de que llegue**. Por eso se toca, no se escribe.

### Paso 3 · Tu plan para ese día

- Una frase que se rellena: **Si [situación], entonces [acción].** Cada hueco admite 3–90 caracteres.
- Sugerencias según el obstáculo. Con «No tuve tiempo»: *si llego tarde a casa · si tengo reuniones todo el día* → *hago una versión de 5 minutos · lo hago nada más levantarme*.
- Dos ayudas suaves, que no bloquean:
  - *«¿Lo podrías ver en una foto? Si no, concrétalo más.»*
  - *«Algo pequeño: 5 minutos o menos.»*
- **¿A qué hora suele pasar?** (opcional): hora y días, por defecto de lunes a viernes. Sin hora no se ofrece el calendario.

### Paso 4 · La vuelta: tu plan

- Cae el sello y se muestra el plan, grande.
- Opciones, en orden de utilidad:

  1. **Recuérdamelo** (solo si hay hora):
     - Crea un **evento repetido** a esa hora y esos días, **durante 4 semanas**: el mes de peligro. Así no se queda para siempre en el calendario. La opción «Repetir siempre» es decisión de Ale.
     - Título del evento: **«Plan B: [acción]»**, con las palabras exactas de la persona. Va corto a propósito, porque los avisos de la pantalla de bloqueo cortan los textos largos. La descripción lleva la frase completa: «Si [situación], entonces [acción]».
     - **Descargar evento** (`.ics`): incluye el aviso a la hora del evento.
     - **Añadir a Google Calendar**, si entra en la v1 (decisión de Ale). Antes de abrirlo se avisa: *«Se abrirá Google Calendar con tu plan»*. En este caso **el aviso lo pone la configuración de Google de cada persona**, no nosotros, y el texto lo dice: *«Te avisará según tus ajustes de Google Calendar»*.
     - Vista previa de cómo se verá el evento, **sin prometer una hora de aviso que no controlamos**.

  2. **Llévatelo:** fondo de pantalla de bloqueo.
     - Vista previa sobre un móvil, con la hora encima.
     - Imagen limpia, sin dirección ni marca.
     - Pasos rápidos para ponerla de fondo en iPhone y en Android.

  3. **Compártelo:** «Mi plan» (imagen para stories con la dirección de la miniapp y un texto listo) o «Reta a alguien» (solo el enlace). Ver §5.

- Al pie: **Empezar otra vez** y **Cómo sabemos que tus datos se quedan en tu móvil**.

---

## 5. Componentes comunes a todas las miniapps

### Compartir

| Qué | Dónde | Qué viaja |
|---|---|---|
| **La miniapp** | Icono arriba, siempre visible, y «Reta a alguien» | El enlace y un texto de invitación fijo, escrito por nosotros |
| **El resultado** | Al final | La imagen o el texto que la persona elige, hacia la app que elige |

- **En el móvil:** el menú de compartir del propio teléfono, con imagen incluida cuando el móvil lo permite.
- **Respaldo:** «Copiar enlace» y enlaces simples a WhatsApp, X, Telegram y correo. **Sin botones ni scripts de redes sociales**, que rastrean a quien visita la página.
- **Vista previa del enlace:** una tarjeta atractiva (imagen, título y frase) por miniapp e idioma, la misma para todos.
- **«Reta a alguien» no lleva nombre ni texto de quien lo envía.**
  - **Por qué:** cualquier texto que viaje en un enlace y se muestre en nuestra web puede usarse para poner insultos o engaños bajo nuestro dominio.
  - **Regla general:** ninguna miniapp muestra texto que venga en la dirección web, salvo valores de una lista cerrada.
- El plan **nunca va dentro del enlace**.

### Explora más

Aparece **después** del resultado, nunca en mitad del recorrido.
- Titular: *«Esta es la miniapp n.º {n} de MiMiniApp. Cada viernes llega una nueva.»* La segunda frase se edita en un solo sitio por si la serie cambia de ritmo.
- **Ver todas las miniapps** lleva al catálogo en el mismo idioma.
- Con más miniapps: dos tarjetas de **«Te puede servir también»**, elegidas a mano.
- Mientras sea la única: **«Ver la próxima el viernes»**, con enlaces simples a las redes del creador (YouTube `@soy.cerobytes`, TikTok `@cerobytes`, Instagram `@cer0bytes`). Nunca se anuncian miniapps que no existen.
- **Ver el código**, cuando el repositorio sea público.
- Arriba, en todas las miniapps, un acceso fijo y discreto: *«MiMiniApp · Todas las miniapps»*.

### Página «Cómo sabemos que tus datos se quedan en tu móvil»

Común a toda la web, corta y honesta:
- Lo que escribes se procesa en tu navegador y no se envía a ningún servidor nuestro.
- No hay cuentas ni cookies. La única medición es un **recuento anónimo** de visitas y de pasos completados, sin cookies y sin nada de lo que escribes (§12).
- **Lo que sí ocurre:**
  - El servicio de alojamiento, como cualquier web, recibe tu dirección IP para poder servirte la página.
  - Si exportas a Google Calendar o compartes, lo que eliges va a ese servicio.
- Cómo comprobarlo tú: el modo avión y el código abierto.
- **Los textos legales completos** (pie, página de privacidad y aviso legal, en ES y EN) se entregan en un documento aparte: «Textos legales de MiMiniApp». Se publican como dos páginas fijas, «Privacidad» y «Aviso legal», enlazadas en el pie de todas las páginas.

### Idioma

- La primera visita propone el idioma del navegador, siempre con un selector visible.
- El selector mantiene la misma miniapp: de `/es/plan-b` a `/en/bad-day-plan`.

---

## 6. Textos clave y reglas de fecha

**Regla de fecha:**
- `{mesSiguiente}` es el mes de dentro de 31 días: en enero, «febrero».
- `{año}` es el año de ese mes.
- Las fechas y los días se escriben según el idioma de la página.

| Clave | ES | EN |
|---|---|---|
| Titular | Es {mesSiguiente} y ya has abandonado tu propósito. | It's {nextMonth} and you've already quit your goal. |
| Paso 2 | Imagina que es 1 de {mesSiguiente} y lo has dejado. ¿Qué ha pasado? | Imagine it's {nextMonth} 1 and you've stopped. What happened? |
| Sello | Este {mesSiguiente}, no. | Not this {nextMonth}. |
| Guía | ¿Lo podrías ver en una foto? Si no, concrétalo más. | Could you see it in a photo? If not, make it more specific. |
| Evento | Plan B: {acción} | Bad Day Plan: {action} |
| Imagen para stories | Mi plan B para {año}. Haz el tuyo en {dirección} | My bad day plan for {year}. Make yours at {url} |
| Invitación | Mira esto: haz tu plan B en 2 minutos. | Try this: make your bad day plan in 2 minutes. |

Los avisos y las imágenes repiten **las palabras exactas** de la persona. Nunca se reescriben ni se conjugan: cambiar «llego» por «llegas» es imposible de hacer bien en todos los idiomas.

## 7. Ejemplo para la demostración

**Ver un ejemplo** rellena siempre lo mismo:
- **Propósito:** «Hacer ejercicio 3 veces por semana».
- **Obstáculo:** «No tuve tiempo».
- **Plan:** «Si llego a casa después de las 20:00, entonces hago 5 minutos de estiramientos antes de sentarme en el sofá».
- **Hora:** de lunes a viernes a las 20:00, durante 4 semanas.

---

## 8. Alcance de la primera versión

**Imprescindible para el 1 de enero (sin esto no se lanza):**
- Los 3 pasos con su texto, el ejemplo y «Empezar otra vez».
- El concepto visual: la hoja que pasa, el apagado de colores y el sello. Si el tiempo aprieta, puede ser una versión sencilla, pero no puede faltar.
- Español e inglés completos.
- **Al menos una forma de recordatorio** que funcione en Android y en iPhone, según la prueba técnica: `.ics`, Google Calendar o las dos.
- Fondo de pantalla en un estilo.
- Compartir la miniapp (menú del móvil y «Copiar enlace»), con su vista previa de enlace.
- «Explora más», en su versión de una sola miniapp.
- Página de privacidad y selector de idioma.
- Accesibilidad básica: teclado, lector de pantalla, contraste y «reducir movimiento».
- La regla de privacidad del §9: ninguna petición lleva nada de lo que escribe la persona.

**Importante (se intenta para el 1 de enero; si no llega, va en la semana siguiente):**
- La imagen para stories («Mi plan») y «Reta a alguien».
- Tres estilos de fondo de pantalla y la vista previa sobre un móvil.
- La segunda forma de recordatorio.
- La vibración.

**Con fecha propia: antes del 31 de enero.** Los textos que cambian con el mes (§6). Si el 1 de enero el texto dice «febrero» fijo, es aceptable, pero tiene que estar adaptado antes de que llegue febrero.

**Fuera de esta versión:** seguimiento de hábitos, rachas, notificaciones propias, varios propósitos, cuentas, IA, historial y estadísticas.

---

## 9. Requisitos de calidad (medibles)

| Área | Requisito |
|---|---|
| **Rendimiento** | Carga rápida en un móvil de gama media con 4G: contenido principal visible en 2,5 s o menos y respuesta al tocar en 200 ms o menos. La animación va fluida y sin saltos |
| **Dispositivos** | Android con Chrome (Samsung Galaxy S24+ y Xiaomi POCO F5 como mínimo), iPhone con Safari (versión actual y la anterior) y navegadores de escritorio actuales |
| **Accesibilidad** | Objetivo WCAG 2.2 AA, comprobado con herramientas automáticas y a mano. Contraste suficiente también en la fase «gris» |
| **Global** | Fechas y días según el idioma. Cualquier alfabeto, emojis y escritura de derecha a izquierda, también en las imágenes generadas |
| **Privacidad** | **Ninguna petición lleva nada de lo que escribe la persona.** Solo se permiten tres tipos: la carga de la página, la medición anónima del §12 y lo que la persona provoca al exportar a Google o compartir. Una prueba automática lo vigila. Si la medición falla o no hay conexión, la miniapp funciona igual |
| **Robustez** | Recargar no pierde el paso. Cerrar la pestaña no deja nada guardado. Funciona sin conexión una vez cargada, salvo Google Calendar, que lo avisa |
| **Seguridad** | No se muestra nunca texto que venga en la dirección web. El texto de la persona se trata siempre como texto, nunca como código |

## 10. Riesgos y cómo los cubrimos

| Riesgo | Mitigación |
|---|---|
| El `.ics` falla en iPhone o Google Calendar no lo importa en Android | Prueba técnica en tres móviles **antes de diseñar el paso 4**. Lanzar solo con lo que funcione; el fondo de pantalla siempre está |
| El aviso de Google Calendar no suena a la hora | No se promete una hora: el texto remite a los ajustes de cada persona |
| Ponerse el fondo de pantalla es engorroso, sobre todo en iPhone | Instrucciones de dos pasos por sistema, comprobadas en un iPhone real |
| No se entiende a la primera | Prueba con 5–8 personas sin ayuda antes del 18 de diciembre. Si menos de la mitad termina un plan concreto en menos de 3 minutos, se cambia el flujo |
| No llega a tiempo | El alcance del §8 marca qué se puede aplazar sin romper la promesa |
| Abuso de enlaces compartidos | El reto no lleva texto de usuario (§5) |

## 11. Criterios para lanzar (se revisan el 18 de diciembre)

1. Todo lo «imprescindible» del §8 funciona en los dispositivos del §9.
2. La prueba con personas cumple el umbral del §10.
3. El modo avión funciona en el recorrido de demostración.
4. No hay fallos graves de accesibilidad.
5. La dirección definitiva (**miminiapp**, en el dominio que compre Ale) está publicada. Sin ella, el vídeo no puede enseñar dónde está la miniapp.

Si algo falla, **se recorta antes que lanzar mal**. Lo que se anuncia en el vídeo tiene que estar probado.

## 12. Cómo sabremos que funciona

**Medición anónima, sin cookies y sin lo que escribe la persona.** Decisión de Ale: necesita saber si los vídeos atraen tráfico.

- **Herramienta: Umami**, de código abierto. No usa cookies ni guarda datos personales, y su fabricante dice que no necesita ventana de consentimiento. Es su postura, no una conclusión legal.
  - **Umami Cloud** tiene un plan gratuito: unos 100.000 eventos al mes en una web, con 6 meses de historial, según fuentes de terceros que hay que comprobar en su web.
  - **Umami en un servidor propio** no tiene límites, pero necesita mantenerse.
- **Qué se mide:**
  - Visitas por página y por idioma.
  - **De dónde llega la gente.** Los enlaces de cada red llevan su etiqueta: el de la bio de TikTok termina en `?utm_source=tiktok`, y lo mismo con Instagram, YouTube y X. Así se ve qué red trae tráfico aunque la app de la red oculte la procedencia.
  - **Eventos sin contenido:** «empezó», «terminó su plan», «descargó el evento», «añadió a Google Calendar», «guardó el fondo», «compartió», «pulsó Explora más». **Nunca** el propósito, el obstáculo escrito, el plan ni la hora.
- **Qué no se usa: Google Analytics.**
  - En la UE necesita una ventana de cookies con consentimiento previo: según la guía de la AEPD descrita por varias fuentes, las cookies de analítica requieren consentimiento salvo una medición anónima muy limitada, que GA4 no cumple en su configuración normal.
  - Además, envía datos a Google.
  - Rompería «sin cookies, sin sorpresas» y la confianza que es el centro del producto.
- **Antes del lanzamiento:** la prueba con 5–8 personas (§10).
- **Después:** las métricas anteriores, más comentarios y fondos de pantalla compartidos en redes y las métricas de los vídeos.

## 13. Decisiones de Ale

1. Si «Añadir a Google Calendar» entra en la v1.
2. La duración del recordatorio: 4 semanas, o con opción de «Repetir siempre».
3. **Umami Cloud gratis o Umami en un servidor propio.** Recomendación: Cloud gratis para empezar.
4. Rellenar los datos de los textos legales: nombre y correo de contacto.
5. **El dominio:** será **miminiapp**, pendiente de compra. Tiene que estar comprado y conectado antes del 11 de diciembre.
