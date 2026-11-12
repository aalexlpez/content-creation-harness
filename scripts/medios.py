"""Medios: inventario con SHA-256, comprobación de copias e inspección con ffprobe.

Los medios (vídeo, audio, proyectos de editor) no se versionan en Git. Su rastro sí:
`videos/VID-NNNN/MEDIOS.csv` guarda ruta, tamaño y huella de cada archivo, y permite
comprobar que una copia de seguridad está completa e intacta.
"""
from __future__ import annotations

import glob
import json
import os
import shutil
import subprocess
from fractions import Fraction
from pathlib import Path

from nucleo import CAB_MEDIOS, ErrorMarco, escribir_csv, exigir, leer_csv, sha_archivo, video_id
from reglas import carpeta_video

IGNORAR = {".DS_Store", "Thumbs.db", "desktop.ini"}


# ---------------------------------------------------------------- inventario

def _recorrer(base: Path) -> dict[str, Path]:
    salida = {}
    for ruta in sorted(base.rglob("*")):
        if ruta.is_file() and ruta.name not in IGNORAR and not ruta.name.startswith(".tmp-"):
            salida[ruta.relative_to(base).as_posix()] = ruta
    return salida


def inventariar(raiz: Path, vid: str) -> tuple[Path, int]:
    video_id(vid)
    base = carpeta_video(raiz, vid) / "media"
    exigir(base.is_dir(), f"No hay carpeta videos/{vid}/media")
    archivos = _recorrer(base)
    exigir(archivos, f"videos/{vid}/media está vacía")
    filas = [{"ruta": r, "bytes": str(p.stat().st_size), "sha256": sha_archivo(p)} for r, p in archivos.items()]
    destino = carpeta_video(raiz, vid) / "MEDIOS.csv"
    escribir_csv(destino, CAB_MEDIOS, filas)
    return destino, len(filas)


def comprobar(raiz: Path, vid: str, copia: str | None = None) -> list[str]:
    """Compara MEDIOS.csv con `media/` del vídeo o con una copia externa. Devuelve problemas."""
    video_id(vid)
    inventario = carpeta_video(raiz, vid) / "MEDIOS.csv"
    exigir(inventario.is_file(), f"Falta videos/{vid}/MEDIOS.csv; créalo con: marco.py medios {vid}")
    base = Path(copia).expanduser() if copia else carpeta_video(raiz, vid) / "media"
    exigir(base.is_dir(), f"No existe la carpeta {base}")
    esperados = {f["ruta"]: f for f in leer_csv(inventario, CAB_MEDIOS)}
    presentes = _recorrer(base)
    problemas = []
    for ruta, fila in esperados.items():
        p = presentes.get(ruta)
        if p is None:
            problemas.append(f"falta {ruta}")
        elif str(p.stat().st_size) != fila["bytes"] or sha_archivo(p) != fila["sha256"]:
            problemas.append(f"distinto {ruta}")
    for ruta in sorted(set(presentes) - set(esperados)):
        problemas.append(f"no inventariado {ruta}")
    return problemas


# ---------------------------------------------------------------- ffprobe

def localizar_ffprobe(raiz: Path, explicito: str | None = None) -> str:
    candidatos = [explicito, os.environ.get("MARCO_FFPROBE")]
    local = raiz / "marco.local.json"
    if local.is_file():
        try:
            candidatos.append(json.loads(local.read_text(encoding="utf-8-sig")).get("ffprobe"))
        except (ValueError, OSError):
            pass
    candidatos.append(shutil.which("ffprobe"))
    if os.name == "nt":
        appdata = os.environ.get("LOCALAPPDATA", "")
        for patron in (r"CapCut\Apps\*\ffprobe.exe", r"Programs\CapCut\*\ffprobe.exe"):
            candidatos += sorted(glob.glob(os.path.join(appdata, patron)), reverse=True)
    for c in candidatos:
        if c and Path(c).is_file():
            return str(c)
    raise ErrorMarco("No encuentro ffprobe. Instálalo, ponlo en el PATH o indica su ruta con --ffprobe, "
                     "la variable MARCO_FFPROBE o {\"ffprobe\": \"ruta\"} en marco.local.json")


def _ffprobe(ffprobe: str, args: list[str], segundos=60) -> str:
    try:
        r = subprocess.run([ffprobe, *args], check=True, capture_output=True, encoding="utf-8",
                           errors="replace", timeout=segundos)
    except subprocess.CalledProcessError as e:
        raise ErrorMarco(f"ffprobe falló: {e.stderr.strip()[:300]}") from None
    except subprocess.TimeoutExpired:
        raise ErrorMarco("ffprobe tardó demasiado") from None
    return r.stdout


def _fps(valor):
    try:
        return float(Fraction(valor))
    except (ZeroDivisionError, ValueError, TypeError):
        return None


