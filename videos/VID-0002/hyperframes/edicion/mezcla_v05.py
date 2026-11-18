"""Mezcla v05 de la edición continua de VID-0002 (ensayo 2). Dos másteres: sin música y con música.

Uso: python mezcla_v05.py <video_sin_sonido.mp4> <salida_base>
  Genera <salida_base>_sin_musica.mp4 (voz + efectos, para añadir el sonido de tendencia dentro de cada app)
  y     <salida_base>.mp4            (voz + efectos + música libre del banco, para publicación directa).
  AV-012 (propuesta): dos másteres por vídeo.

Sonidos reales del banco de Pixabay de Ale (AV-008, AV-011), en la carpeta que dice la variable de entorno
BANCO_AUDIOS (por defecto, C:/Users/aalex/Documents/proyectos/referencias/banco_audios). Estándar: guias/MOTION.md §6.
  - La voz es la voz mejorada de Ale en WAV, cortada con KEEP por cortes.py (media/trabajo/voz_v05.wav). Está
    ≈ 4,4 dB más baja que la original, así que se sube a −17,4 LUFS antes de mezclar: los picos de los efectos
    están calibrados contra esa voz. La mezcla final se lleva a −14 LUFS.
  - Cada efecto se recorta a su tramo audible y su pico cae 1 fotograma después del evento.
  - La música (lofi del banco) va 18 dB bajo la voz y BAJA 4 dB cuando hablas (sidechaincompress), 3 dB más
    baja en la demo, con fundido de entrada de 0,3 s y de salida sobre la cola de imagen final.
  - Los tiempos de CUES siguen en el corte v01 (tiempo viejo); KEEP los traslada al corte v05 y descarta los
    que caen en tramos quitados (= cortes.py = index.html).
Solo biblioteca estándar + ffmpeg.
"""
import array, json, math, os, re, subprocess, sys

BANCO = os.environ.get("BANCO_AUDIOS", r"C:/Users/aalex/Documents/proyectos/referencias/banco_audios").rstrip("/\\") + "/"
AQUI = os.path.dirname(os.path.abspath(__file__))
VOZ = os.path.abspath(os.path.join(AQUI, "..", "..", "media", "trabajo", "voz_v05.wav"))
FPS, SR = 30.0, 48000
VOZ_OBJ = -17.4          # LUFS de la voz antes de mezclar (calibración de los picos de los efectos)
KEEP = [(0.0, 32.60), (33.60, 49.00), (49.86, 52.20), (56.64, 60.15), (61.62, 63.25)]   # = cortes.py
DEMO = (22.70, 41.97)    # tramo de la demo (tiempo viejo): música −3 dB
MUSICA = ("watrfallkero-lofi-beat-chill.mp3", 18.0)   # dB bajo la voz (LUFS integrados)
DUCK = dict(threshold=0.05, ratio=3, attack=80, release=400)   # ≈ −4 dB al hablar
FIN_VOZ = 63.25


def nuevo(t):
    acc = 0.0
    for a, b in KEEP:
        if a <= t < b:
            return acc + (t - a)
        acc += b - a
    return None


