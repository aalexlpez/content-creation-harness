# Alexander Contenido · candidata 4.0.0-rc.1

**Estado:** candidata P0 para ensayos internos. El [piloto audiovisual](PILOTO_AV.md) y la prueba de archivo con soportes físicos siguen pendientes.

1. Extrae el paquete a una carpeta propia. Mantén [legado v3.5](legado/v3.5/MANIFEST_SHA256.json) como referencia de solo lectura. Verifica el paquete recién extraído con `python -B scripts/validar_paquete.py release`.
2. Lee [operación](OPERACION.md) y [criterios editoriales](EDITORIAL.md). MiMiniApp es un [proyecto](proyectos/miminiapp/PROYECTO.md). Copia la plantilla de proyecto si vas a ensayar otro tema. Marca, alias y cuentas siguen [pendientes](marca/IDENTIDAD.md).
3. Añade una idea al CSV del registro. Abre una semana con `python -B scripts/crear_semana.py semana 2026-W46`. El código es un ejemplo. Rellena horas y lote. Alexander registra OK-1 sobre la huella mostrada.
4. Crea un expediente con `python -B scripts/crear_semana.py video 2026-W46 VID-0001 miminiapp I-0001` tras tener la idea y el proyecto correspondiente. En un ensayo usa otra copia de la candidata y añade `--fixture`.
5. Trabaja en GUION, PRODUCCION y CIERRE. Usa `python -B scripts/validar_paquete.py huellas VID-0001` para revisar versiones y `python -B scripts/validar_paquete.py operacion` para comprobar el estado vivo.
6. Para practicar edición, sigue la receta de prueba y conserva el resultado en una copia de trabajo. Para archivo físico, espera a la validación descrita en operación.

Python 3.11+ con biblioteca estándar. Si `python` abre la tienda o no está disponible, invoca la ruta a una instalación existente. Los scripts operan desde la raíz que los contiene. Los cambios de uso legítimos alteran la huella de release. Usa el modo de operación para documentos vivos.

[Pruebas y pendientes](PRUEBAS.md) · [Changelog](CHANGELOG.md) · [Migración](MIGRACION.csv) · [Fuentes](FUENTES.md)
