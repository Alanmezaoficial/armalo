---
title: 'Ármalo · Edición Codex'
---

# Ármalo

Planea lo que vas a construir. Esta guía te acompaña desde la preparación hasta el resultado y señala qué necesita comprobarse en tu entorno.

## Empieza por aquí: tres formas de instalar

Elige solo una opción. La instalación conserva la herramienta completa con sus referencias y scripts. Usa Codex en un entorno con acceso a archivos.

### 1. Copia un prompt con los enlaces · recomendado

Copia el bloque completo, pégalo en un chat nuevo de Codex y deja que prepare la instalación. La guía enlazada es pública en GitHub: no necesita iniciar sesión en el Bunker.

```text
Instala para mi usuario la edición Codex de Ármalo.

Skill: https://github.com/Alanmezaoficial/armalo/tree/main/codex/skills/armalo
Guía pública: https://github.com/Alanmezaoficial/armalo/blob/main/docs/guia-codex.md
Repositorio: https://github.com/Alanmezaoficial/armalo

Lee la guía y usa skill-installer si está disponible, indicando la ruta codex/skills/armalo y la carpeta personal de skills que detecta esta versión de Codex. Conserva la carpeta completa, sus scripts, referencias, plantillas, LICENSE y NOTICE. No sustituyas la herramienta por un resumen ni cambies su contenido. Si ya está instalada con ese nombre, detente y dime qué versión encontraste antes de reemplazarla.

Comprueba que SKILL.md y todos sus recursos quedaron instalados. Indica la ruta final y cómo comprobar que aparece en el selector. No inicies un proyecto ni ejecutes la skill todavía. Si no tienes acceso a archivos o a GitHub, explica qué falta sin afirmar que la instalaste.
```

### 2. Descarga el ZIP y acompáñalo con este prompt

En la ficha de esta edición, pulsa Descargar ZIP. Adjunta el archivo a un chat de Codex o indica su ruta local si el host no admite ese adjunto; después pega el bloque. Descargar o adjuntar el archivo sin pedir la instalación no lo instala. Cada ZIP incluye INSTALAR.md con estas instrucciones.

```text
Instala para mi usuario la edición Codex de Ármalo que adjunto en el ZIP armalo-codex-1.0.1.zip.

Guía pública de apoyo: https://github.com/Alanmezaoficial/armalo/blob/main/docs/guia-codex.md

Localiza el ZIP adjunto o su archivo local accesible, revisa su estructura y extrae de forma segura la carpeta armalo. Copia esa carpeta completa a la ubicación personal de skills que detecta mi Codex. Conserva la carpeta completa, sus scripts, referencias, plantillas, LICENSE y NOTICE. No sustituyas la herramienta por un resumen ni cambies su contenido. Si ya está instalada con ese nombre, detente y dime qué versión encontraste antes de reemplazarla.

Comprueba SKILL.md y la integridad de los archivos copiados, indica la ruta final y cómo comprobar el selector. No ejecutes la skill todavía. Si el ZIP no es accesible desde este chat, pídeme su ruta local; no uses una descarga de la edición Claude.
```

<details>
<summary>3. Prefiero instalar manualmente · Windows · PowerShell</summary>

Descarga el ZIP de esta edición. En Windows, abre PowerShell y pega el bloque completo. Busca el archivo en Descargas; si lo guardaste en otra carpeta, cambia solo zipPath. No necesita pedirle trabajo a una IA.

```powershell
$zipPath = Join-Path $env:USERPROFILE 'Downloads\armalo-codex-1.0.1.zip'
$skillsRoot = Join-Path $env:USERPROFILE '.agents\skills'
$destination = Join-Path $skillsRoot 'armalo'
if (!(Test-Path -LiteralPath $zipPath -PathType Leaf)) { throw 'No encuentro el ZIP en Descargas. Ajusta zipPath a su ubicación.' }
if (Test-Path -LiteralPath $destination) { throw 'La skill ya existe. Revisa su versión antes de actualizar.' }
$staging = Join-Path ([System.IO.Path]::GetTempPath()) ('manos-instalar-' + [guid]::NewGuid().ToString('N'))
Expand-Archive -LiteralPath $zipPath -DestinationPath $staging
$source = Join-Path $staging 'armalo'
if (!(Test-Path -LiteralPath (Join-Path $source 'SKILL.md') -PathType Leaf)) { throw 'El ZIP no tiene la estructura esperada.' }
New-Item -ItemType Directory -Path $skillsRoot -Force | Out-Null
Copy-Item -LiteralPath $source -Destination $destination -Recurse
foreach ($file in Get-ChildItem -LiteralPath $source -File -Recurse) {
  $relative = $file.FullName.Substring($source.Length + 1)
  $copy = Join-Path $destination $relative
  if ((Get-FileHash -LiteralPath $file.FullName).Hash -ne (Get-FileHash -LiteralPath $copy).Hash) { throw ('Copia distinta: ' + $relative) }
}
Write-Output ('Archivos instalados y comprobados en: ' + $destination)
```

