---
name: edicion
description: Edita un vídeo del marco de principio a fin con el estándar de VID-0002 v06 y VID-0003 v04 (corte en silencios medidos, voz mejorada, recorte del 4K, B-roll a tiempo, demo de la app real, motion flotante, música por compases con tres picos, efectos reales, dos másteres y revisión). Usar cuando Ale deja la grabación en media/originales y pide editar, corregir o repetir una edición.
argument-hint: <VID-NNNN> [qué cambiar]
---

# /edicion — editar un vídeo con el estándar del marco

Edita: $ARGUMENTS

Esta skill recoge todo lo aprendido editando VID-0002 (v01–v06f) y VID-0003 (v01–v04) entre el 2026-11-17 y el 2026-11-20, incluidas **todas las correcciones de Ale**. Si otra sesión edita sin seguirla, el resultado sale «poco pulido» (transiciones, volúmenes, tarjetas y efectos): por eso los valores están escritos aquí y en [referencia.md](referencia.md), no en la memoria de una sesión.

**Base canónica:** `videos/VID-0003/hyperframes/edicion/` (edición v04 aprobada por Ale). Un vídeo nuevo **copia esa carpeta** y cambia solo los datos (tiempos, palabras, recursos, música, acciones de la demo y textos). No se reescriben los componentes ni las curvas: si algo falla, se corrige en la base y se anota en [errores.md](errores.md).

Antes de nada lee: la **dirección v2 de motion** ([MOTION §10](../../../guias/MOTION.md): tres niveles de texto, vocabulario de entradas y salidas, tarjetas vivas y auditoría de dinamismo), [referencia.md](referencia.md) (valores exactos), [errores.md](errores.md) (lo que ya salió mal y no se repite) y [revision.md](revision.md) (cómo se revisa antes de entregar).

---

## 0. Antes de empezar

1. `python scripts/marco.py estado` y lee GUION, GUION_BEATS (si hay), PRODUCCION del vídeo y [EDICION](../../../guias/EDICION.md) (Música, B-roll, Demo de la app real, Color).
2. Comprueba el OK-2 con `python scripts/marco.py huellas <VID>`. Si no está vigente, se puede editar como ensayo, pero avisa.
3. Plan con `update_plan`. Rutas largas y nombres con espacios o paréntesis: entre comillas (`"1119 (2)(1).mp4"`). En Git Bash, `cd` en un comando compuesto puede fallar: usa rutas absolutas.
4. Herramientas (no se instala nada): ffmpeg, `npx --yes hyperframes@0.9.42` con `HYPERFRAMES_NO_TELEMETRY=1 DO_NOT_TRACK=1`, Parakeet (`~/.cache/hyperframes/parakeet`), Chrome de HyperFrames (`~/.cache/hyperframes/chrome/chrome-headless-shell/...`) y `puppeteer-core` del caché de npx (`%LOCALAPPDATA%/npm-cache/_npx/<hash>/node_modules`). Si falta Parakeet o el Chrome, pide a Ale permiso para instalarlo (`hyperframes models install parakeet`).

## 1. Copiar la base

```
videos/<VID>/hyperframes/edicion/   ← copia de videos/VID-0003/hyperframes/edicion/ (sin assets/*.mp4 ni palabras.js)
videos/<VID>/media/originales/      ← toma de cámara, voz mejorada, broll/ (con fuentes.txt)
videos/<VID>/media/trabajo/         ← transcript.json, voz.wav, musica.wav, demo_real/, revision/, másteres
videos/<VID>/media/descartado/
```

Los medios no van a Git. `MEDIOS.csv` se completa **añadiendo filas** (ruta, bytes, sha256) de lo nuevo; no ejecutes `marco.py medios` si la copia de `media/` no está completa en esta computadora.

## 2. Medios y audio

1. `ffprobe` de cada original: resolución, fps, rotación (`stream_side_data=rotation`), duración.
2. **La voz es la voz mejorada de Ale** si la deja (`audio-mejorada.wav`); el audio de la cámara **nunca** se usa (va en silencio). Mide el desfase por correlación de la envolvente (1 kHz, ±300 ms) y afínalo a 8 kHz: en VID-0003 el WAV iba **25 ms por detrás** (`VOZ_RETRASO = 0.025`). Sin alinear, los labios no coinciden.
3. Transcribe el WAV alineado a 16 kHz mono con Parakeet: `npx hyperframes@0.9.42 transcribe voz16k.wav --engine parakeet --json` → `media/trabajo/transcript.json`. Parakeet acierta los tiempos pero no siempre el texto: corrige marcas y palabras (`ARREGLOS` en `preparar.py`: «dice»→«hice», «que»→«qué», «tú.»→«tú?»…). Además **adelanta la primera palabra de cada frase**: `palabras()` la lleva al final del silencio medido.
4. **Si la voz grabada no coincide con el GUION** (Ale graba con sus palabras), actualiza la voz literal, sube `Version`, avisa de que el OK-2 caduca y, si el validador da error, `marco.py mover <VID> BORRADOR` hasta que Ale lo renueve.

