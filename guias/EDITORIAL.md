# Línea editorial

**Estado:** provisional. La promesa y los pilares son una propuesta (PR-001 en [DECISIONES](../registro/DECISIONES.md)) que se usa para los primeros ensayos y se confirma o se corrige con datos propios. Las audiencias son hipótesis que hay que validar, no perfiles demostrados.

## Quién habla y de qué

El canal es de **Alexander**, desarrollador, que se presenta como persona. Los proyectos (MiMiniApp y los que vengan) aparecen en los vídeos, pero no son la identidad del canal.

**Promesa propuesta:** «Soy Alexander. Construyo y pruebo proyectos tecnológicos que cualquiera puede entender, y cuento lo que funciona y lo que no».

Lo que lo diferencia (sin pretender exclusividad): cara del creador, utilidad comprobable, interfaz animada con cuidado, proceso abierto y participación de la comunidad.

No se promete que «todo lo de pago será gratis», ni un catálogo o un dominio que aún no existen. No se habla mal de otros creadores o herramientas.

## Audiencias (hipótesis)

| Código | Quién | Qué busca |
|---|---|---|
| A1 | Público general | Resolver un problema cotidiano con un clic |
| A2 | Curiosos | Ideas digitales inusuales y resultados visuales |
| A3 | Desarrolladores | Código, decisiones técnicas, colaboración, open source |

Cada vídeo elige **una** audiencia principal. Mezclarlas sin motivo resta claridad.

## Pilares

| Pilar | Contenido | Audiencia | Señal principal |
|---|---|---|---|
| UTILIDAD | Caso de uso y resultado probado | A1 | Retención, guardados, compartidos |
| PROCESO | Construir en público: decisión, error, avance verificable | A2, A3 | Tiempo visto, comentarios sobre la decisión |
| EXPERIMENTO | Pregunta, hipótesis y resultado reproducible | A2 | Visionados completos, compartidos |
| COMUNIDAD | Pregunta concreta, cómo proponer o contribuir | A3 | Comentarios útiles, propuestas reales |

Un mismo pilar puede repetirse en una semana, pero conviene variar el objetivo.

## Formatos y duraciones de partida

Son rangos para experimentar, no reglas de las plataformas. El montaje sigue la historia: no se alarga un vídeo para llegar a una duración.

| Formato | Familia de guion | Duración inicial |
|---|---|---|
| Demo problema → resultado | A · Demo | 20–45 s |
| Lanzamiento o reto | B · Proceso | 35–65 s |
| Diario de construcción | B · Proceso | 25–60 s |
| Experimento | C · Experimento | 30–60 s |
| Pregunta a la comunidad | D · Comunidad | 15–35 s |
| Tutorial para desarrolladores | E · Tutorial | 45–90 s o dos piezas |

## Seleccionar ideas

1. **Fuentes:** comentarios y preguntas reales, problemas propios, el estado de los proyectos y pruebas hechas. Anota la procedencia en IDEAS.csv. Una segunda fuente independiente da más confianza; separa la señal de la moda.
2. **Descarta** cualquier idea que necesite una demo que no existe o una promesa sin respaldo, salvo que se reenfoque como proceso.
3. **Puntúa** hasta 6 candidatas con cinco criterios de 0 a 2 (0 = ausente, 1 = parcial, 2 = claro y con prueba), 10 puntos en total:
   - valor claro para la audiencia
   - gancho visual comprobable
   - verdad y demostrabilidad (si es 0, no puede ser una demo)
   - encaje con la serie o la comunidad
   - cabe en las horas reales
4. **Elige** las 2–4 mejor respaldadas sin fijar la cantidad antes de mirar la capacidad. En empate gana la que dependa de menos cosas y tenga más prueba real.
5. Ale aprueba el lote con el **OK-1**.

## Capacidad

El presupuesto total es de unas 11–15 h a la semana **incluida la programación**. Al vídeo solo van las horas que sobren después de desarrollo y pruebas. Calcula el coste de cada vídeo con los tiempos reales de `PRODUCCION → Tiempo`. Si falta tiempo, se recortan primero las piezas derivadas, nunca la prueba del producto ni el QC final. Hasta tener datos, cuenta 2–4 h por vídeo sencillo.

## Aprender de los datos

- **Una hipótesis por semana**, con una sola variable: gancho de problema frente a gancho de resultado, demo antes o después de presentarte, duración, densidad de animación, CTA.
- **Ventanas de lectura:** +48h (control rápido) y +7d (comparación). +28d si aporta.
- **Registro** en `registro/METRICAS.csv`, una fila por métrica, publicación, ventana y fecha, con el nombre nativo de la plataforma, la unidad, el denominador si existe y la fuente.
- `NO_DISPONIBLE` con el valor vacío significa que no hay dato. Un `0` con `DISPONIBLE` es una observación real.
- Compara dentro de la misma plataforma. No sumes acumulados de distintas ventanas ni promedies «retención» de redes con definiciones distintas.
- Tras 5–8 piezas, busca patrones descriptivos. Una sola publicación no demuestra causas.
- **Al cerrar la semana:** una cosa que se mantiene, un problema observado y un experimento para la siguiente. Como mucho tres cambios de proceso o de marca por ciclo. No se cambia la marca por un post con pocas impresiones.
