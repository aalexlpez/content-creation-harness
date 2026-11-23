"""Materiales de la edición de VID-0003 (ensayo 3). Solo biblioteca estándar + ffmpeg.

Uso: python preparar.py
Genera (fuera de Git):
  assets/corte.mp4          la toma de cámara cortada con KEEP, recortada del 4K (CROP) a 1080×1920 y con el color
                            «natural» (LOOK y PIEL) aplicado en un solo paso desde el original
  assets/R01.mp4, R04.mp4   recursos «sobre la cara» (cuadrados, 1080×1080) con la misma curva y temperatura (LOOK)
  assets/R02.mp4            recurso a pantalla completa (1080×1920)
  palabras.js               palabras del corte (tiempo tn) y datos del corte para index.html (window.CORTE)
  media/trabajo/voz.wav     la voz MEJORADA de Ale (audio-mejorada.wav), alineada con el vídeo y cortada con KEEP
  media/trabajo/musica.wav  la pista del banco montada por compases para los tres picos del guion

TIEMPOS. «t» = tiempo del original; «tn» = tiempo del corte (= tiempo de la composición: no hay apertura en frío).
VOZ. El audio del vídeo no se usa: la voz es el WAV mejorado, que va 25 ms por detrás del vídeo (medido por
correlación de la envolvente, 2026-11-20). Las palabras salen de Parakeet sobre ese WAV, con el inicio de cada frase
corregido al final del silencio medido (Parakeet adelanta la primera palabra de cada frase).
CORTES. Cada corte cae en un silencio real (< −55 dB en ventanas de 10 ms): se quitan las pausas largas y se dejan
0,30–0,50 s de respiración (0,65 s antes del plan, para que aparezca sin voz encima).
"""
import json
import os
import subprocess

AQUI = os.path.dirname(os.path.abspath(__file__))
VID = os.path.abspath(os.path.join(AQUI, "..", ".."))
ORIG = os.path.join(VID, "media", "originales")
TRABAJO = os.path.join(VID, "media", "trabajo")
VIDEO = os.path.join(ORIG, "1119 (2)(1).mp4")           # toma de Ale (4K vertical, 30 fps, una sola toma ya cortada en el celular)
VOZ = os.path.join(ORIG, "audio-mejorada.wav")          # voz mejorada por Ale (48 kHz)
VOZ_RETRASO = 0.025                                       # s que el WAV va por detrás del vídeo
BANCO = os.environ.get("BANCO_AUDIOS", r"C:/Users/AlexanderLopez/Documents/proyectos/referencias/banco_audios").rstrip("/\\") + "/"
PISTA = BANCO + "musica/top-flow-happy-rock.mp3"

# Tramos del original que se conservan (s). Silencios medidos: 5,17–7,30 · 11,05–13,24 · 16,73–18,27 · 22,60–23,69 ·
# 26,98–29,43 · 32,25–34,03 · 35,93–36,63 · 37,74–fin. La última palabra acaba en 37,74 y se deja 1 s de toma real.
KEEP = [(0.62, 5.47), (7.18, 11.35), (13.12, 17.03), (18.12, 22.95), (23.50, 27.48), (29.28, 32.60), (33.85, 36.25), (36.48, 38.74)]
D = round(sum(b - a for a, b in KEEP), 3)                # 29,72 s

# Recorte del 4K (2160×3840) a un plano medio: 1350×2400 desde (425, 1220), es decir 1,6×. Deja fuera el softbox
# (arriba a la izquierda) y el zócalo; la cabeza queda en el tercio superior. Margen para acercamientos hasta 1,25×.
CROP = (1350, 2400, 425, 1220)

