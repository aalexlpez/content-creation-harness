# Auditoría y jerarquía de evidencias

## Fuentes del proyecto (revisadas)
- `fuentes_proyecto/MiMiniApp_Inicio_Proyecto_Harness_IA_v1.2.md` (4 nov 2026): definición de producto y restricciones de publicación, 11–15 h semanales **incluyendo programación, QA, guion, grabación, edición y comunidad**; ~1 miniapp/semana es objetivo flexible, no garantía. Primera miniapp no seleccionada. Dominio y nombre provisionales.
- `fuentes_proyecto/guia_set_grabacion.md` (4 nov 2026): Samsung S24+, POCO F5, DJI 1 TX+RX, softbox PULUZ, reflector, trípode. No declarar adaptadores/modelos adicionales verificados.
- `referencias/ui_motion/`: los tres JPG 1000845575-77 muestran estados de una interfaz móvil de terceros. **SOLO movimiento/composición**: transformación de tarjeta, reordenación espacial, profundidad y continuidad. No son identidad, colores ni assets publicables. Tres fotogramas no revelan curva de animación exacta, audio o implementación.
- `referencias/tecnologia/`: seis capturas: rostro a cámara, rótulos técnicos, chapter cards, infografía hardware. No permiten verificar herramientas usadas por el creador original.
- `evidencia_tecnica/piloto_hyperframes_8s.mp4`: prueba real del propietario, 8 s, 1080x1920 60 fps, H.264, sin pista de audio; demo ficticia, no prueba de pipeline semanal.
- `documentos_base_v2/` se conserva vía referencia: el v2.0 anterior propuso técnicas y plantillas, pero **no aprobó una identidad final**.

## Fuentes externas primarias verificadas el 5 nov 2026
1. TikTok For Business, guía creativa: https://ads.tiktok.com/business/es/guides/what-is-ad-creative-guide — consistencia, problema, gancho y CTA. **Procede de publicidad**, no implica un rendimiento garantizado en publicación orgánica.
2. TikTok, creative best practices: https://ads.tiktok.com/resources/help/article/creative-best-practices?lang=es — promesa en primeros segundos y subtítulos. Misma cautela.
3. YouTube Help, Shorts discovery: https://support.google.com/youtube/answer/11914225?co=YOUTUBE._YTVideoType%3Dshorts&hl=en — señales de 'elige ver', tiempo y porcentaje visto.
4. YouTube Help, Shorts analytics: https://support.google.com/youtube/answer/12942217?co=YOUTUBE._YTVideoType%3Dshorts&hl=es — métricas, retención, comparaciones prudentes.
5. YouTube entrevista de Todd Sherman y Jenny Hoyos: https://blog.youtube/creator-and-artist-stories/youtube-shorts-deep-dive/ — caso de creadora (opinión/consejo, **no ley algorítmica**), gancho inicial, thumbnail branding.
6. Meta, Instagram Best Practices: https://about.fb.com/news/2024/10/best-practices-education-hub-creators-instagram/amp/ — panel profesional, recomendaciones por cuenta.
7. Meta, Trial Reels: https://about.fb.com/news/2024/12/trial-reels-try-content-non-followers-first-see-what-perfoms-best/ — test con no seguidores cuando función esté disponible.
8. Meta, Facebook original creators 2026: https://about.fb.com/news/2026/03/rewarding-original-creators-on-facebook/amp/ — importancia de contenido original.
9. HyperFrames GitHub README: https://github.com/heygen-com/hyperframes/blob/main/README.md — motor HTML/GSAP, skills, edición y render local.
10. HyperFrames skill oficial: https://github.com/heygen-com/hyperframes/blob/main/skills/hyperframes/SKILL.md — estructura editable, pistas, variables y validación; se debe leer en la versión instalada.
11. Anthropic Cowork Projects: https://support.claude.com/es/articles/14116274-organiza-tus-tareas-con-proyectos-en-claude-cowork — contexto y limitaciones entre Cowork y Code.
12. Anthropic Cowork: https://support.claude.com/es/articles/13345190-comienza-con-claude-cowork — trabajo multietapa y carpetas.
13. W3C WCAG 2.2 contrast: https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum — ratios 4,5:1 (texto normal), 3:1 (grande); se aplica como referencia de legibilidad, no como certificado para vídeo.

## Lo que NO permiten concluir esas fuentes
- No se ha probado que una duración, número de cortes o color cause viralidad.
- Los datos de anuncios no prueban que una fórmula sea óptima para cuentas nuevas orgánicas.
- No existe garantía de que Claude Cowork pueda editar el proyecto local de HyperFrames de forma automática en cualquier superficie/dispositivo.
- No existe evidencia propia de qué pilar, CTA, paleta o guion de MiMiniApp retendrá mejor.

## Política de evidencia para los contenidos
Toda afirmación factual en un guion se clasifica:
- `P` — propiedad de producto verificada con demo/captura/prueba y versión.
- `E` — fuente externa verificable + URL/fecha.
- `O` — opinión/perspectiva personal, expresada como tal.
- `H` — hipótesis/aspiración; no presentar como hecho.
- `X` — pendiente de comprobar: bloquea esa afirmación en publicación.

## Auditoría de estándares y transferencia v3.5 (2026-11-06)
Se contrastó el SOP con Frame.io (media prep, revisión, picture lock, acabado, checksum), YouTube (H.264/bitrate/audio/Rec.709), TikTok for Business (9:16/safe zones, sin extrapolar ads a orgánico) y Adobe (concepto proxies). Vías oficiales y límites están en `17_AUDITORIA_FINAL_ESTANDARES.md` y `18_INGESTA_COLOR_EXPORT_Y_QC.md`. El propietario comprobó que el original de su Samsung conserva mejor calidad que una copia transferida mediante WhatsApp; se actualizó el gate G4 sin inventar mediciones de sus dos archivos.
