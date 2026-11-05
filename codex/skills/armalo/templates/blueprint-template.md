# Blueprint: {Project name}

> Status: confirmed architecture. Generated {date}. Versions verified {date and sources}. Any unresolved pin is marked `VERIFY BEFORE INSTALL`.

## 1. Executive summary

{What is being built, for whom, the outcome, and the recommended approach.}

## 2. Goals and success metrics

- Goal: {measurable outcome}
- Metric and target: {metric}
- Non-goal: {explicit exclusion}

## 3. Users and primary journeys

| User | Need | Happy path | Failure/empty state |
|---|---|---|---|
| {persona} | {need} | {steps} | {behavior} |

## 4. Scope

### Included in v1

{Bullets}

### Excluded from v1

{Bullets with rationale}

## 5. Verified stack

| Layer | Choice | Version | Reason | Verification source/date |
|---|---|---|---|---|
| Runtime | {choice} | {pin} | {reason} | {source} |

List known compatibility constraints and all `VERIFY BEFORE INSTALL` flags.

## 6. System architecture

{Components, trust boundaries, request/data flow, sync and async paths, third parties, and failure handling.}

## 7. Data model and lifecycle

| Entity | Purpose | Key fields | Owner/tenant rule | Retention |
|---|---|---|---|---|
| {entity} | {purpose} | {fields} | {rule} | {policy} |

Include migrations, indexing, backups, deletion and seed strategy.

## 8. Interfaces, routes and contracts

| Surface | Method/route/event | Auth | Input | Output/error |
|---|---|---|---|---|
| {surface} | {contract} | {rule} | {schema} | {schema} |

## 9. Repository structure

```text
{complete proposed tree with responsibilities}
```

## 10. Numbered build order

For every step include dependencies, files/components, acceptance criteria and verification.

### Step {N}: {title}

- Depends on: {ids or none}
- Changes: {paths/components}
- Acceptance: WHEN {trigger} THE SYSTEM SHALL {observable response}.
- Verify: `{command that exits 0}` or {manual procedure}
- Rollback/recovery: {when material}

## 11. Product and visual system

{Information architecture, responsive layout, tokens, typography, components, interaction, loading, empty/error states and accessibility.}

## 12. Identity, authorization and security

{Auth flow, session storage, role/tenant matrix, input validation, secret handling, abuse controls, headers, data protection and threat assumptions.}

## 13. Optional capabilities

{Payments, AI, media, collaboration, offline, notifications or other selected capabilities. Include provider-specific failure and cost controls.}

## 14. Configuration and environments

| Variable | Required in | Secret | Source | Validation |
|---|---|---|---|---|
| `{NAME}` | {local/preview/prod} | {yes/no} | {owner/provider} | {check} |

Never include secret values. Define local, test, preview and production differences.

## 15. Test and quality strategy

{Unit, integration, E2E, accessibility, security and performance coverage; fixtures; CI commands; release gates.}

## 16. Observability and operations

{Structured logs, metrics, traces, alerts, SLOs, dashboards, runbooks, backup/restore and incident owner.}

## 17. Deployment and release

{Chosen provider and rationale, build/start commands, health route, env delivery, preview flow, production gate, domain/routing checks and documented rollback.}

Production must require a preview of the same source plus explicit approval after review.

## 18. Risks, decisions and assumptions

| Item | Type | Impact | Mitigation/owner |
|---|---|---|---|
| {item} | risk/decision/assumption | {impact} | {action} |

No unresolved marker may remain in a final blueprint.

## 19. Codex workspace contract

Include the complete contents of the target project's `AGENTS.md` using [agents-md-template.md](agents-md-template.md). Add repo-local `.agents/skills/` only for genuinely project-specific reusable workflows. Add `.codex/config.toml` only when a documented setting is needed.

## 20. Manos a la Obra handoff and definition of done

The project is ready only when:

- build, lint/typecheck and tests are separately recorded;
- `$checalo` has no unaccepted Critical/High findings;
- `$subelo` preview is reachable and visually/behaviorally checked;
- the user approves that exact preview for production;
- production URL, redirects, health route and key assets are verified.

List the first task id, dependency order and any `VERIFY BEFORE INSTALL` flags.
