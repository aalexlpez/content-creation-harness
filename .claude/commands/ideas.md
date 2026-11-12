---
description: Propone y puntúa ideas de vídeo y añade las elegidas
argument-hint: [tema, proyecto o fuente]
---
Propón ideas de vídeo sobre: $ARGUMENTS

1. Ejecuta `python scripts/marco.py estado` y lee `guias/EDITORIAL.md` y las fichas de `proyectos/`.
2. Propón hasta 6 ideas. Para cada una: proyecto, título, pilar, formato, problema, prueba visual disponible **hoy** y procedencia (comentario, problema propio, estado del proyecto…).
3. Puntúa cada idea con los cinco criterios 0–2 de EDITORIAL y descarta las que dependan de una demo que no existe (salvo como proceso).
4. Presenta una tabla ordenada por puntuación con tu recomendación.
5. Cuando Ale elija, añádelas con `python scripts/marco.py idea <proyecto> "<título>" --problema … --pilar … --formato … --procedencia … --prueba …` y anota la puntuación en `registro/IDEAS.csv`.
