"""Reglas del flujo: altas, aprobaciones con huella, estados y validación."""
from __future__ import annotations

import re
from urllib.parse import unquote
from dataclasses import dataclass, field
from pathlib import Path

from nucleo import (
    CAB_CUENTAS, CAB_IDEAS, CAB_METRICAS, ESTADOS_IDEA, PLATAFORMAS, RE_FECHA, RE_PUBLICACION,
    RE_SEMANA, RE_SHA, RE_VIDEO, VACIOS, Doc, ErrorMarco, corta, escribir_csv, escribir_texto,
    exigir, fecha_iso, fila_tabla, huella, idea_id, leer_csv, leer_texto, proyecto_id, rel,
    semana_id, sha_archivo, siguiente_id, video_id, hoy,
)

ESTADOS = ["BORRADOR", "GUION_APROBADO", "EN_PRODUCCION", "LISTO", "PUBLICADO", "ANALIZADO",
           "BLOQUEADO", "CANCELADO"]
REQUIERE_OK2 = {"GUION_APROBADO", "EN_PRODUCCION", "LISTO"}
REQUIERE_OK3 = {"LISTO"}
PUBLICADOS = {"PUBLICADO", "ANALIZADO"}
TIPOS_CLAIM = {"P", "E", "O", "H", "X"}
MODOS = {"NORMAL", "ENSAYO"}
QC_CAMPOS = ["Tecnico", "Imagen", "Audio", "Textos", "Derechos", "Movil"]
DISPONIBILIDAD = {"DISPONIBLE", "NO_DISPONIBLE"}


# ---------------------------------------------------------------- rutas

def ruta_semana(raiz: Path, semana: str) -> Path:
    return raiz / "semanas" / semana / "SEMANA.md"


def carpeta_video(raiz: Path, vid: str) -> Path:
    return raiz / "videos" / vid


def plantilla(raiz: Path, nombre: str, valores: dict) -> str:
    ruta = raiz / "templates" / nombre
    exigir(ruta.is_file(), f"Falta la plantilla templates/{nombre}")
    texto = leer_texto(ruta)
    for clave, valor in valores.items():
        texto = texto.replace("{{" + clave + "}}", valor)
    sobrantes = re.findall(r"\{\{[A-Z_]+\}\}", texto)
    exigir(not sobrantes, f"Marcadores sin resolver en templates/{nombre}: {sobrantes}")
    return texto


# ---------------------------------------------------------------- registros

def ideas(raiz: Path) -> list[dict]:
    return leer_csv(raiz / "registro" / "IDEAS.csv", CAB_IDEAS)


def proyectos(raiz: Path) -> set[str]:
    base = raiz / "proyectos"
    return {p.parent.name for p in base.glob("*/PROYECTO.md")} if base.is_dir() else set()


def semanas(raiz: Path) -> list[str]:
    base = raiz / "semanas"
    return sorted(p.parent.name for p in base.glob("*/SEMANA.md")) if base.is_dir() else []


def videos(raiz: Path) -> list[str]:
    base = raiz / "videos"
    return sorted(p.name for p in base.iterdir() if p.is_dir() and RE_VIDEO.fullmatch(p.name)) if base.is_dir() else []


def cuentas(raiz: Path) -> list[dict]:
    return leer_csv(raiz / "marca" / "CUENTAS.csv", CAB_CUENTAS)


# ---------------------------------------------------------------- documentos de un vídeo

@dataclass
class Video:
    vid: str
    guion: Doc
    produccion: Doc
    cierre: Doc
    carpeta: Path

    @classmethod
    def cargar(cls, raiz: Path, vid: str) -> "Video":
        video_id(vid)
        c = carpeta_video(raiz, vid)
        exigir(c.is_dir(), f"No existe el vídeo {vid} (carpeta videos/{vid})")
        return cls(vid, Doc(c / "GUION.md"), Doc(c / "PRODUCCION.md"), Doc(c / "CIERRE.md"), c)

    @property
    def control(self) -> dict:
        return self.guion.campos("Control")

    @property
    def estado(self) -> str:
        return self.produccion.campo("Control", "Estado")

    @property
    def modo(self) -> str:
        return self.control.get("Modo", "")


