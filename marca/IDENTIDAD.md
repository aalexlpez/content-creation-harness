# Identidad de Alexander

**Estado:** identidad visual **v2 aprobada «por ahora» el 2026-11-16** (AV-006). Sustituye a la v1 (PR-002: cian, violeta, lima, Inter y Crimson Text + Mr Dafoe), que Ale aprobó y reemplazó el mismo día. El kit vectorial **v1.2** es una **reconstrucción**, no un archivo maestro: sirve para trabajar, y sus pendientes están al final. La tipografía pasó a Plus Jakarta Sans el mismo día (AV-007). Se congela durante al menos cinco vídeos publicados y solo cambia con una decisión registrada. Tokens en [identidad.json](identidad.json).

## Quién es el canal

- El creador es **Alexander**, desarrollador, y se presenta como persona (CREATOR-IDENTITY-001).
- MiMiniApp y otros proyectos son proyectos de Alexander. No son el nombre de las cuentas, ni el canal, ni deciden los colores de los vídeos.
- Bien: «Soy Alexander. Estoy construyendo MiMiniApp, una web de pequeñas herramientas…». Mal: «Somos MiMiniApp» o `@miminiapp` en las cuentas personales.
- El nombre del canal es **cerobytes** (CREATOR-ALIAS-003), siempre en minúsculas. Alexander sigue presentándose como persona: «Soy Alexander…».

## Alias (CREATOR-ALIAS-003)

No hubo un alias libre en todas las redes. Ale eligió el 2026-11-12 quedarse con estos, y no se buscan otros:

| Red | Identificador | URL |
|---|---|---|
| YouTube | `@soy.cerobytes` | https://www.youtube.com/@soy.cerobytes |
| TikTok | `@cerobytes` | https://www.tiktok.com/@cerobytes |
| Instagram | `@cer0bytes` (con el número cero) | https://www.instagram.com/cer0bytes/ |
| Facebook | perfil «cerobytes», sin nombre de usuario propio | https://www.facebook.com/p/cerobytes-61596111701428/ |
| X (solo posts con enlace, DIST-X-001) | `@soycerobytes` | https://x.com/soycerobytes |

Detalle verificado en `marca/CUENTAS.csv`. El JSON del tablero los marcaba como pendientes de verificación; la fuente de verdad es el CSV.

Cómo se nombra, ya que los identificadores no coinciden:

- **Voz**: «cerobytes», sin decir arroba ni deletrear.
- **Máster**: sin `@` grabado en la imagen. Si hace falta firma, se escribe «cerobytes» a secas, que vale en todas las redes.
- **Copy, descripción y tarjetas finales de cada red**: el identificador exacto de esa red, según la tabla. En Instagram es `@cer0bytes`, nunca `@cerobytes`.

## Perfil visual v2

**Concepto:** un wordmark contundente en minúsculas acompañado por una barra diagonal independiente («/»). Dirección *creative tech*: minimalismo tecnológico, contraste alto, composición editorial ordenada, formas simples y mucho espacio negativo. Acabados planos y limpios. Personalidad: creativa, tecnológica, minimalista, moderna, clara y profesional.

### Paleta

| Token | HEX | Uso |
|---|---|---|
| Negro | `#0B0B0D` | Texto sobre fondos claros, fondo alternativo |
| Gris carbón | `#1E2937` | Superficies y textos secundarios sobre claro |
| Azul marino profundo | `#0D213F` | Fondo principal oscuro, tarjetas y rótulos |
| Blanco roto | `#F5F6F8` | Fondo claro, texto y símbolo sobre fondos oscuros |
| Azul de la barra (provisional) | `#003571` | Referencia del kit para la barra sobre fondos claros. **No es color oficial** |

Complementos que usa el kit y no son oficiales: texto secundario sobre marino `#B7C0CC`.

- **Tema claro:** fondo `#F5F6F8`, texto `#0B0B0D`, secundario `#1E2937`, marca `#0D213F`.
- **Tema oscuro:** fondo `#0D213F` (alternativo `#0B0B0D`), texto `#F5F6F8`, superficies `#1E2937`, marca `#F5F6F8`.
- **No hay color de acento oficial.** En vídeo, el énfasis se hace por inversión de contraste (caja blanco roto con texto negro), por peso o por tamaño.
- **Contraste medido:** blanco roto sobre marino 14,9:1 y sobre negro 18,2:1. Carbón, marino y negro casi no se distinguen entre sí (1,1 a 1,3:1): sepáralos con un borde fino de blanco roto al 20 % o con el símbolo. La barra `#003571` sobre negro da solo 1,6:1: por eso en la v1.2 `logo-oscuro.svg` ya lleva la barra blanca, y el azul queda solo en los archivos `*-azul-referencia`, que no se usan sobre negro.
- **Descartados (AV-006):** `#54E0EA`, `#AD8BFF`, `#D9F77A`.

