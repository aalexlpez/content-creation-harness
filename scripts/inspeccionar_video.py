"""Inspección local y de solo lectura. Los metadatos no sustituyen QC humano."""
import argparse
from fractions import Fraction
import json
from pathlib import Path
import shutil
import subprocess
import sys

from comun import exigir, ruta_segura

PERFIL = "SDR1080P30"
ENTRADAS = (
    "format=format_name,duration,size,bit_rate:format_tags=creation_time:"
    "stream=index,codec_type,codec_name,profile,width,height,field_order,r_frame_rate,avg_frame_rate,"
    "pix_fmt,color_space,color_transfer,color_primaries,color_range,sample_rate,channels,duration:"
    "stream_tags=rotate:stream_side_data=rotation"
)


def ejecutar(ffprobe, opciones, segundos=45):
    r = subprocess.run(
        [ffprobe, *opciones], check=True, capture_output=True, encoding="utf-8",
        errors="replace", timeout=segundos,
    )
    return r.stdout


def rotacion(pista):
    indicios = [s["rotation"] for s in pista.get("side_data_list", []) if "rotation" in s]
    if not indicios and "rotate" in pista.get("tags", {}):
        indicios = [pista["tags"]["rotate"]]
    return int(float(indicios[0])) % 360 if indicios else 0


def fps(valor):
    try:
        return float(Fraction(valor))
    except (ZeroDivisionError, ValueError, TypeError):
        return None