# ---------------------------------------------------------------- huellas por puerta

def huella_ok1(doc: Doc) -> str:
    control = doc.campos("Control")
    lote = [(f.get("idea_id", ""), f.get("horas", ""), f.get("motivo", "")) for f in doc.tabla("Lote")]
    return huella("OK-1", sorted(control.items()), lote)


def huella_ok2(v: Video) -> str:
    g = v.guion
    return huella("OK-2", sorted(g.campos("Control").items()), g.seccion("Brief"),
                  [sorted(f.items()) for f in g.tabla("Ganchos")],
                  [sorted(f.items()) for f in g.tabla("Escenas")],
                  [sorted(f.items()) for f in g.tabla("Claims")])


def huella_ok3(v: Video) -> str:
    c = v.cierre
    return huella("OK-3", v.guion.campo("OK-2", "Huella"), sorted(c.campos("Control").items()),
                  [sorted(f.items()) for f in c.tabla("Derechos")], c.seccion("QC"),
                  [sorted(f.items()) for f in c.tabla("Plan de publicación")])


def aprobacion(doc: Doc, puerta: str) -> dict:
    return doc.campos(puerta)


def registrada(doc: Doc, puerta: str) -> bool:
    return aprobacion(doc, puerta).get("Huella", "") not in VACIOS


def vigente(doc: Doc, puerta: str, actual: str) -> bool:
    return aprobacion(doc, puerta).get("Huella", "") == actual


# ---------------------------------------------------------------- altas

def crear_proyecto(raiz: Path, pid: str, nombre: str) -> Path:
    proyecto_id(pid)
    destino = raiz / "proyectos" / pid / "PROYECTO.md"
    exigir(not destino.exists(), f"Ya existe el proyecto {pid}")
    escribir_texto(destino, plantilla(raiz, "PROYECTO.md", {"PROYECTO": pid, "NOMBRE": nombre or pid}))
    return destino


def crear_idea(raiz: Path, proyecto: str, titulo: str, problema: str = "", pilar: str = "",
               formato: str = "", procedencia: str = "", prueba: str = "") -> str:
    proyecto_id(proyecto)
    exigir(proyecto in proyectos(raiz), f"No existe el proyecto '{proyecto}'. Créalo con: marco.py proyecto {proyecto}")
    exigir(titulo.strip(), "La idea necesita un título")
    filas = ideas(raiz)
    nuevo = siguiente_id("I-", [f["idea_id"] for f in filas])
    filas.append({"idea_id": nuevo, "proyecto_id": proyecto, "fecha": hoy(), "titulo": titulo.strip(),
                  "pilar": pilar, "formato": formato, "procedencia": procedencia, "problema": problema,
                  "prueba": prueba, "puntuacion": "", "estado": "NUEVA"})
    escribir_csv(raiz / "registro" / "IDEAS.csv", CAB_IDEAS, filas)
    return nuevo


def crear_semana(raiz: Path, semana: str, horas: str = "", hipotesis: str = "") -> Path:
    semana = semana_id(semana)
    destino = ruta_semana(raiz, semana)
    exigir(not destino.exists(), f"Ya existe la semana {semana}; no se ha tocado")
    texto = plantilla(raiz, "SEMANA.md", {"SEMANA": semana})
    escribir_texto(destino, texto)
    doc = Doc(destino)
    if horas:
        doc.poner_campo("Control", "Horas_netas", horas)
    if hipotesis:
        doc.poner_campo("Control", "Hipotesis", hipotesis)
    doc.guardar()
    return destino


