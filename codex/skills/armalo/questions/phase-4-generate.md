# Phase 4 — Generate for Codex

Enter only after the user explicitly confirms the architecture and no `[NECESITA ACLARACIÓN]` marker remains.

## Procedure

1. Tell the user that generation and validation may take a few minutes.
2. Re-verify every version, compatibility claim, price, limit and provider capability against a current primary source. Record source and date. If a pin cannot be verified, mark `VERIFY BEFORE INSTALL` instead of guessing.
3. Derive and announce bundle mode for 12+ tasks or work that needs resumability; a compact spec can use one Markdown file. Respect an explicit user format choice; do not re-ask settled preferences.
4. Build from the confirmed running brief and [templates/blueprint-template.md](../templates/blueprint-template.md). Do not reopen settled product decisions.
5. In bundle mode write exactly:

```text
./blueprints/<project-slug>/
├── blueprint.md
├── tasks.json
├── epics/
│   └── NN-<epic>.md
└── workspace/
    ├── AGENTS.md
    ├── .agents/
    │   └── skills/<project-skill>/SKILL.md   # only when project-specific reuse helps
    └── .codex/config.toml                    # only when the project needs explicit Codex settings
```

Use [templates/agents-md-template.md](../templates/agents-md-template.md), [templates/tasks-schema.md](../templates/tasks-schema.md) and [templates/epic-template.md](../templates/epic-template.md). Do not create `CLAUDE.md`, `.claude/`, deprecated custom prompts or imaginary Codex commands.

6. In single-file mode include complete `AGENTS.md` and task content in fenced sections inside the blueprint; do not create `tasks.json` or `epics/`.
7. Make every task fit one focused work session. Each task must state inputs, files or components, dependencies, an observable acceptance criterion in the form `WHEN <trigger> THE SYSTEM SHALL <response>`, and a verification command or procedure.
8. Include the Manos a la Obra gates in both blueprint and tasks:
   - implementation and tests;
   - `$checalo` audit;
   - remediation and recheck of Critical/High findings;
   - `$subelo` preview;
   - explicit user approval after preview;
   - production and post-deploy routing verification.
9. Validate with [agents/blueprint-validator.md](../agents/blueprint-validator.md). Iterate until zero `BLOCKER` and zero `MAJOR`. Do not hand over a failing artifact.
10. Report the absolute output path, stack summary, task count, first task id, current verification flags and the next action from the target project root.

## Path rule

All output belongs in the user's active workspace under `./blueprints/`. Supporting files in this skill are read-only sources. Never write generated projects into the installed skill or plugin directory.

## Comprobación adicional

Aplica [references/controles-del-plano.md](../references/controles-del-plano.md). Prueba bootstrap, segunda ejecución, entrada y capa de datos en un directorio temporal solo cuando corresponda al alcance y estén disponibles sus requisitos. Nunca instales en el proyecto objetivo ni crees credenciales para simular un PASS. Registra por separado revisión estática y prueba ejecutada.
