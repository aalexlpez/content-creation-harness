# Herramientas sencillas por las que la gente paga

**Fecha:** 2026-11-12 · **Autor:** Claude, a petición de Ale · **Estado:** investigación. Se fusionará con las otras dos de noviembre en un solo documento cuando Ale cierre la ronda.

**Pregunta:** ¿qué herramientas muy sencillas, con impacto real en la productividad, acaban costando dinero (suscripción, prueba que caduca, pago al descargar), y cuáles podemos hacer gratis en una web estática sin que el archivo salga del móvil?

**Sobre las cifras:** son estimaciones de terceros o datos de páginas de reseñas, a menudo escritas por competidores. Sirven para ver la magnitud. En un vídeo solo entran como claim E, con fuente y fecha, y **sin nombrar marcas** (EDITORIAL: no se habla mal de otras herramientas).

## 1. Dónde está el dinero (y la frustración)

| Necesidad | Señal de mercado | Frustración típica |
|---|---|---|
| PDF (unir, dividir, comprimir, firmar) | Unos 217–265 M de visitas al mes para el líder del sector y unos 37–43 M para el segundo; premium alrededor de 5–15 $/mes (estimaciones de [Semrush](https://www.semrush.com/website/ilovepdf.com/overview/) y [comparativas](https://www.temperstack.com/versus/smallpdf-vs-ilovepdf/)) | Subes documentos personales a un servidor ajeno ([guía](https://pdfyay.pages.dev/guides/is-smallpdf-safe)) |
| Códigos QR | Los QR «dinámicos» creados en una prueba gratuita dejan de funcionar al terminarla; lo documenta el propio proveedor ([soporte](https://support.qr-code-generator.com/hc/en-us/articles/7665046137613)) | Folletos impresos con un QR que ya no lleva a ningún sitio ([reseñas](https://www.trustpilot.com/review/www.qr-code-generator.com?page=8)) |
| Currículum | Varios creadores de CV dejan editar gratis y cobran, o limitan a TXT, al descargar el PDF ([análisis](https://pitchmeai.com/blog/zety-resume-builder-download-paywall)) | Descubres el pago después de una hora escribiendo |
| Presupuesto personal | Mint cerró en marzo de 2024; las alternativas cuestan unos 95–110 $/año ([Motley Fool](https://fool.com/the-ascent/personal-finance/articles/the-mint-budgeting-app-is-gone-here-are-some-alternatives/), [Finder](https://www.finder.com/budgeting/mint-alternatives)) | Conectar el banco o pagar una suscripción para algo que es una suma |
| Gastos compartidos | La app más conocida limita a pocos gastos al día en su versión gratuita desde finales de 2023, según reseñas; Pro, unos 40 $/año ([análisis de reseñas](https://kimola.com/reports/splitwise-app-feedback-report-uncover-user-insights-google-play-en-144452)) | El límite aparece justo en mitad del viaje |
| Escanear documentos | El escáner más popular cuesta unos 50 $/año, pone marca de agua en la versión gratis y en 2019 tuvo malware en un SDK de anuncios en Android ([MakeUseOf](https://www.makeuseof.com/is-camscanner-safe/), [GadgetMatch](https://www.gadgetmatch.com/camscanner-android-google-play-store-malware-kaspersky-lab/)) | Anuncios, marca de agua y permisos excesivos |
| Teleprompter | Apps de creador en torno a 90 $/año o 30 $ de pago único ([PromptSmart](https://www.promptsmart.com/pricing.html), [App Store](https://apps.apple.com/app/id1124958568)) | Pagar al año por desplazar texto |
| Suscripciones en general | En EE. UU., unos 205 $/año en suscripciones que no se usan (CNET/YouGov, abril de 2025, [Cord Cutters News](https://cordcuttersnews.com/americans-now-pay-over-200-in-subscriptions-they-dont-use/)) | Refuerza la idea N3, el ticket de suscripciones |

## 2. La lección importante: «gratis y local» ya no basta

Busques la herramienta que busques, aparecen decenas de webs que prometen «sin subir archivos, sin cuenta». Muchas son clones en dominios gratuitos (`*.pages.dev`, `*.vercel.app`) hechos para posicionar en buscadores. **La versión gratuita local existe para casi todo.** Hasta herramientas muy conocidas que procesan en local incluyen analítica de terceros ([Squoosh](https://github.com/kalvinGit/squoosh/blob/master/README.md)).

Lo que nos diferencia no es la herramienta, sino:

1. **La trampa como gancho.** «Muchas webs de QR te dejan crear el código gratis y lo apagan a los 7 días». Se cuenta el patrón con su fuente, sin señalar a nadie.
2. **Un giro propio** que no tengan los clones (ver la columna «Giro»).
3. **La prueba en vídeo:** modo avión y la herramienta sigue funcionando.
4. **Confianza de colección:** mismo diseño, mismo código abierto (PROD-10) y la misma cara detrás. Un clon anónimo no tiene eso.

## 3. Qué cabe en una web estática y qué no

| Cabe sin problema | Cabe con cuidado | No conviene al principio |
|---|---|---|
| Generar QR, cálculos y presupuestos, PDF con texto e imagen (imprimir a PDF o `pdf-lib`), unir o dividir PDF, cámara del móvil (`getUserMedia`), quitar metadatos de JPG al volver a codificarlo en un `canvas` | HEIC → JPG (necesita un decodificador en WebAssembly), escáner con detección automática de bordes (OpenCV.js pesa mucho), datos compartidos dentro de un enlace (hay que vigilar la longitud) | Convertir o comprimir vídeo: con `ffmpeg.wasm` en el móvil, los límites prácticos rondan los 100–200 MB y la conversión se congela si cambias de pestaña ([guía](https://freetoolonline.com/guides/ffmpeg-online-vs-local-ffmpeg-when-each-wins.html)). Quitar fondos: modelos de decenas de MB y licencias a revisar, alguna AGPL ([nota](https://github.com/opencoredev/bg0/wiki)) |

Dos trampas que romperían la promesa de que «lo que escribes no sale de tu móvil»:
- **Dictado por voz:** el reconocimiento de voz del navegador puede procesarse en servidores del fabricante. Un teleprompter que «sigue tu voz» no cumple la promesa.
- **Persistencia:** Safari borra los datos tras 7 días sin visitar la web (ver IDEAS_ORIGINALES §1). Lo que haya que guardar mucho tiempo se exporta, o se recomienda añadir la web a la pantalla de inicio.

## 4. Candidatas

Puntuación de 0 a 2 en seis criterios (12 en total):

- **Paga (Pa):** la gente paga o cae en una trampa por esto.
- **Gancho (G):** se entiende y engancha en 1–3 s.
- **Viable (V):** estático, sin servidor, en unas 6 h.
- **Global (Gl):** sirve en cualquier país.
- **Giro (Gi):** aporta algo que los clones gratuitos no tienen.
- **Serie (S):** encaja con la serie y con enero.

| # | Miniapp (provisional) | Qué hace | Giro | Gancho | Pa | G | V | Gl | Gi | S | Total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **H1** | **Tu número del día** | Ingresos, gastos fijos y cuánto quieres ahorrar → **una sola cifra: lo que puedes gastar hoy**. Cada día recalcula con lo que llevas gastado | Un número en lugar de 20 categorías. Sin banco ni cuenta. Moneda y formato de cada país con `Intl` | «Mi app de presupuesto tiene una sola pantalla: hoy puedo gastar X» | 2 | 2 | 2 | 2 | 1 | 2 | **11** |
| **H2** | **Cuentas compartidas: el enlace es la base de datos** | Gastos de viaje o de piso. Cada cambio genera un enlace nuevo que se pega en el grupo; los datos viajan dentro del enlace, no en un servidor | Sin app, sin cuenta y sin límite de gastos al día. El chat del grupo hace de historial | «Sin app y sin límite de gastos: la base de datos es tu grupo de WhatsApp» | 2 | 2 | 1 | 2 | 2 | 1 | **10** |
| **H3** | **QR que no caduca** (+ tarjeta Wi-Fi para invitados) | QR estático para enlace, texto o Wi-Fi (formato `WIFI:` que leen las cámaras de iPhone y Android, [guía](https://u2l.ai/blog/qr-code-wifi)), con tarjeta imprimible | Explica la diferencia entre estático y dinámico, prueba de escaneo y tarjeta lista para la nevera | «Tu QR “gratis” deja de funcionar a los 7 días. Este no puede» | 2 | 2 | 2 | 2 | 1 | 1 | **10** |
| **H4** | **Teleprompter de bolsillo** | Texto que se desplaza en el móvil, con velocidad, tamaño, modo espejo y marca de lectura | Ale lo usa para grabar la propia serie. Sin dictado por voz, que rompería la promesa | «Este vídeo lo he grabado con la miniapp que hice esta semana» | 2 | 1 | 2 | 2 | 1 | 2 | **10** |
| H5 | CV que no te cobra al descargar | Plantillas sobrias e internacionales, PDF imprimiendo desde el navegador, copia en un archivo JSON | Sin muro de pago al final, y el CV no pasa por ningún servidor | «Escribes tu CV una hora y al descargar te piden pagar. Aquí no» | 2 | 2 | 1 | 1 | 1 | 1 | **8** |
| H6 | Escáner sin marca de agua | Foto con la cámara, recorte manual, filtro de contraste y PDF de varias páginas | Sin anuncios, sin marca de agua y sin permisos extra | «Escanea un documento sin instalar nada» | 2 | 1 | 1 | 2 | 1 | 1 | **8** |
| H7 | Tu foto dice dónde está tu casa | Lee los metadatos de una foto, muestra si lleva ubicación GPS y la limpia | Lo enseña antes de borrarlo: el «ajá» es ver tus propias coordenadas | «Esta foto dice exactamente dónde la hice» | 0 | 2 | 1 | 2 | 1 | 1 | **7** |
| H8 | Firmar un PDF sin subirlo | Dibujas la firma y la colocas en el PDF con `pdf-lib` | Con aviso claro: firma simple, no firma electrónica avanzada | «Firmar sin subir tu contrato a ninguna web» | 1 | 1 | 1 | 2 | 1 | 1 | **7** |

Notas:

- **H1.** Hay apps de pago con una cifra parecida de «lo que te queda», así que el giro es parcial. Lo nuestro es que no hay banco, ni cuenta, ni nada más. Encaja con los propósitos financieros de enero. El dato para el vídeo es el de Ale o uno de ejemplo declarado: nunca cifras inventadas como reales.
- **H2.** Es la más original de esta lista. Hay que comprobar la longitud de los enlaces con un viaje real de unos 50 gastos (comprimiendo los datos) y cómo los muestra WhatsApp. Si funciona, el concepto «el enlace es la base de datos» sirve para otras miniapps.
- **Preferencias de Ale (2026-11-12):** le gustan **H3 (QR)** y **las herramientas de PDF**. En H3 quiere una demostración vistosa con un uso real del QR.
- **H3.** Es la más fácil y la de gancho más claro, pero tiene muchísimos clones. Su valor en la serie es explicar la trampa y regalar la tarjeta Wi-Fi. La contraseña del Wi-Fi no sale del móvil al generar el QR, pero el QR impreso la muestra a cualquiera que lo escanee: sirve para casa, no para un lugar público. La prueba de escaneo necesita un decodificador propio, porque `BarcodeDetector` no está en todos los navegadores.
- **H4.** Es meta y verdadera: sirve al propio Ale. El público principal son creadores (A3/A2), más pequeño que el de H1.
- **H5–H8.** Útiles, pero con más complejidad, normas que cambian por país (CV) o avisos legales (firma). Mejor más adelante.
- **Descartadas por ahora:** convertir o comprimir vídeo y quitar fondos (§3).

## 5. Cómo encaja con lo anterior

- **Dos tipos de productividad.** Las ideas originales (P1, y P2 «Encoge tu propósito», la favorita de Ale) dan **viralidad**. Las herramientas útiles (H1–H4) dan **tráfico duradero**: la gente las busca todo el año, como muestran las cifras del sector PDF. Alternarlas da a la serie las dos cosas.
- **Propuesta de rotación** para los huecos de productividad:

  | Viernes | Hueco | Propuesta |
  |---|---|---|
  | 1 ene | Productividad | P1 o P2 (propósitos) |
  | 8 ene | Entretenimiento | E1 |
  | 15 ene | Productividad | **H1 · Tu número del día**, finanzas tras las fiestas |
  | 22 ene | Entretenimiento | E2 |
  | 29 ene | Productividad | **H2** o **H3** |

- Con la nota de N3 (el ticket de suscripciones), H1 puede tener una segunda pieza derivada: «¿cuánto de tu número diario se va en suscripciones?».

## 6. Ficha: QR fáciles, rápidos y gratis (H3)

**Estado:** idea aprobada por Ale para el **segundo o tercer vídeo** de la serie (2026-11-12). Se desarrollará más adelante.

**Mensaje:** un QR estático *es* la información, así que no depende de ningún servidor que pueda apagarlo. Los dinámicos de pago sirven para editar el destino o contar escaneos; si no necesitas eso, este te basta.

**Vídeo principal (demostración A):** construir **un QR gigante con pósits** en una ventana, a partir del plano que da la miniapp, y escanearlo: lleva a MiMiniApp. Gancho: «Hice un QR con pósits y funciona».
- El QR mínimo es de 21×21 casillas, unas 29 con el margen. Con pósits de 7,6 cm son unos 2,2 m y unos 200–250 pósits (aproximado).
- Escrito en mayúsculas (`HTTPS://MIMINIAPP.COM`), el enlace usa el modo alfanumérico y debería caber en 21×21. Las capacidades exactas se comprueban al construirlo.
- **Requisito:** dominio definitivo comprado. Un QR impreso con una dirección provisional `*.workers.dev` queda desfasado.

**Piezas derivadas:**
- **B · Etiqueta de objetos perdidos:** se lee sin internet porque el texto va dentro. En el vídeo, modo avión.
- **C · Mensaje escondido en un regalo:** San Valentín, el viernes 12 de febrero.
- **D · Tarjeta Wi-Fi o de contacto:** la que Ale descartó como demostración principal, que queda como función.

**Alcance de la versión 1:**
- **Tipos:** enlace, texto, Wi-Fi y contacto (vCard).
- **Plantillas para imprimir:** tarjeta Wi-Fi, tarjeta de visita, etiqueta y póster.
- **Plano para construirlo a mano.**
- **Diseño:** colores con aviso de contraste, forma de puntos y esquinas, logo central con corrección alta, marco con texto.
- **Exportar** en PNG, SVG o PDF.
- **Prueba de escaneo** dentro de la web.

**Versión 2:** correo, teléfono, SMS, WhatsApp (`wa.me`), evento, ubicación y varios códigos a partir de una lista.

**Por comprobar en móviles reales** (S24+, POCO F5 y un iPhone prestado):
- Unirse al Wi-Fi y añadir contacto escaneando con la cámara.
- Evento y ubicación, que dependen del móvil.
- Contraseñas de Wi-Fi con caracteres especiales escapados.
- Lectura de un QR grande a distancia.

**Lo que no hace, y se dice:** editar el destino después de imprimir, contar escaneos, contraseña o caducidad. Todo eso necesita servidor.

## 7. PDF en una web estática: qué se puede y qué no

**Estado:** a Ale le gusta la línea de PDF (2026-11-12). Propuesta de miniapp en el apartado de abajo.

**Cómo funciona.** El navegador lee el archivo que eliges (`<input type="file">`), una librería de JavaScript lo abre y lo modifica en memoria, y el resultado se descarga o se comparte con el menú del móvil. El documento **no viaja a ningún servidor**. Librerías base:
- **PDF.js**, de Mozilla: dibuja páginas y miniaturas y extrae texto.
- **pdf-lib:** crea y modifica PDF. Ojo: el proyecto original está prácticamente sin mantenimiento y se usan bifurcaciones ([fork de Cantoo](https://unpkg.com/@cantoo/pdf-lib@2.7.1/README.md)). Hay que elegir una y fijar su versión.

| Nivel | Operaciones | Comentario |
|---|---|---|
| **Fácil** | Unir, dividir, extraer, reordenar, girar y borrar páginas. Fotos (JPG/PNG) → PDF. PDF → imágenes. Números de página. Marca de agua. Rellenar formularios sencillos. Firma como imagen | Sale con PDF.js y pdf-lib, que caben en una semana |
| **Con cuidado** | Ajustar el tamaño de un PDF *hecho con fotos* (controlamos la calidad de cada imagen al crearlo). Poner o quitar contraseña (bifurcación o complemento, [ejemplo](https://socket.dev/npm/package/@pdfsmaller/pdf-encrypt)). HEIC → PDF (decodificador WASM). OCR con Tesseract.js (lento en el móvil; datos de idioma pesados) | Viable, con pruebas en móvil |
| **No, por ahora** | Comprimir *cualquier* PDF de verdad: necesita Ghostscript o MuPDF en WASM, que son pesados y **AGPL** ([nota](https://dev.to/pranav_mailarpawar_7039f2/i-ran-ghostscript-inside-a-browser-tab-to-build-a-free-pdf-compressor-2hd9)), en choque con la licencia MIT prevista (ADR-MMA-010). Convertir PDF ↔ Word, Excel o PowerPoint conservando el diseño: necesita motores enormes, como LibreOffice en WASM | Queda fuera hasta que haya otra decisión |

**Límites técnicos que hay que tener en cuenta:**
- **Memoria del móvil:** un PDF de cientos de MB o de cientos de páginas puede bloquear la pestaña, sobre todo en Safari. Hay que poner un límite y avisar.
- **Rendimiento:** las miniaturas de PDF largos se generan poco a poco.
- **Texto con alfabetos no latinos** (marca de agua, números): hay que incrustar fuentes, porque las estándar de PDF no cubren chino, árabe o cirílico. Pesa más, pero es necesario para que sea global.
- **PDF protegidos:** sin la contraseña no se abren.
- **PDF con firma digital:** cualquier cambio invalida la firma existente. Hay que avisar antes.
- **Formularios XFA** (algunos formularios oficiales): no se pueden rellenar con estas librerías.
- **Descargar en iPhone:** se resuelve con el menú de compartir (Web Share API con archivos), que hay que probar en un iPhone.

### Ficha: «PDF para trámites»

**Estado:** idea aprobada por Ale para la serie (2026-11-12): «Vale, documenta esta idea también». La fecha está por decidir y se desarrollará más adelante, como el QR.

Una necesidad global, presente en cualquier país: mandar el documento de identidad por las dos caras, un contrato o unas nóminas **en un solo PDF**, a menudo con un **tamaño máximo** (el típico «máximo 2 MB» de un formulario), y sin subirlos a una web desconocida.

- **Versión 1:**
  - Fotos de la cámara o de la galería y PDF → **un solo PDF**.
  - Miniaturas para **ordenar, girar y quitar** páginas.
  - **«Que pese menos de X MB»**: ajusta la calidad de las fotos hasta llegar.
  - **Marca de agua de uso** opcional, como «Copia solo para el alquiler · enero 2027». Es una indicación de uso, no una protección contra copia. Si tapa datos, el trámite puede rechazar el documento.
  - **Recorte tras la evaluación independiente:** la v1 se queda en unir fotos y PDF, ordenar, girar, quitar y la marca de agua. El «menos de X MB» pasa a v2, y solo para PDF hechos con fotos. Con PDF que ya existen no se puede garantizar sin perder texto seleccionable.
- **Versión 2:** dividir PDF, PDF → imágenes para mandar una página por chat, firma como imagen y números de página.
- **Gancho:** «¿Has subido tu DNI a una web para pasarlo a PDF? Esta lo hace sin que salga de tu móvil.»
- **Demostración:** modo avión, foto de un **documento de ejemplo**, PDF de menos de 2 MB con marca de agua y envío. Nunca un documento real de Ale.
- **Claims:** «no sale de tu móvil» es P y se demuestra. Que la marca de agua de uso reduce el riesgo de mal uso es O u H, salvo que se cite una recomendación oficial con fecha.
- **Decisión técnica pendiente:** qué bifurcación de pdf-lib usar y si se acepta algún componente AGPL en el futuro (afecta a ADR-MMA-010).

## 8. Decisiones que tiene que tomar Ale

1. Si las herramientas útiles entran en la rotación de productividad, tal como propone §5.
2. Si se prueba en prototipo el concepto «el enlace es la base de datos» (H2) antes de comprometer una fecha.
