# Auditoría maestra del sistema de contenido de Alexander

**Fase 1 · Diagnóstico y propuesta · 8 de noviembre de 2026 · Versión auditada v3.5**

**Veredicto actual — No preparado.** La v3.5 sirve para planificar y ensayar con copias. Antes de iniciar un piloto necesita un traspaso de edición probado en el equipo de Alexander, una ruta clara de aprobaciones y un procedimiento de archivo que impida certificar la carpeta de origen como respaldo. El MP4 de ocho segundos acredita una salida vertical de HyperFrames sin audio. La cadena cámara → animación → montaje → control → publicación → restauración sigue sin demostrarse.

**Propuesta para aprobar —** Conservar el método de guion, la disciplina de evidencia, el uso de originales y la separación del histórico de los medios. Reducir los 11 Markdown obligatorios por vídeo a tres, agrupar las decisiones de producción en tres momentos de aprobación humana y dar a CapCut Desktop Gratis una prueba de aceptación concreta, con Shotcut como contingencia. Mantener HyperFrames como motor de animación y la marca definitiva y el alias en sus estados pendientes.

**Cómo leer la evidencia.** [L] observado en los archivos de la carpeta entregada. [T] reproducido en Windows con datos de prueba o inspección de bytes. [O] documentación oficial externa. [BP] práctica documentada, con su ámbito. [D] diseño candidato sujeto a aprobación. [H] hipótesis para contrastar con publicaciones reales. Las referencias locales usan el número del documento o la ruta y, cuando importa, la línea. Las fuentes externas S01–S24 se enlazan al final con fecha y alcance.

## I. Inventario del sistema actual

**Alcance [L/T].** Se inspeccionó la carpeta local indicada, no versiones homónimas en otros lugares. La raíz contiene 23 archivos y el árbol completo 64, con 2.901.052 bytes. Hay 20 guías numeradas, dos instrucciones de agentes, un manifiesto, un JSON de marca, siete registros, cinco scripts, 14 plantillas, tres archivos de fuentes, diez de referencias contando su índice y un MP4. El manifiesto enumera los otros 63 archivos. Validación entregada ejecutada con Python 3.12.14: 27/27 rutas del listado fijo, 19/19 IDs P00–P18, 3/3 JPG y hashes coincidentes. Los cinco scripts compilan. La carpeta original conservó los mismos archivos y hashes después de los ensayos.

| Grupo | Función y dependencias | Evidencia de estado |
|---|---|---|
| 00–05 | Entrada y estado, evidencia, estrategia, identidad audiovisual, guiones, SOP | Métodos legibles y reglas propuestas. B0, posicionamiento y primera miniapp pendientes. Duplicación de rutas, gates y estado con 11, 13, 16 y 19 |
| 06–09 | Operación editorial/técnica, HyperFrames, métricas y 19 prompts | Prompts con IDs únicos. Sin integración ni automatización de proveedores demostrada. P01/P05/P15 y las plantillas se solapan |
| 10–13 | Ejemplo MiMiniApp, checklist, identidad personal/alias y rutas Cowork/Work/Web | Ejemplo explícitamente ficticio. Cuatro alias históricos sin verificación. Checklist y reparto de tareas se repiten |
| 14–19 | Archivo, montaje, recorrido semanal, auditoría anterior, ingesta/QC y mapa documental | Existencia y contenido verificados. El procedimiento de montaje y restauración del editor no está probado con un proyecto audiovisual real |
| `CLAUDE.md`, `COWORK_INSTRUCCIONES.md`, `MANIFEST_SHA256.json` | Reglas por superficie y huellas de la entrega base | Claude Code, Codex y Cowork precisan adaptadores o carga explícita. Manifiesto útil como huella de release. No sirve como canon de datos editables |
| `registro/` | Decisiones, estado, cuentas, ideas, entregas, métricas, archivo | Cuatro filas de cuentas pendientes. IDEAS, ENTREGAS, METRICAS y ARCHIVOS solo tienen cabecera. No hay publicaciones ni métricas propias registradas |
| `brand/` | Tokens de identidad propuesta | Solo existe `IDENTIDAD_PROPUESTA.json`. Faltan deliberadamente `IDENTIDAD_APROBADA.json` y `frame.md` |
| `templates/` | Semana, cierre, idea y 11 documentos por vídeo | 14 plantillas encontradas. El generador copia 11 por vídeo, con marcadores de plantilla literales y 17 subdirectorios en el caso probado |
| `scripts/` | Crear, inspeccionar, generar estilo, validar y gestionar archivo | Implementación real en los cinco. Cuatro ejecutados directamente o con fixtures y el inspector ejecutado hasta el bloqueo por falta de `ffprobe` accesible |
| `fuentes_proyecto/` | Dossier de MiMiniApp v1.2, guía de set e índice | Fuentes de referencia. El dossier cita 11–15 h semanales totales, incluyendo desarrollo y QA. Guía de set propone 4K/30 como captura inicial y 1080p/30 como alternativa. No acreditan estado del repositorio web ni ajustes actuales del móvil |
| `referencias/` | Índice, seis PNG de vídeo tecnológico y tres JPG de UI | Nueve imágenes válidas e inspeccionadas visualmente. Dos PNG son idénticos byte a byte. Los JPG documentan posiciones de un morph, sin revelar su implementación, audio ni licencia de reutilización |
| `evidencia_tecnica/` | MP4 del piloto | 1.668.418 bytes. Lectura independiente de las tablas MP4: una pista `avc1` de 1080×1920, 480 muestras a 60 fps, 8,000 s y cero pistas de audio. No se decodificó el MP4 ni se probó su reproducción en editor o teléfono |

**Reproducciones que delimitan la v3.5 [T].**

| ID | Ensayo no destructivo | Resultado observado |
|---|---|---|
| T01 | Crear con 0 y con 2 expedientes en copia aislada | Ambos crean borradores. Abrir con 0 y volver a pedir 2 falla porque la semana existe. También se acepta `2027-W53`, que no existe en el calendario ISO de 2027 |
| T02 | Quitar una plantilla en la copia y pedir 1 vídeo | El script falla y deja una semana parcialmente creada, con SCRIPT ya copiado. Reintentar sobre esa semana está bloqueado |
| T03 | Inventariar dos archivos, modificar un byte conservando tamaño y verificar | Detecta corrupción por hash. Bloquea marcar offline antes de verificar o sin el argumento de confirmación. Omite un archivo colocado en la raíz fuera de los directorios enumerados |
| T04 | Pasar el propio episodio como destino y, después, modificar el original | La verificación del propio origen termina con código 0. Tras cambiar un original, `marcar-offline` sigue terminando con código 0 y registra ARCHIVADO_OFFLINE |
| T05 | Copiar fixtures aparte, retirar los dos medios de la copia de trabajo y restaurar a una ruta temporal | Los 11 Markdown siguen accesibles y los medios restaurados coinciden con el manifiesto. El script conserva ARCHIVADO_OFFLINE. La transición a RESTAURADO_TEMPORAL es manual y no se probó la reapertura de un proyecto nativo ni un disco físico |
| T06 | Validar el original y luego modificar la copia de trabajo y su manifiesto | Base íntegra. Actualizar ARCHIVOS.csv invalida su hash de release. Un manifiesto con versión 3.5 y `files: {}` pasa aun faltando TAKES.md |
| T07 | Ejecutar el generador de estilo sin aprobación y con un fixture inválido | Bloqueo correcto en la carpeta real. En la copia, una fecha inválida, un color fuera de formato y una firma ficticia no vacía generan `frame.md`. El script comprueba presencia de campos, no una firma autenticada ni un esquema completo |
| T08 | Ejecutar el inspector sobre el piloto | Salida de dependencia no disponible, código 1. Los metadatos del piloto se comprobaron por estructura MP4. No hubo ejecución real de ffprobe sobre un máster ni prueba de CapCut, Shotcut, DaVinci o render HyperFrames |

## II. Evaluación por áreas

**Severidad.** Crítico bloquea un uso seguro o una salida publicable. Importante afecta continuidad, coste o fiabilidad del piloto. Mejora recomendable aporta valor medible tras lo esencial. Opcional depende de un caso de uso.

