**Paso 0 anterior a B0:** mantener claramente separadas la marca personal de Alexander y la marca del producto MiMiniApp. Revisar `12_IDENTIDAD_PERSONAL_Y_HANDLES.md`. El alias se reservará solo si se comprueba disponibilidad real y queda aprobado; de lo contrario no bloquea planificación y los assets provisionales muestran «Alexander» sin @.

# Puesta en marcha real (sin compras automáticas)

## Fase B0: estrategia + identidad (una vez)
- [ ] Aprobar promesa editorial y audiencia principal en `registro/DECISIONES.md`.
- [ ] Revisar propuesta A de identidad en dos frames y aprobar/cambiar una sola vez.
- [ ] Crear `brand/IDENTIDAD_APROBADA.json` (hasta entonces **TEMP**).
- [ ] Generar `frame.md` solo tras B0; el script debe bloquear si falta firma de identidad.
- [ ] Aprobar tipos de guion y métricas.

## Fase P0: entorno (una vez)
- [ ] Elegir si el motor se usará vía HyperFrames Studio+Claude Code o Studio+Codex, con una sola cuenta de agente activa para la prueba.
- [ ] Consultar documentación oficial de versión instalada; no copiar comandos desactualizados sin comprobación.
- [ ] Configurar Node/FFmpeg y skills oficiales con consentimiento.
- [ ] Mantener repo audiovisual separado de la web/product harness.
- [ ] Importar piloto existente solo como evidencia de QA, nunca como marca final.
- [ ] Hacer prueba de audio, UI-morph y render + coste. Registrar resultado real.

## Primera semana real
- [ ] Abrir semana con P01; registrar horas y estado del producto.
- [ ] Seleccionar y aprobar ideas (G1).
- [ ] Redactar, verificar claims y aprobar fichas/guiones (G2).
- [ ] Validar demo y grabaciones necesarias (G3/G4).
- [ ] Elaborar y aprobar EDIT_PLAN (G5).
- [ ] Preview → revisión focalizada → master/portada → publicar tras autorización (G6–G8).
- [ ] Registrar métricas en ventanas acordadas y cerrar (G9).

## Nunca
- No ejecutar una prueba de producto con datos inventados presentados como reales.
- No publicar screenshots de terceros ni música ajena sin licencia.
- No cambiar tres hipótesis de edición por vídeo y declarar causa de viralidad.
- No fusionar decisiones audiovisuales en el harness web sin autorización de su proceso.

## Archivo audiovisual periódico (opcional, requiere autorización)
- [ ] Verificar que episodio, guion, QC, metadatos y URLs estén documentados.
- [ ] Generar `ARCHIVO.json` con rutas relativas y SHA-256.
- [ ] Copiar a disco externo sin eliminar original; verificar contenido y hashes.
- [ ] Si es irremplazable, conservar otra copia independiente: el pendrive único no es respaldo suficiente.
- [ ] Registrar ubicación lógica en `registro/ARCHIVOS.csv` y estado `ARCHIVADO_OFFLINE`.
- [ ] Limpiar manualmente solo medios pesados tras aceptación; mantener documentos de cada semana.
- [ ] Comprobar que se puede abrir semana nueva sin conectar disco antiguo.
Ver procedimiento detallado en `14_POLITICA_ARCHIVO_Y_RESTAURACION.md`.

## Nuevas verificaciones de v3.5
- [ ] Leer manual `16_GUIA_SEMANA_EN_15_MINUTOS.md` y auditoría `17_AUDITORIA_FINAL_ESTANDARES.md`.
- [ ] `scripts/crear_semana.py` genera SCRIPT/CLAIMS/INGESTA/TAKES/LICENCIAS/QC además de BRIEF/EDIT_PLAN.
- [ ] Importar archivo Samsung original, nunca descarga previa de WhatsApp. Registrar FPS/códec/color en INGESTA.
- [ ] Comprobar master con `scripts/inspeccionar_video.py`, registrar hash y revisión en móvil.
- [ ] Registro G7 picture lock separado del G7.5 de master QC; solo entonces G8.
