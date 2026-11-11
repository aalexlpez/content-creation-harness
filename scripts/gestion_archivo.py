"""Inventariar, contrastar copias y recuperar a una ruta nueva. Sin borrado de originales."""
import argparse
from datetime import datetime, timedelta, timezone
from pathlib import Path
from tempfile import mkdtemp
import shutil
import sys

from comun import (
    DOCS_VIDEO, RAICES_MEDIOS, ROOT, SHA, VERSION, VIDEO, bajo, campos,
    disjuntos, escritura_exclusiva, exigir, fecha, hash_archivo, hash_texto,
    identificador, json_guardar, json_leer, leer_md, relativa, ruta_segura,
)

LIGEROS = set(DOCS_VIDEO) | {"ARCHIVO.json", ".archivo.lock"}
ESTADOS = {"LOCAL", "COPIA_VERIFICADA", "OFFLINE", "RESTAURADO_TEMPORAL"}
VIGENCIA = timedelta(hours=24)


def ahora():
    return datetime.now(timezone.utc)


def camino_medio(nombre):
    p = relativa(nombre)
    exigir(len(p.parts) > 1 and p.parts[0] in RAICES_MEDIOS, f"Medio fuera de alcance: {nombre}")
    return p


def archivos(raiz, episodio=False):
    raiz = ruta_segura(raiz)
    exigir(raiz.is_dir(), f"Carpeta inexistente: {raiz}")
    inventario = {}

    def visitar(carpeta):
        for entrada in sorted(carpeta.iterdir()):
            ruta = ruta_segura(entrada)
            if ruta.is_dir():
                visitar(ruta)
            else:
                exigir(ruta.is_file(), f"No es un archivo regular: {entrada}")
                nombre = ruta.relative_to(raiz).as_posix()
                camino_medio(nombre)
                antes = ruta.stat()
                digest = hash_archivo(ruta)
                despues = ruta.stat()
                exigir(
                    (antes.st_size, antes.st_mtime_ns) == (despues.st_size, despues.st_mtime_ns),
                    f"Archivo cambió mientras se leía: {ruta}",
                )
                inventario[nombre] = {"bytes": despues.st_size, "sha256": digest}

    for entrada in sorted(raiz.iterdir()):
        ruta = ruta_segura(entrada)
        if episodio and ruta.name in LIGEROS and ruta.is_file():
            continue
        exigir(
            ruta.name in RAICES_MEDIOS and ruta.is_dir(),
            f"Recurso fuera del alcance del archivo: {ruta}. Clasifícalo primero.",
        )
        visitar(ruta)
    exigir(len({n.casefold() for n in inventario}) == len(inventario), "Rutas de medios duplicadas al ignorar mayúsculas")
    return inventario


def leer_archivo(episodio):
    datos = json_leer(episodio / "ARCHIVO.json")
    exigir(isinstance(datos, dict) and datos.get("esquema") == 1, "Esquema ARCHIVO inválido")
    exigir(datos.get("video") == episodio.name, "ARCHIVO pertenece a otro vídeo")
    modo = campos(leer_md(episodio / "GUION.md"), "Control").get("Modo")
    exigir(modo in {"INTERNO", "FIXTURE"} and modo == datos.get("modo"), "El inventario pertenece a otro modo de trabajo")
    versiones = datos.get("versiones")
    exigir(isinstance(versiones, dict) and datos.get("activa") in versiones, "Inventario activo inexistente")
    for version, inv in versiones.items():
        identificador(version, VERSION, "Versión de archivo")
        exigir(isinstance(inv, dict) and inv.get("estado") in ESTADOS, "Estado de archivo inválido")
        fichas = inv.get("archivos")
        exigir(isinstance(fichas, dict) and fichas, "Inventario vacío")
        for nombre, item in fichas.items():
            camino_medio(nombre)
            exigir(isinstance(item, dict) and type(item.get("bytes")) is int and item["bytes"] >= 0, "Tamaño inválido")
            identificador(item.get("sha256", ""), SHA, "SHA-256")
        exigir(inv.get("huella") == huella(fichas), "Inventario alterado")
        exigir(type(inv.get("irremplazable")) is bool, "Falta clasificación de medios")
        exigir(isinstance(inv.get("copias"), dict), "Faltan copias")
        if inv["estado"] in {"OFFLINE", "RESTAURADO_TEMPORAL"}:
            evento = inv.get("retiro")
            exigir(isinstance(evento, dict) and evento.get("offline_en"), "Falta registro de retirada")
            exigir(evento.get("huella") == inv["huella"], "Retirada de otro inventario")
            respaldos = evento.get("copias", [])
            exigir(isinstance(respaldos, list) and len(respaldos) >= (2 if inv["irremplazable"] else 1), "Faltan copias en el historial de retirada")
            for respaldo in respaldos:
                exigir(isinstance(respaldo, dict), "Copia histórica inválida")
                identificador(respaldo.get("id", ""), r"[A-Za-z0-9][A-Za-z0-9_-]*", "Soporte")
                relativa(respaldo.get("relativa", ""))
                fecha(respaldo.get("verificada_en", ""), hora=True)
            exigir(evento.get("aprobador") == "Alexander" and evento.get("evidencia")
                   and evento.get("evidencia_retirada"), "Registro de retirada incompleto")
            exigir(len({c["id"] for c in respaldos}) == len(respaldos), "Soportes de retirada repetidos")
            fecha(evento.get("preparado_en", ""), hora=True)
            fecha(evento["offline_en"], hora=True)
    return datos