# Color: «natural» (2026-11-20). Ale vio el look B de la serie demasiado notorio en este set (pared más violeta, piel
# naranja, negros aplastados y piel suavizada). Medido en la toma original: piel algo fría y magenta (187,155,152),
# pared lavanda (102,99,125) y camiseta casi negra (8,10,19). Corrección: curva en S muy suave con los negros apenas
# levantados, piel un poco más cálida, la pared menos violeta (selectivecolor en azules y magentas), saturación −2 % y,
# en vez de suavizar la piel, una limpieza de ruido ligera (hqdn3d) y un enfoque muy suave. Los recursos llevan la misma
# curva y temperatura. LOOK_B queda como referencia (EDICION → Color).
LOOK_B = ("curves=master='0/0.03 0.3/0.27 0.7/0.76 1/0.97',eq=gamma=1.08:saturation=1.05,"
          "colorbalance=rs=-0.05:bs=0.06:rh=0.06:bh=-0.05")
LOOK = ("curves=master='0/0.035 0.25/0.238 0.5/0.52 0.75/0.785 1/0.985',"
        "colorbalance=rm=0.035:gm=0.005:bm=-0.04:rh=0.02:bh=-0.025:bs=0.01,"
        "selectivecolor=blues='0 -0.06 0.04 0':magentas='0 -0.05 0.02 0':reds='0 0 0.03 0',eq=saturation=0.98")
PIEL_NATURAL = "hqdn3d=1.2:1.2:2:2,unsharp=5:5:0.2"
LOOK_NATURAL = LOOK
# Sin filtro (2026-11-20, Ale: «Puedes quitarle el filtro»): la toma y los recursos van con su color original, solo
# recortados y escalados. LOOK_B y LOOK_NATURAL quedan como referencia. «null» es el filtro de ffmpeg que no hace nada.
LOOK = "null"
PIEL = "null"

# Recursos: código → (tn inicio, tn fin, entrada en el clip, modo). Cortes en golpes de la música (SEG).
BROLL = {
    "R01": (1.90, 3.25, 2.55, "over"),   # «…mis metas en enero»: la hoja de enero pasa (tarjeta en el pecho)
    "R02": (5.25, 6.90, 2.00, "full"),   # «falta de ganas»: zapatillas sin usar
    "R04": (7.32, 9.02, 1.00, "over"),   # «el día en que no las tengo»: el celular sin ganas (tarjeta en el pecho)
}

# Música (145 BPM; golpes en beats_top-flow-happy-rock.json, medidos con `npx hyperframes@0.9.42 beats`).
# (inicio, fin) en la pista; None = silencio de SILENCIO s. Se encadenan desde tn 0.
SEG = [
    (2.265, 6.685),     # tn 0     → 4,42   intro mínima bajo la confesión
    (6.685, 11.645),    # tn 4,42  → 9,38   pico 1: entra la batería en «app» (3 compases)
    (12.475, 13.305),   # tn 9,38  → 10,21  relleno de 2 golpes antes del estribillo
    (13.305, 24.465),   # tn 10,21 → 21,37  estribillo en «Plan B», que sigue bajo toda la demo (27 golpes)
    # v06 (2026-11-20): antes la demo iba sobre el valle de la pista (26,5–33,2 s, ≈ 5 dB más bajo) y una subida: al
    # abrirse la app sonaba a «bajada de volumen» (Ale, en VID-0003 v07). Ahora el estribillo sigue sin bajar.
    (53.025, 57.995),   # tn 21,37 → 26,34  pico 2: estribillo 2 cuando aparece el plan (12 golpes)
    None,               # tn 26,34 → 26,81  silencio antes de «¿Y tú?»
    (66.265, 69.165),   # tn 26,81 → 29,71  pico 3: golpe en «¿Y tú?» y 7 golpes hasta el final en seco
]
SILENCIO = 0.47

# Correcciones de la transcripción (Parakeet) y silencios medidos para corregir el inicio de las frases
ARREGLOS = {("dice", 13.60): "hice", ("que", 19.36): "qué", ("Y", 35.60): "¿Y", ("tú.", 35.84): "tú?"}
SILENCIOS = [(0.0, 0.78), (3.13, 3.48), (4.21, 4.41), (5.17, 7.30), (11.05, 13.24), (14.04, 14.34), (14.95, 15.43),
             (16.73, 18.27), (19.24, 19.60), (20.67, 21.04), (22.60, 23.69), (26.98, 29.43), (32.25, 34.03),
             (35.45, 35.60), (35.93, 36.63), (37.74, 39.26)]


