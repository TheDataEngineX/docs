---
title: Contributing
description: How to contribute to DataEngineX
---

# Contributing to DataEngineX

We welcome contributions to any part of the DataEngineX ecosystem.

## Repos

| Repo | What to contribute |
|------|-------------------|
| [DEX](https://github.com/TheDataEngineX/DEX) | Core framework, backends, CLI |
| [dex-studio](https://github.com/TheDataEngineX/dex-studio) | Web UI pages, components |
| [infradex](https://github.com/TheDataEngineX/infradex) | Helm charts, Terraform modules |
| [docs](https://github.com/TheDataEngineX/docs) | Documentation improvements |

## Workflow

1. Fork the repo
2. Create a feature branch: `feature/<desc>`
3. Make changes with tests
4. Open a PR to `dev`

## Standards

- `from __future__ import annotations` — first import in every Python file
- Type hints on all public functions (`mypy --strict`)
- No `print()` — use `structlog`
- Tests required for all new code (80%+ coverage)

See [Development](development.md) for tooling setup.
