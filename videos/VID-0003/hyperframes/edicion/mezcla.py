"""Mezcla de VID-0003. Dos másteres (AV-012, propuesta): sin música y con música.

Uso: python mezcla.py <video_sin_sonido.mp4> <salida_base>
  <salida_base>_sin_musica.mp4  voz + efectos (para poner el sonido de tendencia dentro de cada app)
  <salida_base>.mp4             voz + efectos + música montada por compases (media/trabajo/musica.wav, de preparar.py)
  <salida_base>_mezcla.json     registro de efectos y niveles

Receta (la de VID-0002 v06f, MOTION §6):
  - Voz: la voz MEJORADA de Ale (media/trabajo/voz.wav), subida a −17,4 LUFS antes de mezclar (los picos de los
    efectos están calibrados contra ese nivel) y con una compresión suave.
  - Efectos reales del banco de Pixabay de Ale (AV-008, AV-011): cada uno recortado a su tramo audible y con el pico
    1 fotograma después del evento. Pocos: un toque por cada toque real de la app, un sonido por tarjeta y los tres
    golpes de los picos. Los cortes de los recursos van a tiempo de la música y no llevan efecto.
  - Música 13 dB bajo la voz, baja ≈ 5 dB cuando hablas (sidechaincompress), 2 dB menos en la demo y +4 dB en la
    cola sin voz. Mezcla final a −14 LUFS con limitador (pico ≤ −1 dBFS).
Solo biblioteca estándar + ffmpeg.
"""
import array, json, math, os, re, subprocess, sys

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import preparar  # noqa: E402  (D, BANCO, rutas)

BANCO = preparar.BANCO
VOZ = os.path.join(preparar.TRABAJO, "voz.wav")
MUS = os.path.join(preparar.TRABAJO, "musica.wav")
D = preparar.D
FPS, SR = 30.0, 48000
VOZ_OBJ = -17.4
MUS_DB = 13.0
DUCK = dict(threshold=0.04, ratio=4, attack=60, release=350)
DEMO = (12.93, 25.06)               # tn: música −2 dB
SUBE = [(21.27, 21.88, 4.0), (28.80, 40.0, 4.0)]   # tn: sin voz, la música sube: el plan (pico 2) y la cola

TAP = ("screen-tap.mp3", 0.40, 0.70)
POP = ("pop.mp3", 0.19, 0.31)
BUB = ("pop-universfield-bubble.mp3", 0.0, 0.18)
LAPIZ = ("pencil_scribble_short.mp3", 0.0, 0.29)
def toque(t, db, nota):
    return (t, TAP[0], TAP[1], TAP[2], db, nota)
def nodo(t, k, db, nota):
    f = POP if k == 0 else BUB
    return (t, f[0], f[1], f[2], db, nota)
def flecha(t, db=-21):
    return (t, LAPIZ[0], LAPIZ[1], LAPIZ[2], db, "flecha que se dibuja")

