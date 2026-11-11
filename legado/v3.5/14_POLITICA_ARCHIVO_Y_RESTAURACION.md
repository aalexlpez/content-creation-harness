# 14 — Política de archivo audiovisual y restauración (revisada v3.5)

**Responsable de decisión:** Alexander. **Estado:** procedimiento añadido al marco, aún no ejecutado con discos del propietario. **Ámbito:** contenido audiovisual personal (MiMiniApp es solo uno de los productos), no el repositorio de la aplicación.

## Regla central

**El histórico editorial debe seguir funcionando sin acceso al metraje antiguo.** Nunca exigir que una carpeta `media/`, `preview/`, `delivery/` o `hyperframes/` permanezca montada para abrir una nueva semana, redactar un guion o consultar métricas anteriores. Una ruta fuera de línea no implica que el episodio no exista ni que sus datos estén perdidos.

### Dos niveles de almacenamiento

| Siempre accesible (ligero / canónico) | Trasladable a soporte externo (pesado) |
|---|---|
| `registro/DECISIONES.md`, `registro/ESTADO.md`, `registro/IDEAS.csv`, `registro/ENTREGAS.csv`, `registro/METRICAS.csv`, `registro/ARCHIVOS.csv` | Vídeos originales, audio sin comprimir, previsualizaciones, renders masters y variantes |
| `semanas/AAAA-WNN/PLAN.md`, guion, storyboard, `EDIT_PLAN.md`, QA, copy y metadatos de publicación | Proyecto de edición HyperFrames y assets propios de una producción cerrada |
| `semanas/AAAA-WNN/videos/Vxx/ARCHIVO.json` y una muestra fija si es necesaria para reconocer el episodio | Secuencias PNG, MOV transparentes, efectos no compartidos, archivos auxiliares grandes |
| Biblia visual personal, assets compartidos vigentes y scripts | Material temporal reproducible; la caché puede purgarse sin archivar si no tiene valor |

**No mover las dependencias compartidas** necesarias para nuevos vídeos (identidad, música licenciada de uso recurrente, tipografías que tengas derecho a utilizar, componentes HyperFrames comunes, plantillas). Nunca archivar como si fueran descartables los únicos originales.

## Estados de disponibilidad (no son estados editoriales)

- `LOCAL_ACTIVO`: medios accesibles localmente.
- `COPIA_EXTERNA_VERIFICADA`: copia externa contrastada con tamaños y SHA-256; todavía se conserva el original local.
- `ARCHIVADO_OFFLINE`: medios retirados del espacio activo; ubicación lógica registrada; soporte puede estar desconectado. **Estado válido, no error.**
- `RESTAURADO_TEMPORAL`: medios devueltos al espacio activo para reedición.
- `NO_LOCALIZADO`: solo tras intentar acceder a la ubicación registrada y comprobar que falta o está dañada; requiere incidencia y búsqueda de respaldo. No etiquetar así porque el disco esté desconectado.

`PUBLICADA` y `ANALIZADA` son estados **editoriales** independientes de estos estados de almacenamiento.

## Cómo archivar un episodio cerrado (A0–A5)

0. **A0 / autorización:** episodio `PUBLICADA` y con QC aprobado; métricas y documentación de publicación guardadas. Alexander aprueba el archivo. Se puede archivar después de publicar sin esperar a que finalicen las ventanas de métricas: estas se registrarán sin el MP4 local.
1. **A1 / inventario:** en el directorio del marco, ejecutar `python scripts/gestion_archivo.py inventariar AAAA-WNN V01 --archive-id NOMBRE_DEL_DISCO --relative-path AAAA-WNN/V01`. Crea `ARCHIVO.json` con rutas relativas, tamaños, SHA-256 y estado `LOCAL_ACTIVO`. No mueve ni borra nada.
2. **A2 / copia:** copiar la carpeta completa `semanas/AAAA-WNN/videos/V01/` a una ubicación externa, por ejemplo `X:/Alexander_Archivo/AAAA-WNN/V01/`. Mantener estructura relativa. En Windows puede hacerse con el Explorador de archivos; **copiar**, nunca cortar y pegar en el primer paso.
3. **A3 / verificación:** ejecutar `python scripts/gestion_archivo.py verificar AAAA-WNN V01 --destino "X:/Alexander_Archivo/AAAA-WNN/V01"`. Debe encontrar todos los elementos inventariados, con mismo tamaño y SHA-256. Si falla, no eliminar nada. Repetir con una segunda copia de seguridad independiente cuando el material sea irremplazable.
4. **A4 / registrar:** tras verificación, `python scripts/gestion_archivo.py marcar-offline AAAA-WNN V01 --confirmo-archivo` registra `ARCHIVADO_OFFLINE` en `ARCHIVO.json` y `registro/ARCHIVOS.csv`. **El comando no elimina archivos locales.** Requiere copia verificada previa.
5. **A5 / limpieza humana:** Alexander elimina manualmente *solo* las carpetas pesadas archivadas (`media/`, `preview/`, `delivery/`, `hyperframes/`, etc.) después de comprobar que puede abrir el disco externo. Conservar en local `BRIEF.md`, `SCRIPT.md`, `EDIT_PLAN.md`, revisiones, `PRUEBAS_Y_CLAIMS.md`, `PUBLICACION.md`, `ARCHIVO.json` y cualquier otro documento pequeño. No borrar toda la carpeta `V01`.

