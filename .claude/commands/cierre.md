---
description: QC del máster, derechos, plan de publicación y copy
argument-hint: <VID-NNNN> [ruta del máster]
---
Cierra el vídeo: $ARGUMENTS

1. Inspecciona el máster con `python scripts/marco.py inspeccionar <ruta>` y anota el resultado en CIERRE → QC → Tecnico.
2. Repasa con Ale los campos Imagen, Audio, Textos y Movil (lo que solo puede ver él en el móvil) y completa Derechos con cada recurso usado.
3. Prepara el Plan de publicación: una fila por red (`VID-NNNN-YT-01`…), con copy adaptado a cada red, portada y notas. Añade el post de X (`VID-NNNN-X-01`), con la publicación de TikTok o Instagram a la que enlaza en `archivo` y el texto exacto del post (`guias/FLUJO.md` → Posts en X). Comprueba en `marca/CUENTAS.csv` qué cuentas están VERIFICADAS.
4. `python scripts/marco.py validar`. Cuando Ale diga OK-3: `python scripts/marco.py aprobar OK-3 <VID> --master <ruta relativa al vídeo> --evidencia "…"`.
5. Tras publicar, añade cada URL en Publicaciones y ejecuta `python scripts/marco.py mover <VID> PUBLICADO`. Recuerda a Ale que el post de X va después del vídeo enlazado y con su URL real.
