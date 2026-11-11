# Auditoría final y correspondencia con flujos de producción reales
**Fecha:** 2026-11-06 · **Versión auditada:** v3.4 → corregida v3.5. Auditoría de documentos y scripts; NO certificación SMPTE/EBU, no revisión real de un episodio terminado.

## Hallazgos reproducibles del paquete anterior
| Prioridad | Observación v3.4 | Corrección v3.5 | Evidencia de verificación |
|---|---|---|---|
| Alta | IDs **P13/P14 duplicados** en `09_PROMPTS_MAESTROS.md` para tareas distintas | P00–P18 únicos; P15/P16 editor final; P17 ingesta; P18 handoff | script verifica unicidad |
| Alta | `SOP`/prompts requerían `SCRIPT.md`, `PRUEBAS_Y_CLAIMS.md`, `TAKES.md` pero el generador no los creaba | Plantillas explícitas y generador ampliado | prueba de `crear_semana.py` |
| Alta | Archivo excluía `exports/`, `montaje_final/` y `grabaciones_originales/` del inventario | `gestion_archivo.py` actualizado y prueba simulada de hash | prueba inventario/verificación offline |
| Media | Guía operativa v3.1 obsoleta dentro de v3.4 y sección repetida | Guía alineada a v3.5 con ruta única; nueva lectura rápida `16` | revisión documental |
| Media | QC del paquete solo comprobaba presencia de documentos | SHA del manifiesto + `inspeccionar_video.py` para ffprobe y checklist `QC_MASTER.md` | integridad y pruebas positivas/negativas |
| Alta | No se formalizaba la ingestión de **originales Samsung**, con riesgo de compresión de WhatsApp | Nueva `INGESTA.md`, separación original/proxy y trazabilidad de perfil de grabación | prueba de estructura y registro |
| Media | `picture lock` y acabado en CapCut no tenían punto de control separado | Gates G7, G7.5, G8 y criterio explícito de no recomprimir versiones | SOP revisado |
| Media | Licencias, voz, subtítulos, color y encuadre dependían de instrucciones generales | `LICENCIAS_MEDIOS.md` + `QC_MASTER.md` + `18` | checklist por entrega |

## Correspondencia con prácticas documentadas (no normas obligatorias)
| Práctica del sector | Aplicación adaptada a Alexander | Fuente pública |
|---|---|---|
| **Media ingest / preparation** | Se copian archivos cámara originales, se comprueba hash y metadatos, audio y proxies cuando haga falta | Frame.io Workflow Guide, Prep — https://workflow.frame.io/chapters |
| **Rough cut → picture lock** | Previews por escenas, revisión timecoded, bloqueo de decisiones de montaje antes del acabado | Frame.io, Editing Stages — https://workflow.frame.io/guide/editing-stages |
| **Conform/online finishing** | Se vuelve a originales y se crea master desde fuentes íntegras, no desde proxy; se revisa cambio de editor | Frame.io, Workflow Guide — https://workflow.frame.io/guide |
| **Naming/version control** | ID de semana/vídeo + vNN, no sobrescribir `master_final` publicado sin nueva versión | Frame.io, File Naming — https://workflow.frame.io/guide/file-naming |
| **Checksums/backups** | SHA-256 del inventario/copia externa, copia independiente; el histórico documental permanece local | Frame.io, Checksums and Robust Backups — https://workflow.frame.io/guide/checksums-backups |
| **Distribución YouTube** | MP4 H.264, AAC 48 kHz, color SDR Rec.709, frame rate deliberado y bitrate 8 Mbps 1080p/30 como referencia, no dogma para otras plataformas | https://support.google.com/youtube/answer/1722171 |
| **Vertical mobile TikTok** | 9:16, 1080x1920, texto legible en área que no cubra UI, gancho temprano y valor antes de efectos | TikTok for Business — https://ads.tiktok.com/business/es/guides/video-advertising-guide |
| **Proxies en hardware limitado** | Solo copia para montar; utilizar original en export cuando el editor permita relink o realizar conform previo | Adobe, Proxy workflow — https://helpx.adobe.com/es/premiere/desktop/organize-media/ingest-proxy-workflow/ingest-and-proxy-workflow.html |

## Límites de la auditoría
1. No se ha comprobado exportación de CapCut/Shotcut **en el PC de Alexander** ni alfa en su versión concreta. El usuario informa que la prueba directa del original Samsung conservó mejor calidad que la copia enviada por WhatsApp.
2. No se ha producido un vídeo de 45–60 s con voz, música y animaciones reales dentro del SOP. La prueba HyperFrames de 8 s no valida el proceso completo.
3. No hay identidad audiovisual personal, alias, primera miniapp ni promesa editorial aprobados. No se rellenaron datos inventados.
4. Los requisitos por plataforma pueden cambiar; no equiparar guías publicitarias de TikTok con una obligación orgánica ni confirmar soportes de portada sin ver interfaz.
5. Estos gates son una **adaptación operativa**, no afirmación de cumplimiento de una norma industrial certificable. El objetivo es un flujo coherente, eficiente y verificable para una sola persona.

## Criterio de aceptación interno de v3.5
- ZIP íntegro y fotos originales presentes.
- IDs de prompts únicos, paths requeridos existentes.
- Crear semana 0 o N, modelos completos y plantilla de retrospectiva, sin otorgar permisos implícitos.
- Archivo externo prueba hash correcto, da error para archivo corrupto y no borra originales.
- ffprobe distingue original/piloto no publicable de master con audio esperado.
- No se cambian estados de identidad o producción sin aprobación del propietario.
