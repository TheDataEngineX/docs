---
title: Quickstart
description: Run your first DataEngineX pipeline in 5 minutes
---

# Quickstart

## 1. Create a config file

Create `dex.yaml`:

```yaml
project:
  name: my-first-pipeline
  version: "0.1.0"

api:
  enabled: true
  host: "0.0.0.0"
  port: 17000
```

## 2. Validate the config

```bash
dex validate dex.yaml
```

## 3. Start the server

```bash
dex run dex.yaml
```

## 4. Test it

```bash
curl http://localhost:17000/health
```

## Next Steps

- [Architecture](../framework/architecture.md) — Understand the core patterns
- [API Reference](../api-reference/) — Explore the Python API
