# AGENTS.md template

Generate one project-specific file. Keep it concise enough to load on every Codex task.

```md
# {Project name}

## Purpose

{One paragraph: product, users, outcome and current phase.}

## Source of truth

- Architecture and scope: `{relative blueprint path}`
- Task order: `{relative tasks.json path}`
- Existing code and repository conventions override blueprint defaults when they conflict.

## Setup and commands

- Install: `{command}`
- Develop: `{command}`
- Test: `{command}`
- Lint/typecheck: `{command}`
- Build: `{command}`

## Working agreements

- Preserve user changes and inspect the worktree before editing.
- Implement one unblocked task at a time and verify its acceptance criteria.
- Do not invent dependency versions, provider behavior or environment values.
- Never place secrets in source, logs, fixtures, reports or commits.
- Ask before adding a production dependency or performing an external production mutation.

## Architecture invariants

- {Boundary or data-flow rule}
- {Auth/tenant rule}
- {Error and observability rule}

## Manos a la Obra release gates

- Run `$checalo` before the first production release and after substantial security-sensitive changes.
- Resolve or explicitly accept Critical/High findings before production.
- Use `$subelo` to produce and verify a preview.
- Production requires explicit approval after the preview is reviewed.

## Definition of done

- Acceptance criterion is observable.
- Relevant tests pass.
- Documentation/configuration changes are included.
- Verification evidence is reported separately for build, HTTP preview and production.
```

Do not duplicate generic Codex system rules. Include only conventions that change decisions for this project.