def huella(fichas):
    return hash_texto(sorted(fichas.items()))


def iguales(encontrados, esperados, descripcion):
    diferencias = sorted(n for n in encontrados.keys() | esperados.keys() if encontrados.get(n) != esperados.get(n))
    exigir(not diferencias, f"{descripcion}: {', '.join(diferencias[:8])}")


def verificar_destino(episodio, destino, relativa_destino, fixture):
    destino = ruta_segura(destino)
    rel = relativa(relativa_destino)
    exigir(disjuntos(episodio, destino), "Origen y destino deben ser disjuntos")
    exigir(tuple(p.casefold() for p in destino.parts[-len(rel.parts):]) ==
           tuple(p.casefold() for p in rel.parts), "El destino no coincide con la ruta lógica del soporte")
    exigir(destino.is_dir(), f"El destino no está disponible: {destino}")
    dev = destino.stat().st_dev
    exigir(fixture or dev != episodio.stat().st_dev, "El destino no acredita otro volumen de almacenamiento")
    return destino, dev


def inventariar(episodio, datos, version, irremplazable):
    identificador(version, VERSION, "Versión de archivo")
    exigir(version not in datos["versiones"], f"Inventario {version} ya existe")
    if datos["activa"]:
        anterior = datos["versiones"][datos["activa"]]
        exigir(not anterior.get("retiro") or anterior["retiro"].get("offline_en"),
               "Hay una retirada preparada. Revisa y cancela antes de inventariar una nueva versión")
    fichas = archivos(episodio, episodio=True)
    exigir(fichas, "No hay medios para inventariar")
    for anterior in datos["versiones"].values():
        if anterior["estado"] in {"OFFLINE", "RESTAURADO_TEMPORAL"}:
            cambios = [n for n in fichas.keys() & anterior["archivos"].keys() if fichas[n] != anterior["archivos"][n]]
            exigir(not cambios, f"Conserva las rutas históricas y versiona los archivos cambiados: {cambios}")
    datos["activa"] = version
    datos["versiones"][version] = {
        "archivos": fichas, "huella": huella(fichas), "estado": "LOCAL",
        "irremplazable": irremplazable, "copias": {}, "inventariado_en": ahora().isoformat(),
    }


def verificar(episodio, inv, soporte, destino, rel, fixture):
    identificador(soporte, r"[A-Za-z0-9][A-Za-z0-9_-]*", "Soporte")
    exigir(not inv.get("retiro") or inv["retiro"].get("offline_en"), "La retirada preparada fija las copias. Cancélala antes de sustituirlas")
    if inv["estado"] in {"LOCAL", "COPIA_VERIFICADA"}:
        iguales(archivos(episodio, episodio=True), inv["archivos"], "Origen cambió desde el inventario")
    ruta, dev = verificar_destino(episodio, destino, rel, fixture)
    iguales(archivos(ruta), inv["archivos"], "Copia incompleta o alterada")
    for nombre, previa in inv["copias"].items():
        if nombre != soporte:
            exigir(disjuntos(ruta, Path(previa["ruta_verificada"])), "Dos etiquetas apuntan al mismo destino")
            exigir(fixture or dev != previa["volumen"], "Dos etiquetas apuntan al mismo volumen")
    inv["copias"][soporte] = {
        "id": soporte, "ruta_verificada": str(ruta), "relativa": rel, "volumen": dev,
        "verificada_en": ahora().isoformat(), "huella": inv["huella"],
    }
    if inv["estado"] == "LOCAL":
        inv["estado"] = "COPIA_VERIFICADA"


