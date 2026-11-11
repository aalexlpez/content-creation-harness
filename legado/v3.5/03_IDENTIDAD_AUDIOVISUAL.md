**RECTIFICACIÓN OBLIGATORIA (v3.1): la identidad audiovisual pertenece a Alexander y a su futuro alias PERSONAL, no a MiMiniApp.** El nombre «MiMiniApp» en ejemplos antiguos indica el producto mostrado; NO es una marca de canal, firma ni @handle. Ver `12_IDENTIDAD_PERSONAL_Y_HANDLES.md`. La paleta candidata es solo una prueba para Alexander, pendiente de aprobación.

# Identidad audiovisual — separada de la marca de producto
**Estado: propuesta de dirección visual para test; PENDIENTE DE APROBACIÓN.** Esta página no modifica el diseño del sitio Astro ni registra propiedad del nombre/dominio.

## Dos identidades, una relación
- **Producto**: UI útil, accesible, SEO, sistemas de diseño propios de la web.
- **Marca personal de Alexander**: rostro, guion, ritmo, fondos, lenguaje de movimiento, sonido, rótulos, portadas, transiciones. Las cuentas no se llaman MiMiniApp.
- **Puente común**: asociación explícita «Alexander construye MiMiniApp» y demos fieles de la interfaz real; los logotipos y paletas de ambos no deben confundirse. No copiar automáticamente CSS ni paletas desde Astro hacia los vídeos.

## Personalidad audiovisual propuesta
«Laboratorio digital luminoso sobre fondo nocturno»: moderno, dinámico, competente y cercano, con momentos cinematográficos pero sin ruido visual permanente. Diferenciar **acabado sofisticado** de **sensacionalismo**: no usar destellos ni efectos si ocultan el resultado.

## Paleta CANDIDATA A — no es paleta aprobada ni extraída de las capturas
| Token | HEX | Función | Regla |
|---|---|---|---|
| Fondo profundo | `#0B1020` | Base de escenas cinematográficas | Evitar negro puro continuo |
| Panel/relieve | `#17243A` | UI ficticia de vídeo, cards y líneas | No reemplazar estilos de web real |
| Texto principal | `#F3F7FF` | Narrativa, resultados, rótulos | Máxima jerarquía |
| Texto secundario | `#B9CAE2` | Explicación secundaria | Comprobar contraste/escala |
| Cian | `#54E0EA` | Acento primario, trayectoria visual | Moderar brillos |
| Violeta | `#AD8BFF` | Profundidad y gradientes | Máximo 1–2 acentos por plano |
| Lima | `#D9F77A` | Resultado/confirmación puntual | No usar en todas las escenas |

**Por qué es una propuesta y no un hecho:** los colores surgen del análisis del tipo de efecto y de soluciones de legibilidad, no de una encuesta a tu audiencia ni de una identidad ya aprobada. Las tres capturas de una app azul translúcida **NO** se usan como paleta. La marca del creador de IA tampoco. Solo diseñar otra opción B si el propietario rechaza la A, no generar 20 opciones de IA.

## Comprobación objetiva del contraste de la paleta candidata
Contraste calculado con fórmula de luminancia relativa WCAG 2.2 frente a fondo sólido `#0B1020` (aproximado, sin efectos de transparencia): texto principal **17,63:1**; texto secundario **11,37:1**; cian **11,93:1**; violeta **7,13:1**; lima **15,81:1**. Todos superan el umbral WCAG AA de 4,5:1 **solo en esa combinación plana**; en vídeo, gradientes, brillos, desenfoques y compresión pueden reducir la legibilidad real. Es una prueba técnica, no evidencia de que la audiencia prefiera esos colores. Fuente WCAG: https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum

## Reglas formales propuestas para el primer prototipo
- Tipografía: probar una familia de display geométrica + una sans legible; no se define nombre hasta revisar licencias, caracteres españoles y render en Windows. No se garantiza instalación de fuentes.
- Tipo: titular ≤2 líneas en la mayoría de escenas; subtítulos con fondo/contorno legible; 1 punto focal por plano; distinguir rótulos editoriales del texto propio de la demo.
- Layout: fondo limpio, capas interactivas en el tercio central, indicadores secundarios en bordes, revisar margen de cada red en un móvil; evitar cubrir rostro o controles.
- Motion: tarjeta→detalle con continuidad espacial; campos escalonados; zoom 3D justificado; movimiento de acentos mientras aporta orientación. Entradas por `opacity + transform`, máscara, morph, parallax y pistas por escena. Easing/timing concretos deben definirse en storyboard, no como dogma.
- Audio: voz real como elemento principal, SFX breve en acciones verificables (tap, reveal, confirm), música discreta original/licenciada; silencio intencional válido. No usar sonidos como relleno.
- Portada: cada vídeo tiene portada propia con patrón de título corto + un foco (rostro O producto) + marcador de serie opcional. No diseñar portadas idénticas.

## Biblioteca de patrones de marca (no obligación de reutilizar animaciones)
- `F-01`: A-roll del creador + 1 callout verificable + corte motivado.
- `U-01`: vista móvil→tarjeta foco→morph a detalle→interacción→resultado; contenidos variables.
- `T-01`: frase-clave cinética ligada a palabra de voz (no ticker continuo).
- `C-01`: terminal real con puntero/zoom y resaltado, no código falso.
- `Q-01`: pregunta específica, tres opciones visuales máximo y CTA claro.
**Elementos de marca** (tokens, jerarquía, estilo, tipos de transición) sí son consistentes; una escena puede ser totalmente nueva.

## Puerta de aprobación B0 (una sesión)
1. Crear dos frames originales: a cámara con rótulo + móvil/UI animada con paleta A (sin usar las capturas de terceros como activos).
2. Revisarlos en teléfono con brillo habitual; confirmar legibilidad, color, personalidad y legibilidad de subtítulos.
3. Aprobar A o pedir **una única revisión focalizada**. Si no se alcanza el estándar, marcar pendiente y no publicar con marca «definitiva».
4. Guardar `brand/IDENTIDAD_APROBADA.json` (ejemplo de esquema en `brand/IDENTIDAD_PROPUESTA.json`) y registrar ID, fecha, persona y versión.
5. Congelar tokens por un lote piloto de 5 vídeos; se cambian por revisión registrada, no espontáneamente por cada prompt.
