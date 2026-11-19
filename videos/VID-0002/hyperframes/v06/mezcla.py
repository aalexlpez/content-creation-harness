"""Mezcla de la edición v06 de VID-0002. Dos másteres (AV-012, propuesta): sin música y con música.

Uso: python mezcla.py <video_sin_sonido.mp4> <salida_base>
  <salida_base>_sin_musica.mp4  voz + efectos (para poner el sonido de tendencia dentro de cada app)
  <salida_base>.mp4             voz + efectos + música editada por compases (media/trabajo/musica_v06.wav, de preparar.py)
  <salida_base>_mezcla.json     registro de efectos y niveles

Cambios frente a la mezcla del ensayo flotante (edicion/mezcla_flotante.py):
  - Tiempos de los efectos en tn (tiempo del corte, la voz), no en el tiempo viejo. CO (preparar.py) es 0 desde que se
    quitó la apertura en frío; si vuelve a haber algo antes de la voz, todo entra con CO de retraso.
  - Menos efectos: sin un «pop» por cada icono ni un lápiz por cada flecha; los cortes de los recursos van a tiempo de
    la música y no llevan efecto. Golpes: ABANDONASTE (1), el sello (2) y «febrero» tras el silencio (3).
  - La música ya viene montada (preparar.py). Va 13 dB bajo la voz, baja ≈ 5 dB cuando hablas (sidechaincompress),
    2 dB menos en la demo, y sube en la cola (sin voz).
Sonidos reales del banco de Pixabay de Ale (AV-008, AV-011), carpeta BANCO_AUDIOS. Estándar: guias/MOTION.md §6.
Solo biblioteca estándar + ffmpeg.
"""
import array, json, math, os, re, subprocess, sys

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import preparar  # noqa: E402  (CO, D, rutas)

BANCO = preparar.BANCO
VID = preparar.VID
VOZ = os.path.join(VID, "media", "trabajo", "voz_v06.wav")
MUS = os.path.join(VID, "media", "trabajo", "musica_v06.wav")
CO, D = preparar.CO, preparar.D
FPS, SR = 30.0, 48000
VOZ_OBJ = -17.4                       # LUFS de la voz antes de mezclar (calibración de los picos de los efectos)
MUS_DB = 13.0                         # dB bajo la voz (LUFS integrados de la música); con 16 quedaba ≈ 18 dB bajo la voz al hablar (medido, 2026-11-19)
DUCK = dict(threshold=0.04, ratio=4, attack=60, release=350)
DEMO = (22.70, 41.40)                 # tn: música −2 dB (la demo de la app real acaba en 41,40)
SUBE = [(55.55, 60.0, 4.0)]   # tn: tramos sin voz donde la música sube (la cola)

LAPIZ = ("pencil_scribble_short.mp3", 0.0, 0.29)
POP = ("pop.mp3", 0.19, 0.31)
BUB = ("pop-universfield-bubble.mp3", 0.0, 0.18)
def flecha(t, db=-21):
    return (t, LAPIZ[0], LAPIZ[1], LAPIZ[2], db, "flecha que se dibuja")
def nodo(t, k, db, nota):
    f = POP if k == 0 else BUB
    return (t, f[0], f[1], f[2], db, nota)

