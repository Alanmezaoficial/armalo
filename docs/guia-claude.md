---
title: 'Ármalo · Edición Claude'
---

# Ármalo

Planea lo que vas a construir. Esta guía te acompaña desde la preparación hasta el resultado y señala qué necesita comprobarse en tu entorno.

## Empieza por aquí: tres formas de instalar

Elige solo una opción. La instalación conserva la herramienta completa con sus referencias y scripts. Esta edición principal es para Claude Code; la variante Cowork de Súbelo se explica más abajo.

### 1. Copia un prompt con los enlaces · recomendado

Copia el bloque completo, pégalo en un chat nuevo de Claude Code y deja que prepare la instalación. La guía enlazada es pública en GitHub: no necesita iniciar sesión en el Bunker.

```text
Instala para mi usuario la edición Claude Code de Ármalo como plugin completo.

Guía pública: https://github.com/Alanmezaoficial/armalo/blob/main/docs/guia-claude.md
Repositorio: https://github.com/Alanmezaoficial/armalo

Lee la guía. Si estás en Claude Code con acceso a mi equipo, registra el catálogo Alanmezaoficial/armalo e instala armalo@alanmeza-armalo con los comandos admitidos por mi versión. Conserva la carpeta completa, sus scripts, referencias, plantillas, LICENSE y NOTICE. No sustituyas la herramienta por un resumen ni cambies su contenido. Si ya está instalada con ese nombre, detente y dime qué versión encontraste antes de reemplazarla.

Conserva también los comandos, agentes y el manifiesto del plugin. Verifica la instalación con la lista de plugins e indica cómo comprobar su activación en una sesión nueva. No ejecutes la skill todavía. Si estás en una conversación sin acceso al equipo o el host no admite este plugin, explica qué necesito sin simular una instalación.
```

### 2. Descarga el ZIP y acompáñalo con este prompt

En la ficha de esta edición, pulsa Descargar ZIP. Adjunta el archivo a un chat de Claude Code o indica su ruta local si el host no admite ese adjunto; después pega el bloque. Descargar o adjuntar el archivo sin pedir la instalación no lo instala. Cada ZIP incluye INSTALAR.md con estas instrucciones.

```text
Instala para mi usuario la edición Claude Code de Ármalo del ZIP adjunto armalo-claude-1.0.1.zip, como plugin completo.

Guía pública de apoyo: https://github.com/Alanmezaoficial/armalo/blob/main/docs/guia-claude.md

Localiza el ZIP o pide su ruta local si no puedes acceder al adjunto. Extrae de forma segura la carpeta armalo en una ubicación persistente y lee INSTALAR.md. Esta carpeta incluye .claude-plugin/plugin.json y su catálogo local .claude-plugin/marketplace.json, cuyo source es ./; registra ese catálogo local e instala armalo@alanmeza-armalo. Conserva la carpeta completa, sus scripts, referencias, plantillas, LICENSE y NOTICE. No sustituyas la herramienta por un resumen ni cambies su contenido. Si ya está instalada con ese nombre, detente y dime qué versión encontraste antes de reemplazarla.

Conserva comandos, agentes y recursos del plugin. Valida y consulta la lista de plugins, informa de la ruta y de la comprobación pendiente en una sesión nueva. No ejecutes la skill todavía. Si el host no es compatible o no tiene acceso al equipo, indícalo sin afirmar que quedó instalada.
```

<details>
<summary>3. Prefiero instalar manualmente · Terminal · Claude Code</summary>

Con Claude Code instalado y autenticado, abre una terminal y pega estas tres líneas. El catálogo obtiene el plugin completo desde GitHub. No necesita pedirle trabajo a una IA.

```text
claude plugin marketplace add Alanmezaoficial/armalo
claude plugin install armalo@alanmeza-armalo
claude plugin list
```

</details>

### Confirma que quedó disponible

Consulta claude plugin list y abre una sesión nueva de Claude Code para comprobar los comandos del plugin. Si la carpeta existe pero no aparece en el selector, informa de ambas cosas; no son la misma prueba.

Las secciones siguientes explican requisitos y alternativas con más detalle.

## Antes de instalar

