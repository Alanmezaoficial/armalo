# Brownfield mode

Use when the user points at an existing repository or asks to add a substantial capability.

## Phase 0: repository map

Read all applicable `AGENTS.md` instructions, inspect Git status without changing it, and map:

- runtimes, package managers and commands;
- entry points, routes, modules and data stores;
- auth/authorization and tenant boundaries;
- tests, CI/CD, deploy configuration and observability;
- existing conventions and uncommitted user changes.

Existing repository conventions and working code outrank template defaults.

## Interview

Ask at most three questions per message. Establish the requested outcome, users, compatibility constraints, migration/cutover needs and definition of done. Do not redesign unrelated areas.

## Architecture card

Present one recommended change design: affected components, data/API changes, migration and rollback, tests, security impact, deployment phases and explicit non-goals. Require confirmation and zero unresolved markers.

For migrations, define parity evidence, dual-read/write or staged cutover when needed, and a tested rollback. Never propose a flag-day rewrite without an explicit requirement and justification.

## Generation

Return to the Architect `GENERATE` phase. The bundle must distinguish existing paths from new paths, preserve user changes, and schedule the smallest safe sequence. Include `$checalo` for the changed security boundaries and `$subelo` preview before production.
