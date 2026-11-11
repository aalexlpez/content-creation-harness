**Marca de la composición:** utilizar identidad personal del creador Alexander. Solo colocar MiMiniApp en demos y explicaciones de ese producto, no como watermark del canal. Si no hay paleta personal aprobada, renders de prueba marcados TEMP; no exportar masters identificados como marca definitiva.

# Contrato de producción HyperFrames (motor principal)

## Alcance y hechos verificados
- HyperFrames es un proyecto HTML/CSS/medios + animación seekable (GSAP u otros adaptadores), renderizado determinista, editado por agente y Studio. Documentación oficial: https://github.com/heygen-com/hyperframes y skills oficiales.
- **El piloto observado por usuario fue parcial:** 8 s vertical, 60 fps y sin audio. El primer contenido publicable debe superar eso y validar sincronía, legibilidad y claims.
- No asumir que HyperFrames Studio puede abrir cada archivo que crea Claude ni exportar un proyecto CapCut nativo: comprobar capacidades por versión y exportaciones cortas.

## Pila técnica (propuesta)
HyperFrames Studio en Windows + Code/Codex con plugin/skills oficiales; HTML/CSS/GSAP; FFmpeg para inspección/export; fuentes y SFX originales/licenciados; 1080x1920, H.264/AAC, **30 fps iniciales**, no «mejor» universal. Previews por escenas primero. Si UI de la app no está lista, demo animada etiquetada como conceptual y NO PUBLICAR como producto funcional.

## Técnicas que se pueden solicitar por escena
| Código | Técnica | Prueba observable |
|---|---|---|
| T01 | Tipografía cinética | palabra y acento sincronizados, legibilidad móvil |
| T02 | Shared-element morph | un mismo elemento conserva posición/identidad al transformarse |
| T03 | Reveal escalonado de formulario | labels/inputs separados, intervalos claros |
| T04 | Cámara virtual/parallax | profundidad perceptible sin pérdida de legibilidad |
| T05 | Microinteracción tap/auto-fill | respuesta de botón y datos de ejemplo correctos |
| T06 | Gradient/grid/background motion | soporte visual, nunca protagonismo gratuito |
| T07 | UI glass / profundidad | contraste y blur sin perder lectura |
| T08 | Máscaras y reveal de resultados | resultado validado y momento de payoff |
| T09 | Sonido diegético/SFX | evento y sonido alineados, licencia documentada |
| T10 | J/L cut + voz | audio continuo y cambio de imagen intencional |
| T11 | Subtítulos | fidelidad a la voz, sin tapar CTA/UI |
| T12 | Transiciones semánticas | conexión entre escenas, sin efecto por rellenar |

## Gramática por escena obligatoria
`escena:ID | mensaje:... | A-roll/VO:... | duración objetivo | elementos:... | movimientos:... | estado inicial/intermedio/final | trigger:... | técnica Txx | sonido:... | fuente del dato | claim P/E/O/H/X | cierre:...`.

## Fuente visual del motor
HyperFrames prioriza `frame.md` / `design.md` / `DESIGN.md` como fuente de estilo según sus skills. Este paquete **NO incluye `frame.md` todavía**, porque la marca audiovisual está pendiente. Tras B0, ejecutar `scripts/preparar_frame_md.py`, que lee SOLO `brand/IDENTIDAD_APROBADA.json` y exige estado y firma antes de generar `frame.md`. Fuente: https://github.com/heygen-com/hyperframes/blob/main/skills/general-video/SKILL.md


- `style` y contenido artístico están gobernados por `brand/IDENTIDAD_APROBADA.json` **si existe**; nunca inventar tokens para marca aprobada. En ausencia de aprobación usar TEMP y bloquear master público.
- La escena principal no tiene por qué reutilizarse. Reutilizar solo patrones de estilo/movimiento y código cuando simplifique de verdad.
- Exigir pistas editables y IDs estables según skill HyperFrames de versión instalada. Elementos que requieren independencia deben existir como clips/timed elements, no quedar todos dibujados en un único canvas opaco.
- Seek a fotogramas arbitrarios para probar estado inicial/intermedio/final; evitar transiciones CSS no reproducibles como dependencia del estado de página.
- Exportar un preview completo y, si CapCut se utiliza, stems opcionales (escenas MP4 + overlays alfa donde la versión lo permita). No prometer exportación de proyectos CapCut editables.
- Incluir `audio` y comprobar que la salida contiene pista audible si así lo requiere el guion; la primera prueba careció de ella.

## Gates técnicos de aceptación
1. Render vertical válido, fps/resolución planificados y duración dentro del contrato.
2. Sin saltos no intencionados, overlap de capas, letras fuera de cuadro, flicker ni activos rotos.
3. Morph entendible en tres frames (antes, transición, después).
4. Efectos sonoros originales/licenciados y pista de voz verificable cuando se especificó audio.
5. Subtítulos correctos y dentro de zonas seguras verificadas en móvil; conservar copia sin subtítulos solo si aporta.
6. Un único foco por plano, primer mensaje comprensible sin introducción larga.
7. Evidencia de claims (producto real o identificador conceptual) en `PRUEBAS_Y_CLAIMS.md`.
8. Registro de cambios y prueba física de MP4 antes de marcar G7.

## Si el agente se desvía
No pedir «hazlo más profesional». Abrir `REVISION.md` con timecode, defecto observable, cambio solicitado, verificación y límite. Si dos rondas no resuelven, revisar la técnica o alcance, no generar 20 versiones aleatorias.

## Intercambio con editor gratuito (v3.4)
Cuando el storyboard prevea acabado posterior en CapCut Gratis/Shotcut, renderizar por escena **MP4 1080x1920/30fps** con nombres/IDs estables, más audio separado y SRT si corresponde. No incrustar subtítulos si el humano necesita corregirlos en montaje. Opcionalmente entregar overlays transparentes, **pero solo si la importación alfa se verificó en el editor instalado**; en caso contrario exportar escenas completas ya compuestas. Nunca prometer exportación de proyecto nativo editable de CapCut. Consultar `15_MONTAJE_FINAL_GRATUITO.md`.

## Requisitos de intercambio v3.5
El expediente del vídeo contiene `SCRIPT.md`, `PRUEBAS_Y_CLAIMS.md`, `INGESTA.md`, `LICENCIAS_MEDIOS.md` y `QC_MASTER.md`; nunca se aceptan campos vacíos como verificados. Para medios originales del Samsung se emplea `media/camera/original/`; proxys aparte. El master sigue el perfil de `18_INGESTA_COLOR_EXPORT_Y_QC.md`. G7 es el bloqueo de imagen (*picture lock*), G7.5 el acabado + control del archivo final.
