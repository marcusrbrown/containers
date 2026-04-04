# templates/AGENTS.md

Container templates for generating Dockerfiles across categories. **This entire directory is excluded from linting, formatting, CI detection, yamllint, prettier, and dockerfilelint.**

## Structure

```
templates/
├── apps/              # Application containers (Flask, FastAPI, Django, etc.)
├── base/              # Base images (Ubuntu, Alpine, etc.)
├── databases/         # Database containers (PostgreSQL, Redis, MongoDB, etc.)
├── infrastructure/    # Infra containers (Nginx, Traefik, etc.)
├── microservices/     # Microservice containers (API gateways, workers, etc.)
└── <category>/
    └── <template>/
        ├── template.yaml    # Template metadata + configuration
        ├── Dockerfile.j2    # Jinja2 Dockerfile template
        └── ...              # Supporting files (configs, scripts)
```

## Template Configuration (`template.yaml`)

Each template has a `template.yaml` with metadata:

```yaml
name: flask-app
category: apps
description: Production Flask application
base_image: python:3.13-slim
architectures:
  - linux/amd64
  - linux/arm64
packages:
  - curl
  - build-essential
env_vars:
  FLASK_ENV: production
health_check:
  endpoint: /health
  interval: 30s
```

## Jinja2 Templates (`Dockerfile.j2`)

Templates use Jinja2 syntax with variables from `template.yaml`:

```dockerfile
from {{ base_image }}

{% if packages %}
run apt-get update && apt-get install -y {{ packages | join(' ') }} && rm -rf /var/lib/apt/lists/*
{% endif %}
```

Note: lowercase Dockerfile instructions per project convention.

## Key Scripts (in `scripts/`)

| Script | Purpose |
|--------|---------|
| `template_engine.py` | Renders Jinja2 templates into Dockerfiles |
| `template_testing.py` | Validates templates build and pass health checks |
| `template_documentation.py` | Generates docs from template metadata |
| `template_intelligence.py` | AI-powered template recommendations |

## Anti-Patterns

- Do NOT run linters against this directory — it's intentionally excluded from all tooling
- Do NOT add this directory to CI path triggers
- Do NOT use uppercase Dockerfile instructions in `.j2` templates — follow project convention
- Do NOT hardcode architecture — use `template.yaml` to declare supported platforms
