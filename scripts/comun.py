"""Contratos compartidos de la candidata. Solo biblioteca estándar."""
from contextlib import contextmanager
from datetime import date, datetime
from hashlib import file_digest, sha256
from pathlib import Path, PurePosixPath
from tempfile import mkdtemp, NamedTemporaryFile
import csv
import json
import os
import re
import stat

ROOT = Path(__file__).resolve().parents[1]
VIDEO = r"VID-[0-9]{4,}"
IDEA = r"I-[0-9]{4,}"
PROYECTO = r"[a-z0-9]+(?:-[a-z0-9]+)*"
SHA = r"[0-9a-f]{64}"
VERSION = r"v[0-9]{2,}"
PLATAFORMAS = {"Instagram", "Facebook", "TikTok", "YouTube"}
IDEAS_CSV = "idea_id,proyecto_id,fecha,procedencia,problema,prueba".split(",")
DOCS_VIDEO = ("GUION.md", "PRODUCCION.md", "CIERRE.md")
RAICES_MEDIOS = {"media", "hyperframes", "montaje", "entregas"}
PENDIENTE = {"", "PENDIENTE", "SIN_MEDIR", "POR_VERIFICAR"}


def exigir(condicion, mensaje):
    if not condicion:
        raise ValueError(mensaje)


def identificador(valor, patron, nombre):
    exigir(re.fullmatch(patron, valor), f"{nombre} inválido: {valor}")
    return valor


def semana_iso(valor):
    match = re.fullmatch(r"([0-9]{4})-W([0-9]{2})", valor)
    exigir(match, f"Semana ISO inválida: {valor}")
    try:
        date.fromisocalendar(*map(int, match.groups()), 1)
    except ValueError as exc:
        raise ValueError(f"Semana ISO inválida: {valor}") from exc
    return valor


def fecha(valor, *, hora=False):
    if not hora:
        identificador(valor, r"[0-9]{4}-[0-9]{2}-[0-9]{2}", "Fecha ISO")
        return date.fromisoformat(valor)
    instante = datetime.fromisoformat(valor)
    exigir(instante.utcoffset() is not None, f"Fecha sin zona: {valor}")
    return instante


def relativa(valor):
    p = PurePosixPath(valor)
    exigir(
        valor and not p.is_absolute() and p.as_posix() == valor and valor != "."
        and all(
            parte not in {".", ".."} and not parte.endswith((".", " "))
            and not re.search(r'[\\:<>"|?*\x00-\x1f]', parte)
            and not re.fullmatch(r"(?i:CON|PRN|AUX|NUL|COM[1-9]|LPT[1-9])", parte.split(".")[0])
            for parte in p.parts
        ),
        f"Ruta relativa insegura: {valor}",
    )
    return p


def ruta_segura(ruta):
    ruta = Path(ruta).absolute()
    exigir(".." not in ruta.parts, f"Ruta insegura: {ruta}")
    for parte in (*reversed(ruta.parents), ruta):
        try:
            st = parte.lstat()
        except FileNotFoundError:
            continue
        atributos = getattr(st, "st_file_attributes", 0)
        exigir(
            not stat.S_ISLNK(st.st_mode) and not atributos & stat.FILE_ATTRIBUTE_REPARSE_POINT,
            f"No se admiten enlaces ni puntos de reanálisis: {parte}",
        )
    return ruta.resolve()


def bajo(raiz, valor):
    raiz = ruta_segura(raiz)
    destino = ruta_segura(raiz.joinpath(*relativa(valor).parts))
    exigir(destino.is_relative_to(raiz) and destino != raiz, f"Ruta fuera de alcance: {valor}")
    return destino


def disjuntos(primero, segundo):
    a, b = ruta_segura(primero), ruta_segura(segundo)
    return not a.is_relative_to(b) and not b.is_relative_to(a)


def hash_archivo(ruta):
    with ruta_segura(ruta).open("rb") as archivo:
        return file_digest(archivo, "sha256").hexdigest()


def hash_texto(*partes):
    canon = json.dumps(partes, ensure_ascii=False, separators=(",", ":"))
    return sha256(canon.encode("utf-8")).hexdigest()


