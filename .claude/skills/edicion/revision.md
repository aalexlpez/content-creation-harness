# Revisión antes de entregar

Se hace sobre el render, no sobre el código. Lo que no se pudo comprobar se dice («mezcla medida, no escuchada por Claude»).

## 1. Imagen

- [ ] `npx hyperframes@0.9.42 lint .`: 0 errores.
- [ ] Capturas (`snapshot --at`) en cada momento cambiado y en: primer fotograma, cada recurso, cada protagonista, cada paso de la demo, cada flecha al terminar, último fotograma.
- [ ] Hoja de contacto del máster a 2 fps (`fps=2,scale=120:-1,tile=20x3`): ritmo de cambios, nada vacío, nada solapado.
- [ ] Cambios de plano medidos (`select='gt(scene,0.18)'`): nunca más de ≈ 4 s sin un cambio de imagen fuera de la demo.
- [ ] Ningún texto en la barra superior ni por debajo de 1540 px; nada sobre la boca; subtítulos legibles sobre la ropa.
- [ ] Cada protagonista en su zona (sin solapes) y cada flecha con sus dos tarjetas.
- [ ] El texto en pantalla dice lo mismo que la voz (ni contradice ni repite palabra por palabra).
- [ ] Color: el corte coincide con el original (medir pared y negros) o con el look que Ale pidió.

## 1 bis. Dinamismo

- [ ] Auditoría de dinamismo de [MOTION §10.7](../../../guias/MOTION.md): ≥ 16 de 20, o se dice qué falta y por qué.
- [ ] Hoja de contacto lado a lado con la referencia elegida (`referencias/edicion/`).

## 2. Sonido

- [ ] Másteres a −14 LUFS (±0,3) y pico ≤ −1 dBFS.
- [ ] Sonoridad momentánea (`ebur128 … lavfi.r128.M`) en cada pico: la diferencia entre con y sin música dice cuánto pesa la música; un pico sin voz no debe quedar por debajo de ≈ −18 LUFS.
- [ ] Los silencios pedidos existen (antes del pico 3) y el final es seco.
- [ ] Voz sincronizada (desfase medido y aplicado).

## 3. Registro

- [ ] Versión nueva del máster (`edicion_vNN`), PRODUCCION → Historial y `Siguiente_paso`, filas en MEDIOS.csv.
- [ ] `python scripts/marco.py validar` y `python -m unittest discover -s pruebas`.

## Autocrítica

Cuando Ale la pida, se compara con vídeos cortos que retienen bien, sin sesgo del proyecto, y se ordena de más a menos importante en tres grupos:

1. **Se arregla en edición ya** (con propuesta concreta).
2. **Depende de la grabación** (ropa, mirada, B-roll propio, luz).
3. **Depende de la app o de decisiones de Ale** (textos de la app, lema, música con Content ID).

Criterios que se revisan siempre: primer fotograma, promesa en los 3 primeros segundos, tramos sin cambio de imagen, duración de la demo, coherencia texto–voz, zona segura, protagonistas (≤ 4), número de efectos, picos de sonido, bucle (último fotograma ↔ primero) y derechos pendientes.