def crear_video(raiz: Path, idea: str, semana: str, ensayo: bool = False) -> tuple[str, list[str]]:
    """Crea el expediente de un vídeo. Devuelve (id, avisos)."""
    idea_id(idea)
    semana = semana_id(semana)
    avisos = []
    filas = ideas(raiz)
    encontradas = [f for f in filas if f["idea_id"] == idea]
    exigir(encontradas, f"La idea {idea} no está en registro/IDEAS.csv. Añádela con: marco.py idea ...")
    fila_idea = encontradas[0]
    proyecto = fila_idea["proyecto_id"]
    exigir(proyecto in proyectos(raiz), f"La idea {idea} apunta a un proyecto inexistente: {proyecto}")
    ruta_s = ruta_semana(raiz, semana)
    exigir(ruta_s.is_file(), f"No existe la semana {semana}. Créala con: marco.py semana {semana}")
    vid = siguiente_id("VID-", videos(raiz))
    destino = carpeta_video(raiz, vid)
    exigir(not destino.exists(), f"Ya existe {vid}")
    valores = {"VIDEO": vid, "PROYECTO": proyecto, "IDEA": idea, "SEMANA": semana,
               "MODO": "ENSAYO" if ensayo else "NORMAL", "TITULO": fila_idea["titulo"]}
    textos = {n: plantilla(raiz, n, valores) for n in ("GUION.md", "PRODUCCION.md", "CIERRE.md")}
    destino.mkdir(parents=True)
    for nombre, texto in textos.items():
        escribir_texto(destino / nombre, texto)

    # Enlazar con el lote de la semana.
    doc_s = Doc(ruta_s)
    lote = doc_s.tabla("Lote")
    if any(f.get("idea_id") == idea for f in lote):
        cuerpo = doc_s.seccion("Lote")
        lineas = cuerpo.split("\n")
        for i, l in enumerate(lineas):
            celdas = [c.strip() for c in l.strip().strip("|").split("|")]
            if l.strip().startswith("|") and celdas and celdas[0] == idea:
                celdas[1] = vid if celdas[1] in VACIOS else celdas[1] + ", " + vid
                lineas[i] = fila_tabla(celdas)
                break
        doc_s.poner_seccion("Lote", "\n".join(lineas))
    else:
        doc_s.anadir_linea("Lote", fila_tabla([idea, vid, "", "Añadida al crear el vídeo"]))
        if registrada(doc_s, "OK-1"):
            avisos.append(f"La idea {idea} se ha añadido al lote de {semana}: el OK-1 de la semana deberá renovarse.")
    doc_s.guardar()

    if fila_idea["estado"] == "NUEVA":
        fila_idea["estado"] = "SELECCIONADA"
        escribir_csv(raiz / "registro" / "IDEAS.csv", CAB_IDEAS, filas)
    return vid, avisos


# ---------------------------------------------------------------- aprobaciones

def _escribir_aprobacion(doc: Doc, puerta: str, aprobador: str, evidencia: str, h: str) -> None:
    doc.poner_seccion(puerta, "\n".join([
        f"- Aprobador: {aprobador}", f"- Fecha: {hoy()}", f"- Evidencia: {evidencia}", f"- Huella: {h}"]))


def aprobar(raiz: Path, puerta: str, objetivo: str, evidencia: str, aprobador: str = "Alexander",
            master: str | None = None) -> str:
    puerta = puerta.upper()
    exigir(puerta in {"OK-1", "OK-2", "OK-3"}, "Puerta inválida: usa OK-1, OK-2 u OK-3")
    exigir(evidencia.strip(), "Indica --evidencia (p. ej. 'Ale en chat 2026-11-12: «OK-2 VID-0001»')")
    if puerta == "OK-1":
        return _aprobar_ok1(raiz, semana_id(objetivo), aprobador, evidencia)
    v = Video.cargar(raiz, objetivo)
    return _aprobar_ok2(raiz, v, aprobador, evidencia) if puerta == "OK-2" else \
        _aprobar_ok3(raiz, v, aprobador, evidencia, master)


