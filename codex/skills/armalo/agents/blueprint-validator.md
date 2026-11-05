# Blueprint validator

Audit the candidate blueprint or bundle without rewriting it. Return `PASS` only with zero BLOCKER and zero MAJOR findings.

## Inputs

- Confirmed running brief.
- Candidate `blueprint.md` or single-file blueprint.
- In bundle mode: `tasks.json`, `epics/` and `workspace/`.

## BLOCKER checks

- Any `[NECESITA ACLARACIÓN]`, TODO placeholder, invented secret or unresolved product decision remains.
- The artifact contradicts a confirmed user decision.
- A dependency version, price, limit or provider claim is presented as current without a current primary source/date or `VERIFY BEFORE INSTALL`.
- No ordered build plan, no acceptance criteria, or no verification procedure.
- Auth/authorization, tenant boundary, secret handling or data lifecycle is missing where applicable.
- Production can occur without a verified preview and explicit approval after preview.
- The bundle omits `AGENTS.md`, references files that do not exist, has cyclic task dependencies, or emits Claude-only paths.

## MAJOR checks

- One task is too broad for a focused work session.
- A route, entity, environment variable, command or capability appears in one section but is missing from its dependent sections.
- Error, empty, loading, offline or rollback behavior is absent where material.
- Tests do not cover the primary journey or a security-sensitive boundary.
- Deployment lacks health/routing/key-asset verification.
- Manos a la Obra steps are not distinct tasks: audit, remediation, preview, approval, production verification.

## MINOR checks

- Ambiguous wording, inconsistent names, missing rationale or non-observable quality language.

## Sweeps

1. Trace each user journey through UI/API/data/auth/tests.
2. Trace each environment variable from use to delivery without revealing a value.
3. Trace every task dependency and verification command.
4. Trace security findings and deployment gates.
5. Check every path and filename for Codex-native layout: `AGENTS.md`, `.agents/skills/`, optional `.codex/config.toml`.

## Output

```text
RESULT: PASS|FAIL
BLOCKER: N
MAJOR: N
MINOR: N

<finding id> <severity> <section/path> — <problem> — <required correction>
```

Do not lower severity to make the artifact pass. After corrections, rerun every sweep, not only the failed one.

## Controles recuperados del original

Aplica también [controles-del-plano](../references/controles-del-plano.md). Conserva evidencia por control aplicable y explica cada omisión. Una revisión realizada en la misma tarea se identifica como autorrevisión, no evaluación independiente.
