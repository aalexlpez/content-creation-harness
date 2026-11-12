"""Pruebas del marco. Cada prueba trabaja sobre una copia temporal del repositorio.

Ejecutar desde la raíz:  python -m unittest discover -s pruebas -v
"""
import io
import shutil
import subprocess
import sys
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
sys.dont_write_bytecode = True
sys.path.insert(0, str(RAIZ / "scripts"))

import marco  # noqa: E402
import medios  # noqa: E402
import reglas  # noqa: E402
from nucleo import Doc, ErrorMarco, escribir_csv, leer_csv, CAB_CUENTAS  # noqa: E402

SEMANA = "2026-W46"
COPIAR = ["templates", "registro", "marca", "proyectos", "guias", "referencias", "CLAUDE.md", "README.md", "AGENTS.md", "CHANGELOG.md", "pruebas"]


def rellenar_guion(r: Path, vid: str, claim_tipo="P"):
    doc = Doc(r / "videos" / vid / "GUION.md")
    for clave in ("Audiencia", "Objetivo", "Pilar", "Familia", "Promesa", "Prueba_visual", "CTA", "Duracion",
                  "Ritmo", "Musica", "Texto_en_pantalla", "Color"):
        doc.poner_campo("Brief", clave, f"valor de {clave}")
    doc.anadir_linea("Ganchos", "| G1 | ¿Cuántas veces pegaste lo mismo? | problema | 7 | sí |")
    doc.anadir_linea("Escenas", "| S01 | 00:00–00:04 | Hola \\| adiós | Plano a cámara | Voz sola | T1 | C1 |")
    doc.anadir_linea("Claims", f"| C1 | {claim_tipo} | Quita duplicados | Probado con lista de ejemplo |")
    doc.guardar()


def rellenar_cierre(r: Path, vid: str, plan=True):
    doc = Doc(r / "videos" / vid / "CIERRE.md")
    for k in reglas.QC_CAMPOS:
        doc.poner_campo("QC", k, "CONFORME")
    doc.anadir_linea("Derechos", "| Voz e imagen | propio | Grabación de Alexander | todas |")
    if plan:
        doc.anadir_linea("Plan de publicación", f"| {vid}-YT-01 | YouTube | media/entregas/m.mp4 | copy |")
    doc.guardar()


def crear_master(r: Path, vid: str, contenido=b"master v1") -> str:
    ruta = r / "videos" / vid / "media" / "entregas" / "m.mp4"
    ruta.parent.mkdir(parents=True, exist_ok=True)
    ruta.write_bytes(contenido)
    return "media/entregas/m.mp4"