### Tipografía

**Plus Jakarta Sans** (AV-007; sustituye a Satoshi): titulares, rótulos y textos de interfaz y piezas sociales. El logotipo es un trazado vectorial, no texto.

- **Incluida en el proyecto:** `marca/fuentes/plus-jakarta-sans/` (Regular, Medium, SemiBold, Bold y ExtraBold, con su `OFL.txt`). Ale la descargó de Google Fonts el 2026-11-16. La licencia es SIL OFL 1.1: se puede guardar en el repositorio, incrustar y usar en vídeo, siempre con su licencia.
- Pesos propuestos, **sin aprobar**: Medium 500 (secundario), Bold 700 (subtítulos y rótulos) y ExtraBold 800 (frases de impacto). La fuente no tiene peso 900. El interletraje sigue por definir.
- Los SVG del kit declaran `font-family='Plus Jakarta Sans', Inter, Arial, sans-serif`, y los **PNG con texto se exportaron con Plus Jakarta Sans** el 2026-11-16 (15 archivos, incluido el rótulo ajustado).
- Descartadas: Satoshi (AV-007) y Crimson Text + Mr Dafoe como acento.

### Logo y símbolo

- **Logo principal:** «cerobytes» en minúsculas con la barra diagonal a la izquierda. El símbolo solo funciona como isotipo (avatar, favicon, icono de perfil, marca de agua y separador).
- **Geometría de la barra:** un paralelogramo, `M 73 4 L 109 4 L 36 134 L 0 134 Z`: 36 de ancho y 130 de alto, inclinado ≈ 29° respecto a la vertical (≈ 61° sobre la horizontal). Se usa con moderación.
- **Variantes:** principal clara (barra marino, nombre negro), oscura (nombre blanco roto), navy (todo blanco roto) e isotipo independiente.
- **Procedencia del wordmark (advertencia):** es vectorial, pero **no es el diseño maestro original**. Es una reconstrucción trazada a partir de un tablero generado con IA; no se recuperó ningún archivo maestro. Las curvas son editables, pero no es texto vivo, y sus bordes pueden verse irregulares en tamaños grandes. Para llamarlo maestro hace falta revisar curvas, espaciado entre letras, tamaños pequeños y criterios ópticos. Hasta entonces no se le llama «maestro» ni «oficial».
- **Sin ®:** el registro de marca no está acreditado. El tablero lo muestra en la maqueta; no se incorpora.
- **No usar** el logo negro sobre fondo oscuro ni el blanco sobre fondo claro. El monograma «cb» no forma parte del concepto.

### Composición

- **Fondos:** superficies claras en blanco roto, franjas profundas en azul marino y, para el logo invertido, negro.
- **Elementos:** barra diagonal repetida con moderación, divisores finos y bloques de texto con jerarquía.
- **Excluido:** circuitos, redes de nodos, hexágonos, bocadillos, cerebros, mallas neuronales, degradado violeta-azul y efectos de ciencia ficción recargados.

### Mensaje

- **Descripción corta:** «Tecnología, desarrollo y proyectos útiles para el día a día.»
- **Titular de ejemplo:** «Ideas, desarrollo y proyectos útiles.»
- **Descriptor horizontal:** `TECH / PROYECTOS / IDEAS`.
- **Tono:** claro, directo, técnico accesible, creativo y centrado en construir y compartir.
- **Categorías de marca** (no sustituyen a los pilares editoriales de [EDITORIAL](../guias/EDITORIAL.md)): Contenido (YouTube, Reels, Shorts), Desarrollo (proyectos y código) e Ideas (herramientas y experimentos).

### Movimiento y sonido

- **Movimiento:** el tablero no lo define. Propuesta sin aprobar, para los vídeos: la barra como motivo, entradas con barrido diagonal a ≈ 29° de la vertical y superficies planas, sin degradados ni resplandores. Detalle en `videos/VID-0001/GUION_BEATS.md`.
- **Firma sonora:** no existe. Los efectos y la música de los ensayos son provisionales.

## Kit de activos v1.2

Ubicación: `marca/kit/`. Es una **reconstrucción vectorial** hecha a partir del tablero conceptual: los contornos del wordmark salen de la imagen, no son texto editable, y las geometrías arquitectónicas de las plantillas son reinterpretaciones, no la fotografía del tablero. Los SVG se revisaron: no incluyen scripts, imágenes incrustadas ni enlaces externos.

| Qué | Dónde | Para qué |
|---|---|---|
| 37 SVG | `kit/svg/` | Logos, isotipos, wordmarks, avatares, favicon y plantillas. Fuente para exportar |
| 53 PNG | `kit/png/` | Uso directo en CapCut y redes; algunos son transparentes (rótulos y marcas de agua) |
| Tablero conceptual | `kit/referencia/tablero-cerobytes-referencia.png` | Solo referencia. Contiene ®, métricas e insignias de verificación inventadas |
| Vista previa | `kit/vista-previa-v1.2.png` | Resumen visual de las correcciones de la v1.2 |
| Inventario y notas | `kit/manifest-v1.2.json`, `kit/LEEME-v1.2.txt`, `kit/INFORME-CORRECCIONES-v1.2.json` | Trazabilidad del paquete y de las cuatro correcciones sobre la v1.1 |

