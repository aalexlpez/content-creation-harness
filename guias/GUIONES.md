# Cómo escribir un guion

Un guion de este marco es a la vez **texto para decir** y **plan de montaje**. Con él, Ale debe poder grabar y editar sin adivinar nada. Se escribe en `videos/VID-NNNN/GUION.md`.

## 1. Brief: el contrato antes de redactar

| Campo | Qué poner |
|---|---|
| Audiencia | A1, A2 o A3 (ver [EDITORIAL](EDITORIAL.md)) y en una frase quién es |
| Objetivo | Uno: descubrimiento, conversación o conversión verificable (visita, prueba) |
| Pilar | UTILIDAD, PROCESO, EXPERIMENTO o COMUNIDAD |
| Familia | A Demo, B Proceso, C Experimento, D Comunidad o E Tutorial |
| Promesa | Lo que el espectador obtiene, comprobable dentro del vídeo |
| Prueba_visual | El plano concreto que cumple la promesa y en qué segundo aparece |
| CTA | Uno, coherente con el objetivo. «Ninguno» es válido |
| Duracion | Estimada en segundos. Se confirma leyendo en voz alta |
| Ritmo | Cortes por escena, pausas, dónde se acelera o respira |
| Musica | Carácter, entrada, bajada bajo la voz y salida, o «voz sola» |
| Texto_en_pantalla | Jerarquía: subtítulo, rótulo y frase de acento |
| Color | Tratamiento de la toma de cámara. La captura de pantalla conserva su color |
| Perfil_visual | TEMP mientras no haya identidad aprobada |

**Bloquea el guion** si no hay una promesa concreta o no se sabe cómo se va a demostrar.

## 2. Familias de guion

**A · Demo útil**
1. Gancho visual con el resultado o la fricción concreta (primeros 1–3 s).
2. Contexto en una frase: quién pierde tiempo y en qué.
3. Demostración real: entrada, transformación, salida.
4. Prueba del resultado, sin esconder límites.
5. CTA relacionado (probarla si hay URL; si no, seguir el avance o proponer ideas).

**B · Proceso (construir en público)**
1. Gancho con una tensión real: «esta parte no funcionaba» (solo si es verdad).
2. El obstáculo, la decisión y por qué importa a quien lo usará.
3. Antes y después, o prueba de que funciona.
4. Próximo paso real y, si encaja, una pregunta.

**C · Experimento**
1. Pregunta original que cualquiera entiende.
2. Hipótesis explícita, presentada como hipótesis.
3. Experimento y resultado reproducible.
4. Interpretación honesta y su límite.

**D · Comunidad**
1. Contexto o resultado real de la serie.
2. La decisión que se pide, con opciones concretas (tres como máximo).
3. Qué se hará con las respuestas (a mano si no hay sistema de votos).
4. Una sola pregunta.

**E · Tutorial para desarrolladores**
1. Resultado final primero.
2. Requisitos verificados (versiones, enlaces).
3. 2–4 pasos con terminal real y comandos ejecutados de verdad.
4. Prueba de que terminó bien.

## 3. Ganchos

1. Escribe **dos**: uno desde el problema y otro desde el resultado. 18 palabras como máximo.
2. Puntúa cada uno de 0 a 2 en cuatro criterios: se entiende sin contexto, coincide con el contenido, la prueba aparece pronto e interés genuino sin clickbait. Total sobre 8.
3. Gana el de mayor puntuación. En empate, el más claro. Anótalo en la tabla Ganchos (`elegido: sí`).
4. Si los dos fallan, **una** reescritura. Si siguen fallando, el problema está en la idea, no en las palabras.
5. No empieces con «Hola, soy…». Abre con acción o con el conflicto. La presentación, si hace falta, después de ganarte los primeros segundos.

## 4. Voz y estilo

- Primera persona, natural y concreta: «he creado», «voy a probar», «todavía no funciona».
- Frases cortas y una idea por pantalla. Nada de tono de gurú.
- Evita absolutos que no puedes demostrar: «todas», «nunca», «gratis para siempre».
- El texto en pantalla no repite la voz palabra por palabra. Los subtítulos sí transcriben la voz.
- Ale lo **lee en voz alta y lo cronometra** antes del OK-2. La duración real manda sobre la estimada.

