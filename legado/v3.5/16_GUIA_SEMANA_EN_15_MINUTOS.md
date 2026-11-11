# Manual de uso rápido — de lunes editorial a publicación
**Primera lectura recomendada.** Consulta `19_MAPA_DOCUMENTAL_Y_FRECUENCIA.md` para entender cada documento del paquete. Los «15 minutos» describen la lectura y configuración básica de la sesión, NO prometen producir contenido en 15 minutos.

## A. ¿Dónde trabajo?
- **Proyecto editorial:** Claude Cowork, ChatGPT Work o ChatGPT Web. Lee y actualiza el directorio `Alexander-Contenido`. Si la plataforma no puede escribir en Windows, descarga archivos nuevos y cópialos tú al canónico. Un único directorio, nunca tres versiones paralelas.
- **Vídeo/animación:** Claude Code o Codex + HyperFrames; consume exclusivamente el dossier aprobado del vídeo actual y `07_ESPECIFICACION_HYPERFRAMES.md`.
- **Acabado opcional:** CapCut Desktop Gratis (sin recursos Pro); si hay bloqueo/limitación, Shotcut. Retoques sencillos ahí NO requieren tokens de Code.
- **Aprobación:** Alexander. La IA no reserva usuarios, no elige una miniapp, no publica ni compra servicios sin orden expresa.

## B. Antes de la primera semana, una sola vez
1. Descomprimir este paquete en `C:\Proyectos\Alexander-Contenido` (ejemplo) y conservar ZIP original como respaldo.
2. Revisar `registro/ESTADO.md` y `registro/DECISIONES.md`; ejecutar **P00**.
3. Definir/aprobar estrategia e identidad audiovisual PERSONAL en B0: `02_ESTRATEGIA_EDITORIAL.md`, `03_IDENTIDAD_AUDIOVISUAL.md`, `12_IDENTIDAD_PERSONAL_Y_HANDLES.md`. El @handle puede quedar pendiente para planificación, pero no se inventa para publicación.
4. Solo después de aprobación B0, crear `brand/IDENTIDAD_APROBADA.json` y generar `frame.md` con `python scripts/preparar_frame_md.py`.
5. Instalar HyperFrames una vez, validar un render con audio y probar una exportación sencilla de CapCut/Shotcut. No fijar herramienta por afirmaciones no probadas.

## C. Principio de semana: la secuencia exacta

| Paso | Abrir / usar | Qué le pides a la IA | Qué revisas tú | Qué queda guardado |
|---|---|---|---|---|
| 1 | `registro/ESTADO.md`, última retro + P01 | Hasta 6 ideas según estado real y horas de contenido disponibles | Seleccionas vídeos y horas; G1 | `semanas/AAAA-WNN/PLAN.md` |
| 2 | `02_ESTRATEGIA_EDITORIAL.md`, `04_SISTEMA_DE_GUIONES.md`, P02/P03 | 2 ganchos, 1 guion literal, storyboard escena a escena | Apruebas G2 y afirmaciones | `Vxx/BRIEF.md`, `SCRIPT.md`, `PRUEBAS_Y_CLAIMS.md` |
| 3 | `TAKES.md`, P04/P17 y `18_INGESTA_COLOR_EXPORT_Y_QC.md` | Lista de grabación por lotes y control de archivos originales | Grabar Samsung y aprobar G3/G4 | `Vxx/TAKES.md`, `INGESTA.md`, `media/camera/original/` |
| 4 | P05 + `07_ESPECIFICACION_HYPERFRAMES.md` | Plan técnico solamente, sin animar todavía | Apruebas G5 | `Vxx/EDIT_PLAN.md` |
| 5 | P06/P07 + HyperFrames | Animar escena crítica y rough cut, exportar previews | Revisas G6 | `preview/`, `REVISION.md` |
| 6 | P08/P15/P16 + CapCut gratis si es necesario | Correcciones localizadas, stems/escenas | Picture lock G7; QC G7.5 en móvil | `MONTAJE_FINAL.md`, `QC_MASTER.md`, master |
| 7 | `PUBLICACION.md`, P10 | Preparar portada, título, copies; consolidar datos aportados | Publicas tú; G8/G9 | URL reales, `ENTREGAS.csv`, `METRICAS.csv`, `RETRO.md` |

