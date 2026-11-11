# Prompts operativos v3.5 — IDs únicos y límites verificables
Regla de cierre: reportar **estado anterior → acción → archivos creados/modificados → evidencias → aprobación humana solicitada → siguiente paso**. Los prompts no son autorización para comprar, publicar, borrar, modificar el producto o continuar de gate automáticamente.

## P00 — Apertura del sistema (IA editorial)
Lee `00_INICIO_Y_ESTADO.md`, `registro/ESTADO.md`, `registro/DECISIONES.md` y `17_AUDITORIA_FINAL_ESTANDARES.md`. Separa aprobado, propuesto y pendiente. Resuelve discrepancias por registro; no inventes estados. No produzcas guiones ni vídeos. Devuelve próximo gate y archivos que se usarán.

## P01 — Abrir semana: propuestas hasta G1 (Cowork/Work/ChatGPT)
Semana: `[AAAA-WNN]`. Horas para contenido: `[X]` dentro de tiempo total de proyecto: `[Y]`. Estado verificable de MiMiniApp: `[ESTADO/URL]`. Comentarios o ideas: `[EVIDENCIAS]`. Lee `02_ESTRATEGIA_EDITORIAL.md`, `04_SISTEMA_DE_GUIONES.md`, `05_SOP_SEMANAL_Y_GATES.md`, `registro/ESTADO.md` y última retrospectiva. Propón **máximo 6 ideas**, con audiencia, única promesa, prueba disponible, gancho conceptual, formato, dependencia, esfuerzo y puntuación 0–10 razonada. Rellena `semanas/[SEMANA]/PLAN.md` (BORRADOR). **Detente en G1, sin escribir guiones ni abrir edición.**

## P02 — Elegir lote y crear briefs (IA editorial)
Apruebo G1 de `[SEMANA]`, `PLAN.md` versión `[VERSIÓN]`, vídeos `[IDs]` (y rechazo/aplazo los demás). Registrar persona y fecha. Usa `templates/VIDEO.md` para BRIEF. Propón solo 2 ganchos por vídeo, puntúa claridad, relación y prueba; elige uno justificadamente. No des por aprobados G2/G3.

## P03 — Guion + storyboard y claims (IA editorial)
Para `[SEMANA/Vxx]` usa BRIEF y `04_SISTEMA_DE_GUIONES.md`. Completa `SCRIPT.md` con texto literal hablado, indicación A-roll/VO, duración, tabla por escena con cortes/movimientos Txx/sonido/recursos y comprobación de payoff. Completa `PRUEBAS_Y_CLAIMS.md` y marca cada afirmación P/E/O/H/X. **Una única versión principal**, una revisión como máximo y espera G2. Si un claim X no puede verificarse, bloquearlo/reencuadrarlo; no convertirlo en hecho.

## P04 — Lista de rodaje e ingesta (IA editorial → humano)
Según guiones G2 aprobados, agrupa tomas para Samsung S24+ y voz, crea `TAKES.md` con IDs, encuadre, diálogo, luz, micro y assets. Indica transferencia directa de **archivos originales**, NUNCA WhatsApp ni redes. Completa `INGESTA.md` con FPS/resolución/codec/HDR si el dato se ha medido; si no, PENDIENTE. Anota proxies solo cuando estén justificados. Detente en G4 hasta que Alexander compruebe material y audio.

## P05 — Handoff a HyperFrames, SOLO plan (Claude Code/Codex)
Lee `CLAUDE.md`, `07_ESPECIFICACION_HYPERFRAMES.md`, `18_INGESTA_COLOR_EXPORT_Y_QC.md` y de `[SEMANA/Vxx]` BRIEF, SCRIPT, claims, TAKES, INGESTA y assets. Si existe identidad B0 aprobada, lee tokens; si no, solo preview TEMP. Revisa skills instaladas, **no reinstales**. Completa `EDIT_PLAN.md` con intervalos, técnicas Txx, estado inicial/intermedio/final, audio, entrega de escenas para CapCut, QA y límite de reintentos. Sin código ni renders hasta **G5 humano**.

## P06 — Escena crítica de animación (Claude Code)
Autorizo solo `[ESCENA]` de `EDIT_PLAN.md` v`[VERSIÓN]`. Crea animación seekable, pistas y elementos con IDs; entrega frames inicial/intermedio/final y preview corto. Registrar ficheros y tiempo. No alterar guion ni otra escena.

## P07 — Rough cut y previsualización (Claude Code)
Autorizo completar `[VIDEO]` contra `EDIT_PLAN.md` aprobado. Integra escenas, referencias y voz; produce rough cut y reporte de defectos. Si acabaremos en CapCut, exporta escenas sincronizables, WAV/audio y SRT de acuerdo con `15_MONTAJE_FINAL_GRATUITO.md`. **No generes master final, no publiques; espera G6/G7.**

