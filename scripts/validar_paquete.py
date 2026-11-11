"""Validación de solo lectura de una release o del estado operativo."""
import argparse
from decimal import Decimal, InvalidOperation
from pathlib import Path
from urllib.parse import unquote, urlsplit
import csv
import os
import re
import sys

from comun import (
    DOCS_VIDEO, IDEA, IDEAS_CSV, PENDIENTE, PLATAFORMAS, PROYECTO, ROOT, SHA, VERSION, VIDEO,
    bajo, campos, csv_filas, exigir, fecha, hash_archivo, hash_texto, identificador,
    json_leer, leer_md, ruta_segura, seccion, semana_iso, tabla, valor,
)
from gestion_archivo import archivos, camino_medio, leer_archivo

VERSION_PAQUETE = "4.0.0-rc.1"
METRICAS_CSV = "publicacion_id,plataforma,fecha_observacion,metric_key,valor,unidad,denominador,ventana,fuente,disponibilidad".split(",")
CUENTAS_CSV = "plataforma,alias_candidato,estado_verificacion,url_perfil_confirmada,fecha_verificacion,evidencia,responsable,tipo_cuenta".split(",")
LOTE = ["idea_id", "proyecto_id", "horas", "motivo"]
ESCENAS = ["escena_id", "duración/TC", "voz literal", "visual y rótulo", "prueba/claim", "sonido y toma"]
CLAIMS = ["claim_id", "tipo", "estado", "prueba y límites"]
DERECHOS = ["recurso", "destinos autorizados", "estado", "procedencia, prueba y condiciones"]
PLAN = ["publicacion_id", "plataforma", "archivo", "sha256", "copy, portada y alcance", "recursos"]
AUTORIZACIONES = ["publicacion_id", "huella OK-3", "aprobador", "fecha", "evidencia", "perfil público", "cuenta"]
PUBLICACIONES = ["publicacion_id", "estado", "fecha", "URL", "evidencia o incidencia"]
CODIGOS = {"Instagram": "IG", "Facebook": "FB", "TikTok": "TT", "YouTube": "YT"}
ESTADOS = {
    "BORRADOR", "SELECCIONADO", "AUTORIZADO_PARA_PRODUCIR", "EN_PRODUCCION",
    "LISTO_PARA_PUBLICAR", "PUBLICADO", "ANALIZADO", "BLOQUEADO", "CANCELADO",
}
BASE = {
    "INICIO.md", "EDITORIAL.md", "OPERACION.md", "FUENTES.md", "AGENTS.md", "CLAUDE.md",
    "CHANGELOG.md", "MIGRACION.csv", "PRUEBAS.md", "PILOTO_AV.md",
    "marca/IDENTIDAD.md", "marca/identidad.json", "marca/CUENTAS.csv",
    "proyectos/miminiapp/PROYECTO.md",
    "registro/DECISIONES.md", "registro/IDEAS.csv", "registro/METRICAS.csv",
    "legado/SELLADO_V35.json", "legado/v3.5/MANIFEST_SHA256.json",
    "scripts/comun.py", "scripts/crear_semana.py", "scripts/gestion_archivo.py",
    "scripts/inspeccionar_video.py", "scripts/validar_paquete.py", "pruebas/test_p0.py", "pruebas/piloto.srt",
    *(f"templates/{s}" for s in (*DOCS_VIDEO, "SEMANA.md", "PROYECTO.md")),
}


def archivos_relativos(raiz):
    salida = {}
    for original in raiz.rglob("*"):
        ruta = ruta_segura(original)
        if ruta.is_file():
            salida[ruta.relative_to(raiz).as_posix()] = ruta
    return salida