# (evento s en tiempo viejo, archivo, recorte inicio, recorte fin, pico objetivo dBFS, nota)
CUES = [
    # T1 · gancho
    (0.30, "page-turn.mp3", 0.0, 0.55, -14, "hoja ENERO → FEBRERO"),
    (1.28, "cinematic-impact-boom.mp3", 0.0, 1.92, -15, "ABANDONASTE detrás de ti + bajón de color (golpe 1 de 3)"),
    (3.26, "pop.mp3", 0.19, 0.31, -12, "CALMA"),
    (3.82, "page-flip.mp3", 0.64, 1.77, -14, "la hoja vuelve a ENERO"),
    # T2 · el problema
    (4.40, "whoosh_largo_misterioso.mp3", 0.47, 1.71, -15, "zoom a través de la hoja hasta el escenario"),
    *[(5.18 + 1.15 * (1 - (1 - i / 14) ** 1.6), "pencil_scribble_short.mp3" if k % 2 == 0 else "scribble-pencil.mp3",
       0.0, 0.29 if k % 2 == 0 else 0.3, -15 - 1.5 * k, "marca de enero (acelera, volumen en escalera)") for k, i in enumerate(range(0, 14, 4))],
    (6.41, "scribble-pencil.mp3", 0.3, 1.0, -16, "se para a mediados de mes"),
    (7.05, "whoosh_fast-simple-chop.mp3", 0.0, 0.55, -16, "las marcas caen"),
    (8.23, "whoosh_esquiva.mp3", 0.0, 0.53, -14, "cortina «/» a ¿Y ESE DÍA?"),
    (11.24, "pop.mp3", 0.19, 0.31, -13, "el jueves crece"),
    (12.31, "pop-universfield-bubble.mp3", 0.0, 0.18, -14, "SIN GANAS"),
    # T3 · la solución
    (12.69, "whoosh_basico.mp3", 0.0, 0.58, -16, "vuelve la cara entera"),
    (14.59, "click-photos.mp3", 0.0, 0.84, -15, "«Plan B» llena el cuadro"),
    (16.80, "whoosh_esquiva.mp3", 0.0, 0.53, -15, "baja el escenario"),
    (17.10, "scribble-pencil.mp3", 0.3, 0.75, -18, "precio tachado"),
    (17.24, "pop.mp3", 0.19, 0.31, -13, "GRATIS"),
    (18.84, "pop-universfield-bubble.mp3", 0.0, 0.18, -14, "PARA ESE DÍA"),
    (21.64, "light-switch.mp3", 0.0, 0.25, -16, "01 /"),
    # T4 · la demo
    (22.70, "whoosh_largo_misterioso.mp3", 0.47, 1.71, -15, "la tarjeta Plan B se ensancha hasta ser la ventana"),
    (23.80, "iphone_typing.mp3", 0.28, 1.48, -21, "tecleo del propósito"),
    (26.12, "page-turn.mp3", 0.0, 0.55, -15, "salto a febrero"),
    *[(26.87 + 0.13 * i, "pop.mp3" if i % 2 == 0 else "pop-universfield-bubble.mp3", 0.19 if i % 2 == 0 else 0.0,
       0.31 if i % 2 == 0 else 0.18, -14 - 1.6 * i, "tarjeta de obstáculo") for i in range(0, 6, 2)],
    (29.45, "whoosh_esquiva.mp3", 0.0, 0.53, -17, "inserto 1: la ventana pasa a pantalla completa"),
    (29.60, "screen-tap.mp3", 0.40, 0.70, -11, "toque en «No tuve tiempo»"),
    (30.95, "whoosh_fast-simple-chop.mp3", 0.0, 0.55, -18, "inserto 1: vuelve la ventana"),
    (31.50, "whoosh_fast-simple-chop.mp3", 0.0, 0.55, -16, "paso 3"),
    (33.62, "iphone_typing.mp3", 2.58, 3.78, -21, "tecleo «Si…»"),
    (35.70, "iphone_typing.mp3", 5.19, 6.36, -21, "tecleo «entonces…»"),
    # T5 · el resultado
    (37.52, "tension-riser.mp3", 1.78, 2.98, -16, "tensión antes del sello (se coloca por su final)"),
    (37.54, "office-stamp-varios-veces.mp3", 0.0, 0.66, -8, "inserto 2: sello «Este febrero, no.» (golpe 2 de 3)"),
    (38.95, "whoosh_fast-simple-chop.mp3", 0.0, 0.55, -18, "inserto 2: vuelve la ventana"),
    (39.54, "new-notification.mp3", 0.0, 1.38, -15, "evento de calendario"),
    (41.06, "message-envoye-iphone-apple.mp3", 0.0, 0.5, -14, "el plan viaja al fondo de pantalla"),
    # T6 · la serie
    (40.97, "whoosh_basico.mp3", 0.0, 0.58, -15, "la pantalla de bloqueo se encoge hasta la tarjeta 01"),
    (44.65, "click-photos.mp3", 0.0, 0.84, -17, "1 POR SEMANA"),
    (46.61, "pop-universfield-bubble.mp3", 0.0, 0.18, -14, "icono productividad"),
    (47.81, "pop.mp3", 0.19, 0.31, -14, "icono ciencia"),
    (49.92, "pop-universfield-bubble.mp3", 0.0, 0.18, -14, "icono minijuegos"),
    (51.06, "whoosh_fast-simple-chop.mp3", 0.0, 0.55, -16, "la tarjeta se aleja y se ve que sigue"),
    # T7 · llamada a la acción
    (56.50, "whoosh_esquiva.mp3", 0.0, 0.53, -15, "sube el escenario"),
    (59.56, "cinematic-riser-impact.mp3", "pk-0.05", 3.21, -9, "«no.» final (golpe 3 de 3)"),
]


def run(args):
    return subprocess.run(args, capture_output=True, text=True, encoding="utf-8", errors="replace")


def pcm(path, a=0.0, b=None):
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


def lufs(args):
    e = run(["ffmpeg", "-hide_banner", "-nostats", *args, "-af", "ebur128=peak=true", "-f", "null", "-"]).stderr
    return float(re.findall(r"I:\s+(-?[\d.]+) LUFS", e)[-1]), float(re.findall(r"Peak:\s+(-?[\d.]+) dBFS", e)[-1])


