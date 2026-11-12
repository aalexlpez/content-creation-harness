"""Piezas comunes del marco: rutas, Markdown, CSV y huellas.

Solo biblioteca estándar (Python 3.11+). Todo lo que se escribe sale en UTF-8 con
saltos de línea LF, y todo lo que se lee se normaliza, de modo que el marco se
comporta igual en Windows, macOS y Linux y tras pasar por Git.
"""
from __future__ import annotations

import csv
import hashlib
import io
import json
import os
import re
import tempfile
from datetime import date
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent

# Identificadores
RE_IDEA = re.compile(r"I-\d{4}")
RE_VIDEO = re.compile(r"VID-\d{4}")
RE_SEMANA = re.compile(r"(\d{4})-W(\d{2})")
RE_PROYECTO = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")
RE_PUBLICACION = re.compile(r"(VID-\d{4})-(YT|TT|IG|FB|X)-(\d{2})")
RE_FECHA = re.compile(r"\d{4}-\d{2}-\d{2}")
RE_SHA = re.compile(r"[0-9a-f]{64}")

PLATAFORMAS = {"YT": "YouTube", "TT": "TikTok", "IG": "Instagram", "FB": "Facebook", "X": "X"}
# En X no se sube el vídeo: se publica un post que enlaza a la publicación de una de estas redes.
REDES_POST_ENLACE = {"X"}
REDES_ENLAZABLES = {"TT", "IG"}
VACIOS = {"", "PENDIENTE", "-", "—"}

CAB_IDEAS = ["idea_id", "proyecto_id", "fecha", "titulo", "pilar", "formato",
             "procedencia", "problema", "prueba", "puntuacion", "estado"]
ESTADOS_IDEA = {"NUEVA", "SELECCIONADA", "PRODUCIDA", "DESCARTADA"}
CAB_CUENTAS = ["plataforma", "alias", "estado", "url", "fecha_verificacion", "evidencia"]
CAB_METRICAS = ["publicacion_id", "plataforma", "fecha_observacion", "ventana", "metrica",
                "valor", "unidad", "denominador", "fuente", "disponibilidad"]
CAB_MEDIOS = ["ruta", "bytes", "sha256"]


class ErrorMarco(Exception):
    """Error de uso o de datos que se muestra tal cual a la persona."""


def exigir(condicion, mensaje: str) -> None:
    if not condicion:
        raise ErrorMarco(mensaje)


# ---------------------------------------------------------------- identificadores

def idea_id(valor: str) -> str:
    exigir(RE_IDEA.fullmatch(valor or ""), f"Idea inválida: {valor!r} (formato I-0001)")
    return valor


def video_id(valor: str) -> str:
    exigir(RE_VIDEO.fullmatch(valor or ""), f"Vídeo inválido: {valor!r} (formato VID-0001)")
    return valor


def proyecto_id(valor: str) -> str:
    exigir(RE_PROYECTO.fullmatch(valor or ""), f"Proyecto inválido: {valor!r} (minúsculas y guiones)")
    return valor


def semana_id(valor: str) -> str:
    if valor in {"actual", "esta"}:
        anio, num, _ = date.today().isocalendar()
        return f"{anio}-W{num:02d}"
    if valor == "siguiente":
        anio, num, _ = date.fromordinal(date.today().toordinal() + 7).isocalendar()
        return f"{anio}-W{num:02d}"
    m = RE_SEMANA.fullmatch(valor or "")
    exigir(m, f"Semana inválida: {valor!r} (formato ISO 2026-W46, o 'actual'/'siguiente')")
    try:
        date.fromisocalendar(int(m[1]), int(m[2]), 1)
    except ValueError:
        raise ErrorMarco(f"La semana {valor} no existe en el calendario ISO") from None
    return valor


def fecha_iso(valor: str) -> date:
    exigir(RE_FECHA.fullmatch(valor or ""), f"Fecha inválida: {valor!r} (formato AAAA-MM-DD)")
    try:
        return date.fromisoformat(valor)
    except ValueError:
        raise ErrorMarco(f"Fecha inexistente: {valor}") from None


def hoy() -> str:
    return date.today().isoformat()