class Base(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory(prefix="marco-")
        self.r = Path(self._tmp.name) / "repo"
        self.r.mkdir()
        for nombre in COPIAR:
            origen = RAIZ / nombre
            if origen.is_dir():
                shutil.copytree(origen, self.r / nombre)
            elif origen.is_file():
                shutil.copy2(origen, self.r / nombre)
        (self.r / "semanas").mkdir()
        (self.r / "videos").mkdir()

    def tearDown(self):
        self._tmp.cleanup()

    def errores(self):
        return reglas.validar(self.r).errores

    def assertConforme(self):
        self.assertEqual(self.errores(), [])

    def cli(self, *args):
        salida, err = io.StringIO(), io.StringIO()
        with redirect_stdout(salida), redirect_stderr(err):
            codigo = marco.main(["--raiz", str(self.r), *args])
        return codigo, salida.getvalue() + err.getvalue()

    def preparar(self, ensayo=False):
        reglas.crear_idea(self.r, "miminiapp", "Limpiar duplicados", "listas con repetidos")
        reglas.crear_semana(self.r, SEMANA, "6", "Gancho por problema")
        vid, _ = reglas.crear_video(self.r, "I-0001", SEMANA, ensayo)
        return vid

    def verificar_cuenta(self, plataforma="YouTube"):
        ruta = self.r / "marca" / "CUENTAS.csv"
        filas = leer_csv(ruta, CAB_CUENTAS)
        for f in filas:
            if f["plataforma"] == plataforma:
                f.update(alias="alexenbeta", estado="VERIFICADA", url="https://www.youtube.com/@alexenbeta",
                         fecha_verificacion="2026-11-12", evidencia="captura")
        escribir_csv(ruta, CAB_CUENTAS, filas)


class RepositorioReal(unittest.TestCase):
    def test_repositorio_actual_conforme(self):
        inf = reglas.validar(RAIZ)
        self.assertEqual(inf.errores, [], "\n".join(inf.errores))


class Altas(Base):
    def test_semana_recien_creada_valida(self):
        reglas.crear_semana(self.r, SEMANA)
        self.assertConforme()

    def test_ids_automaticos_y_enlace_al_lote(self):
        vid = self.preparar()
        self.assertEqual(vid, "VID-0001")
        lote = Doc(reglas.ruta_semana(self.r, SEMANA)).tabla("Lote")
        self.assertEqual(lote[0]["idea_id"], "I-0001")
        self.assertEqual(lote[0]["video_id"], "VID-0001")
        self.assertEqual(reglas.ideas(self.r)[0]["estado"], "SELECCIONADA")
        reglas.crear_idea(self.r, "miminiapp", "Segunda")
        vid2, _ = reglas.crear_video(self.r, "I-0002", SEMANA)
        self.assertEqual(vid2, "VID-0002")
        self.assertConforme()

    def test_rechazos(self):
        reglas.crear_semana(self.r, SEMANA)
        with self.assertRaisesRegex(ErrorMarco, "Ya existe"):
            reglas.crear_semana(self.r, SEMANA)
        with self.assertRaisesRegex(ErrorMarco, "no existe en el calendario"):
            reglas.crear_semana(self.r, "2027-W53")
        with self.assertRaisesRegex(ErrorMarco, "no está en registro"):
            reglas.crear_video(self.r, "I-0009", SEMANA)
        with self.assertRaisesRegex(ErrorMarco, "Idea inválida"):
            reglas.crear_video(self.r, "../x", SEMANA)
        with self.assertRaisesRegex(ErrorMarco, "No existe el proyecto"):
            reglas.crear_idea(self.r, "noexiste", "x")
        with self.assertRaisesRegex(ErrorMarco, "Proyecto inválido"):
            reglas.crear_proyecto(self.r, "Mal Nombre", "")

    def test_plantilla_ausente_no_deja_restos(self):
        reglas.crear_idea(self.r, "miminiapp", "x")
        reglas.crear_semana(self.r, SEMANA)
        (self.r / "templates" / "CIERRE.md").unlink()
        with self.assertRaisesRegex(ErrorMarco, "Falta la plantilla"):
            reglas.crear_video(self.r, "I-0001", SEMANA)
        self.assertEqual(list((self.r / "videos").iterdir()), [])

    def test_proyecto_nuevo(self):
        reglas.crear_proyecto(self.r, "tutorial-git", "Tutorial Git")
        reglas.crear_idea(self.r, "tutorial-git", "Ramas en 30 s")
        self.assertConforme()


class FlujoEnsayo(Base):
    def test_flujo_completo_ensayo(self):
        vid = self.preparar(ensayo=True)
        with self.assertRaisesRegex(ErrorMarco, "Escenas está vacía"):
            reglas.aprobar(self.r, "OK-2", vid, "chat")
        rellenar_guion(self.r, vid, claim_tipo="X")
        with self.assertRaisesRegex(ErrorMarco, "es X"):
            reglas.aprobar(self.r, "OK-2", vid, "chat")
        g = self.r / "videos" / vid / "GUION.md"
        g.write_text(g.read_text(encoding="utf-8").replace("| C1 | X |", "| C1 | P |"), encoding="utf-8")
        # ENSAYO no necesita OK-1.
        reglas.aprobar(self.r, "OK-2", vid, "Ale en chat: OK-2")
        v = reglas.Video.cargar(self.r, vid)
        self.assertEqual(v.estado, "GUION_APROBADO")
        self.assertConforme()

        # Editar el guion aprobado: error porque el estado exige OK-2.
        g.write_text(g.read_text(encoding="utf-8").replace("Plano a cámara", "Plano lateral"), encoding="utf-8")
        self.assertTrue(any("cambió después del OK-2" in e for e in self.errores()))
        reglas.aprobar(self.r, "OK-2", vid, "Ale en chat: OK-2 v02")
        self.assertConforme()

        reglas.mover(self.r, vid, "EN_PRODUCCION", siguiente="Grabar")
        with self.assertRaisesRegex(ErrorMarco, "exige OK-3"):
            reglas.mover(self.r, vid, "LISTO")
        master = crear_master(self.r, vid)
        with self.assertRaisesRegex(ErrorMarco, "QC debe estar CONFORME"):
            reglas.aprobar(self.r, "OK-3", vid, "chat", master=master)
        rellenar_cierre(self.r, vid, plan=False)
        reglas.aprobar(self.r, "OK-3", vid, "Ale en chat: OK-3", master=master)
        self.assertEqual(reglas.Video.cargar(self.r, vid).estado, "LISTO")
        self.assertConforme()
        with self.assertRaisesRegex(ErrorMarco, "ENSAYO"):
            reglas.mover(self.r, vid, "PUBLICADO")

        # Máster sustituido: error.
        crear_master(self.r, vid, b"otro contenido")
        self.assertTrue(any("no coincide con el aprobado" in e for e in self.errores()))
        # Máster ausente (otro equipo): solo aviso.
        (self.r / "videos" / vid / master).unlink()
        inf = reglas.validar(self.r)
        self.assertEqual(inf.errores, [])
        self.assertTrue(any("no está en este equipo" in a for a in inf.avisos))

    def test_crlf_no_invalida_aprobaciones(self):
        vid = self.preparar(ensayo=True)
        rellenar_guion(self.r, vid)
        reglas.aprobar(self.r, "OK-2", vid, "chat")
        for md in self.r.rglob("*.md"):
            datos = md.read_bytes().replace(b"\r\n", b"\n").replace(b"\n", b"\r\n")
            md.write_bytes(b"\xef\xbb\xbf" + datos)  # CRLF y BOM, como un editor de Windows
        self.assertConforme()
        self.assertTrue(reglas.vigente(reglas.Video.cargar(self.r, vid).guion, "OK-2",
                                       reglas.huella_ok2(reglas.Video.cargar(self.r, vid))))

    def test_espacios_y_alineacion_no_invalidan(self):
        vid = self.preparar(ensayo=True)
        rellenar_guion(self.r, vid)
        reglas.aprobar(self.r, "OK-2", vid, "chat")
        g = self.r / "videos" / vid / "GUION.md"
        texto = g.read_text(encoding="utf-8").replace("| S01 | 00:00–00:04 |", "|   S01   |00:00–00:04|   ")
        g.write_text(texto.replace("## Notas de revisión\n", "## Notas de revisión\n\nAle: me gusta.  \n"), encoding="utf-8")
        self.assertConforme()


class FlujoNormal(Base):
    def test_publicacion_y_metricas(self):
        vid = self.preparar()
        rellenar_guion(self.r, vid)
        with self.assertRaisesRegex(ErrorMarco, "OK-1 vigente"):
            reglas.aprobar(self.r, "OK-2", vid, "chat")
        reglas.aprobar(self.r, "OK-1", SEMANA, "chat")
        reglas.aprobar(self.r, "OK-2", vid, "chat")
        master = crear_master(self.r, vid)
        rellenar_cierre(self.r, vid)
        reglas.aprobar(self.r, "OK-3", vid, "chat", master=master)

        cierre = self.r / "videos" / vid / "CIERRE.md"
        doc = Doc(cierre)
        doc.anadir_linea("Publicaciones", f"| {vid}-YT-01 | 2026-11-13 | https://youtube.com/shorts/abc | |")
        doc.guardar()
        self.assertTrue(any("no está VERIFICADA" in e for e in self.errores()))
        self.verificar_cuenta()
        reglas.mover(self.r, vid, "PUBLICADO")
        self.assertConforme()

        met = self.r / "registro" / "METRICAS.csv"
        with open(met, "a", encoding="utf-8", newline="\n") as f:
            f.write(f"{vid}-YT-01,YouTube,2026-11-15,+48h,Visualizaciones,120,vistas,,YouTube Studio,DISPONIBLE\n")
            f.write(f"{vid}-YT-01,YouTube,2026-11-15,+48h,Suscriptores ganados,,personas,,YouTube Studio,NO_DISPONIBLE\n")
        self.assertConforme()
        with open(met, "a", encoding="utf-8", newline="\n") as f:
            f.write(f"{vid}-TT-01,TikTok,2026-11-15,+48h,Vistas,0,vistas,,TikTok Studio,DISPONIBLE\n")
            f.write(f"{vid}-YT-01,YouTube,15/11/2026,48h,Vistas,1,vistas,,YT,NO_DISPONIBLE\n")
        errores = "\n".join(self.errores())
        self.assertIn("no figura como publicado", errores)
        self.assertIn("fecha_observacion", errores)
        self.assertIn("ventana", errores)
        self.assertIn("NO_DISPONIBLE va con valor vacío", errores)

    def test_cambio_en_lote_caduca_ok1(self):
        self.preparar()
        reglas.aprobar(self.r, "OK-1", SEMANA, "chat")
        reglas.crear_idea(self.r, "miminiapp", "Otra")
        _, avisos = reglas.crear_video(self.r, "I-0002", SEMANA)
        self.assertTrue(avisos)
        inf = reglas.validar(self.r)
        self.assertTrue(any("OK-1 caducado" in a for a in inf.avisos))

    def test_idea_en_dos_lotes_y_proyecto_incoherente(self):
        self.preparar()
        reglas.crear_semana(self.r, "2026-W47")
        doc = Doc(reglas.ruta_semana(self.r, "2026-W47"))
        doc.anadir_linea("Lote", "| I-0001 | | 2 | duplicada |")
        doc.guardar()
        self.assertTrue(any("ya está en el lote" in e for e in self.errores()))

    def test_bloqueado_necesita_motivo(self):
        vid = self.preparar()
        with self.assertRaisesRegex(ErrorMarco, "motivo"):
            reglas.mover(self.r, vid, "BLOQUEADO")
        reglas.mover(self.r, vid, "BLOQUEADO", bloqueo="Falta la miniapp")
        self.assertConforme()


class Integridad(Base):
    def test_enlace_roto_y_tabla_mal_formada(self):
        (self.r / "guias" / "EXTRA.md").write_text("Ver [nada](NOEXISTE.md)\n", encoding="utf-8")
        self.assertTrue(any("enlace roto" in e for e in self.errores()))
        (self.r / "guias" / "EXTRA.md").unlink()
        vid = self.preparar(ensayo=True)
        doc = Doc(self.r / "videos" / vid / "GUION.md")
        doc.anadir_linea("Claims", "| C1 | P | sin cuarta columna |")
        doc.guardar()
        self.assertTrue(any("columnas" in e for e in self.errores()))

    def test_csv_mal_formado(self):
        with open(self.r / "registro" / "IDEAS.csv", "a", encoding="utf-8") as f:
            f.write("I-0001,miminiapp,2026-11-12,falta columnas\n")
        self.assertTrue(self.errores())

    def test_medios_inventario_y_copia(self):
        vid = self.preparar(ensayo=True)
        crear_master(self.r, vid)
        (self.r / "videos" / vid / "media" / "originales").mkdir(parents=True)
        (self.r / "videos" / vid / "media" / "originales" / "toma1.mp4").write_bytes(b"\x00" * 1000)
        ruta, n = medios.inventariar(self.r, vid)
        self.assertEqual(n, 2)
        self.assertEqual(medios.comprobar(self.r, vid), [])
        copia = Path(self._tmp.name) / "disco" / "media"
        shutil.copytree(self.r / "videos" / vid / "media", copia)
        self.assertEqual(medios.comprobar(self.r, vid, str(copia)), [])
        (copia / "originales" / "toma1.mp4").write_bytes(b"\x01" * 1000)
        (copia / "entregas" / "m.mp4").unlink()
        problemas = medios.comprobar(self.r, vid, str(copia))
        self.assertIn("distinto originales/toma1.mp4", problemas)
        self.assertIn("falta entregas/m.mp4", problemas)


class Cli(Base):
    def test_ordenes_basicas(self):
        self.assertEqual(self.cli("idea", "miminiapp", "Desde CLI")[0], 0)
        self.assertEqual(self.cli("semana", SEMANA, "--horas", "4")[0], 0)
        codigo, texto = self.cli("video", "I-0001", "--semana", SEMANA, "--ensayo")
        self.assertEqual(codigo, 0, texto)
        codigo, texto = self.cli("estado")
        self.assertIn("VID-0001 ENSAYO", texto)
        self.assertEqual(self.cli("validar")[0], 0)
        codigo, texto = self.cli("aprobar", "OK-2", "VID-0001", "--evidencia", "x")
        self.assertEqual(codigo, 2)
        self.assertIn("Escenas", texto)
        self.assertEqual(self.cli("huellas", "VID-0001")[0], 0)

    def test_ejecutable_desde_otra_carpeta(self):
        r = subprocess.run([sys.executable, str(RAIZ / "scripts" / "marco.py"), "--raiz", str(self.r), "estado"],
                           cwd=tempfile.gettempdir(), capture_output=True, text=True, encoding="utf-8")
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("Ideas:", r.stdout)


@unittest.skipUnless(shutil.which("ffmpeg") and shutil.which("ffprobe"), "ffmpeg/ffprobe no disponibles")
class Inspector(Base):
    def generar(self, nombre, *opciones):
        ruta = Path(self._tmp.name) / nombre
        subprocess.run(["ffmpeg", "-v", "error", "-y", *opciones, str(ruta)], check=True)
        return ruta

    def test_conforme_y_falla(self):
        bueno = self.generar(
            "bueno.mp4", "-f", "lavfi", "-i", "color=c=blue:s=1080x1920:r=30:d=1", "-f", "lavfi",
            "-i", "sine=f=440:sample_rate=48000:d=1", "-c:v", "libx264", "-pix_fmt", "yuv420p",
            "-colorspace", "bt709", "-color_primaries", "bt709", "-color_trc", "bt709",
            "-c:a", "aac", "-shortest")
        r = medios.inspeccionar(self.r, str(bueno))
        self.assertIn(r["resultado"], {"OK", "REVISAR"}, r)
        self.assertEqual(r["controles"]["resolucion"]["estado"], "OK")
        malo = self.generar("malo.mp4", "-f", "lavfi", "-i", "color=c=red:s=320x240:r=25:d=1",
                            "-c:v", "mpeg4")
        r = medios.inspeccionar(self.r, str(malo))
        self.assertEqual(r["resultado"], "FALLA")
        self.assertEqual(r["controles"]["audio"]["estado"], "FALLA")


if __name__ == "__main__":
    unittest.main()