## P08 — Corrección focalizada
Vídeo `[ID]` preview `[VERSION]`, timecode `[MM:SS–MM:SS]`. Defecto observable: `[X]`. Cambio exacto: `[Y]`. Prueba de aceptación: `[Z]`. Corrige solo pista/escena afectada y genera preview corto. Cuenta esta tanda en `REVISION.md`. Máximo dos tandas antes de replantear.

## P09 — Master y control técnico (HyperFrames/edición final)
El picture lock G7 de `[ID]` está aprobado por `[PERSONA/FECHA]` contra `[VERSIÓN]`. Produce master FINAL desde **originales o fuentes de alta calidad**, no proxies si reducen salida, con perfil definido en `18_INGESTA_COLOR_EXPORT_Y_QC.md`. Ejecuta `scripts/inspeccionar_video.py` si ffprobe está disponible. Completa `QC_MASTER.md`, `LICENCIAS_MEDIOS.md`, portada y `PUBLICACION.md` borrador. **No publiques; espera G7.5 y G8 del humano.**

## P10 — Publicación y retrospectiva (IA editorial)
Solo con URLs verdaderas y métricas efectivamente obtenidas para `[SEMANA]`, registra `ENTREGAS.csv`, `METRICAS.csv`, y `RETRO.md`. Analiza por plataforma sin promediar medidas distintas ni inferir causalidad. Propón máximo 3 mejoras; déjalas PENDIENTES de aprobación. Si faltan estadísticas, registra `NO_DISPONIBLE`.

## P11 — Puerta B0 identidad audiovisual (IA editorial)
Lee `03_IDENTIDAD_AUDIOVISUAL.md` y estado de marca personal. Compara solo dos fotogramas/moodboards propios, sin copiar paleta de las capturas ajenas; verifica legibilidad móvil y licencia de fuentes. No crees `IDENTIDAD_APROBADA.json` sin aprobación expresa de Alexander.

## P12 — Alias del creador (IA editorial)
Lee `12_IDENTIDAD_PERSONAL_Y_HANDLES.md`, `registro/CUENTAS_SOCIALES.csv`. Alexander es el creador, MiMiniApp es producto. No declares disponibilidad por no encontrar resultados públicos. Presenta solo candidatos ya documentados y qué comprobación manual resta; no registres handles sin permiso.

## P13 — Inventariar medios para archivo offline
Lee `14_POLITICA_ARCHIVO_Y_RESTAURACION.md`. Inventaría episodio `[SEMANA/Vxx]`, prepara manifest y destino, verifica copia por hash una vez Alexander la haya realizado. No borres, no marques offline sin evidencia de copia y aprobación.

## P14 — Consulta de histórico desconectado
Consulta `registro/ARCHIVOS.csv` y documentos del episodio para `[PREGUNTA]`. Si `ARCHIVADO_OFFLINE`, puedes analizar guion, decisiones, enlaces y métricas sin medios. No describas fotogramas no vistos; solicita restauración para reeditar o inspeccionar el vídeo.

## P15 — Handoff para CapCut/Shotcut (Claude Code)
Lee `EDIT_PLAN.md` aprobado y `15_MONTAJE_FINAL_GRATUITO.md`. Lista escenas MP4, voz/música/SFX por separado y SRT; IDs, duración y sincronía. No presupongas proyecto CapCut nativo ni transparencia sin test. Plan solo, esperando aprobación de exportación.

## P16 — Revisión montaje final gratis (IA editorial o Code)
Lee `MONTAJE_FINAL.md`, `QC_MASTER.md` y evidencias de un **MP4 exportado realmente disponible**. Comprueba continuidad, voz, música, subtítulos, color, derechos, marcas Pro y requisitos. Si falta el MP4, enumera lo no verificable. No otorgues G7.5; corresponde a Alexander.

## P17 — Ingesta y calidad original Samsung (IA asistencia)
Para `[SEMANA/Vxx]`, comprueba que existe `media/camera/original/`, metadatos con ffprobe, diferencia respecto a proxies/WhatsApp si se adjuntan. No recomprimas originales ni sustituyas originals por proxies. Proporciona incidencias concretas y actualiza `INGESTA.md` sin falsificar mediciones.

## P18 — Apertura, cierre y transferencia entre herramientas
Lee `registro/ESTADO.md` y expediente `[SEMANA/Vxx]`. Resume: qué está autorizado, versión de cada documento, qué recurso falta, qué agente trabaja ahora, próximo gate y tarea exacta. Prepara un handoff pequeño con **solo** documentos/medios del vídeo actual. No asumas que ChatGPT Web tiene escritura en Windows ni que Claude Cowork comparte automáticamente contexto con Code.
