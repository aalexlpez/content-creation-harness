"""Alta independiente de semana o vídeo en borrador."""
import argparse
import re
import sys

from comun import (
    DOCS_VIDEO, IDEA, IDEAS_CSV, PROYECTO, ROOT, VIDEO, bajo, campos, crear_directorio, csv_filas,
    exigir, identificador, leer_md, semana_iso,
)


def plantilla(raiz, nombre, valores):
    ruta = bajo(raiz, f"templates/{nombre}")
    exigir(ruta.is_file(), f"Falta plantilla: {nombre}")
    texto = ruta.read_text(encoding="utf-8-sig")
    for clave, valor in valores.items():
        texto = texto.replace("{{" + clave + "}}", valor)
    exigir(not re.search(r"\{\{[^{}\n]+\}\}", texto), f"Marcadores sin resolver en {nombre}")
    return texto


def crear_semana(raiz, semana):
    semana_iso(semana)
    destino = bajo(raiz, f"semanas/{semana}")
    texto = plantilla(raiz, "SEMANA.md", {"SEMANA": semana, "LOTE": ""})
    crear_directorio(destino, {"SEMANA.md": texto})
    return destino


def crear_video(raiz, semana, video, proyecto, idea, modo):
    semana_iso(semana)
    identificador(video, VIDEO, "Vídeo")
    identificador(proyecto, PROYECTO, "Proyecto")
    identificador(idea, IDEA, "Idea")
    exigir(modo in {"INTERNO", "FIXTURE"}, f"Modo inválido: {modo}")
    leer_md(bajo(raiz, f"semanas/{semana}/SEMANA.md"))
    ficha = leer_md(bajo(raiz, f"proyectos/{proyecto}/PROYECTO.md"))
    control = campos(ficha, "Control")
    exigir(control.get("Proyecto") == proyecto and control.get("Creador") == "Alexander", "Ficha de proyecto inconsistente")
    ideas = [f for f in csv_filas(bajo(raiz, "registro/IDEAS.csv"), IDEAS_CSV) if f["idea_id"] == idea]
    exigir(len(ideas) == 1 and ideas[0]["proyecto_id"] == proyecto, f"Idea no registrada para {proyecto}: {idea}")
    destino = bajo(raiz, f"videos/{video}")
    valores = {"VIDEO": video, "PROYECTO": proyecto, "IDEA": idea, "MODO": modo}
    textos = {nombre: plantilla(raiz, nombre, valores) for nombre in DOCS_VIDEO}
    crear_directorio(destino, textos)
    return destino


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="accion", required=True)
    alta_semana = sub.add_parser("semana")
    alta_semana.add_argument("semana")
    alta_video = sub.add_parser("video")
    for nombre in ("semana", "video", "proyecto", "idea"):
        alta_video.add_argument(nombre)
    alta_video.add_argument("--fixture", action="store_true")
    args = parser.parse_args()
    try:
        if args.accion == "semana":
            salida = crear_semana(ROOT, args.semana)
        else:
            modo = "FIXTURE" if args.fixture else "INTERNO"
            salida = crear_video(ROOT, args.semana, args.video, args.proyecto, args.idea, modo)
        print(f"BORRADOR: {salida}")
    except (OSError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
