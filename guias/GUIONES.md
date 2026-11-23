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
| Texto_en_pantalla | Los tres niveles de [MOTION §10.2](MOTION.md) (frase, clave y escenario): qué claves y qué escenarios, y el acento final |
| Color | Tratamiento de la toma de cámara. La captura de pantalla conserva su color |
| Perfil_visual | v2 (identidad aprobada, ver [IDENTIDAD](../marca/IDENTIDAD.md)) |

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

## 2 bis. Storytelling: personaje, conflicto y cambio

**Estado:** propuesta (PR-004). Las familias de §2 dicen *qué* contar; esta sección dice cómo convertirlo en una historia que se quiera ver hasta el final. Se aplica a todas las familias y se comprueba antes del OK-2.

### Las tres piezas que no pueden faltar

| Pieza | Pregunta | En VID-0003 |
|---|---|---|
| **Personaje con deseo** | ¿Quién quiere qué? | Ale quiere cumplir sus metas del año |
| **Obstáculo con algo en juego** | ¿Qué se lo impide y qué pierde si falla? | Todos los años las deja en enero; el día que no tiene ganas, no hay plan |
| **Cambio** | ¿Qué es distinto al final, para él y para quien mira? | Este año tiene un Plan B para ese día, y tú también puedes tenerlo |

Si falta una, el vídeo es una explicación, no una historia. **El cambio tiene que ser verdad**: si todavía no ha pasado, se cuenta como intención o como proceso («este año lo voy a probar»), nunca como resultado.

### El arco corto (20–45 s)

Cinco tiempos. Encajan dentro de cualquier familia y se marcan en la tabla Escenas.

1. **Antes** (0–3 s): una escena concreta del problema, en primera persona o en segunda («Todos los años dejo mis metas en enero»). Es el gancho.
2. **Deseo y obstáculo** (3–8 s): qué se quiere y por qué no sale. Aquí entra el **«pero»** (§3 bis).
3. **Giro** (8–12 s): la decisión, la idea o la herramienta. Aquí entra el **«por eso»**.
4. **Prueba** (12–25 s): se ve funcionar. Es el tramo más largo y no se esconde el límite.
5. **Después** (últimos 3–5 s): el cambio en una frase y la invitación. Responde a la primera frase para cerrar el bucle.

La plantilla de una línea es **ABT** («Y… pero… por eso…»): si el guion no se puede resumir así, falta el conflicto.

### Reglas de oficio

- **Concreto antes que general.** Una escena, una hora, un objeto: «jueves, 8 de la noche, sin ganas», no «la falta de motivación».
- **Lo que está en juego se dice o se ve.** Perder algo pequeño y cercano (la racha, el propósito, una noche) pesa más que una cifra abstracta.
- **Vulnerabilidad solo si es verdad.** La confesión funciona porque es de Ale; se confirma con él y se registra en Claims como tipo O (C1 de VID-0003).
- **Un solo personaje en primer plano.** Ale o quien mira, no los dos a la vez en la misma frase.
- **Tensión antes de la respuesta.** Una pausa o un silencio de 0,3–0,6 s antes del giro o del resultado (los picos de §3 bis).
- **Cada frase empuja a la siguiente** con «pero» o «por eso». «Y además» es señal de lista, no de historia.
- **Callback.** El cierre repite una palabra o una imagen del principio, transformada («enero» → «este año, sí»).
- **Bucles abiertos entre vídeos.** Una pregunta que solo responde el siguiente episodio, únicamente si ese episodio existe o está fechado (ver el arco de la serie en `proyectos/miminiapp/SERIE.md`).

### Por familia

| Familia | Personaje y deseo | Obstáculo | Cambio |
|---|---|---|---|
| A · Demo | Quien mira, con un problema cotidiano | La fricción concreta | El resultado en sus manos |
| B · Proceso | Ale construyendo | Lo que no funcionaba (verdad) | La decisión y el avance verificable |
| C · Experimento | Ale con una pregunta | La hipótesis que puede fallar | Lo que se aprendió, incluido si falló |
| D · Comunidad | La comunidad | Una decisión abierta | Qué se hará con sus respuestas |
| E · Tutorial | Quien desarrolla | El paso difícil | El resultado funcionando en su máquina |

