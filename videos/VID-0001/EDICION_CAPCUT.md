# VID-0001 · Hoja de edición en CapCut

Hoja para montar el ensayo a mano. Sale del [GUION](GUION.md) v02: si no coinciden, manda el guion. Los segundos de entrada y salida son del bruto `media/originales/VID_20261112_211711.mp4` y hay que afinarlos de oído.

## 1. Preparar el proyecto

- Proyecto nuevo con lienzo 9:16, 1080×1920 y 30 fps.
- Importa el bruto. No lo recortes fuera de CapCut.
- Para tener subtítulos de partida puedes importar `media/trabajo/T1_base.srt`, que es la transcripción automática del bruto entero. Su texto no está corregido, así que cuadra cada frase con la columna «voz literal».
- Antes de empezar, guarda el proyecto en `media/proyecto/`. Si CapCut no te deja elegir carpeta, apunta dónde lo guarda.

## 2. Cortes (8 piezas, unos 39 s)

| # | escena | entrada–salida en el bruto | voz | encuadre y corte |
|---|---|---|---|---|
| 1 | S01 | 75,2 → 78,7 | Llega febrero y abandonas tus metas. | Plano a cámara al 100 %. El vídeo empieza en seco |
| 2 | S02 | 78,7 → 83,3 | Calma, todavía no. Pero para mediados de enero… | Corte directo a la misma toma con escala 110 % |
| 3 | S03 | 111,3 → 114,9 | Soy cerobytes y creé un plan B… | Vuelta al 100 % |
| 4 | S04–S05 | 135,9 → 140,4 | Escribes tu propósito… te lleva un mes al futuro… | Solo se oye la voz: en imagen, la maqueta |
| 5 | S06 | 181,3 → 188,4 | Eliges lo que hizo rendirte… | Solo voz, sobre la maqueta |
| 6 | S07 | 241,4 → 246,2 | Al final te llevas un recordatorio… | Solo voz, sobre la maqueta |
| 7 | S08 | 250,9 → 258,7 | Lo mejor: es gratis… pruébalo en modo avión… | Vuelta a cámara |
| 8 | S09 | 274,0 → 276,8 | Arma tu plan B antes de que llegue febrero. | Cámara con el encuadre de S01. Termina en seco, sin tarjeta final |

Entre piezas deja huecos de 0 a 2 fotogramas, sin transiciones de CapCut. Si algún corte suena a golpe, ponle un fundido de audio de 1 o 2 fotogramas.

## 3. Firma de color (S01 → S02)

En la pieza 1 añade dos keyframes de Ajustar:

- **En «abandonas»:** saturación de 0 a −60 y temperatura de 0 a unos −30 (más frío), en 8 fotogramas.
- **Hasta el final de la pieza 1:** se mantiene así.

En la pieza 2, el color vuelve de golpe al decir «todavía no». Lo más fácil es que la pieza 2 empiece sin ajustes y, si «todavía no» cae unos fotogramas después del corte, partir ahí.

En el resto del vídeo no hay corrección, o solo un ajuste suave igual en todas las piezas de cámara.

## 4. Recursos que se hacen en CapCut

- **R2 · hoja de calendario (S01–S02):** va arriba a la izquierda, sin tapar la cabeza. Muestra «ENERO», pasa a «FEBRERO» al decir «febrero» y vuelve a «ENERO» al decir «todavía no». Puede ser un texto sobre una forma, con un keyframe o un cambio de texto.
- **R1 · maqueta (S04–S07):** un móvil sobre fondo `#0B1020` con cuatro pantallas. Para cada una puedes hacer una captura o imagen, o montarla con texto en CapCut. Pon el rótulo pequeño «Maqueta de ensayo» arriba a la izquierda, fijo de S04 a S07.
  1. **S04:** «¿Qué quieres lograr este año?» y debajo «Hacer ejercicio 3 veces por semana», escrito letra a letra (animación de máquina de escribir).
  2. **S05:** en «futuro» la pantalla se apaga (saturación baja y más oscura). Aparecen escalonadas las seis tarjetas de motivo y hay un toque en «No tuve tiempo» al decir «qué pasó».
  3. **S06:** se rellena la frase «Si llego a casa después de las 20:00, entonces hago 5 minutos de estiramientos antes de sentarme en el sofá». El color vuelve poco a poco. Etiqueta «L–V · 20:00».
  4. **S07:** cae el sello «Este febrero, no.», girado −6°, justo antes de «Al final». En «calendario» el plan pasa a evento «Plan B: hago 5 minutos de estiramientos antes de sentarme en el sofá», y en «fondo», a pantalla de bloqueo con la hora.

Los textos de la app salen de la definición de producto. No los cambies.

## 5. Textos en pantalla

| escena | texto | dónde y cuánto |
|---|---|---|
| S03 | «Plan B · para tu propósito» y debajo, más pequeño, «Miniapp n.º 1» | Entra en «plan B» y dura unos 2,4 s |
| S04–S07 | «Maqueta de ensayo» | Arriba a la izquierda, fijo |
| S08 | «Compruébalo tú» | En el tercio superior al decir «pruébalo en modo avión», unos 1,9 s |
| S09 | «Este febrero, *no*.» («no» en cursiva o manuscrita) | En el tercio superior, unos 2,4 s, separado de la cara y del subtítulo |

- **Subtítulos:** todo el vídeo, en grupos de 2 a 4 palabras. Inter o similar en negrita, sobre placa oscura.
- **Zona segura:** los subtítulos y los rótulos van por encima de la franja inferior, donde las redes ponen sus botones y el texto del post. Deja libre aproximadamente el 20 % inferior y la columna derecha.
- **Tipografías:** Inter, Crimson Text y Mr Dafoe son provisionales (perfil TEMP). Si CapCut no las tiene, usa equivalentes y apúntalo.

## 6. Sonido

- **Voz:** activa Reducir ruido y normaliza el volumen. El objetivo al exportar es −14 LUFS con picos por debajo de −1 dB, y se mide con `inspeccionar`.
- **Opcional:**
  - Efectos de hoja en S01, de toque en S05 y de sello en S07.
  - Cama instrumental suave de S04 a S07, unos −18 dB por debajo de la voz.
- **Derechos:** solo vale música o efectos con derechos claros. Apunta el nombre y la licencia de cada pista para CIERRE. Una pista de la biblioteca de CapCut puede no valer fuera de TikTok: revísalo antes de usarla.

## 7. Exportar y avisar

- Exporta en 1080×1920, 30 fps, H.264, SDR y AAC 48 kHz, sin marca de agua.
- Guarda el archivo en `media/master/VID-0001_master_v01.mp4`.
- Luego dime «exportado» y yo me encargo de:
  - ejecutar `marco.py inspeccionar`,
  - actualizar MEDIOS.csv,
  - rellenar Montaje en PRODUCCION con lo que me cuentes (color, mezcla, cambios).