def comprobar_copias(episodio, inv, copias, fixture):
    exigir(len(copias) >= (2 if inv["irremplazable"] else 1), "Se requieren copias independientes verificadas")
    exigir(len(set(copias)) == len(copias), "Soporte repetido")
    registros = []
    for soporte in copias:
        copia = inv["copias"].get(soporte)
        exigir(copia and copia.get("huella") == inv["huella"], f"Copia sin verificar para este inventario: {soporte}")
        antiguedad = ahora() - fecha(copia["verificada_en"], hora=True)
        exigir(timedelta(0) <= antiguedad <= VIGENCIA, f"Verificación caducada: {soporte}")
        ruta, dev = verificar_destino(episodio, copia["ruta_verificada"], copia["relativa"], fixture)
        exigir(dev == copia["volumen"], f"El volumen montado cambió: {soporte}")
        iguales(archivos(ruta), inv["archivos"], f"Copia alterada o incompleta: {soporte}")
        for anterior in registros:
            exigir(disjuntos(ruta, anterior["ruta_verificada"]), "Dos copias comparten ruta")
            exigir(fixture or dev != anterior["volumen"], "Dos copias comparten volumen")
        registros.append(copia)
    return registros


def preparar(episodio, inv, soportes, aprobador, evidencia, prueba_fisica, fixture):
    exigir(inv["estado"] == "COPIA_VERIFICADA" and not inv.get("retiro"), "Estado no apto para preparar retirada")
    exigir(aprobador == "Alexander" and evidencia.strip() and evidencia != "PENDIENTE",
           "Falta autorización humana separada de retirada")
    exigir(fixture or (prueba_fisica.strip() and prueba_fisica != "PENDIENTE"),
           "Falta referencia a la validación física y a la independencia de los soportes")
    iguales(archivos(episodio, episodio=True), inv["archivos"], "Origen cambió desde el inventario")
    copias = comprobar_copias(episodio, inv, soportes, fixture)
    inv["retiro"] = {
        "aprobador": aprobador, "evidencia": evidencia, "prueba_fisica": prueba_fisica,
        "preparado_en": ahora().isoformat(), "huella": inv["huella"], "copias": copias,
    }


def marcar_offline(episodio, inv, retirada, fixture):
    evento = inv.get("retiro")
    exigir(inv["estado"] == "COPIA_VERIFICADA" and evento, "Falta preparación y autorización de retirada")
    exigir(retirada.strip() and retirada != "PENDIENTE", "Falta evidencia de la retirada manual")
    exigir(not archivos(episodio, episodio=True), "Los medios siguen presentes. El script no los retira")
    comprobar_copias(episodio, inv, [c["id"] for c in evento["copias"]], fixture)
    evento["offline_en"] = ahora().isoformat()
    evento["evidencia_retirada"] = retirada
    inv["estado"] = "OFFLINE"


def recuperar(episodio, inv, soporte, destino_copia, salida, nombres, fixture):
    exigir(inv["estado"] in {"OFFLINE", "RESTAURADO_TEMPORAL"}, "La recuperación requiere archivo offline")
    copia = inv["copias"].get(soporte)
    exigir(copia and copia["huella"] == inv["huella"], "Soporte sin verificar")
    origen, dev = verificar_destino(episodio, destino_copia, copia["relativa"], fixture)
    exigir(dev == copia["volumen"], "El volumen de recuperación cambió")
    salida = ruta_segura(salida)
    exigir(disjuntos(salida, episodio) and disjuntos(salida, origen) and not salida.exists(),
           "La recuperación requiere un destino nuevo, ajeno al episodio y a la copia")
    exigir(salida.parent.is_dir(), "La carpeta padre de recuperación no existe")
    exigir(nombres and len(set(nombres)) == len(nombres), "Selecciona medios sin duplicados")
    for nombre in nombres:
        camino_medio(nombre)
        exigir(nombre in inv["archivos"], f"No inventariado: {nombre}")
    temporal = Path(mkdtemp(prefix=".recuperar-", dir=salida.parent))
    try:
        for nombre in nombres:
            entrada = bajo(origen, nombre)
            esperado = inv["archivos"][nombre]
            exigir(entrada.stat().st_size == esperado["bytes"] and hash_archivo(entrada) == esperado["sha256"],
                   f"Copia alterada: {nombre}")
            archivo = bajo(temporal, nombre)
            archivo.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(entrada, archivo)
            exigir(hash_archivo(archivo) == esperado["sha256"], f"Recuperación alterada: {nombre}")
        exigir(not salida.exists(), f"El destino apareció durante la copia: {salida}")
        temporal.rename(salida)
    finally:
        if temporal.exists():
            exigir(ruta_segura(temporal).parent == salida.parent and temporal.name.startswith(".recuperar-"),
                   "No se puede comprobar la carpeta temporal")
            shutil.rmtree(temporal)
    inv["estado"] = "RESTAURADO_TEMPORAL"
    inv.setdefault("recuperaciones", []).append({
        "fecha": ahora().isoformat(), "soporte": soporte, "salida": str(salida), "archivos": nombres,
    })


