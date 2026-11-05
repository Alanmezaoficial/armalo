# Controles del plano recuperados para Codex

Adaptación de los propósitos del validador original, conservando las convenciones de la adaptación instalada. Revisa cada control aplicable y ubica la evidencia. No obligues al proyecto a añadir infraestructura solo para satisfacer una plantilla.

1. Cada tarea tiene criterios observables y verificación; no basta decir funciona o está implementado.
2. Los criterios se comprueban con el medio adecuado: tipos en typecheck, interfaz en navegador, I/O ejecutándolo.
3. No quedan decisiones de producto abiertas, marcadores ni secretos inventados.
4. La propuesta conserva decisiones confirmadas y limita el alcance de cada tarea.
5. Cada variable tiene dueño, entorno, mecanismo de carga y entrega documentados sin valores.
6. Todo archivo nombrado por un verify lo crea esa tarea, una anterior o el workspace emitido.
7. Las rutas, entidades, eventos, puertos y nombres compartidos concuerdan entre archivos.
8. No se inventa el nombre exacto de un archivo que el generador nombra dinámicamente.
9. Los pins tienen procedencia y fecha; su versión no contradice peers ni estado prerelease.
10. Cada dependencia fijada se instala en un paso o bootstrap identificado.
11. Un servicio requerido por pruebas se provisiona localmente o queda como requisito explícito pendiente.
12. Un cambio en el paso N no rompe silenciosamente el verify de los anteriores.
13. Los pasos son sesiones acotadas y sus criterios no esperan una aprobación externa para declarar construcción comprobada.
14. Las aprobaciones, DNS y publicación siguen como puertas humanas separadas, nunca se inventa su cumplimiento.
15. El orden respeta dependencias; no hay IDs duplicados, ausentes ni ciclos.
16. tasks.json y épicas coinciden en criterios, archivos y todos los comandos verify.
17. El plano conserva todas las secciones que su plantilla requiere; no aplicable tiene motivo.
18. Las exclusiones del alcance están explícitas y no contradicen ejemplos o bootstrap.
19. El workspace conserva instrucciones existentes y usa AGENTS.md y rutas nativas de Codex.
20. Las herramientas o skills recomendadas existen en el entorno o tienen una alternativa honesta.
21. No se exige una allowlist de Claude para ejecutar Codex ni se afirma que frontmatter registre sus subagentes.
22. La configuración emitida es válida y el linter/formatter cubre o excluye conscientemente el bundle.
23. Los loaders de aplicación, pruebas, scripts y build resuelven imports, aliases y condiciones de exportación.
24. Los comandos que leen variables las cargan realmente; no dependen de que el framework las cargue por otro proceso.
25. Las cifras y conteos de criterios coinciden con el contenido literal del propio plano.
26. Un checkpoint que use Git requiere repo/commit existentes; no se inicializa ni se hace reset destructivo por defecto.
27. Los ignore no excluyen archivos que se declara que deben estar versionados o presentes en el build.
28. La entrada se ejecuta cuando la prueba lo exige; compilar un binario no demuestra que arranque.
29. El bootstrap puede repetirse sin fallar ni borrar cambios; el camino no-op devuelve éxito.
30. Verify no depende de un commit o tag que ese mismo paso todavía no creó.
31. Las expectativas literales no contradicen datos ni afirman errores exactos de runtimes no probados.
32. Una prueba de fallo esperado reconoce el código o condición esperada; cualquier error no cuenta como éxito.
33. Los archivos de configuración e ignore se crean antes de los comandos que gobiernan.
34. No se obtiene un contrato de una sección vacía o marcada no aplicable.
35. Brownfield incluye mapa del repo, invariantes, delta concreto y pruebas existentes.
36. Una migración exige paridad observable, harness, coexistencia, secuencia de cambio, criterio de reversión y retirada posterior.
37. Auth, aislamiento, ciclo de datos, errores y recuperación se especifican solo cuando aplican.
38. Auditoría, corrección, preview, autorización y verificación de producción no se colapsan en un paso implícito.
39. Los recursos propios se escriben en el workspace autorizado, nunca en la instalación de la skill.
40. La evidencia distingue lectura, sintaxis, instalación, ejecución, dispositivo y servicios realmente probados.