def inspeccionar(raiz: Path, archivo: str, perfil: str = "entrega", audio: str = "voz",
                 ffprobe: str | None = None, cuadros: bool = False) -> dict:
    """Comprueba metadatos frente al perfil 1080x1920 · 30 fps · H.264 · SDR BT.709 · AAC 48 kHz.

    perfil 'entrega' marca FALLA lo que no cumple; 'ingesta' solo describe (AVISO).
    No sustituye ver y escuchar el archivo en el móvil.
    """
    ruta = Path(archivo).expanduser()
    exigir(ruta.is_file(), f"No existe el archivo {archivo}")
    exe = localizar_ffprobe(raiz, ffprobe)
    meta = json.loads(_ffprobe(exe, ["-v", "error", "-show_format", "-show_streams", "-of", "json", str(ruta)]))
    v = next((s for s in meta.get("streams", []) if s.get("codec_type") == "video"), None)
    a = [s for s in meta.get("streams", []) if s.get("codec_type") == "audio"]
    estricto = perfil == "entrega"
    res = {}

    def poner(nombre, ok, detalle, sin_medir=False):
        res[nombre] = {"estado": "SIN_MEDIR" if sin_medir else "OK" if ok else ("FALLA" if estricto else "AVISO"),
                       "detalle": detalle}

    if not v:
        poner("video", False, "sin pista de vídeo")
    else:
        rot = 0
        for sd in v.get("side_data_list", []) or []:
            if "rotation" in sd:
                rot = int(float(sd["rotation"])) % 360
        if not rot and "rotate" in v.get("tags", {}):
            rot = int(float(v["tags"]["rotate"])) % 360
        w, h = v.get("width"), v.get("height")
        visible = (h, w) if rot in (90, 270) else (w, h)
        poner("resolucion", visible == (1080, 1920), f"{visible[0]}x{visible[1]} (rotación {rot}°)")
        poner("codec", v.get("codec_name") == "h264", v.get("codec_name"))
        fmt = meta.get("format", {}).get("format_name", "")
        poner("contenedor", "mp4" in fmt.split(",") and ruta.suffix.lower() == ".mp4", fmt)
        media, nominal = _fps(v.get("avg_frame_rate")), _fps(v.get("r_frame_rate"))
        poner("fps", media is not None and abs(media - 30) < 0.02, f"media {media}, nominal {nominal}",
              sin_medir=media is None)
        poner("cadencia", media is not None and nominal is not None and abs(media - nominal) < 0.02,
              "CFR" if media == nominal else "posible VFR (media ≠ nominal)", sin_medir=media is None)
        color = [v.get("color_primaries"), v.get("color_transfer"), v.get("color_space")]
        desconocido = any(c in (None, "", "unknown", "unspecified") for c in color)
        poner("color", color == ["bt709"] * 3, "/".join(str(c) for c in color), sin_medir=desconocido)
        if any(c in ("smpte2084", "arib-std-b67", "bt2020") for c in color if c):
            res["color"] = {"estado": "FALLA" if estricto else "AVISO", "detalle": "HDR detectado: hace falta conversión a SDR"}
        campo = v.get("field_order")
        poner("progresivo", campo == "progressive", campo or "no declarado", sin_medir=campo in (None, "", "unknown"))
        if cuadros:
            tiempos = json.loads(_ffprobe(exe, ["-v", "error", "-select_streams", "v:0", "-show_entries",
                                                "frame=best_effort_timestamp_time", "-of", "json", str(ruta)],
                                          segundos=300)).get("frames", [])
            t = [float(f["best_effort_timestamp_time"]) for f in tiempos if "best_effort_timestamp_time" in f]
            pasos = [b - x for x, b in zip(t, t[1:])]
            if pasos:
                poner("cadencia", all(abs(p - 1 / 30) < 0.002 for p in pasos),
                      f"{len(t)} cuadros, intervalo {min(pasos):.4f}–{max(pasos):.4f} s")
    if audio == "voz":
        poner("audio", bool(a), "pista presente (escúchala)" if a else "falta pista de audio")
    elif audio == "silencio":
        poner("audio", not a, "sin pista, como se esperaba" if not a else "hay pista de audio y se esperaba silencio")
    if a:
        s = a[0]
        poner("formato_audio", s.get("codec_name") == "aac" and s.get("sample_rate") == "48000",
              f"{s.get('codec_name')} {s.get('profile', '')} {s.get('sample_rate')} Hz {s.get('channels')} canales")
    dur = meta.get("format", {}).get("duration")
    estados = {r["estado"] for r in res.values()}
    resultado = "FALLA" if "FALLA" in estados else "REVISAR" if estados & {"AVISO", "SIN_MEDIR"} else "OK"
    return {"archivo": ruta.name, "perfil": perfil, "duracion_s": round(float(dur), 2) if dur else None,
            "ffprobe": exe, "controles": res, "resultado": resultado,
            "nota": "Metadatos solo. Falta ver y escuchar el archivo completo en el móvil."}