def _aprobar_ok1(raiz, semana, aprobador, evidencia):
    doc = Doc(ruta_semana(raiz, semana))
    control = doc.campos("Control")
    exigir(re.fullmatch(r"\d+(?:[.,]\d+)?", control.get("Horas_netas", "")),
           "OK-1: rellena Horas_netas con un número antes de aprobar")
    exigir(control.get("Hipotesis", "") not in VACIOS, "OK-1: rellena la Hipotesis de la semana")
    lote = doc.tabla("Lote")
    exigir(lote, "OK-1: el lote está vacío")
    conocidas = {f["idea_id"] for f in ideas(raiz)}
    for f in lote:
        exigir(f.get("idea_id") in conocidas, f"OK-1: la idea {f.get('idea_id')} no está en IDEAS.csv")
    h = huella_ok1(doc)
    _escribir_aprobacion(doc, "OK-1", aprobador, evidencia, h)
    doc.guardar()
    return h


def _aprobar_ok2(raiz, v: Video, aprobador, evidencia):
    exigir(v.estado not in {"CANCELADO"}, "El vídeo está CANCELADO")
    escenas, claims = v.guion.tabla("Escenas"), v.guion.tabla("Claims")
    exigir(escenas, "OK-2: la tabla de Escenas está vacía")
    exigir(claims, "OK-2: la tabla de Claims está vacía (si no hay afirmaciones, usa SIN-CLAIMS | O | ...)")
    for c in claims:
        exigir(c.get("tipo") in TIPOS_CLAIM, f"OK-2: tipo de claim inválido {c.get('tipo')!r} en {c.get('claim_id')}")
        exigir(c.get("tipo") != "X", f"OK-2 bloqueado: el claim {c.get('claim_id')} es X (sin verificar)")
    brief = v.guion.campos("Brief")
    vacios = [k for k, val in brief.items() if val in VACIOS]
    exigir(not vacios, f"OK-2: completa el Brief ({', '.join(vacios)})")
    if v.modo != "ENSAYO":
        semana = v.control.get("Semana", "")
        doc_s = Doc(ruta_semana(raiz, semana))
        exigir(vigente(doc_s, "OK-1", huella_ok1(doc_s)),
               f"OK-2: la semana {semana} no tiene un OK-1 vigente (o cambió después de aprobarse)")
    h = huella_ok2(v)
    _escribir_aprobacion(v.guion, "OK-2", aprobador, evidencia, h)
    v.guion.guardar()
    v.produccion.anadir_linea("Historial", f"- {hoy()} · OK-2 · {v.control.get('Version', '')} · {corta(h)} · {evidencia}")
    if v.estado == "BORRADOR":
        v.produccion.poner_campo("Control", "Estado", "GUION_APROBADO")
    v.produccion.guardar()
    return h


def _aprobar_ok3(raiz, v: Video, aprobador, evidencia, master):
    exigir(vigente(v.guion, "OK-2", huella_ok2(v)), "OK-3: el guion no tiene un OK-2 vigente")
    control = v.cierre.campos("Control")
    ruta_master = master or control.get("Master", "")
    exigir(ruta_master not in VACIOS, "OK-3: indica el máster con --master <ruta> (relativa a la carpeta del vídeo)")
    ruta_master = ruta_master.replace("\\", "/")
    archivo = (v.carpeta / ruta_master).resolve()
    exigir(archivo.is_relative_to(v.carpeta.resolve()), "OK-3: el máster debe estar dentro de la carpeta del vídeo (media/entregas/...)")
    exigir(archivo.is_file(), f"OK-3: no encuentro el máster en videos/{v.vid}/{ruta_master}")
    qc = v.cierre.campos("QC")
    malos = [k for k in QC_CAMPOS if qc.get(k, "") != "CONFORME"]
    exigir(not malos, f"OK-3: el QC debe estar CONFORME en {', '.join(malos)}")
    exigir(v.cierre.tabla("Derechos"), "OK-3: registra al menos una fila en Derechos (también los recursos propios)")
    plan = v.cierre.tabla("Plan de publicación")
    if v.modo != "ENSAYO":
        exigir(plan, "OK-3: el plan de publicación está vacío")
    for f in plan:
        _comprobar_publicacion_id(v.vid, f.get("publicacion_id", ""), f.get("plataforma", ""))
    v.cierre.poner_campo("Control", "Master", ruta_master)
    v.cierre.poner_campo("Control", "Master_sha256", sha_archivo(archivo))
    h = huella_ok3(v)
    _escribir_aprobacion(v.cierre, "OK-3", aprobador, evidencia, h)
    v.cierre.guardar()
    v.produccion.anadir_linea("Historial", f"- {hoy()} · OK-3 · {ruta_master} · {corta(h)} · {evidencia}")
    if v.estado in {"BORRADOR", "GUION_APROBADO", "EN_PRODUCCION"}:
        v.produccion.poner_campo("Control", "Estado", "LISTO")
    v.produccion.guardar()
    return h