def analizar(ruta, ffprobe, perfil, audio, timestamps):
    ruta = ruta_segura(ruta)
    exigir(ruta.is_file(), "Archivo local no encontrado")
    version = ejecutar(ffprobe, ["-version"]).splitlines()[0]
    meta = json.loads(ejecutar(ffprobe, ["-v", "error", "-show_entries", ENTRADAS, "-of", "json", str(ruta)]))
    videos = [s for s in meta.get("streams", []) if s["codec_type"] == "video"]
    audios = [s for s in meta.get("streams", []) if s["codec_type"] == "audio"]
    controles = {}

    def check(nombre, estado, detalle):
        controles[nombre] = {"estado": estado, "detalle": detalle}

    def perfil_check(nombre, conforme, detalle):
        check(nombre, "MEDIDO" if conforme else "FALLA" if perfil else "AVISO", detalle)

    if not videos:
        check("pista_video", "FALLA", "No hay pista de vídeo")
    else:
        v = videos[0]
        ancho, alto = v.get("width"), v.get("height")
        r = rotacion(v)
        display = (alto, ancho) if r in {90, 270} else (ancho, alto)
        perfil_check("orientacion", display == (1080, 1920) and r == 0, {"px": display, "rotacion": r})
        formato = meta.get("format", {})
        perfil_check("contenedor", "mp4" in formato.get("format_name", "").split(",") and ruta.suffix.lower() == ".mp4", formato)
        perfil_check("codec_video", v.get("codec_name") == "h264", v.get("codec_name"))
        campo = v.get("field_order")
        if campo in {None, "", "unknown"}:
            check("progresivo", "SIN_MEDIR", "Orden de campo no declarado")
        else:
            perfil_check("progresivo", campo == "progressive", campo)
        tasa = fps(v.get("avg_frame_rate"))
        detalle_fps = {"promedio": tasa, "nominal": fps(v.get("r_frame_rate"))}
        if tasa is None:
            check("fps", "SIN_MEDIR", detalle_fps)
        else:
            perfil_check("fps", abs(tasa - 30) < 0.015, detalle_fps)
        color = {k: v.get(k) for k in ("color_space", "color_transfer", "color_primaries", "color_range", "pix_fmt")}
        primarios = [color[k] for k in ("color_space", "color_transfer", "color_primaries")]
        if any(x in {None, "", "unknown", "unspecified"} for x in primarios):
            check("color", "SIN_MEDIR", color)
        else:
            perfil_check("color", primarios == ["bt709"] * 3, color)
        if color["color_range"] not in {"tv", "pc"}:
            check("rango", "AVISO", "Rango no declarado. Verificar en comparación visual")
        else:
            check("rango", "MEDIDO", color["color_range"])
        if timestamps or perfil:
            frames = json.loads(ejecutar(ffprobe, [
                "-v", "error", "-select_streams", "v:0", "-show_frames", "-show_entries",
                "frame=best_effort_timestamp_time", "-of", "json", str(ruta),
            ], segundos=120)).get("frames", [])
            medidas = [float(f["best_effort_timestamp_time"]) for f in frames if "best_effort_timestamp_time" in f]
            if len(medidas) != len(frames) or len(medidas) < 2:
                check("cadencia", "SIN_MEDIR", "Faltan timestamps por cuadro")
            else:
                pasos = [b - a for a, b in zip(medidas, medidas[1:])]
                check("cadencia", "MEDIDO" if all(abs(x - 1 / 30) < 0.002 for x in pasos)
                      else "FALLA" if perfil else "AVISO",
                      {"cuadros": len(medidas), "intervalo_min": min(pasos), "intervalo_max": max(pasos)})
        else:
            check("cadencia", "SIN_MEDIR", "Usar --timestamps para inspeccionar cuadros")

    if audio == "voz":
        perfil_check("audio", bool(audios), "Pista requerida" if not audios else "Pista presente, audibilidad por revisar")
    elif audio == "silencio":
        check("audio", "MEDIDO" if not audios else "AVISO", "Silencio previsto; escuchar para verificar")
    else:
        check("audio", "MEDIDO", f"Pistas de audio: {len(audios)}")
    if audios:
        audio_info = audios[0]
        perfil_check("formato_audio", audio_info.get("codec_name") == "aac"
                     and audio_info.get("profile") == "LC" and audio_info.get("sample_rate") == "48000"
                     and audio_info.get("channels") in {1, 2}, audio_info)
    else:
        check("formato_audio", "MEDIDO" if audio == "silencio" else "SIN_MEDIR", "Sin pista")
    check("qc_humano", "SIN_MEDIR", "Audibilidad, clipping, sincronía, contraste, marca, derechos y reproducción móvil")
    estados = {x["estado"] for k, x in controles.items() if k != "qc_humano"}
    resultado = "FALLA" if "FALLA" in estados else "PENDIENTE" if "SIN_MEDIR" in estados else "CONFORME"
    return {"herramienta": version, "perfil": perfil or "INGESTA", "archivo": ruta.name, "controles": controles,
            "metadatos": meta, "resultado_metadatos": resultado}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("archivo", type=Path)
    parser.add_argument("--perfil", choices=[PERFIL])
    parser.add_argument("--audio", choices=["voz", "silencio", "indiferente"], default="indiferente")
    parser.add_argument("--timestamps", action="store_true")
    parser.add_argument("--ffprobe", help="Ruta explícita a un ffprobe local ya disponible")
    args = parser.parse_args()
    ffprobe = args.ffprobe or shutil.which("ffprobe")
    try:
        exigir(ffprobe, "ffprobe no disponible. Indica --ffprobe con un binario existente")
        if args.ffprobe:
            ffprobe = str(ruta_segura(ffprobe))
        exigir(not args.perfil or args.audio != "indiferente", "Declara --audio voz o silencio para el perfil de entrega")
        resultado = analizar(args.archivo, ffprobe, args.perfil, args.audio, args.timestamps)
        print(json.dumps(resultado, ensure_ascii=False, indent=2))
        return {"CONFORME": 0, "FALLA": 2, "PENDIENTE": 3}[resultado["resultado_metadatos"]]
    except (OSError, ValueError, subprocess.SubprocessError, IndexError, KeyError) as exc:
        print(f"SIN_MEDIR: {exc}", file=sys.stderr)
        return 3


if __name__ == "__main__":
    sys.exit(main())