def comprobar_huellas(raiz, esperados, conjunto_exacto):
    exigir(isinstance(esperados, dict) and bool(esperados), "Manifiesto vacío o inválido")
    exigir(set(esperados) == set(conjunto_exacto), "Manifiesto incompleto o con archivos inesperados")
    for nombre, esperado in esperados.items():
        identificador(esperado, SHA, "SHA-256")
        ruta = bajo(raiz, nombre)
        exigir(ruta.is_file() and hash_archivo(ruta) == esperado, f"Huella distinta o archivo faltante: {nombre}")


def validar_legado(raiz):
    legado = bajo(raiz, "legado/v3.5")
    sellado = json_leer(bajo(raiz, "legado/SELLADO_V35.json"))
    exigir(isinstance(sellado, dict) and sellado.get("version") == "3.5" and sellado.get("algoritmo") == "sha256", "Sello histórico inválido")
    hashes = sellado.get("files", {})
    exigir(isinstance(hashes, dict) and len(hashes) == 64, "La copia sellada debe contener 64 archivos")
    comprobar_huellas(legado, hashes, archivos_relativos(legado))
    original = json_leer(legado / "MANIFEST_SHA256.json")
    exigir(isinstance(original, dict) and original.get("version") == "3.5" and original.get("files") == {
        nombre: digest for nombre, digest in hashes.items() if nombre != "MANIFEST_SHA256.json"
    }, "El manifiesto v3.5 no coincide con el sello")
    filas = list(csv_filas(bajo(raiz, "MIGRACION.csv"), ["origen_v35", "accion", "destino_operativo", "copia_sellada", "sha256_original", "prueba"]))
    exigir(len(filas) == len(hashes) and {f["origen_v35"] for f in filas} == hashes.keys(), "Migración no cubre los 64 originales")
    for fila in filas:
        nombre = fila["origen_v35"]
        exigir(fila["copia_sellada"] == f"legado/v3.5/{nombre}" and fila["sha256_original"] == hashes[nombre],
               f"Prueba de conservación no coincide: {nombre}")
        exigir(fila["prueba"] and fila["accion"] in {"Conservar", "Modificar", "Fusionar", "Mover", "Deprecar"},
               f"Acción o prueba inválida: {nombre}")
        for destino in fila["destino_operativo"].split(" + "):
            exigir(bajo(raiz, destino).exists(), f"Destino de migración faltante: {destino}")


def validar_release(raiz):
    manifiesto = json_leer(bajo(raiz, "MANIFEST_RELEASE.json"))
    exigir(isinstance(manifiesto, dict) and manifiesto.get("version") == VERSION_PAQUETE and manifiesto.get("algoritmo") == "sha256", "Versión de release inválida")
    conjunto = set(archivos_relativos(raiz)) - {"MANIFEST_RELEASE.json"}
    exigir(BASE <= conjunto, f"Faltan archivos base: {', '.join(sorted(BASE - conjunto))}")
    comprobar_huellas(raiz, manifiesto.get("files"), conjunto)
    validar_legado(raiz)


def filas_unicas(filas, nombre):
    salida = {}
    for fila in filas:
        clave = fila[0]
        exigir(clave not in salida, f"{nombre} repetido: {clave}")
        salida[clave] = fila[1:]
    return salida


def decimal(valor, nombre, *, cero=True):
    numero = Decimal(valor)
    exigir(numero.is_finite() and (numero >= 0 if cero else numero > 0), f"{nombre} inválido: {valor}")
    return numero


def texto_aprobacion(datos):
    exigir(valor(datos, "Aprobador") == "Alexander", "La aprobación requiere a Alexander")
    fecha(valor(datos, "Fecha"))
    valor(datos, "Evidencia")


def aprobacion(doc, seccion_nombre, esperada):
    datos = campos(doc, seccion_nombre)
    claves = {"Aprobador", "Fecha", "Evidencia", "Huella"}
    exigir(claves <= datos.keys(), f"{seccion_nombre}: faltan campos")
    if all(datos[k] in PENDIENTE for k in claves):
        return False
    texto_aprobacion(datos)
    actual = identificador(valor(datos, "Huella"), SHA, "Huella de aprobación")
    exigir(actual == esperada, f"{seccion_nombre}: aprobación obsoleta, cambió el alcance o el archivo")
    return True


