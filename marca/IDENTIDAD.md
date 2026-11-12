# Identidad de Alexander

**Estado:** provisional. Se trabaja con el perfil **TEMP** hasta que Ale apruebe una identidad pública (decisión B0). Publicar con TEMP está permitido. Lo que no se hace es presentarlo como marca definitiva ni usar un @alias sin verificar.

## Quién es el canal

- El creador es **Alexander**, desarrollador, y se presenta como persona (CREATOR-IDENTITY-001).
- MiMiniApp y otros proyectos son proyectos de Alexander. No son el nombre de las cuentas, ni el canal, ni deciden los colores de los vídeos.
- Bien: «Soy Alexander. Estoy construyendo MiMiniApp, una web de pequeñas herramientas…». Mal: «Somos MiMiniApp» o `@miminiapp` en las cuentas personales.
- Hasta tener alias verificado: nombre mostrado **«Alexander | Desarrollador»**, sin `@` en vídeos, portadas ni subtítulos.

## Alias (pendiente: CREATOR-ALIAS-002)

Objetivo: el mismo `@alias` en YouTube, TikTok, Instagram y Facebook.

Criterios: empieza por Alex, fácil de decir y escribir en español, 14 caracteres como máximo, sin tildes, puntos, guiones ni números, que no ate a una sola app o lenguaje y que se pueda registrar en las cuatro redes.

| Prioridad | Candidato | A favor | En contra |
|---|---|---|---|
| 1 | `alexenbeta` | Personal y memorable, cuenta un proceso | «beta» puede envejecer mal |
| 2 | `alexcompila` | Vínculo claro con programar | Algo técnico para el público general |
| 3 | `alexcreabits` | Tecnológico, admite varios proyectos | Menos natural al decirlo |
| 4 | `alexiterativo` | Experimentación continua | Concepto menos inmediato |

Una búsqueda sin resultados **no** demuestra que esté libre. La prueba es intentar guardarlo en cada red:

1. Instagram → Editar perfil → Nombre de usuario → guardar.
2. TikTok → Editar perfil → Nombre de usuario (solo se puede cambiar cada 30 días).
3. YouTube Studio → Personalización → Identificador.
4. Facebook → la página o el perfil profesional elegido → nombre de usuario.

Si falla en una, se prueba el siguiente candidato. No se abren cuentas con nombres distintos. Al confirmar, se rellena `marca/CUENTAS.csv` (alias, URL, fecha, evidencia, estado `VERIFICADA`) y se cierra la decisión en [DECISIONES](../registro/DECISIONES.md).

## Perfil TEMP

| Elemento | Valor de prueba |
|---|---|
| Personalidad | «Laboratorio digital luminoso sobre fondo nocturno»: moderno, cercano, con momentos cinematográficos y sin ruido visual |
| Paleta candidata A | Ver tabla siguiente y [identidad.json](identidad.json) |
| Tipografía | Inter (subtítulos y rótulos) y combinaciones de acento de [EDICION](../guias/EDICION.md) |
| Sonido | Voz real primero, efectos solo en acciones, música discreta o silencio |
| Movimiento | Interfaz por capas, transformaciones con continuidad, rótulos breves |

| Token | HEX | Uso | Contraste sobre fondo |
|---|---|---|---|
| Fondo | `#0B1020` | Base de escenas animadas, sin negro puro | — |
| Panel | `#17243A` | Tarjetas e interfaz ficticia de vídeo | — |
| Texto principal | `#F3F7FF` | Narrativa y resultados | 17,6:1 |
| Texto secundario | `#B9CAE2` | Explicaciones | 11,4:1 |
| Cian | `#54E0EA` | Acento principal | 11,9:1 |
| Violeta | `#AD8BFF` | Profundidad, degradados | 7,1:1 |
| Lima | `#D9F77A` | Confirmación puntual del resultado | 15,8:1 |

El contraste está calculado con la fórmula WCAG sobre color plano. En vídeo, los degradados, brillos y la compresión lo reducen: compruébalo en el móvil. La paleta es una propuesta de diseño, no una preferencia demostrada de la audiencia.

## Cómo se aprueba la identidad (B0)

1. Crear dos fotogramas originales con el perfil candidato: uno a cámara con rótulo y otro con interfaz animada.
2. Verlos en el móvil con el brillo habitual: legibilidad, color, personalidad y subtítulos.
3. Ale aprueba o pide **una** revisión concreta.
4. Se registra la decisión en DECISIONES, se pasa `identidad.json` a `"estado": "APROBADA"` con versión y fecha, y el perfil visual de los vídeos pasa de `TEMP` a `v1`.
5. La identidad se congela durante al menos cinco vídeos. Solo se cambia con una decisión registrada.
