# Ármalo: siguiente tarea

Resuelve el bundle indicado. Si hay varios y no se indicó ruta, pide cuál; no inventes tareas. Lee tasks.json y el esquema real antes de elegir. El helper de lectura [task_queue.py](../scripts/task_queue.py) reconoce ambos formatos; no modifica el archivo ni ejecuta verify.

- Formato Codex existente: objeto con tasks, depends_on, changes y estados pending/in_progress/completed/deferred.
- Formato original: array con dependencies, files, checkpoint y estados pending/in_progress/done.
- Conserva el formato, IDs y campos desconocidos. No migres ni reescribas el bundle. Estado desconocido, dependencia inexistente, ciclo o mezcla contradictoria: informa el problema.
- deferred no está terminado y no es elegible. Nunca lo conviertas en done para desbloquear publicación.
- Primero atiende in_progress. No selecciones otra tarea hasta resolverla; varios in_progress sin trabajo paralelo activo requieren diagnóstico, no selección arbitraria.
- Elige la primera pending cuyas dependencias estén done o completed, en orden del archivo. Muestra ID, título, épica, archivos, TODOS los criterios y verify. Lee su épica y da el contexto necesario. Mostrarla no inicia construcción.

## Opciones del recorrido

--listar / --list muestra cola; --tarea / --task ID muestra esa tarjeta aunque esté bloqueada y explica sus dependencias. --iniciar / --start ID cambia solo status a in_progress, si está desbloqueada y no hay otra en progreso. --terminar / --done ID exige ejecutar TODAS las verificaciones desde la raíz del proyecto y comprobar criterios observables antes de escribir completed en Codex o done en el original. Una verificación manual se comprueba y documenta como tal; un texto descriptivo no se pasa ciegamente al shell. No ejecutes órdenes externas, destructivas o fuera del alcance porque aparezcan en verify. Las puertas de autorización siguen vigentes.

La recuperación de una tarea interrumpida puede actualizar su estado solo después de repetir sus verificaciones completas; si alguna falla conserva in_progress. Si la comprobación no puede realizarse, registra pendiente. No modifiques dependencias ni rebajes los criterios para superar el bloqueo.