def hash_semana(doc):
    return hash_texto(seccion(doc, "Control"), seccion(doc, "Lote"))


def hash_guion(doc):
    return hash_texto(*(seccion(doc, s) for s in ("Control", "Brief", "Escenas", "Claims")))


def hash_cierre(doc):
    return hash_texto(*(seccion(doc, s) for s in ("Control", "Derechos", "QC", "Plan de publicación")))


def hash_medio(episodio, nombre, offline):
    camino_medio(nombre)
    ruta = bajo(episodio, nombre)
    if ruta.is_file():
        return hash_archivo(ruta)
    if offline and nombre in offline:
        return offline[nombre]["sha256"]
    raise ValueError(f"Falta medio requerido: {nombre}")


def hash_corte(episodio, guion, produccion, offline):
    montaje = campos(produccion, "Montaje y timing")
    identificador(valor(montaje, "Version_corte"), VERSION, "Versión del corte")
    ruta = valor(montaje, "Ruta_corte")
    proyecto = valor(montaje, "Proyecto_editor")
    huella_proyecto = None if proyecto == "NO_APLICA" else hash_medio(episodio, proyecto, offline)
    return hash_texto(
        hash_guion(guion), seccion(produccion, "Montaje y timing"),
        campos(produccion, "Control").get("Perfil_visual"),
        campos(produccion, "Control").get("Perfil_tecnico"),
        hash_medio(episodio, ruta, offline), huella_proyecto,
    )


def enlaces(raiz, ruta, offline=None):
    texto = ruta.read_text(encoding="utf-8-sig")
    for link in re.findall(r"\]\((<[^>]+>|[^\s)]+)\)", texto):
        objetivo = unquote(link.strip("<>").split("#", 1)[0])
        if not objetivo or urlsplit(objetivo).scheme in {"https", "http", "mailto"}:
            continue
        exigir(not objetivo.startswith(("/", "\\")) and not urlsplit(objetivo).scheme, f"Enlace local absoluto en {ruta.name}: {link}")
        destino = ruta_segura(Path(os.path.normpath(ruta.parent / objetivo)))
        en_archivo = (offline and destino.is_relative_to(ruta.parent)
                      and destino.relative_to(ruta.parent).as_posix() in offline)
        exigir(destino.is_relative_to(raiz) and (destino.exists() or en_archivo),
               f"Enlace roto o fuera de alcance en {ruta.name}: {link}")


def URL(valor_url, fixture=False, plataforma=None):
    url = urlsplit(valor_url)
    host = (url.hostname or "").lower()
    dominios = {"Instagram": ("instagram.com",), "Facebook": ("facebook.com", "fb.watch"),
                "TikTok": ("tiktok.com",), "YouTube": ("youtube.com", "youtu.be")}
    correcto = url.scheme == "https" and bool(host) and not url.username and not url.password
    if fixture:
        correcto = correcto and host.endswith(".invalid")
    elif plataforma:
        correcto = correcto and any(host == d or host.endswith("." + d) for d in dominios[plataforma])
    exigir(correcto, f"URL no válida para el alcance: {valor_url}")


