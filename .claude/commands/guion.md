---
description: Redacta guion y dirección de montaje de un vídeo
argument-hint: <I-NNNN o VID-NNNN> [notas]
---
Escribe el guion para: $ARGUMENTS

1. Si recibes una idea (I-NNNN) sin vídeo, crea el expediente con `python scripts/marco.py video <idea>` (añade `--ensayo` si Ale dice que es una prueba).
2. Lee `guias/GUIONES.md`, `guias/EDICION.md`, la ficha del proyecto y la fila de la idea.
3. Rellena en `videos/VID-NNNN/GUION.md`: Brief completo, dos ganchos puntuados, tabla de Escenas con voz literal y montaje (texto exacto, corte, sonido, toma) y tabla de Claims. Nada de demos ni datos inventados.
4. Actualiza `Siguiente_paso` en PRODUCCION ("Ale: leer en voz alta y aprobar OK-2") y ejecuta `python scripts/marco.py validar`.
5. Entrega a Ale un resumen: gancho elegido, duración estimada, qué hay que grabar y qué falta acreditar.
6. Cuando Ale diga OK-2, regístralo con `python scripts/marco.py aprobar OK-2 VID-NNNN --evidencia "Ale en chat, <fecha>: «…»"`.
