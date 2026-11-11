**Separación de identidades obligatoria:** Cowork organiza los contenidos de Alexander; HyperFrames/Claude Code producen sus vídeos. MiMiniApp es un proyecto tratado por el canal. El alias personal está sin confirmar y no puede colocarse en renders definitivos ni en assets de publicación. Consultar `12_IDENTIDAD_PERSONAL_Y_HANDLES.md`.

# Proyecto persistente en Claude Cowork + edición en Claude Code

## Aclaración verificada
**Cowork** permite proyectos con archivos, instrucciones, contexto y memoria. **Claude Code** trabaja sobre repositorios/carpetas e instrucciones `CLAUDE.md`. Anthropic no garantiza sincronización automática de proyectos Cowork hacia Claude Code en el flujo general; algunos usuarios tienen un nuevo sistema de proyectos de Code en beta. Para este sistema **los archivos del directorio son la fuente de verdad**, no la memoria de cada superficie.
Fuentes: https://support.claude.com/es/articles/14116274-organiza-tus-tareas-con-proyectos-en-claude-cowork y https://support.claude.com/es/articles/9517075-que-son-los-proyectos

## Puesta en marcha, una sola vez
1. Extraer este ZIP en carpeta local `MiMiniApp-Contenido` separada de la web. Respaldarla/versionarla; **no subir activos de terceros ni fuentes sin permisos a repositorios públicos**.
2. En Claude Cowork (si el plan tiene acceso), crear un proyecto «MiMiniApp · Dirección editorial» y enlazar carpeta existente si esa opción está disponible. Introducir `COWORK_INSTRUCCIONES.md` como instrucciones de proyecto.
3. Para edición, abrir **otro workspace**, derivado del mismo directorio: `produccion_hyperframes/` en Claude Code/HyperFrames Studio. Cargar `CLAUDE.md`, `brand/IDENTIDAD_APROBADA.json` cuando exista y la ficha de un solo vídeo.
4. Instalar skills oficiales de HyperFrames **solo en ese proyecto y con permiso**. Según versión: plugin oficial de Claude o Core Skills oficiales del motor. Documentar versión/CLI instalado. No ejecutar instaladores repetidamente.
5. Un vídeo se entrega a Code solo cuando cumple G2–G4. Cowork no puede «dar por aprobado» su propio guion.

**Handoff de identidad:** tras aprobar B0, generar `frame.md` desde los tokens del JSON aprobado. Antes de B0 no existe `frame.md` y los previews son TEMP no publicables.


- Cowork/ChatGPT: leer evidencia, priorizar, redactar guiones y briefs, verificar citas, preparar decisiones para aprobación, consolidar métricas.
- Code/HyperFrames: generar HTML/GSAP editables, previsualizar, renderizar, validar pistas/medios, documentar cambios técnicos.
- Humano: aprobar ideas, marca, guiones, claims, ejecución y publicación.

## Protocolo de intercambio (archivo, no chat)
`semanas/AAAA-WNN/PLAN.md` → `videos/Vxx/BRIEF.md` + `SCRIPT.md` + `PRUEBAS_Y_CLAIMS.md` + `TAKES.md` + `INGESTA.md` → `EDIT_PLAN.md` → `preview/` y `REVISION.md` → `MONTAJE_FINAL.md` + `QC_MASTER.md` → `PUBLICACION.md` → `RETRO.md`.
Cada archivo tiene `versión`, `estado`, `referencias a evidencias`, `última aprobación`. El agente puede pedir aclaración dentro del documento, sin fabricar valores.

## Suscripciones
Una cuenta ChatGPT ya existe. Claude Cowork y Claude Code pueden estar sujetos a los límites y condiciones del plan Anthropic; confirmar la oferta vigente y **no asumir agentes o créditos infinitos**. El sistema funciona con ChatGPT + Codex + HyperFrames como ruta alternativa. No hace falta comprar 3 suscripciones para probar guion y primer montaje.

## Operación con soportes externos desconectados
Antes de buscar medios de una semana anterior, consultar `registro/ARCHIVOS.csv` y el `ARCHIVO.json` de su vídeo. Si dice `ARCHIVADO_OFFLINE`, no tratar los MP4 ausentes como incidencia ni pedir restauración para redactar o analizar métricas. Si se solicita reedición o reutilización directa de elementos visuales, identificar los archivos necesarios y pedir conectar/restaurar el soporte. Aplicar `14_POLITICA_ARCHIVO_Y_RESTAURACION.md`. No borrar ni mover por cuenta del agente.

## Nuevo handoff de montaje final v3.4
Cowork/Work prepara guion y referencias; Claude Code + HyperFrames produce **escenas y stems**; Alexander puede usar CapCut Desktop Gratis para unir piezas, corregir timings, audio, SRT y títulos. Si CapCut solicita Pro al exportar, eliminar recursos premium o pasar a Shotcut, **sin autorizar una compra por defecto**. El agente no debe reconstruir un render complejo si bastan dos cortes del editor. La versión aprobada del archivo se registra en `templates/MONTAJE_FINAL.md` y `registro/ENTREGAS.csv`.

## Correcciones de ruta v3.5
`16_GUIA_SEMANA_EN_15_MINUTOS.md` es el manual de apertura. `09_PROMPTS_MAESTROS.md` tiene identificadores **P00–P18 sin duplicados**. `18_INGESTA_COLOR_EXPORT_Y_QC.md` establece cómo ingresar fuentes Samsung exactas; no usar clips comprimidos por WhatsApp. Contenido de Vxx en `semanas/AAAA-WNN/videos/Vxx/` y editor nativo en `montaje_final/`; expedientes y registros permanecen fuera de medios archivables.
