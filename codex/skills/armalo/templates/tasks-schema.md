# tasks.json contract

Bundle mode uses a JSON object with a version and ordered task array:

```json
{
  "schema_version": 1,
  "project": "project-slug",
  "blueprint": "./blueprint.md",
  "tasks": [
    {
      "id": "T-001",
      "epic": "E-01",
      "title": "Focused task title",
      "status": "pending",
      "depends_on": [],
      "inputs": ["blueprint.md#section"],
      "changes": ["path/or/component"],
      "acceptance": [
        "WHEN <trigger> THE SYSTEM SHALL <observable response>"
      ],
      "verify": ["command that exits 0"],
      "risk": "low|medium|high",
      "external_mutation": false
    }
  ]
}
```

Rules:

- IDs are stable and unique; dependencies reference earlier valid IDs and contain no cycles.
- A task fits one focused work session and has at least one acceptance criterion and verification.
- Commands must be valid for the selected platform and package manager.
- Security audit, remediation, preview, explicit production approval and post-deploy verification are distinct tasks.
- The production task sets `external_mutation: true` and depends on a verified preview plus the user approval gate.
- Do not embed secrets or unresolved product decisions.