| Área | Fortaleza que conviene conservar | Hallazgo, severidad y riesgo | Evidencia y acción propuesta |
|---|---|---|---|
| A · Arquitectura | Marca personal separada por principio. Un directorio canónico y expedientes legibles sin proveedor | **A1 · Importante.** El desacoplamiento es declarativo. Proyecto, serie y campaña carecen de IDs operativos. Reglas de estado y apertura repartidas. Una sola persona debe reconciliarlas | [L] 00:10–19, 02:1, 06 paso 2, 09/P01, COWORK:2, SEMANA:4–14, VIDEO:1–7 y scripts/crear_semana.py:11–30. [D] Modelo de entidades, ID estable de vídeo y fuentes de verdad por dato |
| B · Editorial | Una audiencia por pieza, cinco criterios 0–2, filtro de demostrabilidad, cautela con causalidad | **B1 · Importante.** El backlog tiene origen pero carece de un método mínimo para contrastar problemas, distinguir señal de moda y llevar un aprendizaje a una idea nueva. El 3/2/4 puede sesgar la planificación | [L] 02:10–46, IDEAS.csv, 08 y 10. [BP/D] Investigación breve con señal, contexto y confianza, un objetivo por pieza y horas reales. [H] Las aperturas por resultado pueden funcionar mejor en demos útiles. S01, S02, S06, S19 y S23 |
| C · Guion | Cinco familias, prueba del payoff, voz literal, claims P/E/O/H/X, dos ganchos y reescritura limitada | **C1 · Importante.** Storyboard y plan técnico reiteran tiempos y pistas. G2 bloquea claims X antes de G3, que verifica el producto. P02 puntúa tres criterios mientras 04 y VIDEO puntúan cuatro | [L] 04, 05 G2/G3, 09/P02–P05, SCRIPT y EDIT_PLAN. [D] Una fila por escena y una aprobación del guion que incluya la evidencia exigible. Validar capturas definitivas al ingestar |
| D · Identidad | Paleta etiquetada como candidata. Buenas referencias de composición, rótulos, continuidad y uso de sonido | **D1 · Importante.** B0 une promesa, marca y elegibilidad de publicación, con reglas TEMP distintas según el documento. Falta ficha de cámara, reglas concretas de subtítulos, recorte de portada, uso de UI y verificación de licencias de fuentes. El JSON no cubre todo lo que 03 promete | [L/T] 00, 03:14–50, 05 B0, 06, 07:32–41, 12, P05/P11 y T07. [D] Separar aprobación editorial, perfil audiovisual provisional y marca definitiva. Pruebas de legibilidad y escucha. S16–S18 |
| E · Producción | Originales, proxies separados, revisión móvil, picture lock, versiones, licencias y QC diferenciados | **E1 · Crítico.** Montaje gratuito e intercambio con voz sin probar. G6.5 solo existe en 15 y 15 permite omitir G7, mientras P09 exige picture lock. La práctica puede producir un master sin corte aprobado o un editor bloqueado | [L/T] 05, 07, 09/P07/P09/P15, 15:23–33, 17:28–33 y T08. [D] CapCut como montaje habitual, una prueba de intercambio previa al piloto y picture lock independiente de herramienta. S09–S15 |
| E · Técnica | El perfil 1080×1920/30 SDR está presentado como elección interna. Distinción correcta entre etiquetar y convertir HDR | **E2 · Importante.** 18 pide rotación, fecha y metadatos de color que el script no comprueba plenamente. FPS medio no prueba CFR, primarias 709 no prueban SDR y audio presente no prueba audibilidad. El master sin audio se bloquea incluso si el diseño es silencioso | [L] 18:7–31 y scripts/inspeccionar_video.py:13–35. [D] Inspección por perfil, checks de timestamps y canales según alcance, estado explícito por dato y revisión humana. S04, S12–S15 |
| E · Derechos | Tabla por recurso, alcance por red y rechazo de referencias de terceros como material publicable | **E3 · Importante.** Falta estado por destino, evidencia de licencia fechada, restricciones de uso/archivo y distinción entre promoción propia y contenido editorial. Se puede descubrir una limitación al final | [L] LICENCIAS_MEDIOS, 15 y 18. [D] Derechos desde el guion y revisión por red en entrega. Primera prueba con voz propia, música opcional y recursos verificables. S03, S05, S08 |
| F · IA | Ya existen límites de rondas, permisos y alcance por episodio. Se evita reinstalar por rutina | **F1 · Importante.** Ruta de trabajo técnica ausente, repetición de instrucciones, autolectura de CLAUDE.md por Codex sin configurar, y verificación de release que no representa la preparación del episodio | [L/T] 06 pasos 2–5, 13, CLAUDE.md, P00/P05/P18, scripts/validar_paquete.py y T06. [D] Canon local, traspaso versionado y reglas ligeras por agente. S09–S11 |
| G · Archivo | Copiar antes de retirar, SHA-256, ubicación lógica y consulta sin vídeos | **G1 · Crítico.** La verificación no acredita independencia del destino ni vigencia del inventario. Las dos escrituras de estado pueden divergir y el estado offline se registra antes de la retirada real | [L/T] 14:30–59, gestion_archivo.py:52–71, 96–127 y T03–T05. [D] Un manifiesto canónico versionado, destino explícito, revalidación y transición tras retirada humana. S12 |
| G · Trazabilidad | Guion y evidencia se reconocen como canónicos. Se prevén ventanas, denominadores y URLs reales | **G2 · Importante.** V01 se repite cada semana. METRICAS no incluye semana y ENTREGAS empaqueta URLs sin filas por plataforma. El mismo estado, versión, hash, copy o URL se puede editar varias veces | [L] CSV y plantillas de BRIEF, MONTAJE_FINAL, QC, PUBLICACION, CIERRE; 08:14–30. [D] ID inmutable, publicación y métrica con claves propias y una sola ubicación editable por dato |
| A/D · Mantenimiento | Ejemplos y evidencia previa permiten explicar el origen de decisiones | **M1 · Mejora recomendable.** Reducir carga de lectura y preservar procedencia de capturas. Dos PNG duplicados son evidencia histórica, no trabajo activo | [L/T] 01, 16, 17, 19 y comparación de imágenes. [D] Índice pequeño, historial inmutable, contacto visual fuera del paquete operativo si hace falta |
| E/F · Escalado | Se prevén alternativa de motor y alfa opcional | **M2 · Opcional.** Alfa, segunda cámara, 4K, Remotion y DaVinci añaden complejidad sin necesidad demostrada para el primer ciclo | [L] 07, 15 y guía de set. [D] Activarlos por caso de uso y prueba registrada |

## III. Problemas estructurales y referencias

| ID | Situación comprobada | Consecuencia y resolución candidata |
|---|---|---|
| R01 | `01_EVIDENCIA_Y_AUDITORIA.md:9` menciona `documentos_base_v2/` como referencia histórica. No hay carpeta ni ruta resoluble en esta copia | Conservar mención con estado «no incluida». Si se aporta la v2, enlazar su copia identificada. No reconstruirla de memoria |
| R02 | 06 paso 3 apunta a `produccion_hyperframes/`, ausente. 13 envía a un segundo workspace y 15/16 usan `Vxx/hyperframes/` | Un directorio técnico por vídeo, con dependencias compartidas pequeñas. Un único punto de entrada con ruta y comando de la versión instalada |
| R03 | 15 G6 pide `manifest.md`, pero el generador y las plantillas no lo crean ni el contrato define su esquema | Añadir inventario del intercambio como sección de producción. Generarlo como vista derivada solo si la prueba lo justifica |
| R04 | 06 pide registrar la entrega en `templates/MONTAJE_FINAL.md`; 19 prohíbe escribir estado real en el molde. 13 usa `REGISTROS` sin ruta literal, la carpeta es `registro/` | Corregir destinos en el arranque y validar enlaces y referencias de plantillas sin confundir archivos generados con faltantes |
| R05 | P01 redacta PLAN antes de G1. 00 sugiere llamar al generador después de G1. 16 permite crear con cero y añadir por vía manual. T01 confirma que el generador posterior no funciona | Separar crear semana de crear expediente, con el mismo camino manual o asistido y sin sobreescritura |
| R06 | 05 y P09 exigen G7. 15 permite saltarlo cuando HyperFrames ya entrega el montaje y añade G6.5. 07 conserva la frase «antes de marcar G7» en sus checks de aceptación del render | Distinguir prueba de intercambio, aprobación del corte y QC del archivo. El corte queda aprobado aunque se use un solo motor |
| R07 | 12 manda anotar tipo de cuenta en CUENTAS_SOCIALES.csv. La columna no existe. El registro de alias supone un candidato común, pero guardar es una operación real con efectos por plataforma | Registrar tipo, identidad pública verificada y enlace por red. Cualquier cambio de alias requiere decisión explícita, con efectos de reservar en una red antes de poder comprobar otra |
| R08 | `ESTADO.md` conserva encabezado del 5/11 y estado v3.0, seguido de actualización v3.5 del 6/11. 00, 05, 06, 11 y 16 mezclan identidad definitiva, estrategia y autorización de publicación | Mantener historia, una entrada vigente con punteros y política explícita de piloto interno/provisional/público. No inferir que B0 o un alias están aprobados |
| R09 | El manifiesto de release cubre CSV y estado vivos. El script valida solo lo que enumera y un subconjunto fijo. Los registros de archivo se reescriben en dos ubicaciones | Separar huella de distribución de validador operativo. Rechazar manifiestos vacíos y rutas fuera del alcance. Evitar doble escritura autoritativa |
| R10 | 14 dice que ARCHIVADO_OFFLINE significa medios retirados. A4 lo registra antes de A5 y restauración actualiza dos archivos manualmente. Copiar carpeta completa puede reintroducir Markdown antiguos | Verificar medios enumerados desde una ruta nueva, restaurar sin sobrescribir el expediente y registrar la disponibilidad real al final |
| R11 | 15/18 proponen proxy 1080p H.264 aun cuando su coste de decodificación puede seguir alto. La guía de set sugiere 4K/30 y 18 prioriza 30 SDR sin una resolución de captura única | Para el piloto probar 1080p/30 SDR directo. Usar preview o proxy más pequeño solo si la reproducción falla. Conservar la recomendación 4K como alternativa cuando el reencuadre lo justifique |
| R12 | No existen aún semanas reales, carpeta técnica ejecutable, proyecto nativo de editor, guion aprobado, cuentas verificadas ni licencia concreta de las referencias. No existen `frame.md` o tokens aprobados | Los primeros son ausencias de evidencia o artefactos de trabajo futuros. Los tokens y el frame son un bloqueo deliberado de marca. No completar esos huecos con datos inventados |



## IV. Arquitectura objetivo

### Estructura candidata

