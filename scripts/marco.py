"""marco.py — línea de comandos del marco de contenido de Alexander.

Uso rápido (desde cualquier carpeta):
  python scripts/marco.py estado                     tablero: semanas, vídeos y qué falta
  python scripts/marco.py idea miminiapp "Título" --problema "..."
  python scripts/marco.py semana actual --horas 6 --hipotesis "..."
  python scripts/marco.py video I-0001 [--semana 2026-W46] [--ensayo]
  python scripts/marco.py aprobar OK-2 VID-0001 --evidencia "Ale en chat, 2026-11-12"
  python scripts/marco.py mover VID-0001 EN_PRODUCCION --siguiente "Grabar S01–S03"
  python scripts/marco.py validar
Ejecuta `python scripts/marco.py <orden> -h` para ver las opciones de cada orden.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))

import medios  # noqa: E402
import reglas  # noqa: E402
from nucleo import RAIZ, VACIOS, Doc, ErrorMarco, corta, semana_id  # noqa: E402


def _consola_utf8():
    for flujo in (sys.stdout, sys.stderr):
        try:
            flujo.reconfigure(encoding="utf-8", errors="replace")
        except (AttributeError, ValueError):
            pass


# ---------------------------------------------------------------- tablero

def _marca(doc: Doc, puerta: str, actual: str) -> str:
    if not reglas.registrada(doc, puerta):
        return "pendiente"
    return "vigente" if reglas.vigente(doc, puerta, actual) else "CADUCADO"


def tablero(raiz: Path) -> str:
    lineas = []
    try:
        filas = reglas.ideas(raiz)
    except ErrorMarco as e:
        filas = []
        lineas.append(f"! {e}")
    nuevas = [f for f in filas if f["estado"] == "NUEVA"]
    lineas.append(f"Ideas: {len(filas)} en total, {len(nuevas)} sin asignar")
    for f in nuevas[:8]:
        lineas.append(f"  {f['idea_id']}  [{f['proyecto_id']}] {f['titulo']}")
    lineas.append("")
    for s in reglas.semanas(raiz)[-4:]:
        try:
            doc = Doc(reglas.ruta_semana(raiz, s))
            ctl = doc.campos("Control")
            lineas.append(f"Semana {s} · {ctl.get('Horas_netas', '?')} h · OK-1 {_marca(doc, 'OK-1', reglas.huella_ok1(doc))}"
                          f" · {len(doc.tabla('Lote'))} en lote")
        except ErrorMarco as e:
            lineas.append(f"Semana {s}: ! {e}")
    lineas.append("")
    activos = 0
    for vid in reglas.videos(raiz):
        try:
            v = reglas.Video.cargar(raiz, vid)
        except ErrorMarco as e:
            lineas.append(f"{vid}: ! {e}")
            continue
        if v.estado in {"ANALIZADO", "CANCELADO"}:
            continue
        activos += 1
        ctl = v.produccion.campos("Control")
        modo = " ENSAYO" if v.modo == "ENSAYO" else ""
        titulo = v.guion.cabeza.strip().split("\n")[0].lstrip("# ").split(" · ", 1)[-1]
        lineas.append(f"{vid}{modo} · {v.estado} · {v.control.get('Proyecto')} · {v.control.get('Idea')} · {titulo}")
        lineas.append(f"    OK-2 {_marca(v.guion, 'OK-2', reglas.huella_ok2(v))} · OK-3 {_marca(v.cierre, 'OK-3', reglas.huella_ok3(v))}"
                      f" · siguiente: {ctl.get('Siguiente_paso', '—')}")
        if ctl.get("Bloqueo", "NINGUNO") not in VACIOS | {"NINGUNO"}:
            lineas.append(f"    BLOQUEO: {ctl['Bloqueo']}")
    if not activos:
        lineas.append("No hay vídeos activos.")
    inf = reglas.validar(raiz)
    lineas.append("")
    lineas.append(f"Validación: {len(inf.errores)} errores, {len(inf.avisos)} avisos"
                  + (" (ejecuta: marco.py validar)" if inf.errores or inf.avisos else ""))
    return "\n".join(lineas)


# ---------------------------------------------------------------- órdenes

def ord_estado(a):
    print(tablero(a.raiz))


def ord_validar(a):
    inf = reglas.validar(a.raiz)
    for e in inf.errores:
        print(f"ERROR  {e}")
    for w in inf.avisos:
        print(f"AVISO  {w}")
    if inf.errores:
        print(f"\n{len(inf.errores)} errores, {len(inf.avisos)} avisos.")
        return 1
    print(("CONFORME" if not inf.avisos else f"CONFORME con {len(inf.avisos)} avisos") + ".")
    return 0


def ord_proyecto(a):
    ruta = reglas.crear_proyecto(a.raiz, a.id, a.nombre)
    print(f"Proyecto creado: {ruta.relative_to(a.raiz).as_posix()}")


def ord_idea(a):
    i = reglas.crear_idea(a.raiz, a.proyecto, a.titulo, a.problema, a.pilar, a.formato, a.procedencia, a.prueba)
    print(f"Idea {i} añadida a registro/IDEAS.csv")


def ord_semana(a):
    ruta = reglas.crear_semana(a.raiz, a.semana, a.horas, a.hipotesis)
    print(f"Semana creada: {ruta.relative_to(a.raiz).as_posix()}")


def ord_video(a):
    semana = a.semana or "actual"
    vid, avisos = reglas.crear_video(a.raiz, a.idea, semana, a.ensayo)
    print(f"Vídeo {vid} creado en videos/{vid}/ (GUION, PRODUCCION, CIERRE)")
    for w in avisos:
        print(f"AVISO  {w}")


def ord_aprobar(a):
    h = reglas.aprobar(a.raiz, a.puerta, a.objetivo, a.evidencia, a.aprobador, a.master)
    print(f"{a.puerta.upper()} registrado para {a.objetivo} · huella {corta(h)}")


def ord_mover(a):
    avisos = reglas.mover(a.raiz, a.video, a.estado, a.siguiente, a.bloqueo)
    print(f"{a.video} → {a.estado.upper()}")
    for w in avisos:
        print(f"AVISO  {w}")


def ord_huellas(a):
    obj = a.objetivo
    if obj.startswith("VID-"):
        v = reglas.Video.cargar(a.raiz, obj)
        for puerta, doc, actual in (("OK-2", v.guion, reglas.huella_ok2(v)), ("OK-3", v.cierre, reglas.huella_ok3(v))):
            print(f"{puerta}: actual {actual} · registrada {doc.campo(puerta, 'Huella') or '—'} · {_marca(doc, puerta, actual)}")
    else:
        s = semana_id(obj)
        doc = Doc(reglas.ruta_semana(a.raiz, s))
        actual = reglas.huella_ok1(doc)
        print(f"OK-1: actual {actual} · registrada {doc.campo('OK-1', 'Huella') or '—'} · {_marca(doc, 'OK-1', actual)}")


def ord_medios(a):
    if a.comprobar is not None or a.copia:
        problemas = medios.comprobar(a.raiz, a.video, a.copia)
        destino = a.copia or f"videos/{a.video}/media"
        if problemas:
            for p in problemas:
                print(f"DIFERENCIA  {p}")
            print(f"\n{len(problemas)} diferencias en {destino}")
            return 1
        print(f"Copia íntegra: {destino} coincide con MEDIOS.csv")
        return 0
    ruta, n = medios.inventariar(a.raiz, a.video)
    print(f"Inventario de {n} archivos en {ruta.relative_to(a.raiz).as_posix()}")
    return 0


def ord_inspeccionar(a):
    r = medios.inspeccionar(a.raiz, a.archivo, a.perfil, a.audio, a.ffprobe, a.cuadros)
    if a.json:
        print(json.dumps(r, ensure_ascii=False, indent=2))
    else:
        print(f"{r['archivo']} · perfil {r['perfil']} · {r['duracion_s']} s")
        for nombre, c in r["controles"].items():
            print(f"  {c['estado']:<9} {nombre:<14} {c['detalle']}")
        print(f"Resultado: {r['resultado']}. {r['nota']}")
    return {"OK": 0, "REVISAR": 3, "FALLA": 2}[r["resultado"]]


# ---------------------------------------------------------------- argumentos

def construir_parser():
    p = argparse.ArgumentParser(prog="marco.py", description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--raiz", type=Path, default=RAIZ, help=argparse.SUPPRESS)
    sub = p.add_subparsers(dest="orden", required=True, metavar="orden")

    s = sub.add_parser("estado", help="tablero de ideas, semanas y vídeos")
    s.set_defaults(f=ord_estado)

    s = sub.add_parser("validar", help="comprueba todo el marco (sale con 1 si hay errores)")
    s.set_defaults(f=ord_validar)

    s = sub.add_parser("proyecto", help="crea proyectos/<id>/PROYECTO.md")
    s.add_argument("id")
    s.add_argument("--nombre", default="")
    s.set_defaults(f=ord_proyecto)

    s = sub.add_parser("idea", help="añade una idea a registro/IDEAS.csv")
    s.add_argument("proyecto")
    s.add_argument("titulo")
    for campo in ("problema", "pilar", "formato", "procedencia", "prueba"):
        s.add_argument(f"--{campo}", default="")
    s.set_defaults(f=ord_idea)

    s = sub.add_parser("semana", help="crea semanas/AAAA-WNN/SEMANA.md")
    s.add_argument("semana", help="2026-W46, 'actual' o 'siguiente'")
    s.add_argument("--horas", default="")
    s.add_argument("--hipotesis", default="")
    s.set_defaults(f=ord_semana)

    s = sub.add_parser("video", help="crea el expediente de un vídeo a partir de una idea")
    s.add_argument("idea")
    s.add_argument("--semana", help="por defecto, la semana actual")
    s.add_argument("--ensayo", action="store_true", help="vídeo de prueba que no se publica (no exige OK-1)")
    s.set_defaults(f=ord_video)

    s = sub.add_parser("aprobar", help="registra OK-1 (semana), OK-2 (guion) u OK-3 (máster) con su huella")
    s.add_argument("puerta", help="OK-1, OK-2 u OK-3")
    s.add_argument("objetivo", help="semana (OK-1) o vídeo (OK-2/OK-3)")
    s.add_argument("--evidencia", required=True, help="dónde y cuándo lo aprobó Alexander")
    s.add_argument("--aprobador", default="Alexander")
    s.add_argument("--master", help="OK-3: ruta del máster relativa a la carpeta del vídeo")
    s.set_defaults(f=ord_aprobar)

    s = sub.add_parser("mover", help="cambia el estado de un vídeo (comprueba que se cumplen los requisitos)")
    s.add_argument("video")
    s.add_argument("estado", help=", ".join(reglas.ESTADOS))
    s.add_argument("--siguiente", help="texto para Siguiente_paso")
    s.add_argument("--bloqueo", help="motivo (obligatorio para BLOQUEADO)")
    s.set_defaults(f=ord_mover)

    s = sub.add_parser("huellas", help="muestra huellas actuales y registradas de una semana o vídeo")
    s.add_argument("objetivo")
    s.set_defaults(f=ord_huellas)

    s = sub.add_parser("medios", help="inventaría media/ en MEDIOS.csv o comprueba una copia")
    s.add_argument("video")
    s.add_argument("--copia", help="carpeta de una copia de seguridad a comparar con MEDIOS.csv")
    s.add_argument("--comprobar", action="store_const", const=True, help="compara media/ con MEDIOS.csv")
    s.set_defaults(f=ord_medios)

    s = sub.add_parser("inspeccionar", help="metadatos de un vídeo con ffprobe frente al perfil de entrega")
    s.add_argument("archivo")
    s.add_argument("--perfil", choices=["entrega", "ingesta"], default="entrega")
    s.add_argument("--audio", choices=["voz", "silencio", "indiferente"], default="voz")
    s.add_argument("--ffprobe")
    s.add_argument("--cuadros", action="store_true", help="mide la cadencia cuadro a cuadro (más lento)")
    s.add_argument("--json", action="store_true")
    s.set_defaults(f=ord_inspeccionar)
    return p


def main(argv=None) -> int:
    _consola_utf8()
    args = construir_parser().parse_args(argv)
    args.raiz = args.raiz.resolve()
    try:
        return args.f(args) or 0
    except ErrorMarco as e:
        print(f"ERROR  {e}", file=sys.stderr)
        return 2
    except OSError as e:
        print(f"ERROR  {e}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
