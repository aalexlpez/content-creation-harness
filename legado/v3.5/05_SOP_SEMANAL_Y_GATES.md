# SOP semanal v3.5 — cadena de producción, aprobaciones y trazabilidad
**Titular:** Alexander, NO MiMiniApp. **Identidad audiovisual B0:** pendiente. Alias pendiente no bloquea planificación interna; sin marca aprobada NO se entrega master con marca definitiva.

Este procedimiento adapta fases de postproducción real —ingesta, montaje de estructura, *rough cut*, *picture lock*, acabado, QC, entregas, archivo— a una persona y un editor de IA. Los gates son controles propios del proyecto, NO un estándar oficial de las redes.

| Fase / gate | Quién | Entradas / acción | Entregable verificable | No avanzar si… |
|---|---|---|---|---|
| B0 (una vez) | Alexander | Aprobar posicionamiento e identidad personal | `brand/IDENTIDAD_APROBADA.json` + decisión | faltan identidad o aprobación para master con marca |
| S0/G0 | IA editorial + Alexander | Histórico, métricas realmente disponibles y estado de producto | `registro/ESTADO.md`, retrospectiva previa | se inventan publicaciones o datos |
| S1/G1 | IA propone, Alexander elige | Hasta 6 ideas, horas reales disponibles, prueba visual | `semanas/AAAA-WNN/PLAN.md` | no hay selección o capacidad aprobada |
| S2/G2 | IA redacta, Alexander aprueba | Dos ganchos máximo; guion literal, storyboard y afirmaciones | `Vxx/BRIEF.md`, `SCRIPT.md`, `PRUEBAS_Y_CLAIMS.md` | promesa sin prueba, claims X o guion no aprobado |
| S3/G3 | Alexander/producto | Verificar UI/funciones/resultados y estado real | `PRUEBAS_Y_CLAIMS.md` con pruebas, URLs/commit o limitación explícita | demo ficticia presentada como real |
| S4/G4 | Alexander | Lista de tomas, rodaje por lotes, copiar originales sin WhatsApp, escuchar audio, inspeccionar metadatos, guardar respaldos | `TAKES.md`, `INGESTA.md`, `media/camera/original/`, pruebas fuente | originales ausentes/no identificados, voz defectuosa |
| S5/G5 | Claude Code + HyperFrames prepara, Alexander autoriza | Plan técnico por escena y activos existentes, coste externo = 0 salvo aprobación | `EDIT_PLAN.md` con versión aprobada | agente quiere implementar sin aprobación |
| S6/G6 | Claude Code + HyperFrames | Prueba escena crítica, rough cut y previews cortos; resultados con voz si corresponde | `preview/`, informe de revisión | no hay preview para evaluar historia y visuales |
| S7/G7 | Alexander + CapCut/Shotcut opcional | Cortes, orden, subtítulos, audio, ajustes; máximo 2 rondas focalizadas; **picture lock** | `MONTAJE_FINAL.md`, `REVISION.md`, proyecto nativo si existe | estructura, timing o claims todavía cambian |
| S7.5/G7.5 | Editor + Alexander | Acabado, normalización razonable, export único, QC técnico y visual en móvil | `delivery/master_final.mp4`, `QC_MASTER.md`, `PUBLICACION.md` borrador | audio ausente, calidad dañada, marcas, licencia, error de texto |
| S8/G8 | Alexander | Publicación por plataforma y URL real; autorización humana | `PUBLICACION.md` + `registro/ENTREGAS.csv` | archivo no revisado o sin autorización |
| S9/G9 | IA editorial + Alexander | Registrar estadísticas solo cuando estén disponibles; análisis +48 h/+7 d (periodos propuestos) | `registro/METRICAS.csv`, `RETRO.md`, cierre semanal | métricas inventadas o sin fuente |
| A0…A5 (opcional) | Alexander | Copia externa, SHA-256, comprobación, registro offline | `ARCHIVO.json`, `registro/ARCHIVOS.csv` | no hay copia verificada o respaldo suficiente |

## Política de producción eficaz
- No hay calendario de días fijos obligatorio. Agrupar guiones/rodaje y delegar una composición por vídeo.
- **Una idea principal y un CTA por vídeo**; hasta dos propuestas de gancho y una reescritura antes de replantear la promesa.
- Máximo dos tandas focalizadas de correcciones; indicar intervalo `mm:ss`, defecto observable, cambio y criterio de aceptación.
- Delimitar cuál herramienta hace cada trabajo: IA editorial no altera interfaz web; HyperFrames anima/monta; CapCut/Shotcut solo hace ajustes de montaje; Alexander aprueba/publica.
- Si el montaje ya está terminado en HyperFrames, marcar editor externo `NO_NECESARIO`. No repetir exportaciones.
- Trabajar con fuentes reales y registrar licencias cross-platform de música, fotos, efectos y tipografías en `LICENCIAS_MEDIOS.md`.
- Mantener originales de cámara intactos, utilizar proxy solo si resulta necesario y recuperar fuentes de calidad para master.
- **Versiones:** vídeo `AAAA-WNN_V01_v01_...`, luego `v02`; no sobreescribir masters. El master publicado se identifica por hash y fichero.
- Evidencia de aprobación: fecha, persona, ID gate, documento/versión, evidencia revisada, alcance autorizado y siguiente gate.

## Estados editoriales
`BACKLOG → SELECCIONADA → GUION_APROBADO → FUENTES_VALIDADAS → RODAJE_LISTO → PLAN_TECNICO_APROBADO → ROUGH_CUT → PICTURE_LOCK → MASTER_QC_APROBADO → PUBLICADA → ANALIZADA`.
Estados alternos: `BLOQUEADA`, `CANCELADA`, `ARCHIVADO_OFFLINE` (estado de **medios**, no editorial).

## Entregable documental mínimo por episodio
`BRIEF.md`, `SCRIPT.md`, `PRUEBAS_Y_CLAIMS.md`, `TAKES.md`, `INGESTA.md`, `EDIT_PLAN.md`, `REVISION.md`, `MONTAJE_FINAL.md`, `LICENCIAS_MEDIOS.md`, `QC_MASTER.md`, `PUBLICACION.md`; y `semanas/AAAA-WNN/RETRO.md` para cierre. Se pueden marcar secciones `NO_APLICA`, nunca presentar como aprobado lo no verificado.
