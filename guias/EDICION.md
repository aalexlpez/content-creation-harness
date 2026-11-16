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

Técnicas que se pueden pedir por escena: tipografía cinética sincronizada, transformación de un mismo elemento (*shared element*), aparición escalonada de campos, cámara virtual o parallax, microinteracción de toque, máscara para revelar el resultado, sonido ligado al evento, corte J/L con la voz y transiciones con sentido. Cada una debe poder comprobarse en tres fotogramas: antes, durante y después.

## Portada

Cada vídeo lleva su propia portada: título corto, un único foco (cara **o** producto) y, si hay serie, una marca de serie. Comprueba en cada red si se puede subir una portada propia antes de prometerla en el plan.

## Referencias visuales

En [referencias/LEER.md](../referencias/LEER.md). Sirven para estudiar la técnica. No se copian imágenes, tipografías, logos ni identidades.
