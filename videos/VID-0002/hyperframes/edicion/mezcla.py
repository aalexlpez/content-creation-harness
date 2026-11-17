"""Mezcla de sonido de la edición continua de VID-0002 (ensayo 2).

Uso: python mezcla.py <video_sin_efectos.mp4> <salida.mp4>

Sonidos reales del banco de Pixabay de Ale (licencia Pixabay), en
C:/Users/aalex/Documents/proyectos/referencias/banco_audios. AV-008: nada sintetizado.
Estándar: guias/MOTION.md §6.
  - Cada efecto se recorta a su tramo audible y su pico cae 1 fotograma después del evento.
  - La ganancia lleva el pico de cada recorte a un nivel objetivo (dBFS) antes de la mezcla.
  - Música lofi en todo el vídeo, unos 16–18 dB bajo la voz, fundido de 0,2 s al final.
  - Voz con compresión suave; total a −14 LUFS y pico ≤ −1,5 dBFS (dos pasadas: mide y corrige).
Solo biblioteca estándar + ffmpeg.
"""
import array, json, os, re, subprocess, sys

BANCO = r"C:/Users/aalex/Documents/proyectos/referencias/banco_audios/"
FPS = 30.0
SR = 48000
FIN = 63.25

# (evento s, archivo, recorte inicio, recorte fin, pico objetivo dBFS, nota)
# recorte: números en s; "pk-0.05" = desde 50 ms antes del pico del archivo; None = hasta el final del tramo audible
CUES = [
    # T1 · gancho
    (0.30, "page-turn.mp3", 0.0, 0.55, -14, "hoja ENERO → FEBRERO"),
    (1.28, "cinematic-impact-boom.mp3", 0.0, 1.92, -15, "bajón de color en «abandonaste» (golpe 1 de 3)"),
    (3.82, "page-flip.mp3", 0.64, 1.77, -14, "la hoja vuelve a ENERO"),
    # T2 · el problema
    (4.56, "whoosh_basico.mp3", 0.0, 0.58, -14, "baja el escenario"),
    *[(5.18 + 1.15 * (1 - (1 - i / 14) ** 1.6), "pencil_scribble_short.mp3" if k % 2 == 0 else "scribble-pencil.mp3",
       0.0, 0.29 if k % 2 == 0 else 0.3, -15 - 1.2 * k, "marca de enero (acelera, volumen en escalera)") for k, i in enumerate(range(0, 14, 2))],
    (6.41, "scribble-pencil.mp3", 0.3, 1.0, -16, "se para a mitad de mes"),
    (7.05, "whoosh_fast-simple-chop.mp3", 0.0, 0.55, -16, "las marcas caen"),
    (8.23, "whoosh_esquiva.mp3", 0.0, 0.53, -14, "cortina «/» a ¿Y ESE DÍA?"),
    *[(9.3 + 0.12 * k, "mouse-click-sfx.mp3", 0.0, 0.15, -24 - 0.6 * n, "check de la semana") for n, k in enumerate([0, 1, 2, 4, 5, 6])],
    (11.24, "pop.mp3", 0.19, 0.31, -13, "el jueves crece"),
    (12.31, "pop-universfield-bubble.mp3", 0.0, 0.18, -14, "SIN GANAS"),
    # T3 · la solución
    (12.69, "whoosh_basico.mp3", 0.0, 0.58, -16, "sube el escenario"),
    (14.55, "click-photos.mp3", 0.0, 0.84, -15, "rótulo Plan B"),
    (16.80, "whoosh_esquiva.mp3", 0.0, 0.53, -15, "baja el escenario"),
    (17.24, "pop.mp3", 0.19, 0.31, -13, "GRATIS"),
    (18.84, "pop-universfield-bubble.mp3", 0.0, 0.18, -14, "PARA ESE DÍA"),
    (21.64, "light-switch.mp3", 0.0, 0.25, -16, "01 /"),
    # T4 · la demo (maqueta)
    (22.75, "whoosh_largo_misterioso.mp3", 0.47, 1.71, -14, "la tarjeta se vuelve la maqueta"),
    (23.80, "iphone_typing.mp3", 0.28, 1.48, -21, "tecleo del propósito"),
    (26.12, "page-turn.mp3", 0.0, 0.55, -15, "salto a febrero"),
    *[(26.87 + 0.13 * i, "pop.mp3" if i % 2 == 0 else "pop-universfield-bubble.mp3", 0.19 if i % 2 == 0 else 0.0,
       0.31 if i % 2 == 0 else 0.18, -14 - 1.6 * i, "tarjeta de obstáculo") for i in range(6)],
    (29.60, "screen-tap.mp3", 0.40, 0.70, -11, "toque en «No tuve tiempo»"),
    (31.50, "whoosh_fast-simple-chop.mp3", 0.0, 0.55, -16, "paso 3"),
    (33.62, "iphone_typing.mp3", 2.58, 3.78, -21, "tecleo «Si…»"),
    (35.70, "iphone_typing.mp3", 5.19, 6.36, -21, "tecleo «entonces…»"),
    # T5 · el resultado
    (37.52, "tension-riser.mp3", 1.78, 2.98, -16, "tensión antes del sello (se coloca por su final)"),
    (37.54, "office-stamp-varios-veces.mp3", 0.0, 0.66, -8, "sello «Este febrero, no.» (golpe 2 de 3)"),
    (39.54, "new-notification.mp3", 0.0, 1.38, -15, "evento de calendario"),
    (41.06, "message-envoye-iphone-apple.mp3", 0.0, 0.5, -14, "el plan viaja al fondo de pantalla"),
    # T6 · la serie
    (41.90, "whoosh_basico.mp3", 0.0, 0.58, -15, "vuelta al escenario"),
    *[(44.65 + 0.16 * k, "pop.mp3", 0.19, 0.31, -14 - 3 * k, "tarjetas 02–04") for k in range(3)],
    (45.68, "click-photos.mp3", 0.0, 0.84, -16, "1 POR SEMANA"),
    (46.61, "pop-universfield-bubble.mp3", 0.0, 0.18, -14, "icono productividad"),
    (47.81, "pop.mp3", 0.19, 0.31, -14, "icono ciencia"),
    (49.48, "pop-universfield-bubble.mp3", 0.0, 0.18, -14, "icono minijuegos"),
    (51.06, "whoosh_fast-simple-chop.mp3", 0.0, 0.55, -16, "la fila se aleja"),
    (54.04, "switch-toggle.mp3", 0.0, 0.46, -15, "LIBRES"),
    (54.60, "light-switch.mp3", 0.0, 0.25, -15, "GRATIS"),
    *[(55.24 + 0.14 * k, "pop.mp3", 0.19, 0.31, -17 - 3 * k, "personas") for k in range(3)],
    # T7 · llamada a la acción
    (56.50, "whoosh_esquiva.mp3", 0.0, 0.53, -15, "sube el escenario"),
    (57.85, "click-photos.mp3", 0.0, 0.84, -15, "rótulo ARMA TU PLAN B"),
    (59.56, "cinematic-riser-impact.mp3", "pk-0.05", 3.21, -9, "«no.» final (golpe 3 de 3)"),
    (61.15, "benkirb-shine.mp3", 0.0, 1.0, -20, "link en el perfil"),
]
MUSICA = ("watrfallkero-lofi-beat-chill.mp3", 18.0)   # dB bajo la voz (LUFS integrados)


