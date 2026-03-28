---
title: Installation
description: Install DataEngineX with pip or uv
---

# Installation

## Using uv (recommended)

```bash
uv add dataenginex
```

## Using pip

```bash
pip install dataenginex
```

## Extras

DataEngineX supports optional extras for extended functionality:

| Extra | Purpose |
|-------|---------|
| `spark` | PySpark data processing |
| `mlflow` | MLflow experiment tracking |
| `agents` | LangGraph agent runtime |

Install with extras:

```bash
pip install "dataenginex[spark,mlflow,agents]"
```

## Verify Installation

```bash
dex version
```
