"""Materiales de la edición v06 de VID-0002 (plan: edicion/PLAN_v06.md). Solo biblioteca estándar + ffmpeg.

Uso: python preparar.py
Genera (fuera de Git):
  assets/corte_v06.mp4     imagen del corte (KEEP de edicion/cortes.py) con COLA s de último fotograma
  assets/demo_v06.mp4      la demo (MG-06 + MG-07 v04) con los mismos cortes (copia de edicion/assets/demo_v05.mp4)
  assets/R0x.mp4           cada recurso (B-roll) recortado a su tramo, a 30 fps:
                             «full»  → 1080×1920 a pantalla completa (vertical, u horizontal en 4K recortado al centro)
                             «card»  → 1080×1080 del centro (horizontal en 1080: va como tarjeta, sin ampliar)
  media/trabajo/voz_v06.wav     voz mejorada cortada con KEEP (WAV si está; si no, el MP3 con el mismo contenido)
  media/trabajo/musica_v06.wav  la pista elegida, editada por compases y colocada en el tiempo de la composición

TIEMPOS. «tn» = tiempo del corte (la voz). CO = 0: la composición empieza con la voz (T = tn).
  Corrección de Ale (2026-11-19): fuera la apertura en frío de 1,24 s («no hay contexto»); los recursos del gancho y
  del problema pasan de 3 a 4 golpes (≈ 1,65 s) para que se entienda la relación entre imagen y frase.
MÚSICA. Golpes medidos con `npx hyperframes@0.9.42 beats` (145 BPM, 0,414 s por golpe, compás de 4 golpes).
  Estructura de la pista: intro suave 0–6,7 · batería 6,7–13,3 · estribillo 13,3–24,9 · valle 26,5–39,8 ·
  subida 39,8–53,0 · estribillo 2 53,0–64,6 · … · final 76,6.
  Se monta por tramos (SEG) para que los cambios caigan donde manda la voz (EDICION → Música):
    tn 0     intro mínima en el gancho (golpe en 0,075)
    tn 4,625 entra la batería en «Pero…» (2 compases + los 4 de la sección: 6 compases)
    tn 14,555 estribillo en «Plan B»
    tn 22,835 valle (con un golpe de anacrusa) en la entrada de la demo
    tn 36,495 estribillo 2 en el sello («Este febrero, no.» en la maqueta, 36,54)
    tn 49,735 subida (2 compases) en «cualquier ámbito…»
    tn 52,86  silencio de 0,4 s
    tn 53,26  golpe en «febrero» y 8 golpes hasta el final en seco (tn 56,58)
"""
import os
import shutil
import subprocess
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
HF = os.path.dirname(AQUI)
VID = os.path.dirname(HF)
sys.path.insert(0, os.path.join(HF, "edicion"))
import cortes  # noqa: E402  (KEEP, cortar, local)

KEEP = cortes.KEEP
COLA = 1.20                         # el vídeo acaba en tn 56,58: el corte necesita ≥ 1,10 s de cola
CO = 0.0                            # sin apertura en frío (era 1,165 s en la primera v06)
FIN_TN = 56.58                      # final en seco (golpe 8 tras «febrero»)
D = round(CO + FIN_TN, 3)           # duración de la composición
BANCO = os.environ.get("BANCO_AUDIOS", r"C:/Users/AlexanderLopez/Documents/proyectos/referencias/banco_audios").rstrip("/\\") + "/"
PISTA = BANCO + "musica/top-flow-happy-rock.mp3"

# Recursos: código → (archivo, entrada en el clip s, duración en pantalla s, modo). Tramos en tn (= composición − CO).
BROLL = {
    "R01": (0.000, 1.325, 2.55, "card"),    # «Es febrero»: la mano pasa la hoja de enero a febrero (abre el vídeo)
    "R02": (1.325, 2.985, 2.00, "full"),    # «abandonaste tu propósito de año nuevo»: zapatillas sin usar (4K)
    "R03": (6.695, 8.345, 0.50, "full"),    # «hemos tirado la toalla»: rendida en un banco (vertical 4K)
    "R04": (9.175, 10.835, 1.00, "card"),   # «no piensa en qué va a hacer»: el celular sin ganas
    "R07": (45.600, 46.840, 0.00, "full"),  # «productividad»: escritorio desde arriba (4K)
    "R08": (46.840, 48.075, 1.00, "card"),  # «ciencia»: microscopio
    "R09": (48.075, 49.315, 5.50, "full"),  # «minijuegos»: manos con mandos (vertical 4K)
}

# Música: (inicio en la pista, fin en la pista); se encadenan desde T = 0. None = silencio de esa duración.
SEG = [
    (2.060, 6.685),     # tn 0 → 4,625      intro (el golpe de 2,135 cae en tn 0,075)
    (6.685, 9.995),     # tn 4,625 → 7,935  batería (2 compases)
    (6.685, 13.305),    # tn 7,935 → 14,555 batería (4 compases)
    (13.305, 21.585),   # tn 14,555 → 22,835 estribillo (5 compases)
    (26.125, 39.785),   # tn 22,835 → 36,495 valle (anacrusa + 8 compases)
    (53.025, 66.265),   # tn 36,495 → 49,735 estribillo 2 (8 compases)
    (49.715, 52.840),   # tn 49,735 → 52,86  subida (corta antes del golpe)
    None,               # tn 52,86 → 53,26  silencio
    (53.025, 56.345),   # tn 53,26 → 56,58  golpe en «febrero» y 8 golpes
]
SILENCIO = 0.40