```text
Alexander-Contenido/
  INICIO.md                   índice corto y próximo trabajo por referencia
  OPERACION.md                flujo, permisos, montaje/QC, archivo y traspasos
  EDITORIAL.md                investigación, guiones, métricas y experimentos
  FUENTES.md                  evidencia, consultas externas y vigencia
  AGENTS.md / CLAUDE.md        adaptadores breves hacia las mismas reglas
  marca/
    IDENTIDAD.md              guía audiovisual del creador y estado de cada decisión
    identidad.json            tokens candidatos y perfiles autorizados por versión
    CUENTAS.csv               perfil comprobado y opciones por plataforma
  proyectos/
    miminiapp/PROYECTO.md      clave ilustrativa, confirmar en migración
    otro-proyecto/PROYECTO.md  ficha independiente, con fuentes propias
  registro/
    DECISIONES.md             decisiones transversales y cambios del sistema
    IDEAS.csv                 backlog global con referencias de evidencia
    METRICAS.csv              observaciones por publicación y fecha
  semanas/AAAA-WNN/SEMANA.md   horas, selección, orden, revisión y aprendizaje
  videos/VID-0001/
    GUION.md                  brief, guion literal, storyboard y claims
    PRODUCCION.md             tomas, ingesta, intercambio, edición y revisión
    CIERRE.md                 derechos, QC, aprobaciones y salidas por red
    ARCHIVO.json              solo si se archiva, inventario y verificaciones
    media/                    originales y copias de trabajo separados
    hyperframes/              solo si se necesita animación, fuente y lockfile
    montaje/                  proyecto nativo y ficheros necesarios
    entregas/                 master versionado y derivados justificados
  templates/                  semana, tres documentos por vídeo y ficha de proyecto
  scripts/                    utilidades locales con ruta manual equivalente
  referencias/                originales de consulta, procedencia y restricciones
  legado/v3.5/                copia sellada fuera de la lectura operativa diaria
```

El slug propuesto para el proyecto real es `miminiapp`. Los nombres de rutas y claves en este informe son candidatos. El perfil audiovisual humano y sus tokens legibles por máquina tienen responsabilidades diferentes. La guía guarda reglas y el JSON guarda valores, versión y referencia de aprobación, sin duplicar paleta en los dos. `frame.md`, si la versión instalada lo admite o requiere, será una proyección del perfil autorizado para ese render. `FUENTES.md` sustituye la evidencia repetida por enlaces con fecha y alcance. La ficha de proyecto se crea solo al usar un proyecto nuevo. Fuentes técnicas del set permanecen como referencia común.

| Entidad | Qué representa | Dónde queda su dato vigente |
|---|---|---|
| Marca del creador | Alexander, identidad visual/sonora, cuentas públicas | `marca/`. Alias e identidad definitiva siguen pendientes |
| Proyecto | Producto o iniciativa con sus pruebas y enlaces. Ej. MiMiniApp y un tutorial independiente sobre Git | `proyectos/<slug>/PROYECTO.md`, ID estable, URL/versión y límites. Para una línea sin producto puede existir un proyecto editorial propio con evidencia técnica |
| Pilar y objetivo | Pilar como tema recurrente. Objetivo principal como descubrimiento, comunidad o conversión verificable | Taxonomía en `EDITORIAL.md`, elección para esa pieza en `GUION.md`. Formato y perfil técnico son campos distintos |
| Serie | Línea recurrente, incluso transversal a varios proyectos | Clave opcional en un listado breve de `EDITORIAL.md` y referencia desde el vídeo |
| Campaña | Iniciativa temporal con propósito, fechas y cierre | Clave opcional y definición en ficha de proyecto o en `EDITORIAL.md` si es transversal. Sin carpetas nuevas por defecto |
| Idea y selección | Origen, problema, prueba potencial y elección humana | Idea ID en `IDEAS.csv`. Razón, coste, orden y aprobación del lote en `SEMANA.md`. El vídeo referencia la idea |
| Semana | Lote por capacidad, puede mezclar proyectos | ISO AAAA-WNN. Solo enlaces a vídeos, disponibilidad, selección y retrospectiva. Replanificar mantiene su ID |
| Vídeo | Episodio estable que puede pasar a otra semana y varias plataformas | `VID-0001` y versión en su expediente. Una línea `estado / bloqueo / siguiente paso` editable en PRODUCCION. El control de capacidad y la cola semanal se derivan de punteros |
| Publicación | Un acto de publicación de una versión concreta en una plataforma | Una fila en `CIERRE.md` por `publication_id` único, por ejemplo VID-0001-YT-01. Conserva URL, fecha ISO con zona, cuenta, versión, hash por artefacto, copy y perfil/licencia aplicables. Un repost tiene ID nuevo |
| Métrica | Observación de la plataforma y ventana | `METRICAS.csv`, clave `publication_id + fecha_observacion + metric_key`, valor, unidad, denominador si existe, ventana, fuente y disponibilidad. La fecha y URL de publicación se resuelven por referencia |
| Decisiones | Política transversal o aceptación de una versión/entrega | `DECISIONES.md` para lo transversal, aprobaciones de episodio en el documento que fijan. No volver a escribir esas aprobaciones en el registro global |
| Medios y archivo | Bytes disponibles y copias verificadas | `ARCHIVO.json` por lote o versión de archivo y destino. Estado editorial independiente. Un eventual índice de archivos se regenera, sin edición paralela |

**Responsabilidad [D].** Alexander es director, operador de cámara, editor final y aprobador de su publicación. El agente editorial investiga, propone y documenta. El agente técnico recibe solo el alcance autorizado, genera o ajusta animaciones y devuelve pruebas. Los scripts validan y enumeran. Una sola persona o agente escribe cada expediente a la vez. Se usa la versión base al devolver cambios y se reconcilian diferencias antes de aplicar una copia web. El trabajo manual usa los mismos archivos y condiciones. Git local o copias fechadas son suficientes para documentos y código ligero según la práctica disponible. Los medios pesados, credenciales y cachés quedan fuera de versionado y de la carga al asistente.

### Operación editorial y guion

1. **Investigar durante 20–30 min por lote como punto de partida [D].** Buscar un problema real en comentarios propios si existen, consultas de plataforma, preguntas de comunidades, soporte técnico o una observación reproducible de Alexander. Registrar consulta/URL, fecha, contexto, qué intenta hacer esa persona y prueba disponible. Una señal sirve para explorar. Dos fuentes independientes o una prueba propia elevan confianza. Una tendencia añade contexto y tiene fecha de caducidad. Evitar copiar formulaciones y tratar rankings o volumen como indicios.
2. **Ordenar hasta seis ideas [D].** Mantener la escala 0–2 de valor, visual, demostrabilidad, encaje y capacidad. Separar horas humanas de render. Reservar primero desarrollo/QA y compromisos ya existentes. Probar primero una pieza sencilla y una segunda solo si cabe en el presupuesto de contenido. Subir de dos a tres cuando dos ciclos completos respeten tiempo y QC. Nunca comprometer una miniapp nueva solo por llenar una semana.
3. **Definir objetivo y éxito antes de escribir [D].** Descubrimiento busca una señal de atención o compartidos. Comunidad busca un comentario o respuesta cualificados. Conversión exige un destino funcional, una acción concreta y medición disponible. Seleccionar un indicador principal por red si existe, con baseline comparable. El CTA puede ser ninguno si no aporta. Una pieza de demo entrega utilidad aunque la audiencia no visite el producto.
4. **Elegir la estructura y comprobar el resultado [D].** Demo, construcción pública, experimento, comunidad o tutorial. Hasta dos ganchos con claridad, alineación, prueba visible e interés honesto. Una versión y una reescritura. Si sigue sin pagarse la promesa, replantear o aparcar. Leer en voz alta y cronometrar. Una fila por escena con ID, objetivo, texto literal de A-roll/VO, rótulo, plano o animación, duración, evidencia y sonido. Si al quitar la escena se entiende igual, recortarla. Separar narración, subtítulos y rótulos. Demostración real antes/después con versión o datos de prueba claramente identificados. Una recreación fiel se ancla a prueba real. Un concepto se identifica en pantalla y en el copy si puede confundirse con una función.
5. **Aprender con una hipótesis por ciclo [D/H].** Por ejemplo, alternar resultado primero y problema primero entre demos comparables de una misma red. Documentar diferencias de tema, duración y distribución. Revisar primero el dato disponible y comentarios, no una atribución causal. Proponer una decisión, una incidencia y el experimento siguiente. S01, S02, S06 y S19.

### Identidad audiovisual y accesibilidad

| Ámbito | Regla candidata de uso y aceptación |
|---|---|
| Marca personal y producto | Rótulos, portadas y firma de Alexander por perfil aprobado. UI de producto capturada fielmente o reconstruida con indicación si altera la realidad. Paleta A, fuentes, firma y alias conservan estado pendiente |
| Cámara y luz | Prueba corta de piel, foco, exposición y bandas en el lugar real con softbox, reflector, antorchas y DJI. Medir o registrar ajuste del S24+, distancia, posición de luz, micrófono, ganancia y ruido. En caso de bandas probar ajustes de obturación disponibles con luz de red de 50 Hz y confirmar en clip. Segunda cámara solo si mejora un plano |
| Paleta y tipo | Dos frames originales, A-roll con rótulo y demo en UI. Medir contraste sobre fondos reales y observar el peor tramo del movimiento. WCAG 4,5:1 para texto normal y 3:1 para texto grande como referencia web de legibilidad. Revisar glifos ES, peso, números, términos técnicos y licencia antes de elegir familia. S16 |
| Subtítulos | Hasta dos líneas como punto de partida, segmentadas por sentido, corregidas a mano, con respaldo de contraste. Incluir indicios sonoros relevantes cuando aporten significado. Revisar sin audio en móvil y confirmar que los subtítulos de plataforma no dupliquen o tapen los incrustados. Conservar SRT UTF-8 revisado. S01 y S16 |
| Composición y portada | Un foco y título corto. Mantener rostro, prueba y texto crítico dentro de la zona comprobada en la interfaz de cada red y revisar recortes de perfil y feed en móvil. Registrar captura/fecha cuando cambie la UI. Los márgenes de una campaña publicitaria sirven como referencia, sin extenderlos a todas las superficies. S02, S06 y S07 |
| Motion y audio | Usar movimiento para orientar o demostrar, transiciones motivadas, puntos inicial/intermedio/final reconocibles y texto sin destellos. Voz delante, SFX puntuales y música opcional. No copiar marcas, colores, clips, fuente, sonidos o diseño distintivo de terceros. S16–S18 |
| Perfil provisional | Piloto interno con estilo temporal y sin @ inventado. Cualquier piloto público provisional requiere autorización de Alexander para ese perfil y cuentas verificadas. Ese permiso no convierte paleta, fuentes, firma o alias en decisiones permanentes |

