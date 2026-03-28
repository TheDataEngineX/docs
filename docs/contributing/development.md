---
title: Development Setup
description: Set up your development environment for DataEngineX
---

# Development Setup

## Prerequisites

- Python 3.13+
- [uv](https://docs.astral.sh/uv/)
- Git

## Clone and Install

```bash
git clone https://github.com/TheDataEngineX/DEX.git
cd DEX
uv sync
```

## Quality Commands

```bash
uv run poe lint          # Ruff lint
uv run poe typecheck     # mypy --strict
uv run poe test          # pytest
uv run poe check-all     # all of the above
```

## Branch Convention

- `feature/<desc>` or `fix/<desc>` — never commit directly to `dev` or `main`
- Flow: feature branch → PR to `dev` → PR `dev` to `main`

## Conventional Commits

| Type | Bump | Use for |
|------|------|---------|
| `feat:` | minor | New feature |
| `fix:` | patch | Bug fix |
| `feat!:` | major | Breaking change |
| `chore:`, `refactor:`, `test:`, `ci:`, `docs:` | none | No release |
