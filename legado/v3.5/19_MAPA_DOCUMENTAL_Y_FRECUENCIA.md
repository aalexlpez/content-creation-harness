# Mapa de archivos: qué usar una vez, qué abrir cada semana y qué entrega cada vídeo

**Regla:** los Markdown de raíz son normas y guías; `templates/` es un molde; `registro/` almacena estado real; `semanas/` contiene trabajos. **No editar plantillas como si fueran episodios**.

## Documentos 00–19
| Archivo | Para qué sirve | Cuándo se utiliza |
|---|---|---|
| `00_INICIO_Y_ESTADO.md` | Regla general, decisiones y pendientes | Primera vez o ante un cambio importante |
| `01_EVIDENCIA_Y_AUDITORIA.md` | Fuentes, hechos y límites de la investigación | Primera vez, revisión de claims |
| `02_ESTRATEGIA_EDITORIAL.md` | Audiencias, pilares, selección de ideas | Inicio de cada semana (S1) |
| `03_IDENTIDAD_AUDIOVISUAL.md` | Propuesta de marca audiovisual **personal**, no colores de MiMiniApp | Aprobación B0 / cuando se revise la marca |
| `04_SISTEMA_DE_GUIONES.md` | Estructuras, ganchos y criterio de revisión finita | Cada guion (S2) |
| `05_SOP_SEMANAL_Y_GATES.md` | Secuencia y controles de aprobación | Referencia durante toda la semana |
| `06_OPERACION_COWORK_CLAUDECODE.md` | Transferir dossiers entre editorial y animación | Primera instalación y handoff G5 |
| `07_ESPECIFICACION_HYPERFRAMES.md` | Técnicas de animación y QC de escenas | Cada edición en Claude Code/HyperFrames |
| `08_MEDICION_Y_APRENDIZAJE.md` | Métricas, ventanas y prudencia estadística | Tras publicar y al cerrar semana |
| `09_PROMPTS_MAESTROS.md` | P00–P18 copiables por fase; sin duplicados | Ejecutar solo el prompt de la fase actual |
| `10_EJEMPLO_PLAN_SEMANA_01.md` | Caso ficticio de planificación | Consulta, no es semana aprobada |
| `11_PUESTA_EN_MARCHA_Y_CHECKLIST.md` | Configuración inicial y checklist B0/P0 | Primera vez y auditorías |
| `12_IDENTIDAD_PERSONAL_Y_HANDLES.md` | Alexander y alias; no confundir con producto | B0/registro de cuentas; alias pendiente |
| `13_GUIA_OPERATIVA_COWORK_WORK_CHATGPT_WEB.md` | Elegir IA editorial y coordinar archivos | Al configurar o cambiar de plataforma |
| `14_POLITICA_ARCHIVO_Y_RESTAURACION.md` | Copiar y retirar medios offline verificando SHA-256 | Tras publicar, opcional |
| `15_MONTAJE_FINAL_GRATUITO.md` | CapCut Gratis/Shotcut, montaje y export | Si el episodio precisa acabado externo |
| `16_GUIA_SEMANA_EN_15_MINUTOS.md` | Receta breve desde inicio de semana hasta cierre | **Primera lectura práctica de cada semana** |
| `17_AUDITORIA_FINAL_ESTANDARES.md` | Problemas corregidos, equivalencias profesionales y límites | Al evaluar la fiabilidad del sistema |
| `18_INGESTA_COLOR_EXPORT_Y_QC.md` | Original Samsung, proxies, SDR/HDR, sonido y control MP4 | S4 y export G7.5 |
| `19_MAPA_DOCUMENTAL_Y_FRECUENCIA.md` | Este índice de cada archivo | Si tienes dudas de qué documento tocar |

## Instrucciones a los agentes
- `COWORK_INSTRUCCIONES.md`: instrucciones persistentes para el agente **editorial** Cowork/Work/ChatGPT.
- `CLAUDE.md`: reglas persistentes para el agente **técnico** Claude Code/Codex/HyperFrames. **No sustituye al brief de cada vídeo**.

## Registros editables, sin vídeo adjunto
- `registro/ESTADO.md`: siguiente gate / bloqueo.
- `registro/DECISIONES.md`: qué fue aprobado, por quién y cuándo.
- `registro/IDEAS.csv`: backlog, origen, evidencia.
- `registro/ENTREGAS.csv`: qué master se publicó y dónde.
- `registro/METRICAS.csv`: datos por red y fecha, sin inventar.
- `registro/CUENTAS_SOCIALES.csv`: alias real comprobado.
- `registro/ARCHIVOS.csv`: archivo externo de medios, puede estar desconectado.

## Plantillas de `templates/`, una copia por trabajo
- `SEMANA.md` → `semanas/AAAA-WNN/PLAN.md` (S1/G1).
- `IDEA.md` → `semanas/AAAA-WNN/ideas/IDEA-xxx.md` (según ideas).
- `VIDEO.md` → `videos/Vxx/BRIEF.md` (S2).
- `SCRIPT.md` → `videos/Vxx/SCRIPT.md` (S2: guion y storyboard únicos).
- `PRUEBAS_Y_CLAIMS.md` → verificación de afirmaciones y producto (S3).
- `TAKES.md` → tomas de cámara y voz (S4).
- `INGESTA.md` → original del teléfono y metadatos (S4).
- `EDIT_PLAN.md` → plan de HyperFrames autorizado (S5/G5).
- `REVISION.md` → defectos exactos por timecode (S6/S7).
- `MONTAJE_FINAL.md` → ensamblaje en CapCut/Shotcut, si se usa (S7).
- `LICENCIAS_MEDIOS.md` → derechos de música/SFX/tipografías (G7.5).
- `QC_MASTER.md` → aceptación técnica/visual del MP4 final (G7.5).
- `PUBLICACION.md` → título, portada, URL y estado por red (G8).
- `CIERRE_SEMANAL.md` → `semanas/AAAA-WNN/RETRO.md` (G9).

## Scripts de `scripts/`
- `crear_semana.py`: crea carpetas y modelos sin otorgar aprobaciones.
- `preparar_frame_md.py`: **bloqueado** hasta B0; convierte identidad personal aprobada a `frame.md`.
- `inspeccionar_video.py`: lee metadatos con FFprobe, verifica master sin cambiarlo.
- `gestion_archivo.py`: inventario, verifica copia externa por SHA-256, registra offline; **no borra**.
- `validar_paquete.py`: comprueba hashes, JPG originales, documentos y prompts únicos.

## Carpetas de medios y fuentes (no confundir con marca)
- `referencias/ui_motion/`: 3 JPG de referencia de **movimiento**, colores no aprobados.
- `referencias/tecnologia/`: 6 capturas visuales de referencia, no para publicación directa.
- `fuentes_proyecto/`: estado del producto y equipo de grabación.
- `evidencia_tecnica/`: piloto HyperFrames 8s sin audio, prueba parcial, no master.
- `brand/IDENTIDAD_PROPUESTA.json`: candidata, no definitiva. `IDENTIDAD_APROBADA.json` se crea solo con aprobación.
- `MANIFEST_SHA256.json`: integridad del kit base; no versiones de las semanas nuevas.