# (tn, archivo, recorte inicio, recorte fin, pico objetivo dBFS, nota). Un recorte inicial «pk-0.05» empieza 0,05 s antes del pico.
CUES = [
    # Gancho
    (0.45, "page-turn.mp3", 0.0, 0.55, -18, "R01: la hoja pasa a febrero"),
    (1.325, "cinematic-impact-boom.mp3", 0.0, 1.92, -15, "ABANDONASTE sobre R02 (golpe 1 de 3)"),
    (3.24, "pop.mp3", 0.19, 0.31, -13, "CALMA"),
    # Problema
    nodo(4.70, 1, -16, "calendario de enero"),
    *[(4.95 + 1.10 * (1 - (1 - i / 14) ** 1.6), "pencil_scribble_short.mp3" if k % 2 == 0 else "scribble-pencil.mp3",
       0.0, 0.29 if k % 2 == 0 else 0.3, -16 - 1.5 * k, "marca de enero (acelera, volumen en escalera)") for k, i in enumerate(range(0, 14, 4))],
    (6.30, "whoosh_fast-simple-chop.mp3", 0.0, 0.55, -19, "las marcas caen"),
    nodo(10.84, 0, -15, "la semana"),
    nodo(11.15, 1, -15, "JUEVES ?"), flecha(11.3),
    nodo(12.25, 0, -14, "SIN GANAS"),
    # Solución
    nodo(12.70, 1, -16, "etiqueta cerobytes"),
    (14.59, "click-photos.mp3", 0.0, 0.84, -16, "«Plan B» llena el cuadro (con el estribillo)"),
    nodo(15.23, 0, -15, "teléfono Plan B"), flecha(15.4),
    (17.10, "scribble-pencil.mp3", 0.3, 0.75, -18, "precio tachado"),
    nodo(17.24, 1, -14, "GRATIS"),
    nodo(18.84, 0, -15, "tarjeta JUEVES"),
    (21.64, "light-switch.mp3", 0.0, 0.25, -16, "01 /"),
    # Demo: la app REAL (demo/grabar.mjs), un toque = un sonido, a la vez que la acción de ACCIONES
    (22.70, "whoosh_largo_misterioso.mp3", 0.47, 1.71, -15, "el teléfono flotante se convierte en el celular de la demo"),
    (23.45, "screen-tap.mp3", 0.40, 0.70, -15, "toque en «¿Necesitas una idea?»"),
    (24.20, "screen-tap.mp3", 0.40, 0.70, -13, "toque en «Hacer ejercicio»"),
    (25.25, "screen-tap.mp3", 0.40, 0.70, -14, "Continuar → «1 de febrero»"),
    (25.30, "page-turn.mp3", 0.0, 0.55, -17, "la app te lleva a febrero"),
    (29.35, "whoosh_esquiva.mp3", 0.0, 0.53, -18, "acercamiento a las razones"),
    (29.62, "screen-tap.mp3", 0.40, 0.70, -11, "toque en «No tuve tiempo»"),
    (30.80, "screen-tap.mp3", 0.40, 0.70, -15, "Continuar → paso 3"),
    (30.95, "whoosh_fast-simple-chop.mp3", 0.0, 0.55, -19, "se aleja: el paso 3 entero"),
    (31.85, "screen-tap.mp3", 0.40, 0.70, -15, "toque en «Escribir la mía»"),
    (32.62, "iphone_typing.mp3", 2.58, 3.78, -21, "tecleo «llego a casa después de las 20:00»"),
    (34.55, "screen-tap.mp3", 0.40, 0.70, -15, "Continuar → paso 4"),
    (35.10, "iphone_typing.mp3", 5.19, 6.36, -21, "tecleo «hago 5 minutos de estiramientos»"),
    (36.28, "screen-tap.mp3", 0.40, 0.70, -13, "toque en «Ver mi plan»"),
    (36.48, "tension-riser.mp3", 1.78, 2.98, -18, "tensión antes del plan (se coloca por su final)"),
    (36.50, "cinematic-impact-boom.mp3", 0.0, 1.92, -17, "aparece el plan con el estribillo 2 (golpe 2 de 3)"),
    (37.55, "screen-tap.mp3", 0.40, 0.70, -14, "toque en «Añadir recordatorio»"),
    (37.95, "new-notification.mp3", 0.0, 1.38, -16, "hora 20:00: el recordatorio"),
    (39.20, "whoosh_basico.mp3", 0.0, 0.58, -18, "baja hasta el fondo de pantalla"),
    (40.95, "whoosh_fast-simple-chop.mp3", 0.0, 0.55, -16, "el celular se encoge hasta el teléfono flotante"),
    nodo(41.36, 0, -15, "el teléfono vuelve"),
    # Serie (los recursos van a tiempo de la música, sin efecto)
    nodo(43.55, 1, -15, "1 POR SEMANA"),
    # Cierre
    nodo(51.30, 0, -15, "el teléfono Plan B"), nodo(51.40, 1, -16, "hoja de calendario"), flecha(51.90),
    (52.90, "page-flip.mp3", 0.64, 1.77, -16, "la hoja pasa a FEBRERO"),
    (53.26, "cinematic-riser-impact.mp3", "pk-0.05", 3.21, -9, "«febrero» tras 0,4 s de silencio: «no.» (golpe 3 de 3)"),
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


def mezclar(vI, musica, destino, work, log):
    """Una mezcla (con o sin música) de D s, normalizada a −14 LUFS. Devuelve (LUFS, pico)."""
    dv = int(round(CO * 1000))
    inputs, filt, labels = ["-i", VOZ], [], []
    gv = VOZ_OBJ - vI
    filt.append(f"[0:a]aresample=48000,aformat=channel_layouts=mono,volume={gv:.2f}dB,"
                f"acompressor=threshold=-18dB:ratio=2:attack=10:release=150:makeup=1,adelay={dv}|{dv},apad=whole_dur={D}"
                + (",asplit=2[vm][vk]" if musica else "[vm]"))
    labels.append("[vm]")
    for t, f, a, b, pk_db, note in CUES:
        path = BANCO + f
        if isinstance(a, str):
            x = pcm(path); i, _ = peak(x); a = max(0.0, i / SR + float(a[2:]))
        x = pcm(path, a, b)
        i, p = peak(x)
        lag = i / SR
        start = CO + t + 1 / FPS - lag                 # el pico cae 1 fotograma después del evento
        if "por su final" in note:
            start = CO + t - (b - a)
        gain = pk_db - 20 * math.log10(p / 32768)
        d = max(0, int(round(start * 1000)))
        inputs += ["-ss", f"{a}", "-t", f"{b - a}", "-i", path]
        k = len(labels)
        filt.append(f"[{k}:a]aresample=48000,aformat=channel_layouts=mono,afade=t=out:st={max(0, b - a - 0.04):.3f}:d=0.04,volume={gain:.2f}dB,adelay={d}|{d}[s{k}]")
        labels.append(f"[s{k}]")
        if musica:
            log.append({"tn": round(t, 3), "T": round(CO + t, 3), "archivo": f, "recorte": [round(a, 3), round(b, 3)],
                        "pico_en": round(lag, 3), "entra": round(start, 3), "pico_dbfs": pk_db, "nota": note})
    if musica:
        mI, _ = lufs(["-i", MUS])
        mg = (VOZ_OBJ - MUS_DB) - mI
        inputs += ["-i", MUS]; k = len(labels)
        env = f"volume={mg:.2f}dB,volume=-2dB:enable='between(t,{CO + DEMO[0]:.2f},{CO + DEMO[1]:.2f})'"
        for a, b, db in SUBE:
            env += f",volume={db}dB:enable='between(t,{CO + a:.2f},{CO + b:.2f})'"
        filt.append(f"[{k}:a]aresample=48000,aformat=channel_layouts=mono,{env}[mus]")
        filt.append(f"[mus][vk]sidechaincompress=threshold={DUCK['threshold']}:ratio={DUCK['ratio']}:attack={DUCK['attack']}:release={DUCK['release']}:makeup=1[musd]")
        labels.append("[musd]")
        log.append({"musica_lufs": mI, "musica_ganancia_db": round(mg, 2), "bajada_al_hablar": DUCK, "sube": SUBE})
    filt.append(f"{''.join(labels)}amix=inputs={len(labels)}:normalize=0:duration=first,atrim=0:{D}[mix]")
    crudo = os.path.join(work, "cruda_" + ("musica" if musica else "sin") + ".wav")
    r = run(["ffmpeg", "-v", "error", "-y", *inputs, "-filter_complex", ";".join(filt), "-map", "[mix]", "-ar", "48000", crudo])
    if r.returncode:
        print(r.stderr[-2500:]); sys.exit(1)
    I, _ = lufs(["-i", crudo])
    g = -14.0 - I
    for _ in range(3):
        run(["ffmpeg", "-v", "error", "-y", "-i", crudo, "-af", f"volume={g:.2f}dB,alimiter=limit=0.84:attack=2:release=60:level=disabled", "-ar", "48000", destino])
        I2, P2 = lufs(["-i", destino])
        if abs(I2 + 14) <= 0.3:
            break
        g -= (I2 + 14)
    return I2, P2


def main(src, base):
    work = os.path.join(os.path.dirname(os.path.abspath(base)), "mezcla_tmp"); os.makedirs(work, exist_ok=True)
    vI, _ = lufs(["-i", VOZ])
    log, res = [], {}
    for musica, destino in ((False, base + "_sin_musica.mp4"), (True, base + ".mp4")):
        wav = os.path.join(work, "final_v06_" + ("musica" if musica else "sin") + ".wav")
        I2, P2 = mezclar(vI, musica, wav, work, log)
        r = run(["ffmpeg", "-v", "error", "-y", "-i", src, "-i", wav, "-map", "0:v", "-map", "1:a", "-c:v", "copy", "-c:a", "aac", "-b:a", "256k", "-ac", "2", "-ar", "48000", "-shortest", destino])
        if r.returncode:
            print(r.stderr[-2500:]); sys.exit(1)
        res["con_musica" if musica else "sin_musica"] = {"lufs": I2, "pico_dbfs": P2, "archivo": os.path.basename(destino)}
        print(("con música" if musica else "sin música"), f"{I2:.1f} LUFS, pico {P2:.1f} dBFS -> {destino}")
    json.dump({"voz_lufs_original": vI, "voz_lufs_mezcla": VOZ_OBJ, "CO": CO, "D": D, "masters": res,
               "efectos": [x for x in log if "archivo" in x], "musica": [x for x in log if "musica_lufs" in x]},
              open(base + "_mezcla.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(len([x for x in log if "archivo" in x]), "efectos")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