La edición principal necesita **Claude Code**, no solo una conversación en claude.ai. Debes tenerlo instalado, autenticado y con acceso a la carpeta del proyecto. Las herramientas del proyecto y las CLIs de alojamiento se obtienen aparte cuando hagan falta. No hay credenciales ni cuentas incluidas.

Se conserva el flujo original de Claude y su resolución de recursos. En Súbelo, el original principal declara macOS/Linux y WSL2 para Windows. Un paquete que se puede descomprimir en Windows no demuestra que todos sus comandos POSIX funcionen en PowerShell.

## Instalar desde GitHub

El [repositorio público](https://github.com/Alanmezaoficial/armalo) contiene el catálogo y las dos ediciones. Dentro de una sesión de Claude Code:

```text
/plugin marketplace add Alanmezaoficial/armalo
/plugin install armalo@alanmeza-armalo
/plugin list
```

El nombre después de `@` corresponde al catálogo de este repositorio, distinto en cada skill. Instalarlo registra el plugin en tu entorno; comprueba después el comando indicado abajo y ejecuta un encargo pequeño. La publicación del repositorio no sustituye esa prueba del host.

## Prueba el plugin local

Descomprime el repositorio preparado y abre una terminal en su raíz. Para cargar el plugin solo durante esa sesión:

```text
claude --plugin-dir ./claude
```

Para registrarlo mediante su catálogo local:

```text
claude plugin validate .
claude plugin validate ./claude
claude plugin marketplace add .
claude plugin install armalo@alanmeza-armalo
claude plugin list
```

Los comandos de catálogo cambian la configuración local de Claude; ejecútalos cuando quieras instalar. No utilizan un repositorio público. Si descargaste solo el ZIP Claude, descomprímelo y usa `claude --plugin-dir` con su carpeta superior: el ZIP ahora incluye también su propio catálogo local. Después de guardarlo en una ubicación persistente, puedes registrar esa carpeta con `claude plugin marketplace add RUTA_A_LA_CARPETA` e instalar el plugin por su nombre.

## Comprueba qué se cargó

Abre el menú de skills/comandos y busca `/armalo:armalo`. El prefijo es el nombre del plugin. Si copias solo el `SKILL.md`, faltarán sus referencias; conserva la carpeta completa. No mezcles la instalación como plugin con una copia parcial en `~/.claude/skills`.

Validar el manifiesto, instalarlo y ejecutar un encargo son tres pasos diferentes. Los JSON/YAML y recursos de esta edición se revisan localmente; la instalación y el flujo conversacional en Claude Code o Cowork no se presentan como probados si no se abrió ese host.

## El primer encargo: una idea con un límite claro

Puedes empezar con algo pequeño: organizar tus clips, preparar una portada o documentar una aplicación que ya tienes. Explica qué quieres conseguir, quién lo usará y dónde trabajas. No necesitas elegir todas las tecnologías antes de comenzar.

```text
/armalo:armalo Quiero una herramienta local para ordenar mis clips por proyecto. La usaré yo en Windows. Primero ayúdame a definir el alcance y el plano; la construcción vendrá después.
```

Ármalo pregunta, propone una arquitectura y espera tu confirmación antes de generar el plano. Rápido reduce la entrevista; mantiene esa confirmación. La salida puede ser un Markdown compacto o un bundle con `blueprint.md`, tareas, épicas e instrucciones de trabajo. El documento no es una aplicación construida.

## Elige el recorrido que corresponde

| Recorrido | Cuándo sirve | Activación lista para adaptar |
|---|---|---|
| Ármalo | Una idea nueva con decisiones por resolver | `/armalo:armalo Quiero planear una herramienta para organizar mis clips.` |
| Ármalo rápido | Ya sabes qué quieres, quién lo usa y tus límites técnicos | `/armalo:rapido Una portada local de portafolio, para mostrar mis videos.` |
| Ármalo sobre lo existente | Ya hay código y quieres un cambio concreto | `/armalo:sobre-lo-existente Añade un buscador a este proyecto conservando las rutas y su diseño.` |
| Ármalo: siguiente tarea | Tienes un bundle y quieres retomarlo | `/armalo:siguiente-tarea blueprints/mi-proyecto --listar` |
| Ármalo: actualiza versiones | El diseño sigue siendo válido, pero sus versiones requieren revisión | `/armalo:actualiza-versiones blueprints/mi-proyecto` |
| Ármalo: revisa el plano | Quieres comprobar contratos, tareas y verificaciones sin editar | `/armalo:revisa-el-plano blueprints/mi-proyecto` |

Los nombres de rutas como `mi-proyecto` son ejemplos que debes cambiar por tu carpeta real.

## Reanudar no significa volver a empezar

«Siguiente tarea» lee el archivo actual, respeta las dependencias y atiende trabajo interrumpido antes de repartir otro. `--listar` muestra la cola; `--tarea ID` muestra una tarjeta; `--iniciar ID` registra progreso; `--terminar ID` exige comprobar todas las verificaciones antes de cerrar la tarea. Los alias ingleses `--list`, `--task`, `--start` y `--done` se conservan por compatibilidad.

Un estado `deferred` sigue pendiente. No se convierte en terminado para saltar una puerta de publicación. Si faltan dependencias o hay un ciclo, el resultado correcto es explicar el bloqueo. El helper de lectura de Codex no escribe ni ejecuta verificaciones automáticamente.

## Actualizar y revisar son trabajos distintos

La revisión del plano es de lectura. La actualización de versiones primero informa qué cambió, con fuentes actuales y posibles migraciones. `--aplicar` o su alias `--apply` solicita los cambios de versiones; no autoriza rediseñar el producto ni actualizar la skill instalada.

## Qué te pedirá y qué recibirás

Te pedirá el resultado esperado, usuarios, alcance, tecnología obligatoria, restricciones y decisiones que aún no pueda deducir. Sobre un repositorio leerá sus convenciones antes de proponer cambios. Recibirás el plano, criterios observables, orden de trabajo, comandos o procedimientos de verificación y requisitos pendientes.

El flujo completo cubre cuatro fases. Las 14 formas de producto, cinco familias de runtime y 18 capacidades son recursos que se consultan cuando corresponden; no necesitas instalar una skill para cada una.

## Diferencias entre ediciones

Claude conserva su plugin, comandos y recursos originales, con instrucciones de proyecto propias de ese host. Codex conserva la adaptación que usa `AGENTS.md`, herramientas disponibles y Windows; añade lectura de los dos esquemas de tareas y controles de consistencia recuperados. No interpreta el esquema antiguo como si fuera el nuevo ni reemplaza un proveedor de IA por cambiar el host del agente.

## Si algo no encaja

- **El plano menciona un archivo inexistente:** pide «revisa el plano» y conserva el hallazgo; no marques la tarea terminada.
- **Un bundle anterior no se reconoce:** revisa su estructura y estados; no lo reformatees a mano solo para que pase.
- **No se pudo comprobar una versión:** debe figurar como pendiente de verificación, sin afirmar que una fecha de caché es una consulta actual.
- **La entrevista vuelve a preguntar algo decidido:** señala la decisión ya confirmada y pide que se conserve en el resumen de trabajo.

## Mantener esta edición

Antes de actualizar guarda una copia de tu carpeta instalada y de cualquier cambio propio. Revisa `upstream.lock.json`, `CHANGELOG.md` y `docs/actualizar-desde-original.md` en el repositorio preparado. Compara la siguiente revisión en otra carpeta; no uses un reemplazo completo para integrar cambios pequeños.

Actualiza solo la edición que utilizas. Comprueba referencias y extracción, vuelve a instalar en un destino aislado y después ejecuta un encargo representativo. Las actualizaciones de estas skills y las versiones del proyecto que estás construyendo son trabajos distintos.

## Autoría y comprobaciones

Adaptación y documentación de **Alanmeza.ai**, sobre los proyectos originales de **Enrique Rocha / Hainrixz** y, en Chécalo, **Cyber Neo Contributors**. Se conservan MIT, `LICENSE`, `NOTICE` y los avisos de procedencia. Consulta el registro de validación de esta edición para distinguir scripts probados, copia instalada y host conversacional pendiente.
