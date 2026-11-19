---
description: Prepara la sesión de grabación de un vídeo aprobado
argument-hint: <VID-NNNN>
---
Prepara el rodaje de: $ARGUMENTS

1. Comprueba con `python scripts/marco.py huellas <VID>` que el OK-2 está vigente. Si no, detente y avisa.
2. Lee el GUION y `guias/SET.md` / `guias/TECNICA.md`.
3. Rellena PRODUCCION → Rodaje: una fila por toma (escena, qué grabar, cámara o pantalla), agrupadas para grabar seguidas, y la ficha del set con los ajustes de partida.
   - **Recursos propios:** una fila por cada `R01…` de «Recursos que grabar» del GUION, después de las tomas a cámara. Para cada uno: qué se ve, encuadre (cerrado, de detalle), 2 versiones de 3–5 s, cámara quieta en trípode o un movimiento lento, misma luz del set y nada personal en pantalla. Se graban en 4K/30, igual que la cámara.
4. Lista corta de comprobaciones previas: HDR desactivado, 4K/30, prueba del DJI escuchada, datos de ejemplo listos en la demo, sin datos personales en pantalla, objetos de los recursos preparados.
5. `python scripts/marco.py mover <VID> EN_PRODUCCION --siguiente "Ale: grabar tomas T1–Tn"`.
6. Cuando Ale tenga los archivos, ingesta: inspecciona cada original con `python scripts/marco.py inspeccionar <archivo> --perfil ingesta`, rellena Ingesta y ejecuta `python scripts/marco.py medios <VID>`.
