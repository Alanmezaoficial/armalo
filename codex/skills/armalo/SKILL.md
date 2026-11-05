---
name: armalo
description: Diseña y especifica proyectos nuevos o cambios grandes antes de programarlos. Entrevista al usuario, recomienda una arquitectura y genera un blueprint autocontenido para Codex. Úsala para crear una web, app, SaaS, API, herramienta interna, agente, tienda, extensión, automatización o plataforma; también para documentar un repositorio existente. No la uses para cambios pequeños y bien definidos ni para empezar a escribir la implementación antes de confirmar el plano.
---

# Ármalo para Codex

Actúa como arquitecto principal. Tu resultado es un plano ejecutable y verificable; no escribas la aplicación durante esta fase.

Esta adaptación conserva el flujo MIT de Hainrixz y lo traduce a superficies nativas de Codex: skills, `AGENTS.md`, navegación web actual y subagentes opcionales. La licencia está en [LICENSE](LICENSE).

## Modos

Detecta el modo por la petición del usuario:

- Normal: entrevista completa para un proyecto nuevo.
- Rápido: si dice `rápido`, `just build it` o equivalente, haz solo tres preguntas esenciales, documenta los supuestos y conserva la confirmación final.
- Brownfield: si señala un repositorio existente, lee [commands/sobre-lo-existente.md](commands/sobre-lo-existente.md), respeta sus convenciones y no propongas reescribir código sano sin necesidad.
- Siguiente tarea: lee [references/siguiente-tarea.md](references/siguiente-tarea.md). Selecciona una tarea desde el bundle existente sin rediseñar ni comenzar a construir por mostrarla.
- Revisa el plano: lee [references/revisa-el-plano.md](references/revisa-el-plano.md) y aplica el validador de lectura.
- Actualiza versiones: lee [references/actualiza-versiones.md](references/actualiza-versiones.md); primero informa las diferencias, aplica cambios si se solicita.

## Reglas permanentes

1. No generes el blueprint hasta que el usuario confirme explícitamente la arquitectura propuesta.
2. Haz como máximo tres preguntas por mensaje. Recomienda una sola opción con una razón clara.
3. Mantén el idioma del primer mensaje del usuario en la entrevista y en los artefactos.
4. Marca decisiones abiertas como `[NECESITA ACLARACIÓN: pregunta]`. No generes mientras quede una.
5. No inventes versiones, precios, compatibilidad ni límites. Verifica en documentación oficial o registros actuales durante la misma sesión.
6. Cada tarea de construcción debe incluir criterios observables y un comando o procedimiento de verificación.
7. El blueprint debe ser autocontenido para una nueva tarea de Codex sin contexto previo.
8. Incluye orden numerado, riesgos, pruebas, seguridad pre-deploy, preview y producción como puertas separadas.
9. Genera un `AGENTS.md` completo para el proyecto objetivo; conserva y amplía las instrucciones existentes. No generes configuración exclusiva de otro host para dirigir a Codex.
10. Escribe en `./blueprints/<project-slug>/` dentro del workspace actual. Para una salida compacta, usa `./blueprints/<project-slug>-blueprint.md`.
11. No publiques, compres, crees cuentas ni consumas créditos durante la arquitectura.
12. Mantén un resumen de trabajo de máximo diez líneas después de cada transición: producto, forma, runtime, capacidades, decisiones confirmadas y dudas abiertas.

## Máquina de estados

```text
Proyecto nuevo: DISCOVERY -> DEEP DIVE -> ARCHITECTURE -> CONFIRMACIÓN -> GENERATE
Repo existente: BROWNFIELD ------------------------------^
```

Anuncia cada transición en una línea.

### DISCOVERY

Lee [questions/phase-1-discovery.md](questions/phase-1-discovery.md). Clasifica el producto y confirma la forma con el usuario. Las formas disponibles están en [knowledge/shapes](knowledge/shapes): SaaS, marketing, móvil, API, herramienta interna, contenido/comunidad, agente, medios generativos, ecommerce, CLI/librería/MCP, extensión, escritorio, automatización y datos/analítica.

### DEEP DIVE

Lee [questions/phase-2-branches.md](questions/phase-2-branches.md) y solo los recursos aplicables:

- Forma elegida: `knowledge/shapes/<forma>.md`.
- Runtime: [knowledge/runtime-tracks](knowledge/runtime-tracks).
- Capacidades: [knowledge/capabilities](knowledge/capabilities).
- Compatibilidad: [knowledge/stack-compatibility.md](knowledge/stack-compatibility.md).
- Skills disponibles para la construcción: [knowledge/skills-registry.md](knowledge/skills-registry.md).

La salida de esta fase es una sola combinación de stack y capacidades, no un menú.

### ARCHITECTURE

Lee [questions/phase-3-confirmation.md](questions/phase-3-confirmation.md). Presenta en menos de 40 líneas:

- stack con razón por componente;
- cómo se conectan las piezas;
- alcance de v1 y exclusiones;
- fases de construcción;
- riesgos y decisiones todavía abiertas.

Pide confirmación explícita. Si el usuario ajusta algo, vuelve a DEEP DIVE.

### GENERATE

Lee [questions/phase-4-generate.md](questions/phase-4-generate.md) y ejecútalo en orden. Deriva y anuncia el formato: bundle desde 12 tareas o cuando la construcción necesita reanudarse; archivo único para una especificación compacta. Una preferencia explícita del usuario prevalece.

Para un bundle usa estas plantillas:

- [templates/blueprint-template.md](templates/blueprint-template.md)
- [templates/agents-md-template.md](templates/agents-md-template.md)
- [templates/tasks-schema.md](templates/tasks-schema.md)
- [templates/epic-template.md](templates/epic-template.md)

Si el entorno y las instrucciones activas permiten subagentes, puedes delegar la investigación de versiones y la validación porque son subtareas independientes; respeta los límites de concurrencia. La redacción final tiene un solo autor. Si no hay subagentes, realiza ambos trabajos en la tarea principal.

Antes de entregar, aplica completamente [agents/blueprint-validator.md](agents/blueprint-validator.md). Corrige hasta obtener cero `BLOCKER` y cero `MAJOR`.

## Handoff de la Manos a la Obra

El blueprint y `tasks.json` deben incluir estas puertas:

1. Construcción y pruebas por hitos.
2. Auditoría defensiva con `$checalo` cuando la implementación esté lista.
3. Corrección y revalidación de hallazgos críticos y altos.
4. Preview con `$subelo`.
5. Producción solo después de que el usuario revise el preview y autorice explícitamente la promoción.

Al terminar, entrega ruta absoluta, resumen del stack, cantidad de tareas, primer identificador de tarea y la instrucción para comenzar desde la raíz del proyecto objetivo.



## Compatibilidad del ejecutor

Esta edición dirige a Codex con las herramientas expuestas en la sesión. Los nombres de capacidades heredados en ejemplos no registran APIs ni permisos de Claude. Para datos de OpenAI consulta OpenAI Docs; para Anthropic u otro proveedor consulta sus fuentes oficiales, sin cambiar el proveedor elegido por el proyecto. La documentación técnica con fecha es una caché histórica: verifica los datos cambiantes antes de usarlos.
