"""Mezcla de efectos de sonido reales (CC0, Freesound) sobre el ensayo de edición continua.

Uso: python sonido.py <video_sin_efectos.mp4> <carpeta_sfx> <salida.mp4>
La carpeta sfx contiene fs-<id>.wav (mono, 48 kHz) convertidos de las vistas previas de Freesound.

Cada efecto: (tiempo del evento en el vídeo, archivo, recorte inicio-fin en s, instante del golpe
dentro del recorte, ganancia en dB). Las ganancias dejan cada efecto entre 8 y 18 dB por debajo de
los picos de la voz (rms 10 ms p99 ≈ −15 dBFS antes de normalizar). Después se sube todo a −14 LUFS
y se limita el pico a −1,5 dBFS. La voz pasa antes por una compresión suave (umbral −20 dBFS, 3:1)
para no depender del limitador. La ganancia final se calcula en dos pasadas (mide y corrige).
Solo biblioteca estándar + ffmpeg.
"""
import subprocess
import sys

WHOOSH, PAPEL, CLIC, TECLA, SELLO, SWITCH, GOLPE = (
    "fs-878248.wav", "fs-856497.wav", "fs-528561.wav", "fs-348239.wav", "fs-470710.wav", "fs-878244.wav", "fs-683031.wav")
# archivo: (inicio, fin, golpe dentro del recorte)
RECORTE = {WHOOSH: (0.0, 0.2, 0.03), PAPEL: (0.25, 1.1, 0.17), CLIC: (0.0, 0.1, 0.0), TECLA: (0.0, 0.2, 0.0),
           SELLO: (0.45, 1.1, 0.11), SWITCH: (0.0, 0.12, 0.0), GOLPE: (0.15, 0.68, 0.03)}

CUES = [
    # gancho: la hoja gira y vuelve; bajón en "abandonas"
    (0.86, PAPEL, -9.7), (1.58, GOLPE, -25.5), (3.42, PAPEL, -11.0),
    # escenario baja / sube y barridos de la barra entre tramos
    (4.2, WHOOSH, -8.5), (7.03, WHOOSH, -9.5), (10.73, WHOOSH, -9.5), (18.95, WHOOSH, -9.5),
    (23.6, WHOOSH, -8.5), (28.18, WHOOSH, -9.5), (36.0, WHOOSH, -9.5),
    # enero: seis marcas
    *[(4.45 + 0.21 * i, CLIC, -6.7 - 0.6 * i) for i in range(6)],
    # la miniapp: logo y "Plan B"
    (7.32, CLIC, -7.5), (8.5, WHOOSH, -11.0),
    # cómo funciona: tecleo del propósito y nodos
    *[(11.46 + 0.075 * i, TECLA, -16.9 + (1.8 if i % 3 == 0 else -1.2 if i % 3 == 1 else 0.0)) for i in range(12)],
    (12.73, CLIC, -6.7), (14.37, CLIC, -6.7), (15.25, CLIC, -3.7), (16.97, CLIC, -6.7),
    # lo que te llevas: sello, calendario, fondo
    (24.1, SELLO, -16.5), (25.62, CLIC, -7.5), (27.22, CLIC, -7.5),
    # lo que no te pide: fichas y modo avión
    (29.28, CLIC, -6.7), (30.48, CLIC, -6.7), (34.5, SWITCH, -12.2),
    # acento final "no."
    (38.27, GOLPE, -17.5),
]


def mezclar(video, carpeta, salida, ganancia_db):
    archivos = sorted({c[1] for c in CUES})
    entradas = ["-i", video]
    for a in archivos:
        entradas += ["-i", f"{carpeta}/{a}"]
    partes, etiquetas = [], []
    for k, (t, a, g) in enumerate(CUES):
        idx = archivos.index(a) + 1
        ini, fin, golpe = RECORTE[a]
        ms = max(0, round((t - golpe) * 1000))
        partes.append(f"[{idx}:a]atrim={ini}:{fin},asetpts=PTS-STARTPTS,afade=t=out:st={fin - ini - 0.03:.3f}:d=0.03,"
                      f"volume={g}dB,adelay={ms}|{ms},apad[c{k}]")
        etiquetas.append(f"[c{k}]")
    n = len(CUES) + 1
    partes.append(f"[0:a]aformat=channel_layouts=mono,aresample=48000,"
                  f"acompressor=threshold=0.1:ratio=3:attack=8:release=150:knee=4[voz]")
    partes.append(f"[voz]{''.join(etiquetas)}amix=inputs={n}:normalize=0:duration=first,"
                  f"volume={ganancia_db:.2f}dB,alimiter=limit=0.84:level=false,aformat=channel_layouts=stereo[mez]")
    cmd = ["ffmpeg", "-v", "error", "-y", *entradas, "-filter_complex", ";".join(partes),
           "-map", "0:v", "-map", "[mez]", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-ar", "48000", salida]
    subprocess.run(cmd, check=True)


def loudness(archivo):
    out = subprocess.run(["ffmpeg", "-hide_banner", "-i", archivo, "-vn", "-af", "ebur128=peak=true", "-f", "null", "-"],
                         capture_output=True, text=True).stderr
    i = [l for l in out.splitlines() if l.strip().startswith("I:")][-1]
    return float(i.split()[1])


def main(video, carpeta, salida, objetivo=-14.0):
    g = 8.0
    for _ in range(3):
        mezclar(video, carpeta, salida, g)
        i = loudness(salida)
        print(f"ganancia {g:+.2f} dB -> {i:.1f} LUFS")
        if abs(i - objetivo) < 0.3:
            break
        g += objetivo - i


if __name__ == "__main__":
    main(*sys.argv[1:4])