**Advertencias:** un disco externo o pendrive **no es una copia de seguridad si es el único ejemplar**. Usar al menos una segunda copia independiente para material importante. No archivar contraseñas, tokens ni información privada sin control de acceso/cifrado apropiado. Excluir material cuyo uso contractual no permita archivarlo.

## Ubicación sin rutas frágiles

No guardar como identificador permanente `E:\\` o `F:\\`: Windows puede cambiar la letra. Usar en manifiesto:

- `archive_id`: etiqueta reconocible del dispositivo o colección (por ejemplo `DISCO_A`). **El ejemplo no indica que exista o esté comprado.**
- `archive_relative_path`: como `2026-W46/V01`.
- `last_verified_utc`: último momento en que la copia se verificó físicamente.
- `files`: lista de archivos, bytes y SHA-256.
- `storage_status`: estado descrito anteriormente.

El directorio exacto se resuelve cuando el disco esté conectado. El agente no debe intentar abrir automáticamente una unidad desconectada ni inventar su ruta.

## Restauración y reedición

1. Consultar `registro/ARCHIVOS.csv` y `ARCHIVO.json`. Identificar el soporte por `archive_id` y la ruta relativa.
2. Conectar el soporte y copiar la carpeta archivada a su ruta original `semanas/AAAA-WNN/videos/V01/`, **sin sobrescribir** documentos locales más recientes.
3. Ejecutar `python scripts/gestion_archivo.py verificar AAAA-WNN V01 --destino "RUTA_DE_LA_COPIA_RESTAURADA"` si esa carpeta restaurada conserva todos los medios del manifiesto; si solo se restaura un subconjunto, documentar ese alcance y verificar las huellas de esos archivos manualmente.
4. Reparar en HyperFrames referencias absolutas a recursos que cambiaron de ubicación; usar rutas relativas al proyecto donde sea posible. Probar previsualización y exportación antes de modificar el montaje.
5. Registrar `RESTAURADO_TEMPORAL` en `ARCHIVO.json` y `registro/ARCHIVOS.csv` mediante actualización documental expresa. No sobrescribir el master publicado; para reedición crear una nueva versión, registrar motivo y mantener el enlace de la publicación original.
6. Tras completar los cambios, archivar la nueva versión con un manifiesto independiente o actualizar el inventario bajo control de versiones. Nunca sustituir silenciosamente la copia histórica.

## Comportamiento obligatorio de Cowork / Work / ChatGPT Web / Claude Code

- Para **ideas, estrategia y análisis histórico**: leer el histórico documental, métricas y URLs reales. **No es obligatorio recuperar vídeos antiguos.**
- Para **volver a usar una animación ya archivada**: consultar su localización; solicitar restauración o generar una nueva pieza claramente identificada como nueva. No afirmar que se ha inspeccionado el proyecto offline.
- Para **comparación visual o reedición**: si no se han restaurado los medios, responder `BLOQUEADO_POR_MEDIA_OFFLINE` e indicar archivos y `archive_id`; no improvisar su contenido.
- Si las métricas o textos históricos bastan, continuar aunque las carpetas pesadas falten.
- En **ChatGPT Web**, adjuntar explícitamente los documentos ligeros relevantes si no están cargados en el proyecto. Cowork/Work pueden leer carpetas concedidas por el usuario, pero no acceden por arte de magia a un disco desconectado.
- Un archivo faltante en `media/` de un episodio marcado `ARCHIVADO_OFFLINE` **no debe provocar fallo del control de integridad de la documentación**. Si el episodio está `LOCAL_ACTIVO`, investigar ausencia inesperada.

## Prueba de aceptación antes del primer archivo real

Crear una semana de prueba y un V01 ficticio con dos archivos de pocos bytes. Generar manifiesto, copiar, verificar, registrar offline y retirar solo los archivos ficticios locales. Iniciar otra semana y consultar su histórico. Debe ser posible trabajar con documentos antiguos y sin el disco conectado. Después restaurar la prueba y verificar hashes. **No usar primero originales importantes.**

## Próxima acción no automática

Este procedimiento está redactado, pero no traslada ningún episodio real ni autoriza borrar medios. La primera operación efectiva de archivado requiere aprobación humana explícita.

## Proyectos de editor final v3.4
Archivar junto al vídeo el proyecto nativo de CapCut/Shotcut y **todas las fuentes que referencia**. Guardar manifest con editor/versión, rutas relativas cuando el formato lo permita y estado de restauración. La copia del `.mp4` final sola **no** permite reabrir la edición por pistas ni modificar animaciones de HyperFrames. Tras desconectar almacenamiento externo, el agente debe seguir usando guiones y decisiones, pero indicar que la reedición exige restaurar los archivos referenciados.

## Ampliación de inventario v3.5
El script de archivo ahora incluye expresamente `media/`, `exports/`, `montaje_final/`, `hyperframes/`, `src/`, `preview/`, `delivery/` y `grabaciones_originales/` cuando existan. **Los expedientes `SCRIPT.md`, `PRUEBAS_Y_CLAIMS.md`, `INGESTA.md`, `LICENCIAS_MEDIOS.md`, `MONTAJE_FINAL.md`, `QC_MASTER.md`, `PUBLICACION.md` y manifiestos viven en la raíz de cada vídeo y no deben eliminarse al retirar los medios**. Seguir prohibición de borrados automáticos.