### Comprobación de historia (antes del OK-2)

- [ ] Se resume en una línea ABT.
- [ ] Hay personaje, deseo, obstáculo y cambio, y el cambio es verdad o se presenta como intención.
- [ ] La primera escena es concreta y está en los primeros 3 s.
- [ ] El giro está antes del 40 % del vídeo y la prueba antes del 70 %.
- [ ] El cierre hace callback al principio.
- [ ] Cada frase de la confesión y del cambio está en Claims con su tipo.
- [ ] La voz coincide con [PERSONAJE](../marca/PERSONAJE.md) (tono, palabras propias, lo que no se dice).

## 3. Ganchos

1. Escribe **dos**: uno desde el problema y otro desde el resultado. 18 palabras como máximo.
2. Puntúa cada uno de 0 a 2 en cuatro criterios: se entiende sin contexto, coincide con el contenido, la prueba aparece pronto e interés genuino sin clickbait. Total sobre 8.
3. Gana el de mayor puntuación. En empate, el más claro. Anótalo en la tabla Ganchos (`elegido: sí`).
4. Si los dos fallan, **una** reescritura. Si siguen fallando, el problema está en la idea, no en las palabras.
5. No empieces con «Hola, soy…». Abre con acción o con el conflicto. La presentación, si hace falta, después de ganarte los primeros segundos.

## 3 bis. Retención: picos y encadenado

Reglas que se repiten en los vídeos cortos que retienen (sin cifras propias todavía; se medirán con METRICAS):

1. **Gancho triple en 0–2 s:** voz, imagen y texto cuentan lo mismo a la vez.
2. **Brecha de curiosidad:** el gancho abre una pregunta que solo responde el vídeo.
3. **Concreto mejor que abstracto:** una escena («jueves, 8 de la noche») vale más que un concepto («falta de motivación»).
4. **Segundo gancho a los 3–6 s:** una frase que sube la apuesta cuando el espectador decide si se queda.
5. **«Pero» o «por eso», no «y entonces»:** cada frase empuja a la siguiente con un giro o una consecuencia.
6. **El valor antes del 70 %:** el resultado aparece pronto, no al final.
7. **Tres picos, uno por tercio** (gancho, revelación y cierre), cada uno con golpe de música, corte y palabra protagonista. Entre picos, un cambio de imagen o gráfico como mucho cada 3 s (cada 1–2 s en el gancho), como en [MOTION](MOTION.md).
8. **Final que responde al inicio:** la última frase cierra lo que abrió la primera y el último plano encaja con el primero, para el bucle.

**Tipos de gancho:** confesión (primera persona, solo si es verdad), contraste («Planeaste X. ¿Planeaste Y?»), escena concreta, contraria («no falla por A, falla por B»), advertencia y pregunta directa. Se escriben varios, se puntúan y se graban 2–3 tomas del segundo mejor como alternativa. Un gancho tiene que funcionar **el día que se publica** (VID-0003: «Es febrero…» no servía para el 1 de enero).

## 4. Voz y estilo

- Primera persona, natural y concreta: «creé», «voy a probar», «todavía no funciona».
- **Español latinoamericano** (CONTENIDO-LATAM-001): «celular», «link», «computadora» y pretérito simple («abandonaste», no «has abandonado»). Nada de expresiones de España.
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

**Recursos (B-roll) en la columna «toma o recurso».** Además de la toma a cámara, cada escena que lo pida lleva sus planos de recurso con código `R01`, `R02`…: qué se ve, duración (1–3 s) y origen. **Propio** si Ale lo puede grabar en la misma sesión (objetos, manos, el celular, la pantalla real de la app) y **stock** solo si no se puede grabar (un gimnasio vacío, un laboratorio). Debajo de la tabla de escenas va la lista «Recursos que grabar», para que `/rodaje` la convierta en tomas. Criterios en [EDICION → Planos de recurso](EDICION.md#planos-de-recurso-b-roll).

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

Demo de 20 s de una miniapp que quita duplicados. Perfil v2, música pendiente de acreditar.

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