## 3. Corte (`preparar.py → KEEP`)

- Mide silencios en ventanas de 10 ms (< −55 dB; con −60 dB para confirmar). **Cada corte cae dentro de un silencio real**, nunca a mitad de palabra (VID-0002: «te pasaste de recorte»).
- Deja **0,30–0,50 s** de respiración entre frases, **≈ 0,6 s** antes de una revelación sin voz (el plan) y **1 s de toma real** después de la última palabra (no un fotograma congelado si hay toma).
- Quita las pausas largas; las cortas (< 0,5 s) se dejan: cada corte es un salto visible.
- En la composición, los saltos a cámara se tapan con un **cambio de escala** (1,0 ↔ 1,07–1,10) en el empalme, o caen dentro de un recurso o de la demo.

## 4. Encuadre y color

- **4K vertical → recorte 1,5–1,6×** (VID-0003: `CROP = (1350, 2400, 425, 1220)`): cabeza en el tercio superior, fuera el softbox y el zócalo; deja margen para acercamientos hasta 1,25×. Se mide sobre fotogramas con cuadrícula. Un solo paso de codificación desde el original (CRF 10).
- **Color: por defecto, sin filtro** (Ale, 2026-11-20). El look B y el «natural» quedan como referencia en `preparar.py` (`LOOK_B`, `LOOK_NATURAL`); solo se usan si Ale lo pide, y antes se **mide** la toma (pared, piel, negros) y se enseña una comparación de fotogramas (original · propuesta). Nunca viñeta ni suavizado de piel por defecto.

## 5. Música (`SEG`)

- Pista del banco de Ale (Pixabay; Content ID por confirmar). Golpes con `npx hyperframes@0.9.42 beats <pista>` (guardados en `beats_<pista>.json`); a 145 BPM, 0,414 s por golpe y compás de 4.
- **Tres picos, uno por tercio**, cada uno con golpe de música, corte o acercamiento y palabra protagonista. La música se monta por tramos de la pista (intro → batería → relleno → estribillo → valle → subida → estribillo 2 → silencio → golpe final) para que los picos caigan donde manda la voz. **La voz nunca se mueve.** Empalmes en golpes, con fundidos de 8 ms (120 ms el primero).
- Antes del pico final: **silencio de la música de 0,4–0,5 s** y golpe en la palabra; final en seco en un golpe.

## 6. Recursos (B-roll)

- Entran y salen **en golpes** de la música (`BROLL`: tn inicio, fin, entrada en el clip, modo).
- Un recurso que **cuenta** algo dura **≈ 1,6–2 s** y cubre la frase; una **lista** puede ir a ≈ 1,2 s por elemento.
- Modos: `full` (vertical o 4K horizontal recortado a 1080×1920) y `over` (horizontal en 1080: tarjeta cuadrada de 400 px en el pecho, **sin tapar la boca**, la cara sigue a la vista). La primera frase del vídeo, si lleva recurso, siempre `over`.
- Enlace de cada recurso en `media/originales/broll/fuentes.txt` (Derechos).

## 7. Demo de la app real (`demo/grabar.mjs`)