def leer_md(ruta):
    ruta = ruta_segura(ruta)
    try:
        texto = ruta.read_text(encoding="utf-8-sig")
    except FileNotFoundError as exc:
        raise ValueError(f"Falta documento: {ruta}") from exc
    partes = re.split(r"^## ([^\n]+)\n", texto, flags=re.MULTILINE)
    titulos = partes[1::2]
    exigir(len(set(titulos)) == len(titulos), f"Secciones repetidas: {ruta}")
    return dict(zip(titulos, (p.strip() for p in partes[2::2])))


def seccion(doc, titulo):
    exigir(titulo in doc, f"Falta sección {titulo}")
    return doc[titulo]


def campos(doc, titulo):
    pares = re.findall(r"^- ([A-Za-z_0-9-]+):[ \t]*([^\n]*)$", seccion(doc, titulo), re.M)
    exigir(len({k for k, _ in pares}) == len(pares), f"Campos repetidos en {titulo}")
    return {k: v.strip() for k, v in pares}


def valor(datos, clave):
    texto = datos.get(clave, "")
    exigir(texto not in PENDIENTE, f"Falta campo {clave} o sigue PENDIENTE")
    return texto


def tabla(doc, titulo, encabezado):
    lineas = [s for s in seccion(doc, titulo).splitlines() if s.strip().startswith("|")]
    celdas = [[x.strip() for x in s.strip().strip("|").split("|")] for s in lineas]
    exigir(
        len(celdas) >= 2 and celdas[0] == encabezado
        and len(celdas[1]) == len(encabezado)
        and all(re.fullmatch(r":?-{3,}:?", x) for x in celdas[1]),
        f"Cabecera inválida en {titulo}",
    )
    for fila in celdas[2:]:
        exigir(len(fila) == len(encabezado) and fila[0], f"Fila inválida en {titulo}: {fila}")
    return celdas[2:]


def csv_filas(ruta, encabezado):
    with ruta_segura(ruta).open(encoding="utf-8-sig", newline="") as archivo:
        lector = csv.DictReader(archivo, strict=True)
        exigir(lector.fieldnames == encabezado, f"Cabecera inválida: {ruta.name}")
        for fila in lector:
            exigir(None not in fila and None not in fila.values(), f"Fila incompleta: {ruta.name}:{lector.line_num}")
            yield fila


def json_leer(ruta):
    return json.loads(ruta_segura(ruta).read_text(encoding="utf-8-sig"))


@contextmanager
def escritura_exclusiva(ruta):
    ruta = ruta_segura(ruta)
    try:
        archivo = ruta.open("x", encoding="utf-8")
    except FileExistsError as exc:
        raise ValueError(f"Operación en curso o bloqueo por revisar: {ruta}") from exc
    try:
        with archivo:
            archivo.write(str(os.getpid()))
        yield
    finally:
        ruta.unlink(missing_ok=True)


def json_guardar(ruta, datos):
    ruta = ruta_segura(ruta)
    cuerpo = json.dumps(datos, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    with NamedTemporaryFile(mode="w", dir=ruta.parent, encoding="utf-8", delete=False) as archivo:
        temporal = Path(archivo.name)
        try:
            archivo.write(cuerpo)
        except BaseException:
            archivo.close()
            temporal.unlink(missing_ok=True)
            raise
    try:
        temporal.replace(ruta)
    finally:
        temporal.unlink(missing_ok=True)


def crear_directorio(destino, textos):
    destino = ruta_segura(destino)
    destino.parent.mkdir(parents=True, exist_ok=True)
    with escritura_exclusiva(destino.parent / ".alta.lock"):
        exigir(not destino.exists(), f"Ya existe, conservado: {destino.name}")
        temporal = Path(mkdtemp(prefix=".alta-", dir=destino.parent))
        try:
            for nombre, texto in textos.items():
                (temporal / nombre).write_text(texto, encoding="utf-8")
            temporal.rename(destino)
        finally:
            if temporal.is_dir():
                for nombre in textos:
                    (temporal / nombre).unlink(missing_ok=True)
                temporal.rmdir()
