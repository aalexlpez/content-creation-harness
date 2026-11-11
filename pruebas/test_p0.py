"""Ensayos de estructura. Todas las escrituras ocurren sobre datos ficticios."""
from datetime import timedelta
from pathlib import Path
from tempfile import TemporaryDirectory
import csv
import os
import re
import shutil
import subprocess
import sys
import unittest

BASE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BASE / "scripts"))

from comun import DOCS_VIDEO, campos, csv_filas, hash_archivo, json_guardar, json_leer, leer_md
from crear_semana import crear_semana, crear_video
from gestion_archivo import ahora, ejecutar, parser_archivo
from validar_paquete import (
    METRICAS_CSV, VERSION_PAQUETE, archivos_relativos, huellas, validar_legado,
    validar_operacion, validar_release,
)

SEMANA = "2026-W46"
VIDEO = "VID-0001"
IDEA = "I-0001"
OTRA = "2026-W47"
TS = "2026-11-08T10:00:00+01:00"


def modificar(ruta, viejo, nuevo):
    texto = ruta.read_text(encoding="utf-8")
    if viejo not in texto:
        raise AssertionError(f"Falta texto de fixture: {viejo}")
    ruta.write_text(texto.replace(viejo, nuevo, 1), encoding="utf-8")


def fila(ruta, seccion, contenido):
    patron = rf"(^## {re.escape(seccion)}\n\n\|[^\n]+\n\|[^\n]+\|)\n"
    antes = ruta.read_text(encoding="utf-8")
    nuevo, n = re.subn(patron, lambda m: m[1] + "\n" + contenido + "\n", antes, count=1, flags=re.M)
    if n != 1:
        raise AssertionError(f"Falta tabla: {seccion}")
    ruta.write_text(nuevo, encoding="utf-8")


def registrar(ruta, valores):
    with ruta.open("a", newline="", encoding="utf-8") as salida:
        csv.writer(salida).writerow(valores)


def sellar_aprobacion(ruta, seccion, huella):
    modificar(
        ruta, f"## {seccion}\n\n- Aprobador: PENDIENTE\n- Fecha: PENDIENTE\n- Evidencia: PENDIENTE\n- Huella: PENDIENTE",
        f"## {seccion}\n\n- Aprobador: Alexander\n- Fecha: 2026-11-08\n- Evidencia: Referencia sintética sin efecto\n- Huella: {huella}",
    )