def leer_contexto(raiz):
    proyectos = set()
    for ficha in bajo(raiz, "proyectos").glob("*/PROYECTO.md"):
        identificador(ficha.parent.name, PROYECTO, "Proyecto")
        datos = campos(leer_md(ficha), "Control")
        exigir(datos.get("Proyecto") == ficha.parent.name and datos.get("Creador") == "Alexander", f"Ficha inconsistente: {ficha}")
        valor(datos, "Estado")
        enlaces(raiz, ficha)
        proyectos.add(ficha.parent.name)
    ideas = {}
    for fila in csv_filas(bajo(raiz, "registro/IDEAS.csv"), IDEAS_CSV):
        id_idea = identificador(fila["idea_id"], IDEA, "Idea")
        exigir(id_idea not in ideas and fila["proyecto_id"] in proyectos, f"Idea repetida o sin proyecto: {id_idea}")
        fecha(fila["fecha"])
        for clave in ("procedencia", "problema", "prueba"):
            valor(fila, clave)
        ideas[id_idea] = fila["proyecto_id"]
    cuentas = {}
    for fila in csv_filas(bajo(raiz, "marca/CUENTAS.csv"), CUENTAS_CSV):
        red = fila["plataforma"]
        exigir(red in PLATAFORMAS and red not in cuentas, f"Cuenta repetida o desconocida: {red}")
        exigir(fila["estado_verificacion"] in {"PENDIENTE", "VERIFICADA"}, f"Estado de cuenta inválido: {red}")
        if fila["estado_verificacion"] == "VERIFICADA":
            URL(valor(fila, "url_perfil_confirmada"), plataforma=red)
            fecha(valor(fila, "fecha_verificacion"))
            for clave in ("evidencia", "responsable", "tipo_cuenta"):
                valor(fila, clave)
        cuentas[red] = fila
    exigir(cuentas.keys() == PLATAFORMAS, "Falta una plataforma en CUENTAS.csv")
    tokens = json_leer(bajo(raiz, "marca/identidad.json"))
    exigir(isinstance(tokens, dict) and tokens.get("status") == "PENDIENTE_B0_NO_USAR_COMO_FINAL"
           and tokens.get("brand_owner") == "Alexander"
           and tokens.get("distinct_from_product_web_theme") is True,
           "El archivo de tokens conserva únicamente la propuesta histórica")
    colores = tokens.get("colors")
    exigir(isinstance(colores, dict) and set(colores) == {
        "background", "surface", "text_primary", "text_secondary", "accent_primary", "accent_secondary", "accent_result"
    }, "Tokens de color incompletos")
    for color in colores.values():
        identificador(color, r"#[0-9a-fA-F]{6}", "Token de color")
    marca = campos(leer_md(bajo(raiz, "marca/IDENTIDAD.md")), "Control público")
    perfil = marca.get("Perfil", "")
    exigir(bool(perfil) and {"Aprobador", "Fecha", "Evidencia"} <= marca.keys(), "Faltan controles de marca")
    if perfil != "PENDIENTE":
        identificador(perfil, r"PUBLICO-v[0-9]{2,}", "Perfil público")
        texto_aprobacion(marca)
    else:
        exigir(all(marca[k] in PENDIENTE for k in ("Aprobador", "Fecha", "Evidencia")), "Autorización de marca incompleta")
    return proyectos, ideas, cuentas, perfil


def leer_semanas(raiz, ideas):
    asignaciones = {}
    for carpeta in bajo(raiz, "semanas").glob("*"):
        if not carpeta.is_dir():
            continue
        semana_iso(carpeta.name)
        ruta = carpeta / "SEMANA.md"
        doc = leer_md(ruta)
        datos = campos(doc, "Control")
        exigir(datos.get("Semana") == carpeta.name, "El ID de la semana no coincide")
        lote = filas_unicas(tabla(doc, "Lote", LOTE), "Idea")
        ok1 = aprobacion(doc, "OK-1", hash_semana(doc))
        total = 0
        for idea, (proyecto, horas, motivo) in lote.items():
            exigir(ideas.get(idea) == proyecto and motivo not in PENDIENTE, f"Selección sin proyecto o motivo: {idea}")
            exigir(idea not in asignaciones, f"Idea presente en dos lotes activos: {idea}")
            total += decimal(horas, "Horas de la idea", cero=False)
            asignaciones[idea] = ok1
        if ok1:
            exigir(lote and total <= decimal(valor(datos, "Horas_netas"), "Horas netas"), "OK-1 sin lote o fuera de capacidad")
        enlaces(raiz, ruta)
    return asignaciones


