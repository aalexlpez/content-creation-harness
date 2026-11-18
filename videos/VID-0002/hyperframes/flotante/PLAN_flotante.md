# VID-0002 · Ensayo 3: edición flotante

Ensayo del 2026-11-18 a petición de Ale, tras ver la v05: «la mayoría del video está cortado en dos partes, arriba con muchas animaciones y abajo mi cara. La división de la pantalla debería aprovecharse más que todo para las demos de la aplicación, no para elementos que acompañen salvo algún caso especial. Quiero una edición más flotante, blur, iconos flotantes con movimientos leves, flechas que los interconecten, un poco más neón o llamativos, que acompañen perfectamente el guion».

Mismo corte, misma voz mejorada y mismos sonidos que la v05 ([PLAN_v05](../edicion/PLAN_v05.md)). Cambia **cómo se reparte la pantalla** y **el estilo de la capa gráfica**. La composición está en `index.html` de esta carpeta; la mezcla, en `../edicion/mezcla_flotante.py`.

## 1. Qué cambia frente a la v05

| | v05 | Flotante |
|---|---|---|
| Pantalla | Dividida el 67 % del vídeo (panel arriba, cara abajo) | **Cara a pantalla completa** casi todo el vídeo; **dividida solo en la demo** (22,7–41,3 s del corte v01) |
| Gráficos | Dentro del panel, quietos, en una cuadrícula | **Flotan sobre la cara**, en los márgenes y por encima de la cabeza; nunca encima de la cara |
| Movimiento | Entradas y salidas | Además, **deriva leve** continua (±5–14 px y ±1,6°) con fase propia por elemento |
| Profundidad | Plano | Cada elemento tiene una profundidad: los lejanos van más pequeños, más tenues y con 2 px de desenfoque; entran y salen **desenfocados** (14 → 0 px) |
| Conexiones | Ninguna | **Flechas** que se dibujan, llevan un punto de luz que viaja y salen antes de que se vaya su destino |
| Estilo | Líneas planas, sin resplandor | **Trazo blanco con resplandor** (neón en blanco roto), cristal translúcido oscuro y borde luminoso |

## 2. Reglas de la capa flotante

1. **La cara no se tapa.** Zonas libres a cámara: por encima de la cabeza (y 170–480), las dos columnas laterales (x < 370 y x > 790) y el pecho bajo el mentón (y 1040–1140). Las flechas que cruzan el cuadro **dan la vuelta por encima de la cabeza** (vértice en y ≈ 205); ninguna pasa por el mentón.
2. **Un elemento por idea con peso**, que aparece en la palabra que lo nombra y sale antes de que cambie la frase. Entre 1 y 6 elementos a la vez.
3. **La flecha cuenta la relación:** de «hoja» a «propósito», de «marcas de enero» a «la toalla», de «semana» a «jueves», de «Plan B» a «gratis» y a «planear ese día», de «teléfono» a «1 por semana» y de cada categoría a la siguiente.
4. **El teléfono flotante es el hilo del vídeo:** nace en «Esta es una nueva aplicación», **se ensancha hasta ser la ventana de la demo** (el panel de la pantalla dividida baja justo entonces), **se vuelve a encoger hasta el teléfono** al terminar la demo y se queda como el nodo «01» de la serie. En el cierre aparece otra vez con «PLAN B».
5. **La pantalla dividida solo en la demo**, con la ventana y sus dos insertos a pantalla completa (el toque en «No tuve tiempo» y el sello), como en la v05.
6. Se mantienen: palabras protagonistas detrás de la persona (ABANDONASTE y CALMA), «Plan B» que llena el cuadro, encuadre alterno y oscurecido en los empalmes, subtítulos en banda fija y el acento «Este febrero, no.» con su golpe.

## 3. Elementos, flechas y tiempos (tiempo del corte v01; los posteriores a 33,60 s caen 1,0 s antes en el vídeo)