class PruebasP0(unittest.TestCase):
    def setUp(self):
        tmp = Path(os.environ.get("MARCO_TEST_TMP") or BASE.parent).resolve()
        carpeta = TemporaryDirectory(prefix="prueba-marco-", dir=tmp)
        self.addCleanup(carpeta.cleanup)
        self.entorno = Path(carpeta.name).resolve()
        self.assertEqual(self.entorno.parent, tmp)
        self.r = self.entorno / "candidata"
        shutil.copytree(BASE, self.r, ignore=shutil.ignore_patterns("__pycache__"))
        self.e = self.r / "videos" / VIDEO
        self.g, self.p, self.c = (self.e / nombre for nombre in DOCS_VIDEO)
        self.s = self.r / f"semanas/{SEMANA}/SEMANA.md"

    def idea(self, id_idea=IDEA, proyecto="miminiapp"):
        registrar(self.r / "registro/IDEAS.csv", [id_idea, proyecto, "2026-11-08", "Fixture", "Pregunta ficticia", "Prueba ficticia"])

    def alta(self):
        self.idea()
        crear_semana(self.r, SEMANA)
        crear_video(self.r, SEMANA, VIDEO, "miminiapp", IDEA, "FIXTURE")

    def semana_aprobada(self, ruta, id_semana, ideas):
        modificar(ruta, "- Horas_netas: PENDIENTE", "- Horas_netas: 5")
        for id_idea, proyecto in ideas:
            fila(ruta, "Lote", f"| {id_idea} | {proyecto} | 2 | Ensayo ficticio |")
        sellar_aprobacion(ruta, "OK-1", huellas(self.r, id_semana)["OK-1"])

    def guion_aprobado(self):
        self.alta()
        self.semana_aprobada(self.s, SEMANA, [(IDEA, "miminiapp")])
        modificar(self.g, "- Audiencia, pilar y objetivo:", "- Audiencia, pilar y objetivo: Entender un concepto")
        fila(self.g, "Claims", "| C01 | P | CONFORME | Reproducción ficticia, no implica función real |")
        fila(self.g, "Escenas", "| S01 | 00:00–00:01 | Voz ficticia | Rótulo | C01 | guía / toma01 |")
        fila(self.g, "Escenas", "| S02 | 00:01–00:02 | SIN VOZ | Fondo sintético | C01 | silencio |")
        sellar_aprobacion(self.g, "OK-2", huellas(self.r, VIDEO)["OK-2"])

    def material(self, rel, datos):
        p = self.e / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_bytes(datos)
        return p

    def cierre_aprobado(self):
        self.guion_aprobado()
        corte = self.material("montaje/corte_v01.bin", b"cut-version-1")
        master = self.material("entregas/master_v01.mp4", b"mock-video-1")
        modificar(self.p, "- Proyecto_editor: PENDIENTE", "- Proyecto_editor: montaje/corte_v01.bin")
        modificar(self.p, "- Ruta_corte: PENDIENTE", "- Ruta_corte: montaje/corte_v01.bin")
        modificar(self.p, "- Version_corte: PENDIENTE", "- Version_corte: v01")
        huella = huellas(self.r, VIDEO)["Picture lock"]
        sellar_aprobacion(self.p, "Picture lock", huella)
        modificar(self.c, "- Ruta_master: PENDIENTE", "- Ruta_master: entregas/master_v01.mp4")
        modificar(self.c, "- Master_sha256: PENDIENTE", f"- Master_sha256: {hash_archivo(master)}")
        modificar(self.c, "- Version_master: PENDIENTE", "- Version_master: v01")
        modificar(self.c, "- Huella_corte: PENDIENTE", f"- Huella_corte: {huella}")
        for k in ("Tecnico", "Visual", "Audio", "Derechos"):
            modificar(self.c, f"- {k}: PENDIENTE", f"- {k}: CONFORME")
        modificar(self.c, "- Evidencia: PENDIENTE", "- Evidencia: QC ficticio, sin aprobar un máster real")
        fila(self.c, "Derechos", "| R01 | YouTube, Instagram | CONFORME | Material ficticio propio |")
        for id_red, red in (("YT", "YouTube"), ("IG", "Instagram")):
            fila(self.c, "Plan de publicación", f"| {VIDEO}-{id_red}-01 | {red} | entregas/master_v01.mp4 | {hash_archivo(master)} | Copy ficticio | R01 |")
        sellar_aprobacion(self.c, "OK-3", huellas(self.r, VIDEO)["OK-3"])
        return corte, master

    def publicacion(self, red, resultado, url):
        pid = f"{VIDEO}-{red}-01"
        hash_cierre = huellas(self.r, VIDEO)["OK-3"]
        fila(self.c, "Autorización de publicación", f"| {pid} | {hash_cierre} | Alexander | 2026-11-08 | Permiso simulado | TEMP-FIXTURE | cuenta-fixture |")
        fila(self.c, "Publicaciones", f"| {pid} | {resultado} | {TS} | {url} | Incidencia o resultado simulado |")

    def archivo(self, accion, *args, version="v01"):
        return ejecutar(self.r, parser_archivo().parse_args(["--fixture", accion, VIDEO, version, *map(str, args)]))

    def copia(self, etiqueta):
        ruta = self.entorno / etiqueta / VIDEO / "v01"
        ruta.mkdir(parents=True)
        for nombre in ("media", "montaje", "entregas"):
            if (self.e / nombre).is_dir():
                shutil.copytree(self.e / nombre, ruta / nombre)
        return ruta

    def test_a01_a02_t01_t02_alta_y_reintento(self):
        self.idea()
        crear_semana(self.r, SEMANA)
        validar_operacion(self.r)
        anterior = self.s.read_bytes()
        with self.assertRaisesRegex(ValueError, "Ya existe"):
            crear_semana(self.r, SEMANA)
        with self.assertRaisesRegex(ValueError, "Semana ISO inválida"):
            crear_semana(self.r, "2027-W53")
        p = self.r / "templates/CIERRE.md"
        temp = p.rename(p.with_suffix(".guardado"))
        with self.assertRaisesRegex(ValueError, "Falta plantilla"):
            crear_video(self.r, SEMANA, VIDEO, "miminiapp", IDEA, "FIXTURE")
        self.assertFalse(self.e.exists())
        temp.rename(p)
        crear_video(self.r, SEMANA, VIDEO, "miminiapp", IDEA, "FIXTURE")
        with self.assertRaisesRegex(ValueError, "Ya existe"):
            crear_video(self.r, SEMANA, VIDEO, "miminiapp", IDEA, "FIXTURE")
        with self.assertRaisesRegex(ValueError, "inválido"):
            crear_video(self.r, SEMANA, "../videos", "miminiapp", IDEA, "FIXTURE")
        self.assertEqual(set(x.name for x in self.e.iterdir()), set(DOCS_VIDEO))
        self.assertEqual(anterior, self.s.read_bytes())
        self.assertNotIn("{{", self.g.read_text(encoding="utf-8"))
        validar_operacion(self.r)

    def test_a03_proyectos_y_reprogramacion(self):
        self.alta()
        carpeta = self.r / "proyectos/tutorial-git"
        carpeta.mkdir()
        (carpeta / "PROYECTO.md").write_text("# Tutorial Git\n\n## Control\n\n- Proyecto: tutorial-git\n- Creador: Alexander\n- Estado: FIXTURE\n", encoding="utf-8")
        self.idea("I-0002", "tutorial-git")
        crear_video(self.r, SEMANA, "VID-0002", "tutorial-git", "I-0002", "FIXTURE")
        plantilla = self.s.read_bytes()
        self.semana_aprobada(self.s, SEMANA, [(IDEA, "miminiapp"), ("I-0002", "tutorial-git")])
        validar_operacion(self.r)
        otra = crear_semana(self.r, OTRA) / "SEMANA.md"
        self.semana_aprobada(otra, OTRA, [("I-0002", "tutorial-git")])
        with self.assertRaisesRegex(ValueError, "dos lotes"):
            validar_operacion(self.r)
        self.s.write_bytes(plantilla)
        self.semana_aprobada(self.s, SEMANA, [(IDEA, "miminiapp")])
        validar_operacion(self.r)
        self.assertTrue((self.r / "videos/VID-0002/GUION.md").is_file())

    def test_a04_a05_a13_guion_traspaso_y_claim(self):
        self.guion_aprobado()
        digest = huellas(self.r, VIDEO)["OK-2"]
        self.material("hyperframes/s01.html", b"<html>Fixture</html>")
        modificar(self.p, "- Dossier manual y perfil autorizado:", f"- Dossier manual y perfil autorizado: {VIDEO}, v01, {digest}, TEMP. S01, 30 frames, voz guía. S02, 30 frames, silencio. [Fuente](hyperframes/s01.html)")
        validar_operacion(self.r)
        resultado = subprocess.run([sys.executable, "-B", str(self.r / "scripts/validar_paquete.py"), "huellas", VIDEO], capture_output=True, check=True, text=True)
        self.assertIn(digest, resultado.stdout)
        modificar(self.p, "(hyperframes/s01.html)", "(hyperframes/no-existe.html)")
        with self.assertRaisesRegex(ValueError, "Enlace roto"):
            validar_operacion(self.r)
        modificar(self.p, "(hyperframes/no-existe.html)", "(hyperframes/s01.html)")
        modificar(self.g, "- Version: v01", "- Version: v02")
        with self.assertRaisesRegex(ValueError, "OK-2: aprobación obsoleta"):
            validar_operacion(self.r)
        modificar(self.g, "- Version: v02", "- Version: v01")
        modificar(self.g, "| C01 | P | CONFORME", "| C01 | X | CONFORME")
        with self.assertRaisesRegex(ValueError, "Claim sin prueba"):
            validar_operacion(self.r)

    def test_a07_timing_master_y_historico(self):
        _, master = self.cierre_aprobado()
        validar_operacion(self.r)
        modificar(self.p, "- Timing, voz guía y sustituciones:", "- Timing, voz guía y sustituciones: cambiado")
        with self.assertRaisesRegex(ValueError, "Picture lock: aprobación obsoleta"):
            validar_operacion(self.r)
        modificar(self.p, "- Timing, voz guía y sustituciones: cambiado", "- Timing, voz guía y sustituciones:")
        original = master.read_bytes()
        master.write_bytes(b"mock-video-2")
        with self.assertRaisesRegex(ValueError, "Cambió el máster"):
            validar_operacion(self.r)
        master.write_bytes(original)
        self.publicacion("YT", "PUBLICADA", "https://youtube.invalid/fixture")
        cierres = leer_md(self.c)
        nombres = ("Control", "Derechos", "QC", "Plan de publicación", "OK-3", "Autorización de publicación", "Publicaciones")
        historia = "\n\n".join(f"## {s} [v01]\n\n{cierres[s]}" for s in nombres)
        nueva = (self.r / "templates/CIERRE.md").read_text(encoding="utf-8").replace("{{VIDEO}}", VIDEO).replace("Revision_cierre: v01", "Revision_cierre: v02")
        self.c.write_text(nueva + "\n\n" + historia + "\n", encoding="utf-8")
        modificar(self.p, "Estado: BORRADOR", "Estado: PUBLICADO")
        validar_operacion(self.r)
        self.assertEqual(master.read_bytes(), original)

    def test_a08_a09_publicacion_y_metricas(self):
        self.cierre_aprobado()
        fila(self.c, "Publicaciones", f"| {VIDEO}-YT-01 | PUBLICADA | {TS} | https://youtube.invalid/v | Simulada |")
        with self.assertRaisesRegex(ValueError, "autorización de publicación independiente"):
            validar_operacion(self.r)
        self.publicacion("YT", "PUBLICADA", "https://youtube.invalid/v")
        # Conservar un solo registro del acto simulado.
        texto = self.c.read_text(encoding="utf-8")
        self.c.write_text(texto.replace(f"| {VIDEO}-YT-01 | PUBLICADA | {TS} | https://youtube.invalid/v | Simulada |\n", ""), encoding="utf-8")
        self.publicacion("IG", "FALLIDA", "")
        validar_operacion(self.r)
        fila(self.c, "Publicaciones", f"| {VIDEO}-YT-01 | PUBLICADA | {TS} | https://youtube.invalid/v | Duplicado |")
        with self.assertRaisesRegex(ValueError, "Publicación repetido"):
            validar_operacion(self.r)
        texto = self.c.read_text(encoding="utf-8")
        self.c.write_text(texto.replace(f"| {VIDEO}-YT-01 | PUBLICADA | {TS} | https://youtube.invalid/v | Duplicado |\n", ""), encoding="utf-8")
        modificar(self.c, f"| {VIDEO}-IG-01 | FALLIDA | {TS} |  |", f"| {VIDEO}-IG-01 | PUBLICADA | {TS} | https://instagram.invalid/v |")
        r = self.r / "registro/METRICAS.csv"
        registrar(r, [f"{VIDEO}-YT-01", "YouTube", "2026-11-10T10:00:00+01:00", "vistas", 0, "vistas", 100, "+48 h", "Fixture YT", "DISPONIBLE"])
        registrar(r, [f"{VIDEO}-YT-01", "YouTube", "2026-11-15T10:00:00+01:00", "vistas", 5, "vistas", 100, "+7 d", "Fixture YT", "DISPONIBLE"])
        registrar(r, [f"{VIDEO}-IG-01", "Instagram", "2026-11-10T10:00:00+01:00", "alcance", "", "personas", "", "+48 h", "Fixture IG", "NO_DISPONIBLE"])
        validar_operacion(self.r)
        obs = list(csv_filas(r, METRICAS_CSV))
        self.assertEqual([(x["plataforma"], x["valor"], x["ventana"]) for x in obs], [
            ("YouTube", "0", "+48 h"), ("YouTube", "5", "+7 d"), ("Instagram", "", "+48 h")])

    def test_a10_a11_a12_t03_t04_t05_archivo(self):
        _, master = self.cierre_aprobado()
        self.publicacion("YT", "PUBLICADA", "https://youtube.invalid/fixture")
        modificar(self.p, "Estado: BORRADOR", "Estado: PUBLICADO")
        registrar(self.r / "registro/METRICAS.csv", [f"{VIDEO}-YT-01", "YouTube", "2026-11-10T10:00:00+01:00", "vistas", 0, "vistas", 100, "+48 h", "Fixture YT", "DISPONIBLE"])
        original = self.material("media/camera/original/origen.bin", b"captura")
        modificar(self.p, "- Dossier manual y perfil autorizado:", "- Dossier manual y perfil autorizado: [Original](media/camera/original/origen.bin)")
        fuera = self.e / "dependencia.bin"
        fuera.write_bytes(b"indefinida")
        with self.assertRaisesRegex(ValueError, "fuera del alcance"):
            self.archivo("inventariar")
        fuera.unlink()
        self.assertEqual(self.archivo("inventariar"), "LOCAL")
        with self.assertRaisesRegex(ValueError, "Falta preparación"):
            self.archivo("registrar-offline", "--retirada", "fixture")
        logica = f"{VIDEO}/v01"
        with self.assertRaisesRegex(ValueError, "disjuntos"):
            self.archivo("verificar", "--soporte", "X", "--destino", self.e, "--relativa", VIDEO)
        a, b = self.copia("a"), self.copia("b")
        copia_a = a / original.relative_to(self.e)
        copia_a.write_bytes(b"xxxxxxx")
        with self.assertRaisesRegex(ValueError, "alterada"):
            self.archivo("verificar", "--soporte", "A", "--destino", a, "--relativa", logica)
        copia_a.write_bytes(b"captura")
        for etiqueta, ruta in (("A", a), ("B", b)):
            self.archivo("verificar", "--soporte", etiqueta, "--destino", ruta, "--relativa", logica)
        with self.assertRaisesRegex(ValueError, "mismo destino"):
            self.archivo("verificar", "--soporte", "C", "--destino", a, "--relativa", logica)
        prep = ["--soportes", "A", "B", "--aprobador", "Alexander", "--evidencia", "Fixture"]
        with self.assertRaisesRegex(ValueError, "independientes"):
            self.archivo("preparar-retiro", "--soportes", "A", "--aprobador", "Alexander", "--evidencia", "Fixture")
        original.write_bytes(b"cambio origen")
        with self.assertRaisesRegex(ValueError, "Origen cambió"):
            self.archivo("preparar-retiro", *prep)
        original.write_bytes(b"captura")
        manifiesto = self.e / "ARCHIVO.json"
        datos = json_leer(manifiesto)
        datos["versiones"]["v01"]["copias"]["B"]["verificada_en"] = (ahora() - timedelta(hours=25)).isoformat()
        json_guardar(manifiesto, datos)
        with self.assertRaisesRegex(ValueError, "caducada"):
            self.archivo("preparar-retiro", *prep)
        self.archivo("verificar", "--soporte", "B", "--destino", b, "--relativa", logica)
        self.archivo("preparar-retiro", *prep)
        with self.assertRaisesRegex(ValueError, "siguen presentes"):
            self.archivo("registrar-offline", "--retirada", "Fixture")
        ligeros = {p.name: p.read_bytes() for p in (self.g, self.p, self.c)}
        for nombre in json_leer(manifiesto)["versiones"]["v01"]["archivos"]:
            (self.e / nombre).unlink()
        self.assertEqual(self.archivo("registrar-offline", "--retirada", "Retirada de bytes ficticios"), "OFFLINE")
        suspendida = a.rename(a.with_name("desconectada"))
        validar_operacion(self.r)
        self.assertEqual(campos(leer_md(self.g), "Control")["Idea"], IDEA)
        self.assertIn("youtube.invalid", self.c.read_text(encoding="utf-8"))
        observacion = next(csv_filas(self.r / "registro/METRICAS.csv", METRICAS_CSV))
        self.assertEqual((observacion["valor"], observacion["disponibilidad"]), ("0", "DISPONIBLE"))
        suspendida.rename(a)
        salida = self.entorno / "restaurado"
        rel = master.relative_to(self.e).as_posix()
        with self.assertRaisesRegex(ValueError, "destino nuevo"):
            self.archivo("recuperar", "--soporte", "A", "--destino", a, "--salida", self.e, "--archivos", rel)
        self.assertEqual(self.archivo("recuperar", "--soporte", "A", "--destino", a, "--salida", salida, "--archivos", rel), "RESTAURADO_TEMPORAL")
        self.assertEqual(hash_archivo(salida / rel), hash_archivo(a / rel))
        self.assertEqual(ligeros, {p.name: p.read_bytes() for p in (self.g, self.p, self.c)})
        self.assertFalse(master.exists())
        validar_operacion(self.r)
        self.material("entregas/master_v02.mp4", b"nuevo ensayo")
        self.assertEqual(self.archivo("inventariar", version="v02"), "LOCAL")
        validar_operacion(self.r)
        segundo = self.entorno / "recuperacion-historica"
        self.assertEqual(self.archivo("recuperar", "--soporte", "A", "--destino", a, "--salida", segundo, "--archivos", rel),
                         "RESTAURADO_TEMPORAL")
        self.assertEqual(hash_archivo(segundo / rel), hash_archivo(a / rel))
        validar_operacion(self.r)

    def test_a14_t06_t07_faltantes_y_marca(self):
        validar_legado(self.r)
        manifiesto = self.r / "MANIFEST_RELEASE.json"
        archivos = {n: hash_archivo(p) for n, p in archivos_relativos(self.r).items() if n != manifiesto.name}
        json_guardar(manifiesto, {"version": VERSION_PAQUETE, "algoritmo": "sha256", "files": archivos})
        validar_release(self.r)
        self.alta()
        validar_operacion(self.r)
        with self.assertRaisesRegex(ValueError, "Manifiesto incompleto"):
            validar_release(self.r)
        json_guardar(manifiesto, {"version": VERSION_PAQUETE, "algoritmo": "sha256", "files": {}})
        with self.assertRaisesRegex(ValueError, "vacío"):
            validar_release(self.r)
        self.c.unlink()
        with self.assertRaisesRegex(ValueError, "Falta documento"):
            validar_operacion(self.r)
        tokens = self.r / "marca/identidad.json"
        modificar(tokens, '"#0B1020"', '"color inválido"')
        with self.assertRaisesRegex(ValueError, "Token de color"):
            validar_operacion(self.r)
        modificar(tokens, '"color inválido"', '"#0B1020"')
        marca = self.r / "marca/IDENTIDAD.md"
        modificar(marca, "- Perfil: PENDIENTE", "- Perfil: PUBLICO-v01")
        with self.assertRaisesRegex(ValueError, "Aprobador"):
            validar_operacion(self.r)

    def test_a14_temp_y_aprobacion_de_entrega(self):
        self.cierre_aprobado()
        modificar(self.g, "- Modo: FIXTURE", "- Modo: INTERNO")
        modificar(self.g, f"- Huella: {campos(leer_md(self.g), 'OK-2')['Huella']}", f"- Huella: {huellas(self.r, VIDEO)['OK-2']}")
        modificar(self.p, f"- Huella: {campos(leer_md(self.p), 'Picture lock')['Huella']}", f"- Huella: {huellas(self.r, VIDEO)['Picture lock']}")
        modificar(self.c, f"- Huella_corte: {campos(leer_md(self.c), 'Control')['Huella_corte']}", f"- Huella_corte: {huellas(self.r, VIDEO)['Picture lock']}")
        modificar(self.c, f"- Huella: {campos(leer_md(self.c), 'OK-3')['Huella']}", f"- Huella: {huellas(self.r, VIDEO)['OK-3']}")
        validar_operacion(self.r)
        huella = huellas(self.r, VIDEO)["OK-3"]
        fila(self.c, "Autorización de publicación", f"| {VIDEO}-YT-01 | {huella} | Alexander | 2026-11-08 | Fixture | PUBLICO-v01 | https://youtube.com/@fixture |")
        with self.assertRaisesRegex(ValueError, "TEMP o marca pendiente"):
            validar_operacion(self.r)
        modificar(self.c, "- Tecnico: CONFORME", "- Tecnico: PENDIENTE")
        with self.assertRaisesRegex(ValueError, "OK-3: aprobación obsoleta"):
            validar_operacion(self.r)


if __name__ == "__main__":
    unittest.main(verbosity=2)
