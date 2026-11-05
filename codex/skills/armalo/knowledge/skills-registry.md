# Codex skill routing

Do not hardcode availability. Inspect the skills and tools exposed in the current task, then recommend only relevant ones. If a named workflow is unavailable, complete the underlying work with native tools or say what remains unavailable.

## Manos a la Obra

- `$armalo`: architecture and blueprint before implementation.
- `$checalo`: read-only defensive audit before production.
- `$subelo`: local/preview/production workflow with explicit production approval.

## Common Codex capabilities

- Use the official OpenAI documentation skill for OpenAI models, APIs, pricing and Codex configuration.
- Use browser or Chrome control for reference-site inspection and real preview validation when available.
- Use Sites building/hosting when the project contains `.openai/hosting.json` or the user chooses Sites.
- Use image generation for raster assets; use repo-native code/SVG for code-native visuals.
- Use document, PDF, presentation and spreadsheet skills only when those artifact types are in scope.
- Use the payment integration skill when the project needs a new supported checkout flow.
- Use plugin management only when an external service would materially help and no native tool already covers it.

## Blueprint rule

Mention a skill in the blueprint only when it changes a concrete build or validation step. Give the fallback behavior and never make an optional third-party skill a prerequisite for completing the project.