def run(args):
    return subprocess.run(args, capture_output=True, text=True, encoding="utf-8", errors="replace")


def pcm(path, a=0.0, b=None):
    """Mono float aprox. como array de int16 a 48 kHz del tramo [a, b]."""
    args = ["ffmpeg", "-v", "error", "-ss", f"{a}", "-i", path]
    if b is not None:
        args += ["-t", f"{max(0.01, b - a)}"]
    args += ["-ac", "1", "-ar", str(SR), "-f", "s16le", "-"]
    raw = subprocess.run(args, capture_output=True).stdout
    x = array.array("h"); x.frombytes(raw[: len(raw) // 2 * 2]); return x


def peak(x):
    if not x:
        return 0, 1
    i = max(range(len(x)), key=lambda k: abs(x[k])); return i, abs(x[i]) or 1


def lufs(path_or_args):
    e = run(["ffmpeg", "-hide_banner", "-nostats", *path_or_args, "-af", "ebur128=peak=true", "-f", "null", "-"]).stderr
    I = float(re.findall(r"I:\s+(-?[\d.]+) LUFS", e)[-1]); P = float(re.findall(r"Peak:\s+(-?[\d.]+) dBFS", e)[-1]); return I, P


def main(src, out):
    work = os.path.join(os.path.dirname(os.path.abspath(out)), "mezcla_tmp"); os.makedirs(work, exist_ok=True)
    inputs, filt, labels, log = ["-i", src], [], [], []
    # voz: compresión suave
    filt.append("[0:a]aresample=48000,aformat=channel_layouts=mono,acompressor=threshold=-20dB:ratio=3:attack=8:release=120:makeup=1[voz]")
    labels.append("[voz]")
    vI, _ = lufs(["-i", src, "-vn"])
    for n, (t, f, a, b, pk_db, note) in enumerate(CUES):
        path = BANCO + f
        if isinstance(a, str):
            x = pcm(path); i, _ = peak(x); a = max(0.0, i / SR + float(a[2:]))
        x = pcm(path, a, b)
        i, p = peak(x)
        lag = i / SR                                   # pico dentro del recorte
        start = t + 1 / FPS - lag                      # el pico cae 1 fotograma después del evento
        if "por su final" in note:
            start = t - (b - a)
        gain = pk_db - 20 * __import__("math").log10(p / 32768)
        d = max(0, int(round(start * 1000)))
        inputs += ["-ss", f"{a}", "-t", f"{b - a}", "-i", path]
        k = len(labels)
        filt.append(f"[{k}:a]aresample=48000,aformat=channel_layouts=mono,afade=t=out:st={max(0, b - a - 0.04):.3f}:d=0.04,volume={gain:.2f}dB,adelay={d}|{d}[s{k}]")
        labels.append(f"[s{k}]")
        log.append({"t": round(t, 3), "archivo": f, "recorte": [round(a, 3), round(b, 3)], "pico_en": round(lag, 3), "entra": round(start, 3), "pico_dbfs": pk_db, "nota": note})
    # música: nivel relativo a la voz
    mpath = BANCO + MUSICA[0]
    mI, _ = lufs(["-t", "60", "-i", mpath])
    mg = (vI - MUSICA[1]) - mI
    inputs += ["-i", mpath]; k = len(labels)
    filt.append(f"[{k}:a]aresample=48000,aformat=channel_layouts=mono,atrim=0:{FIN},afade=t=in:st=0:d=0.3,afade=t=out:st=63.0:d=0.2,volume={mg:.2f}dB[mus]")
    labels.append("[mus]")
    filt.append(f"{''.join(labels)}amix=inputs={len(labels)}:normalize=0:duration=first,atrim=0:{FIN}[mix]")
    tmp = os.path.join(work, "mezcla_cruda.wav")
    r = run(["ffmpeg", "-v", "error", "-y", *inputs, "-filter_complex", ";".join(filt), "-map", "[mix]", "-ar", "48000", tmp])
    if r.returncode: print(r.stderr[-2000:]); sys.exit(1)
    I, P = lufs(["-i", tmp])
    g = -14.0 - I
    final = os.path.join(work, "mezcla.wav")
    run(["ffmpeg", "-v", "error", "-y", "-i", tmp, "-af", f"volume={g:.2f}dB,alimiter=limit=0.84:attack=2:release=60:level=disabled", "-ar", "48000", final])
    I2, P2 = lufs(["-i", final])
    if abs(I2 + 14) > 0.3:
        run(["ffmpeg", "-v", "error", "-y", "-i", tmp, "-af", f"volume={g - (I2 + 14):.2f}dB,alimiter=limit=0.84:attack=2:release=60:level=disabled", "-ar", "48000", final])
        I2, P2 = lufs(["-i", final])
    r = run(["ffmpeg", "-v", "error", "-y", "-i", src, "-i", final, "-map", "0:v", "-map", "1:a", "-c:v", "copy", "-c:a", "aac", "-b:a", "256k", "-ac", "2", "-ar", "48000", "-shortest", out])
    if r.returncode: print(r.stderr[-2000:]); sys.exit(1)
    json.dump({"voz_lufs": vI, "musica_ganancia_db": round(mg, 2), "final_lufs": I2, "final_pico_dbfs": P2, "efectos": log},
              open(os.path.splitext(out)[0] + "_mezcla.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"{len(CUES)} efectos + música ({mg:+.1f} dB) · voz {vI:.1f} LUFS -> final {I2:.1f} LUFS, pico {P2:.1f} dBFS -> {out}")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
