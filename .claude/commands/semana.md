---
description: Prepara el lote de la semana listo para el OK-1
argument-hint: [semana, p. ej. actual o 2026-W47] [horas disponibles]
---
Prepara la semana: $ARGUMENTS

1. Ejecuta `python scripts/marco.py estado`. Si la semana no existe, créala con `python scripts/marco.py semana <semana> --horas <h>`.
2. Pregunta a Ale las horas netas solo si no las ha dado.
3. Elige 2–4 ideas de `registro/IDEAS.csv` según EDITORIAL (puntuación, dependencia, capacidad) y rellena el Lote con horas estimadas y motivo.
4. Propón **una** hipótesis con una sola variable.
5. Ejecuta `python scripts/marco.py validar` y pide a Ale el OK-1. Regístralo solo cuando lo diga: `python scripts/marco.py aprobar OK-1 <semana> --evidencia "Ale en chat, <fecha>: «…»"`.
