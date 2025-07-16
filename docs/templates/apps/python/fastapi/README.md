# Python FastAPI

High-performance Python web API with FastAPI framework

## Overview

- **Category**: App
- **Version**: 1.0.0
- **Author**: Container Template Engine
- **License**: MIT
- **Tags**: python, fastapi, web, api, async

## Quick Start

### Generate from Template

```bash
# Basic usage
poetry run template-engine generate apps/python/fastapi ./my-Python FastAPI

# With custom parameters
poetry run template-engine generate apps/python/fastapi ./my-Python FastAPI \
  --param param_name=value \
  --param another_param=value

# Using parameter file
poetry run template-engine generate apps/python/fastapi ./my-Python FastAPI \
  --params params.json
```

### Using Docker Compose

```bash
cd my-Python FastAPI
docker-compose up -d
```

### Manual Docker Build

```bash
cd my-Python FastAPI
docker build -t my-Python FastAPI:latest .
docker run -d --name my-Python FastAPI my-Python FastAPI:latest
```

## Parameters

### Required Parameters

- `app_name` (string): Application name (default: `fastapi-app`)

### Optional Parameters

- `alpine_version` (string): Alpine Linux version (default: `3.20`)
- `packages` (array): Additional packages to install (default: `['curl', 'wget', 'ca-certificates']`)
- `user_name` (string): Non-root user name (default: `appuser`)
- `user_uid` (integer): User UID (default: `1000`)
- `timezone` (string): System timezone (default: `UTC`)
- `enable_security_updates` (boolean): Enable automatic security updates (default: `True`)
- `python_version` (string): Python version (default: `3.11`)
- `port` (integer): Application port (default: `8000`)
- `debug` (boolean): Enable debug mode (default: `False`)
- `cors_origins` (array): CORS allowed origins (default: `['http://localhost:3000']`)
- `database_url` (string): Database connection URL (default: `sqlite:///./app.db`)
- `secret_key` (string): Application secret key (default: `{{ random_string(32) }}`)
- `enable_docs` (boolean): Enable API documentation (default: `True`)
- `workers` (integer): Number of worker processes (default: `1`)

[📋 **Full Parameter Reference**](PARAMETERS.md)

## Generated Files

This template generates the following files:

### Dockerfile

- `Dockerfile`

### Compose

- `docker-compose.yml`

### Config

- `requirements.txt`
- `app.py`
- `config.py`

### Docs

- `README.md`
- `api_docs.md`

### Scripts

- `entrypoint.sh`
- `healthcheck.py`

### Tests

- `test_app.py`

## Examples

[📖 **Usage Examples**](EXAMPLES.md)

## Troubleshooting

[🔧 **Troubleshooting Guide**](TROUBLESHOOTING.md)

## Dependencies

### Build

- python:{{ python_version }}-alpine
- gcc
- musl-dev
- postgresql-dev

### Runtime

- fastapi[all]
- uvicorn[standard]
- sqlalchemy
- asyncpg
- alembic
- pydantic-settings

### Test

- pytest
- pytest-asyncio
- httpx

## Supported Platforms

linux/amd64, linux/arm64

## Testing

This template includes comprehensive testing:

### Test Commands

- `python -m pytest tests/ -v`
- `python -c 'import app; print("App imports successfully")'`

## Contributing

To modify this template:

1. Edit the template files in `templates/apps/python/fastapi/`
2. Update `template.yaml` for parameter changes
3. Test your changes: `poetry run template-engine test apps/python/fastapi`
4. Regenerate documentation: `poetry run generate-docs`

## Related Templates

Browse other templates in the same category: [**App Templates**](../app/README.md)

---

_Documentation generated automatically from template metadata_
_Last updated: 2025-07-15 21:54:36_
