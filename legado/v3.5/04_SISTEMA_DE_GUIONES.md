# Sistema de guiones: estrategia, pruebas, hooks y revisión finita
**Estado: método editorial propuesto, no algoritmo secreto.** Fuentes y cautelas: `01_EVIDENCIA_Y_AUDITORIA.md`.

## Contrato de un vídeo antes de redactar
Completar: `audiencia principal`, `problema/pregunta`, `beneficio o revelación`, `prueba visual disponible`, `única idea central`, `CTA único`, `tipo de guion`, `duración estimada`, `fuente/estado de cada claim`, `nivel de esfuerzo`.
**Bloquea el guion** si no hay promesa concreta o evidencia de cómo se cumplirá.

## Familias de guion con estructuras propuestas
### A. Demo útil (usuario general)
1. **Gancho visual + resultado o fricción concreta** (primeros 1–3 s; hipótesis de diseño, no duración universal).
2. Contexto en una frase: quién pierde tiempo y en qué.
3. Demostración real o reconstrucción cinematográfica fiel (mostrar entrada, transformación, salida).
4. Prueba: resultado validado, sin esconder limitaciones.
5. CTA relacionado con el caso (probar si URL existe; de lo contrario seguir el avance o sugerir idea).

### B. Construir en público
1. Gancho: tensión verificable («esta parte no funcionaba», si hay evidencia).
2. Obstáculo, decisión y por qué importaba para la persona que lo usará.
3. Antes/después o prueba funcional.
4. Próximo paso real y una pregunta si encaja.

### C. Curiosidad / experimento
1. Pregunta original que una persona entiende.
2. Hipótesis explícita, sin presentar como hecho.
3. Experimento y resultado reproducible.
4. Interpretación honesta y límite.

### D. Comunidad / colaboración
1. Resultado o contexto real de la serie.
2. Qué decisión se pide a la audiencia, con un marco concreto.
3. Qué sucederá con sus respuestas (manual si no existe sistema de votos).
4. Pregunta única; para colaboradores, condiciones reales y pasos verificables de GitHub.

### E. Tutorial desarrollador
1. Resultado final mostrado primero.
2. Prerrequisitos verificados (versión/URL/ramas).
3. 2–4 pasos con terminal real, comandos efectivamente ejecutados.
4. Prueba de que terminó bien; documentación en enlace si existe.

## Elegir el gancho sin iteración infinita
1. Un agente redacta **2 ganchos** (uno por problema, otro por resultado), máximo 18 palabras cada uno como norma interna inicial.
2. Puntuar de 0–2 cada uno: `comprensible sin contexto`, `alineado a contenido`, `evidencia visible pronta`, `interés genuino/no clickbait`. Gana el mayor; empate: el más claro.
3. Únicamente **una** reescritura si ambos fallan. Si siguen fallando: no rehacer el estilo; volver al problema o elegir otra idea.
4. No comenzar «Hola, soy...» cuando la audiencia aún no sabe por qué debería quedarse; el rostro puede abrir con acción y conflicto sin presentación larga.
5. El storyboard marca el fotograma/prueba que paga la promesa. Si no se cumple, gancho rechazado.

## Lenguaje y estilo de voz
- Primera persona, natural, concreto. No hacer del autor un «gurú» de la IA.
- Preferir «voy a probar», «he creado», «hoy conseguí» y «aún no funciona» según evidencia real.
- Evitar «todas las herramientas cobran», «gratis para siempre» y claims absolutos no demostrables.
- En textos editoriales, **una promesa por pantalla**, frases cortas y subtítulos sincronizados; no duplicar el mismo párrafo en texto y voz.

## Ejemplo de guion de lanzamiento — PROVISIONAL, sujeto a estado real
- Gancho con rostro: «Me cansé de encontrar herramientas que me pedían suscripción. Así que empecé a construir mis propias alternativas» (`O`: experiencia subjetiva; comprobar naturalidad del diálogo).
- Qué es: «Quiero reunir miniherramientas que cualquiera pueda probar desde su navegador» (`H`: objetivo, no catálogo ya publicado).
- Prueba: «Esta semana estoy preparando la primera» + presentar solo material realmente implementado; si no existe, mostrar progreso y no demo falsa.
- Cierre: «¿Qué pequeña herramienta te ahorraría tiempo?» (pregunta concreta, sin prometer implementación automática).

## Tiempos y claridad: presupuestos de trabajo, NO hechos de algoritmo
- Borrador 1 → reescritura 1 → **aprobación o bloqueo**. Nunca 9 versiones sin cambio de evidencia.
- Una vez aprobado el guion, cambios de texto requieren ticket breve (motivo, alcance, efecto en audio/animación).
- Leerlo en voz alta y medir duración; el modelo no inventa el tiempo exacto a partir del número de palabras.
- Validar que el storyboard muestre el resultado pronto sin sacrificar honestidad.

## «Guion técnico» es distinto de «guion narrado»
Cada escena requiere: ID, tiempo aproximado, voz literal, emoción/intención, plano/activo, fuente de verdad, técnica HyperFrames, transformación de UI, pista de audio/SFX, subtítulo, CTA, verificación y estado.
El agente editor no decide después de grabar qué quiere decir la historia.