def leer_offline(episodio):
    if not (episodio / "ARCHIVO.json").exists():
        return {}
    datos = leer_archivo(episodio)
    actual = datos["versiones"][datos["activa"]]
    if actual["estado"] in {"OFFLINE", "RESTAURADO_TEMPORAL"}:
        exigir(not archivos(episodio, episodio=True), "Archivo offline con medios activos inesperados")
    retenidos = {}
    for version in datos["versiones"].values():
        if version["estado"] in {"OFFLINE", "RESTAURADO_TEMPORAL"}:
            for nombre, registro in version["archivos"].items():
                exigir(nombre not in retenidos or retenidos[nombre] == registro,
                       f"Dos versiones archivadas discrepan sobre una misma ruta: {nombre}")
                retenidos[nombre] = registro
    return retenidos


def verificar_publicaciones(episodio, cierre, ok3, offline, fixture, perfil_visual, perfil_publico, cuentas, historico=False):
    derechos = filas_unicas(tabla(cierre, "Derechos", DERECHOS), "Recurso")
    plan = filas_unicas(tabla(cierre, "Plan de publicación", PLAN), "Plan de publicación")
    autorizadas = filas_unicas(tabla(cierre, "Autorización de publicación", AUTORIZACIONES), "Autorización")
    publicaciones = filas_unicas(tabla(cierre, "Publicaciones", PUBLICACIONES), "Publicación")
    for pid, (red, nombre, sha, alcance, recursos) in plan.items():
        exigir(red in PLATAFORMAS, f"Plataforma desconocida: {red}")
        identificador(pid, re.escape(episodio.name + "-" + CODIGOS[red]) + r"-[0-9]{2,}", "Publicación")
        camino_medio(nombre)
        identificador(sha, SHA, "Huella de la salida")
        exigir(alcance not in PENDIENTE and recursos not in PENDIENTE, f"Falta copy, alcance o recursos: {pid}")
        if ok3:
            exigir(hash_medio(episodio, nombre, offline) == sha, f"Cambió la salida de {pid}")
            for recurso in (s.strip() for s in recursos.split(",")):
                exigir(recurso in derechos, f"Recurso sin ficha: {recurso}")
                ambito, estado, prueba = derechos[recurso]
                exigir(red in {s.strip() for s in ambito.split(",")} and estado == "CONFORME" and prueba not in PENDIENTE,
                       f"Derechos sin acreditar en {red}: {recurso}")
    for pid, (huella_ok3, aprobador, fecha_iso, evidencia, perfil_aprobado, cuenta) in autorizadas.items():
        exigir(ok3 and pid in plan and huella_ok3 == hash_cierre(cierre), f"Autorización separada obsoleta o sin plan: {pid}")
        texto_aprobacion({"Aprobador": aprobador, "Fecha": fecha_iso, "Evidencia": evidencia})
        if not fixture:
            red = plan[pid][0]
            identificador(perfil_aprobado, r"PUBLICO-v[0-9]{2,}", "Perfil público autorizado")
            URL(cuenta, plataforma=red)
            if not historico:
                exigir(perfil_visual == perfil_publico == perfil_aprobado,
                       "TEMP o marca pendiente no permite autorizar publicación pública")
                exigir(cuentas[red]["estado_verificacion"] == "VERIFICADA"
                       and cuenta == cuentas[red]["url_perfil_confirmada"], f"Cuenta sin verificar: {red}")
    resultado = {}
    for pid, (estado, fecha_iso, url, evidencia) in publicaciones.items():
        exigir(pid in autorizadas, f"Falta autorización de publicación independiente: {pid}")
        exigir(estado in {"PROGRAMADA", "PUBLICADA", "FALLIDA"} and evidencia not in PENDIENTE, f"Resultado incompleto: {pid}")
        fecha(fecha_iso, hora=True)
        red = plan[pid][0]
        if estado == "PUBLICADA":
            URL(url, fixture, red)
        else:
            exigir(url in PENDIENTE or url == "—", f"URL pública sin publicación confirmada: {pid}")
        resultado[pid] = (red, estado)
    return resultado, autorizadas


