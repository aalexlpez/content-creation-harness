# Flujo de trabajo

De la idea al dato. Tres aprobaciones humanas, un expediente por vídeo y un CLI que hace el papeleo.

## El ciclo

```
idea ──► semana (OK-1) ──► guion (OK-2) ──► rodaje y montaje ──► máster (OK-3) ──► publicación ──► métricas ──► retrospectiva
```

| Paso | Quién | Comando o documento |
|---|---|---|
| 1. Ideas | Claude propone, Ale elige | `marco.py idea …` → `registro/IDEAS.csv` |
| 2. Lote semanal | Claude prepara, Ale aprueba (**OK-1**) | `marco.py semana actual` → `SEMANA.md` · `marco.py aprobar OK-1 2026-W46 …` |
| 3. Expediente | Claude | `marco.py video I-0001` → `videos/VID-NNNN/` |
| 4. Guion y montaje | Claude redacta, Ale lee en voz alta y aprueba (**OK-2**) | `GUION.md` · `marco.py aprobar OK-2 VID-0001 …` |
| 5. Rodaje e ingesta | Ale graba; Claude prepara tomas y comprueba archivos | `PRODUCCION.md` · `marco.py inspeccionar …` |
| 6. Animación y montaje | Claude (HyperFrames) y Ale (CapCut/Shotcut) | `PRODUCCION.md` |
| 7. Máster y QC | Ale revisa en el móvil y aprueba (**OK-3**) | `CIERRE.md` · `marco.py aprobar OK-3 VID-0001 --master media/entregas/…` |
| 8. Publicación | Ale publica; Claude registra la URL | `CIERRE.md` → Publicaciones · `marco.py mover VID-0001 PUBLICADO` |
| 8b. Post en X | Claude redacta; Ale publica después del vídeo enlazado | `CIERRE.md` → Plan y Publicaciones (ver [Posts en X](#posts-en-x)) |
| 9. Métricas | Ale aporta datos; Claude los registra | `registro/METRICAS.csv` a +48h y +7d |
| 10. Retrospectiva | Ambos | `SEMANA.md` → Retrospectiva |

Para **probar el flujo sin publicar**, crea el vídeo con `--ensayo`: no necesita OK-1 y el validador impide publicarlo.

## Aprobaciones

Cada aprobación guarda quién, cuándo, la evidencia (por ejemplo, el mensaje de chat) y una **huella** SHA-256 de lo aprobado. Si el contenido cambia después, la huella deja de coincidir y la aprobación **caduca**. Así nadie, ni persona ni agente, cambia un guion aprobado sin que se note.

| Puerta | Qué cubre | Requisitos para registrarla |
|---|---|---|
| OK-1 | Control (horas, hipótesis) y lote de la semana (idea, horas, motivo) | Horas numéricas, hipótesis y al menos una idea registrada |
| OK-2 | Control, brief, ganchos, escenas y claims del guion | Brief completo, escenas y claims con filas, ningún claim X, OK-1 vigente (salvo ENSAYO) |
| OK-3 | Máster exacto (bytes), derechos, QC, plan de publicación y OK-2 vigente | QC completo en CONFORME, al menos una fila de derechos y un plan (salvo ENSAYO) |

- Registra la aprobación con `marco.py aprobar`. Nunca se escribe a mano.
- Añadir el `video_id` a una fila del lote no caduca el OK-1. Añadir o quitar ideas, sí.
- Las notas de revisión, el rodaje, el montaje, las publicaciones y el aprendizaje no forman parte de ninguna huella: se pueden editar libremente.
- Para ver si siguen vigentes: `marco.py huellas VID-0001` o `marco.py estado`.

## Estados de un vídeo

El estado vive en `PRODUCCION.md → Control → Estado`. Cámbialo con `marco.py mover`, que se niega si faltan requisitos.

| Estado | Significa | Requisito |
|---|---|---|
| BORRADOR | Guion en preparación | — |
| GUION_APROBADO | Guion cerrado, listo para rodar | OK-2 vigente (`aprobar OK-2` lo pone solo) |
| EN_PRODUCCION | Grabando, animando o montando | OK-2 vigente |
| LISTO | Máster aprobado, pendiente de publicar | OK-2 y OK-3 vigentes (`aprobar OK-3` lo pone solo) |
| PUBLICADO | Al menos una red publicada | OK-3 registrado, URL real, cuenta VERIFICADA y modo NORMAL |
| ANALIZADO | Métricas y aprendizaje registrados | Igual que PUBLICADO |
| BLOQUEADO | Parado por algo concreto | Motivo en `Bloqueo` (`--bloqueo "…"`) |
| CANCELADO | Descartado | — |

Mantén al día `Siguiente_paso` (`--siguiente "…"`). Es lo primero que se lee al retomar un vídeo en otra sesión o en otra herramienta.

## Cambios después de aprobar

- **Guion**: edita, sube `Version` a v02 y pide un nuevo OK-2. Si el vídeo estaba en GUION_APROBADO o EN_PRODUCCION, el validador marcará error hasta renovarlo, o hasta que lo devuelvas a BORRADOR.
- **Máster nuevo** (otra exportación): guárdalo con otra versión (`…_v02.mp4`), actualiza `Version_master` y vuelve a aprobar el OK-3 con `--master`. El historial de aprobaciones queda en `PRODUCCION.md → Historial`.
- **Republicar o añadir una red**: añade una fila nueva al plan (`VID-0001-IG-02`). Si el plan cambia antes de publicar, renueva el OK-3.
- **Reprogramar** un vídeo a otra semana: mueve la fila del lote a la semana nueva, cambia `Semana` en el GUION y anota el motivo en `Seguimiento` de las dos semanas. Una idea solo puede estar en un lote.

## Posts en X

En X **no se sube el vídeo**. Se publica un post propio que lleva al vídeo ya publicado en TikTok o Instagram (DIST-X-001).

| Paso | Qué se hace |
|---|---|
| Plan | Una fila `VID-NNNN-X-NN` con plataforma `X`. En la columna `archivo` va la publicación a la que enlaza (`VID-NNNN-TT-01` o `VID-NNNN-IG-01`), que tiene que estar en el mismo plan. En `copy, portada y notas`, el texto exacto del post |
| OK-3 | El post entra en la huella del plan como cualquier otra fila: si cambia su texto o su enlace, el OK-3 se renueva |
| Publicar | Ale publica primero el vídeo de destino y después el post, pegando la URL real de ese vídeo |
| Registrar | URL del post en Publicaciones, con una fecha igual o posterior a la del vídeo enlazado |
| Medir | Métricas del post en `METRICAS.csv` con la plataforma `X` (por ejemplo, clics en el enlace) |

El validador rechaza un post de X que apunte a un archivo de vídeo, a YouTube o Facebook, o a una publicación que no esté en el plan. También rechaza que se registre como publicado antes que su vídeo.

Cómo escribir el post:
- Es un texto para X, no la descripción de TikTok copiada. Una frase con la idea central del vídeo y el enlace.
- Sin hashtags de relleno. Como mucho uno, si de verdad sirve para encontrarlo.
- La cuenta es `@soycerobytes`. Al mencionar el vídeo, usa el identificador de la red de destino ([IDENTIDAD](../marca/IDENTIDAD.md)).
- Mismas reglas de claims que el guion: el post no promete nada que el vídeo no enseñe.

## Identificadores

| Elemento | Formato | Ejemplo |
|---|---|---|
| Idea | `I-NNNN` | I-0007 |
| Semana | ISO `AAAA-WNN` | 2026-W46 |
| Vídeo | `VID-NNNN` | VID-0003 |
| Publicación | `VID-NNNN-RED-NN` (red: YT, TT, IG, FB, X) | VID-0003-TT-01 |
| Proyecto | minúsculas con guiones | miminiapp |

Los IDs los asigna el CLI y no cambian aunque el vídeo cambie de semana.

## Medios y copias de seguridad

```
videos/VID-0001/
  GUION.md  PRODUCCION.md  CIERRE.md  MEDIOS.csv     ← en Git
  media/                                             ← fuera de Git
    originales/   copias intactas de cámara y micrófono
    trabajo/      proxies, capturas de pantalla, escenas animadas, audio
    montaje/      proyecto de CapCut o Shotcut y sus recursos
    entregas/     VID-0001_v01.mp4, portada, SRT
```

1. Tras la ingesta o al terminar: `marco.py medios VID-0001` escribe `MEDIOS.csv` (ruta, tamaño y SHA-256 de cada archivo).
2. Copia `media/` a un disco o nube y comprueba la copia: `marco.py medios VID-0001 --copia "E:/copias/VID-0001/media"`.
3. Antes de borrar nada del equipo, confirma que la copia está íntegra. Borrar es decisión de Ale.
4. Para restaurar, copia de vuelta a `media/` y ejecuta `marco.py medios VID-0001 --comprobar`.

El máster aprobado se identifica por su SHA-256 en `CIERRE.md`. En otro equipo sin los medios, el validador avisa pero no falla. Si el archivo está y no coincide, falla.

## Retomar el trabajo en otra sesión o herramienta

1. `git pull` y `python scripts/marco.py estado`.
2. Abre el vídeo, lee `Siguiente_paso`, `Bloqueo` y el `Historial`.
3. Trabaja y ejecuta `marco.py validar` antes de hacer commit.

Una sola persona o agente escribe en un expediente a la vez. Si dos sesiones tocan el mismo archivo, Git mostrará el conflicto al hacer pull: resuélvelo y valida.