def ffmpeg(*args):
    subprocess.run(["ffmpeg", "-v", "error", "-y", *args], check=True)


def nuevo(t):
    acc = 0.0
    for a, b in KEEP:
        if a <= t < b:
            return acc + (t - a)
        acc += b - a
    return None


def corte(salida):
    a_, f = len(KEEP), []
    w, h, x, y = CROP
    for i, (a, b) in enumerate(KEEP):
        f.append(f"[0:v]trim={a}:{b},setpts=PTS-STARTPTS[v{i}]")
    f.append("".join(f"[v{i}]" for i in range(a_)) + f"concat=n={a_}:v=1:a=0,crop={w}:{h}:{x}:{y},"
             f"scale=1080:1920:flags=lanczos,{LOOK},{PIEL},format=yuv420p[v]")
    ffmpeg("-i", VIDEO, "-filter_complex", ";".join(f), "-map", "[v]", "-c:v", "libx264", "-crf", "10",
           "-preset", "medium", "-g", "30", "-keyint_min", "30", "-r", "30", salida)


def voz(salida):
    f, n = [], len(KEEP)
    for i, (a, b) in enumerate(KEEP):
        a2, b2 = a + VOZ_RETRASO, b + VOZ_RETRASO
        f.append(f"[0:a]atrim={a2}:{b2},asetpts=PTS-STARTPTS,afade=t=in:d=0.012,afade=t=out:st={b - a - 0.015:.3f}:d=0.015[a{i}]")
    f.append("".join(f"[a{i}]" for i in range(n)) + f"concat=n={n}:v=0:a=1,apad=whole_dur={D}[a]")
    ffmpeg("-i", VOZ, "-filter_complex", ";".join(f), "-map", "[a]", "-ar", "48000", "-c:a", "pcm_s16le", salida)


def recursos(assets):
    src = os.path.join(ORIG, "broll")
    for code, (a, b, ss, modo) in BROLL.items():
        t = b - a + 0.25
        vf = ("scale=1080:1920:force_original_aspect_ratio=increase:flags=lanczos,crop=1080:1920" if modo == "full"
              else "crop=ih:ih:(iw-ih)/2:0,scale=1080:1080:flags=lanczos")
        ffmpeg("-ss", f"{ss}", "-t", f"{t:.3f}", "-i", os.path.join(src, code + ".mp4"), "-an", "-vf",
               vf + "," + LOOK + ",fps=30,format=yuv420p", "-c:v", "libx264", "-crf", "14", "-g", "15",
               os.path.join(assets, code + ".mp4"))


def musica(salida):
    f, k, pos = [], 0, 0.0
    for s in SEG:
        if s is None:
            f.append(f"anullsrc=r=48000:cl=stereo,atrim=0:{SILENCIO}[m{k}]"); pos += SILENCIO
        else:
            a, b = s
            fi = 0.12 if k == 0 else 0.008
            f.append(f"[0:a]atrim={a}:{b},asetpts=PTS-STARTPTS,aresample=48000,afade=t=in:d={fi},"
                     f"afade=t=out:st={b - a - 0.008:.3f}:d=0.008[m{k}]")
            print(f"  música: tn {pos:6.3f}  pista {a:7.3f}–{b:7.3f}")
            pos += b - a
        k += 1
    f.append("".join(f"[m{i}]" for i in range(k)) + f"concat=n={k}:v=0:a=1,apad=whole_dur={D},atrim=0:{D},"
             f"afade=t=out:st={D - 0.025:.3f}:d=0.025[m]")
    ffmpeg("-i", PISTA, "-filter_complex", ";".join(f), "-map", "[m]", "-ar", "48000", "-c:a", "pcm_s16le", salida)


