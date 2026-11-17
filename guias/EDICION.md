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

**Orden de trabajo:** primero el corte, después la capa. Los tiempos por palabra de la versión cortada son la base; con el bruto solo se puede planificar. Pasos: (1) transcripción con tiempos (`hyperframes transcribe`, ver [TECNICA](TECNICA.md)); (2) lista de eventos por frase, que Ale revisa; (3) composición sobre el corte; (4) revisión con capturas y `hyperframes check`; (5) sonidos reales en una segunda pasada.

## Portada

Cada vídeo lleva su propia portada: título corto, un único foco (cara **o** producto) y, si hay serie, una marca de serie. Comprueba en cada red si se puede subir una portada propia antes de prometerla en el plan.

## Referencias visuales

En [referencias/LEER.md](../referencias/LEER.md). Sirven para estudiar la técnica. No se copian imágenes, tipografías, logos ni identidades.