# Color: look B «cálido cinematográfico», elegido por Ale el 2026-11-19 entre tres looks (revision_v06/looks_color.png).
# Curva en S suave, sombras frías y luces cálidas, y piel suavizada respetando bordes (barba, gafas y ojos nítidos).
# La viñeta la pone la composición (#vig). Los recursos llevan la misma temperatura y curva, sin suavizado de piel.
LOOK_B = ("curves=master='0/0.03 0.3/0.27 0.7/0.76 1/0.97',eq=gamma=1.08:saturation=1.05,"
          "colorbalance=rs=-0.05:bs=0.06:rh=0.06:bh=-0.05")
PIEL = "bilateral=sigmaS=3:sigmaR=0.05,unsharp=5:5:0.45"


def ffmpeg(*args):
    subprocess.run(["ffmpeg", "-v", "error", "-y", *args], check=True)


def dur(p):
    return float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", p],
                                capture_output=True, text=True).stdout.strip())


def recursos(assets):
    src = os.path.join(VID, "media", "originales", "broll")
    for code, (a, b, ss, modo) in BROLL.items():
        p = os.path.join(src, code + ".mp4")
        t = b - a + 0.25                                   # margen por si el render pide un fotograma más
        if modo == "full":
            vf = "scale=1080:1920:force_original_aspect_ratio=increase:flags=lanczos,crop=1080:1920"
        else:
            vf = "crop=ih:ih:(iw-ih)/2:0,scale=1080:1080:flags=lanczos"
        ffmpeg("-ss", f"{ss}", "-t", f"{t:.3f}", "-i", p, "-an", "-vf", vf + "," + LOOK_B + ",fps=30,format=yuv420p",
               "-c:v", "libx264", "-crf", "14", "-preset", "medium", "-g", "15", os.path.join(assets, code + ".mp4"))
        print(f"{code}: {modo}, clip {ss:.2f}+{t:.2f} s, tn {a:.3f}–{b:.3f}")


def voz(salida):
    """La voz mejorada cortada con KEEP, con la cola en silencio (WAV 48 kHz)."""
    wav = os.path.join(VID, "media", "trabajo", "audio_mejora", cortes.VOZ)
    src = wav if os.path.exists(wav) else os.path.join(VID, "media", "trabajo", "voz_mejorada_v2.mp3")
    f, n = [], len(KEEP)
    for i, (a, b) in enumerate(KEEP):
        f.append(f"[0:a]atrim={a}:{b},asetpts=PTS-STARTPTS,afade=t=in:d=0.012,afade=t=out:st={b - a - 0.015:.3f}:d=0.015[a{i}]")
    f.append("".join(f"[a{i}]" for i in range(n)) + f"concat=n={n}:v=0:a=1,apad=pad_dur={COLA}[a]")
    ffmpeg("-i", src, "-filter_complex", ";".join(f), "-map", "[a]", "-ar", "48000", "-c:a", "pcm_s16le", salida)
    print("voz:", os.path.basename(src))


def musica(salida):
    """Encadena los tramos de SEG con fundidos de 8 ms en los empalmes (caen en golpes) y corta en seco al final."""
    f, k, pos, marcas = [], 0, 0.0, []
    for s in SEG:
        if s is None:
            f.append(f"anullsrc=r=48000:cl=stereo,atrim=0:{SILENCIO}[m{k}]"); pos += SILENCIO
        else:
            a, b = s
            fi = 0.12 if k == 0 else 0.008                    # la primera entra con un fundido corto
            f.append(f"[0:a]atrim={a}:{b},asetpts=PTS-STARTPTS,aresample=48000,afade=t=in:d={fi},afade=t=out:st={b - a - 0.008:.3f}:d=0.008[m{k}]")
            marcas.append((round(pos, 3), round(pos - CO, 3), a, b)); pos += b - a
        k += 1
    f.append("".join(f"[m{i}]" for i in range(k)) + f"concat=n={k}:v=0:a=1,atrim=0:{D},afade=t=out:st={D - 0.025:.3f}:d=0.025[m]")
    ffmpeg("-i", PISTA, "-filter_complex", ";".join(f), "-map", "[m]", "-ar", "48000", "-c:a", "pcm_s16le", salida)
    for T, tn, a, b in marcas:
        print(f"  música: T {T:6.3f} (tn {tn:6.3f})  pista {a:6.3f}–{b:6.3f}")
    print(f"música: {pos:.3f} s (composición {D} s)")


def main():
    assets = os.path.join(AQUI, "assets")
    trabajo = os.path.join(VID, "media", "trabajo")
    crudo = os.path.join(assets, "_corte_sin_color.mp4")
    cortes.cortar(os.path.join(VID, "media", "originales", "ensayo_2.mp4"), None, crudo, KEEP, COLA)
    ffmpeg("-i", crudo, "-vf", f"{LOOK_B},{PIEL},format=yuv420p", "-c:v", "libx264", "-crf", "10", "-preset", "medium",
           "-g", "30", "-keyint_min", "30", "-r", "30", os.path.join(assets, "corte_v06.mp4"))
    os.remove(crudo)
    shutil.copyfile(os.path.join(HF, "edicion", "assets", "demo_v05.mp4"), os.path.join(assets, "demo_v06.mp4"))
    recursos(assets)
    voz(os.path.join(trabajo, "voz_v06.wav"))
    musica(os.path.join(trabajo, "musica_v06.wav"))
    print(f"corte_v06: {dur(os.path.join(assets, 'corte_v06.mp4')):.3f} s · CO {CO} · D {D}")


if __name__ == "__main__":
    main()