def mezclar(fin, vI, musica, destino, work, log):
    """Una mezcla (con o sin música) normalizada a −14 LUFS. Devuelve (LUFS, pico)."""
    inputs, filt, labels = ["-i", VOZ], [], []
    gv = VOZ_OBJ - vI
    if musica:
        filt.append(f"[0:a]aresample=48000,aformat=channel_layouts=mono,volume={gv:.2f}dB,acompressor=threshold=-18dB:ratio=2:attack=10:release=150:makeup=1,asplit=2[vm][vk]")
    else:
        filt.append(f"[0:a]aresample=48000,aformat=channel_layouts=mono,volume={gv:.2f}dB,acompressor=threshold=-18dB:ratio=2:attack=10:release=150:makeup=1[vm]")
    labels.append("[vm]")
    for t_v01, f, a, b, pk_db, note in CUES:
        t = nuevo(t_v01)
        if t is None or t > fin - 0.2:
            continue
        path = BANCO + f
        if isinstance(a, str):
            x = pcm(path); i, _ = peak(x); a = max(0.0, i / SR + float(a[2:]))
        x = pcm(path, a, b)
        i, p = peak(x)
        lag = i / SR
        start = t + 1 / FPS - lag                      # el pico cae 1 fotograma después del evento
        if "por su final" in note:
            start = t - (b - a)
        gain = pk_db - 20 * math.log10(p / 32768)
        d = max(0, int(round(start * 1000)))
        inputs += ["-ss", f"{a}", "-t", f"{b - a}", "-i", path]
        k = len(labels)
        filt.append(f"[{k}:a]aresample=48000,aformat=channel_layouts=mono,afade=t=out:st={max(0, b - a - 0.04):.3f}:d=0.04,volume={gain:.2f}dB,adelay={d}|{d}[s{k}]")
        labels.append(f"[s{k}]")
        if musica:
            log.append({"t_v01": t_v01, "t": round(t, 3), "archivo": f, "recorte": [round(a, 3), round(b, 3)], "pico_en": round(lag, 3), "entra": round(start, 3), "pico_dbfs": pk_db, "nota": note})
    if musica:
        mpath = BANCO + MUSICA[0]
        mI, _ = lufs(["-t", "60", "-i", mpath])
        mg = (VOZ_OBJ - MUSICA[1]) - mI
        inputs += ["-i", mpath]; k = len(labels)
        d0, d1 = (nuevo(DEMO[0]) or 0.0), (nuevo(DEMO[1] - 0.01) or 0.0)
        filt.append(f"[{k}:a]aresample=48000,aformat=channel_layouts=mono,atrim=0:{fin},afade=t=in:st=0:d=0.3,afade=t=out:st={fin - 1.0:.2f}:d=1.0,"
                    f"volume={mg:.2f}dB,volume=-3dB:enable='between(t,{d0:.2f},{d1:.2f})'[mus]")
        filt.append(f"[mus][vk]sidechaincompress=threshold={DUCK['threshold']}:ratio={DUCK['ratio']}:attack={DUCK['attack']}:release={DUCK['release']}:makeup=1[musd]")
        labels.append("[musd]")
        log.append({"musica_ganancia_db": round(mg, 2), "bajada_al_hablar": DUCK})
    filt.append(f"{''.join(labels)}amix=inputs={len(labels)}:normalize=0:duration=first,atrim=0:{fin}[mix]")
    crudo = os.path.join(work, "cruda_" + ("musica" if musica else "sin") + ".wav")
    r = run(["ffmpeg", "-v", "error", "-y", *inputs, "-filter_complex", ";".join(filt), "-map", "[mix]", "-ar", "48000", crudo])
    if r.returncode:
        print(r.stderr[-2500:]); sys.exit(1)
    I, _ = lufs(["-i", crudo])
    g = -14.0 - I
    for _ in range(2):
        run(["ffmpeg", "-v", "error", "-y", "-i", crudo, "-af", f"volume={g:.2f}dB,alimiter=limit=0.84:attack=2:release=60:level=disabled", "-ar", "48000", destino])
        I2, P2 = lufs(["-i", destino])
        if abs(I2 + 14) <= 0.3:
            break
        g -= (I2 + 14)
    return I2, P2


def main(src, base):
    fin = float(run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", src]).stdout.strip())
    work = os.path.join(os.path.dirname(os.path.abspath(base)), "mezcla_tmp"); os.makedirs(work, exist_ok=True)
    vI, _ = lufs(["-i", VOZ])
    log, res = [], {}
    for musica, destino in ((False, base + "_sin_musica.mp4"), (True, base + ".mp4")):
        wav = os.path.join(work, "final_" + ("musica" if musica else "sin") + ".wav")
        I2, P2 = mezclar(fin, vI, musica, wav, work, log)
        r = run(["ffmpeg", "-v", "error", "-y", "-i", src, "-i", wav, "-map", "0:v", "-map", "1:a", "-c:v", "copy", "-c:a", "aac", "-b:a", "256k", "-ac", "2", "-ar", "48000", "-shortest", destino])
        if r.returncode:
            print(r.stderr[-2500:]); sys.exit(1)
        res["con_musica" if musica else "sin_musica"] = {"lufs": I2, "pico_dbfs": P2, "archivo": destino}
        print(("con música" if musica else "sin música"), f"{I2:.1f} LUFS, pico {P2:.1f} dBFS -> {destino}")
    json.dump({"voz_lufs_original": vI, "voz_lufs_mezcla": VOZ_OBJ, "masters": res, "efectos": [x for x in log if "archivo" in x],
               "musica": [x for x in log if "musica_ganancia_db" in x]},
              open(base + "_mezcla.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(len([x for x in log if 'archivo' in x]), "efectos")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