def _comprobar_publicacion_id(vid: str, pub: str, plataforma: str) -> None:
    m = RE_PUBLICACION.fullmatch(pub)
    exigir(m, f"publicacion_id inválido {pub!r} (formato {vid}-YT-01; redes YT, TT, IG, FB)")
    exigir(m[1] == vid, f"{pub} no pertenece a {vid}")
    exigir(plataforma == PLATAFORMAS[m[2]], f"{pub}: la plataforma debe ser {PLATAFORMAS[m[2]]}, no {plataforma!r}")


# ---------------------------------------------------------------- estados

def mover(raiz: Path, vid: str, estado: str, siguiente: str | None = None, bloqueo: str | None = None) -> list[str]:
    estado = estado.upper()
    exigir(estado in ESTADOS, f"Estado inválido. Opciones: {', '.join(ESTADOS)}")
    v = Video.cargar(raiz, vid)
    v.produccion.poner_campo("Control", "Estado", estado)
    if bloqueo is not None:
        v.produccion.poner_campo("Control", "Bloqueo", bloqueo or "NINGUNO")
    elif estado != "BLOQUEADO":
        v.produccion.poner_campo("Control", "Bloqueo", "NINGUNO")
    if siguiente is not None:
        v.produccion.poner_campo("Control", "Siguiente_paso", siguiente)
    # Comprobar antes de escribir.
    errores, avisos = [], []
    _validar_estado(raiz, v, errores, avisos, {c["plataforma"]: c for c in cuentas(raiz)})
    exigir(not errores, "No se puede pasar a " + estado + ":\n  - " + "\n  - ".join(errores))
    v.produccion.anadir_linea("Historial", f"- {hoy()} · Estado → {estado}")
    v.produccion.guardar()
    return avisos


# ---------------------------------------------------------------- validación

@dataclass
class Informe:
    errores: list[str] = field(default_factory=list)
    avisos: list[str] = field(default_factory=list)

    def error(self, donde: str, texto: str):
        self.errores.append(f"{donde}: {texto}")

    def aviso(self, donde: str, texto: str):
        self.avisos.append(f"{donde}: {texto}")


def _proteger(informe: Informe, donde: str, funcion, *args):
    try:
        return funcion(*args)
    except ErrorMarco as e:
        informe.error(donde, str(e))
    return None


def validar(raiz: Path) -> Informe:
    inf = Informe()
    lista_ideas = _proteger(inf, "registro/IDEAS.csv", _validar_ideas, raiz, inf) or {}
    lista_cuentas = _proteger(inf, "marca/CUENTAS.csv", _validar_cuentas, raiz, inf) or {}
    for p in sorted(proyectos(raiz)):
        _proteger(inf, f"proyectos/{p}", _validar_proyecto, raiz, p)
    asignadas = {}
    for s in semanas(raiz):
        _proteger(inf, f"semanas/{s}", _validar_semana, raiz, s, lista_ideas, asignadas, inf)
    publicaciones = {}
    for vid in videos(raiz):
        _proteger(inf, f"videos/{vid}", _validar_video, raiz, vid, lista_ideas, asignadas,
                  lista_cuentas, publicaciones, inf)
    _proteger(inf, "registro/METRICAS.csv", _validar_metricas, raiz, publicaciones, inf)
    _proteger(inf, "enlaces", _validar_enlaces, raiz, inf)
    return inf