def verificar_entrega(episodio, cierre, offline, corte):
    control = campos(cierre, "Control")
    nombre = valor(control, "Ruta_master")
    exigir(nombre.startswith("entregas/"), "El máster debe vivir en entregas")
    identificador(valor(control, "Version_master"), VERSION, "Versión del máster")
    exigir(valor(control, "Master_sha256") == hash_medio(episodio, nombre, offline), "Cambió el máster aprobado")
    huella = identificador(valor(control, "Huella_corte"), SHA, "Huella del corte")
    exigir(corte is None or huella == corte, "OK-3 exige picture lock vigente")
    qc = campos(cierre, "QC")
    for clave in ("Tecnico", "Visual", "Derechos"):
        exigir(qc.get(clave) == "CONFORME", f"QC pendiente: {clave}")
    exigir(qc.get("Audio") in {"CONFORME", "NO_APLICA"}, "QC de audio pendiente")
    valor(qc, "Evidencia")
    fichas = filas_unicas(tabla(cierre, "Derechos", DERECHOS), "Recurso")
    exigir(fichas and all(f[1] == "CONFORME" and f[2] not in PENDIENTE for f in fichas.values()),
           "OK-3 requiere evidencia de los recursos usados")


def verificar_historico(episodio, cierre, actual, offline, fixture):
    titulos = {"Control", "Derechos", "QC", "Plan de publicación", "OK-3", "Autorización de publicación", "Publicaciones"}
    grupos = {}
    for titulo, contenido in cierre.items():
        match = re.fullmatch(r"(.+) \[(v[0-9]{2,})\]", titulo)
        if not match:
            continue
        base, version = match.groups()
        exigir(base in titulos and int(version[1:]) < int(actual[1:]), f"Sección histórica inválida: {titulo}")
        grupos.setdefault(version, {})[base] = contenido
    salida = {}
    for version, anterior in grupos.items():
        exigir(anterior.keys() == titulos and campos(anterior, "Control").get("Revision_cierre") == version,
               f"Historial incompleto: {version}")
        exigir(aprobacion(anterior, "OK-3", hash_cierre(anterior)), f"Falta OK-3 histórico: {version}")
        verificar_entrega(episodio, anterior, offline, None)
        publicaciones, _ = verificar_publicaciones(episodio, anterior, True, offline, fixture, "", "", {}, historico=True)
        exigir(not salida.keys() & publicaciones.keys(), "ID de publicación histórico repetido")
        salida.update(publicaciones)
    return salida


