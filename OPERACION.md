# Operación P0

## Dónde vive cada dato

| Dato | Fuente editable |
|---|---|
| Decisión transversal, alcance nuevo y política | registro/DECISIONES.md |
| Perfil público y cuentas por red | marca/IDENTIDAD.md y marca/CUENTAS.csv |
| Prueba del proyecto y materiales de referencia | proyectos/<proyecto>/PROYECTO.md |
| Idea | registro/IDEAS.csv |
| Lote y capacidad | semanas/AAAA-WNN/SEMANA.md |
| Guion, storyboard, claims y OK-2 | videos/VID-NNNN/GUION.md |
| Estado, siguiente paso, ingesta, montaje y corte fijado | videos/VID-NNNN/PRODUCCION.md |
| QC, licencia, máster, OK-3, autorización y resultados por red | videos/VID-NNNN/CIERRE.md |
| Observación por publicación y fecha | registro/METRICAS.csv |
| Disponibilidad y copias de medios | ARCHIVO.json del episodio |

El vídeo conserva ID, proyecto e idea si cambia de semana. Pasa la asignación antigua a retrospectiva, actualiza los dos lotes y vuelve a validar OK-1 donde cambió la huella. La carpeta videos no depende de la semana. Utiliza un escritor a la vez. Una propuesta devuelta por otra conversación incluye versión base. Compara la huella antes de aplicarla. Las plantillas son moldes. El agente trabaja con referencias, rutas y archivos mínimos y se detiene si una autorización falta.

## Secuencia y aprobaciones

| Etapa | Acción humana y condición |
|---|---|
| OK-1 | Seleccionar lote y horas netas. Huella de Control y Lote |
| OK-2 | Aprobar guion, evidencia, escenas y alcance. Huella de Control, Brief, Escenas y Claims. Un borrador puede existir antes de OK-1. Un OK-2 válido exige OK-1 vigente |
| Producción y picture lock | Grabar, verificar originales, animar si aporta y montar. La huella de corte liga guion, perfil, timing y bytes de una vista de corte o proyecto autocontenido. Registra correcciones y tiempo antes de fijar el corte |
| OK-3 | Alexander verifica el máster exacto, derechos, QC y corte fijado. Huella de Control, Derechos, QC y Plan de publicación. Un OK-3 de un ensayo interno puede aprobar QC sin plan público |
| Autorización independiente de publicación | Una fila por salida enlaza a OK-3. Exige cuenta verificada, perfil público aprobado aparte y evidencia expresa por destino. Solo Alexander realiza la publicación |
| Resultado | Una fila por publicación y una clave única, por ejemplo VID-0001-YT-01. Usa fecha con zona y URL real solo al confirmar. Si un destino falla, anota causa y conserva el resultado de los demás |
| Métricas y archivo | Registra por ID en METRICAS. El archivo de medios no cambia el estado editorial ni retira los documentos |

El comando de huellas solo calcula. En cada control, Alexander registra nombre, fecha ISO, referencia al permiso y huella que revisó. Una huella asegura correspondencia con los datos, no autentica a quien escribe. Mantén una copia del registro humano que respalda cada aprobación. Anula el alcance al cambiar versión. Si caduca OK-2, el corte y OK-3 asociados requieren revisión. Si cambia corte o máster, la salida afectada exige un nuevo QC y una nueva autorización. Gastos, instalación, acceso a material personal, decisiones de marca, retirada y publicación son permisos independientes. Los scripts trabajan localmente y no realizan esas acciones.

Para una nueva variante o republicación tras cerrar la primera, conserva los bytes previos. Mueve el contenido de las secciones Control, Derechos, QC, Plan de publicación, OK-3, Autorización de publicación y Publicaciones a los mismos encabezados con sufijo de revisión, por ejemplo Control [v01]. Copia solo los cuerpos tal como fueron aprobados. Restablece las secciones activas desde el molde con Revision_cierre v02 y plan nuevo. Cada salida aprobada conserva sus propios derechos, QC, huellas, perfil, cuenta y permiso. Usa nuevos IDs de publicación y rutas de artefacto. Conserva en el historial de Producción o de Guion cualquier evidencia original del corte y la versión revisada. El expediente sigue teniendo tres Markdown.

Estados de PRODUCCION: BORRADOR, SELECCIONADO, AUTORIZADO_PARA_PRODUCIR, EN_PRODUCCION, LISTO_PARA_PUBLICAR, PUBLICADO, ANALIZADO, BLOQUEADO o CANCELADO. BLOQUEADO incluye motivo y siguiente paso. LISTO_PARA_PUBLICAR requiere OK-3 y un destino con autorización pública. Los ensayos TEMP pueden conservar OK-3 interno en EN_PRODUCCION.

## Rodaje, edición y QC

Antes de OK-2, prepara en GUION una propuesta de edición por escena y revisa junto con Alexander qué debe quedar grabado. Durante el montaje registra en PRODUCCION los tiempos y ajustes efectivos. En CIERRE verifica cómo se leen los textos en móvil, que la voz domine la mezcla, que el color mantenga la piel y la interfaz y que los recursos tengan derechos acreditados para los destinos previstos. Consulta la [guía de dirección de edición](referencias/DIRECCION_DE_EDICION.md).

