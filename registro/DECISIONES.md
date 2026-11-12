# Registro de decisiones

Una fila por decisión, con ID único. No se reescribe la historia: si una decisión cambia, se añade una fila nueva que la sustituye y se cambia el estado de la anterior a `SUSTITUIDA por <ID>`. Una PROPUESTA solo pasa a APROBADA con la fecha y el texto de aprobación de Ale.

| ID | Fecha | Decisión | Estado | Base |
|---|---|---|---|---|
| CREATOR-IDENTITY-001 | 2026-11-05 | El creador es Alexander. Cuentas y marca audiovisual personales, independientes de MiMiniApp | APROBADA | Mensaje explícito de Ale |
| AV-001 | 2026-11-05 | HyperFrames es el motor de animación principal; Remotion, la alternativa si falla una prueba real | APROBADA | Conversación |
| AV-002 | 2026-11-05 | Interfaz cinematográfica por capas, no grabación de pantalla plana por defecto | APROBADA | Conversación y capturas de referencia |
| AV-003 | 2026-11-05 | Animaciones nuevas para cada vídeo; se reutiliza el flujo, no todos los recursos | APROBADA | Conversación |
| AV-004 | 2026-11-05 | Planificación semanal, guiones y aprobaciones humanas antes de publicar | APROBADA | Conversación; concretado en el marco 5.0 |
| AV-005 | 2026-11-05 | La identidad audiovisual es distinta de la identidad web de los productos | APROBADA | Conversación |
| D-EDIT | 2026-11-06 | CapCut Desktop gratis como editor final y Shotcut como alternativa. Sin funciones de pago | APROBADA; exportación gratis por probar | Propuesta de Ale |
| D-EDICION | 2026-11-08 | Cada guion incluye la dirección de montaje: música, efectos, tipografía, color y marca | APROBADA | Petición de Ale |
| PR-001 | 2026-11-05 | Promesa editorial y cuatro pilares de [EDITORIAL](../guias/EDITORIAL.md) | PROPUESTA; se usa en los ensayos | Investigación y criterio editorial |
| PR-002 | 2026-11-05 | Paleta candidata A y estilo de movimiento del perfil TEMP | PROPUESTA | Diseño propio, sin datos de audiencia |
| PR-003 | 2026-11-05 | Selección de ideas con cinco criterios 0–2 y dos ganchos como máximo | PROPUESTA; se usa en los ensayos | Criterio de eficiencia |
| CREATOR-ALIAS-002 | 2026-11-05 | Un único @alias en las cuatro redes; candidatos en [IDENTIDAD](../marca/IDENTIDAD.md) | PENDIENTE | Falta comprobarlo en cada red |
| PROD-14 | 2026-11-05 | Primera miniapp de MiMiniApp | PENDIENTE | Aplazada expresamente |
| MARCO-5.0 | 2026-11-12 | Marco 5.0: estructura limpia, CLI único, aprobaciones con un comando, medios fuera de Git y sin legado en el árbol de trabajo | APROBADA | Ale en chat: autoriza rehacer el marco y no conservar la información antigua |