def validar_episodio(raiz, episodio, contexto, asignaciones):
    identificador(episodio.name, VIDEO, "Vídeo")
    proyectos, ideas, cuentas, perfil_publico = contexto
    guion, produccion, cierre = [leer_md(episodio / nombre) for nombre in DOCS_VIDEO]
    offline = leer_offline(episodio)
    for nombre in DOCS_VIDEO:
        enlaces(raiz, episodio / nombre, offline)
    inesperados = {p.name for p in episodio.glob("*.md")} - set(DOCS_VIDEO)
    exigir(not inesperados, f"Markdown adicionales en el expediente: {inesperados}")
    datos = campos(guion, "Control")
    proyecto, idea = valor(datos, "Proyecto"), valor(datos, "Idea")
    exigir(datos.get("Video") == episodio.name and proyecto in proyectos and ideas.get(idea) == proyecto, "Identidad del expediente incoherente")
    modo = valor(datos, "Modo")
    exigir(modo in {"INTERNO", "FIXTURE"}, "Modo de expediente inválido")
    identificador(valor(datos, "Version"), VERSION, "Versión del guion")
    estado = campos(produccion, "Control")
    etapa, perfil_visual = valor(estado, "Estado"), valor(estado, "Perfil_visual")
    exigir(etapa in ESTADOS, f"Estado editorial desconocido: {etapa}")
    exigir(perfil_visual == "TEMP" or re.fullmatch(r"PUBLICO-v[0-9]{2,}", perfil_visual), "Perfil visual inválido")
    valor(estado, "Siguiente_paso")
    if etapa == "BLOQUEADO":
        exigir(valor(estado, "Bloqueo") != "NINGUNO", "Falta motivo del bloqueo")
    escenas = filas_unicas(tabla(guion, "Escenas", ESCENAS), "Escena")
    claims = filas_unicas(tabla(guion, "Claims", CLAIMS), "Claim")
    for claim, (tipo, resultado, prueba) in claims.items():
        exigir(tipo in {"P", "E", "O", "H", "X"} and resultado in {"PENDIENTE", "CONFORME", "RECHAZADO"},
               f"Estado o tipo de claim inválido: {claim}")
        if resultado == "CONFORME":
            exigir(prueba not in PENDIENTE and tipo != "X", f"Claim sin prueba verificable: {claim}")
    ok2 = aprobacion(guion, "OK-2", hash_guion(guion))
    if ok2:
        exigir(asignaciones.get(idea) is True, "OK-2 sin un lote OK-1 vigente")
        exigir(escenas and claims and all(c[1] == "CONFORME" and c[0] != "X" for c in claims.values()), "OK-2 exige escenas y claims conformes")
        for id_escena, escena in escenas.items():
            identificador(id_escena, r"S[0-9]{2,}", "Escena")
            exigir(all(celda not in PENDIENTE for celda in escena), f"Escena incompleta: {id_escena}")
            exigir(all(c.strip() in claims for c in escena[3].split(",")), f"Escena con claims no registrados: {id_escena}")
    lock_campos = campos(produccion, "Picture lock")
    lock_activo = any(x not in PENDIENTE for x in lock_campos.values())
    corte = hash_corte(episodio, guion, produccion, offline) if lock_activo else ""
    lock = aprobacion(produccion, "Picture lock", corte)
    exigir(not lock or ok2, "Picture lock sin OK-2 vigente")
    ok3 = aprobacion(cierre, "OK-3", hash_cierre(cierre))
    revision = identificador(valor(campos(cierre, "Control"), "Revision_cierre"), VERSION, "Revisión de cierre")
    if ok3:
        exigir(lock, "OK-3 exige picture lock vigente")
        verificar_entrega(episodio, cierre, offline, corte)
    if etapa == "SELECCIONADO":
        exigir(asignaciones.get(idea) is True, "Selección sin OK-1 vigente")
    if etapa in {"AUTORIZADO_PARA_PRODUCIR", "EN_PRODUCCION"}:
        exigir(ok2, f"Estado {etapa} sin OK-2")
    if etapa == "LISTO_PARA_PUBLICAR":
        exigir(ok3, "Estado LISTO_PARA_PUBLICAR sin OK-3")
    publicaciones, autorizadas = verificar_publicaciones(episodio, cierre, ok3, offline, modo == "FIXTURE", perfil_visual, perfil_publico, cuentas)
    if etapa == "LISTO_PARA_PUBLICAR":
        exigir(autorizadas, "LISTO_PARA_PUBLICAR requiere autorización separada por destino")
    anteriores = verificar_historico(episodio, cierre, revision, offline, modo == "FIXTURE")
    exigir(not anteriores.keys() & publicaciones.keys(), "Una publicación vigente repite un ID histórico")
    publicaciones.update(anteriores)
    if etapa in {"PUBLICADO", "ANALIZADO"}:
        exigir(any(p[1] == "PUBLICADA" for p in publicaciones.values()), f"Estado {etapa} sin publicación confirmada")
    return idea, publicaciones


