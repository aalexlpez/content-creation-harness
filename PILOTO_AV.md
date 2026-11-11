# P0.4 · Prueba audiovisual interna

**Estado:** preparada. Falta grabación autorizada de Samsung/DJI, confirmar el flujo gratuito en CapCut y comprobar HyperFrames en una instalación existente o autorizada. El resultado se mantiene TEMP y privado.

## Inventario comprobado el 8 de noviembre de 2026

| Elemento | Resultado |
|---|---|
| Windows | Entorno de pruebas disponible |
| Python / Node | 3.12.14 / 24.22.1 localizados |
| CapCut Desktop | Binario 9.7.1.4203 localizado. Flujo de exportación gratuita y reapertura pendientes |
| FFmpeg / ffprobe | Binarios localizados en el directorio de CapCut. PATH no los resuelve |
| HyperFrames / Shotcut | No localizados en PATH o en las ubicaciones de instalación revisadas |
| Material Samsung/DJI | No se seleccionó ni se accedió a grabaciones personales |
| Evidencia v3.5 | Piloto archivado, 8 s sin pista de voz. Sirve como referencia de la prueba anterior |

## Preparación y permiso

Alexander aporta un original vertical de unos 15–25 s del Samsung con voz DJI, sin datos sensibles y con un gesto o frase reconocible cerca del inicio y del final. Indica la ruta exacta de ese archivo o lo adjunta. Autoriza abrir ese archivo y el editor en una carpeta de ensayo. Si HyperFrames ya existe, indica la carpeta o binario. Si falta, autoriza por separado la instalación gratuita tras acordar versión y procedencia. Shotcut solo requiere instalación aparte si se elige la contingencia. No es necesario conceder acceso a toda la biblioteca ni a cuentas.

## Dossier técnico del ensayo

Propuesta de timing para un clip de 18 s, ajustable tras ingesta. Perfil 1080×1920/30 CFR SDR BT.709. El guion, hash, tomas y permisos se completan con material autorizado. Los archivos de salida son nuevos y separados de la fuente.

| Escena | Intervalo y cuadros | Imagen / audio | Entrega y revisión |
|---|---|---|---|
| S01 | 0–7 s · cuadros 0–209 | Original de Samsung, voz DJI | Comprobar exposición, foco y primera marca de sincronía |
| S02 | 7–12 s · cuadros 210–359 | Composición propia con rótulo y animación HyperFrames, voz guía separada o silencio | S02_v01.mp4, proyecto y fuente editable. Verificar tres puntos de seek |
| S03 | 12–18 s · cuadros 360–539 | Original de Samsung, voz DJI | Comprobar segunda marca de sincronía y subtítulo final |

Usar el SRT de prueba, una sola pista de voz efectiva y ningún audio con licencia pendiente. Registrar versiones, entradas, rutas relativas, huellas y resultado en PRODUCCION y CIERRE.

## Ensayo

1. Registrar modelo, ajustes efectivos, tiempo inicial y versiones. Ingerir copia intacta, hash y metadatos. Comprobar voz, color, rotación, cadencia y sincronía. Elegir una escena animada propia y de recursos autorizados.
2. Completar el dossier de intercambio. Renderizar la escena vertical con HyperFrames. Probar seek en inicio, medio y final. Entregar escena, voz y [SRT UTF-8 de muestra](pruebas/piloto.srt) con tres líneas en español.
3. En proyecto local, importar, ordenar, cortar, añadir subtítulos y previsualizar. Exportar sin Pro ni marca. Cerrar, reabrir el proyecto desde una ruta de ensayo, confirmar que las fuentes religan y volver a exportar.
4. Comparar exportado y originales en móvil y verificar el archivo con ffprobe. Revisar voz, sincronía al inicio y al final, texto, orientación, SDR, artefactos y tiempos. Anotar tiempo humano y de render. Referencia inicial: 45 min de manipulación con los recursos listos y 10 min para exportar la muestra.
5. Si hay bloqueo Pro, error SRT, audio inesperado o color incorrecto, detener salida. Documentar causa. Repetir solo con una alternativa autorizada y disponible. Para Shotcut fijar modo vertical, V1 para A-roll, V2 para superposiciones, comprobar subtítulos y exportar desde originales.

| Prueba | Evidencia a completar en el ensayo |
|---|---|
| Cámara/DJI, ingesta y hash | PENDIENTE |
| Render HyperFrames y prueba de seek | PENDIENTE |
| Edición, exportación gratuita y reapertura | PENDIENTE |
| Visionado móvil, voz, color y sincronía | PENDIENTE |
| Tiempo humano, render y decisión de ruta | PENDIENTE |