def _validar_ideas(raiz, inf):
    salida = {}
    conocidos = proyectos(raiz)
    for f in ideas(raiz):
        i = f["idea_id"]
        donde = f"IDEAS.csv {i or '(sin id)'}"
        try:
            idea_id(i)
        except ErrorMarco as e:
            inf.error(donde, str(e))
            continue
        if i in salida:
            inf.error(donde, "idea_id repetido")
        if f["proyecto_id"] not in conocidos:
            inf.error(donde, f"proyecto inexistente {f['proyecto_id']!r}")
        if f["fecha"]:
            _proteger(inf, donde, fecha_iso, f["fecha"])
        if f["estado"] not in ESTADOS_IDEA:
            inf.error(donde, f"estado {f['estado']!r} inválido ({', '.join(sorted(ESTADOS_IDEA))})")
        if f["puntuacion"] and not re.fullmatch(r"(10|\d)", f["puntuacion"]):
            inf.error(donde, "puntuacion debe ser un entero 0–10")
        if not f["titulo"]:
            inf.error(donde, "falta el título")
        salida[i] = f
    return salida


def _validar_cuentas(raiz, inf):
    salida = {}
    for f in cuentas(raiz):
        p = f["plataforma"]
        donde = f"CUENTAS.csv {p}"
        if p not in PLATAFORMAS.values():
            inf.error(donde, "plataforma desconocida")
        if f["estado"] not in {"PENDIENTE", "VERIFICADA"}:
            inf.error(donde, "estado debe ser PENDIENTE o VERIFICADA")
        if f["estado"] == "VERIFICADA":
            if not (f["alias"] and f["url"].startswith("https://") and f["evidencia"]):
                inf.error(donde, "una cuenta VERIFICADA necesita alias, url https:// y evidencia")
            if f["fecha_verificacion"]:
                _proteger(inf, donde, fecha_iso, f["fecha_verificacion"])
            else:
                inf.error(donde, "falta fecha_verificacion")
        salida[p] = f
    return salida


def _validar_proyecto(raiz, p):
    doc = Doc(raiz / "proyectos" / p / "PROYECTO.md")
    exigir(doc.campo("Control", "Proyecto") == p, f"Control.Proyecto debe ser '{p}'")


def _validar_semana(raiz, s, lista_ideas, asignadas, inf):
    doc = Doc(ruta_semana(raiz, s))
    donde = f"semanas/{s}"
    exigir(doc.campo("Control", "Semana") == s, f"Control.Semana debe ser {s}")
    for f in doc.tabla("Lote"):
        i = f.get("idea_id", "")
        if i not in lista_ideas:
            inf.error(donde, f"el lote incluye {i!r}, que no está en IDEAS.csv")
        if i in asignadas:
            inf.error(donde, f"la idea {i} ya está en el lote de {asignadas[i]}; muévela, no la dupliques")
        asignadas[i] = s
        for vid in [x.strip() for x in f.get("video_id", "").split(",") if x.strip() not in VACIOS]:
            if not RE_VIDEO.fullmatch(vid) or not carpeta_video(raiz, vid).is_dir():
                inf.error(donde, f"video_id {vid!r} del lote no existe")
    if registrada(doc, "OK-1") and not vigente(doc, "OK-1", huella_ok1(doc)):
        inf.aviso(donde, "OK-1 caducado: la semana cambió después de aprobarse (renueva con marco.py aprobar OK-1)")


