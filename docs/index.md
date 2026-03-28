---
title: DataEngineX Documentation
description: Unified Data + ML + AI framework — config-driven, self-hosted, production-ready
---

# DataEngineX

Unified **Data + ML + AI** framework. Config-driven, self-hosted, production-ready.

Define your entire data pipeline, ML lifecycle, and AI agents in a single `dex.yaml` config file.

## Quick Links

- **[Getting Started](getting-started/)** — Install and run in 5 minutes
- **[Framework](framework/architecture.md)** — Core architecture and patterns
- **[API Reference](api-reference/)** — Python API autodoc
- **[Studio](studio/)** — Web UI for the DataEngineX platform
- **[Deploy](deploy/deploy-runbook.md)** — Kubernetes deployment guide
- **[Contributing](contributing/)** — How to contribute

## Ecosystem

| Component | Description |
|-----------|-------------|
| **[dataenginex](https://pypi.org/project/dataenginex/)** | Core framework — config, registry, CLI, API, ML, AI |
| **[dex-studio](https://github.com/TheDataEngineX/dex-studio)** | Web UI — single pane of glass (NiceGUI) |
| **[infradex](https://github.com/TheDataEngineX/infradex)** | K3s / Helm / Terraform infrastructure |

## Install

```bash
pip install dataenginex
```

Or with extras:

```bash
pip install "dataenginex[spark,mlflow,agents]"
```
