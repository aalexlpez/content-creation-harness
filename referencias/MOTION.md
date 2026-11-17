# Referencias de motion graphics

Recursos estudiados el 2026-11-17 para subir el nivel de los motion graphics. Se estudia la **técnica**: no se copian diseños, imágenes, iconos, paletas ni identidades. Las decisiones que salen de aquí están en [DECISIONES](../registro/DECISIONES.md) (AV-008, AV-009) y el método, en [EDICION → Edición continua](../guias/EDICION.md#edición-continua).

## Lo que aprendimos

1. **El problema era de planteamiento, no de herramienta.** Hicimos piezas sueltas (hoja, rótulo, maqueta) en huecos pequeños alrededor de la cara. Lo que funciona es una capa gráfica continua ligada a cada frase, con una composición fija.
2. **Ilustrar la idea antes que la interfaz.** Recrear la app pantalla por pantalla obliga a leer; un diagrama que crece frase a frase se entiende al vuelo.
3. **Si se muestra la interfaz, a pantalla completa y legible.** Un celular pequeño en el centro deja el texto a ~20 px; a escala ×2,6 llega a ~44 px.
4. **Un sistema pequeño y repetido** (un estilo de iconos, una tipografía, el énfasis por inversión) se percibe como diseño.
5. **Cortar primero, animar después:** la capa necesita los tiempos por palabra del corte.

## Creador de referencia

| Recurso | Qué se estudió | Qué se toma |
|---|---|---|
| Reel de Erik Taveras en Instagram (`/reel/Df0ntGdutpy/`, 95,8 s, analizado fotograma a fotograma; el archivo solo estuvo en la carpeta temporal de la sesión) | Mitad superior oscura con el gráfico y mitad inferior con la cara; cabecera fija con título de tramo y contador («1 de 5»); un cambio cada 0,5–1,5 s ligado a la voz; diagramas de icono → flecha → icono que se reorganizan al crecer; subtítulos de 2–4 palabras con la palabra clave destacada; notas pequeñas en monoespaciada; barridos de líneas al cambiar de tramo | El método completo (E-01). No su verde, sus iconos ni su composición exacta |

## Herramientas y repositorios

| Recurso | Licencia | Veredicto |
|---|---|---|
| Catálogo de **HyperFrames** (`npx hyperframes catalog --json`, código en `heygen-com/hyperframes/registry/`) | Apache-2.0 | **El más útil.** 448 bloques con video de muestra; plantillas verticales de demos (`notes-reveal`, `message-thread-reveal`, `share-sheet-carousel`) y componentes de cámara (`cursor-zoom-follow`, `camera-rig-depth-stack`). Ya usamos sus técnicas: `render(t)`, cursor que sigue el texto y cámara que se acerca a cada toque |
| **video-shotcraft** (`Vincentwei1021/video-shotcraft`) | Apache-2.0 | Recetario de 124 planos con tiempos, curvas y sonido ([galería](https://vincentwei1021.github.io/video-shotcraft/)) y efectos reales de Freesound con control de licencias. Usado: giro *split-flap*, *blackout* al elegir, golpe de impacto y la barra como cortina. Hecho para Remotion y promos horizontales, probado solo en macOS |
| **GSAP** (gsap.com) | Licencia estándar sin coste | Desde la 3.13 los plugins (SplitText, Flip, CustomEase, MorphSVG) son gratis. Hoy solo usamos el núcleo 3.12.5 como reloj |
| **Freesound** (filtro CC0) | Por sonido | Fuente de efectos reales. Cada sonido se escucha antes y se apunta en Derechos (AV-008) |
| `yihui-dev/awesome-opus5-5-videos` | MIT | 703 prompts de videos hechos con Opus 5.5. Útil por el formato `<inputs>`/`<direction>`/`<structure>` y su lista explícita de prohibidos |
| `joeseesun/opus-video-prompts` | Sin licencia | 18 prompts comentados. Solo lectura |
| `lemomo-ai/lemo-opuscar` | MIT el código; CC BY-NC las guías | Descartado: sus efectos son sintetizados (contra AV-008) y está pensado para películas completas |
| `JohnHeibel/ClaudeAnimationBase` | MIT | Descartado: estética pintada a mano y un personaje de terceros (Clawd), contra la marca plana v2 |
| `pmndrs/react-three-rapier` y `pmndrs/react-postprocessing` | MIT | Descartados: física 3D y posprocesado (bloom, glitch) que la marca v2 prohíbe |
| `librosa/librosa` | ISC | Innecesario: HyperFrames ya mide audio (`audio`) y saca tiempos por palabra (`transcribe`) |

## Pendiente

- Probar en CapCut que importa las capas con alfa (MOV ProRes 4444 o WebM).
- Elegir los sonidos reales del ensayo (candidatos CC0 anotados en `videos/VID-0002/PRODUCCION.md`).
- Si la edición continua se aprueba (AV-009), convertirla en plantilla para la serie de miniapps.