| t (s) | Palabra | Elemento flotante | Flecha |
|---|---|---|---|
| 0,30 | febrero | Hoja de calendario (ENERO → FEBRERO) | — |
| 2,00 | propósito | Tarjeta «PROPÓSITO» con una diana (derecha) | De la hoja a la diana, por encima de la cabeza |
| 5,00 | mediados | Calendario de enero (izquierda): los días 1–14 se marcan cada vez más rápido y se detienen | — |
| 7,05 | tirado la toalla | Tarjeta «LA TOALLA» con una bandera blanca; las marcas caen | Del calendario a la bandera |
| 8,30 | Y la mayoría | La semana (LU–DO) marcada salvo el jueves | — |
| 11,00 | día | Tarjeta «JUEVES ?» | De la semana al jueves |
| 12,25 | ganas | Etiqueta «SIN GANAS» | — |
| 12,79 | Soy cerobytes | Etiqueta con el logo (el del kit, blanco) | — |
| 14,59 | Plan B | «Plan B» llena el cuadro (sobre la camiseta) | — |
| 15,23 | aplicación | Teléfono flotante «PLAN B» | Del logo al teléfono |
| 17,24 | gratis | «$» tachado → «GRATIS» (bajo el teléfono) | Del teléfono a «GRATIS» |
| 18,84 | planear ese día | Tarjeta «JUEVES» con un calendario | Del teléfono al día, por encima de la cabeza |
| 21,64 | primera | El teléfono pasa a «01 /» | — |
| 22,70 | (demo) | **El teléfono se ensancha hasta ser la ventana**; baja el panel | — |
| 40,97 | pantalla | La ventana se encoge hasta volver a ser el teléfono («01 /») | — |
| 44,55 | a la semana | Etiqueta «1 POR SEMANA» | Del teléfono a la etiqueta |
| 46,55 | productividad | Tarjeta «PRODUCTIVIDAD» (columna izquierda) | De «1 por semana» a la tarjeta |
| 47,76 | ciencia | Tarjeta «CIENCIA» | De la anterior a esta |
| 49,80 | minijuegos | Tarjeta «MINIJUEGOS» | De la anterior a esta |
| 51,00 | cualquier ámbito | «…» (sigue) | De «minijuegos» a «…» |
| 57,60 | arma tu plan B | Teléfono «PLAN B» y hoja de calendario (izquierda) | De la hoja al teléfono; la hoja pasa a FEBRERO en «febrero» |
| 59,56 | febrero | «Este febrero, no.» (golpe 3 de 3) | — |

## 4. ⚠ Estilo y marca: hace falta una decisión de Ale

Ale pidió «un poco más neón o llamativos». **AV-007 prohíbe resplandores, degradados y sombras difusas** en la identidad v2, y la identidad pública solo la decide Ale. Para el ensayo se hizo lo mínimo que lo logra **sin tocar la paleta ni la tipografía**: el resplandor es del mismo blanco roto `#F5F6F8` (`drop-shadow` de 7 y 22 px) y el cristal usa un azul casi negro. **No hay color de acento.**

Queda registrado como **AV-013 (propuesta)**: si Ale lo aprueba tras verlo, pasa a ser un estilo aceptado (por ejemplo, solo para la capa flotante); si no, se descarta y la marca v2 sigue como está. Si quiere un color de acento (cian, ámbar…), eso es un cambio de marca y también es suyo.

## 5. Lo que hay que mirar en el celular

- Si el resplandor de las flechas y los iconos cansa o ayuda.
- Si hay demasiados elementos a la vez en «La serie» (hasta 6).
- Si el desenfoque de entrada y salida se ve fino o «borroso» en pantallas pequeñas.
- Si las flechas por encima de la cabeza distraen en el gancho.

## 6. Resultado (entregado el 2026-11-18)

`media/trabajo/flotante_v01.mp4` (con música) y `flotante_v01_sin_musica.mp4`, 56,43 s, 1080×1920, 30 fps, con la voz mejorada de Ale. `hyperframes check`: sin errores (queda un aviso de «línea breve» del «$» que se tacha, marcado como a propósito con `data-hold`).

**Medido con `revisar.py`:** pantalla dividida **25.5 % del vídeo** (en la v05 era 67,6 %) · cara tapada por insertos 5.3 % · inserto continuo más largo 1.5 s · ningún tramo sin cambio de más de 3 s · -14.3 LUFS, pico real -1.3 dBFS · 61 efectos (un pop por cada elemento que aparece y un trazo de lápiz por cada flecha que se dibuja). **El sonido está medido, no escuchado.**

**Correcciones durante la revisión (capturas):** las flechas del primer montaje cruzaban el mentón (la cabeza ocupa de y 500 a 1040, no de 300 a 720): ahora todas dan la vuelta por encima; «CALMA» chocaba con la tarjeta del propósito (la tarjeta sale en 3,2 s); «SIN GANAS» duraba 0,4 s (ahora ≈ 1,1 s); «GRATIS» y el día pasaron a la derecha para no cruzar la cara; y se subió la intensidad del resplandor.