## V. Flujo operativo definitivo propuesto

**Tres aprobaciones ordinarias.** OK-1 selecciona lote y presupuesto. OK-2 autoriza producir una versión de guion y storyboard con claims comprobables, alcance y límite de coste. OK-3 autoriza el archivo exacto de publicación tras picture lock y QC. Picture lock y QC tienen evidencias y momentos distintos. Pueden revisarse en la misma sesión si el corte ya quedó fijado antes del acabado. El archivo externo tiene autorización propia cuando se usa, igual que compras, instalaciones, cambios de marca y variaciones importantes de alcance. Los checks intermedios bloquean defectos y se registran en el expediente sin abrir una conversación de aprobación por cada paso.

| Fase y responsable | Entrada y acción | Salida / estado y condición |
|---|---|---|
| Idea → investigación → plan · Alexander + IA editorial | Backlog, evidencia, horas netas, retrospectiva y fichas de proyecto | `SEMANA.md` BORRADOR → OK-1 → SELECCIONADO. Guarda motivo, idea, proyecto, orden y presupuesto. Las propuestas no elegidas siguen en backlog |
| Brief → guion → storyboard · IA editorial, aprueba Alexander | Promesa, formato, prueba, gancho, texto literal, escenas, claims y CTA | `GUION.md` versión aprobada en OK-2. Claim X impide autorizar esa afirmación. Cambios de promesa, demo, voz o riesgo reabren OK-2 |
| Plan de rodaje → grabación → ingesta · Alexander, asistencia técnica | Guion, tomas y recursos. Grabar prueba del set y después originales y capturas. USB o transferencia de archivo comprobada. No se usa copia recomprimida de mensajería como fuente | `PRODUCCION.md` con toma/ruta/hash si procede, FPS, rotación, códec, color, audio, sincronía y copia adicional. Marcar BLOQUEADO si falta prueba real, original o audio válido. Eliminar del teléfono queda bajo control humano después de verificar respaldo |
| Animación · agente técnico | Dossier de un vídeo y corte/recursos autorizados. Probar una escena difícil antes del resto. Sin gastos o instalación implícitos | Fuente editable, render corto, log, escenas y manifest del intercambio en PRODUCCION. Si falla repetidamente, usar demo directa o simplificar. Técnica nueva que cambie coste o alcance vuelve a Alexander |
| Montaje → revisión → picture lock · Alexander | Originales, audio, escenas y guion. Rough cut por historia. Máximo dos rondas de cambios localizados con timecode y verificación | Corte versionado con versión y tiempo fijados. Cambios de duración, orden o contenido reabren picture lock. El mismo check aplica si el montaje ya está completo en HyperFrames |
| Acabado → QC → OK-3 · Alexander, agente verifica metadatos | Corte bloqueado, subtítulos, niveles, color, derechos, copy y opciones por red. Exportar desde fuentes íntegras | `CIERRE.md` con resultado técnico/visual, aprobación humana, versión/hash, destinos autorizados y archivo exacto. Un cambio de bytes o copy sensible requiere nueva revisión y alcance de aprobación actualizado |
| Publicar · Alexander | Cuenta verificada, QC, opciones de portada, etiquetas de promoción cuando apliquen, derechos y OK-3 | Fila por publicación con estado PROGRAMADA/PUBLICADA/FALLIDA y URL cuando exista. Confirmar cuenta correcta y reproducción después de la subida. Una red fallida no borra el éxito de otra |
| Análisis · Alexander + IA editorial | Datos obtenidos manualmente, ventanas de +48 h y +7 d como referencia, +28 d opcional | Snapshot fechado por publicación, estado NO_DISPONIBLE separado de 0 y cierre semanal con horas y decisión. El histórico sigue disponible si no hay vídeos locales |
| Archivo y restauración · Alexander | Aprobación explícita, inventario congelado, copias, verificación y restauración de muestra | Medios disponibles por estado. Expediente, derechos, fuentes pequeñas, datos y registro editorial legibles offline. Versiones publicadas inmutables |

**Estados mínimos.** Editorial: BORRADOR → SELECCIONADO → AUTORIZADO_PARA_PRODUCIR → EN_PRODUCCION → LISTO_PARA_PUBLICAR → PUBLICADO → ANALIZADO, con BLOQUEADO y CANCELADO y su motivo. Picture lock, QC y render son checks versionados. Publicación se registra por destino. Medios: LOCAL, COPIA_VERIFICADA, OFFLINE, RESTAURADO_TEMPORAL o NO_LOCALIZADO tras intentar acceso a la ubicación. El episodio puede estar publicado en parte y archivado mientras llegan métricas.

### Edición para el primer ciclo

**Ruta propuesta [D].** S24+ en 1080p/30 y SDR para probar compatibilidad. Desactivar HDR de vídeo y comprobar ajustes efectivos del dispositivo. Una pista A-roll/VO y una para B-roll/escenas, con subtítulos y música/SFX solo si hacen falta. En CapCut Desktop Gratis, crear un proyecto local vertical y guardar su ubicación real y versión. Importar original y escenas. Ordenar y recortar con la tabla del guion. Ajustar voz, evitar duplicar audio guía y voz final. Importar SRT si está disponible en la instalación o usar el archivo aprobado con la ruta probada en Shotcut. Revisar y fijar corte. Corregir subtítulos, mezcla y color en el acabado. Exportar MP4 vertical, comprobar resultado y conservar editable y dependencias. Dos correcciones focalizadas como máximo antes de simplificar. S10–S17.

**Prueba de 15–25 s [D].** Original Samsung con voz DJI, escena propia HyperFrames, tres subtítulos SRT que incluyan caracteres españoles y un ajuste de corte. Abrir proyecto, importar, cortar, exportar sin Pro y sin marca, guardar, cerrar, reabrir y exportar de nuevo. Comprobar móvil, voz, color, proporción, sincronía al inicio y al final, fuentes referenciadas y tiempo humano/render. Como objetivo de ensayo, hasta 45 min de manipulación tras tener el material y hasta 10 min de exportación de la muestra. Se registran resultados y causa si se supera, sin extrapolar a un minuto. Si falla CapCut, repetir con Shotcut y escoger una ruta operativa. En Shotcut fijar el modo de vídeo vertical, usar V1 para A-roll y V2 para superposiciones, bajar escala de previsualización si hay saltos, usar la ruta de subtítulos probada y comprobar que exporta desde originales. DaVinci queda para una necesidad concreta de acabado y una prueba en el equipo.

**Contrato de intercambio [D/O].** Recibir `VID + versión/hash de GUION + versión de estilo o TEMP + lista de tomas/recursos permitidos + perfil`. Cada escena declara ID, duración en frames y segundos, TC de entrada/salida, pistas, fuentes relativas, modo de audio (silencio, guía, stem o integrado), versión del motor/Node/navegador/FFmpeg cuando aplique, técnica y check de aceptación. Entregar fuente HTML/CSS/JS y recursos, preview ligera, MP4 H.264 por escena a resolución/fps del proyecto, WAV PCM 48 kHz si aplica, SRT UTF-8, y nombres `VID_S03_v02.mp4`. Verificar seek al inicio, medio y final, pistas y tiempos, errores del navegador/CLI y reproducción en editor. Usar comandos soportados por la versión fijada. La guía actual documenta `lint` y `check`, con comandos anteriores deprecados. Un overlay alfa queda opcional hasta probar exportación e importación. Para el piloto, componer el fondo con su escena. No se requiere intercambio nativo de proyectos entre HyperFrames y CapCut. S09–S11.

**Perfil de entrega interno [D].** 9:16, 1080×1920, H.264 progresivo, MP4, 30 CFR para material nuevo capturado o conformado a 30, SDR BT.709 y AAC-LC 48 kHz. Empezar alrededor de 8 Mb/s como referencia YouTube para SDR 1080p de FPS estándar y revisar detalle en móvil. YouTube aconseja mantener FPS de captura. Si hay 60 fps, VFR o HDR, decidir y registrar conformación antes del montaje, comprobar timestamps y sincronía y conservar original. HDR → SDR requiere una transformación tonal verificada, no solo metadatos. Usar escala de preview o proxy más pequeño, por ejemplo 540p/720p si el editor admite la ruta, y confirmar relink a originales o intermedios de calidad antes del master. Revisar voz con auriculares y altavoz de móvil. Si se mide sonoridad, registrar LUFS y dBTP como observaciones de mezcla, sin trasladar objetivos de emisión EBU como exigencia de las redes. El QC usa el MP4 exportado completo, incluyendo cuadros defectuosos, desajuste de audio, rótulos, derechos, marca de agua, color y decodificación. S04, S12–S17.