def _validar_video(raiz, vid, lista_ideas, asignadas, lista_cuentas, publicaciones, inf):
    v = Video.cargar(raiz, vid)
    donde = f"videos/{vid}"
    ctl = v.control
    if ctl.get("Video") != vid:
        inf.error(donde, f"GUION Control.Video debe ser {vid}")
    if ctl.get("Proyecto") not in proyectos(raiz):
        inf.error(donde, f"proyecto inexistente {ctl.get('Proyecto')!r}")
    i = ctl.get("Idea", "")
    if i not in lista_ideas:
        inf.error(donde, f"idea inexistente {i!r}")
    elif lista_ideas[i]["proyecto_id"] != ctl.get("Proyecto"):
        inf.error(donde, f"la idea {i} pertenece a {lista_ideas[i]['proyecto_id']}, no a {ctl.get('Proyecto')}")
    semana = ctl.get("Semana", "")
    if not RE_SEMANA.fullmatch(semana) or not ruta_semana(raiz, semana).is_file():
        inf.error(donde, f"semana inexistente {semana!r}")
    elif i in asignadas and asignadas[i] != semana:
        inf.error(donde, f"Control.Semana es {semana} pero la idea {i} está en el lote de {asignadas[i]}")
    if v.modo not in MODOS:
        inf.error(donde, f"Modo debe ser NORMAL o ENSAYO, no {v.modo!r}")
    if v.estado not in ESTADOS:
        inf.error(donde, f"Estado inválido {v.estado!r}")
    for c in v.guion.tabla("Claims"):
        if c.get("tipo") not in TIPOS_CLAIM:
            inf.error(donde, f"claim {c.get('claim_id')}: tipo {c.get('tipo')!r} inválido (P, E, O, H, X)")
    _validar_estado(raiz, v, inf.errores, inf.avisos, lista_cuentas, prefijo=donde + ": ")
    for f in v.cierre.tabla("Publicaciones"):
        if f.get("url"):
            publicaciones[f["publicacion_id"]] = vid


def _validar_estado(raiz, v: Video, errores, avisos, lista_cuentas, prefijo=""):
    e = v.estado
    ok2_vig = vigente(v.guion, "OK-2", huella_ok2(v))
    ok3_vig = vigente(v.cierre, "OK-3", huella_ok3(v))
    if e in REQUIERE_OK2 and not ok2_vig:
        errores.append(prefijo + ("el guion cambió después del OK-2: vuelve a aprobarlo o devuelve el vídeo a BORRADOR"
                                  if registrada(v.guion, "OK-2") else f"el estado {e} exige OK-2"))
    elif registrada(v.guion, "OK-2") and not ok2_vig:
        avisos.append(prefijo + "OK-2 caducado: el guion cambió después de aprobarse")
    if e in REQUIERE_OK3 and not ok3_vig:
        errores.append(prefijo + ("el cierre (QC, derechos, plan o máster) cambió tras el OK-3"
                                  if registrada(v.cierre, "OK-3") else f"el estado {e} exige OK-3"))
    elif registrada(v.cierre, "OK-3") and not ok3_vig:
        avisos.append(prefijo + "OK-3 caducado: el cierre cambió después de aprobarse")
    if e == "BLOQUEADO" and v.produccion.campo("Control", "Bloqueo") in VACIOS | {"NINGUNO"}:
        errores.append(prefijo + "BLOQUEADO necesita un motivo en Control.Bloqueo")

    # Máster: si está en este equipo, debe ser exactamente el aprobado.
    control_c = v.cierre.campos("Control")
    sha = control_c.get("Master_sha256", "")
    if sha not in VACIOS:
        if not RE_SHA.fullmatch(sha):
            errores.append(prefijo + "Master_sha256 mal formado")
        else:
            archivo = v.carpeta / control_c.get("Master", "").replace("\\", "/")
            if archivo.is_file():
                if sha_archivo(archivo) != sha:
                    errores.append(prefijo + f"el máster {control_c.get('Master')} no coincide con el aprobado (bytes distintos)")
            elif e in REQUIERE_OK3:
                avisos.append(prefijo + "el máster aprobado no está en este equipo (los medios no se versionan)")

    # Plan y publicaciones.
    plan = {}
    for f in v.cierre.tabla("Plan de publicación"):
        try:
            _comprobar_publicacion_id(v.vid, f.get("publicacion_id", ""), f.get("plataforma", ""))
            plan[f["publicacion_id"]] = f
        except ErrorMarco as ex:
            errores.append(prefijo + str(ex))
    publicadas = 0
    for f in v.cierre.tabla("Publicaciones"):
        pub = f.get("publicacion_id", "")
        if pub not in plan:
            errores.append(prefijo + f"{pub}: publicación fuera del plan de publicación")
            continue
        if f.get("fecha"):
            try:
                fecha_iso(f["fecha"])
            except ErrorMarco as ex:
                errores.append(prefijo + f"{pub}: {ex}")
        if f.get("url"):
            publicadas += 1
            if not f["url"].startswith("https://"):
                errores.append(prefijo + f"{pub}: la URL debe empezar por https://")
            if v.modo == "ENSAYO":
                errores.append(prefijo + f"{pub}: un vídeo ENSAYO no se publica")
            if not registrada(v.cierre, "OK-3"):
                errores.append(prefijo + f"{pub}: publicado sin OK-3")
            plataforma = plan[pub]["plataforma"]
            if lista_cuentas.get(plataforma, {}).get("estado") != "VERIFICADA":
                errores.append(prefijo + f"{pub}: la cuenta de {plataforma} no está VERIFICADA en marca/CUENTAS.csv")
    if e in PUBLICADOS and not publicadas:
        errores.append(prefijo + f"el estado {e} exige al menos una publicación con URL en CIERRE")
    if e in PUBLICADOS and v.modo == "ENSAYO":
        errores.append(prefijo + "un vídeo ENSAYO no puede estar PUBLICADO")