def ejecutar(raiz, args):
    identificador(args.video, VIDEO, "Vídeo")
    episodio = bajo(raiz, f"videos/{args.video}")
    control = campos(leer_md(episodio / "GUION.md"), "Control")
    exigir(control.get("Modo") in {"FIXTURE", "INTERNO"}, "Modo de episodio inválido")
    fixture = control["Modo"] == "FIXTURE"
    exigir(fixture == args.fixture, "El modo fixture debe coincidir con GUION y con --fixture")
    ruta = episodio / "ARCHIVO.json"
    with escritura_exclusiva(episodio / ".archivo.lock"):
        datos = leer_archivo(episodio) if ruta.exists() else {"esquema": 1, "video": args.video, "modo": control["Modo"], "activa": None, "versiones": {}}
        if args.accion == "inventariar":
            inventariar(episodio, datos, args.version, not args.reemplazable)
        else:
            exigir(args.version in datos["versiones"], "Versión de inventario inexistente")
            inv = datos["versiones"][args.version]
            if args.version != datos["activa"]:
                exigir(args.accion in {"verificar", "recuperar"}
                       and inv["estado"] in {"OFFLINE", "RESTAURADO_TEMPORAL"},
                       "Acción reservada al inventario activo")
            if args.accion == "verificar":
                verificar(episodio, inv, args.soporte, args.destino, args.relativa, fixture)
            elif args.accion == "preparar-retiro":
                preparar(episodio, inv, args.soportes, args.aprobador, args.evidencia, args.prueba_fisica, fixture)
            elif args.accion == "cancelar-retiro":
                evento = inv.get("retiro")
                exigir(evento and not evento.get("offline_en"), "No hay retirada preparada que pueda cancelarse")
                iguales(archivos(episodio, episodio=True), inv["archivos"], "La retirada ya cambió el origen. Revisar manualmente")
                inv.setdefault("retiros_cancelados", []).append(inv.pop("retiro"))
            elif args.accion == "registrar-offline":
                marcar_offline(episodio, inv, args.retirada, fixture)
            elif args.accion == "recuperar":
                recuperar(episodio, inv, args.soporte, args.destino, args.salida, args.archivos, fixture)
        json_guardar(ruta, datos)
    return datos["versiones"][args.version]["estado"]


def parser_archivo():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--fixture", action="store_true")
    sub = parser.add_subparsers(dest="accion", required=True)
    for nombre in ("inventariar", "verificar", "preparar-retiro", "cancelar-retiro", "registrar-offline", "recuperar"):
        opcion = sub.add_parser(nombre)
        opcion.add_argument("video")
        opcion.add_argument("version")
        if nombre == "inventariar":
            opcion.add_argument("--reemplazable", action="store_true")
        if nombre in {"verificar", "recuperar"}:
            opcion.add_argument("--soporte", required=True)
            opcion.add_argument("--destino", required=True)
        if nombre == "verificar":
            opcion.add_argument("--relativa", required=True)
        if nombre == "preparar-retiro":
            opcion.add_argument("--soportes", nargs="+", required=True)
            opcion.add_argument("--aprobador", required=True)
            opcion.add_argument("--evidencia", required=True)
            opcion.add_argument("--prueba-fisica", default="")
        if nombre == "registrar-offline":
            opcion.add_argument("--retirada", required=True)
        if nombre == "recuperar":
            opcion.add_argument("--salida", required=True)
            opcion.add_argument("--archivos", nargs="+", required=True)
    return parser


def main():
    args = parser_archivo().parse_args()
    try:
        print(ejecutar(ROOT, args))
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
