"""Medición automática del render de VID-0002 antes de enseñarlo (REVIEW §4 punto 4, PLAN_v05 §10).

Uso: python revisar.py <video.mp4> [<video_sin_musica.mp4>]
Mide sobre el MP4 ya renderizado, no sobre el código:
  - loudness integrado, rango y pico real (ebur128);
  - tiempo con la cara tapada por un inserto a pantalla completa y el inserto continuo más largo;
  - tramos del escenario sin cambio visual de más de 3 s (zona superior, 10 fotogramas por segundo);
  - nivel de la voz en cada empalme de KEEP (debe ser silencio medido, < −60 dBFS);
  - hoja de contacto de 1 fotograma por segundo y hoja a 360 px de ancho (media/trabajo/revision/).
Escribe media/trabajo/revision_<nombre>.json y un resumen en texto. Solo biblioteca estándar + ffmpeg.
"""
import array, json, math, os, re, subprocess, sys

AQUI = os.path.dirname(os.path.abspath(__file__))
VID = os.path.abspath(os.path.join(AQUI, "..", ".."))
KEEP = [(0.0, 32.60), (33.60, 49.00), (49.86, 52.20), (56.64, 60.15), (61.62, 63.25)]   # = cortes.py
FPS = 10
W, H = 108, 192            # fotogramas reducidos (1/10 de 1080×1920)
NAVY = (13, 33, 63)


def run(args, **kw):
    return subprocess.run(args, capture_output=True, **kw)


def lufs(path):
    e = run(["ffmpeg", "-hide_banner", "-nostats", "-i", path, "-vn", "-af", "ebur128=peak=true", "-f", "null", "-"], text=True, encoding="utf-8", errors="replace").stderr
    g = lambda k: float(re.findall(k + r":\s+(-?[\d.]+)", e)[-1])
    return {"lufs": g("I"), "lra": g("LRA"), "pico_dbfs": g("Peak")}


def frames(path):
    raw = run(["ffmpeg", "-v", "error", "-i", path, "-vf", f"fps={FPS},scale={W}:{H}", "-pix_fmt", "rgb24", "-f", "rawvideo", "-"]).stdout
    n = len(raw) // (W * H * 3)
    return [raw[i * W * H * 3:(i + 1) * W * H * 3] for i in range(n)]


def region_mean(fr, y0, y1):
    s = [0, 0, 0]; c = 0
    for y in range(y0, y1):
        row = fr[y * W * 3:(y + 1) * W * 3]
        for ch in range(3):
            s[ch] += sum(row[ch::3])
        c += W
    return tuple(v / c for v in s)


def diff(a, b, y0, y1):
    ra, rb = a[y0 * W * 3:y1 * W * 3], b[y0 * W * 3:y1 * W * 3]
    return sum(abs(x - y) for x, y in zip(ra[::7], rb[::7])) / len(ra[::7])


def voz_en_empalmes():
    wav = os.path.join(VID, "media", "trabajo", "voz_v05.wav")
    if not os.path.exists(wav):
        return []
    acc, out = 0.0, []
    for i, (a, b) in enumerate(KEEP[:-1]):
        acc += b - a
        raw = run(["ffmpeg", "-v", "error", "-ss", f"{acc - 0.03:.3f}", "-t", "0.06", "-i", wav, "-ac", "1", "-f", "s16le", "-"]).stdout
        x = array.array("h"); x.frombytes(raw[: len(raw) // 2 * 2])
        pk = max((abs(v) for v in x), default=0)
        out.append({"empalme_s": round(acc, 2), "pico_dbfs": round(20 * math.log10(pk / 32768), 1) if pk else -120.0})
    return out


def main(video, sin_musica=None):
    nombre = os.path.splitext(os.path.basename(video))[0]
    res = {"video": video, "sonido": lufs(video)}
    if sin_musica:
        res["sonido_sin_musica"] = lufs(sin_musica)
    dur = float(run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", video], text=True).stdout.strip())
    fr = frames(video)
    n = len(fr)
    estado = []                      # 'E' escenario, 'I' inserto a pantalla completa, 'C' a cámara
    for f in fr:
        top = region_mean(f, 0, 30)
        full = region_mean(f, 0, H)
        navy = all(abs(top[i] - NAVY[i]) < 22 for i in range(3))
        luz = full[0] > 175 and full[1] > 175 and full[2] > 165     # maqueta clara a pantalla completa
        oscuro = full[0] < 45 and full[1] < 45 and full[2] < 55    # pantalla de bloqueo a pantalla completa
        estado.append("I" if (luz or oscuro) else "E" if navy else "C")
    tapada = estado.count("I") / n
    largo = cur = 0
    for e in estado:
        cur = cur + 1 if e == "I" else 0
        largo = max(largo, cur)
    # tramos del escenario sin cambio: diferencia media entre fotogramas en la mitad superior
    quietos, ini = [], None
    for i in range(1, n):
        if estado[i] == "E":
            mov = diff(fr[i - 1], fr[i], 0, 100)
            if mov < 0.9:
                ini = i - 1 if ini is None else ini
            else:
                if ini is not None and (i - ini) / FPS > 3.0:
                    quietos.append((round(ini / FPS, 1), round(i / FPS, 1)))
                ini = None
        else:
            if ini is not None and (i - ini) / FPS > 3.0:
                quietos.append((round(ini / FPS, 1), round(i / FPS, 1)))
            ini = None
    res.update({"duracion_s": round(dur, 2),
                "cara_tapada_pct": round(100 * tapada, 1), "inserto_continuo_max_s": round(largo / FPS, 1),
                "escenario_pct": round(100 * estado.count("E") / n, 1),
                "escenario_sin_cambio_mas_de_3s": quietos, "voz_en_empalmes": voz_en_empalmes()})
    out = os.path.join(VID, "media", "trabajo", "revision"); os.makedirs(out, exist_ok=True)
    run(["ffmpeg", "-v", "error", "-y", "-i", video, "-vf", "fps=1,scale=135:240,tile=10x6", "-frames:v", "1", os.path.join(out, nombre + "_hoja_1fps.jpg")])
    run(["ffmpeg", "-v", "error", "-y", "-ss", "1", "-i", video, "-vf", "fps=1/6,scale=360:640,tile=5x2", "-frames:v", "1", os.path.join(out, nombre + "_hoja_360px.jpg")])
    json.dump(res, open(os.path.join(VID, "media", "trabajo", f"revision_{nombre}.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    s = res["sonido"]
    print(f"{nombre}: {dur:.2f} s · {s['lufs']:.1f} LUFS, LRA {s['lra']:.1f}, pico {s['pico_dbfs']:.1f} dBFS")
    print(f"  escenario {res['escenario_pct']} % · cara tapada {res['cara_tapada_pct']} % · inserto continuo más largo {res['inserto_continuo_max_s']} s")
    print(f"  escenario sin cambio > 3 s: {quietos or 'ninguno'}")
    print("  voz en los empalmes: " + ", ".join(f"{e['empalme_s']} s → {e['pico_dbfs']} dBFS" for e in res["voz_en_empalmes"]))


if __name__ == "__main__":
    main(*sys.argv[1:3])