def _validar_metricas(raiz, publicaciones, inf):
    vistas = set()
    for n, f in enumerate(leer_csv(raiz / "registro" / "METRICAS.csv", CAB_METRICAS), start=2):
        donde = f"METRICAS.csv línea {n}"
        pub = f["publicacion_id"]
        m = RE_PUBLICACION.fullmatch(pub)
        if not m:
            inf.error(donde, f"publicacion_id inválido {pub!r}")
            continue
        if pub not in publicaciones:
            inf.error(donde, f"{pub} no figura como publicado (con URL) en ningún CIERRE")
        if f["plataforma"] != PLATAFORMAS[m[2]]:
            inf.error(donde, f"plataforma debe ser {PLATAFORMAS[m[2]]}")
        if not RE_FECHA.fullmatch(f["fecha_observacion"]):
            inf.error(donde, "fecha_observacion debe ser AAAA-MM-DD")
        if not re.fullmatch(r"\+\d+(h|d)", f["ventana"]):
            inf.error(donde, "ventana con formato +48h, +7d, +28d")
        if f["disponibilidad"] not in DISPONIBILIDAD:
            inf.error(donde, "disponibilidad debe ser DISPONIBLE o NO_DISPONIBLE")
        elif f["disponibilidad"] == "NO_DISPONIBLE" and f["valor"]:
            inf.error(donde, "NO_DISPONIBLE va con valor vacío (cero es un dato DISPONIBLE)")
        elif f["disponibilidad"] == "DISPONIBLE" and not re.fullmatch(r"-?\d+(?:[.,]\d+)?", f["valor"]):
            inf.error(donde, "un dato DISPONIBLE necesita un valor numérico")
        if not f["metrica"] or not f["fuente"]:
            inf.error(donde, "faltan metrica o fuente")
        clave = (pub, f["ventana"], f["metrica"], f["fecha_observacion"])
        if clave in vistas:
            inf.error(donde, "observación duplicada")
        vistas.add(clave)


IGNORAR_ENLACES = {".git", "node_modules", "media", "hyperframes"}


def _validar_enlaces(raiz, inf):
    for md in sorted(raiz.rglob("*.md")):
        partes = md.relative_to(raiz).parts
        if any(p in IGNORAR_ENLACES for p in partes) or partes[0] == "templates":
            continue
        texto = leer_texto(md)
        texto = re.sub(r"```.*?```", "", texto, flags=re.S)
        texto = re.sub(r"`[^`\n]*`", "", texto)
        for enlace in re.findall(r"\]\(([^)\s]+)\)", texto):
            destino = enlace.split("#", 1)[0]
            if not destino or re.match(r"^[a-z][a-z0-9+.-]*:", destino):
                continue
            objetivo = (md.parent / unquote(destino)).resolve()
            if not objetivo.is_relative_to(raiz.resolve()):
                inf.error(rel(md, raiz), f"enlace fuera del repositorio: {enlace}")
            elif not objetivo.exists():
                inf.error(rel(md, raiz), f"enlace roto: {enlace}")