### Publicaciones y aprendizaje por plataforma

| Plataforma | Verificado y alcance | Qué comprobar en cada cuenta y guardar |
|---|---|---|
| TikTok | El centro de ayuda documenta Search Insights, Studio y subtítulos de accesibilidad. Para promocionar marca, producto o servicio, la guía pide divulgación de contenido y recomienda su biblioteca comercial para música en TikTok. Las guías de ads no fijan una obligación orgánica | Ver superposición de UI, texto, subtítulos, portada, etiqueta cuando aplique, música habilitada por licencia y resultados de Studio. S01–S03 |
| Instagram Reels | Meta publica Best Practices, insights de tiempo total y promedio y Trial Reels. Las especificaciones públicas encontradas en Postman son de API. Las páginas de ayuda orgánica de tamaño e insights redirigieron a inicio de sesión en esta consulta | Confirmar elegibilidad de cuenta, portada/recorte, opciones de prueba, métricas que aparecen y definición observada. No convertir la API en una regla de carga manual. S06–S07 |
| Facebook Reels | Meta anunció unificación de vídeo y Reels y documenta prioridad de contenido original. El anuncio describe un despliegue. Su documentación pública no verifica esta cuenta ni todas sus métricas actuales | Confirmar tipo de perfil, audiencia, flujo de Reel, subtítulos, recorte y métricas del panel. Guardar URL de Facebook aunque se cruce una publicación desde Instagram. S08 y S24 |
| YouTube Shorts | Ayuda oficial documenta Shorts cuadrados o verticales de hasta tres minutos dentro de los criterios aplicables y un bloqueo de Shorts de más de un minuto con un reclamo Content ID activo. Studio distingue vistas de reproducciones interesadas y métricas ligadas a estas | Registrar métrica exacta y ventana, revisar si se puede seleccionar el frame deseado como portada en la ruta utilizada, verificar SRT nativo o incrustado sin duplicación y guardar URL. S04–S05 |

**Métricas [D].** Usar observaciones comparables dentro de cada red. En YouTube guardar `views`, `engaged_views` y `stayed_to_watch_pct` si aparecen y el contexto de sus denominadores. La ayuda de YouTube señala que el conteo de vistas al iniciar reproducción se extendió a formatos de vídeo el 24 de agosto de 2026. En las demás redes guardar el nombre nativo y si es vistas, alcance, tiempo total, promedio o acción. Los recuentos acumulados de +48 h y +7 d se conservan como snapshots, sin sumar ambos. Solo atribuir tráfico cuando exista evidencia de enlace o medición. Si una plataforma retiene estadísticas o cambia la definición, registrar la fecha y alcance. S01, S05, S06 y S08.

**Archivo seguro candidato [D].** Inventariar alcance de fuentes y editables antes de copiar. Confirmar la identidad lógica y la ruta real de cada destino distinto del origen. Registrar verificaciones por copia y conjunto de hashes. Para irremplazables, mantener dos copias independientes verificadas antes de retirar la activa. Probar restauración de un subconjunto y, antes del primer archivo real, reabrir el proyecto nativo desde una ruta distinta. Actualizar el inventario si cambian los bytes. El humano retira medios tras aprobación y comprobación fresca. Solo después se registra OFFLINE. Al restaurar, usar carpeta temporal y verificar antes de enlazar. Mantener licencia/claim y guion en el nivel ligero. Conservar fuentes editables con lockfile, presets y medios que necesitan, y distinguir proxies/cachés regenerables. S12.



## VI. Plan de migración por archivo

Las acciones son para la Fase 2. **Conservar** retiene uso o evidencia. **Modificar** mantiene la función con cambios. **Fusionar** consolida la información vigente y preserva el original. **Mover** cambia ubicación con mapeo. **Deprecar** retira del uso operativo y conserva el original. Las 64 entradas tienen acción primaria. No se propone eliminar archivos históricos. Cualquier futura eliminación se presenta por separado con su alcance y autorización.

| Archivo actual | Acción | Destino y motivo |
|---|---|---|
| `00_INICIO_Y_ESTADO.md` | Modificar | INICIO. Mantener índice mínimo y apuntar al estado, sin copiar pendientes |
| `01_EVIDENCIA_Y_AUDITORIA.md` | Fusionar | FUENTES para evidencia y EDITORIAL para tipología de claims. Preservar las consultas anteriores |
| `02_ESTRATEGIA_EDITORIAL.md` | Modificar | EDITORIAL. Conservar puntuación y alcance propuesto, añadir investigación, objetivos y presupuesto |
| `03_IDENTIDAD_AUDIOVISUAL.md` | Modificar | marca/IDENTIDAD. Separar reglas, pruebas y propuestas, apuntar a tokens |
| `04_SISTEMA_DE_GUIONES.md` | Fusionar | EDITORIAL. Mantener cinco familias, prueba y límites de revisión |
| `05_SOP_SEMANAL_Y_GATES.md` | Modificar | OPERACION. Unificar estados y tres aprobaciones, retener checks técnicos |
| `06_OPERACION_COWORK_CLAUDECODE.md` | Fusionar | OPERACION, con handoff agnóstico y rutas existentes |
| `07_ESPECIFICACION_HYPERFRAMES.md` | Modificar | Sección técnica de OPERACION. Conservar técnicas T01–T12 como repertorio, exigir solo las aplicables |
| `08_MEDICION_Y_APRENDIZAJE.md` | Fusionar | EDITORIAL. Ventanas, definición, comparabilidad y aprendizajes |
| `09_PROMPTS_MAESTROS.md` | Fusionar | OPERACION y plantillas. Reducir a cinco instrucciones por trabajo, conservar correspondencia P00–P18 |
| `10_EJEMPLO_PLAN_SEMANA_01.md` | Mover | proyectos/miminiapp/referencias. Mantener etiqueta de ejemplo y calendario no aprobado |
| `11_PUESTA_EN_MARCHA_Y_CHECKLIST.md` | Fusionar | INICIO y OPERACION. Una sola puesta en marcha y checklist de piloto |
| `12_IDENTIDAD_PERSONAL_Y_HANDLES.md` | Fusionar | marca/IDENTIDAD y CUENTAS. Conservar candidatos y fecha de consulta como histórico |
| `13_GUIA_OPERATIVA_COWORK_WORK_CHATGPT_WEB.md` | Fusionar | OPERACION, capacidades por superficie y traspaso manual |
| `14_POLITICA_ARCHIVO_Y_RESTAURACION.md` | Modificar | OPERACION. Retener copia verificada, offline, recuperación y excepciones |
| `15_MONTAJE_FINAL_GRATUITO.md` | Modificar | OPERACION. Convertir en receta de edición principal y prueba de contingencia |
| `16_GUIA_SEMANA_EN_15_MINUTOS.md` | Fusionar | INICIO y OPERACION. Un recorrido semanal y una primera lectura |
| `17_AUDITORIA_FINAL_ESTANDARES.md` | Mover | legado/v3.5. Conservar auditoría fechada y reutilizar enlaces verificados |
| `18_INGESTA_COLOR_EXPORT_Y_QC.md` | Fusionar | OPERACION. Perfil, ingesta, color, QC y límites comprobables |
| `19_MAPA_DOCUMENTAL_Y_FRECUENCIA.md` | Deprecar | Preservar en legado. INICIO indexa solo documentos vigentes |
| `CLAUDE.md` | Modificar | Adaptador técnico breve. Añadir AGENTS.md para Codex, ambos apuntan al canon |
| `COWORK_INSTRUCCIONES.md` | Fusionar | Sección editorial de OPERACION, con extracto copiable por superficie |
| `MANIFEST_SHA256.json` | Conservar | Mantener original con la copia sellada. Crear huella separada de la nueva release |
| `brand/IDENTIDAD_PROPUESTA.json` | Modificar | Migrar valores a identidad.json con estado candidato, sin generar aprobación |
| `evidencia_tecnica/piloto_hyperframes_8s.mp4` | Conservar | Evidencia técnica privada, hash y limitaciones. Retener MP4 íntegro |
| `fuentes_proyecto/LEER.md` | Fusionar | FUENTES. Preservar origen y carácter de copia de referencia |
| `fuentes_proyecto/guia_set_grabacion.md` | Mover | referencias/set. Conservar copia íntegra y usar OPERACION para ajuste operativo corto |
| `fuentes_proyecto/MiMiniApp_Inicio_Proyecto_Harness_IA_v1.2.md` | Mover | proyectos/miminiapp/referencias. Preservar gobierno del producto y separar alcance |
| `referencias/LEER.md` | Modificar | Índice con procedencia, uso de técnica y restricciones. Corregir ruta del piloto como hermana de referencias |
| `referencias/tecnologia/image(20261105-083522).png` | Conservar | Composición de cara a cámara con agenda |
| `referencias/tecnologia/image(20261105-083524).png` | Conservar | Tarjeta de capítulo y jerarquía |
| `referencias/tecnologia/image(20261105-083525).png` | Conservar | Rotulación técnica junto al creador |
| `referencias/tecnologia/image(20261105-083527).png` | Conservar | Infografía de hardware, referencia activa del par duplicado |
| `referencias/tecnologia/image(20261105-083529).png` | Deprecar | Mismos bytes que 083527. Retener original y vínculo en legado, sin borrar |
| `referencias/tecnologia/image(20261105-083530).png` | Conservar | Composición de creador con comparativa de componentes |
| `referencias/ui_motion/1000845575.jpg` | Conservar | Estado inicial, referencia interna |
| `referencias/ui_motion/1000845576.jpg` | Conservar | Estado intermedio, referencia interna |
| `referencias/ui_motion/1000845577.jpg` | Conservar | Estado final, referencia interna |
| `registro/ARCHIVOS.csv` | Deprecar | ARCHIVO.json será canónico. Si hace falta búsqueda global, índice derivado |
| `registro/CUENTAS_SOCIALES.csv` | Modificar | marca/CUENTAS.csv con perfil, tipo, estado, URL y fecha por red. Mantener pendientes |
| `registro/DECISIONES.md` | Conservar | Importar IDs, fechas, estados y texto histórico sin reescribirlos. Añadir decisiones nuevas como entradas |
| `registro/ENTREGAS.csv` | Deprecar | Salidas por red en CIERRE. Exportar índice solo si se necesita |
| `registro/ESTADO.md` | Fusionar | INICIO apunta a estado activo del vídeo y decisiones. Conservar cortes históricos |
| `registro/IDEAS.csv` | Modificar | Añadir proyecto, procedencia fechada y vínculo a prueba. Puntuación y selección vigentes en la semana |
| `registro/METRICAS.csv` | Modificar | Observaciones por publicación, plataforma, fecha, clave, unidad, denominador y fuente |
| `scripts/crear_semana.py` | Modificar | Separar creación de semana y de episodio y comprobar plantillas antes de escribir |
| `scripts/gestion_archivo.py` | Modificar | Inventario y verificación seguros, una fuente de estado y restauración explícita |
| `scripts/inspeccionar_video.py` | Modificar | Identificar dependencias, alcance técnico y checks que no se hicieron |
| `scripts/preparar_frame_md.py` | Modificar | Proyección determinista de perfil autorizado por versión. Activación tras prueba de necesidad |
| `scripts/validar_paquete.py` | Modificar | Separar comprobaciones de release y operativas. Especificar límites de cada modo |
| `templates/CIERRE_SEMANAL.md` | Fusionar | SEMANA, sección retrospectiva con referencias, sin copiar métricas ni estados de archivo |
| `templates/EDIT_PLAN.md` | Fusionar | PRODUCCION, plan e intercambio técnico por escena referenciada |
| `templates/IDEA.md` | Deprecar | IDEAS.csv y notas vinculadas cuando la investigación lo justifique |
| `templates/INGESTA.md` | Fusionar | PRODUCCION, inventario y copia verificada de originales |
| `templates/LICENCIAS_MEDIOS.md` | Fusionar | CIERRE, permisos por recurso/red y prueba de licencia |
| `templates/MONTAJE_FINAL.md` | Fusionar | PRODUCCION para ruta de proyecto/corte. CIERRE para versión de entrega y QC |
| `templates/PRUEBAS_Y_CLAIMS.md` | Fusionar | GUION, tabla de evidencia y límites por escena |
| `templates/PUBLICACION.md` | Fusionar | CIERRE, filas de publicación y aprobación vinculada al máster |
| `templates/QC_MASTER.md` | Fusionar | CIERRE, control técnico, visual y de derechos |
| `templates/REVISION.md` | Fusionar | PRODUCCION, dos rondas, timecode y picture lock |
| `templates/SCRIPT.md` | Modificar | GUION, consolidar voz y escena en una representación |
| `templates/SEMANA.md` | Modificar | SEMANA, lotes por horas con proyectos e ideas referenciados |
| `templates/TAKES.md` | Fusionar | PRODUCCION, enlace entre toma, escena y original |
| `templates/VIDEO.md` | Fusionar | GUION conserva brief, objetivo y gancho. Publicación y almacenamiento referenciados |

