# Identidad de Alexander

**Estado:** provisional. Se trabaja con el perfil **TEMP** hasta que Ale apruebe una identidad pública (decisión B0). Publicar con TEMP está permitido. Lo que no se hace es presentarlo como marca definitiva ni usar un @alias sin verificar.

## Quién es el canal

- El creador es **Alexander**, desarrollador, y se presenta como persona (CREATOR-IDENTITY-001).
- MiMiniApp y otros proyectos son proyectos de Alexander. No son el nombre de las cuentas, ni el canal, ni deciden los colores de los vídeos.
- Bien: «Soy Alexander. Estoy construyendo MiMiniApp, una web de pequeñas herramientas…». Mal: «Somos MiMiniApp» o `@miminiapp` en las cuentas personales.
- El nombre del canal es **cerobytes** (CREATOR-ALIAS-003). Alexander sigue presentándose como persona: «Soy Alexander…».

## Alias (CREATOR-ALIAS-003)

No hubo un alias libre en todas las redes. Ale eligió el 2026-11-12 quedarse con estos, y no se buscan otros:

| Red | Identificador | URL |
|---|---|---|
| YouTube | `@soy.cerobytes` | https://www.youtube.com/@soy.cerobytes |
| TikTok | `@cerobytes` | https://www.tiktok.com/@cerobytes |
| Instagram | `@cer0bytes` (con el número cero) | https://www.instagram.com/cer0bytes/ |
| Facebook | perfil «cerobytes», sin nombre de usuario propio | https://www.facebook.com/p/cerobytes-61596111701428/ |
| X (solo posts con enlace, DIST-X-001) | `@soycerobytes` | https://x.com/soycerobytes |

Detalle verificado en `marca/CUENTAS.csv`.

Cómo se nombra, ya que los identificadores no coinciden:

- **Voz**: «cerobytes», sin decir arroba ni deletrear.
- **Máster**: sin `@` grabado en la imagen. Si hace falta firma, se escribe «cerobytes» a secas, que vale en todas las redes.
- **Copy, descripción y tarjetas finales de cada red**: el identificador exacto de esa red, según la tabla. En Instagram es `@cer0bytes`, nunca `@cerobytes`.

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
