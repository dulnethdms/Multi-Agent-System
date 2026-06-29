# AGENTS.md

## Project context
This repository appears to be a new multi-agent system project with a Zoom-oriented focus. Keep changes lightweight, well-scoped, and easy for future agents to understand.

## Working conventions
- Prefer small, composable changes over large rewrites.
- Keep agent responsibilities clearly separated and documented.
- Favor configuration over hard-coded behavior, especially for external services.
- Do not commit secrets or credentials. Use environment variables and keep examples safe.

## Zoom-specific guidance
- If implementing Zoom-related functionality, treat Zoom API access, auth, and webhook handling as integration boundaries.
- Keep Zoom configuration in environment variables such as client IDs, secrets, webhook tokens, and base URLs.
- When adding agent workflows, make the data flow explicit: input -> agent reasoning -> tool/action -> result.
- Prefer resilient error handling for network calls, retries, and missing configuration.

## Development expectations
- Preserve existing project structure when files already exist; otherwise keep new code organized and easy to navigate.
- When adding documentation or instructions, keep them concise and actionable.
- If a feature touches multiple agents or services, explain the handoff points clearly.

## Notes for agents
- If a task involves Zoom integration, verify whether the change affects authentication, event handling, persistence, or observability.
- Avoid introducing unnecessary dependencies or framework churn unless the task explicitly requires it.
