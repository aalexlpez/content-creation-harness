"""Cortes de la edición continua de VID-0002 (ensayo 2) sobre el corte v01 de Ale (63,25 s).

Uso: python cortes.py
Genera, en assets/ (fuera de Git):
  - corte_v05.mp4: imagen de media/originales/ensayo_2.mp4, SIN audio, solo con los tramos de KEEP y
    una cola de COLA s con el último fotograma (el vídeo acaba sobre la música, plan v05 §3);
  - demo_v05.mp4: MG-06 (v04) y MG-07 (v04) con los mismos cortes en su tiempo local;
  - media/trabajo/voz_v05.wav: la voz mejorada de Ale (WAV, media/trabajo/audio_mejora/) cortada con los
    mismos KEEP, con crossfades de 12–15 ms y la cola en silencio. La mezcla parte de este archivo.
v05 (2026-11-18): la voz ya no viaja dentro del vídeo (AAC): se mantiene en WAV hasta la mezcla.

Regla (2026-11-18): cada corte cae en un silencio real de la voz (< −60 dB medido en ventanas
de 10 ms) y, si es posible, en final de frase. Nunca en mitad de una frase que sigue.
KEEP se comparte con index.html y mezcla.py: si cambia aquí, se cambia en los tres.
Solo biblioteca estándar + ffmpeg.
"""
import os
import subprocess

AQUI = os.path.dirname(os.path.abspath(__file__))
VID = os.path.abspath(os.path.join(AQUI, "..", ".."))

# Tramos del corte v01 que se conservan (s). Medidos sobre la voz mejorada:
#   32,60 | 33,60  «armas un plan.» … silencio … (fuera «¿Como cuál?») … «Si llego»
#   49,00 | 49,86  «ciencia,» … silencio … (fuera «eh,») … «minijuegos»
#   52,20 | 56,64  «cualquier ámbito.» … (fuera «Y que pues sean libres y gratis…») … «Así que»
#   60,15 | 61,62  «…llegue febrero.» … (fuera «Y me dices qué tal.») … «El link»
KEEP = [(0.0, 32.60), (33.60, 49.00), (49.86, 52.20), (56.64, 60.15), (61.62, 63.25)]
COLA = 1.0   # s de último fotograma tras la última palabra
VOZ = "ensayo_2_voz_original-mejorada-v2.wav"
DEMO0, MG7_0, MG6_D, MG7_D = 22.70, 37.12, 14.42, 5.18   # dónde empiezan MG-06 y MG-07 en el corte v01


def ffmpeg(*args):
    subprocess.run(["ffmpeg", "-v", "error", "-y", *args], check=True)


def cortar(video, audio, salida, tramos, cola=0.0):
    f, n = [], len(tramos)
    for i, (a, b) in enumerate(tramos):
        f.append(f"[0:v]trim={a}:{b},setpts=PTS-STARTPTS[v{i}]")
        if audio:
            f.append(f"[1:a]atrim={a}:{b},asetpts=PTS-STARTPTS,afade=t=in:d=0.012,afade=t=out:st={b - a - 0.015:.3f}:d=0.015[a{i}]")
    if audio:
        f.append("".join(f"[v{i}][a{i}]" for i in range(n)) + f"concat=n={n}:v=1:a=1[v][a]")
        mapa = ["-map", "[v]", "-map", "[a]", "-c:a", "aac", "-b:a", "256k", "-ar", "48000"]
    else:
        f.append("".join(f"[v{i}]" for i in range(n)) + f"concat=n={n}:v=1:a=0" + (f",tpad=stop_mode=clone:stop_duration={cola}" if cola else "") + "[v]")
        mapa = ["-map", "[v]"]
    entradas = ["-i", video] + (["-i", audio] if audio else [])
    ffmpeg(*entradas, "-filter_complex", ";".join(f), *mapa,
           "-c:v", "libx264", "-crf", "12", "-preset", "medium", "-pix_fmt", "yuv420p", "-g", "30", "-keyint_min", "30", "-r", "30", salida)


def local(tramos, ini, dur):
    """Tramos de KEEP que caen dentro de [ini, ini+dur), en tiempo local de la pieza."""
    out = []
    for a, b in tramos:
        a2, b2 = max(a, ini), min(b, ini + dur)
        if b2 > a2:
            out.append((round(a2 - ini, 3), round(b2 - ini, 3)))
    return out


def voz(salida, tramos, cola):
    """Voz mejorada cortada con los mismos tramos (WAV 16 bits, 48 kHz, estéreo) + cola en silencio."""
    src = os.path.join(VID, "media", "trabajo", "audio_mejora", VOZ)
    f, n = [], len(tramos)
    for i, (a, b) in enumerate(tramos):
        f.append(f"[0:a]atrim={a}:{b},asetpts=PTS-STARTPTS,afade=t=in:d=0.012,afade=t=out:st={b - a - 0.015:.3f}:d=0.015[a{i}]")
    f.append("".join(f"[a{i}]" for i in range(n)) + f"concat=n={n}:v=0:a=1,apad=pad_dur={cola}[a]")
    ffmpeg("-i", src, "-filter_complex", ";".join(f), "-map", "[a]", "-ar", "48000", "-c:a", "pcm_s16le", salida)


def main():
    assets = os.path.join(AQUI, "assets")
    cortar(os.path.join(VID, "media", "originales", "ensayo_2.mp4"), None,
           os.path.join(assets, "corte_v05.mp4"), KEEP, COLA)
    voz(os.path.join(VID, "media", "trabajo", "voz_v05.wav"), KEEP, COLA)
    d6, d7 = os.path.join(assets, "_d6.mp4"), os.path.join(assets, "_d7.mp4")
    cortar(os.path.join(assets, "MG-06_v04.mp4"), None, d6, local(KEEP, DEMO0, MG6_D))
    cortar(os.path.join(assets, "MG-07_v04.mp4"), None, d7, local(KEEP, MG7_0, MG7_D))
    ffmpeg("-i", d6, "-i", d7, "-filter_complex", "[0:v][1:v]concat=n=2:v=1:a=0[v]", "-map", "[v]",
           "-c:v", "libx264", "-crf", "12", "-pix_fmt", "yuv420p", "-g", "30", "-keyint_min", "30", "-r", "30", os.path.join(assets, "demo_v05.mp4"))
    os.remove(d6); os.remove(d7)
    total = sum(b - a for a, b in KEEP)
    demo = sum(b - a for a, b in local(KEEP, DEMO0, MG6_D)) + sum(b - a for a, b in local(KEEP, MG7_0, MG7_D))
    print(f"corte_v05: {total:.2f} s + cola {COLA} s · demo_v05: {demo:.2f} s")


if __name__ == "__main__":
    main()