1. Comprueba foco, parpadeo, exposición y voz. Transfiere el original sin recomprimir y contrasta copia, metadatos y sincronía. Mantén original, copia de trabajo y proxy separados.
2. Prepara en PRODUCCION el intercambio por ID de escena, fotogramas, rango, fuentes, pistas, audio, perfil y prueba de seek. Incluye versiones de las herramientas, links a recursos autorizados y huella de GUION. HyperFrames se limita a la animación que aporte. Entrega MP4 por escena, WAV y SRT si aplican, más fuentes editables.
3. Edita el rough cut. Usa CapCut Desktop si la prueba gratuita pasa, o Shotcut validado. Revisa voz y timing en el inicio y final, evita duplicar voz guía, fija el corte y realiza acabado. Exporta desde originales o intermedio de calidad. No actives Pro. Dos rondas focalizadas como referencia.
4. Conserva el máster en entregas con versión. El perfil inicial es 1080×1920, 30 CFR, MP4 H.264 progresivo, SDR BT.709 y audio AAC-LC 48 kHz si hay voz. Si aparecen HDR o VFR, registra y prueba la conformación antes de montar. Revisa el archivo completo en móvil, incluidos voz, texto, recortes, derechos y ausencia de marca de agua. Puedes inspeccionar con `python -B scripts/inspeccionar_video.py <archivo> --perfil SDR1080P30 --audio voz`. La comprobación de metadatos es parcial hasta revisar el clip.

El [protocolo audiovisual](PILOTO_AV.md) define la prueba de CapCut, Shotcut y HyperFrames con material autorizado. El perfil TEMP solo es interno. Las referencias visuales sirven para estudiar técnica. Conserva licencia, procedencia y alcance de cada recurso.

## Archivo de medios y restauración

Medios dentro de media, hyperframes, montaje y entregas. Conserva todos los recursos y editables necesarios para reabrir el proyecto. El inventario incluye todos los archivos de esos árboles. Si un recurso vive fuera, clasifícalo primero. Protege permisos de licencia y no incluyas credenciales ni material sin derecho de archivo. Los tres Markdown y el manifiesto quedan accesibles.

1. En un episodio ficticio, antepone `--fixture` a la acción de gestión de archivo. En el uso real se exige un soporte separado y evidencia física antes de preparar la retirada. El archivador no mueve ni borra originales.
2. `inventariar VID-0001 v01` congela rutas, tamaños y SHA-256. Trata los medios como irremplazables por defecto. Se permite `--reemplazable` cuando el propietario documenta por qué.
3. Copia los árboles inventariados a cada soporte. `verificar VID-0001 v01 --soporte DISCO_A --relativa archivo/VID-0001/v01 --destino <ruta>` compara la lista completa. La ruta efectiva debe terminar con la ruta relativa declarada. Dos etiquetas no pueden corresponder a la misma ruta ni al mismo volumen en uso real.
4. `preparar-retiro VID-0001 v01 --soportes DISCO_A DISCO_B --aprobador Alexander --evidencia <referencia> --prueba-fisica <referencia>` revalida origen y copias de menos de 24 horas. La referencia física acredita restauración de prueba y que los soportes son físicamente independientes. Volumen distinto es un control técnico, no demuestra disco físico distinto.
5. La retirada real es manual y necesita permiso expreso. Detén otras escrituras y comprueba el alcance autorizado. Tras retirar solo los medios aprobados, `registrar-offline VID-0001 v01 --retirada <referencia>` comprueba ausencia en origen y revalida copias. Si no se retiró nada, se puede cancelar la preparación y verificar de nuevo.
6. Para recuperar, conecta un soporte y usa `recuperar VID-0001 v01 --soporte DISCO_A --destino <ruta_de_copia> --salida <ruta_nueva> --archivos <ruta_relativa>`. Comprueba el resultado y religa fuentes en el editor desde la salida nueva. Los documentos vigentes y el máster histórico se conservan. La recuperación cambia disponibilidad a RESTAURADO_TEMPORAL, con salida y selección registradas.

Invoca las acciones con `python -B scripts/gestion_archivo.py`. Comprueba y consulta ARCHIVO.json aunque el disco esté desconectado. Usa el inventario para localizar medios, sin abrir rutas indisponibles. No cambies manualmente la disponibilidad para sortear controles. Si falla una escritura tras recuperar bytes, conserva la copia verificada, revisa su registro y usa otro destino nuevo en el reintento.

## Ruta manual, traspaso y mantenimiento

- Para crear manualmente, copia SEMANA en la ruta ISO o los tres Markdown en videos/VID-NNNN y completa todos los marcadores. Añade el proyecto al que corresponde y la idea al registro. Valida antes de usar.
- Entrega al editor la huella de GUION, fuentes autorizadas, entradas, perfil y decisión vigente. Adjunta solo los materiales de ese episodio. Para reanudar, lee siguiente paso y bloqueo, valida versiones y aplica cambios solo a una versión base coincidente.
- Durante un expediente, el dossier es una sección de PRODUCCION. Los archivos pesados y los cachés quedan fuera de los traspasos. Mantén por versión las fuentes necesarias y elimina del alcance de archivo cualquier caché reproducible antes de inventariar, bajo revisión humana.
- Modo release verifica archivos exactos y copia v3.5. Modo operacion verifica documentos vigentes y permite faltas de medios justificadas por el manifiesto. No modifica decisiones ni infiere permisos.
