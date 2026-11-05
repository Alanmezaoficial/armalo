# Blueprint writer

Compose the confirmed architecture into one internally consistent artifact. One writer owns all generated files.

Read [the blueprint template](../templates/blueprint-template.md), [AGENTS template](../templates/agents-md-template.md), and in bundle mode [tasks schema](../templates/tasks-schema.md) plus [epic template](../templates/epic-template.md).

Inputs must include the confirmed running brief, chosen shape/runtime/capabilities, verified version report, output mode and destination path. Refuse to invent missing decisions; return the exact gap instead.

Requirements:

- Fill all 20 blueprint sections with concrete project-specific content.
- Preserve confirmed scope and exclusions.
- Use one stack choice per layer with rationale and current verification evidence.
- Keep routes, data model, env vars, tests and tasks cross-consistent.
- Write observable acceptance criteria and executable verification.
- Generate Codex-native `AGENTS.md`; never emit `CLAUDE.md` or `.claude/`.
- Include distinct Chécalo and Súbelo gates.
- Write only under the requested `./blueprints/` destination.

Return paths, task count, assumptions, verification flags and any gap that prevented completion. The validator is the final gate.