## 5. Escenas: guion y montaje en una tabla

Una fila por escena. Cada intervención se ancla a un tiempo aproximado y a una palabra o acción visible, para encontrarla en el editor.

| Columna | Qué poner |
|---|---|
| escena | S01, S02… |
| tiempo | `00:00–00:04` aproximado |
| voz literal | Exactamente lo que se dice, o «—» si no hay voz |
| imagen y texto en pantalla | Plano (cámara, pantalla, animación), punto de corte, texto exacto entre comillas, estilo (subtítulo, rótulo, acento), posición y duración |
| sonido | Entrada, bajada o salida de música, efecto puntual o silencio |
| toma o recurso | Qué hay que grabar o qué archivo se usa. Marca `POR ACREDITAR` lo que aún no tenga derechos |
| claim | ID del claim que sostiene la escena, o «—» |

Si una escena funciona con voz, plano fijo y subtítulos, escríbelo así. No añadas efectos por rellenar. Cómo decidir texto, música, color y movimiento: [EDICION](EDICION.md).

## 6. Claims

Toda afirmación que se pueda comprobar va a la tabla Claims.

| Tipo | Significa | Ejemplo |
|---|---|---|
| P | Producto o prueba propia, demostrada en el vídeo o en el repositorio | «Elimina duplicados de una lista de 1.000 líneas» (probado) |
| E | Fuente externa citada, con fecha | «YouTube recomienda 8 Mbps para 1080p30» (enlace) |
| O | Opinión o experiencia personal | «Me cansé de pagar suscripciones» |
| H | Hipótesis declarada como tal | «Creo que esto ahorra tiempo a…» |
| X | Sin verificar | **Bloquea el OK-2** hasta probarse, reformularse o quitarse |

Si el vídeo no afirma nada comprobable, deja una fila `SIN-CLAIMS | O | — | Pieza de opinión o proceso`. Las recreaciones o datos de prueba se declaran en pantalla.

## 7. Revisiones

- Borrador → una reescritura → aprobación o bloqueo. Nunca nueve versiones sin evidencia nueva.
- Las correcciones se piden con tiempo, defecto observable, cambio y criterio para darlo por bueno. No sirve «hazlo más profesional».
- Dos rondas de correcciones de montaje como máximo. Si no se resuelve, se revisa el brief o la técnica.
- Un cambio de guion después del OK-2 sube la `Version` y exige un nuevo OK-2.

## 8. Ejemplo (ficticio)

Demo de 20 s de una miniapp que quita duplicados. Perfil TEMP, música pendiente de acreditar.

**Ganchos**

| gancho | texto | tipo | puntos | elegido |
|---|---|---|---|---|
| G1 | ¿Cuántas veces pegaste lo mismo sin darte cuenta? | problema | 7 | sí |
| G2 | Lista limpia en un clic. | resultado | 5 | no |

**Escenas**

| escena | tiempo | voz literal | imagen y texto en pantalla | sonido | toma o recurso | claim |
|---|---|---|---|---|---|---|
| S01 | 00:00–00:04 | ¿Cuántas veces pegaste lo mismo sin darte cuenta? | Plano a cámara, subtítulo base abajo. Corte directo a pantalla al terminar la pregunta | Voz sola | T1 cámara frontal | — |
| S02 | 00:04–00:14 | Pego la lista, pulso limpiar y aquí queda sin duplicados. | Captura de pantalla. Clic visible al decir «pulso». Resultado en pantalla 2 s. Subtítulo fuera de los controles | Entra cama instrumental suave bajo la voz. Clic audible en «pulso» | T2 captura de la miniapp con datos de ejemplo | C1 |
| S03 | 00:14–00:20 | La misma lista, sin repetir nada. | Vuelve a cámara en «la misma lista». Acento «Lista *limpia*» 2 s, «limpia» en manuscrita | Música se funde al salir | T1 cámara frontal | — |

**Claims**

| claim_id | tipo | afirmación | prueba y límites |
|---|---|---|---|
| C1 | P | Quita líneas duplicadas de la lista pegada | Probado con la lista de ejemplo de la miniapp, versión 0.1. No distingue mayúsculas |
