# VID-0002 · Plan v06 (recursos, música y estándar)

Plan del 2026-11-19, tras el análisis del 2026-11-19 y los comentarios de Ale. **Es un plan:** no se ejecuta sin el OK de Ale.

Parte de la v05 y del ensayo flotante (mismo corte de 55,48 s, misma voz mejorada). Reglas: [EDICION → Música](../../../../guias/EDICION.md#música-cómo-elegirla-y-sincronizarla), [EDICION → Planos de recurso](../../../../guias/EDICION.md#planos-de-recurso-b-roll) y [EDICION → Hacia un estándar estable](../../../../guias/EDICION.md#hacia-un-estándar-estable). Tiempos: los del corte v04/v05.

## 1. Lo que Ale aclaró (2026-11-19)

- El bruto está en **4K (13 min)**; el corte se exportó de CapCut en 1080×1920.
- El set: luz azul suave de fondo y luz cálida al otro lado de la cara, a ≈ 1 m de la pared; no hay más espacio. Se puede añadir un cuadro o una luz detrás.
- El micrófono va enganchado, no en la mano.
- Los recursos propios tienen que estar en el plan de grabación (ya está en [GUIONES](../../../../guias/GUIONES.md) y en `/rodaje`).
- Para B-roll y música hace falta un plan concreto: qué, para qué y dónde buscar.

## 2. Ruta 4K

1. **Probar primero en CapCut:** en Exportar → Resolución, ver si ofrece 2K o 4K en la versión gratis. Si lo ofrece sin marca de agua, exportar el mismo corte en 4K (solo vídeo, como el paso 1 de EDICION).
2. **Si no:** dejar el bruto 4K en `media/originales/` (≈ 2–3 GB). Claude reconstruye el corte en 4K buscando cada tramo del corte en el bruto por su audio (correlación de la forma de onda) y comprueba la coincidencia fotograma a fotograma.
3. **Qué gana:** acercamientos del 110–130 % sin perder nitidez y simular un segundo plano (cerrado) en las frases clave. El vídeo final sigue en 1080×1920.

## 3. Recursos (B-roll)

> **Actualización 2026-11-19:** Ale no puede grabar recursos propios por ahora («solo puedo buscarlos»). Para este vídeo **todos los recursos son de stock** (lista de abajo, columna «buscar»); R05 y R06 se quedan con la maqueta. La regla general de [EDICION](../../../../guias/EDICION.md#planos-de-recurso-b-roll) («primero propios») sigue para cuando sea posible.
>
> **Dónde dejarlos:** `media/originales/broll/` con el código delante (`R02_zapatillas.mp4`), y el enlace de la página de cada uno en `media/originales/broll/fuentes.txt` (para Derechos). Van casi siempre **a pantalla completa** (1–1,5 s, con la voz debajo), así que necesitan resolución: **vertical en 1080 o más, u horizontal solo en 4K** (un horizontal de 1080 recortado a 9:16 queda en 608 px de ancho y se ve borroso). Si es horizontal, que lo importante esté en el centro. Clips de 5–15 s (se usa 1–1,5 s).

Primero propios (se graban en 10–15 min en la próxima sesión); stock solo donde no se puede grabar. Duración en pantalla 1–1,5 s, con la voz debajo; la cara vuelve antes de que termine la frase.

| Código | t (s) | Frase | Qué se ve | Origen | Si es stock, buscar |
|---|---|---|---|---|---|
| R01 | 0,3–1,3 | «Es febrero…» | Un calendario o agenda real que pasa de enero a febrero (mano que pasa la hoja) | **Propio** | — |
| R02 | 1,6–2,6 | «…ya abandonaste tu propósito» | Zapatillas de correr junto a la puerta, sin usar; o una pesa con polvo | **Propio** | Pexels: «running shoes by door», «dusty dumbbell» |
| R03 | 6,4–7,6 | «…hemos tirado la toalla» | Una toalla que cae al piso, a cámara lenta (grabada a 60 fps) | **Propio** | Pixabay: «towel falling floor» |
| R04 | 9,3–10,6 | «…no piensa en qué va a hacer ese día» | Tú en el sofá con el celular, sin ganas (de espaldas o de perfil) | **Propio** | Pexels: «tired person couch phone» (sin cara) |
| R05 | 15,2–16,8 | «Esta es una nueva aplicación…» | Manos con el celular abriendo Plan B en el navegador | **Propio** (cuando la app esté publicada; mientras, la maqueta) | — |
| R06 | 38,5–40,0 | «…un recordatorio en tu calendario y tu plan como fondo de pantalla» | Un celular real que vibra con el recordatorio y su pantalla de bloqueo con el plan | **Propio** (con la app publicada) | — |
| R07 | 45,6–46,4 | «productividad» | Escritorio con agenda y lápiz, desde arriba | Stock | Pexels: «planner desk top view» |
| R08 | 46,8–47,6 | «ciencia» | Matraz o microscopio, de detalle | Stock | Pixabay: «science lab close up» |
| R09 | 48,0–48,8 | «minijuegos» | Manos con un mando o un celular con un juego | Stock | Pexels: «hands game controller» |

**Para el ensayo actual (sin regrabar):** solo los de stock (R07–R09) y, si Ale los graba aparte en 10 minutos con el mismo set, R01–R04; se insertan sobre el mismo corte porque la voz no cambia. R05 y R06 esperan a la app publicada.

**Lista para la próxima sesión de grabación** (va a PRODUCCION → Rodaje con `/rodaje`): R01, R02, R03 (a 60 fps), R04, y R05–R06 cuando exista la app. 2 versiones de 3–5 s cada una, trípode, misma luz, nada personal en pantalla.

## 4. Música

**Brief** (por tramos, tiempos del corte):

| Tramo | t (s) | Energía |
|---|---|---|
| Gancho | 0–4,6 | Intro mínima o solo un pulso |
| Problema | 4,6–12,8 | Entra la batería, suave |
| Solución | 12,8–22,7 | Subida |
| Demo | 22,7–36,5 | Parte principal, groove |
| Resultado | 36,5–41 | **Pico:** el sello cae en un tiempo fuerte |
| Serie | 41–50,3 | Se mantiene; los tres recursos R07–R09 van a tiempo |
| Cierre | 50,3–56,5 | Baja; **silencio 0,4 s antes de «no.»** (53,26) y golpe; final en seco |

- **Tempo:** 95–115 BPM. **Duración de la pista:** 1–3 min, con intro, subida y caída claras.
- **Dónde:** Pixabay Music (el banco de Ale). Búsquedas: «upbeat tech», «modern vlog beat», «motivational beat», «future bass uplifting», «minimal electronic». Filtro de duración 1–3 min. Evitar las que digan que están registradas en Content ID.
- **Cómo se elige:** Claude propone 5 enlaces que cumplan el brief; Ale escucha y elige 2–3; Claude las monta sobre el vídeo (con la voz) y Ale elige la final **escuchándola montada**.
- **Sincronía:** `hyperframes beats` sobre la pista elegida; tiempo fuerte en la entrada de la demo (22,7) y en el sello (36,54); compases editados en los cambios de tramo; transiciones al tiempo fuerte más cercano (±0,12 s). La voz no se mueve.

## 5. Imagen y capa gráfica (lo aceptado del análisis)

1. **Grado de color** suave de la toma de cámara (contraste, piel, viñeta leve), constante en todo el vídeo, y el mismo en los recursos.
2. **Movimiento de cámara continuo** casi imperceptible (100 → 103 % por frase) y acercamientos fuertes (120–130 %, en 4K) solo en 3–4 frases.
3. **Apertura en frío:** 1–1,5 s del resultado (el sello cayendo o el fondo de pantalla) antes de «Es febrero…».
4. **3–4 momentos protagonistas** (el sello, «Plan B» llenando el cuadro, el fondo de pantalla, «Este febrero, *no*.»); el resto, discreto. **Flechas: 2–3 en todo el vídeo.**
5. **La demo** como celular en perspectiva sobre la toma desenfocada (AV-002), en lugar del rectángulo sobre el panel.
6. **Estilo:** decidir entre E-01 (escenario) y flotante (AV-013, resplandor blanco). Recomendación: flotante para el resto y celular en perspectiva para la demo, **con el resplandor más contenido** (solo en los momentos protagonistas).

## 6. Qué necesita el sí de Ale

| # | Qué | Recomendación |
|---|---|---|
| 1 | Probar la exportación 4K en CapCut, o dejar el bruto 4K en `media/originales/` | Sí |
| 2 | Grabar R01–R04 (10–15 min, mismo set) | Sí, para el ensayo; si no, solo stock |
| 3 | Que Claude busque y proponga (sin descargar) los recursos de stock R07–R09 y 5 pistas de música | Sí |
| 4 | Estilo: flotante con resplandor contenido y demo en perspectiva (AV-013) | Sí, como prueba |
| 5 | Descargar lo elegido (stock y música) a `media/trabajo/` | Tras escucharlo/verlo |

## 7. Orden de trabajo (cuando Ale apruebe)

1. 4K (§2) y, si se graban, ingesta de R01–R04.
2. Búsqueda de stock y música; Ale elige.
3. v06 sobre el corte: color, cámara, apertura en frío, protagonistas, recursos, demo en perspectiva.
4. Música montada y sincronizada; escucha de Ale en el celular.
5. Con la v06 aprobada, empieza la estandarización (EDICION → Hacia un estándar estable): `eventos.csv`, librería de componentes y `editar.py`.

## 8. v06 hecha (2026-11-19)

Ale eligió y descargó los recursos y la música («Ahí tengo todo»); sin 4K por ahora. Proyecto: `hyperframes/v06/` (`preparar.py` → `index.html` → `mezcla.py`).

**Recursos usados** (todos de stock, `media/originales/broll/`; cortes en golpes de la música):

| Código | tn (s) | Frase | Tramo del clip | Cómo va |
|---|---|---|---|---|
| R01 | 0–1,325 | «Es febrero y ya» | 2,55 s (la mano pasa la hoja de enero a febrero) | Tarjeta 940×940 sobre su imagen desenfocada (horizontal 1080) |
| R02 | 1,325–2,985 | «abandonaste tu propósito de año nuevo» | 2,00 s | Pantalla completa (4K recortado), con ABANDONASTE encima |
| R03 | 6,695–8,345 | «hemos tirado la toalla» | 0,50 s | Pantalla completa (vertical 4K) |
| R04 | 9,175–10,835 | «no piensa en qué va a hacer» | 1,00 s | Tarjeta |
| R07 | 45,60–46,84 | «productividad» | 0,00 s | Pantalla completa (4K recortado) |
| R08 | 46,84–48,075 | «ciencia» | 1,00 s | Tarjeta |
| R09 | 48,075–49,315 | «minijuegos» | 5,50 s | Pantalla completa (vertical 4K) |

**Música** (`top-flow-happy-rock.mp3`, 145 BPM, 0,414 s por golpe): montada por tramos en `preparar.py` (lista `SEG`). Estribillo en la apertura en frío, intro en el gancho, batería en «Pero…», estribillo en «Plan B» (14,56), valle en la demo (22,84, con un golpe de anacrusa para que el siguiente punto cuadre), estribillo 2 en el sello (36,50), subida en «cualquier ámbito» (49,74), **silencio de 0,4 s** y golpe en «febrero» (53,26) y final en seco al octavo golpe (56,58). Los empalmes caen en golpes; la voz no se mueve.

**Imagen:** apertura en frío de 1,24 s (el plan como fondo de pantalla en un celular sobre la cara desenfocada; se va con un zoom al primer golpe del gancho), grado de color y viñeta constantes (también en los recursos), deriva de cámara 100 → 103 % por plano, demo en un celular en perspectiva sobre la cara desenfocada y oscurecida (los encuadres de la v05 se convierten en acercamientos al celular; los insertos llevan la maqueta a pantalla completa), 3 flechas en todo el vídeo, sin resplandor salvo en los protagonistas («Plan B», el sello y «no.») y en la apertura. Los subtítulos se apagan mientras está la palabra protagonista (ABANDONASTE, CALMA, «Plan B»).

**Correcciones de Ale tras verla (2026-11-19) → v06b** (`media/trabajo/edicion_v06b*.mp4`):

| Comentario de Ale | Cambio |
|---|---|
| El inicio no se entiende: «una foto de fondo y música alta», sin contexto, y pasa un segundo hasta que hablo | **Fuera la apertura en frío.** El vídeo empieza con la voz y con R01 (el calendario que pasa a febrero) desde el primer fotograma; la música empieza en la intro suave. Regla nueva en EDICION: nada antes de la primera palabra |
| La transición entre los recursos de las zapatillas y la toalla es demasiado rápida; no se entiende la relación entre imagen y narración | R01–R04 pasan de 3 a **4 golpes (≈ 1,65 s)** y cubren la frase entera (R02 hasta «año nuevo», R03 hasta después de «toalla», R04 hasta «hacer»). Los de la serie (R07–R09) se quedan en 3 golpes: son una lista |
| Una flecha se queda flotando cuando se va la tarjeta de la que sale | Las flechas terminan, como tarde, cuando se va su primera tarjeta (lo calcula la composición); la de cerobytes → teléfono acababa 1,8 s después de la etiqueta |

**Segunda corrección de Ale → v06c** (`media/trabajo/edicion_v06c*.mp4`): un «corte abrupto» entre «nuevo» y «calma» (3,2 s) donde no hay corte. Causa: la deriva de cámara (100 → 103 %) se reiniciaba en límites que no son cortes (3,20; 3,82; 12,79; 15,23; 53,26); el plano de 2,985 a 3,20 duraba 0,2 s, así que subía un 3 % muy rápido y volvía de golpe. Ahora la deriva solo vuelve a 100 % en cortes reales (vuelta de un recurso, demo, empalmes de KEEP).

**Inicio con la cara → v06d** (`media/trabajo/edicion_v06d*.mp4`): a propuesta de Claude, aceptada por Ale («Sí, pruébalo»). El vídeo abre con Ale hablando a cámara y R01 como tarjeta de 480 px flotando en el pecho (inclinada −3°, sin tapar la boca) mientras dice «Es febrero»; las zapatillas siguen a pantalla completa. Motivo: es una serie con su cara y el gancho es una frase directa; así se ven la cara y el contexto desde el primer fotograma.

**Demo con la app REAL → v06e** (`media/trabajo/edicion_v06e*.mp4`, petición de Ale del 2026-11-19: «la aplicación está desarrollada completamente»). Sustituye la maqueta MG-06/MG-07 por la app de staging (`miminiapp-staging…/es/apps/plan-b/`, repo `aalexlpez/miminiapp`):

- **Grabación:** `hyperframes/v06/demo/grabar.mjs` con el Chrome de HyperFrames (sin instalar nada): iPhone de 393×852 pt a 1080×2342 px, tema claro, fotograma a fotograma con las animaciones de la app ralentizadas para que vayan a su velocidad real. Cada toque y cada tecleo están en `ACCIONES`, en el tiempo de la voz: la app hace cada cosa cuando Ale la dice, sin acelerar ni cortar. Fotogramas en `media/trabajo/demo_real/toma4/` y vídeo en `toma4.mp4`.
- **Fecha emulada en enero de 2027** (el reloj sigue corriendo): en noviembre la app dice «1 de diciembre»; en enero dice «este año» y «1 de febrero», que es lo que verá quien use la app cuando salga el vídeo. No se inventa nada: es su comportamiento real en enero.
- **Recorrido grabado:** idea «Hacer ejercicio» → «Imagina que es 1 de febrero…» → «No tuve tiempo» → «llego a casa después de las 20:00» → «hago 5 minutos de estiramientos» → «Ver mi plan» → «Añadir recordatorio» (20:00, de lunes a viernes) → «Tu fondo de pantalla». No se pulsa Google Calendar, ni descargar, ni compartir.
- **Composición:** celular de proporción real (19,5:9), 13 encuadres nuevos que siguen la voz (dos a todo el ancho: «No tuve tiempo» y el plan con el estribillo 2), el celular se encoge al teléfono flotante después de «fondo de pantalla» (tn 40,95). Efectos de la demo: un toque de pantalla por cada toque real.
- **Lo que cambia frente al guion:** la app no tiene el sello «Este febrero, no.» (la maqueta sí); el golpe 2 cae ahora en la aparición del plan. El sello del cierre es gráfico del vídeo y se mantiene.
- **Para los claims (no se tocó el GUION aprobado):** C3 y C4 se ven tal cual en staging (recorrido, recordatorio .ics/Google Calendar y fondo de 1179×2556); siguen en H hasta que la app esté publicada y probada en iPhone y Android. C5: la app dice «Gratis y sin cuenta». **C10 («libres» = código abierto): el repo es público pero no tiene licencia (`package.json`: `"license": "UNLICENSED"`, sin archivo LICENSE), así que hoy no es código abierto;** sigue en H.
- **Textos de la app con expresiones de España** (fuera del alcance de este vídeo, son de la app): «has abandonado», «lo has dejado. ¿Qué ha pasado?», «el móvil». Se ven en pantalla en la demo.

**Color: look B → v06f** (`media/trabajo/edicion_v06f*.mp4`). Ale eligió el look B («cálido cinematográfico») entre tres propuestas (`media/trabajo/revision_v06/looks_color.png`). Va en `preparar.py` (`LOOK_B`, `PIEL`) y se aplica con ffmpeg antes de la composición, no con un filtro CSS: curva en S suave, sombras frías y luces cálidas y piel suavizada respetando bordes en el corte; la misma curva y temperatura, sin suavizado, en los recursos. La viñeta sigue en la composición.

**Pendiente de Ale:** escuchar las dos mezclas en el celular; los enlaces de cada recurso y de la canción en sus `fuentes.txt` (Derechos), y si la canción dice que está registrada en Content ID; decidir el resplandor (AV-013).