**No se salta un gate** porque la IA haya terminado antes. La cantidad de vídeos semanal se ajusta a tu tiempo real (11–15 h para TODO MiMiniApp, incluido desarrollo), no al calendario deseado de 3/2/4.

## D. Qué carpetas crea el script
En Windows, desde la carpeta raíz:
```powershell
python scripts\crear_semana.py 2026-W46 2
```
Crea semana 2026-W46 con dos expedientes `V01`, `V02` **en BORRADOR**, carpeta `ideas/` y `RETRO.md` en borrador. No autoriza esos dos vídeos. Cambia código/fecha y número según el lote decidido. Puedes abrir semana con 0 expedientes si aún no has aprobado ideas; después crea un expediente mediante plantillas.

Cada `Vxx` tiene documentos editoriales en la raíz, `media/camera/original/` (archivo exacto Samsung), `media/camera/proxy/` (solo si se necesita), `media/audio/`, `hyperframes/`, `exports/` (escenas/audio/subtítulos), `montaje_final/`, `preview/` y `delivery/` (master, portada, metadatos).

## E. Prompt de inicio listo para pegar en Cowork, Work o ChatGPT Web
> Abre semana **[AAAA-WNN]** según `05_SOP_SEMANAL_Y_GATES.md`. Lee `registro/ESTADO.md`, `registro/DECISIONES.md`, `02_ESTRATEGIA_EDITORIAL.md`, `04_SISTEMA_DE_GUIONES.md` y el último cierre. Dispongo de **[X] horas exclusivamente para contenido**; el estado verificable del producto es **[X]**; estas son mis ideas/comentarios con evidencia: **[X]**. Ejecuta **P01**, propone máximo 6 ideas con prueba y coste estimado, deja `PLAN.md` BORRADOR y detente en G1. No escribas guiones todavía. Indica archivos modificados, pendientes y aprobación necesaria.

## F. Ejemplo de aprobación
> Apruebo G1 de 2026-W46, PLAN v0.2: V01 demostración y V02 historia de desarrollo. V03 queda aplazado. Registra fecha y responsable. Puedes preparar BRIEF/SCRIPT como BORRADOR; todavía NO apruebo G2, edición ni publicación.

## G. Reglas de conservación, coste y calidad
- Pasar originales Samsung por cable USB, Quick Share en modo de archivo original o transferencia sin compresión verificada; **nunca WhatsApp como ruta de ingestión**.
- Guardar originales, usar proxys para previsualizar si el PC lo necesita y **evitar exportar master desde la copia degradada**.
- YouTube recomienda subir contenido al mismo FPS de captura. Como plan interno de contenidos nuevos se puede grabar a 30 y editar a 30; si ya es 60, decidir explícitamente conversión antes de editar. Ver `18_INGESTA_COLOR_EXPORT_Y_QC.md`.
- Conservar música/efectos con derechos comprobados para todas las plataformas, no asumir que una pista disponible dentro de TikTok se puede reutilizar en Facebook/YouTube.
- Editar con preview comprimido, master una sola vez tras picture lock; QC manual en móvil y validación `ffprobe`.
- Después de publicación, originales/proyectos pueden pasar a disco externo siguiendo `14_POLITICA_ARCHIVO_Y_RESTAURACION.md`, manteniendo fichas, manifests y métricas sin disco.

## H. Cómo terminar cada tarea de IA
Exigir siempre: **«Qué se hizo, qué cambió, qué evidencia se verificó, qué sigue pendiente y cuál es el próximo gate; NO continúes sin mi autorización».**