# (tn, archivo, recorte inicio, recorte fin, pico objetivo dBFS, nota). «pk-0.05» = empieza 0,05 s antes del pico.
CUES = [
    # S01 · confesión
    nodo(0.42, 1, -19, "promesa en pantalla"),
    (2.35, "page-turn.mp3", 0.0, 0.55, -18, "R01: la hoja de enero pasa"),
    nodo(3.79, 0, -17, "HICE"),
    nodo(4.10, 0, -16, "UNA"),
    (4.42, "cinematic-impact-boom.mp3", 0.0, 1.92, -15, "pico 1: «APP» y entra la batería (golpe 1 de 3)"),
    (4.42, "whoosh_fast-simple-chop.mp3", 0.0, 0.55, -19, "el teléfono Plan B entra"),
    # S02 · el motivo
    nodo(7.32, 1, -17, "R04: tarjeta en el pecho"),
    # S03 · Plan B
    nodo(9.14, 0, -16, "etiqueta cerobytes"), flecha(9.55),
    (10.20, "click-photos.mp3", 0.0, 0.84, -16, "«Plan B» llena el cuadro (estribillo)"),
    nodo(10.62, 1, -17, "MINIAPP 01"),
    (11.30, "scribble-pencil.mp3", 0.3, 0.75, -18, "precio tachado"),
    nodo(11.45, 1, -14, "GRATIS"),
    (12.62, "whoosh_largo_misterioso.mp3", 0.47, 1.71, -16, "el teléfono flotante se convierte en el celular de la demo"),
    # S04–S06 · demo de la app real: solo 4 toques con sonido (meta, «No tuve tiempo», «Ver mi plan», recordatorio);
    # 10 toques en 12 s sonaban a clics sin parar (autocrítica de la v02)
    toque(13.55, -13, "«Hacer ejercicio»"),
    (14.15, "page-turn.mp3", 0.0, 0.55, -20, "la app te lleva a febrero"),
    toque(14.95, -11, "«No tuve tiempo»"),
    (17.95, "iphone_typing.mp3", 2.58, 3.98, -21, "tecleo «llego a casa después de las 20:00»"),
    (19.75, "iphone_typing.mp3", 5.19, 6.39, -21, "tecleo «hago 5 minutos de estiramientos»"),
    toque(21.15, -13, "«Ver mi plan»"),
    (21.34, "tension-riser.mp3", 1.78, 2.98, -19, "tensión antes del plan (se coloca por su final)"),
    (21.37, "office-stamp-varios-veces.mp3", 0.0, 0.66, -10, "pico 2: aparece el plan con el estribillo 2 (golpe 2 de 3)"),
    toque(22.40, -14, "«Añadir recordatorio»"),
    (22.90, "new-notification.mp3", 0.0, 1.38, -17, "hora 20:00: el recordatorio"),
    (23.40, "whoosh_basico.mp3", 0.0, 0.58, -19, "baja hasta el fondo de pantalla"),
    (24.75, "whoosh_fast-simple-chop.mp3", 0.0, 0.55, -17, "el celular se encoge hasta el teléfono flotante"),
    nodo(25.12, 0, -16, "el teléfono vuelve"),
    # S07 · cierre
    nodo(25.25, 1, -17, "hoja de calendario"), flecha(25.55),
    (26.30, "page-flip.mp3", 0.64, 1.77, -17, "la hoja pasa a FEBRERO"),
    (26.81, "cinematic-riser-impact.mp3", "pk-0.05", 3.21, -10, "pico 3: «¿Y tú?» tras 0,47 s de silencio de la música (golpe 3 de 3)"),
    nodo(27.85, 0, -15, "«sí.» del acento final"),
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
    inputs, filt, labels = ["-i", VOZ], [], []
    gv = VOZ_OBJ - vI
    filt.append(f"[0:a]aresample=48000,aformat=channel_layouts=mono,volume={gv:.2f}dB,"
                f"acompressor=threshold=-18dB:ratio=2:attack=10:release=150:makeup=1,apad=whole_dur={D}"
                + (",asplit=2[vm][vk]" if musica else "[vm]"))
    labels.append("[vm]")
    for t, f, a, b, pk_db, note in CUES:
        path = BANCO + f
        if isinstance(a, str):
            x = pcm(path); i, _ = peak(x); a = max(0.0, i / SR + float(a[2:]))
        x = pcm(path, a, b)
        i, p = peak(x)
        lag = i / SR
        start = t + 1 / FPS - lag
        if "por su final" in note:
            start = t - (b - a)
        gain = pk_db - 20 * math.log10(p / 32768)
        d = max(0, int(round(start * 1000)))
        inputs += ["-ss", f"{a}", "-t", f"{b - a}", "-i", path]
        k = len(labels)
        filt.append(f"[{k}:a]aresample=48000,aformat=channel_layouts=mono,afade=t=out:st={max(0, b - a - 0.04):.3f}:d=0.04,volume={gain:.2f}dB,adelay={d}|{d}[s{k}]")
        labels.append(f"[s{k}]")
        if musica:
            log.append({"tn": round(t, 3), "archivo": f, "recorte": [round(a, 3), round(b, 3)], "pico_en": round(lag, 3),
                        "entra": round(start, 3), "pico_dbfs": pk_db, "nota": note})
    if musica:
        mI, _ = lufs(["-i", MUS])
        mg = (VOZ_OBJ - MUS_DB) - mI
        inputs += ["-i", MUS]; k = len(labels)
        env = f"volume={mg:.2f}dB,volume=-2dB:enable='between(t,{DEMO[0]:.2f},{DEMO[1]:.2f})'"
        for a, b, db in SUBE:
            env += f",volume={db}dB:enable='between(t,{a:.2f},{b:.2f})'"
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
        wav = os.path.join(work, "final_" + ("musica" if musica else "sin") + ".wav")
        I2, P2 = mezclar(vI, musica, wav, work, log)
        r = run(["ffmpeg", "-v", "error", "-y", "-i", src, "-i", wav, "-map", "0:v", "-map", "1:a", "-c:v", "copy", "-c:a", "aac", "-b:a", "256k", "-ac", "2", "-ar", "48000", "-shortest", destino])
        if r.returncode:
            print(r.stderr[-2500:]); sys.exit(1)
        res["con_musica" if musica else "sin_musica"] = {"lufs": I2, "pico_dbfs": P2, "archivo": os.path.basename(destino)}
        print(("con música" if musica else "sin música"), f"{I2:.1f} LUFS, pico {P2:.1f} dBFS -> {destino}")
    json.dump({"voz_lufs_original": vI, "voz_lufs_mezcla": VOZ_OBJ, "D": D, "masters": res,
               "efectos": [x for x in log if "archivo" in x], "musica": [x for x in log if "musica_lufs" in x]},
              open(base + "_mezcla.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(len([x for x in log if "archivo" in x]), "efectos")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