**Secuencia y reversión [D].** Crear copia fechada con hashes y dejarla en modo de referencia. Construir la candidata en carpeta separada. Mapear rutas y documentar cambios por hallazgo y decisión aprobada, con origen, destino, versión y prueba. Importar solo estados respaldados por la v3.5. Conservar las cuatro cuentas pendientes y los CSV históricos vacíos. Probar con fixtures antes de mover datos reales. Validar que todo lo de la matriz conserve una ruta o una referencia al legado. Entregar versión, changelog, guía breve y pruebas. Si falla, volver al árbol v3.5 intacto y mantener la candidata separada.

## VII. Automatizaciones y límites

| Utilidad | Resultado actual | Corrección propuesta y prueba |
|---|---|---|
| Crear semana | Implementada. Copia archivos, protege frente a sobreescritura. T01/T02 | P0. Validar semana ISO, preparar todo antes de confirmar cambios, usar creación segura que no deje directorio incompleto, separar episodio y semana e inyectar IDs. Reintentar sin duplicar. Manual con los mismos moldes |
| Gestionar archivo | Implementada. SHA-256 y errores útiles. T03–T05 | P0 si se usa archivo. Conservar hash, comprobar rutas resueltas y reparse points/enlaces, destino distinto del origen, alcance y evidencias por destino. Un manifiesto por versión, escritura atómica, revalidar cuando cambien fuentes y transiciones coherentes. Sin limpieza automática |
| Inspeccionar vídeo | Código existente. T08 impidió ejecutar inspección real | P0. Registrar versión de ffprobe, inspeccionar contenedor, orientación, pistas, perfil de color, rango, timestamps y formato de audio según perfil. Desglosar MEDIDO, AVISO, FALLA y SIN_MEDIR. Prueba sobre clip real, fixture incompatible y resultado sin dependencia. QC humano sigue siendo criterio de salida |
| Preparar frame | Bloquea ausencia de aprobación. Acepta campos inválidos. T07 | P1 tras necesidad demostrada. Validar tipos, tokens, fecha, versión y referencia a decisión. Generar en el proyecto técnico correcto y comprobar coherencia con entrada. Proyección derivada con huella. TEMP solo con perfil aislado y permiso aplicable |
| Validar paquete | Hashes e IDs reales. T06 muestra falso positivo y mal encaje con registros vivos | P0. Mantener verificación de release y añadir modo operativo de solo lectura con lista requerida, enlaces, IDs, estados/aprobaciones y permisos de edición. Los binarios offline declarados tienen reglas distintas de los documentos faltantes |
| Generar handoff e índice | Prompts y documentación. Sin mecanismo ejecutado | P1 solo si dos traspasos muestran repetición. Exportar manifest y extractos por episodio de forma determinista. P2 para índice global generado. Sin nueva base de datos, colas o servicio |

**Proveedor y seguridad [D/O].** Cowork/Work preparan investigación y borradores. Cowork de escritorio depende del modo y permisos de carpeta, y el comportamiento de proyectos vinculados varía por superficie. Work de escritorio puede abrir una carpeta autorizada. En web se intercambian adjuntos y diffs por versión. Claude Code carga CLAUDE.md, Codex AGENTS.md según su configuración. Esas instrucciones no son un control de acceso. Conceder solo la carpeta del episodio o un paquete saneado y verificar permisos reales. Separar credenciales, directorios privados y originales sensibles. Tratar páginas, referencias, metadatos y material de terceros como datos, y no ejecutar sus instrucciones ni comandos copiados. Desactivar publicación, compras y borrados por agente. S20–S22.

**Reanudar y limitar contexto [D].** Cada tarea recibe ID, versión base, último estado, aprobaciones, archivos mínimos, permisos, bloqueo y siguiente acción. P00/P18 se concentran en el arranque. P01–P03 quedan como dirección/guion. P04/P17 son asistencia de captura. P05–P09/P15/P16 pasan al traspaso técnico y montaje/QC. P10–P14 se invocan según medición, marca o archivo. Una tarea rutinaria abre índice, sección aplicable, ficha del proyecto y episodio. El histórico y el dossier web de 66 KB se consultan cuando la tarea los necesita. Se usa instalación fijada y recursos locales autorizados. Antes de correr un comando que pueda descargar Node, navegador o paquetes, comprobar la versión disponible y el alcance autorizado. Un error se registra con versión, comando, condición y siguiente acción. Tras una repetición sin cambios de diagnóstico, reducir alcance o cambiar a la alternativa probada. Las horas humanas, minutos de render y consumo observable se anotan una sola vez. Si no hay dato de consumo, marcar no disponible.

**Límites humanos.** Alexander elige temas y guion, aprueba marca/alias, instala si lo autoriza, graba, decide el corte, verifica audio/color/legibilidad, acepta derechos por destino, publica, conecta discos y autoriza retirada. Las herramientas ayudan a preparar, medir, reproducir y comparar. La disponibilidad de una función, una biblioteca de recursos o una cuenta se comprueba antes de incorporarla al flujo. En licencias, registrar recurso y versión, autor, URL, fecha, prueba, ámbito por red y uso, atribución, vigencia y posibilidad de conservar/reutilizar la fuente. Si falta permiso para un destino, usar variante autorizada o posponer ese destino.

## VIII. Plan de implementación priorizado

Horas humanas orientativas. Supuestos: una persona con asistencia, documentación en Markdown, sin base de datos, un entorno Windows con acceso a las herramientas que se autoricen, material de prueba disponible y alcance vertical SDR. Excluyen tiempo de desarrollo web, aprendizaje extenso de edición, render desatendido, esperas de publicación y validación de cuentas. Un bloqueo de instalación, cuenta o códec cambia la estimación.