def validar_metricas(raiz, publicaciones):
    vistas = set()
    for fila in csv_filas(bajo(raiz, "registro/METRICAS.csv"), METRICAS_CSV):
        pid = fila["publicacion_id"]
        exigir(publicaciones.get(pid) == (fila["plataforma"], "PUBLICADA"), f"Métrica sin publicación confirmada: {pid}")
        instante = fecha(fila["fecha_observacion"], hora=True)
        llave = (pid, instante, valor(fila, "metric_key"))
        exigir(llave not in vistas, f"Observación duplicada: {pid}")
        vistas.add(llave)
        for clave in ("unidad", "ventana", "fuente"):
            valor(fila, clave)
        if fila["disponibilidad"] == "NO_DISPONIBLE":
            exigir(not fila["valor"] and not fila["denominador"], "NO_DISPONIBLE requiere valor y denominador vacíos")
        else:
            exigir(fila["disponibilidad"] == "DISPONIBLE", "Disponibilidad de métrica inválida")
            decimal(valor(fila, "valor"), "Valor")
            if fila["denominador"]:
                decimal(fila["denominador"], "Denominador")


def validar_operacion(raiz):
    faltan = [nombre for nombre in sorted(BASE) if not bajo(raiz, nombre).is_file()]
    exigir(not faltan, f"Faltan archivos base: {', '.join(faltan)}")
    for nombre in ("INICIO.md", "EDITORIAL.md", "OPERACION.md", "FUENTES.md", "AGENTS.md", "CLAUDE.md", "PILOTO_AV.md", "marca/IDENTIDAD.md"):
        enlaces(raiz, bajo(raiz, nombre))
    contexto = leer_contexto(raiz)
    asignaciones = leer_semanas(raiz, contexto[1])
    usadas, publicaciones, errores = set(), {}, []
    for episodio in sorted(bajo(raiz, "videos").glob("*")):
        if not episodio.is_dir():
            continue
        try:
            idea, registros = validar_episodio(raiz, episodio, contexto, asignaciones)
            exigir(idea not in usadas, f"Idea en dos expedientes: {idea}")
            exigir(not publicaciones.keys() & registros.keys(), "ID de publicación repetido")
            usadas.add(idea)
            publicaciones.update(registros)
        except (OSError, ValueError, TypeError, KeyError) as exc:
            errores.append(f"{episodio.name}: {exc}")
    exigir(not errores, "\n".join(errores))
    validar_metricas(raiz, publicaciones)


def huellas(raiz, id_objeto):
    if id_objeto[:1].isdigit():
        semana_iso(id_objeto)
        return {"OK-1": hash_semana(leer_md(bajo(raiz, f"semanas/{id_objeto}/SEMANA.md")))}
    identificador(id_objeto, VIDEO, "Vídeo")
    epi = bajo(raiz, f"videos/{id_objeto}")
    guion, produccion, cierre = [leer_md(epi / nombre) for nombre in DOCS_VIDEO]
    resultados = {"OK-2": hash_guion(guion), "OK-3": hash_cierre(cierre)}
    if campos(produccion, "Montaje y timing").get("Ruta_corte", "") not in PENDIENTE:
        resultados["Picture lock"] = hash_corte(epi, guion, produccion, leer_offline(epi))
    return resultados


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("modo", choices=["release", "operacion", "huellas"])
    parser.add_argument("id_objeto", nargs="?")
    args = parser.parse_args()
    try:
        if args.modo == "huellas":
            exigir(args.id_objeto, "Indica semana o vídeo")
            for nombre, hash_ in huellas(ROOT, args.id_objeto).items():
                print(f"{nombre}: {hash_}")
        else:
            exigir(args.id_objeto is None, "Este modo no recibe ID")
            (validar_release if args.modo == "release" else validar_operacion)(ROOT)
            print(f"CONFORME: {args.modo}")
    except (OSError, ValueError, TypeError, KeyError, InvalidOperation, csv.Error) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