def siguiente_id(prefijo: str, existentes) -> str:
    numeros = [int(x.split("-")[-1]) for x in existentes if x.startswith(prefijo)]
    return f"{prefijo}{(max(numeros) if numeros else 0) + 1:04d}"


# ---------------------------------------------------------------- lectura/escritura

def leer_texto(ruta: Path) -> str:
    """Lee UTF-8 (con o sin BOM) y normaliza los saltos de línea a LF."""
    try:
        texto = Path(ruta).read_text(encoding="utf-8-sig")
    except FileNotFoundError:
        raise ErrorMarco(f"No existe: {rel(ruta)}") from None
    except UnicodeDecodeError:
        raise ErrorMarco(f"{rel(ruta)} no está en UTF-8. Guárdalo como UTF-8 y repite.") from None
    return texto.replace("\r\n", "\n").replace("\r", "\n")


def escribir_texto(ruta: Path, texto: str) -> None:
    """Escritura atómica en UTF-8 con LF: o queda el archivo nuevo o el anterior."""
    ruta = Path(ruta)
    ruta.parent.mkdir(parents=True, exist_ok=True)
    if not texto.endswith("\n"):
        texto += "\n"
    fd, tmp = tempfile.mkstemp(prefix=".tmp-", dir=ruta.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as f:
            f.write(texto)
        os.replace(tmp, ruta)
    finally:
        if os.path.exists(tmp):
            os.unlink(tmp)


def rel(ruta, raiz: Path | None = None) -> str:
    raiz = raiz or RAIZ
    try:
        return Path(ruta).resolve().relative_to(raiz.resolve()).as_posix()
    except ValueError:
        return str(ruta)


def dentro(raiz: Path, relativa: str) -> Path:
    """Resuelve una ruta relativa y comprueba que no escapa de `raiz`."""
    exigir(relativa and not os.path.isabs(relativa) and not re.match(r"^[A-Za-z]:", relativa),
           f"Usa una ruta relativa: {relativa!r}")
    destino = (raiz / relativa).resolve()
    exigir(destino.is_relative_to(raiz.resolve()), f"Ruta fuera del alcance permitido: {relativa}")
    return destino


# ---------------------------------------------------------------- CSV

def leer_csv(ruta: Path, cabecera: list[str]) -> list[dict]:
    texto = leer_texto(ruta)
    lector = csv.DictReader(io.StringIO(texto), strict=True)
    exigir(lector.fieldnames == cabecera,
           f"Cabecera de {rel(ruta)} distinta de la esperada: {','.join(cabecera)}")
    filas = []
    for fila in lector:
        exigir(None not in fila and None not in fila.values(),
               f"{rel(ruta)}, línea {lector.line_num}: número de columnas incorrecto")
        filas.append({k: (v or "").strip() for k, v in fila.items()})
    return filas


def escribir_csv(ruta: Path, cabecera: list[str], filas: list[dict]) -> None:
    salida = io.StringIO()
    escritor = csv.DictWriter(salida, fieldnames=cabecera, lineterminator="\n")
    escritor.writeheader()
    for fila in filas:
        escritor.writerow({k: fila.get(k, "") for k in cabecera})
    escribir_texto(ruta, salida.getvalue())


# ---------------------------------------------------------------- Markdown

class Doc:
    """Documento Markdown dividido en secciones `## Título`.

    Conserva el texto exacto para poder reescribir una sección sin tocar el resto.
    """

    def __init__(self, ruta: Path):
        self.ruta = Path(ruta)
        self.texto = leer_texto(self.ruta)
        partes = re.split(r"^## +(.+?) *$", self.texto, flags=re.M)
        self.cabeza = partes[0]
        self.titulos = [t.strip() for t in partes[1::2]]
        self.cuerpos = partes[2::2]
        repetidas = {t for t in self.titulos if self.titulos.count(t) > 1}
        exigir(not repetidas, f"{rel(self.ruta)}: secciones repetidas {sorted(repetidas)}")

    def tiene(self, titulo: str) -> bool:
        return titulo in self.titulos

    def seccion(self, titulo: str) -> str:
        exigir(titulo in self.titulos, f"{rel(self.ruta)}: falta la sección '## {titulo}'")
        return self.cuerpos[self.titulos.index(titulo)].strip("\n")

    def campos(self, titulo: str) -> dict[str, str]:
        pares = re.findall(r"^- ([A-Za-z_0-9áéíóúñÁÉÍÓÚÑ-]+):[ \t]*(.*)$", self.seccion(titulo), flags=re.M)
        return {k: v.strip() for k, v in pares}

    def campo(self, titulo: str, clave: str) -> str:
        return self.campos(titulo).get(clave, "")

    def tabla(self, titulo: str) -> list[dict]:
        lineas = [l.strip() for l in self.seccion(titulo).split("\n") if l.strip().startswith("|")]
        if not lineas:
            return []
        celdas = [[c.strip() for c in _partir_fila(l)] for l in lineas]
        cab = celdas[0]
        exigir(len(celdas) >= 2 and all(re.fullmatch(r":?-{3,}:?", c) for c in celdas[1]),
               f"{rel(self.ruta)}: tabla mal formada en '## {titulo}'")
        filas = []
        for fila in celdas[2:]:
            if not any(fila):
                continue
            exigir(len(fila) == len(cab),
                   f"{rel(self.ruta)}: fila con {len(fila)} columnas en '## {titulo}' (esperadas {len(cab)}): {' | '.join(fila)}")
            filas.append(dict(zip(cab, fila)))
        return filas

    def poner_seccion(self, titulo: str, cuerpo: str) -> None:
        exigir(titulo in self.titulos, f"{rel(self.ruta)}: falta la sección '## {titulo}'")
        self.cuerpos[self.titulos.index(titulo)] = "\n\n" + cuerpo.strip("\n") + "\n\n"

    def poner_campo(self, titulo: str, clave: str, valor: str) -> None:
        cuerpo = self.seccion(titulo)
        patron = re.compile(rf"^- {re.escape(clave)}:.*$", re.M)
        linea = f"- {clave}: {valor}"
        if patron.search(cuerpo):
            cuerpo = patron.sub(lambda _: linea, cuerpo, count=1)
        else:
            cuerpo = (cuerpo + "\n" + linea).strip("\n")
        self.poner_seccion(titulo, cuerpo)

    def anadir_linea(self, titulo: str, linea: str) -> None:
        cuerpo = self.seccion(titulo)
        self.poner_seccion(titulo, (cuerpo + "\n" + linea).strip("\n"))

    def guardar(self) -> None:
        texto = self.cabeza
        for t, c in zip(self.titulos, self.cuerpos):
            texto += f"## {t}\n" + c
        self.texto = re.sub(r"\n{3,}", "\n\n", texto).rstrip("\n") + "\n"
        escribir_texto(self.ruta, self.texto)


def _partir_fila(linea: str) -> list[str]:
    linea = linea.strip()
    if linea.startswith("|"):
        linea = linea[1:]
    if linea.endswith("|") and not linea.endswith("\\|"):
        linea = linea[:-1]
    return [c.replace("\\|", "|") for c in re.split(r"(?<!\\)\|", linea)]


def fila_tabla(valores) -> str:
    return "| " + " | ".join(str(v).replace("|", "\\|") for v in valores) + " |"


# ---------------------------------------------------------------- huellas

def normalizar(texto: str) -> str:
    """Forma canónica para la huella: LF, sin espacios finales, sin líneas vacías extra."""
    lineas = [l.rstrip() for l in texto.replace("\r\n", "\n").replace("\r", "\n").split("\n")]
    return re.sub(r"\n{3,}", "\n\n", "\n".join(lineas)).strip("\n")


def huella(*partes) -> str:
    canon = json.dumps([normalizar(p) if isinstance(p, str) else p for p in partes],
                       ensure_ascii=False, separators=(",", ":"))
    return hashlib.sha256(canon.encode("utf-8")).hexdigest()


def sha_archivo(ruta: Path) -> str:
    h = hashlib.sha256()
    with open(ruta, "rb") as f:
        for bloque in iter(lambda: f.read(1 << 20), b""):
            h.update(bloque)
    return h.hexdigest()


def corta(h: str) -> str:
    return h[:12] if h else "—"