| Prioridad / tarea | Dependencia y esfuerzo | Criterio de aceptación |
|---|---|---|
| P0.1 · Copia sellada, mapeo y canon de datos | Aprobación de Fase 2. 2–3 h | Original verificable, matriz aplicada, estado pendiente conservado y expedientes con ID global |
| P0.2 · SOP, tres plantillas y aprobación | P0.1. 3–5 h | Dos proyectos en una semana con el mismo sistema. Handoff a editor, QC y publicación no dependen de duplicar archivos |
| P0.3 · Generación y validación segura | P0.2. 2–3 h | Tests de alta, reintento, plantilla faltante, rechazo de ruta inválida y aprobación no acreditada. Ruta manual documentada |
| P0.4 · Prueba técnica de extremo a extremo en Windows | P0.2 y herramientas autorizadas. 3–5 h | Exportación real con Samsung/DJI, HyperFrames, editor gratuito, voz, subtítulos y QC móvil. Una ruta principal reabre y exporta el proyecto nativo |
| P0.5 · Archivo de prueba y protección | P0.1 y P0.2. 2–4 h | Verificación rechaza origen, copia vieja y material alterado. Consulta offline y recuperación seguras. Hasta pasar, archivo físico y retirada quedan inhabilitados en piloto |
| P1.1 · Primer ciclo y métricas por red | P0, autorización de publicación y cuentas. 2–4 h de ajuste de proceso, más producción | Una pieza sencilla aprobada. Guardar versión/hash y URL o evidencia de fallo por red. Snapshot de cada ventana cuando haya datos |
| P1.2 · Continuidad y segunda iteración | P1.1. 2–4 h de ajuste, más producción | Reanudar desde una conversación nueva, terminar un segundo ciclo y medir cuello de botella. Decidir cadencia con horas reales |
| P1.3 · Probar perfil visual y mejora de handoff | P0.4 y decisión separada de Alexander. 2–4 h | Dos frames legibles, registro de decisión y prueba de fuente/licencia. Automatizar el dossier solo si el traspaso manual lo pide |
| P2.1 · Vistas derivadas o ayudas de QC | Datos de P1. 1–3 h por mejora | Demostrar reducción de tiempo o errores frente a la operación manual |
| P2.2 · Formatos y técnicas adicionales | Necesidad editorial y equipo disponible. 2–5 h por prueba | Prueba real de alfa, 4K, HDR, multicámara, Remotion o DaVinci según la necesidad seleccionada. Excluir del perfil habitual hasta validar |

**P0 estimado 12–20 h. P1 estimado 6–12 h de estabilización, además del tiempo de producir dos ciclos.** Para planificar una primera pieza sencilla, reservar 2–4 h humanas si ya existe prueba de producto y se usa un patrón básico. Una escena a medida eleva ese coste. Registrar diferencias y mover el volumen antes de recortar QC.



## IX. Pruebas de aceptación de la candidata

Ejecutar primero con datos ficticios identificados y carpeta de prueba. Un resultado de la v3.5 en T01–T08 no se transfiere a la candidata. Usar las plataformas reales solo con perfiles y salida autorizados. Si una prueba externa queda bloqueada, registrar alcance y continuar las pruebas independientes.

| ID | Caso y entradas | Evidencia de aceptación |
|---|---|---|
| A01 | Crear semana ISO válida vacía. Repetir y probar semana ISO inválida | Un borrador con horas y lote vacío. Segundo intento preserva datos y la inválida se rechaza |
| A02 | Añadir dos expedientes después de crear la semana. Quitar una plantilla en fixture y reintentar | Cada expediente tiene ID estable y tres documentos. Error no deja estructura parcial. Los IDs y guiones anteriores se conservan |
| A03 | Añadir una idea de MiMiniApp y un tutorial de Git independiente. Reprogramar uno | Dos proyectos en el mismo lote. Cada uno hereda marca personal, usa su propia prueba y mantiene ID. Tutorial no pide miniapp, staging ni copia del sistema |
| A04 | Aprobar un guion y transferirlo al editor. Introducir claim X y luego cambiar versión | El editor recibe versión/huella, escenas, voz literal, pruebas, tomas y permisos. Se bloquean claim no comprobado y revisión obsoleta |
| A05 | Generar dossier HyperFrames para una escena con voz o guía y una sin audio | Incluye frame/tiempo, recursos, derechos, estado de marca, alcance y checks. Una escena renderiza, reproduce, se inspecciona y se importa con el audio esperado. Dossier con referencias rotas falla |
| A06 | Intercambio de 15–25 s en Windows con Samsung/DJI y editor gratuito | MP4 sin marca y sin Pro, 9:16, voz, tres subtítulos, sincronía, color y reproducción móvil. Proyecto nativo reabre. Registrar versión, tiempos y ruta de contingencia si aplica |
| A07 | Cambiar timing después de picture lock o reemplazar bytes del máster tras OK-3 | El corte cambiado pierde lock y la variante pierde aprobación de salida hasta revisión. El master original sigue identificable |
| A08 | Registrar publicación de fixture en dos destinos, con uno fallido. Después repetir con una pieza real autorizada | Fila independiente por plataforma y versión/hash. Sin URL inventada. Reintento no duplica el mismo acto. Verificación del post real y cuenta en P1 |
| A09 | Cargar snapshots de +48 h y +7 d, dos redes, cero y dato ausente | Consulta devuelve por red, nombre y denominador, conserva ventanas y diferencia cero de ausencia. No agrega métricas incompatibles |
| A10 | Archivar con fixtures. Probar mismo origen, copia alterada, verificación antigua y recursos fuera de alcance | Rechaza origen y desajustes. No certifica datos nuevos a partir de copia anterior. Solo transiciona tras evidencia por destino, aprobación y retirada registrada. Manifiesto auditable |
| A11 | Consultar episodio archivado desconectando carpeta de medios de prueba | Responde de idea, proyecto, aprobación, derechos, URL, métricas y ubicación desde archivos ligeros. Si se pide ver fotogramas, informa el bloqueo de medios |
| A12 | Recuperar un recurso y reabrir un proyecto de editor desde otra ruta | Hash de la selección coincide, documentos actuales intactos, medios referenciados se religan. Estado temporal correcto y salida histórica preservada. Prueba física con soporte antes de uso real |
| A13 | Reanudar en una conversación o proveedor distinto sin historial de chat | A partir del paquete mínimo identifica última versión, aprobación, bloqueo y siguiente paso. Devuelve cambios sin pisar una versión más reciente. Registrar superficie y permisos probados |
| A14 | Retirar un documento obligatorio y simular aprobación incompleta de marca o de entrega | El validador reporta documento y campo concreto. Un medio offline declarado no dispara un falso faltante. El perfil TEMP no concede publicación pública |
| A15 | Simular bloqueo Pro, importación SRT fallida o audio/SDR inesperados | Se registra causa, se usa el camino gratuito probado o se bloquea la salida. Al comparar reproducción y metadatos, QC identifica el desajuste |

## X. Veredicto de preparación y decisiones

| Nivel | Condición verificable | Estado |
|---|---|---|
| No preparado | Flujos fundamentales tienen fallos reproducidos o falta la prueba de intercambio y QC | **Estado de v3.5.** T01, T04, T06 y T08 bloquean la puesta en marcha con garantías. Se puede revisar y ensayar documentación |
| Preparado para piloto controlado | P0 completada y A01–A07, A10–A12, A14–A15 aprobadas con fixtures y material de cámara real donde corresponda. Cuenta y aprobación adicionales para piloto público | Pendiente. La prueba técnica puede ser interna y temporal. Sin retirada de originales reales durante el ensayo |
| Preparado para producción recurrente | Dos ciclos completos con presupuesto y QC, al menos dos proyectos probados en el sistema, evidencias de publicación y métricas reales donde estén disponibles, continuidad entre sesiones y restauración con medios propios | Pendiente. Se sube la frecuencia tras medir tiempo, rendimiento y calidad. No se deduce de una validación de hashes |

**Decisiones que sí requieren a Alexander.**

| Decisión | Opciones e implicaciones | Propuesta |
|---|---|---|
| Alcance de Fase 2 | Aprobar P0 completa, ajustar alcance o posponer. P0 implica construir candidata aparte y comprobarla, con instalaciones separadas si fueran necesarias | Aprobar P0 como primer bloque. P1 y P2 se activan según evidencia y capacidad |
| Alcance del piloto | Interno TEMP permite probar sin definir marca pública. Público provisional requiere perfil específico, cuenta(s) verificadas y autorización de salida. Esperar marca definitiva aplaza aprendizaje de distribución | Empezar interno. Evaluar publicación de la primera pieza solo después del QC del equipo |
| Cadencia inicial | Una pieza prioritaria y una opcional, dos comprometidas, o tres si el tiempo medido lo permite. A más piezas simultáneas, menos margen de aprendizaje del editor y de pruebas | Una sencilla más una opcional en el primer ciclo. Fijar dos o tres a partir de tiempos reales |
| Marca y alias | Perfil provisional aprobado para una salida concreta o identidad definitiva tras revisar dos frames y cuentas. Un alias común requiere comprobación dentro de cada plataforma | Mantener alias, paleta, tipografías y firma pendientes. Resolver solo las decisiones necesarias para la siguiente salida |

La Fase 1 entrega el diagnóstico y estas propuestas. La Fase 2 requiere aprobación explícita. Las pruebas sobre material real y el acceso a funciones concretas de cuentas, editores y agentes siguen pendientes.

## Fuentes externas

**Fecha de consulta de cada entrada — 8 de noviembre de 2026.** [O] indica documentación o comunicación primaria del proveedor. [BP] indica una referencia técnica, práctica del sector o método transferible. La disponibilidad concreta por cuenta, región o versión sigue sujeta a prueba. Los enlaces que exigieron sesión o devolvieron contenido limitado se identifican por su alcance.

