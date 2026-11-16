# VID-0001 · Producción

Rodaje, ingesta, animación y montaje. Referencias: [TECNICA](../../guias/TECNICA.md) · [SET](../../guias/SET.md).

## Control

- Estado: CANCELADO
- Bloqueo: NINGUNO
- Siguiente_paso: Ensayo cerrado el 2026-11-16; lo sustituye un nuevo ensayo de la miniapp 1
- Perfil_visual: v2
- Perfil_tecnico: 1080x1920 · 30 fps · H.264 · SDR BT.709 · AAC 48 kHz
- Editor: CapCut Desktop (versión gratis). El montaje v01 con ffmpeg y HyperFrames se descartó el 2026-11-15 y está en `media/descartado/`

## Rodaje

| toma | escena | qué grabar | cámara o pantalla | hecha |
|---|---|---|---|---|
| T1 | S01–S09 | Las nueve frases a cámara, en orden y sin moverse del sitio, tres tomas de cada una. Antes de cada frase, decir el número de escena; 1 s quieto antes y después | Cámara A · Galaxy S24+ trasera, plano medio corto, 4K/30, HDR desactivado | sí |
| T3 | S08 | Detalle de la mano activando el modo avión. Opcional, más adelante | Cámara A recolocada | no |
| R1 | S04–S07 | Maqueta de las cuatro pantallas. No se graba: se prepara para el montaje | Animación o maqueta HTML | no |
| R2 | S01 · S02 | Hoja de calendario «ENERO» → «FEBRERO» → «ENERO». No se graba: se prepara para el montaje | Animación | no |

- Fecha: 2026-11-12
- Set (luz, posición, reflector):
- Cámara (móvil, resolución, fps, HDR, blancos):
- Audio (DJI, modo, prueba escuchada):
- Observaciones: Una sola grabación continua de 4 min 53 s con varias tomas por frase. Ale sostiene el micro DJI en la mano y se ve en plano. La camiseta lleva un logotipo de terceros («WESTNETZ») visible: revisar antes del vídeo real. T3 no se grabó

## Ingesta

| archivo | escena | resolución · fps · color | audio | notas |
|---|---|---|---|---|
| VID_20261112_211711.mp4 | S01–S09 | 3840×2160 con rotación −90° (vertical) · 30 fps · H.264 62 Mbps · SDR BT.709 | AAC 48 kHz estéreo · −14,2 LUFS integrados · LRA 15 LU | 292,8 s · 2,3 GB. Medido con ffprobe y ebur128 |
| softbox-left-face.mp4 · softbox-right-face.mp4 | — | 3840×2160 con rotación −90° · 30 fps · H.264 · SDR BT.709 | AAC 48 kHz | Pruebas de luz de 8 s y 25 s. No se usan en el montaje |

Originales intactos en `media/originales/`. Comprobación: `python scripts/marco.py inspeccionar <archivo> --perfil ingesta`.

## Animación

- Herramienta y versión: PENDIENTE: los recursos R1 y R2 se harán en CapCut
- Escenas animadas y entrega (MP4 por escena, WAV, SRT):
- Prueba de seek (inicio, medio, final):

## Montaje

- Proyecto_editor:
- Corte_actual:
- Cambios frente al guion:
- Color aplicado:
- Mezcla (voz, música, efectos):
- Subtítulos:

## Correcciones

| ronda | tiempo | defecto | cambio | verificado |
|---|---|---|---|---|

## Tiempo

| fecha | tarea | minutos |
|---|---|---|

## Historial

- 2026-11-12 · Estado → BORRADOR
- 2026-11-12 · Estado → BORRADOR
- 2026-11-13 · Ingesta, corte de cámara y montaje v01 (guion v02)
- 2026-11-15 · Se descarta el montaje v01 (ffmpeg + HyperFrames); Ale monta en CapCut con el guion v02
- 2026-11-16 · Estado → CANCELADO