- La app de staging, en un iPhone de 393×852 pt a 1080×2342, tema claro, fotograma a fotograma con las animaciones ralentizadas. Detalles técnicos en [EDICION → Demo de la app real](../../../guias/EDICION.md#demo-de-la-app-real).
- `ACCIONES` en el tiempo del corte: cada toque y tecleo **cuando la voz lo dice** (el plan aparece en el silencio antes del pico 2). Si la app depende del mes, fija la fecha de publicación (`FECHA`).
- Variables: `NPXNM` (node_modules del caché de npx con `puppeteer-core`) y `CHROME` (chrome-headless-shell). Después: `ffmpeg -framerate 30 -i toma/f%05d.jpg … tpad=stop_mode=clone:stop_duration=0.8` → `assets/demo_real.mp4`.
- Demo de **≈ 12 s en tres momentos**; `FRAMES` (encuadres) siguen la voz; dos o tres a todo el ancho (escala 0,98–1,0).

## 8. Composición (`index.html`)

Todo es función del tiempo (`render(t)`, t = tiempo del corte, leído de `palabras.js`). Se cambian **solo datos**: `NODES` (show, textos), `ARROWS` (máx. 3), `FRAMES`, `ZP` y `SHOTS`, tiempos de protagonistas, promesa y acento. Valores en [referencia.md](referencia.md). Reglas que no se tocan:

- Cara a pantalla completa; el celular de la demo nace del teléfono flotante y vuelve a él; la cara detrás se desenfoca (18 px) y oscurece al 50 %.
- **Texto en tres niveles** (MOTION §10.2): frase en minúsculas palabra a palabra (a cámara 1035, con tarjeta 1430, en la demo 1440 y en caja), clave grande en degradado Señal con su entrada, y palabra escenario detrás de la persona. **Nunca dos frases en una línea**; la frase se apaga donde hay un tratamiento grande. Todo texto sobre imagen lleva `--sombra`.
- **Tratamientos**: cada bloque tiene su entrada y su salida del vocabulario (MOTION §10.3, laboratorio §10.9), nunca el mismo par dos veces seguidas. Color: solo la paleta Señal de cerobytes (AV-014); los colores de un producto, solo dentro del celular. Sin resplandor mientras AV-013 siga sin decidir. Si Ale hace un gesto (manos que se abren), la palabra **nace del gesto**: se mide la apertura fotograma a fotograma y se usa como máscara (`REV`).
- **Deriva de cámara** 100 → 103 % por plano, que **solo se reinicia en cortes reales** (`SHOTS`).
- Las flechas **nunca sobreviven a sus tarjetas** (`showEnd`). Nada de anillos de toque ni dedos simulados.
- Textos fijos (promesa, acento) **por debajo de la barra superior de las apps** (≥ 168 px) y nada importante por debajo de ≈ 1540 px ni en los 120 px de la derecha.
- **Sin apertura en frío**: el vídeo empieza con la voz y con la cara (acercamiento 1,12 → 1,0 en 0,45 s).

## 9. Mezcla (`mezcla.py`)

`python mezcla.py <imagen.mp4> <base>` → `<base>.mp4` (con música), `<base>_sin_musica.mp4` y `<base>_mezcla.json`. Receta y niveles en [referencia.md](referencia.md#sonido). **Pocos efectos y reales** (banco de Pixabay de Ale, nunca sintetizados): uno por tarjeta, los toques importantes de la demo (≈ 4), tecleo, y los tres golpes. Los cortes de recursos no llevan efecto. Mide la sonoridad momentánea en los picos: si un pico sin voz queda a −20 LUFS, sube la música ahí (`SUBE`).

## 10. Render, revisión y entrega

1. `npx hyperframes@0.9.42 lint .` (0 errores) y `snapshot --at …` en **cada momento cambiado** antes del render completo.
2. `npx hyperframes@0.9.42 render . -q delivery --quiet -o ../../media/trabajo/edicion_vNN_imagen.mp4` (en segundo plano; tarda minutos, no tokens) y después `mezcla.py`.
3. Revisión de [revision.md](revision.md): hoja a 2 fps, momentos clave, sonoridad por momentos, primer y último fotograma.
4. Registro: PRODUCCION → Historial (versión, qué cambió, LUFS, pico), `Siguiente_paso`, filas nuevas en MEDIOS.csv, `marco.py validar` y pruebas. Cada entrega es una versión nueva (`edicion_vNN`), nunca se sobrescribe la anterior.
5. Entrega con `SendUserFile` y un resumen: qué cambió, qué no se pudo comprobar («mezcla medida, no escuchada por Claude») y qué decide Ale.
6. Si Ale pide autocrítica: lista priorizada, separando lo que se arregla en edición de lo que depende de la grabación o de la app (ver [revision.md](revision.md#autocrítica)).

## Lo que decide Ale

Aprobaciones (OK-2 con su frase literal), publicar, gastar, instalar programas o modelos, el lema y los textos de marca (p. ej. el acento final), el color o look, borrar medios (las tomas de prueba se dejan y se le dice dónde están) y commitear o subir (solo cuando lo pide).