def palabras(salida):
    """palabras.js: [texto, inicio, fin] en tn, con el inicio de frase corregido y las correcciones de ARREGLOS."""
    tr = json.load(open(os.path.join(TRABAJO, "transcript.json"), encoding="utf-8"))
    tr = tr if isinstance(tr, list) else tr["words"]
    out = []
    for i, w in enumerate(tr):
        s, e = w["start"], w["end"]
        for a, b in SILENCIOS:              # una palabra no empieza dentro de un silencio medido
            if a <= s < b:
                s = b
        nx = tr[i + 1]["start"] if i + 1 < len(tr) else e
        for a, b in SILENCIOS:              # ni termina dentro del siguiente
            if a < e <= b or (s < a < e):
                e = min(e, a)
        e = max(min(e, nx), s + 0.08)
        txt = ARREGLOS.get((w["text"], round(w["start"], 2)), w["text"])
        ns, ne = nuevo(s), nuevo(min(e, s + 2) - 0.001)
        if ns is None:
            continue
        out.append([txt, round(ns, 3), round(ne if ne is not None else ns + 0.3, 3)])
    for i in range(1, len(out)):            # inicios estrictamente crecientes (dos palabras corregidas al mismo silencio)
        if out[i][1] <= out[i - 1][1]:
            out[i][1] = round(out[i - 1][1] + 0.08, 3)
            out[i - 1][2] = min(out[i - 1][2], out[i][1])
            out[i][2] = max(out[i][2], out[i][1] + 0.08)
    juntas, acc = [], 0.0
    for a, b in KEEP[:-1]:
        acc += b - a; juntas.append(round(acc, 3))
    datos = {"D": D, "juntas": juntas, "broll": {k: [v[0], v[1], v[3]] for k, v in BROLL.items()}}
    with open(salida, "w", encoding="utf-8") as f:
        f.write("// Generado por preparar.py: no editar a mano.\n")
        f.write("window.PALABRAS = " + json.dumps(out, ensure_ascii=False) + ";\n")
        f.write("window.CORTE = " + json.dumps(datos) + ";\n")
    print(f"palabras.js: {len(out)} palabras")


# Siluetas para las palabras escenario detrás de la persona (dirección v2): tramos (inicio en tn, duración) del corte.
MATES = [(0.0, 5.0, "persona_0_5.webm"), (24.9, 4.82, "persona_25_30.webm")]


def mates(assets):
    """Recorta a Ale del fondo en los tramos de MATES (npx hyperframes remove-background, modelo local en la caché). Tarda minutos."""
    for a, d, nombre in MATES:
        tmp = os.path.join(TRABAJO, f"corte_{a:g}_{d:g}.mp4")
        ffmpeg("-ss", f"{a}", "-i", os.path.join(assets, "corte.mp4"), "-t", f"{d}", "-c:v", "libx264", "-crf", "12", "-pix_fmt", "yuv420p", "-g", "30", tmp)
        r = subprocess.run(["npx", "--yes", "hyperframes@0.9.42", "remove-background", tmp, "-o", os.path.join(assets, nombre)], shell=os.name == "nt")
        if r.returncode:
            raise SystemExit(f"remove-background falló en {nombre}")


def main():
    assets = os.path.join(AQUI, "assets")
    os.makedirs(assets, exist_ok=True); os.makedirs(TRABAJO, exist_ok=True)
    palabras(os.path.join(AQUI, "palabras.js"))
    corte(os.path.join(assets, "corte.mp4"))
    voz(os.path.join(TRABAJO, "voz.wav"))
    recursos(assets)
    musica(os.path.join(TRABAJO, "musica.wav"))
    print(f"corte: {D} s")


if __name__ == "__main__":
    import sys
    if "--mates" in sys.argv:
        mates(os.path.join(AQUI, "assets"))
    else:
        main()
