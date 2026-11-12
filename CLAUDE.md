# Instrucciones para Claude

Este repositorio es el marco con el que **Alexander** (Ale) produce vídeos verticales cortos para YouTube Shorts, TikTok, Instagram Reels y Facebook, más posts en X que enlazan al vídeo de TikTok o Instagram, con ayuda de Claude. Ale dirige, graba, aprueba y publica. Claude propone, escribe, organiza, comprueba y prepara.

## Al empezar una sesión

1. Ejecuta `python scripts/marco.py estado`. Muestra ideas, semanas, vídeos, su estado y el siguiente paso.
2. Si la tarea es sobre un vídeo, lee sus tres documentos en `videos/VID-NNNN/` y la guía que toque.
3. Si no puedes ejecutar comandos (por ejemplo, en el chat sin acceso al equipo), trabaja sobre los archivos y dile a Ale qué comando debe ejecutar.

En Windows, si `python` no responde, usa `py -3`.

## Dónde vive cada cosa

| Qué | Dónde |
|---|---|
| Ciclo, estados, aprobaciones y medios | [guias/FLUJO.md](guias/FLUJO.md) |
| Promesa, audiencias, pilares, selección de ideas y métricas | [guias/EDITORIAL.md](guias/EDITORIAL.md) |
| Cómo escribir guion, ganchos, escenas y claims | [guias/GUIONES.md](guias/GUIONES.md) |
| Dirección de montaje: texto, música, color y movimiento | [guias/EDICION.md](guias/EDICION.md) |
| Perfil técnico, ingesta, edición, exportación y QC | [guias/TECNICA.md](guias/TECNICA.md) |
| Set de grabación (luz, cámara, micro) | [guias/SET.md](guias/SET.md) |
| Identidad, alias y cuentas | [marca/IDENTIDAD.md](marca/IDENTIDAD.md), `marca/CUENTAS.csv` |
| Proyectos que aparecen en los vídeos | `proyectos/<id>/PROYECTO.md` |
| Ideas, decisiones y métricas | `registro/IDEAS.csv`, [registro/DECISIONES.md](registro/DECISIONES.md), `registro/METRICAS.csv` |
| Lote semanal | `semanas/AAAA-WNN/SEMANA.md` |
| Un vídeo | `videos/VID-NNNN/` → `GUION.md`, `PRODUCCION.md`, `CIERRE.md` |

## Qué haces sin preguntar

- Proponer ideas, puntuarlas y añadirlas con `marco.py idea`.
- Crear semanas y expedientes cuando Ale lo pida (`marco.py semana`, `marco.py video`).
- Redactar y corregir brief, ganchos, escenas, claims, lista de tomas, copy y retrospectivas.
- Rellenar PRODUCCION y CIERRE con datos medidos (inspector, inventario de medios, tiempos que Ale te diga).
- Ejecutar `estado`, `validar`, `huellas`, `inspeccionar` y `medios`, y cambiar estados con `mover` cuando se cumplan los requisitos.
- Mejorar este marco (guías, plantillas, scripts) si Ale lo pide o si algo falla. Mantén las pruebas en verde.

Después de cambiar documentos, ejecuta `python scripts/marco.py validar`.

## Qué solo hace o decide Ale

- **Aprobaciones.** Registra OK-1, OK-2 u OK-3 solo cuando Ale lo diga explícitamente en la conversación actual ("OK-2 para VID-0003"). Usa `marco.py aprobar ... --evidencia "Ale en chat, AAAA-MM-DD: «texto literal»"`. Nunca deduzcas una aprobación de un "me gusta" o de silencio.
- **Publicar**, retirar o editar publicaciones en redes. Tú preparas el copy y el plan; Ale publica y te da la URL.
- **Gastar dinero**, instalar programas o activar pruebas de pago (CapCut Pro incluido).
- **Abrir material personal** (grabaciones, fotos, cuentas) que Ale no haya indicado expresamente.
- **Identidad pública**: alias, paleta, tipografías, logo o firma sonora definitivos. Mientras tanto se usa el perfil TEMP.
- **Borrar medios** u originales.

Si una tarea necesita algo de esta lista, prepara todo lo demás y pide exactamente lo que falta.

## Reglas de contenido

- **Nada inventado**: ni demos, ni resultados, ni métricas, ni URL, ni citas. Si algo no existe todavía, el vídeo lo cuenta como proceso.
- Cada afirmación verificable va a la tabla Claims con su tipo (P, E, O, H, X). Un claim X bloquea el OK-2.
- Una idea central y un CTA por vídeo. Dos ganchos como máximo y una reescritura.
- Con cada guion, entrega la dirección de montaje por escena (texto exacto en pantalla, corte, sonido, toma), siguiendo [GUIONES](guias/GUIONES.md) y [EDICION](guias/EDICION.md).
- Si cambias un guion ya aprobado, sube `Version` (v02…) y avisa a Ale de que el OK-2 tiene que renovarse.
- Los tiempos son estimaciones hasta que Ale lea el guion en voz alta o haya material.

## Reglas técnicas

- Los medios (vídeo, audio, proyectos del editor) viven en `videos/VID-NNNN/media/` y **no se suben a Git** (`.gitignore`). Su rastro va en `MEDIOS.csv` (`marco.py medios`).
- No edites a mano los campos `Huella`, `Master_sha256` ni las secciones OK-*: los escribe `marco.py aprobar`.
- Documentos en UTF-8. Tablas Markdown con el número de columnas de la cabecera; si un texto lleva `|`, escríbelo como `\|`.
- No cambies de nombre secciones (`## …`) ni campos (`- Clave:`) de las plantillas: los scripts los leen.
- El código usa solo la biblioteca estándar de Python 3.11+. Pruebas: `python -m unittest discover -s pruebas`.

## Forma de trabajar con Ale

Entrega borradores completos en lugar de preguntas sueltas; si hay una decisión de verdad, plantéala con una recomendación. Escribe en español, claro y sin relleno.

Atajos (en Claude Code son comandos `/`; en cualquier otro sitio, Ale puede pedirlos con esas palabras):

| Atajo | Qué hace |
|---|---|
| `/ideas <tema>` | Propone y puntúa hasta 6 ideas y añade las que Ale elija |
| `/semana` | Prepara el lote de la semana con horas y una hipótesis, listo para el OK-1 |
| `/guion <idea o VID>` | Crea el expediente si falta y redacta brief, ganchos, escenas, claims y montaje |
| `/rodaje <VID>` | Lista de tomas, ficha del set y comprobaciones antes de grabar |
| `/cierre <VID>` | QC del máster, derechos, plan de publicación y copy por red |
| `/retro` | Métricas registradas, retrospectiva de la semana y siguiente hipótesis |