| Ref. | Tipo y conclusión acotada | Enlaces |
|---|---|---|
| S01 | [O] TikTok dispone de herramientas de investigación de búsquedas, Studio y opciones de accesibilidad. Algunas páginas directas devolvieron texto limitado. La disponibilidad y métricas de la cuenta no se verificaron | [Centro de ayuda, resultados de Search Insights y Studio](https://support.tiktok.com/en/search?searchTerm=tiktok+creator+search+insights) · [Accesibilidad en TikTok](https://support.tiktok.com/en/using-tiktok/accessibility) |
| S02 | [O] Material de TikTok for Business sobre diseño de anuncios y legibilidad. Transferible como inspiración, sin extrapolar rendimiento ni reglas orgánicas | [TikTok Creative Best Practices](https://ads.tiktok.com/resources/help/article/creative-best-practices?lang=es) |
| S03 | [O] TikTok documenta divulgación de contenido que promociona marca, producto o servicio, incluida la marca propia, y uso comercial de música. El permiso no se generaliza a otras redes | [Promoción y divulgación](https://support.tiktok.com/en/business-and-creator/creator-and-business-accounts/promoting-a-brand-product-or-service?lang=en) · [Uso comercial de música](https://support.tiktok.com/en/business-and-creator/creator-and-business-accounts/commercial-use-of-music-on-tiktok?lang=en) |
| S04 | [O] Recomendaciones de subida SDR a YouTube, perfiles MP4/H.264, FPS, audio y bitrate. Referencia de diseño del máster común | [YouTube, codificación de subida](https://support.google.com/youtube/answer/1722171?hl=en) |
| S05 | [O] Elegibilidad de Shorts, reclamos activos para más de un minuto y definiciones de vistas/engaged views | [Shorts de tres minutos](https://support.google.com/youtube/answer/15424877?hl=en) · [Analytics de Shorts](https://support.google.com/youtube/answer/12942217?co=YOUTUBE._YTVideoType%3Dshorts&hl=en) · [Cómo se cuentan las vistas](https://support.google.com/youtube/answer/2991785?hl=en) |
| S06 | [O] Meta documenta consejos en panel profesional, pruebas con no seguidores y métricas de tiempo. Cada función debe comprobarse en cuenta | [Instagram Best Practices](https://about.fb.com/news/2024/10/best-practices-education-hub-creators-instagram/) · [Trial Reels](https://about.fb.com/news/2024/12/trial-reels-try-content-non-followers-first-see-what-perfoms-best/) · [Métricas de tiempo en Reels](https://about.fb.com/news/2023/04/instagram-reels-trending-audio-and-gifts-updates/) |
| S07 | [O] Colección oficial Meta para API de publicación de Reels. Los enlaces de ayuda orgánica se redirigieron a inicio de sesión. Los valores de API no se atribuyen al editor manual | [Instagram API, Reels Publishing](https://www.postman.com/meta/instagram/folder/830j7my/reels-publishing) · [Ayuda de tamaño orgánico, acceso limitado](https://www.facebook.com/help/instagram/1038071743007909) · [Ayuda de insights, acceso limitado](https://www.facebook.com/help/instagram/202865988324236) |
| S08 | [O] Meta anunció simplificación del vídeo como Reels y priorización de originales. La página de reglas musicales redirigió a inicio de sesión. Los permisos deben acreditarse por pista y destino | [Unificación de vídeo y Reels](https://about.fb.com/news/2025/06/making-it-easier-create-videos-facebook/) · [Originalidad en Facebook](https://about.fb.com/news/2026/03/rewarding-original-creators-on-facebook/) · [Reglas musicales, acceso limitado](https://www.facebook.com/legal/music_guidelines) |
| S09 | [O] HyperFrames documenta composición HTML, línea de tiempo y render. El motor documenta Node 22+, navegador y FFmpeg. La CLI actual indica que la versión instalada es la autoridad y documenta `check` y `lint` | [Composiciones](https://github.com/heygen-com/hyperframes/blob/main/docs/concepts/compositions.mdx) · [Motor](https://github.com/heygen-com/hyperframes/blob/main/packages/engine/README.md) · [CLI](https://github.com/heygen-com/hyperframes/blob/main/docs/packages/cli.mdx) |
| S10 | [O] HyperFrames documenta render y contrato HTML. Los formatos admitidos por el motor no demuestran importación en otro editor | [Render](https://github.com/heygen-com/hyperframes/blob/main/docs/guides/rendering.mdx) · [Esquema HTML](https://github.com/heygen-com/hyperframes/blob/main/docs/reference/html-schema.mdx) |
| S11 | [O] HyperFrames documenta `frame.md` como primera opción de diseño audiovisual en su repertorio actual. CapCut explica importación de subtítulos, bloqueo por Pro y exportación sin marca con recursos elegibles | [Especificación de diseño HyperFrames](https://github.com/heygen-com/hyperframes/blob/main/skills/hyperframes-creative/references/design-spec.md) · [CapCut, SRT](https://www.capcut.com/es-es/help/how-to-import-subtitles) · [Bloqueo Pro](https://www.capcut.com/help/join-capcut-pro-for-exporting) · [Marca de agua](https://www.capcut.com/help/video-without-watermark) |
| S12 | [BP] Frame.io documenta etapas de edición y comprobaciones de integridad. Se adapta al trabajo de una persona y a un procedimiento de recuperación | [Etapas de edición](https://workflow.frame.io/guide/editing-stages) · [Checksums y copias](https://workflow.frame.io/guide/checksums-backups) |
| S13 | [O/BP] Shotcut documenta preview scaling y proxies. Adobe explica la distinción entre original y copia de trabajo para Premiere, sin asumir igual implementación en CapCut | [Shotcut, FAQ](https://www.shotcut.org/FAQ/) · [Shotcut, guía](https://shotcut.org/howtos/Shotcut%20User%20Guide.pdf) · [Adobe, ingesta y proxies](https://helpx.adobe.com/premiere/desktop/organize-media/ingest-proxy-workflow/ingest-and-proxy-workflow.html) |
| S14 | [O] Samsung documenta HDR10+ de vídeo en modelos y modos compatibles. El modo y firmware del teléfono concreto se comprueban en ensayo | [Samsung, HDR10+ en Galaxy](https://www.samsung.com/us/support/answer/ANS10003388/) |
| S15 | [O] FFprobe permite inspeccionar contenedor, pistas y fotogramas. La interpretación de metadatos y el control perceptual son pasos diferentes | [FFprobe](https://www.ffmpeg.org/ffprobe.html) |
| S16 | [O/BP] W3C WCAG 2.2 documenta contraste mínimo, subtítulos para audio pregrabado y umbrales de destellos. Se usa como referencia de accesibilidad, sin afirmar conformidad formal del vídeo social | [Contraste](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html) · [Subtítulos](https://www.w3.org/WAI/WCAG22/Understanding/captions-prerecorded.html) · [Destellos](https://www.w3.org/WAI/WCAG22/Understanding/three-flashes-or-below-threshold.html) |
| S17 | [O/BP] EBU define medición y normalización de sonoridad y picos en su ámbito. Sus objetivos no se imputan a TikTok, Meta o YouTube | [EBU R 128](https://tech.ebu.ch/publications/r128) · [Suplemento streaming](https://tech.ebu.ch/publications/r128s2) |
| S18 | [O/BP] YouTube publica un caso de creadora sobre gancho y ritmo. Sus criterios son experiencia editorial y no garantizan distribución | [Conversación de Shorts con Todd Sherman y Jenny Hoyos](https://blog.youtube/creator-and-artist-stories/youtube-shorts-deep-dive/) |
| S19 | [BP] Investigación centrada en qué intenta hacer la gente, qué usa ahora y qué supuestos quedan por comprobar. Se adapta a una revisión editorial breve | [GOV.UK, investigación de usuarios](https://www.gov.uk/service-manual/user-research/how-user-research-improves-service-design) · [Planificar una ronda](https://www.gov.uk/service-manual/user-research/plan-round-of-user-research) |
| S20 | [O] Claude Cowork documenta proyectos y capacidades por superficie. La portabilidad del expediente no depende de sincronización entre proveedores | [Proyectos en Cowork](https://support.claude.com/es/articles/14116274-organiza-tus-tareas-con-proyectos-en-claude-cowork) · [Cowork web, escritorio y móvil](https://support.claude.com/en/articles/15520349-use-claude-cowork-on-web-desktop-and-mobile) |
| S21 | [O] Claude Code documenta carga de CLAUDE.md y permisos. Codex documenta AGENTS.md. Las instrucciones por archivo no sustituyen una prueba de permisos | [Claude Code, instrucciones](https://code.claude.com/docs/en/memory) · [Permisos](https://code.claude.com/docs/en/permissions) · [Codex, AGENTS.md](https://developers.openai.com/codex/guides/agents-md/) |
| S22 | [O] OpenAI documenta uso de carpetas locales en escritorio con permisos y organización del contexto en proyectos. Work web no accede directamente a archivos del PC | [ChatGPT Work y Codex](https://help.openai.com/es-es/articles/20001275-chatgpt-work-y-codex) · [Proyectos en ChatGPT](https://help.openai.com/es-es/articles/10169521-projects-in-chatgpt) |
| S23 | [O] YouTube explica que el descubrimiento se personaliza y documenta señales de interacción, sin imponer una frecuencia de publicación. Útil al formular hipótesis de retención | [Descubrimiento de Shorts](https://support.google.com/youtube/answer/11914225?co=YOUTUBE._YTVideoType%3Dshorts&hl=en-GB) |
| S24 | [O] Meta explica herramientas para experimentar con contenido y consultar insights en Facebook. La función disponible en la cuenta queda por comprobar | [Pruebas e insights para creadores en Facebook](https://about.fb.com/news/2023/11/helping-creators-test-content-and-earn-rewards/) |