**Qué usar en un vídeo:**

| Necesito | Archivo |
|---|---|
| Logo sobre fondo marino | `kit/svg/logo-navy.svg` (PNG: `kit/png/logo-navy-2000.png`) |
| Logo sobre fondo negro | `kit/svg/logo-oscuro.svg` (en la v1.2, todo en blanco roto). No uses los `*-azul-referencia` sobre negro |
| Marca de agua | `kit/png/marca-agua-logo-blanco-1520.png` o `kit/png/marca-agua-isotipo-blanco-512.png` |
| Rótulo inferior 9:16 | `kit/png/rotulo-inferior-video-9x16-ajustado-1080.png` (transparente; SVG: `kit/svg/rotulo-inferior-video-9x16-ajustado.svg`). Es un derivado del proyecto sobre el kit v1.2, desplazado 100 px: caja en y 1230–1400, sin pisar los subtítulos (y 1060–1180) y dentro del límite de la red (y 1420). El original del kit (y 1130–1300) pisa 50 px esa banda |
| Pantalla de inicio y de cierre | `kit/png/pantalla-inicio-9x16-1080.png` y `kit/png/pantalla-cierre-9x16-1080.png`. Son fotogramas estáticos, no animaciones |
| Portada 9:16 | `kit/png/plantilla-portada-9x16-1080.png` (sustituye el título de ejemplo) |
| Miniatura 16:9 | `kit/png/plantilla-miniatura-16x9-1280.png` |
| Avatar de las cuentas | `kit/png/avatar-navy-512.png` o `-1024.png` |
| Favicon | `kit/svg/favicon.svg` |

Los PNG con texto (rótulos, portada, plantillas, pantallas 9:16) están exportados con Plus Jakarta Sans (AV-007). Reglas de uso: revisa los márgenes de cada cabecera tras subirla a la red, porque las dimensiones de las plataformas cambian. En las plantillas, sustituye los textos de ejemplo.

**Volver a exportar los PNG** (los de este kit ya se exportaron con Plus Jakarta Sans el 2026-11-16): con la fuente instalada o incrustada desde `marca/fuentes/plus-jakarta-sans/`, exporta cada SVG con texto conservando la transparencia. Con Inkscape: `inkscape kit/svg/<archivo>.svg --export-type=png --export-filename=<salida>.png --export-width=1080` (ancho 1080 en las piezas 9:16). Claude puede hacerlo en una sesión con Chromium. Después comprueba que no hay desbordes y que el rótulo sigue entre y 1230 y 1400.

Observación del kit: en `tarjeta-perfil-social` el avatar circular se solapa con el descriptor «TECNOLOGÍA / DESARROLLO / IDEAS». Es un defecto de la plantilla, no de la tipografía.

## Pendientes

1. Maestro vectorial oficial del logo, con proporciones y espaciados definitivos (el wordmark actual es un trazado reconstruido).
2. Valor exacto del azul de la barra diagonal.
3. Reglas de tamaño mínimo y área de protección.
4. Confirmar los pesos de Plus Jakarta Sans (propuestos: 500, 700 y 800) y su interletraje.
5. Aprobación del tratamiento de movimiento.
6. Firma sonora.
7. Validación legal del registro de marca, si corresponde.

## Historial

| Fecha | Cambio | Decisión |
|---|---|---|
| 2026-11-05 | Perfil provisional TEMP (paleta A, Inter) | PR-002 (propuesta) |
| 2026-11-16 | Ale aprueba la paleta A como identidad v1 | PR-002 (aprobada) |
| 2026-11-16 | Ale elige la dirección *creative tech* y el kit vectorial v1.1: identidad v2 | AV-006, sustituye a PR-002 |
| 2026-11-16 | El kit v1.2 sustituye a la v1.1: rótulo MG-02 recolocado, logo oscuro con barra blanca, SVG con Satoshi → Inter → Arial y advertencia de procedencia del wordmark | Revisión del kit de AV-006 |
| 2026-11-16 | Ale elige Plus Jakarta Sans (Google Fonts, OFL) en lugar de Satoshi; se incluye en `marca/fuentes/` y se exportan de nuevo los PNG con texto | AV-007, modifica la tipografía de AV-006 |

Para cambiar la identidad hace falta una decisión nueva en [DECISIONES](../registro/DECISIONES.md). La identidad de MiMiniApp (Space Grotesk, DM Sans, violeta `#7950F2`) es distinta y vive en el repositorio `soycerobytes/miminiapp` (AV-005).