</details>

### Confirma que quedó disponible

Abre el selector de skills en una sesión nueva y busca Ármalo. Si no aparece, reinicia Codex. Si la carpeta existe pero no aparece en el selector, informa de ambas cosas; no son la misma prueba.

Las secciones siguientes explican requisitos y alternativas con más detalle.

## Antes de instalar

Necesitas Codex con acceso al sistema de archivos del equipo y una carpeta de trabajo. La biblioteca está en el apartado ChatGPT, pero este paquete está preparado para Codex: descargarlo desde un teléfono no lo instala en tu computadora ni lo habilita en todas las modalidades de ChatGPT.

La skill utiliza las herramientas que estén disponibles en esa sesión. Python es necesario para los helpers incluidos; las tareas del proyecto pueden necesitar Node, Git u otro runtime. No se necesita una clave de API para leer estas instrucciones ni se incluye ninguna.

## Obtener desde GitHub

El [repositorio público](https://github.com/Alanmezaoficial/armalo) incluye ambas ediciones. Si tienes Git, puedes obtenerlo en una carpeta nueva:

```text
git clone https://github.com/Alanmezaoficial/armalo.git
cd armalo
```

También puedes descargar el ZIP desde **Code → Download ZIP** en GitHub. Antes de copiar, abre la raíz que contiene `claude/` y `codex/`.

## Instala una copia con nombre propio

Descomprime el repositorio preparado. Abre PowerShell en su raíz, donde están `claude/` y `codex/`. Este comando copia únicamente la skill nueva y se detiene si ya existe ese destino:

```powershell
$source = (Resolve-Path '.\codex\skills\armalo').Path
$destination = Join-Path $env:USERPROFILE '.agents\skills\armalo'
if (Test-Path -LiteralPath $destination) { throw 'El destino ya existe; revisa su versión antes de actualizar.' }
New-Item -ItemType Directory -Path (Split-Path -Parent $destination) -Force | Out-Null
Copy-Item -LiteralPath $source -Destination $destination -Recurse
```

Si descargaste el ZIP de la edición Codex en lugar del repositorio completo, su carpeta superior ya se llama `armalo`: copia esa carpeta completa a `.agents/skills` de tu usuario. Deben quedar `SKILL.md`, sus recursos y `agents/openai.yaml` dentro de ella. Conserva `LICENSE` y `NOTICE`. Las instalaciones anteriores con otros nombres pueden seguir presentes.

## Verifica antes de encargar trabajo

Comprueba que existe `$env:USERPROFILE\.agents\skills\armalo\SKILL.md`. Inicia una sesión nueva de Codex y selecciona la skill; en CLI/extensión puedes escribir `$armalo` o abrir `/skills`. Si no aparece, reinicia el host y revisa la carpeta: no debe haber un nivel adicional `armalo/armalo`.

La presencia del archivo comprueba la copia; verla en el selector comprueba descubrimiento; completar un encargo comprueba ese recorrido. Son verificaciones distintas. Nuestro registro separa extracción/copia verificadas de la activación en una sesión nueva, que queda pendiente si el host no se probó.

## El primer encargo: una idea con un límite claro

Puedes empezar con algo pequeño: organizar tus clips, preparar una portada o documentar una aplicación que ya tienes. Explica qué quieres conseguir, quién lo usará y dónde trabajas. No necesitas elegir todas las tecnologías antes de comenzar.

```text
$armalo Quiero una herramienta local para ordenar mis clips por proyecto. La usaré yo en Windows. Primero ayúdame a definir el alcance y el plano; la construcción vendrá después.
```

Ármalo pregunta, propone una arquitectura y espera tu confirmación antes de generar el plano. Rápido reduce la entrevista; mantiene esa confirmación. La salida puede ser un Markdown compacto o un bundle con `blueprint.md`, tareas, épicas e instrucciones de trabajo. El documento no es una aplicación construida.

## Elige el recorrido que corresponde

| Recorrido | Cuándo sirve | Activación lista para adaptar |
|---|---|---|
| Ármalo | Una idea nueva con decisiones por resolver | `$armalo Quiero planear una herramienta para organizar mis clips.` |
| Ármalo rápido | Ya sabes qué quieres, quién lo usa y tus límites técnicos | `$armalo rápido: Una portada local de portafolio, para mostrar mis videos.` |
| Ármalo sobre lo existente | Ya hay código y quieres un cambio concreto | `$armalo sobre lo existente: Añade un buscador a este proyecto conservando las rutas y su diseño.` |
| Ármalo: siguiente tarea | Tienes un bundle y quieres retomarlo | `$armalo siguiente tarea en blueprints/mi-proyecto --listar` |
| Ármalo: actualiza versiones | El diseño sigue siendo válido, pero sus versiones requieren revisión | `$armalo actualiza versiones de blueprints/mi-proyecto` |
| Ármalo: revisa el plano | Quieres comprobar contratos, tareas y verificaciones sin editar | `$armalo revisa el plano en blueprints/mi-proyecto` |

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
